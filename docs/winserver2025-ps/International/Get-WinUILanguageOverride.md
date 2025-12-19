---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/get-winuilanguageoverride?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WinUILanguageOverride
---

# Get-WinUILanguageOverride

## 摘要
获取当前用户账户的 Windows 用户界面语言覆盖设置。

## 语法

```
Get-WinUILanguageOverride [<CommonParameters>]
```

## 描述
`Get-WinUILanguageOverride` cmdlet 会显示用户在重启或登出后希望使用的 Windows 用户界面（UI）的语言设置。如果未应用任何语言覆盖设置，`Get-WinUILanguageOverride` 将不会返回任何值；如果有待生效的更改，该 cmdlet 会返回这些更改的相关信息。

有关更多信息，请参阅 `Get-WinUserLanguageList` 和 `Set-WinUserLanguageList` cmdlet。

## 示例

### 示例 1：显示语言覆盖设置
```
PS C:\> Get-WinUILanguageOverride
LCID             Name             DisplayName
----             ----             -----------
1033             en-US            English (United States)
```

该命令用于获取并显示当前用户账户的UI语言设置（即是否允许更改Windows界面的语言）。如果当前用户账户尚未设置UI语言相关的选项，那么该命令将返回空值（null）。

## 参数

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### CultureInfo
此cmdlet返回当前用户账户的Windows UI语言设置。有关**CultureInfo**对象的更多信息，请参阅[CultureInfo类](https://go.microsoft.com/fwlink/?LinkID=242306)。

## 备注

## 相关链接

[Get-WinUserLanguageList](./Get-WinUserLanguageList.md)

[Set-WinUILanguageOverride](./Set-WinUILanguageOverride.md)

[Set-WinUserLanguageList](./Set-WinUserLanguageList.md)

