---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/set-culture?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-Culture
---

# Set-Culture

## 摘要
设置当前用户账户的用户文化（即用户所使用的地区、语言等相关信息）。

## 语法

```
Set-Culture [-CultureInfo] <CultureInfo> [<CommonParameters>]
```

## 描述
**Set-Culture** cmdlet 用于为当前用户账户设置特定的文化环境。在非托管代码开发中，这种“文化环境”被称为 “locale”。相关信息包括该文化的名称、书写系统、日历以及日期和字符串的格式设置等。有关更多详细信息，请参阅 [CultureInfo 类](https://go.microsoft.com/fwlink/?LinkID=242306) 和 [可配置的语言和文化设置](https://go.microsoft.com/fwlink/?LinkID=242307)。

## 示例

#### 示例 1：设置文化环境（即语言、地区等相关信息）
```powershell
PS C:\> Set-Culture -CultureInfo de-DE
```

此命令将当前用户账户的文化设置设置为德语（德国）。

## 参数

### -CultureInfo
指定一种文化（即语言环境或风俗习惯）。

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
此 cmdlet 支持以下常见参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注
使用此cmdlet所做的更改将在后续的PowerShell会话中生效。

## 相关链接

[GetCulture 类](https://go.microsoft.com/fwlink/?LinkID=243343)

