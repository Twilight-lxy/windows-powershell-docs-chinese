---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/new-msmqqueue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-MsmqQueue
---

# New-MsmqQueue

## 摘要
创建公共或私有的队列。

## 语法

```
New-MsmqQueue [-Name] <String[]> [-QueueType <MSMQQueueType>] [-Transactional] [-Label <String>]
 [-Authenticate] [-Journaling] [-QueueQuota <Int64>] [-JournalQuota <Int64>]
 [-PrivacyLevel <EncryptionRequired>] [-MulticastAddress <String>] [<CommonParameters>]
```

## 描述
`New-MsmqQueue` cmdlet 可用于创建公共或私有队列。该 cmdlet 会返回表示新队列的 `System Messaging.MessageQueue` 对象。如果未指定 `QueueType` 参数，cmdlet 将创建一个私有队列。

## 示例

### 示例 1：创建一个公共队列
```
PS C:\> New-MsmqQueue -Name "OrderQueue" -QueueType Public
```

此命令创建了一个名为“OrderStatus”的公共队列。

### 示例 2：为已认证的消息创建一个私有队列
```
PS C:\> New-MsmqQueue -Name "OrderQueue" -Authenticate -MulticastAddress "234.12.3:8001" -QueueQuota 200000
```

这个命令创建了一个名为 OrderQueue 的私有队列。该队列仅接受经过身份验证的消息。命令还指定了队列的容量（即允许存储的最大消息数量）。

## 参数

### -Authenticate
表示该队列仅接受已认证的消息。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -JournalQuota
指定日志队列的最大大小。请以千字节为单位输入数值。如果未指定数值，此cmdlet将使用默认的日志队列配额。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Journaling
表示接收到的消息会被复制到日志队列中。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Label
用于指定一个标签。该参数所指定的标签用于描述相应的队列。默认值为空字符串。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MulticastAddress
指定与队列关联的多播地址。如果您不指定多播地址，该cmdlet将不会为此队列分配多播地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个队列名称数组。该参数用于为队列提供友好的名称（即易于理解的名称）。此参数不支持通配符字符。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PrivacyLevel
指定与队列相关的隐私级别。默认值为“可选”（Optional）。

```yaml
Type: EncryptionRequired
Parameter Sets: (All)
Aliases:
Accepted values: None, Optional, Body

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -QueueQuota
指定队列的最大大小（以千字节为单位）。如果您没有指定值，此cmdlet将使用默认的队列配额。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -QueueType
指定队列类型。该参数的可接受值如下：

- Private.
The cmdlet creates a private queue with the name that the *Name* parameter specifies.
- Public.
The cmdlet creates a public queue with the name that the *Name* parameter specifies.

默认值是“Private”（私密的）。

```yaml
Type: MSMQQueueType
Parameter Sets: (All)
Aliases:
Accepted values: Private, Public

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Transactional
表示该cmdlet会在指定的路径创建一个事务性队列。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### System.Object

## 备注

## 相关链接

[Clear-MsmqQueue](./Clear-MSMQQueue.md)

[Get-MsmqQueue](./Get-MsmqQueue.md)

[接收-MsmqQueue](./Receive-MsmqQueue.md)

[Remove-MsmqQueue](./Remove-MsmqQueue.md)

[Send-MsmqQueue](./Send-MsmqQueue.md)

[Set-MsmqQueue](./Set-MsmqQueue.md)

