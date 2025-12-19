---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/get-winsystemlocale?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WinSystemLocale
---

# Get-WinSystemLocale

## 摘要
获取当前计算机的系统区域设置（System-locale）。

## 语法

```
Get-WinSystemLocale [<CommonParameters>]
```

## 描述
`Get-WinSystemLocale` cmdlet 返回 `System-Locale` 设置的当前值。`System-Locale` 设置决定了计算机默认使用哪些代码页，这些代码页包括 ANSI、DOS 和 Macintosh 等。

## 示例

#### 示例 1：获取系统的区域设置（locale）
```
PS C:\> GET-WinSystemLocale
LCID             Name             DisplayName
----             ----             -----------
1033             en-US            English (United States)
```

该命令用于获取并显示当前计算机的系统区域设置（System-locale）。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### CultureInfo
此cmdlet返回当前计算机的系统区域设置（locale）。有关CultureInfo对象的更多信息，请参阅[CultureInfo类](https://go.microsoft.com/fwlink/?LinkID=242306)。

## 备注

## 相关链接

[在 Windows 10 中管理输入和显示语言设置](https://support.microsoft.com/help/4496404/windows-10-manage-the-input-and-display-language#input_language)

[Set-WinSystemLocale](./Set-WinSystemLocale.md)

