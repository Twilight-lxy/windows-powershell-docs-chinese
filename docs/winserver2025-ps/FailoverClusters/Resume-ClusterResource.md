---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/resume-clusterresource?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Resume-ClusterResource
---

# Resume-ClusterResource

## 摘要
在故障转移集群中，会关闭某个磁盘资源或集群共享卷（Cluster Shared Volume）的维护功能。

## 语法

```
Resume-ClusterResource [[-Name] <String>] [-VolumeName <String>] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Resume-ClusterResource` cmdlet 用于关闭故障转移集群中某个磁盘资源或集群共享卷（Cluster Shared Volume）的维护模式。

此cmdlet仅适用于磁盘和集群共享卷（Cluster Shared Volumes）。我们建议在维护任务完成后，立即关闭该磁盘或集群共享卷的维护功能。

## 示例

### 示例 1

```powershell
Resume-ClusterResource "Cluster Disk 2"
```

这个示例会关闭名为“Cluster Disk 2”的CSV文件的维护功能。

### 示例 2

```powershell
Get-ClusterSharedVolume "Cluster Disk 5" | Resume-ClusterResource
```

这个示例会关闭名为“Cluster Disk 5”的CSV文件中所有卷的维护功能。

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

### -InputObject

指定要恢复的集群资源。

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

指定要恢复的集群资源的名称。

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

### -VolumeName

指定要挂起的卷的名称。此参数仅适用于集群共享卷（Cluster Shared Volumes）。如果未指定该参数，操作将针对集群共享卷上的所有卷进行。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters PowerShell ClusterResource

### Microsoft FAILoverClusters.PowerShellClusterSharedVolume

## 输出

### Microsoft FailoverClusters PowerShell ClusterResource

### Microsoft FAILoverClusters.PowerShellClusterSharedVolume

## 备注

## 相关链接

[Add-ClusterResource](./Add-ClusterResource.md)

[Get-ClusterResource](./Get-ClusterResource.md)

[Move-ClusterResource](./Move-ClusterResource.md)

[Remove-ClusterResource](./Remove-ClusterResource.md)

[启动集群资源](./Start-ClusterResource.md)

[Stop-ClusterResource](./Stop-ClusterResource.md)

[暂停集群资源](./Suspend-ClusterResource.md)
