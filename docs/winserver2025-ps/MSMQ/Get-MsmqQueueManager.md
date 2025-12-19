---
description: 使用此主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/get-msmqqueuemanager?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-MsmqQueueManager
---

# Get-MsmqQueueManager

## 摘要
获取一个队列管理器。

## 语法

```
Get-MsmqQueueManager [<CommonParameters>]
```

## 描述
`Get-MsmqQueueManager` cmdlet 可以获取一个 `QueueManager` 对象。该 `QueueManager` 对象包含了本地队列管理器的状态信息。此 cmdlet 通过使用 Microsoft Message Queuing（简称 MSMQ）的原生 API 来获取 `QueueManager` 对象的属性。

## 示例

#### 示例 1：获取队列管理器
```
PS C:\> Get-MsmqQueueManager
```

这个命令用于获取队列管理器。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Set-MsmqQueueManager](./Set-MsmqQueueManager.md)

