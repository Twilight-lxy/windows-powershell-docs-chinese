---
description: 将 `ClusterGroup` 添加到 `AffinityRule` 中
external help file: ClusterAffinityRule.cdxml-help.xml
Module Name: FailoverClusters
ms.date: 09/20/2023
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clustergrouptoaffinityrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: 将 `ClusterGroup` 添加到 `AffinityRule` 中
---

# 将 ClusterGroup 添加到 AffinityRule 中

## 摘要
将一个集群组添加到亲和规则中。

## 语法

### 查询（CDXML）（默认值）

```
将 `ClusterGroup` 添加到 `AffinityRule` 中 [[-Name] <String[]>] [-Groups] <String[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

### InputObject (cdxml)

```
将 `ClusterGroup` 添加到 `AffinityRule` 中 -InputObject <CimInstance[]> [-Groups] <String[]>
[-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

## 描述

将一个集群组添加到某个已命名的亲和性规则中。

## 示例

### 示例 1 - 向亲和性规则中添加一个组

```powershell
将 `ClusterGroup` 添加到 `AffinityRule` 中 -Groups MyGroup -Name MyRule -Cluster MyCluster
```

这个示例将名为 `MyGroup` 的组添加到名为 `MyRule` 的亲和性规则中，该规则应用于名为 `MyCluster` 的集群上。

### 示例 2 - 使用管道将一个组添加到亲和性规则中

```powershell
Get-ClusterAffinityRule -name Rule1 |
 将 `ClusterGroup` 添加到 `AffinityRule` 中 -Groups MyGroup
```

该命令获取了亲和性规则 `Rule1` 对象，并将其传递给 `将 `ClusterGroup` 添加到 `AffinityRule` 中` 命令。该命令将集群组 `MyGroup` 添加到该亲和性规则中。

## 参数

### -AsJob

将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，使用的是本地计算机上的当前会话。

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

### -Groups

这是需要添加到亲和性规则中的组列表。

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

指定在管道命令中使用的亲和规则对象。

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

用于添加组的“亲和性规则”（Affinity rule）。

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

返回传递给该命令的原始亲和性规则对象。默认情况下，此cmdlet不会生成任何输出。

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

该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入`0`，PowerShell会根据计算机上正在运行的CIM cmdlet的数量来计算一个最优的节流限制（即允许同时运行的cmdlet数量）。这个节流限制仅适用于当前的cmdlet，而不影响整个会话或计算机本身。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

当一个字符串通过管道传递给此cmdlet时，该值将被用作亲和性规则的名称，用于将集群共享卷添加到相应的规则中。

### Microsoft.ManagementInfrastructure.CimInstance[]

此cmdlet接受表示亲和性规则的CIM实例对象，这些对象类似于[Get-ClusterAffinityRule](Get-ClusterAffinityRule.md) cmdlet返回的对象。

## 输出

### 无

默认情况下，该cmdlet不会返回任何输出结果。

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#root/MSCLUSTER/MSCluster_AffinityRule

当指定了 **PassThru** 参数时，该 cmdlet 会返回一个对象，该对象表示一条亲和性规则，并以 CIM 实例的形式存在于 `root/MSCLUSTER/MSCluster_AffinityRule` 路径下。

## 备注

## 相关链接

[从关联规则中移除集群组](Remove-ClusterGroupFromAffinityRule.md)
