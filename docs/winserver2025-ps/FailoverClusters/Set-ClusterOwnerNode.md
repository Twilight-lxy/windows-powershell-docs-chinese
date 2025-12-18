---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/set-clusterownernode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ClusterOwnerNode
---

# 设置集群所有者节点

## 摘要
指定在故障转移集群中哪些节点可以拥有某个资源；或者为集群角色或资源组确定各个节点的优先顺序。

## 语法

```
Set-ClusterOwnerNode [-Resource <String>] [-Group <String>] -Owners <StringCollection>
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Set-ClusterOwnerNode` cmdlet 用于指定在故障转移集群中哪些节点可以拥有某个资源，或者为集群角色或资源组确定节点之间的优先顺序。控制这些所有权设置的因素会影响集群在资源或集群角色发生故障时的响应方式。

## 示例

### 示例 1

```powershell
Get-ClusterResource -Name "Cluster Disk 3" | Set-ClusterOwnerNode -Owners node1,node2
```

这个示例将名为“Cluster Disk 3”的集群的可能所有者设置为本地集群中的节点`node1`和`node2`。

### 示例 2

```powershell
Set-ClusterOwnerNode -Group cluster12FS -Owners node3,node2
```

这个示例将名为 `cluster12FS` 的集群服务的首选所有者设置为本地集群中的 `node3` 节点，其次再设置为 `node2` 节点。

## 参数

### -Cluster

指定要运行此cmdlet的集群名称。如果该参数的输入值为`.`或被省略，则cmdlet将在本地集群上运行。

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

### -Group

指定用于设置所有者节点的集群组的名称。

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

### -InputObject

指定要设置所有者节点的集群组或集群资源。

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

### -Owners

指定所有者节点的列表。如果这是针对一个集群组，则该列表中的节点将作为该集群组的优选所有者；如果这是针对一个集群资源，则该列表列出了可能成为该集群资源所有者的节点。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Resource

指定用于设置所有者节点的集群资源的名称。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft_failoverClusters.PowerShellClusterGroup

### MicrosoftFailoverClusters.PowerShellClusterResource

## 输出

### 无

## 备注

## 相关链接

[Get-ClusterOwnerNode](./Get-ClusterOwnerNode.md)
