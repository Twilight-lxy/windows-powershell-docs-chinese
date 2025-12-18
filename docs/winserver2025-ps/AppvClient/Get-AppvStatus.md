---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/get-appvstatus?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppvStatus
---

# 获取应用程序版本状态（Get-AppvStatus）

## 摘要
获取App-V服务的状态。

## 语法

```
Get-AppvStatus [<CommonParameters>]
```

## 描述
`Get-AppvStatus` cmdlet 用于获取 Microsoft 应用程序虚拟化（App-V）服务的状态。该 cmdlet 会返回一个 `$True` 或 `$False` 的值，表示 App-V 是否已启用以及是否需要重启。

## 示例

#### 示例 1：获取状态信息
```
PS C:\> Get-AppvStatus
```

这个命令用于获取App-V服务的状态信息。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[禁用 AppV](./Disable-Appv.md)

[Enable-Appv](./Enable-Appv.md)

