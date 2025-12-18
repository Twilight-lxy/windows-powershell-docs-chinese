---
description: New-ClusterAffinityRule
external help file: ClusterAffinityRule.cdxml-help.xml
Module Name: FailoverClusters
ms.date: 07/27/2023
online version: https://learn.microsoft.com/powershell/module/failoverclusters/new-clusteraffinityrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ClusterAffinityRule
---

# 新集群亲和性规则

## 摘要
创建新的亲和性规则。

## 语法

```
New-ClusterAffinityRule [-Name] <String> [-RuleType <RuleType>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

此 cmdlet 允许为集群创建新的亲和性规则，这些规则可用于控制某些角色（例如虚拟机、资源组等）是否应在同一节点上运行。有关更多信息，请参阅 [集群亲和性](/windows-server/failover-clustering/cluster-affinity)。

可用的规则类型包括：相同的故障域、不同的故障域、相同的节点以及不同的节点。

## 示例

### 示例 1 - 创建一个新的亲和性规则

```powershell
New-ClusterAffinityRule -Name AffinityRule1 -RuleType SameFaultDomain -Cluster Cluster1
```

此命令为 `Cluster1` 创建一条新的亲和性规则，以确保资源始终位于同一个故障域内。

## 参数

### -AsJob

以后台作业的形式运行该 cmdlet。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

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

### -Name

要创建的规则的名字。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RuleType

新规则的亲和类型（affinity type）。该参数的有效取值为：

- `SameFaultDomain` - Resources must stay within the same fault domain.
- `SameFaultDomain` - Resources must stay within the same fault domain.
- `SameNode` - Resources must stay on the same cluster node.
- `DifferentFaultDomain` - Resources must stay in different fault domain (anti-affinity).
- `DifferentNode` - Resources must stay on different cluster nodes (anti-affinity).

```yaml
Type: RuleType
Parameter Sets: (All)
Aliases:
Accepted values: SameFaultDomain, SameNode, DifferentFaultDomain, DifferentNode

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit

指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，PowerShell 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或计算机本身。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

这个cmdlet不接受来自管道的任何输入。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#root/MSCluster/MSCluster_AffinityRule
该cmdlet返回一个对象，该对象表示一条亲和性规则，并以CIM实例的形式存在于`root/MSCLUSTER/MSCluster_AffinityRule`路径下。

## 备注

## 相关链接

[Get-ClusterAffinityRule](Get-ClusterAffinityRule.md)

[Remove-ClusterAffinityRule](Remove-ClusterAffinityRule.md)

[Set-ClusterAffinityRule](Set-ClusterAffinityRule.md)
