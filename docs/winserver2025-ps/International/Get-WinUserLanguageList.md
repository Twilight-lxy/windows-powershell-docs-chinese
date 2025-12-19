---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/get-winuserlanguagelist?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WinUserLanguageList
---

# Get-WinUserLanguageList

## 摘要
获取当前用户账户对应的语言列表。

## 语法

```
Get-WinUserLanguageList [<CommonParameters>]
```

## 描述
`Get-WinUserLanguageList` cmdlet 可以返回当前用户的语言设置。这些设置包括输入法、拼写设置、文本预测设置以及手写输入模式等信息。有关更多详细信息，请参阅 [CultureInfo 类](https://go.microsoft.com/fwlink/?LinkID=242306) 和 [在 Windows 10 中管理输入和显示语言设置](https://support.microsoft.com/help/4496404/windows-10-manage-the-input-and-display-language#input_language)。

## 示例

### 示例 1：获取当前账户的语言列表
```
PS C:\> Get-WinUserLanguageList
LanguageTag     : en-US
Autonym         : English (United States)
EnglishName     : English (United States)
LocalizedName   : English (United States)
ScriptName      : Latin
InputMethodTips : {0409:00000409}
Handwriting     : False
LanguageTag     : fr-FR
Autonym         : français (France)
EnglishName     : French (France)
LocalizedName   : French (France)
ScriptName      : Latin
InputMethodTips : {040c:0000040c}
Handwriting     : False
```

此命令返回当前用户账户的语言列表、BCP-47标签以及相应的显示名称。

### 示例 2：显示输入方法
```
PS C:\> (Get-WinUserLanguageList)[0].InputMethodTips
0409:00000409
0409:00010409
```

该命令以 TIP 字符串的形式返回当前已启用的输入方法列表。

### 示例 3：显示一个自命名（autonym）属性
```
PS C:\> (Get-WinUserLanguageList)[0].autonym
English (United States)
```

该命令返回用户语言列表中第一个项目的“autonym”属性值。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Collections.Generic.List<Microsoft.InternationalSettingscommands.WinUserLanguage>
此 cmdlet 返回一个 **WinUserLanguage** 对象列表，这些对象包含当前用户账户语言列表中的一个或多个语言及相关属性。有关 **Generic.List** 对象的详细信息，请参阅 [List(Of T) 类](https://go.microsoft.com/fwlink/?LinkID=243342)。

通用列表对象支持以下方法：

- Add("`LanguageTag`")
- Insert(index, "`LanguageTag`")
- Remove(Index)

`outputLanguage` 对象包含以下属性：

- **LanguageTag** (READ).
A standard BCP-47 language tag that is used to identify languages.
For more information, see the [Internet Engineering Task Force (IETF) BCP 47 RFC](https://go.microsoft.com/fwlink/?LinkID=242207).
- **Autonym** (LP database) (READ).
The name of the language in the language itself.
- **EnglishName** (LP database) (READ).
The name of the language in English.
- **LocalizedName** (LP database) (READ).
The name of the language in the current Windows display language.
- **ScriptName** (LP database) (READ).
The writing system of the language.
- **InputMethodTips** (READ/WRITE).
A list of input method Tablet Input Panel (TIP) strings that are enabled for this language.
The enabled Input methods are listed in the format `Language ID: Keyboard layout ID`.
- **Handwriting** (READ/WRITE).
This value is either 0 (freehand) or 1 (write each character separately).

## 备注

## 相关链接

[New-WinUserLanguageList](./New-WinUserLanguageList.md)

[Set-WinUserLanguageList](./Set-WinUserLanguageList.md)
