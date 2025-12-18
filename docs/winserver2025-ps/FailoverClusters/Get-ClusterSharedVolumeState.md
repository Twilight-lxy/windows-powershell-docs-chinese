---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clustersharedvolumestate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterSharedVolumeState
---

# 获取集群共享卷的状态

## 摘要
获取集群中群集共享卷（Cluster Shared Volumes）的状态。

## 语法

```
Get-ClusterSharedVolumeState [-Node <StringCollection>] [[-Name] <StringCollection>]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Get-ClusterSharedVolumeState` cmdlet 用于获取集群中集群共享卷（Cluster Shared Volumes）的状态。

## 示例

### 示例 1

```powershell
Get-ClusterSharedVolumeState
```

该命令用于获取本地集群中群集共享卷（Cluster Shared Volumes）的状态。

## 参数

### -Cluster

指定用于运行此 cmdlet 的集群名称。如果您使用点（`.`）作为集群名称，或者未指定该参数，则 cmdlet 会在本地集群上运行。

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

指定要输入到此 cmdlet 的数据。您可以使用这个参数，也可以将数据通过管道（pipe）传递给该 cmdlet。

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

指定要获取状态信息的集群共享卷（Cluster Shared Volumes）的名称，这些名称以字符串集合的形式提供。

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

### -Node

指定用于获取集群共享卷（Cluster Shared Volumes）状态的集群节点的名称，这些名称以字符串集合的形式提供。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters PowerShell Cluster

### Microsoft FailoverClusters.PowerShell ClusterNode

### MicrosoftFailoverClusters.PowerShell-clusterSharedVolume

## 输出

## 备注

## 相关链接

[Get-ClusterSharedVolume](./Get-ClusterSharedVolume.md)
