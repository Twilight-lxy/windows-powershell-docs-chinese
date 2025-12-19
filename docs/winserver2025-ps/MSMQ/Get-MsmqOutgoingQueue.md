---
description: 使用此主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/get-msmqoutgoingqueue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-MsmqOutgoingQueue
---

# Get-MsmqOutgoingQueue

## 摘要
获取出站消息队列。

## 语法

```
Get-MsmqOutgoingQueue [[-Name] <String[]>] [<CommonParameters>]
```

## 描述
`Get-MsmqOutgoingQueue` cmdlet 用于获取 `MsmqOutgoingQueue` 对象。每个对象代表一个事务性或非事务性的出站队列。该 cmdlet 会获取运行该 cmdlet 的计算机上的所有出站队列；如果您没有指定参数，它将获取主机计算机的所有出站队列。

## 示例

### 示例 1：获取传出消息队列
```
PS C:\> Get-MsmqOutgoingQueue -Name "Order*"
```

这个命令会获取当前计算机上所有以“Order”开头的外发消息队列。

## 参数

### -Name
指定一个队列名称数组。这些名称表示用于发送数据的输出队列。该参数支持通配符；默认值为“*”。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### System.Object

## 备注

## 相关链接

[Clear-MsmqOutgoingQueue](./Clear-MsmqOutgoingQueue.md)

[ Resume-MsmqOutgoingQueue](./Resume-MsmqOutgoingQueue.md)

[暂停 MsmqOutgoingQueue 服务](./Suspend-MsmqOutgoingQueue.md)

