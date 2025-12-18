---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clustersharedvolume?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterSharedVolume
---

# Get-ClusterSharedVolume

## 摘要
获取关于故障转移集群中集群共享卷（Cluster Shared Volumes）的信息。

## 语法

```
Get-ClusterSharedVolume [[-Name] <StringCollection>] [-InputObject <PSObject>] [-Cluster <String>]
 [<CommonParameters>]
```

## 描述

`Get-ClusterSharedVolume` cmdlet 可以获取关于故障转移集群中集群共享卷（Cluster Shared Volumes）的信息。

## 示例

### 示例 1

```powershell
Get-ClusterSharedVolume
```

这个示例列出了本地集群中的所有集群共享卷（Cluster Shared Volumes）。

### 示例 2

```powershell
Get-ClusterSharedVolume -Cluster cluster1
```

这个示例列出了名为 `cluster1` 的集群中的所有集群共享卷（Cluster Shared Volumes）。

### 示例 3

```powershell
Get-ClusterSharedVolume -Name "Cluster Disk 4"
```

这个示例展示了名为“Cluster Disk 4”的集群共享卷（Cluster Shared Volume）的状态。

## 参数

### -Cluster

指定要运行此 cmdlet 的集群的名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 会在本地集群上运行。

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

指定用于枚举集群共享卷（Cluster Shared Volumes）的集群。

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

指定要获取的集群共享卷（Cluster Shared Volume）的名称。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters PowerShellCluster

## 输出

### MicrosoftFailoverClusters.PowerShellClusterSharedVolume

## 备注

## 相关链接

[添加集群共享卷](./Add-ClusterSharedVolume.md)

[Move-ClusterSharedVolume](./Move-ClusterSharedVolume.md)

[Remove-ClusterSharedVolume](./Remove-ClusterSharedVolume.md)
