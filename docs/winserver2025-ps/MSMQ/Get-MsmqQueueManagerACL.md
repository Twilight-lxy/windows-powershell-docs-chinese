---
description: 使用此主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/get-msmqqueuemanageracl?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-MsmqQueueManagerACL
---

# Get-MsmqQueueManagerACL

## 摘要
获取本地队列管理器的访问控制列表。

## 语法

```
Get-MsmqQueueManagerACL [<CommonParameters>]
```

## 描述
`Get-MsmqQueueManagerACL` cmdlet 用于获取本地队列管理器的 `MsmqQueueManagerAcl` 对象数组。

## 示例

### 示例 1：获取本地队列管理器的消息队列管理器访问控制列表（ACL）
```
PS C:\> Get-MsmqQueueManagerACL
```

此命令用于获取本地队列管理器的消息队列管理器访问控制列表（ACL）信息。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Set-MsmqQueueManagerACL](./Set-MsmqQueueManagerACL.md)

