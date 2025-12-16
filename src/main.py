import os
from pathlib import Path
import time
import polib
from loguru import logger


class FileTree:
    root: Path
    sub_file: list[Path]
    sub_dict: list["FileTree"]

    def __init__(self, root: Path) -> None:
        self.root = root
        self.sub_dict = []
        self.sub_file = []

    def build(self) -> None:
        for item in self.root.iterdir():
            if item.is_dir():
                subtree = FileTree(item)
                subtree.build()
                self.sub_dict.append(subtree)
            elif item.is_file():
                self.sub_file.append(item)

    def print_tree(self, indent: str = "") -> None:
        logger.info(f"{indent}{self.root.name}/")
        indent += "    "
        for f in self.sub_file:
            logger.info(f"{indent}{f.name}")
        for d in self.sub_dict:
            d.print_tree(indent)

    def get_sub_files(self) -> list[Path]:
        return self.sub_file

    def get_sub_dirs(self) -> list["FileTree"]:
        return self.sub_dict

    def find_sub_dir(self, name: str) -> FileTree | None:
        for d in self.sub_dict:
            if d.root.name == name:
                return d
        return None

    def find_sub_file(self, name: str) -> Path | None:
        for f in self.sub_file:
            if f.name == name:
                return f
        return None


class Translator:
    input_dir: Path
    output_dir: Path
    po_dir: Path
    exts: set

    def __init__(
        self, input_dir: Path, output_dir: Path, po_dir: Path, exts: set
    ) -> None:
        if not po_dir.exists():
            logger.error(f".po 文件目录未找到: {po_dir}")
            exit(1)
        self.po_dir = po_dir
        logger.info(f"使用的 .po 目录: {self.po_dir}")
        if not input_dir.exists():
            logger.error(f"输入目录未找到: {input_dir}")
            exit(1)
        self.input_dir = input_dir
        logger.info(f"使用的输入目录: {self.input_dir}")
        if output_dir.exists():
            suffix = time.strftime("_%Y%m%d_%H%M%S", time.localtime())
            output_dir = output_dir.with_name(output_dir.name + suffix)
            logger.warning(f"输出目录已存在, 将使用新的输出目录: {output_dir}")
            if output_dir.exists():
                logger.error(f"输出目录已存在: {output_dir}")
                exit(1)
        self.output_dir = output_dir
        os.makedirs(self.output_dir)
        logger.info(f"使用的输出目录: {self.output_dir}")
        if not exts:
            logger.error("未指定任何文件扩展名")
            exit(1)
        self.exts = exts
        logger.info(f"处理的文件扩展名: {self.exts}")

        self.make_file_tree(self.input_dir)

        self.resolve_translate(self.input_file_tree, self.po_file_tree)

    def make_file_tree(self, input_dir: Path) -> None:
        self.input_file_tree = FileTree(input_dir)
        self.input_file_tree.build()

        self.po_file_tree = FileTree(self.po_dir)
        self.po_file_tree.build()

    def resolve_translate(
        self,
        input_file_tree: FileTree,
        po_file_tree: FileTree,
        use_po_file_dict: dict = {},
        dir_num: int = 0,
    ) -> None:

        for input_file in input_file_tree.get_sub_files():
            input_file_dir_without_root = input_file.parent.relative_to(self.input_dir)
            po_file = (
                self.po_dir / input_file_dir_without_root / (input_file.stem + ".po")
            )
            output_file = (
                self.output_dir / input_file_dir_without_root / input_file.name
            )

            if po_file_tree.find_sub_file(po_file.name) is None:
                logger.warning(f".po 文件未找到: {po_file}")
                continue
            os.makedirs(output_file.parent, exist_ok=True)
            use_po_file_dict.update({po_file: dir_num + 1})

            with open(input_file, "r", encoding="utf-8") as f:
                content = f.read()
            translated_content = self.translate(content, use_po_file_dict)

            with open(output_file, "w", encoding="utf-8") as f:
                f.write(translated_content)

            logger.info(f"已翻译文件: {input_file} -> {output_file}")

            use_po_file_dict.pop(po_file, None)

        for input_sub_dir in input_file_tree.sub_dict:
            po_sub_dir = po_file_tree.find_sub_dir(input_sub_dir.root.name)
            if po_sub_dir is None:
                logger.warning(f".po 目录未找到: {input_sub_dir.root}")
                continue
            po_file = po_file_tree.find_sub_file(input_sub_dir.root.name + ".po")
            if po_file is not None:
                use_po_file_dict.update({po_file: dir_num + 1})
            self.resolve_translate(
                input_sub_dir,
                po_sub_dir,
                use_po_file_dict,
                dir_num + 1,
            )
            use_po_file_dict.pop(po_file, None)

    def translate(self, text: str, use_po_file_dict: dict) -> str:
        sorted_po_files = sorted(use_po_file_dict.items(), key=lambda x: -x[1])
        translations = {}

        for po_file, weight in sorted_po_files:
            translations.update(self.load_translations(po_file))

        text = self.translate_text(text, translations)

        return text

    def load_translations(self, po_path: Path):
        po = polib.pofile(str(po_path))
        translations = {}
        for entry in po:
            if entry.msgstr:
                translations[entry.msgid] = entry.msgstr
        return translations

    def translate_text(self, text: str, translations: dict):
        # 按长度降序排序以避免部分匹配问题
        for src in sorted(translations.keys(), key=lambda s: -len(s)):
            dst = translations[src]
            if src in text:
                text = text.replace(src, dst)
        return text


def translate_directory(input_dir: Path, output_dir: Path, po_dir: Path, exts: set):

    for item in input_dir.rglob("*"):
        if item.is_dir():
            relative_path = item.relative_to(input_dir)
            (output_dir / relative_path).mkdir(parents=True, exist_ok=True)

    input_file_list = [f for f in input_dir.rglob("*") if f.suffix in exts]


def check_po_files(po_dir: Path) -> None:
    def test_po_file(po_path: Path):
        po = polib.pofile(str(po_path))

    error_flag = False
    for po_file in po_dir.rglob("*.po"):
        po_path = po_file.relative_to(po_dir)
        try:
            test_po_file(po_file)
        except Exception as e:
            logger.error(f".po 文件格式错误: {po_path}, 错误信息: {e}")
            error_flag = True
    if error_flag:
        logger.error("存在格式错误的 .po 文件, 请修正后重试.")
        exit(1)


def main():
    log_file_name = time.strftime("loguru_%Y%m%d_%H%M%S.log", time.localtime())
    logger.add(log_file_name)

    po_dir = Path("./translate")
    input_dir = Path("./docset")
    output_dir = Path("./docs")

    exts = {".md"}
    check_po_files(po_dir)
    Translator(input_dir, output_dir, po_dir, exts)


if __name__ == "__main__":
    main()
