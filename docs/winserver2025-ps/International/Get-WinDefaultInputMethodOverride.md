---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.InternationalSettings.Commands.dll-Help.xml
Locale: en-US
Module Name: International
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/international/get-windefaultinputmethodoverride?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WinDefaultInputMethodOverride
---

# Get-WinDefaultInputMethodOverride

## 摘要
获取当前用户账户的默认输入法覆盖设置。

## 语法

```
Get-WinDefaultInputMethodOverride [<CommonParameters>]
```

## 描述
`Get-WinDefaultInputMethodOverride` cmdlet 用于检索默认的输入方法覆盖设置，该设置指定了当前用户账户的默认输入方法。如果没有使用任何覆盖设置，则输入方法会从当前用户账户的语言列表中动态确定。有关更多信息，请参阅 `Get-WinUserLanguageList` 和 `Set-WinUserLanguageList` cmdlets。

## 示例

#### 示例 1：显示默认的输入方法
```
PS C:\> Get-WinDefaultInputMethodOverride
InputMethodTip      Keyboard name
---------------     -------------
0409:00000409       English (United States) - US
```

该命令会返回并显示当前用户账户的默认输入方法。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### WinKeyboardObject
这个 cmdlet 返回用于设置默认输入方法的 Tablet Input Panel（TIP）相关字符串。

## 备注

## 相关链接

[Set-WinDefaultInputMethodOverride](./Set-WinDefaultInputMethodOverride.md)

