---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/set-msmqqueueacl?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-MsmqQueueACL
---

# Set-MsmqQueueACL

## 摘要
修改队列的访问权限。

## 语法

```
Set-MsmqQueueACL [-InputObject] <MessageQueue[]> -UserName <String[]> [-Allow <MessageQueueAccessRights>]
 [-Deny <MessageQueueAccessRights>] [-Remove <MessageQueueAccessRights>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-MsmqQueueACL` cmdlet 用于修改队列的访问权限。该 cmdlet 会返回一个更新后的 `MsmqQueueAcl` 对象，并能够修改私有队列、公共队列、日志队列、系统日志队列、系统死信队列以及系统事务性死信队列的权限设置。

## 示例

### 示例 1：修改按名称指定的队列的访问控制列表（ACL）
```powershell
PS C:\> $queue = Get-MsmqQueue -Name "Order*" -QueueType Private
PS C:\> $rights = "DeleteQueue", "PeekMessage", "ReceiveMessage", "WriteMessage"
PS C:\> $rights | Foreach-Object { Set-MsmqQueueAcl -InputObject $queue -UserName "CONTOSO\DavidChew" -Allow $PSItem}
PS C:\> Set-MsmqQueueAcl -InputObject $queue -UserName "CONTOSO\DavidChew" -Deny TakeQueueOwnership
```

该命令使用 **Get-MsmqQueue** cmdlet 获取所有名称以 “Order” 开头的私有队列。此 cmdlet 会修改这些队列的访问控制列表（ACL）。

## 参数

### -Allow
指定一个权限数组，该cmdlet会将这些权限授予用户账户或组。

此参数的可接受值为：

- DeleteQueue - Delete the specified queue
- FullControl - Full control of the specified queue
- GetQueuePermissions - Get the permissions of the specified queue
- GetQueueProperties - Get the properties of the specified queue
- ReceiveJournalMessage - Receive messages from the journal queue. This includes the rights to delete and peek messages from the journal queue
- DeleteJournalMessage - Delete messages from the journal queue
- PeekMessage - Peek a message from the specified queue
- ReceiveMessage - Receive messages from the queue. This includes the rights to delete and peek messages
- WriteMessage - Send a message to the specified queue
- DeleteMessage - Delete a message from the specified queue
- ChangeQueuePermissions - Set the permissions of the specified queue
- SetQueueProperties - Set the properties of the specified queue
- TakeQueueOwnership - Assign the specified queue to oneself
- GenericRead - A combination of `GetQueueProperties`, `GetQueuePermissions`, `ReceiveMessage`, and `ReceiveJournalMessage`
- GenericWrite - A combination of `GetQueueProperties`, `GetQueuePermissions`, and `WriteMessage`

```yaml
Type: MessageQueueAccessRights
Parameter Sets: (All)
Aliases:
Accepted values: DeleteMessage, PeekMessage, ReceiveMessage, WriteMessage, DeleteJournalMessage, ReceiveJournalMessage, SetQueueProperties, GetQueueProperties, DeleteQueue, GetQueuePermissions, GenericWrite, GenericRead, ChangeQueuePermissions, TakeQueueOwnership, FullControl

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
Prompts you for confirmation before running the cmdlet.

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

### -Deny
Specifies an array of permissions that the cmdlet revokes from a user account or group.

此参数的可接受值为：

- DeleteQueue - Delete the specified queue
- FullControl - Full control of the specified queue
- GetQueuePermissions - Get the permissions of the specified queue
- GetQueueProperties - Get the properties of the specified queue
- ReceiveJournalMessage - Receive messages from the journal queue. This includes the rights to delete and peek messages from the journal queue
- DeleteJournalMessage - Delete messages from the journal queue
- PeekMessage - Peek a message from the specified queue
- ReceiveMessage - Receive messages from the queue. This includes the rights to delete and peek messages
- WriteMessage - Send a message to the specified queue
- DeleteMessage - Delete a message from the specified queue
- ChangeQueuePermissions - Set the permissions of the specified queue
- SetQueueProperties - Set the properties of the specified queue
- TakeQueueOwnership - Assign the specified queue to oneself
- GenericRead - A combination of `GetQueueProperties`, `GetQueuePermissions`, `ReceiveMessage`, and `ReceiveJournalMessage`
- GenericWrite - A combination of `GetQueueProperties`, `GetQueuePermissions`, and `WriteMessage`

```yaml
Type: MessageQueueAccessRights
Parameter Sets: (All)
Aliases:
Accepted values: DeleteMessage, PeekMessage, ReceiveMessage, WriteMessage, DeleteJournalMessage, ReceiveJournalMessage, SetQueueProperties, GetQueueProperties, DeleteQueue, GetQueuePermissions, GenericWrite, GenericRead, ChangeQueuePermissions, TakeQueueOwnership, FullControl

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
Specifies an array of **MsmqQueue** objects.
This cmdlet updates permissions for the queues that the **MsmqQueue** objects specify.
This parameter accepts pipeline input.

```yaml
Type: MessageQueue[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Remove
Specifies an array of permissions that this cmdlet removes from a user account or group.

此参数的可接受值为：

- DeleteQueue - Delete the specified queue
- FullControl - Full control of the specified queue
- GetQueuePermissions - Get the permissions of the specified queue
- GetQueueProperties - Get the properties of the specified queue
- ReceiveJournalMessage - Receive messages from the journal queue. This includes the rights to delete and peek messages from the journal queue
- DeleteJournalMessage - Delete messages from the journal queue
- PeekMessage - Peek a message from the specified queue
- ReceiveMessage - Receive messages from the queue. This includes the rights to delete and peek messages
- WriteMessage - Send a message to the specified queue
- DeleteMessage - Delete a message from the specified queue
- ChangeQueuePermissions - Set the permissions of the specified queue
- SetQueueProperties - Set the properties of the specified queue
- TakeQueueOwnership - Assign the specified queue to oneself
- GenericRead - A combination of `GetQueueProperties`, `GetQueuePermissions`, `ReceiveMessage`, and `ReceiveJournalMessage`
- GenericWrite - A combination of `GetQueueProperties`, `GetQueuePermissions`, and `WriteMessage`

```yaml
Type: MessageQueueAccessRights
Parameter Sets: (All)
Aliases:
Accepted values: DeleteMessage, PeekMessage, ReceiveMessage, WriteMessage, DeleteJournalMessage, ReceiveJournalMessage, SetQueueProperties, GetQueueProperties, DeleteQueue, GetQueuePermissions, GenericWrite, GenericRead, ChangeQueuePermissions, TakeQueueOwnership, FullControl

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UserName
指定该cmdlet要更改权限的用户账户或组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

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
此 cmdlet 支持以下常见参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Msmq.PowerShellcommands.MessageQueue[]

## 输出

### System.Object

## 备注

## 相关链接

[Get-MsmqQueue](./Get-MsmqQueue.md)

[Get-MsmqQueueACL](./Get-MsmqQueueACL.md)

