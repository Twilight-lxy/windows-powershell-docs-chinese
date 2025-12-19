---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/get-winacceptlanguagefromlanguagelistoptout?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WinAcceptLanguageFromLanguageListOptOut
---

# 使用 `Get-WinAcceptLanguageFromLanguageListOptOut` 命令获取用户的语言偏好设置

## 摘要
从当前用户账户的语言列表设置中获取HTTP Accept Language（即用户支持的编程语言）。

## 语法

```
Get-WinAcceptLanguageFromLanguageListOptOut [<CommonParameters>]
```

## 描述
`Get-WinAcceptLanguageFromLanguageListOptOut` cmdlet 可以获取当前用户账户的 “从语言列表中排除 HTTP 接受语言”（HTTP Accept Language from Language List opt-out）设置。默认情况下，`HTTP 接受语言列表` 是根据当前用户账户的语言列表自动生成的。

当该设置为 `$True` 时，会删除 **HTTP Accept Language** 注册表键中的当前内容，并阻止对语言列表的任何更改重新设置该键。当该设置为 `$False` 时，会根据当前用户账户的语言列表来重新设置 **HTTP Accept Language List**。

## 示例

### 示例 1：获取设置的状态
```
PS C:\> Get-WinAcceptLanguageFromLanguageListOptOut
TRUE
```

该命令返回当前用户账户的“HTTP Accept Language（来自语言列表的拒绝选项）”设置的状态。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 布尔值（Boolean）
此cmdlet返回一个布尔值，用于报告当前用户账户的“HTTP接受语言（来自语言列表的禁用选项）”设置的状态。

## 备注

## 相关链接

[Set-WinAcceptLanguageFromLanguageListOptOut](./Set-WinAcceptLanguageFromLanguageListOptOut.md)

[Get-WinUserLanguageList](./Get-WinUserLanguageList.md)
