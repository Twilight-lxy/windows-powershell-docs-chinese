---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/set-winsystemlocale?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WinSystemLocale
---

# Set-WinSystemLocale

## 摘要
设置当前计算机的系统区域设置（locale）。

## 语法

```
Set-WinSystemLocale [-SystemLocale] <CultureInfo> [<CommonParameters>]
```

## 描述
`Set-WinSystemLocale` cmdlet 用于设置当前计算机的系统区域设置（system locale）。系统区域设置决定了计算机默认使用哪些代码页，这些代码页包括 ANSI、DOS 和 Macintosh 等编码格式。如果您更改了系统区域设置，系统会自动安装相应的位图字体文件，以支持使用所选语言的旧版应用程序。

这是一个系统设置。只有拥有管理员权限的用户才能更改它。更改会在计算机重新启动后生效。

## 示例

#### 示例 1：设置系统区域设置
```
PS C:\> Set-WinSystemLocale -SystemLocale ja-JP
```

这个命令将系统的区域设置设置为日语（日本）。

## 参数

### -SystemLocale
指定一个系统区域设置（locale）。

```yaml
Type: CultureInfo
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### CultureInfo
一个包含 BCP-47 标签的对象，用于指定当前计算机的系统区域设置。有关 CultureInfo 对象的更多信息，请参阅 [CultureInfo 类](https://go.microsoft.com/fwlink/?LinkID=242306)。

## 输出

## 备注
请注意，计算机上的“系统区域设置”主要用于选择旧的代码页和作为字体替代方案。这个设置主要被那些不支持Unicode的应用程序所使用。它不应被视为传统的地区设置或文化信息，也不应与用户的地区设置（区域格式）混淆。

在更改系统区域设置时，强烈建议同时更改计算机的 Windows 显示语言或用户界面（UI）语言设置，以确保它们与系统区域设置保持一致。在某些情况下，UI 语言的正确显示可能依赖于代码页和/或字体。如果不这样做，可能会导致非 Unicode 应用程序无法正常运行。

## 相关链接

[可配置的语言和文化设置](https://go.microsoft.com/fwlink/?LinkID=242307)

[Get-WinSystemLocale](./Get-WinSystemLocale.md)

