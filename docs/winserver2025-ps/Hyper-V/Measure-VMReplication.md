---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/measure-vmreplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Measure-VMReplication
---

# 测量虚拟机复制性能（Measure-VMReplication）

## 摘要
获取与虚拟机相关的复制统计数据和信息。

## 语法

### VMName（默认值）
```
Measure-VMReplication [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [[-VMName] <String[]>] [-ReplicaServerName <String>] [-PrimaryServerName <String>]
 [-ReplicationState <VMReplicationState>] [-ReplicationHealth <VMReplicationHealthState>]
 [-ReplicationMode <VMReplicationMode>] [-ReplicationRelationshipType <VMReplicationRelationshipType>]
 [-TrustGroup <String>] [<CommonParameters>]
```

### VMObject
```
Measure-VMReplication [-VM] <VirtualMachine[]> [-ReplicationRelationshipType <VMReplicationRelationshipType>]
 [<CommonParameters>]
```

## 描述
`Measure-VMReplication` cmdlet 可获取与虚拟机相关的复制统计数据和信息。这些复制统计数据是根据通过 `Set-VMReplicationServer` cmdlet 指定的监控间隔，在预定的时间段内计算得出的。

## 示例

### 示例 1
```
PS C:\> Measure-VMReplication
```

这个示例会获取本地主机上所有正在进行复制的虚拟机的复制监控详细信息。

### 示例 2
```
PS C:\> Measure-VMReplication VM01
```

这个示例获取了名为VM01的虚拟机的复制监控详细信息。

### 示例 3
```
PS C:\>  Measure-VMReplication -ReplicationHealth Warning
```

这个示例获取了所有复制健康状态为“警告”的虚拟机的复制监控详细信息。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于获取复制统计信息的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全合格的域名进行标识。默认值是本地计算机。可以使用 “localhost” 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PrimaryServerName
指定主服务器的名称。所有虚拟机的复制统计信息均从指定的主服务器中获取。

```yaml
Type: String
Parameter Sets: VMName
Aliases: PrimaryServer

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicaServerName
指定要获取其复制统计信息的虚拟机副本服务器的名称。

```yaml
Type: String
Parameter Sets: VMName
Aliases: ReplicaServer

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicationHealth
指定您想要获取复制统计信息的虚拟机的复制健康状态。有效值有“Critical”（严重）、“Warning”（警告）、“Normal”（正常）和“NotApplicable”（不适用）。

```yaml
Type: VMReplicationHealthState
Parameter Sets: VMName
Aliases: Health
Accepted values: NotApplicable, Normal, Warning, Critical

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicationMode
指定您希望获取复制统计信息的虚拟机的复制模式。有效值为 “None”、“Primary”、“Replica”、“TestReplica” 和 “ExtendedReplica”。

```yaml
Type: VMReplicationMode
Parameter Sets: VMName
Aliases: Mode
Accepted values: None, Primary, Replica, TestReplica, ExtendedReplica

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicationRelationshipType
用于指定虚拟机的复制关系类型。需要明确该复制关系是属于简单的主从结构，还是扩展的复制链结构。此cmdlet会获取与具有所指定复制类型的虚拟机相关的复制统计数据和信息。

```yaml
Type: VMReplicationRelationshipType
Parameter Sets: (All)
Aliases: Relationship
Accepted values: Simple, Extended

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicationState
指定您希望获取复制统计信息的虚拟机的复制状态。有效值包括：

- Error
- FailOverWaitingCompletion
- FailedOver
- NotApplicable
- ReadyForInitialReplication
- Replicating
- Resynchronizing
- ResynchronizeSuspended
- Suspended
- SyncedReplicationComplete
- WaitingForInitialReplication
- WaitingForStartResynchronize

```yaml
Type: VMReplicationState
Parameter Sets: VMName
Aliases: State
Accepted values: Disabled, ReadyForInitialReplication, InitialReplicationInProgress, WaitingForInitialReplication, Replicating, PreparedForFailover, FailedOverWaitingCompletion, FailedOver, Suspended, Error, WaitingForStartResynchronize, Resynchronizing, ResynchronizeSuspended, RecoveryInProgress, FailbackInProgress, FailbackComplete, WaitingForUpdateCompletion, UpdateError, WaitingForRepurposeCompletion, PreparedForSyncReplication, PreparedForGroupReverseReplication, FiredrillInProgress

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TrustGroup
指定一个与虚拟机关联的信任组，您希望获取该虚拟机的复制统计信息。

```yaml
Type: String
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定您想要获取复制统计信息的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定您希望获取虚拟机复制统计信息的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases: Name

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMReplicationHealth

## 备注

## 相关链接

