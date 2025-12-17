from pathlib import Path
from dataclasses import dataclass
import re
import frontmatter
from markdown import markdown
from bs4 import BeautifulSoup
from openai import OpenAI
import polib
from datetime import datetime, timezone
import argparse


@dataclass
class Node:
    tag: str
    type: str
    text: str
    raw: str
    md_raw: str


class MarkdownParser:
    """封装的 Markdown 解析器：接受 Markdown 文本（string），返回 list[Node]."""

    def __init__(self, md_text: str):
        self.md_text = md_text
        self.parse_and_collect()
        self.nodes_from_elems()

    def parse_and_collect(self):
        # frontmatter
        fm = frontmatter.loads(self.md_text)
        # keep markdown body for md_raw extraction
        self.md_content = fm.content
        # build markdown blocks for ordered matching
        self.md_blocks = self._split_markdown_blocks(self.md_content)
        self._block_idx = 0
        self.elems = []
        if fm.metadata:
            # get raw frontmatter block from original text if present
            fm_raw = ""
            m = re.match(r"^---\s*\n(.*?\n)---\s*\n", self.md_text, re.S)
            if m:
                fm_raw = m.group(0).strip()
            else:
                fm_raw = "\n".join([f"{k}: {v}" for k, v in fm.metadata.items()])
            self.elems.append(("frontmatter", "frontmatter", fm_raw, fm_raw, fm_raw))

        # convert markdown body to HTML (preserve fenced code, tables, lists)
        html = markdown(fm.content, extensions=["fenced_code", "tables"])
        soup = BeautifulSoup(html, "html.parser")

        # iterate over top-level elements in order
        for node in soup.contents:
            if getattr(node, "name", None) is None:
                # text node (whitespace/newline)
                continue
            tag = node.name.lower()
            raw = str(node)
            text = node.get_text(" ", strip=True)
            md_raw = self._get_next_block_for(tag, text)
            if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
                level = int(tag[1])
                self.elems.append((tag, "heading", text, raw, md_raw))
            elif tag == "p":
                self.elems.append((tag, "paragraph", text, raw, md_raw))
            elif tag == "pre":
                # code block may be <pre><code>...</code></pre>
                code = node.get_text()
                self.elems.append(("pre", "code", code.rstrip("\n"), raw, md_raw))
            elif tag == "code":
                self.elems.append(("code", "code", text, raw, md_raw))
            elif tag == "table":
                self.elems.append(("table", "table", text, raw, md_raw))
            elif tag in ("ul", "ol"):
                lst_text = self.extract_list_html(node)
                self.elems.append((tag, "list", lst_text, raw, md_raw))
                # also include individual li items
                for li in node.find_all("li", recursive=False):
                    li_raw = str(li)
                    li_text = li.get_text(" ", strip=True)
                    li_md = self._get_next_block_for("li", li_text)
                    self.elems.append(("li", "list_item", li_text, li_raw, li_md))
            else:
                self.elems.append((tag, "paragraph", text, raw, md_raw))

    def nodes_from_elems(self):
        self.nodes = []
        for item in self.elems:
            if item[0] == "frontmatter":
                # item: ('frontmatter','frontmatter', fm_raw, fm_raw, fm_raw)
                self.nodes.append(
                    Node(
                        tag="frontmatter",
                        type="frontmatter",
                        text=item[2],
                        raw=item[3],
                        md_raw=item[4],
                    )
                )
                continue
            tag, typ, text, raw, md_raw = item
            self.nodes.append(
                Node(tag=tag, type=typ, text=text, raw=raw, md_raw=md_raw)
            )

    def _split_markdown_blocks(self, md: str):
        """将 Markdown 文本切分为有序块（代码围栏、标题、表格、列表、段落），返回块列表。"""
        blocks = []
        lines = md.splitlines()
        i = 0
        list_re = re.compile(r"^(\s*([-+*]|\d+\.)\s+).+")
        while i < len(lines):
            line = lines[i]
            if line.strip() == "":
                i += 1
                continue
            # fenced code
            if line.strip().startswith("```"):
                fence = line
                j = i + 1
                while j < len(lines) and not lines[j].strip().startswith("```"):
                    j += 1
                # include closing fence if exists
                if j < len(lines):
                    j += 1
                blocks.append("\n".join(lines[i:j]))
                i = j
                continue
            # heading
            if line.lstrip().startswith("#"):
                blocks.append(line)
                i += 1
                continue
            # table (contiguous lines with '|')
            if "|" in line:
                j = i
                tbl = []
                while j < len(lines) and "|" in lines[j]:
                    tbl.append(lines[j])
                    j += 1
                blocks.append("\n".join(tbl))
                i = j
                continue
            # list block
            if list_re.match(line):
                j = i
                lst = []
                while j < len(lines) and (
                    lines[j].strip() == ""
                    or list_re.match(lines[j])
                    or lines[j].startswith("  ")
                ):
                    if lines[j].strip() == "":
                        break
                    lst.append(lines[j])
                    j += 1
                blocks.append("\n".join(lst))
                i = j
                continue
            # paragraph: consecutive non-blank lines until blank
            j = i
            para = []
            while j < len(lines) and lines[j].strip() != "":
                para.append(lines[j])
                j += 1
            blocks.append("\n".join(para))
            i = j
        return blocks

    def _get_next_block_for(self, tag, text):
        """按顺序从 self.md_blocks 中查找最先匹配的块并返回，同时推进指针。"""

        # normalized compare helper
        def norm(s):
            return re.sub(r"\s+", " ", s).strip()

        target = norm(text)
        # try from current index to end
        for idx in range(self._block_idx, len(self.md_blocks)):
            blk = self.md_blocks[idx]
            if not blk:
                continue
            # render block to HTML then extract plain text for robust comparison
            try:
                blk_html = markdown(blk, extensions=["fenced_code", "tables"])
                blk_plain = BeautifulSoup(blk_html, "html.parser").get_text(
                    " ", strip=True
                )
            except Exception:
                blk_plain = norm(blk)

            nblk = norm(blk_plain)
            # exact or contains match using rendered plain text
            if target and target in nblk:
                self._block_idx = idx + 1
                return blk
            # for headings: match line starting with # and same text
            if tag.startswith("h"):
                # check original markdown heading text
                if blk.lstrip().startswith("#") and target == re.sub(
                    r"^#+\s*", "", norm(blk)
                ):
                    self._block_idx = idx + 1
                    return blk
            # for code blocks, check fenced code presence
            if tag in ("pre", "code"):
                if blk.strip().startswith("```"):
                    # check if code contains target first line
                    code_inner = re.sub(r"^```.*\n|\n```$", "", blk, flags=re.S)
                    if target.split(" ")[0] in norm(code_inner):
                        self._block_idx = idx + 1
                        return blk
            # for list items, check line-wise inclusion
            if tag in ("li", "ul", "ol"):
                lines = [l.strip() for l in blk.splitlines() if l.strip()]
                for l in lines:
                    # compare against rendered/plain line as well
                    if target in norm(l) or target in norm(
                        BeautifulSoup(markdown(l), "html.parser").get_text(
                            " ", strip=True
                        )
                    ):
                        self._block_idx = idx + 1
                        return blk
        # fallback: return empty and do not advance pointer
        return ""

    def extract_list_html(self, tag):
        # 将 ul/ol 转为缩进表示的多级列表文本
        def walk_list(node, depth=0):
            lines = []
            for child in node.children:
                if child.name in ("li",):
                    text_parts = []
                    for c in child.contents:
                        if getattr(c, "name", None) in ("ul", "ol"):
                            # nested list
                            pass
                        else:
                            text_parts.append(
                                getattr(c, "string", str(c)).strip()
                                if getattr(c, "string", None) is not None
                                else ""
                            )
                    prefix = ("  " * depth) + "- "
                    lines.append(prefix + " ".join([p for p in text_parts if p]))
                    # nested lists
                    for sub in child.find_all(["ul", "ol"], recursive=False):
                        lines.extend(walk_list(sub, depth + 1))
            return lines

        return "\n".join(walk_list(tag))


