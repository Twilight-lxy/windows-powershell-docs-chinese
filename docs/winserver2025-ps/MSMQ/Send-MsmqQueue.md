---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/send-msmqqueue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Send-MsmqQueue
---

# Send-MsmqQueue

## 摘要
向远程队列发送一条测试消息。

## 语法

### 名称（默认值）
```
Send-MsmqQueue [-Name] <String> [-MessageObject <Message>] [-Body <Object>] [-Label <String>] [-Recoverable]
 [-Authenticated] [-Journaling] [-Transactional] [-AcknowledgeType <AcknowledgeTypes>]
 [-AdminQueuePath <String>] [-ResponseQueuePath <String>] [-TimeToReachQueue <TimeSpan>]
 [-TimeToBeReceived <TimeSpan>] [<CommonParameters>]
```

### InputObject
```
Send-MsmqQueue -InputObject <MessageQueue[]> [-MessageObject <Message>] [-Body <Object>] [-Label <String>]
 [-Recoverable] [-Authenticated] [-Journaling] [-Transactional] [-AcknowledgeType <AcknowledgeTypes>]
 [-AdminQueuePath <String>] [-ResponseQueuePath <String>] [-TimeToReachQueue <TimeSpan>]
 [-TimeToBeReceived <TimeSpan>] [<CommonParameters>]
```

## 描述
`Send-MsmqQueue` cmdlet 可以向一个或多个远程队列发送测试消息。该 cmdlet 允许为 `Name` 参数输入路径名、格式名称或直接格式名称作为值。某些其他与 Message Queuing（也称为 MSMQ）相关的 cmdlet 需要为队列提供一个友好的名称。默认情况下，此 cmdlet 会发送简单类型的消息，并返回一个表示所发送消息的 `System.Messaging.Message` 对象。

## 示例

### 示例 1：向队列发送一条测试消息
```
PS C:\> Get-MsmqQueue -Name "a04bm10\private$\order_queue" | Send-MsmqQueue -AdminQueuePath ".\private$\admin_queue" -Recoverable -Transactional
```

该命令使用 **Get-MsmqQueue** cmdlet 获取具有指定名称的队列。然后，通过管道运算符将结果传递给当前的 cmdlet。当前 cmdlet 会向该队列发送一条测试消息，并指定这条消息的属性。

### 示例 2：向队列发送一条带有标签的测试消息
```
PS C:\> Get-MsmqQueue -Name "FormatName:DIRECT=TCP:10.199.37.61\order_queue" | Send-MsmqQueue -Label "From PowerShell" -Transactional
```

该命令使用 `Get-MsmqQueue` 获取具有指定名称的队列。命令通过管道运算符将结果传递给当前的 cmdlet（脚本片段）。当前 cmdlet 会向该队列发送一条测试消息，这条测试消息包含一个标签。

## 参数

### -AcknowledgeType
指定消息队列（Messageing Queuing）可以返回的确认消息类型。

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
指定一个路径。该路径所指向的队列会接收消息队列（Message Queuing）生成的确认消息。

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
表示该cmdlet以已认证的消息形式发送该消息。

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
指定消息的正文内容。该 cmdlet 会将该参数所指定的正文内容包含在消息中，并将这些消息发送到队列中。

```yaml
Type: Object
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定一个 **MessageQueue** 对象数组。此 cmdlet 将消息发送到由这些 **MessageQueue** 对象指定的目标队列中。该参数支持管道输入（pipeline input）。

```yaml
Type: MessageQueue[]
Parameter Sets: InputObject
Aliases:

Required: True
Position: Named
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

### -MessageObject
指定一个预先构建的消息对象，您可以将其作为管道输入来使用。

```yaml
Type: Message
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个名称。

```yaml
Type: String
Parameter Sets: Name
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Recoverable
表示该cmdlet将消息作为可恢复的消息进行发送。

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
指定一个路径。该参数所指定的队列用于接收应用程序生成的响应消息。

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

### -Transactional
表示此cmdlet会将该消息作为事务性消息发送。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Msmq POWERShellCommands.MessageQueue[]

## 输出

### System.Object

## 备注

## 相关链接

[Clear-MsmqQueue](./Clear-MSMQQueue.md)

[Get-MsmqQueue](./Get-MsmqQueue.md)

[New-MsmqQueue](./New-MsmqQueue.md)

[接收 Msmq 队列](./Receive-MsmqQueue.md)

[Remove-MsmqQueue](./Remove-MsmqQueue.md)

[Set-MsmqQueue](./Set-MsmqQueue.md)

