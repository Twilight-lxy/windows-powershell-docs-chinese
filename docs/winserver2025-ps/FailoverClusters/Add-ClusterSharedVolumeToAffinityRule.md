---
description: 将 `Add-ClusterSharedVolumeToAffinityRule`
external help file: ClusterAffinityRule.cdxml-help.xml
Module Name: FailoverClusters
ms.date: 07/27/2023
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clustersharedvolumetoaffinityrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: 将 `Add-ClusterSharedVolumeToAffinityRule`
---

# 将集群共享卷添加到亲和性规则中

## 摘要
将一个集群共享卷（Cluster Shared Volume，简称 CSV）添加到现有的亲和性规则中。

## 语法

### 查询（CDXML）（默认值）

```
将 `Add-ClusterSharedVolumeToAffinityRule` [[-Name] <String[]>] [-ClusterSharedVolumes] <String[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

### InputObject（cdxml）

```
将 `Add-ClusterSharedVolumeToAffinityRule` -InputObject <CimInstance[]>
 [-ClusterSharedVolumes] <String[]> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru]
 [<CommonParameters>]
```

## 描述

此cmdlet允许您使用CSV名称或对象，将集群共享卷（Cluster Shared Volumes，简称CSVs）添加到现有的亲和性规则（Affinity Rule）中。

## 示例

### 示例 1 – 将 CSV 文件添加到亲和性规则中

```powershell
将 `Add-ClusterSharedVolumeToAffinityRule` -ClusterSharedVolumes MyVolume -Name MyRule -Cluster MyCluster
```

此命令将集群共享卷“MyVolume”添加到集群“MyCluster”的亲和性规则“MyRule”中。

### 示例 2：使用管道将 CSV 文件添加到亲和规则中

```powershell
Get-ClusterAffinityRule -name Rule1 |
 将 `Add-ClusterSharedVolumeToAffinityRule` -ClusterSharedVolumes Volume1
```

该命令获取了亲和性规则 `Rule1` 对象，并将其传递给 `将 `Add-ClusterSharedVolumeToAffinityRule`` 命令。该命令将集群共享卷 `Volume1` 添加到该亲和性规则中。

## 参数

### -AsJob

将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ClusterSharedVolumes

该集群共享了卷，以便将这些卷添加到亲和性规则中。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定用于管道命令中的亲和性规则对象。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name

用于将集群共享卷添加到的关联规则的名称。

```yaml
Type: String[]
Parameter Sets: Query (cdxml)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru

返回传递给该命令的原始关联规则对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -ThrottleLimit

该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 PowerShell 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值（即并发操作的数量）。此限制仅适用于当前正在运行的 cmdlet，而不适用于整个会话或计算机本身。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

当一个字符串通过管道传递给这个cmdlet时，该字符串的值将被用作要添加集群共享卷的亲和性规则的名称。

### Microsoft.ManagementInfrastructure.CimInstance[]

此cmdlet接受表示亲和性规则的CIM实例对象，这些对象类似于[Get-ClusterAffinityRule](Get-ClusterAffinityRule.md) cmdlet返回的对象。

## 输出

### 无

默认情况下，该cmdlet不会返回任何输出结果。

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#root/MSCLUSTER/MSCluster_AffinityRule

当指定了 **PassThru** 参数时，该 cmdlet 会返回一个对象，该对象表示一条亲和性规则，并作为 CIM 实例存在于 `root/MSCLUSTER/MSCluster_AffinityRule` 路径下。

## 备注

## 相关链接

[Remove-ClusterSharedVolumeFromAffinityRule](Remove-ClusterSharedVolumeFromAffinityRule.md)
