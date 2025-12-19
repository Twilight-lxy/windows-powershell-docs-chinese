---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/set-msmqqueuemanager?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-MsmqQueueManager
---

# Set-MsmqQueueManager

## 摘要
配置队列管理器。

## 语法

### 全部（默认值）
```
Set-MsmqQueueManager [-RenewEncryptionKey] [-MsgStore <String>] [-MsgLogStore <String>]
 [-TransactionLogStore <String>] [-MessageQuota <Int64>] [-JournalQuota <Int64>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 连接
```
Set-MsmqQueueManager [-Connect] [-RenewEncryptionKey] [-MsgStore <String>] [-MsgLogStore <String>]
 [-TransactionLogStore <String>] [-MessageQuota <Int64>] [-JournalQuota <Int64>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 断开连接
```
Set-MsmqQueueManager [-Disconnect] [-RenewEncryptionKey] [-MsgStore <String>] [-MsgLogStore <String>]
 [-TransactionLogStore <String>] [-MessageQuota <Int64>] [-JournalQuota <Int64>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-MsmqQueueManager` cmdlet 用于配置消息队列（也称为 MSMQ）队列管理器的属性。该 cmdlet 会返回一个 `QueueManager` 对象，该对象表示已修改的本地队列管理者。如果您指定了 `RenewEncryptionKey` 参数来更新加密密钥，则必须重新启动消息队列服务，以便新密钥能够生效。

## 示例

### 示例 1：配置队列管理器
```
PS C:\> Set-MsmqQueueManager -MessageQuota 2048576 -MsgStore "C:\MSMQ\MessageFiles" -TransactionLogStore "C:\MSMQ\TransactionLogs"
```

此命令用于配置消息队列（Message Queuing）队列管理器的属性。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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

### -Connect
表示此 cmdlet 用于将计算机连接到网络和目录服务。如果您指定了该参数，则无法指定 *Disconnect* 参数。

```yaml
Type: SwitchParameter
Parameter Sets: Connect
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Disconnect
表示此 cmdlet 会断开计算机与网络以及目录服务的连接。如果您指定了此参数，则无法指定 *Connect* 参数。

```yaml
Type: SwitchParameter
Parameter Sets: Disconnect
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -JournalQuota
指定消息队列（Message Queuing）的总日志消息存储配额。

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

### -MessageQuota
指定消息队列（Message Queuing）的总消息存储配额。

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

### -MsgLogStore
这表明该 cmdlet 会更改消息记录器的存储位置，并将所有消息记录器文件移至新位置。

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

### -MsgStore
指定一个新的消息存储位置。该cmdlet会将所有消息文件移至新位置。

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

### -RenewEncryptionKey
表示此cmdlet用于更新公共加密密钥。

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

### -TransactionLogStore
指定一个新的事务日志存储位置。此命令行工具会将所有事务日志文件移动到新位置。

```yaml
Type: String
Parameter Sets: (All)
Aliases: XactLogStore

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Get-MsmqQueueManager](./Get-MsmqQueueManager.md)