def main():
    parser = argparse.ArgumentParser(
        description="Translate Markdown and produce a .po file"
    )
    parser.add_argument("-i", "--input", help="path to input markdown file")
    parser.add_argument("-o", "--outdir", help="output directory for .po file")
    parser.add_argument("-a", "--author", help="author of the translation")
    args = parser.parse_args()

    path = Path(args.input)
    out_dir = Path(args.outdir)
    client = OpenAI(api_key="", base_url="http://127.0.0.1:1234/v1")
    model = "hunyuan-mt-7b"
    prampt = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "你是一个精通翻译的助手，能够准确翻译markdown文档。",
            },
            {"role": "user", "content": "帮我把下面的文本翻译成英文：\n\n文件内容"},
        ],
        "temperature": 0.7,
        "max_tokens": 2048,
        "top_p": 0.9,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }

    if not path.exists():
        print(f"文件未找到: {path}")
        return

    text = path.read_text(encoding="utf-8")

    parser = MarkdownParser(text)
    # print(json.dumps([asdict(node) for node in parser.nodes], ensure_ascii=False, indent=2))
    nodes = parser.nodes
    # prepare output .po file using polib
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / path.name.replace(".md", ".po")
    po = polib.POFile()
    # minimal metadata: author (Last-Translator), date (PO-Revision-Date), language
    po.metadata = {
        "Last-Translator": args.author,
        "PO-Revision-Date": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %z"),
        "Language": "zh_CN",
    }
    can_translate_type = ("paragraph", "heading")
    for node in nodes:
        text = ""
        if node.type == "frontmatter":
            for line in node.text.splitlines():
                if line.startswith("description: "):
                    text = line[13:]
        if node.type in can_translate_type:
            text = node.md_raw
            if text.startswith("### -"):
                continue
            if "```" in text:
                continue
        input_text = text.replace("\n", " ")
        prampt["messages"][1][
            "content"
        ] = f"帮我把下面的文本翻译成中文，确保原有markdown格式不变：\n\n{input_text}"
        response = client.chat.completions.create(**prampt)
        translation = response.choices[0].message.content
        # skip empty msgid
        if not text or str(text).strip() == "":
            continue
        entry = polib.POEntry(msgid=str(text), msgstr=str(translation))
        po.append(entry)
    po.save(str(out_path))
    print(f"Wrote translations to {out_path}")


if __name__ == "__main__":
    main()
