---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmsnapshot?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMSnapshot
---

# Get-VMSnapshot

## 摘要
获取与虚拟机关联的检查点（snapshot）信息。

## 语法

### VMName（默认值）
```
Get-VMSnapshot [-VMName] <String[]> [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [[-Name] <String>] [-SnapshotType <SnapshotType>] [<CommonParameters>]
```

### VMObject
```
Get-VMSnapshot [-VM] <VirtualMachine[]> [[-Name] <String>] [-SnapshotType <SnapshotType>] [<CommonParameters>]
```

### ID
```
Get-VMSnapshot [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Id] <Guid> [<CommonParameters>]
```

### 父级（Parent）
```
Get-VMSnapshot [[-Name] <String>] -ParentOf <VirtualMachineBase> [-SnapshotType <SnapshotType>]
 [<CommonParameters>]
```

### 子节点（Child）
```
Get-VMSnapshot [[-Name] <String>] -ChildOf <VMSnapshot> [-SnapshotType <SnapshotType>] [<CommonParameters>]
```

## 描述
`Get-VMSnapshot` cmdlet 可以获取与虚拟机或检查点关联的所有快照（checkpoint）。

注意：在 Windows Server 2012 R2 中，虚拟机快照被重新命名为“虚拟机检查点”。为便于理解，本文档将把虚拟机快照称为“检查点”。

## 示例

### 示例 1
```
PS C:\> Get-VMSnapshot -VMName TestVM
```

获取虚拟机 TestVM 的所有检查点信息。

### 示例 2
```
PS C:\> Get-VM -Name TestVM | Get-VMSnapshot -SnapshotType Standard
```

获取虚拟机TestVM的所有标准检查点信息。

### 示例 3
```
PS C:\> $snapshot = Get-VMSnapshot -Name 'Before applying updates' -VMName TestVM


PS C:\> Get-VMSnapshot -ParentOf $snapshot
```

在应用虚拟机TestVM的更新之前，获取该检查点的直接父级节点。

### 示例 4
```
PS C:\> $snapshot = Get-VMSnapshot -Name 'Before applying updates' -VMName TestVM


PS C:\> Get-VMSnapshot -ChildOf $snapshot
```

在应用对虚拟机 TestVM 的更新之前，获取该检查点（checkpoint）的直接子检查点（child checkpoints）。

## 参数

### -ChildOf
指定要获取其子检查点的检查点。这里仅获取直接的子检查点。

```yaml
Type: VMSnapshot
Parameter Sets: Child
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VMName, Id
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于检索检查点的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址或完全限定的域名作为主机标识。默认值为本地计算机；可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName, Id
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值是当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName, Id
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Id
指定要检索其检查点的虚拟机的唯一标识符。

```yaml
Type: Guid
Parameter Sets: Id
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Name
指定要检索的检查点的名称。

```yaml
Type: String
Parameter Sets: VMName, VMObject, Parent, Child
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ParentOf
指定要检索其直接父检查点的那个检查点。

```yaml
Type: VirtualMachineBase
Parameter Sets: Parent
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SnapshotType
指定要检索的检查点的类型。允许的值包括 **Standard**（标准）、**Recovery**（恢复）、**Planned**（计划中的）、**Missing**（缺失的）、**Replica**（副本）、**AppConsistentReplica**（应用程序一致性副本）和 **SyncedReplica**（同步副本）。

```yaml
Type: SnapshotType
Parameter Sets: VMName, VMObject, Parent, Child
Aliases: VMRecoveryCheckpoint
Accepted values: Standard, Recovery, Planned, Missing, Replica, AppConsistentReplica, SyncedReplica

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要检索其检查点的虚拟机。

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
指定要检索其检查点的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMSnapshot

## 备注

## 相关链接

