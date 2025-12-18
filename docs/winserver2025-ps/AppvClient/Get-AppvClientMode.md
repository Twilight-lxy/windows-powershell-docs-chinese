---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/get-appvclientmode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppvClientMode
---

# Get-AppvClientMode

## 摘要
显示 App-V 客户端的模式。

## 语法

```
Get-AppvClientMode [<CommonParameters>]
```

## 描述
`Get-AppvClientMode` cmdlet 用于显示 Microsoft 应用虚拟化（App-V）客户端当前所处的模式。有效的值有 “Normal” 和 “Uninstall”。

## 示例


## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.AppV.AppvClientPowerShell.AppvClientMode
此cmdlet生成一个**AppvClientMode**对象，用于描述当前的App-V客户端模式（正常模式或卸载模式）。

## 备注

## 相关链接

[Set-AppvClientMode](./Set-AppvClientMode.md)

