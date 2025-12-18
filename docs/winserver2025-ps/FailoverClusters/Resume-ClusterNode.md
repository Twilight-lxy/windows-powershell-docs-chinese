---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/resume-clusternode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Resume-ClusterNode
---

# Resume-ClusterNode

## 摘要
从暂停状态恢复节点，或将已耗尽资源的工作负载重新分配回该节点，或者同时执行这两项操作。

## 语法

```
Resume-ClusterNode [[-Name] <StringCollection>] [[-Failback] <ResumeClusterNodeFailbackType>]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Resume-ClusterNode` cmdlet 用于在故障转移集群节点被暂停或停止运行后恢复其活动，或者将已被移除的工作负载重新分配回该节点。当一个节点被恢复运行时，之前从该节点上移除的集群角色会被重新添加回去；同时，当前处于离线状态的集群角色或资源也可以在该节点上重新上线。

## 示例

### 示例 1

```powershell
Resume-ClusterNode node1
```

这个示例用于在本地集群上重新启动节点1。

### 示例 2

```powershell
Resume-ClusterNode node2 -Cluster mycluster
```

这个示例会在名为 `mycluster` 的集群中重新启动节点2。

### 示例 3

```powershell
Get-ClusterNode | Resume-ClusterNode
```

这个示例会恢复本地集群中所有处于挂起（suspended）或暂停（paused）状态的节点。

### 示例 4

```powershell
Get-ClusterNode | Resume-ClusterNode -Failback Immediate
```

这个示例会恢复本地集群中所有处于挂起（suspended）或暂停（paused）状态的节点，并立即将之前从这些节点上移除的工作负载重新加载回这些节点。

## 参数

### -Cluster

指定用于运行此cmdlet的集群名称。如果该参数的输入值为`.`或被省略，则cmdlet将在本地集群上运行。

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

### -Failback

该参数用于设置策略，以便将资源消耗殆尽的工作负载重新恢复到相应的节点上。可接受的参数值包括：

- `NoFailBack` - Don't failback at all.
- `Immediate` - Failback immediately.
- `Policy` - Failback only during specific hours.

```yaml
Type: ResumeClusterNodeFailbackType
Parameter Sets: (All)
Aliases:
Accepted values: NoFailback, Immediate, Policy

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定要运行该cmdlet的组、节点、资源或服务，以及对应的集群。

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

指定要运行该 cmdlet 的组、节点、资源或服务的名称，以及对应的集群名称。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft_failoverClusters.PowerShell ClusterNode

## 输出

### Microsoft_failoverClusters.PowerShell ClusterNode

## 备注

## 相关链接

[添加集群节点](./Add-ClusterNode.md)

[Clear-ClusterNode](./Clear-ClusterNode.md)

[Get-ClusterNode](./Get-ClusterNode.md)

[Remove-ClusterNode](./Remove-ClusterNode.md)

[启动集群节点](./Start-ClusterNode.md)

[停止集群节点](./Stop-ClusterNode.md)

[暂停集群节点](./Suspend-ClusterNode.md)
