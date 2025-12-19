---
description: `Get-InstalledLanguage` cmdlet 可以让你查看当前正在运行的 Windows 系统中安装了哪些语言。
external help file: Microsoft.LanguagePackManagement.Powershell.Commands.dll-Help.xml
Module Name: LanguagePackManagement
ms.date: 08/15/2022
online version: https://learn.microsoft.com/powershell/module/languagepackmanagement/get-installedlanguage?view=windowsserver2025-ps
schema: 2.0.0
title: Get-InstalledLanguage
---

# Get-InstalledLanguage

## 摘要
返回有关设备上已安装语言的信息。

## 语法

```
Get-InstalledLanguage [-Language] <String> [<CommonParameters>]
```

## 描述
返回一个列表，其中包含设备上安装的语言以及相关的语言功能。

## 示例

### 示例 1：查看设备上安装了哪些语言

```powershell
Get-InstalledLanguage
```

这个命令会显示设备上安装的所有语言组件。

### 示例 2：查看某种特定语言安装了哪些语言组件

```powershell
Get-InstalledLanguage -language en-US
```

这条命令会显示为“en-US”语言安装的语言特性（即该语言支持的功能或特性）。

## 参数

### -Language

显示为指定语言安装的语言相关组件。

```yaml
Type: String
Parameter Sets: (All)
Aliases: LanguageId, LanguageTag

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### System.Collections.Generic.List<Microsoft(LanguagePackManagement.PowershellCommands.InstalledLanguage>

## 备注

## 相关链接

[Set-SystemPreferredUILanguage](Set-SystemPreferredUILanguage.md)
