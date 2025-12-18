---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clustersharedvolume?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterSharedVolume
---

# 添加集群共享卷

## 摘要
在故障转移集群中，将某个卷设置为可用状态，并将其添加到集群共享卷（Cluster Shared Volumes）中。

## 语法

```
Add-ClusterSharedVolume [[-Name] <StringCollection>] [-InputObject <PSObject>] [-Cluster <String>]
 [<CommonParameters>]
```

## 描述

`Add-ClusterSharedVolume` cmdlet 可用于在故障转移集群中创建一个可用于“集群共享卷”（Cluster Shared Volumes）的卷。该集群共享卷必须从“可用存储”（Available Storage）中的磁盘列表中选取；也就是说，这些磁盘已被添加到集群中，但尚未被分配给特定的用途。

## 示例

### 示例 1

```powershell
Add-ClusterSharedVolume -Name "Cluster Disk 4"
```

这个示例将“Cluster Disk 4”添加到本地集群中的集群共享卷（Cluster Shared Volumes）中。

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

指定要添加到集群共享卷（Cluster Shared Volumes）中的集群磁盘资源。

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

指定要添加的集群磁盘资源的名称。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters.PowerShellClusterResource

## 输出

### MicrosoftFailoverClusters.PowerShell ClusterSharedVolume

## 备注

## 相关链接

[添加集群磁盘](./Add-ClusterDisk.md)

[Get-ClusterSharedVolume](./Get-ClusterSharedVolume.md)

[Move-ClusterSharedVolume](./Move-ClusterSharedVolume.md)

[ Remove-ClusterSharedVolume](./Remove-ClusterSharedVolume.md)
