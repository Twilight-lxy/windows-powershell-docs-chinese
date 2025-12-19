---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/set-msmqqueuemanageracl?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-MsmqQueueManagerACL
---

# Set-MsmqQueueManagerACL

## 摘要
修改队列管理器的访问权限。

## 语法

```
Set-MsmqQueueManagerACL -UserName <String[]> [-Allow <QueueManagerAccessRights>]
 [-Deny <QueueManagerAccessRights>] [-Remove <QueueManagerAccessRights>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-MsmqQueueManagerACL` cmdlet 用于修改本地队列管理器的访问权限。该 cmdlet 会返回更新后的 `MsmqQueueManagerAcl` 对象。

## 示例

### 示例 1：修改本地队列管理器的访问权限
```
PS C:\> Set-MsmqQueueManagerAcl -UserName "CONTOSO\DavidChew" -Allow DeleteMessage,PeekMessage -Deny TakeOwnership,SetPermissions
```

此命令会修改本地队列管理器的访问权限。

## 参数

### -Allow
指定此 cmdlet 授予用户账户或组的权限数组。该参数的可接受值为：

- AllExtendedRights.
All extended rights for the specified queue manager.
- CreateChildObjects.
Create child objects with the specified queue manager.
- CreateQueue.
Create a queue with the specified queue manager.
- Delete.
Delete queues of the specified queue manager.
- DeleteChildObjects.
Delete child objects from the specified queue manager.
- FullControl.
Full control of the specified queue manager.
- GetPermissions.
Get the permissions of the specified queue manager.
- GetProperties.
Get the properties of the specified queue manager.
- ListContent.
List content stored in the queues of the specified queue manager.
- PeekDeadLetter.
Peek a message from the specified queue manager system dead letter queue and transactional dead letter queue.
- PeekJournal.
Peek a message from the specified queue manager system journal queue.
- ReceiveDeadLetter.
Receive a message from the specified queue manager system dead letter queue and transactional dead letter queue.
- ReceiveJournal.
Receive a message from the specified queue manager system journal queue.
- SetPermissions.
Set the permissions of the specified queue manager.
- SetProperties.
Set the properties of the specified queue manager.
- TakeOwnership.
Assign a queue of the specified queue manager to oneself.

```yaml
Type: QueueManagerAccessRights
Parameter Sets: (All)
Aliases:
Accepted values: FullControl, CreateQueue, ReceiveDeadLetter, ReceiveComputerJournal, GetProperties, SetProperties, GetPermissions, SetPermissions, TakeOwnership, Delete, PeekDeadLetter, PeekComputerJournal, AllExtendedRights, CreateAllChildObjects, DeleteAllChildObjects, ListObjects

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
The acceptable values for this parameter are:

- AllExtendedRights.
All extended rights for the specified queue manager.
- CreateChildObjects.
Create child objects with the specified queue manager.
- CreateQueue.
Create a queue with the specified queue manager.
- Delete.
Delete queues of the specified queue manager.
- DeleteChildObjects.
Delete child objects from the specified queue manager.
- FullControl.
Full control of the specified queue manager.
- GetPermissions.
Get the permissions of the specified queue manager.
- GetProperties.
Get the properties of the specified queue manager.
- ListContent.
List content stored in the queues of the specified queue manager.
- PeekDeadLetter.
Peek a message from the specified queue manager system dead letter queue and transactional dead letter queue.
- PeekJournal.
Peek a message from the specified queue manager system journal queue.
- ReceiveDeadLetter.
Receive a message from the specified queue manager system dead letter queue and transactional dead letter queue.
- ReceiveJournal.
Receive a message from the specified queue manager system journal queue.
- SetPermissions.
Set the permissions of the specified queue manager.
- SetProperties.
Set the properties of the specified queue manager.
- TakeOwnership.
Assign a queue of the specified queue manager to oneself.

```yaml
Type: QueueManagerAccessRights
Parameter Sets: (All)
Aliases:
Accepted values: FullControl, CreateQueue, ReceiveDeadLetter, ReceiveComputerJournal, GetProperties, SetProperties, GetPermissions, SetPermissions, TakeOwnership, Delete, PeekDeadLetter, PeekComputerJournal, AllExtendedRights, CreateAllChildObjects, DeleteAllChildObjects, ListObjects

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Remove
Specifies an array of permissions that this cmdlet removes from a user account or group.
The acceptable values for this parameter are:

- AllExtendedRights.
All extended rights for the specified queue manager.
- CreateChildObjects.
Create child objects with the specified queue manager.
- CreateQueue.
Create a queue with the specified queue manager.
- Delete.
Delete queues of the specified queue manager.
- DeleteChildObjects.
Delete child objects from the specified queue manager.
- FullControl.
Full control of the specified queue manager.
- GetPermissions.
Get the permissions of the specified queue manager.
- GetProperties.
Get the properties of the specified queue manager.
- ListContent.
List content stored in the queues of the specified queue manager.
- PeekDeadLetter.
Peek a message from the specified queue manager system dead letter queue and transactional dead letter queue.
- PeekJournal.
Peek a message from the specified queue manager system journal queue.
- ReceiveDeadLetter.
Receive a message from the specified queue manager system dead letter queue and transactional dead letter queue.
- ReceiveJournal.
Receive a message from the specified queue manager system journal queue.
- SetPermissions.
Set the permissions of the specified queue manager.
- SetProperties.
Set the properties of the specified queue manager.
- TakeOwnership.
Assign a queue of the specified queue manager to oneself.

```yaml
Type: QueueManagerAccessRights
Parameter Sets: (All)
Aliases:
Accepted values: FullControl, CreateQueue, ReceiveDeadLetter, ReceiveComputerJournal, GetProperties, SetProperties, GetPermissions, SetPermissions, TakeOwnership, Delete, PeekDeadLetter, PeekComputerJournal, AllExtendedRights, CreateAllChildObjects, DeleteAllChildObjects, ListObjects

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
展示了如果该cmdlet运行会发生什么情况。但实际上该cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Get-MsmqQueueManagerACL](./Get-MsmqQueueManagerACL.md)

