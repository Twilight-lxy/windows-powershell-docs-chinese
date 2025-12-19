---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/new-winuserlanguagelist?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-WinUserLanguageList
---

# New-WinUserLanguageList

## 摘要
创建一个新的语言列表对象。

## 语法

```
New-WinUserLanguageList [-Language] <String> [<CommonParameters>]
```

## 描述
`New-WinUserLanguageList` cmdlet 用于创建一个用户语言列表对象。该对象的设置包括输入方法、拼写设置、文本预测设置以及手写输入模式等。有关更多详细信息，请参阅 [CultureInfo 类](https://go.microsoft.com/fwlink/?LinkID=242306) 和 [可配置的语言和文化设置](https://go.microsoft.com/fwlink/?LinkID=242307)。

## 示例

### 示例 1：创建并设置语言列表
```powershell
PS C:\> $UserLanguageList = New-WinUserLanguageList -Language "en-US"
PS C:\> $UserLanguageList.Add("fr-FR")
PS C:\> Set-WinUserLanguageList -LanguageList $UserLanguageList
```

第一个命令创建了一个语言列表，其中包含了美式英语（US English）。该命令将这个列表存储在 `$UserLanguageList` 变量中。

第二个命令将“France French”添加到 `$UserLanguageList` 中的对象中。

最后一个命令使用 **Set-WinUserLanguageList** cmdlet 将 `$UserLanguageList` 中的列表分配给当前用户账户。

## 参数

### -Language
用于指定一种语言。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Collections.Generic.List<Microsoft.InternationalSettingscommandsWinUserLanguage>
这是一个包含 **WinUserLanguage** 对象的列表，这些对象表示当前用户账户语言列表中的一种或多种语言及其相关属性。有关 **Generic.List** 对象的更多信息，请参阅 [System.Collections.Generic.List(Of T)](https://go.microsoft.com/fwlink/?LinkID=243342)。

这个通用的列表对象支持以下方法：

- Add("BCP-47")
- Insert(index, "BCP-47")
- Remove(Index)

`LanguageList` 是当前用户账户中语言对象列表的一个集合。该语言列表对象包含了以下方法：

- **Add** ("BCP-47")
- **Insert** (BCP-47, index)
- **Remove** (BCP-47)
- **Remove** (Index)

`languageList` 对象包含以下属性：

- **BCP-47** (READ).
A standard language tag that is used to identify languages.
For more information, see the [Internet Engineering Task Force (IETF) BCP 47 RFC](https://go.microsoft.com/fwlink/?LinkID=242207).
- **Autonym** (LP database) (READ).
The name of the language in the language itself.
- **English name** (LP database) (READ).
The name of the language in English.
- **Localized name** (LP database) (READ).
The name of the language in the current Windows display language.
- **Script** (LP database) (READ).
The writing system of the language.
- **Input methods** (READ/WRITE).
A list of input method Tablet Input Panel (TIP) strings that are enabled for this language.
The enabled input methods are listed in the format `Language ID: Keyboard layout ID`.
- **Handwriting recognition input mode** (READ/WRITE).
This value is either 0 (freehand) or 1 (write each character separately).

## 备注

## 相关链接

[Get-WinUserLanguageList](./Get-WinUserLanguageList.md)

[Set-WinUserLanguageList](./Set-WinUserLanguageList.md)

