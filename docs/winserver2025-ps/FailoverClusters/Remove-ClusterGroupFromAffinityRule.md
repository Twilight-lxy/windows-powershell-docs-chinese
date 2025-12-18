---
description: Remove-ClusterGroupFromAffinityRule
external help file: ClusterAffinityRule.cdxml-help.xml
Module Name: FailoverClusters
ms.date: 09/20/2023
online version: https://learn.microsoft.com/powershell/module/failoverclusters/remove-clustergroupfromaffinityrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ClusterGroupFromAffinityRule
---

# 从亲和性规则中删除集群组

## 摘要
从亲和性规则中移除一个集群组。

## 语法

### 查询（cdxml）（默认设置）

```
Remove-ClusterGroupFromAffinityRule [[-Name] <String[]>] [-Groups] <String[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

### InputObject (cdxml)

```
Remove-ClusterGroupFromAffinityRule -InputObject <CimInstance[]> [-Groups] <String[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

## 描述

从亲和性规则中移除一个集群组。这并不会删除该规则本身。

## 示例

### 示例 1 - 从亲和性规则中删除某个组

```powershell
Remove-ClusterGroupFromAffinityRule -Name MuRyle -Groups MyGroup -Cluster MyCluster
```

这个示例将集群组 `MyGroup` 从名为 `MyRule` 的亲和性规则中删除。

### 示例 2：使用流水线将某个组从关联规则中移除

```powershell
Get-ClusterAffinityRule -name Rule1 |
 Remove-ClusterGroupFromAffinityRule -Groups MyGroup
```

该命令获取了亲和性规则 `Rule1` 对象，并将其传递给 `Remove-ClusterGroupFromAffinityRule` 命令。该命令会将集群组 `MyGroup` 从该亲和性规则中移除。

## 参数

### -AsJob

将 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关PowerShell后台作业的更多信息，请参阅[关于作业（about_Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

需要从亲和性规则中移除的组。

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

用于移除组的亲和性规则的名称。

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

返回传递给该命令的原始亲和规则对象。默认情况下，此cmdlet不会生成任何输出。

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

该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 PowerShell 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

当一个字符串通过管道传递给这个 cmdlet 时，该字符串的值会被用作affinity规则的名称，用于移除集群共享卷。

### Microsoft.ManagementInfrastructure.CimInstance[]

指定要删除的亲和性规则对象，该对象由[Get-ClusterAffinityRule](Get-ClusterAffinityRule.md) cmdlet返回。

## 输出

### 无

默认情况下，该cmdlet不会返回任何输出结果。

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#root/MSCLUSTER/MSCluster_AffinityRule

当指定了 **PassThru** 参数时，该 cmdlet 会返回一个对象，该对象表示一条亲和性规则，并以 CIM 实例的形式存在于 `root/MSCLUSTER/MSCluster_AffinityRule` 路径下。

## 备注

## 相关链接

[将集群组添加到亲和性规则中](Add-ClusterGroupToAffinityRule.md)
