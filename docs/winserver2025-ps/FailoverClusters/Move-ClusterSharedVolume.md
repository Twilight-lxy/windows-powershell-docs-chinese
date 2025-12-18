---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/move-clustersharedvolume?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Move-ClusterSharedVolume
---

# 移动集群共享卷（Move-ClusterSharedVolume）

## 摘要
将集群共享卷（Cluster Shared Volume, CSV）的所有权转移给故障转移集群中的另一个节点。

## 语法

```
Move-ClusterSharedVolume [[-Name] <String>] [[-Node] <String>] [-Wait <Int32>]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Move-ClusterSharedVolume` cmdlet 将集群共享卷（Cluster Shared Volume，简称 CSV）的所有权从一个节点转移到故障转移集群中的另一个节点。

在这样一个使用CSV文件的故障转移集群中，任何时候对每个CSV文件的访问都由一个特定的节点控制，这个节点被称为该CSV文件的所有者。然而，单个CSV文件可以包含虚拟硬盘（VHD）文件，这些文件被多个集群中的虚拟机所使用，并且这些虚拟机分布在不同的集群节点上。

## 示例

### 示例 1

```powershell
Move-ClusterSharedVolume -Name "Cluster Disk 3"
```

这个示例将名为“Cluster Disk 3”的集群共享卷移动到另一个集群节点上。

### 示例 2

```powershell
Move-ClusterSharedVolume -Name "Cluster Disk 3" -Node node1
```

这个示例将名为“Cluster Disk 3”的集群共享卷移动到名为“node1”的节点上。

## 参数

### -Cluster

指定要运行此 cmdlet 的集群的名称。如果该参数的输入值为 `.` 或省略，则 cmdlet 将在本地集群上运行。

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

指定要移动的集群共享卷（Cluster Shared Volume）。

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

指定要移动的集群共享卷（Cluster Shared Volume）的名称。

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

### -Node

指定要将集群共享卷（Cluster Shared Volume）移动到的集群节点的名称。

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

指定等待该cmdlet完成所需的时间（以秒为单位）。如果未指定**Wait**参数，那么cmdlet会一直等待直到完成。如果指定了`-Wait 0`，则cmdlet会立即开始执行并立即返回结果，而不会等待任何时间。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters.PowerShellClusterSharedVolume

## 输出

### Microsoft FailoverClusters.PowerShellClusterSharedVolume

## 备注

## 相关链接

[添加集群共享卷](./Add-ClusterSharedVolume.md)

[Get-ClusterSharedVolume](./Get-ClusterSharedVolume.md)

[Remove-ClusterSharedVolume](./Remove-ClusterSharedVolume.md)

[ Resume-ClusterResource ](./Resume-ClusterResource.md)

[Start-ClusterResource](./Start-ClusterResource.md)

[Stop-ClusterResource](./Stop-ClusterResource.md)

[暂停集群资源](./Suspend-ClusterResource.md)
