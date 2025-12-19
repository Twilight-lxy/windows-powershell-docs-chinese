---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/get-winculturefromlanguagelistoptout?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WinCultureFromLanguageListOptOut
---

# 使用 `Get-WinCultureFromLanguageListOptOut` 函数获取指定语言列表中的相关文化信息

## 摘要
从当前用户账户的语言列表设置中获取相应的“文化信息”（即与该语言相关的文化背景或习俗等数据）。

## 语法

```
Get-WinCultureFromLanguageListOptOut [<CommonParameters>]
```

## 描述
`Get-WinCultureFromLanguageListOptOut` cmdlet 用于获取当前用户账户的“文化设置”（即用户语言环境）的配置。当该设置为 `$True` 时，Windows 显示语言的更改不会影响用户的“文化设置”。而当设置为 `$False` 时，每当显示语言发生变化时，“文化设置”会自动重新调整以匹配新的显示语言。默认值为 `$False`。

## 示例

### 示例 1：获取 Culture （文化设置）的覆盖值
```
PS C:\> Get-WinCultureFromLanguageListOptOut
```

这个命令用于获取当前用户账户的文化设置（即语言或区域相关偏好）。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 布尔值（Boolean）
此cmdlet返回一个布尔值，用于报告该设置的状态。

## 备注

## 相关链接

[Set-WinCultureFromLanguageListOptOut](./Set-WinCultureFromLanguageListOptOut.md)

