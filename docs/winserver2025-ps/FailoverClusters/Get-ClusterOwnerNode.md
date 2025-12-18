---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusterownernode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterOwnerNode
---

# Get-ClusterOwnerNode

## 摘要
获取关于在故障转移集群中哪些节点可以拥有某个资源的信息，或者关于负责执行特定集群角色的节点之间的优先级顺序的信息。

## 语法

```
Get-ClusterOwnerNode [-Resource <String>] [-Group <String>] [-ResourceType <String>]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Get-ClusterOwnerNode` cmdlet 可以获取关于在故障转移集群中哪些节点可以拥有某资源的信息，或者关于拥有该资源的节点之间的优先级顺序的信息。

用于控制资源所有者或集群角色所有者的设置，会影响到集群在资源或集群角色发生故障时的响应方式。

## 示例

### 示例 1

```powershell
Get-ClusterResource -Cluster "Cluster Disk 1" | Get-ClusterOwnerNode
```

这个示例列出了本地集群中名为“Cluster Disk 1”的集群的可能所有者。

### 示例 2

```powershell
Get-ClusterGroup -Group cluster1FS12 | Get-ClusterOwnerNode
```

这个示例列出了在本地集群中名为 `cluster1FS12` 的集群文件服务器或资源组的首选所有者。

## 参数

### -Cluster

指定用于运行此 cmdlet 的集群名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 将在本地集群上运行。

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

指定用于枚举所有者节点的集群组的名称。

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

指定要枚举所有者节点的集群组或集群资源。

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

### -Resource

指定要枚举所有者节点的集群资源的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Res

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourceType

指定用于枚举所有者节点的集群资源类型的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ResType

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell_clusterResource

### MicrosoftFailoverClusters.PowerShellClusterGroup

### MicrosoftFailoverClusters.PowerShell_CLUSTERResourceType

## 输出

### MicrosoftFailoverClusters.PowerShell ClusterOwnerNodeList

## 备注

## 相关链接

[Set-ClusterOwnerNode](./Set-ClusterOwnerNode.md)
