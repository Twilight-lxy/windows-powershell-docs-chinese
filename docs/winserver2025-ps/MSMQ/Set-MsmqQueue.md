---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/set-msmqqueue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-MsmqQueue
---

# Set-MsmqQueue

## 摘要
设置队列的属性。

## 语法

```
Set-MsmqQueue -InputObject <MessageQueue[]> [-Label <String>] [-Authenticate <Boolean>] [-Journaling <Boolean>]
 [-QueueQuota <Int64>] [-JournalQuota <Int64>] [-PrivacyLevel <EncryptionRequired>]
 [-MulticastAddress <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-MsmqQueue` cmdlet 用于设置队列的属性。该 cmdlet 会返回一个表示已修改队列的 `MsmqQueue` 对象。您可以指定要修改的私有队列或公共队列。如果您指定了日志队列、系统日志队列、系统死信队列或系统事务性死信队列，该 cmdlet 会返回错误。

## 示例

### 示例 1：修改队列的属性
```
PS C:\> Get-MsmqQueue -Name "Order*" -QueueType Private | Set-MsmqQueue -Journaling:$true -QueueQuota 500000
```

这个命令使用 **Get-MsmqQueue** cmdlet 来获取名称以 “Order” 开头的私有队列。该命令通过管道运算符将查询结果传递给当前的 cmdlet。当前 cmdlet 会修改这些队列的日志记录功能以及队列配额的大小。

## 参数

### -Authenticate
表示该队列是否仅接受已通过身份验证的消息。没有默认值。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定一个包含 **MsmqQueue** 对象的数组。此 cmdlet 会修改该参数所指定的队列的属性。此参数支持管道输入（pipeline input）。

```yaml
Type: MessageQueue[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -JournalQuota
指定日志队列的最大大小。请以千字节（KB）为单位输入数值。该参数没有默认值。

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
该参数用于指示是否将接收到的消息复制到日志队列中。默认值为空（即不执行任何操作）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Label
指定一个标签。该参数所指定的标签用于描述队列。没有默认值。

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
指定与队列相关联的多播地址。该参数没有默认值。

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

### -PrivacyLevel
指定与队列相关的隐私级别。该字段没有默认值。

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
指定队列的最大大小（以千字节为单位）。该参数没有默认值。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Msmq.PowerShellcommands.MessageQueue[]

## 输出

### System.Object

## 备注

## 相关链接

[Clear-MsmqQueue](./Clear-MSMQQueue.md)

[Get-MsmqQueue](./Get-MsmqQueue.md)

[New-MsmqQueue](./New-MsmqQueue.md)

[接收-MsmqQueue](./Receive-MsmqQueue.md)

[Remove-MsmqQueue](./Remove-MsmqQueue.md)

[Send-MsmqQueue](./Send-MsmqQueue.md)

