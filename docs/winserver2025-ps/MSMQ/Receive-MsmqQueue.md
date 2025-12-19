---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/receive-msmqqueue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Receive-MsmqQueue
---

# 接收 MSMQ 队列消息

## 摘要
从队列中进行破坏性读取（即修改队列中的数据）。

## 语法

### 事务型（默认设置）
```
Receive-MsmqQueue -InputObject <MessageQueue> [-Transactional] [-RetrieveBody] [-Timeout <TimeSpan>]
 [-Count <Int32>] [<CommonParameters>]
```

### 快看
```
Receive-MsmqQueue -InputObject <MessageQueue> [-Peek] [-RetrieveBody] [-Timeout <TimeSpan>] [-Count <Int32>]
 [<CommonParameters>]
```

## 描述
`Receive-MsmqQueue` cmdlet 会从队列中读取数据（这种操作属于“破坏性读取”，即数据在被读取后会被清除）。该 cmdlet 会返回一个 `System.Messaging.Message` 对象。该 cmdlet 支持为 `Name` 参数指定路径名、格式名称或直接格式名称等值。某些其他与消息队列（也称为 MSMQ）相关的 cmdlet 需要为队列提供一个友好的名称。如果指定了 `Peek` 参数，该 cmdlet 会仅查看队列中的消息内容而不会实际读取数据。只要返回了至少一条消息，该 cmdlet 就视为操作成功。

如果您指定了 **Peek** 参数，此cmdlet将返回消息的数量，该数量是 **Count** 参数提供的数值与队列中实际消息数量的较小值。

## 示例

#### 示例 1：执行带事务处理的读取操作
```powershell
PS C:\> Get-MsmqQueue -Name "a04bm10\private$\order_queue" | Receive-MsmqQueue -Transactional
```

此命令使用 **Get-MsmqQueue** cmdlet 来获取指定的队列。该命令通过管道运算符将结果传递给当前的 cmdlet。当前 cmdlet 对该队列执行事务性读取操作。

## 参数

### -Count
指定要返回的消息数量。默认值为 1。您必须指定一个大于 0 的值。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
用于指定一个 **MessageQueue** 对象。该 cmdlet 会从该 **MessageQueue** 指定的队列中读取数据。此参数支持管道输入（pipeline input）。

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

### -Peek
表示此cmdlet会返回队列中第一条消息的副本，而不会将该消息从队列中删除。

```yaml
Type: SwitchParameter
Parameter Sets: Peek
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RetrieveBody
表示此cmdlet会返回消息的正文内容。

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

### -Timeout
指定等待队列中包含消息的最大时间（以毫秒为单位）。默认值为 0。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Transactional
表示该cmdlet执行了一个带事务处理的接收操作（即接收数据的过程会包含事务管理机制）。

```yaml
Type: SwitchParameter
Parameter Sets: Transactional
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Msmq POWERShell Commands.MessageQueue

## 输出

### System.Object

## 备注

## 相关链接

[Clear-MsmqQueue](./Clear-MSMQQueue.md)

[Get-MsmqQueue](./Get-MsmqQueue.md)

[New-MsmqQueue](./New-MsmqQueue.md)

[Remove-MsmqQueue](./Remove-MsmqQueue.md)

[Send-MsmqQueue](./Send-MsmqQueue.md)

[Set-MsmqQueue](./Set-MsmqQueue.md)

