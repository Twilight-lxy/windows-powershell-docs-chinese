---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/new-msmqmessage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-MsmqMessage
---

# New-MsmqMessage

## 摘要
创建一个消息对象。

## 语法

```
New-MsmqMessage [[-Body] <Object>] [-Recoverable] [-Authenticated] [-Journaling] [-Label <String>]
 [-AdminQueuePath <String>] [-AcknowledgeType <AcknowledgeTypes>] [-ResponseQueuePath <String>]
 [-TimeToReachQueue <TimeSpan>] [-TimeToBeReceived <TimeSpan>] [<CommonParameters>]
```

## 描述
`New-MsmqMessage` cmdlet 创建一个 `SystemMessaging.Message` 对象，该对象包含由参数指定的属性。

## 示例

#### 示例 1：创建一条测试消息
```
PS C:\> New-MsmqMessage -Body "Test Message" -AdminQueuePath ".\private$\adminqueue" -Recoverable
```

此命令会创建一条测试消息，并指定接收确认消息的队列。

## 参数

### -AcknowledgeType
指定消息队列（Messaging Queueing）可以返回的确认消息类型。

```yaml
Type: AcknowledgeTypes
Parameter Sets: (All)
Aliases:
Accepted values: None, PositiveArrival, PositiveReceive, NotAcknowledgeReachQueue, FullReachQueue, NegativeReceive, NotAcknowledgeReceive, FullReceive

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AdminQueuePath
指定一个路径。该路径所对应的队列会接收消息队列（Message Queuing）生成的确认消息。

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

### -Authenticated
表示该 cmdlet 以已认证的消息形式发送该信息。

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

### -Body
用于指定消息的正文内容。默认值为空字符串（即没有正文）。

```yaml
Type: Object
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Journaling
表示发送消息的计算机会在日志中保存该消息的副本。

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
用于指定一个标签。该参数所指定的标签用于描述消息的内容。默认值为空字符串。

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

### -Recoverable
表示该 cmdlet 设置了消息对象的可恢复（recoverable）属性。

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

### -ResponseQueuePath
指定一个路径。该参数所指向的队列用于接收应用程序生成的响应消息。

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

### -TimeToBeReceived
指定从目标队列接收消息的最大时间长度（以毫秒为单位）。默认值为 49.17:02:47.295。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases: TTBR

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TimeToReachQueue
指定消息到达队列的最大时间长度（以毫秒为单位）。默认值为 49.17:02:47.295。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases: TTRQ

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.Object

## 输出

### System.Object

## 备注

## 相关链接

[Move-MsmqMessage](./Move-MsmqMessage.md)

