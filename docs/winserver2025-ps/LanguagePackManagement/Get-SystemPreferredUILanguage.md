---
description: `Get-SystemPreferredUILanguage` cmdlet 可以让你查看在当前运行的 Windows 系统中，哪种语言被设置为“系统首选用户界面语言”（System Preferred UI Language）。
external help file: Microsoft.LanguagePackManagement.Powershell.Commands.dll-Help.xml
Module Name: LanguagePackManagement
ms.date: 06/21/2023
online version: https://learn.microsoft.com/powershell/module/languagepackmanagement/get-systempreferreduilanguage?view=windowsserver2025-ps
schema: 2.0.0
title: Get-SystemPreferredUILanguage
---

# Get-SystemPreferredUILanguage

## 摘要
返回当前系统的首选语言。

## 语法

```
Get-SystemPreferredUILanguage [<CommonParameters>]
```

## 描述

返回被设置为系统首选语言的语言。

## 示例

### 示例 1

```powershell
Get-SystemPreferredUILanguage
```

这个命令会返回当前设置为系统首选用户界面语言的语言。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.String

## 相关链接

[Set-SystemPreferredUILanguage](set-systempreferreduilanguage.md) [InstallLanguage](install-language.md)
