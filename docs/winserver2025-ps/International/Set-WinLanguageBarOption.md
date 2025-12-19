---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/set-winlanguagebaroption?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WinLanguageBarOption
---

# Set-WinLanguageBarOption

## 摘要
为当前用户账户设置语言栏的类型和模式。

## 语法

```
Set-WinLanguageBarOption [-UseLegacySwitchMode] [-UseLegacyLanguageBar] [<CommonParameters>]
```

## 描述
`Set-WinLanguageBarOption` cmdlet 使用 `LanguageBar` 对象来设置语言栏的类型和模式。类型和模式的值可以是 `true` 或 `false`。每个设置的默认值为 `false`。

## 示例

#### 示例 1：设置语言栏选项
```
PS C:\> Set-WinLanguageBarOption -UseLegacySwitchMode -UseLegacyLanguageBar
```

此命令将语言栏模式设置为旧版设置，并将语言栏类型设置为每线程独立设置。

### 示例 2：将语言栏选项设置回默认值
```
PS C:\> Set-WinLanguageBarOption
```

此命令将语言栏的模式和类型设置为默认值。

## 参数

### -UseLegacyLanguageBar
该参数表示此cmdlet会将语言栏模式设置为旧版设置。如果您未指定此参数，cmdlet会将语言栏模式设置为默认设置。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseLegacySwitchMode
表示此cmdlet将语言栏切换模式设置为“传统模式”或“每线程模式”。如果您不指定此参数，cmdlet会将语言栏切换模式设置为默认值或“每个用户单独设置”的模式。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-WinLanguageBarOption](./Get-WinLanguageBarOption.md)

