---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clusteriscsitargetserverrole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusteriSCSITargetServerRole
---

# 为 iSCSI 目标服务器角色添加集群支持

## 摘要
创建一个高可用性的 iSCSI 目标服务器。

## 语法

```
Add-ClusteriSCSITargetServerRole -Storage <StringCollection> [-StaticAddress <StringCollection>]
 [-IgnoreNetwork <StringCollection>] [[-Name] <String>] [-Wait <Int32>] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Add-ClusteriSCSITargetServerRole` cmdlet 用于创建一个高可用性的 iSCSI 目标服务器。

## 示例

### 示例 1：创建一个集群化的目标服务器

```powershell
Add-ClusteriSCSITargetServerRole -Storage "Cluster Disk 5"
```

这个示例使用“Cluster Disk 5”创建了一个集群化的iSCSI目标服务器，并为其分配了一个默认名称。

### 示例 2

```powershell
Add-ClusteriSCSITargetServerRole -Storage "Cluster Disk 5" -Name MyiSCSITarget
```

这个示例使用“Cluster Disk 5”创建了一个集群化的iSCSI目标服务器，并为其分配了名称“MyiSCSITarget”。

### 示例 3

```powershell
Add-ClusteriSCSITargetServerRole -Storage "Cluster Disk 5" -Wait 0
```

这个示例使用“Cluster Disk 5”创建了一个集群化的iSCSI目标服务器，并为其分配了一个默认名称。该命令行脚本在所有资源都上线之前就完成了执行过程，无需等待它们全部准备好。

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

### -IgnoreNetwork

指定在运行该 cmdlet 时需要忽略的一个或多个网络。启用了 DHCP 的网络始终会被包含在内，但其他网络需要使用 **StaticAddress** 参数来指定静态地址，或者应该通过 **IgnoreNetwork** 参数明确地将其忽略。

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

### -InputObject

指定用于创建高可用性 iSCSI 目标服务器的集群。

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

指定要创建的高可用性 iSCSI 目标服务器的名称。

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

### -StaticAddress

指定一个或多个静态地址，在运行该 cmdlet 时使用这些地址。启用了 DHCP 的网络会自动被包含在内，但其他网络需要通过 **StaticAddress** 参数来指定静态地址；或者可以使用 **IgnoreNetwork** 参数明确忽略这些网络。

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

### -Storage

指定要添加到新建的高可用性 iSCSI 目标服务器中的集群磁盘资源。

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

### -Wait

指定等待该cmdlet完成所需的时间（以秒为单位）。如果未指定**Wait**参数，则cmdlet会一直等待直到任务完成；如果指定的值为`0`，则cmdlet会立即被执行并立即返回结果，而不会等待任何时间。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft_failoverClusters.PowerShellCluster

## 输出

### Microsoft FAILoverClusters.PowerShell.ClusterGroup

## 备注

## 相关链接

[Get-ClusterResource](./Get-ClusterResource.md)
