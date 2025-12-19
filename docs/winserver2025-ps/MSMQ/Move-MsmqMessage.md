---
description: 使用此主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/move-msmqmessage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Move-MsmqMessage
---

# 移动 MSMQ 消息

## 摘要
在子队列之间或主队列与子队列之间移动消息。

## 语法

```
Move-MsmqMessage -InputObject <MessageQueue> -DestinationQueue <MessageQueue> -Message <Message>
 [-Transactional] [<CommonParameters>]
```

## 描述
`Move-MsmqMessage` cmdlet 可以在同一队列的子队列之间，或者在主队列与其某个子队列之间移动消息。该 cmdlet 会返回一个表示被移动消息的 `Message` 对象。执行“移动”（Move）和“打开”（Open）操作时会隐式地创建子队列。你可以使用 `Get-MsmqQueue` cmdlet 来获取子队列的信息。

## 示例

### 示例 1：将消息移动到子队列中
```
PS C:\> $SrcQueue = Get-MsmqQueue -QueueType Private -Name "MyQueue"
PS C:\> $DstQueue = Get-MsmqQueue -QueueType Private -Name "MyQueue" -SubQueue "MySubqueue"
PS C:\> $Message = $SrcQueue | Receive-MsmqQueue -Peek
PS C:\> $SrcQueue | Move-MsmqMessage -DestinationQueue $DstQueue -Message $Message
```

第一个命令使用 `Get-MsmqQueue` cmdlet 创建了一个名为 `MyQueue` 的私有队列，并将结果存储在 `$SrcQueue` 变量中。

第二个命令使用 `Get-MsmqQueue` 获取一个名为 `MySubqueue` 的子队列。该子队列属于名为 `MyQueue` 的私有队列。该命令将结果存储在 `$DstQueue` 变量中。

第三个命令使用了 **Receive-MsmqQueue** cmdlet 从源队列中获取消息，并将其存储在 `$Message` 变量中。

最后的命令将 `$Message` 中的消息从源队列移动到目标队列。该目标队列是 `MyQueue` 的一个子队列。

## 参数

### -DestinationQueue
指定一个 `MsmqQueue` 对象，该对象表示用于移动消息的目标队列。目标队列可以是子队列，也可以是主队列。

```yaml
Type: MessageQueue
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
用于指定一个 **MsmqQueue** 对象。该 cmdlet 会将该参数所指定的源队列中的消息移动出去。源队列可以是一个子队列，也可以是一个主队列。此参数支持管道输入（pipeline input）。

```yaml
Type: MessageQueue
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Message
指定一个表示要移动的消息的 **Message** 对象。

```yaml
Type: Message
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Transactional
表示此cmdlet在事务上下文中移动消息。

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

### Microsoft.Msmq.PowerShellCommands.MessageQueue

## 输出

### System.Object

## 备注

## 相关链接

[Get-MsmqQueue](./Get-MsmqQueue.md)

[New-MsmqMessage](./New-MsmqMessage.md)

[接收-MsmqQueue](./Receive-MsmqQueue.md)

