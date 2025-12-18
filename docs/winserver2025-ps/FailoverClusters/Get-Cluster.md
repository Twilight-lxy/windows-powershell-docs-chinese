---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 02/08/2023
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-cluster?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-Cluster
---

# Get-Cluster

## 摘要
获取有关给定域中一个或多个故障转移集群的信息。

## 语法

```
Get-Cluster [[-Name] <String>] [-Domain <String>] [<CommonParameters>]
```

## 描述

`Get-Cluster` cmdlet 可以获取给定域中的一个或多个故障转移集群的相关信息。

此cmdlet可以获取关于故障转移集群的各种配置和状态信息，包括以下内容：

- State information about whether a backup is in progress.
- State information about whether the cluster is in a forced quorum state.
- Cross-network settings that are especially relevant for multi-site clusters.

要为集群设置一个通用属性，请使用此cmdlet获取集群对象，然后直接在该集群对象上设置相应的属性。

## 示例

### 示例 1

```powershell
Get-Cluster | Format-List -Property *
```

这个示例以列表的形式显示了本地集群的状态和属性信息。

### 示例 2

```powershell
Get-Cluster -Name cluster1
```

这个示例获取名为 `cluster1` 的集群的相关信息。

### 示例 3

```powershell
Get-Cluster -Domain contoso.com
```

这个示例会获取 `contoso.com` 域中每个集群的相关信息。

### 示例 4

```powershell
Get-Cluster | ForEach-Object -Process {$_.CrossSubnetDelay = 1500}
```

这个示例将名为 `CrossSubnetDelay` 的通用属性设置为 `1500`，用于本地集群。

### 示例 5

```powershell
(Get-Cluster).DynamicQuorum = 1
```

这个示例为集群启用了动态法定人数（Dynamic Quorum）功能。

### 示例 6

```powershell
Get-Cluster | Format-List -Property Quarantine*
```

这个示例展示了本地集群中 **QuarantineThreshold**（隔离阈值）和 **QuarantineDuration**（隔离持续时间）的默认值。

- **QuarantineThreshold**: This is the number of times that a node can become isolated in an hour
 before the cluster will be quarantined. This is set to 3 by default.
- **QuarantineDuration**: This setting, set to 7200 seconds or 2 hours by default, controls how long
  a host will remain quarantined.

### 示例 7

```powershell
(Get-Cluster).MaximumParallelMigrations = 2
```

从 2022-09 的累积更新开始，你现在可以配置集群中同时进行的实时迁移操作的数量。有关更多信息，请参阅[KB5017381](https://support.microsoft.com/help/5017381)（适用于 Windows Server 2022）和[KB5017382](https://support.microsoft.com/help/5017382)（适用于 Azure Stack HCI，版本 21H2）。

这个示例将集群属性“MaximumParallelMigrations”设置为值`2`，从而限制了集群节点可以参与的活动迁移（即同时进行的迁移操作）的数量。无论是现有的还是新的集群节点都会继承这个值`2`，因为这是一个集群属性。设置该集群属性会覆盖使用 `[Set-VMHost](../hyper-v/Set-VMHost.md)` 命令配置的任何相关值。

## 参数

### -Domain

指定用于枚举集群的域的名称。

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

### -Name

指定要获取的集群名称。

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

### CommonParameters

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### MicrosoftFailoverClusters.PowerShell_cluster

## 备注

## 相关链接

[ForEach-Object](https://go.microsoft.com/fwlink/p/?LinkId=113300)

[格式化列表](https://go.microsoft.com/fwlink/p/?LinkId=113302)

[新集群](./New-Cluster.md)

[Remove-Cluster](./Remove-Cluster.md)

[启动集群](./Start-Cluster.md)

[Stop-Cluster](./Stop-Cluster.md)

[测试集群](./Test-Cluster.md)
