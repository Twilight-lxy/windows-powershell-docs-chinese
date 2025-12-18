---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusteravailabledisk?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterAvailableDisk
---

# 获取集群中可用的磁盘

## 摘要
获取有关可以支持故障转移集群（Failover Clustering）的磁盘的信息，这些磁盘对所有节点都是可见的，但尚未成为集群磁盘集合的一部分。

## 语法

```
Get-ClusterAvailableDisk [[-Cluster] <String>] [-Disk <CimInstance>] [-All]
 [-InputObject <PSObject>] [<CommonParameters>]
```

## 描述

`Get-ClusterAvailableDisk` cmdlet 可以获取有关那些能够支持故障转移集群（Failover Clustering）且对所有节点都可见的磁盘的信息，但这些磁盘尚未成为集群磁盘集合的一部分。

如果某个磁盘突然从可用于集群的磁盘列表中消失，请确保存储配置允许所有集群服务器上的操作系统能够根据需要识别并挂载该磁盘。该磁盘必须是基本磁盘（而非动态磁盘），并且不应被其他服务器访问或使用。

## 示例

### 示例 1

```powershell
Get-ClusterAvailableDisk
```

这个示例列出了可以添加到集群中的磁盘。

### 示例 2

```powershell
Get-ClusterAvailableDisk | Add-ClusterDisk
```

这个示例将所有可以添加到本地集群中的磁盘都添加进来。

## 参数

### -All

请帮我填写所有相关描述内容。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Cluster

指定用于运行此 cmdlet 的集群名称。如果该参数的输入为`.` 或被省略，则 cmdlet 将在本地集群上运行。

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

### -Disk

指定要枚举的磁盘。

```yaml
Type: CimInstance
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -InputObject

指定用于列举可用共享磁盘的集群。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters.PowerShellCluster

## 输出

### MicrosoftFailoverClusters.PowerShell ClusterDiskInfo

## 备注

## 相关链接

[添加集群磁盘](./Add-ClusterDisk.md)
