---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusternode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterNode
---

# Get-ClusterNode

## 摘要
获取关于故障转移集群中一个或多个节点或服务器的信息。

## 语法

```
Get-ClusterNode [[-Name] <StringCollection>] [-InputObject <PSObject>] [-Cluster <String>]
 <CommonParameters>]
```

## 描述

`Get-ClusterNode` cmdlet 可以获取关于故障转移集群中的一个或多个节点或服务器的信息。

使用此cmdlet来获取有关节点状态的信息。要查看某个特定节点当前拥有的资源，请在该cmdlet中指定该节点，然后将结果通过`Get-ClusterResource` cmdlet进行处理。

## 示例

### 示例 1

```powershell
Get-ClusterNode
```

这个示例显示了本地集群中每个节点或服务器的名称、ID和状态。

### 示例 2

```powershell
Get-ClusterNode -Cluster cluster1
```

这个示例显示了名为`cluster1`的集群中每个节点或服务器的名称、ID和状态。

### 示例 3

```powershell
Get-ClusterNode -Name node1 | Get-ClusterResource
```

这个示例列出了当前由本地集群中名为 `node1` 的节点所拥有的所有集群资源。

## 参数

### -Cluster

指定要运行此 cmdlet 的集群的名称。如果该参数的输入为`.` 或被省略，则 cmdlet 将在本地集群上运行。

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

指定用于枚举集群节点的集群。

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

指定要获取的集群节点的名称。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters PowerShell Cluster

## 输出

### MicrosoftFailoverClusters.PowerShellClusterNode

## 备注

## 相关链接

[添加集群节点](./Add-ClusterNode.md)

[Get-ClusterResource](./Get-ClusterResource.md)

[Remove-ClusterNode](./Remove-ClusterNode.md)

[Resume-ClusterNode](./Resume-ClusterNode.md)

[开始创建集群节点](./Start-ClusterNode.md)

[停止集群节点](./Stop-ClusterNode.md)

[Pause-ClusterNode](./Suspend-ClusterNode.md)
