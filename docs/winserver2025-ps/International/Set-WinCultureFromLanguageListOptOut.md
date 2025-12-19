---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/set-winculturefromlanguagelistoptout?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WinCultureFromLanguageListOptOut
---

# Set-WinCultureFromLanguageListOptOut

## 摘要
将当前用户账户的语言列表中的“退出”设置所对应的文化值进行设置。

## 语法

```
Set-WinCultureFromLanguageListOptOut [-OptOut] <Boolean> [<CommonParameters>]
```

## 描述
`Set-WinCultureFromLanguageListOptOut` cmdlet 用于设置当前用户账户的“文化设置”（即用户区域设置）的相关选项。将此选项设置为 `$True` 可以禁用根据 Windows 显示语言的变化动态调整用户文化设置的功能；将其设置为 `$False` 则会启用该动态调整功能。默认值为 `$False`。

## 示例

### 示例 1：块级动态设置
```
PS C:\> Set-WinCultureFromLanguageListOptOut -OptOut $True
```

此命令会阻止动态设置功能的执行。

## 参数

### -OptOut
指定退出（opt-out）操作的值。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-WinCultureFromLanguageListOptOut](./Get-WinCultureFromLanguageListOptOut.md)

