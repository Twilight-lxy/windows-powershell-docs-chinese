---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/23/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/suspend-clusternode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Suspend-ClusterNode
---

# 暂停集群节点（Suspend-ClusterNode）

## 摘要
暂停故障转移集群节点上的所有活动，即让该节点进入休眠状态。

## 语法

```
Suspend-ClusterNode [[-Name] <StringCollection>] [-Drain] [-ForceDrain] [-Wait]
 [[-TargetNode] <String>] [-InputObject <PSObject>] [-Cluster <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Suspend-ClusterNode` cmdlet 用于暂停故障转移集群节点上的所有活动，即使该节点进入休眠状态。如果使用了 `Drain` 参数，在节点被暂停之前，当前在该节点上运行的集群角色将会被关闭（即它们的资源会被释放）。

暂停或中止一个节点通常是在对该节点应用软件更新时进行的。如果你需要对某个集群节点进行全面的诊断或维护操作，那么直接停止该节点上的集群服务（而不是仅仅将其置于暂停状态）可能会更加方便和高效。

## 示例

#### 示例 1：暂停本地集群中的一个节点

```powershell
Suspend-ClusterNode -Name "node1"
```

这个示例会暂停本地集群中名为 `node1` 的节点。

### 示例 2：暂停集群中的一个节点

```powershell
Suspend-ClusterNode "node2" -Cluster "cluster2"
```

这个例子会暂停名为 `node2` 的节点在名为 `cluster2` 的集群中的运行。

### 示例 3：暂停一个节点并迁移其工作负载

```powershell
Suspend-ClusterNode -Name "node1" -Target "node2" -Drain
```

这个示例会暂停名为 `node1` 的节点，并将其上的工作负载转移到名为 `node2` 的节点上。

### 示例 4：预览暂停操作

```powershell
Suspend-ClusterNode node1 -Drain -WhatIf
```

这个示例展示了将对名为`node1`的节点执行的操作的预览结果。

## 参数

### -Cluster

指定要运行此cmdlet的集群名称。如果该参数的输入为`.`或被省略，则cmdlet将在本地集群上运行。

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

### -Drain

该方案确保所有工作负载都能优雅地迁移到其他节点上，同时保持最高的可用性，并采用最优的调度策略。

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

### -ForceDrain

-ForceDrain开关与-Drain开关配合使用，可以确保所有工作负载安全地迁移到其他节点上，同时保持最高的可用性，并运用最优的节点分配策略。

如果某些或所有工作负载无法安全地迁移，那么那些发生故障的工作负载将会被停止，并迁移到另一个节点上（在该节点上以“失败状态”存在）。此后，该节点将被强制进入暂停状态。

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

### -InputObject

指定要挂起的集群节点（可选择是否执行数据清理操作），或者指定用于运行该命令行的集群。

```yaml
Type: PSObject
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name

指定要暂停的集群节点的名称，可以选择是否进行数据清理（draining）。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetNode

指定一个用于接收工作负载的节点。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Wait

指定等待该cmdlet完成所需的时间（以秒为单位）。如果未指定**Wait**参数，那么将立即启动调用，且cmdlet会立即返回结果而不会进行等待；如果指定了一个值为0的**Wait**参数，同样也会立即启动调用，但cmdlet会在完成后返回结果。

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

### -WhatIf

展示了如果运行该 cmdlet 会发生什么情况。但实际上并没有运行该 cmdlet。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell.Cluster

### Microsoft FailoverClusters PowerShell ClusterNode

## 输出

### Microsoft FailoverClusters PowerShell ClusterNode

## 备注

## 相关链接

[添加集群节点](./Add-ClusterNode.md)

[Get-ClusterNode](./Get-ClusterNode.md)

[Remove-ClusterNode](./Remove-ClusterNode.md)

[Resume-ClusterNode](./Resume-ClusterNode.md)

[启动集群节点](./Start-ClusterNode.md)

[Stop-ClusterNode](./Stop-ClusterNode.md)
