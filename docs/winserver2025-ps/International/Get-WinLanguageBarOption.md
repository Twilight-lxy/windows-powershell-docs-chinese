---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/get-winlanguagebaroption?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WinLanguageBarOption
---

# Get-WinLanguageBarOption

## 摘要
获取当前用户账户的语言栏模式和语言栏类型。

## 语法

```
Get-WinLanguageBarOption [<CommonParameters>]
```

## 描述
`Get-WinLanguageBarOption` cmdlet 使用 `LanguageBar` 对象来获取语言栏的类型和模式。类型和模式的设置值可以是 `true` 或 `false`。每个设置的默认值为 `false`。

## 示例

### 示例 1：获取语言栏的设置
```
PS C:\> Get-WinLanguageBarOption
IsLegacyLanguageBar    IsLegacySwitchingMode
-------------------    ---------------------
False                  False
```

此命令返回当前用户账户的语言栏选项的当前设置。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### LanguageBar
此cmdlet返回一个对象，其中包含以下设置。

- **IsLegacyLanguageBar**.
When this setting is set to true, the desktop language bar is used, where available.
When this setting is set to false, the modem input switcher is used.
This is recommended.
- **IsLegacySwitchingMode**.
When this setting is set to true, the current input method, which includes keyboard layout or input method editor (IME), is selected for the current application only.
When new applications start, the default input method is selected.
For more information, see the **Get-WinDefaultInputMethodOverride** cmdlet.
When this setting is set to false, the input method is selected for all applications and changes only when the user actively switches input methods (recommended).

## 备注

## 相关链接

[Get-WinDefaultInputMethodOverride](./Get-WinDefaultInputMethodOverride.md)

[Set-WinLanguageBarOption](./Set-WinLanguageBarOption.md)

