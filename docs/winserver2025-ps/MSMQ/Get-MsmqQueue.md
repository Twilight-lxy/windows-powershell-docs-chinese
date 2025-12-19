---
description: 使用此主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/get-msmqqueue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-MsmqQueue
---

# Get-MsmqQueue

## 摘要
获取消息队列。

## 语法

### 全部（默认设置）
```
Get-MsmqQueue [[-Name] <String[]>] [-QueueType <QueueType>] [<CommonParameters>]
```

### 期刊
```
Get-MsmqQueue [[-Name] <String[]>] [-QueueType <QueueType>] [-Journal] [<CommonParameters>]
```

### SubQueue
```
Get-MsmqQueue [[-Name] <String[]>] [-QueueType <QueueType>] [-SubQueue <String>] [<CommonParameters>]
```

## 描述
`Get-MsmqQueue` cmdlet 用于获取一组 `MsmqQueue` 对象。每个 `MsmqQueue` 对象代表一个现有的私有队列、公共队列或系统队列。该 cmdlet 会获取运行该 cmdlet 的计算机上的所有队列；如果未指定参数，它将获取主机计算机上的所有公共队列、私有队列和系统队列。

## 示例

### 示例 1：获取公共队列、私有队列和系统队列
```
PS C:\> Get-MsmqQueue
```

这个命令可以获取主机计算机上的公共队列、私有队列和系统队列信息。

#### 示例 2：获取私有队列
```
PS C:\> Get-MsmqQueue -Name "Order*" -QueueType Private
```

此命令用于获取主机计算机上名称以“Order”开头的私有队列。

### 示例 3：获取私有日志队列
```
PS C:\> Get-MsmqQueue -Name "Order*" -Journal -QueueType Private
```

这个命令用于获取主机计算机上那些名称以字符串“Order”开头的私有日志队列（Journal queues）。

### 示例 4：获取系统日志队列
```
PS C:\> Get-MsmqQueue -QueueType SystemJournal
```

这个命令用于获取主机计算机的系统日志队列（system journal queues）。

### 示例 5：获取所有本地队列及其消息数量
```
PS C:\> Get-MsmqQueue | Select QueueName, MessageCount
```

此命令会列出主机计算机上所有队列的消息数量。

## 参数

### -Journal
表示此cmdlet会检索与*Name*参数匹配的日志队列（或多个队列）。

```yaml
Type: SwitchParameter
Parameter Sets: Journal
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个队列名称数组。该参数支持通配符；默认值为 *。

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

### -QueueType
指定队列类型。该参数的可接受值为：

- PrivateAndPublic.
The cmdlet gets public and private queues that match the *Name* parameter.
- Private.
The cmdlet gets private queues that match the *Name* parameter.
- Public.
The cmdlet gets public queues that match the *Name* parameter.
- SystemDeadLetter.
The cmdlet gets non-transactional dead-letter queues that match the *Name* parameter.
- SystemJournal.
The cmdlet gets system journal queues that match the *Name* parameter.
- SystemTransactionalDeadLetter.
The cmdlet gets transactional dead-letter queues that match the *Name* parameter.

默认值是 PrivateAndPublic。

```yaml
Type: QueueType
Parameter Sets: (All)
Aliases:
Accepted values: PrivateAndPublic, Private, Public, SystemJournal, SystemDeadLetter, SystemTransactionalDeadLetter

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SubQueue
指定一个用于从主队列中获取数据的子队列对象。如果该子队列不存在，此cmdlet会隐式地创建它。问号（?）和星号（*）并不被视为通配符，而是子队列名称的一部分。

```yaml
Type: String
Parameter Sets: SubQueue
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### System.Object

## 备注

## 相关链接

[Clear-MsmqQueue](./Clear-MSMQQueue.md)

[New-MsmqQueue](./New-MsmqQueue.md)

[接收-MsmqQueue](./Receive-MsmqQueue.md)

[Remove-MsmqQueue](./Remove-MsmqQueue.md)

[Send-MsmqQueue](./Send-MsmqQueue.md)

[Set-MsmqQueue](./Set-MsmqQueue.md)
