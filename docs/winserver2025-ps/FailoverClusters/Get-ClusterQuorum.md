---
description: 使用此主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusterquorum?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterQuorum
---

# Get-ClusterQuorum

## 摘要
获取有关故障转移集群的法定人数（quorum）配置的信息。

## 语法

```
Get-ClusterQuorum [[-Cluster] <String>] [-InputObject <PSObject>] [<CommonParameters>]
```

## 描述

`Get-ClusterQuorum` cmdlet 可以获取有关故障转移集群的投票机制（quorum）配置的信息。

在故障转移集群中，法定人数（quorum）的配置决定了该集群能够承受的故障数量。如果再发生一次故障，那么集群就必须停止运行。这里所指的相关故障包括节点故障，或者在某些情况下，还包括磁盘见证（disk witness，其中保存了集群配置的副本）或文件共享见证（file share witness）的故障。

## 示例

### 示例 1

```powershell
Get-ClusterQuorum
```

这个示例展示了本地集群的法定人数（quorum）配置信息。

### 示例 2

```powershell
Get-ClusterQuorum -Cluster Cluster1
```

这个示例显示了名为`Cluster1`的集群的法定人数（quorum）配置信息。

## 参数

### -Cluster

指定用于运行此 cmdlet 的集群名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 将在本地集群上运行。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定要查询法定人数（quorum）类型的集群。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell-cluster

## 输出

### MicrosoftFailoverClusters.PowerShellClusterQuorumSettings

## 备注

## 相关链接

[Set-ClusterQuorum](./Set-ClusterQuorum.md)
