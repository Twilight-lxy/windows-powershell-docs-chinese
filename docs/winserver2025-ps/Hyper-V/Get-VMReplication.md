---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmreplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMReplication
---

# Get-VMReplication

## 摘要
获取虚拟机的复制设置信息。

## 语法

### VMName（默认值）
```
Get-VMReplication [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [[-VMName] <String[]>] [-ReplicaServerName <String>] [-PrimaryServerName <String>]
 [-ReplicationState <VMReplicationState>] [-ReplicationHealth <VMReplicationHealthState>]
 [-ReplicationMode <VMReplicationMode>] [-ReplicationRelationshipType <VMReplicationRelationshipType>]
 [-TrustGroup <String>] [<CommonParameters>]
```

### VMObject
```
Get-VMReplication [-VM] <VirtualMachine[]> [-ReplicationRelationshipType <VMReplicationRelationshipType>]
 [<CommonParameters>]
```

## 描述
`Get-VMReplication` cmdlet 可以获取虚拟机的复制设置信息。

## 示例

### 示例 1
```
PS C:\> Get-VMReplication
```

这个示例获取了本地Hyper-V主机上所有启用复制功能的虚拟机的复制设置信息。

### 示例 2
```
PS C:\> Get-VMReplication VM01
```

这个示例获取了名为VM01的虚拟机的复制设置信息。

### 示例 3
```
PS C:\> Get-VMReplication -ReplicaServerName server01.domain01.contoso.com
```

这个示例获取了所有正在复制到服务器 server01.domain01.contoso.com 的虚拟机的复制设置。

### 示例 4
```
PS C:\> Get-VMReplication -ReplicationState Replicating
```

这个示例获取了所有处于“复制中”状态的虚拟机的复制设置信息。

### 示例 5
```
PS C:\> Get-VMReplication -TrustGroup DEFAULT
```

这个示例获取了名为 DEFAULT 的信任组中所有虚拟机的复制设置。

### 示例 6
```
PS C:\> Get-VMReplication -ReplicationMode Primary
```

这个示例获取了本地主机上所有主虚拟机的复制设置信息。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。您可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个或多个 Hyper-V 主机，以从中检索虚拟机的复制设置。允许使用 NetBIOS 名称、IP 地址和完全限定域名作为主机标识。默认值为本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

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
指定要检索其复制设置的信息的虚拟机的主要服务器。

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
指定要获取复制设置的虚拟机的副本服务器名称。

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
获取具有指定复制健康状态的虚拟机的复制设置。有效值为 Normal（正常）、Warning（警告）和 Critical（严重）。

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
获取具有指定复制模式的虚拟机的复制设置。有效值包括：None（无）、Primary（主节点）、Replica（副本节点）和TestReplica（测试复制节点）。

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
指定虚拟机的复制关系类型。需要明确该复制关系是属于简单的主从结构，还是扩展的复制链结构。此cmdlet会获取具有所指定复制类型的虚拟机的相应复制设置信息。

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
获取具有指定复制状态的虚拟机的复制设置。有效值包括：

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
指定您想要检索复制设置的虚拟机的信任组。

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
指定要获取其复制设置信息的虚拟机。

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
指定要获取其复制设置信息的虚拟机的名称。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMReplication

## 备注

## 相关链接

