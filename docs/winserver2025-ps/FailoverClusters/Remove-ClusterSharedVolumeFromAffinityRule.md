---
description: Remove-ClusterSharedVolumeFromAffinityRule
external help file: ClusterAffinityRule.cdxml-help.xml
Module Name: FailoverClusters
ms.date: 07/28/2023
online version: https://learn.microsoft.com/powershell/module/failoverclusters/remove-clustersharedvolumefromaffinityrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ClusterSharedVolumeFromAffinityRule
---

# 从关联规则中移除集群共享卷（Remove-ClusterSharedVolumeFromAffinityRule）

## 摘要
从关联规则中移除一个集群共享卷。

## 语法

### 查询（CDXML）（默认设置）

```
Remove-ClusterSharedVolumeFromAffinityRule [[-Name] <String[]>] [-ClusterSharedVolumes] <String[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

### InputObject（cdxml）

```
Remove-ClusterSharedVolumeFromAffinityRule -InputObject <CimInstance[]>
 [-ClusterSharedVolumes] <String[]>  [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [<CommonParameters>]
```

## 描述

从关联规则中移除一个集群共享卷。

## 示例

#### 示例 1 - 从亲和性规则中删除一个 CSV 文件

```powershell
Remove-ClusterSharedVolumeFromAffinityRule -ClusterSharedVolumes Volume -Name Rule -Cluster Cluster
```

此命令会从集群 `_Cluster_` 的亲和性规则 `_Rule_` 中移除集群共享卷 `_Volume_`。

### 示例 2：使用管道将 CSV 文件转换为关联规则

```powershell
Get-ClusterAffinityRule -name Rule1 |
 Remove-ClusterSharedVolumeFromAffinityRule -ClusterSharedVolumes Volume1
```

该命令获取了亲和性规则 `Rule1` 对象，并将其传递给 `Remove-ClusterSharedVolumeFromAffinityRule` 命令。该命令会将集群共享卷 `Volume1` 从该亲和性规则中移除。

## 参数

### -AsJob

将该 cmdlet 作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，随后显示命令提示符。在作业完成的过程中，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关PowerShell后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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

这些集群化的共享卷需要被添加到给定的亲和性规则中。

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

指定用于管道命令中的亲和性规则输入对象。

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

用于添加组的亲和性规则的名称。

```yaml
Type: String[]
Parameter Sets: Query (cdxml)
Aliases: Set

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru

返回传递给该命令的原始关联规则对象。默认情况下，此cmdlet不会生成任何输出。

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

该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，PowerShell 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳节流限制。该节流限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

当一个字符串通过管道传递给这个cmdlet时，该字符串的值将被用作删除集群共享卷的亲和性规则（affinity rule）的名称。

### Microsoft.ManagementInfrastructure.CimInstance[]

指定要删除的亲和性规则对象，该对象由[Get-ClusterAffinityRule](Get-ClusterAffinityRule.md) cmdlet返回。

## 输出

### 无

默认情况下，该cmdlet不会返回任何输出结果。

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#root/MSCLUSTER/MSCluster_AffinityRule

当指定了**PassThru**参数时，该cmdlet会返回一个对象，该对象表示一条亲和性规则，并以CIM实例的形式存在于`root/MSCLUSTER/MSCluster_AffinityRule`路径下。

## 备注

## 相关链接

[将集群共享卷添加到亲和性规则中](Add-ClusterSharedVolumeToAffinityRule.md)
