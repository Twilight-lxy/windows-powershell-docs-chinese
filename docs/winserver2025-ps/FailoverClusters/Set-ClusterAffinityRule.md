---
description: Set-ClusterAffinityRule
external help file: ClusterAffinityRule.cdxml-help.xml
Module Name: FailoverClusters
ms.date: 07/27/2023
online version: https://learn.microsoft.com/powershell/module/failoverclusters/set-clusteraffinityrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ClusterAffinityRule
---

# 设置集群亲和性规则（Set-ClusterAffinityRule）

## 摘要
启用或禁用某种亲和性规则，并更新该规则的类型。

## 语法

### 查询（cdxml）（默认值）

```
Set-ClusterAffinityRule [[-Name] <String[]>] [-RuleType <RuleType>] [-Enabled <UInt32>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

### InputObject (cdxml)

```
Set-ClusterAffinityRule -InputObject <CimInstance[]> [-RuleType <RuleType>] [-Enabled <UInt32>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

## 描述

`Set-ClusterAffinityRule` cmdlet 可以启用或禁用现有的亲和性规则，同时也可以更改规则的类型（**RuleType**）。

## 示例

### 示例 1 - 启用亲和性规则

```powershell
Set-ClusterAffinityRule -Name AffinityRule1 -Enabled $true
```

这个示例启用了一个名为 `AffinityRule1` 的集群亲和性规则。

### 示例 2 - 禁用一个亲和性规则

```powershell
Set-ClusterAffinityRule -Name AffinityRule1 -Enabled $false
```

这个示例禁用了名为 `AffinityRule1` 的集群亲和性规则。

#### 示例 3 – 更改亲和规则类型

```powershell
Get-ClusterAffinityRule -Name AffinityRule1 | Set-ClusterAffinityRule -RuleType DifferentNode
```

这个示例获取名为 `AffinityRule1` 的亲和规则对象，并将该对象传递给 `Set-ClusterAffinityRule` 命令行工具。`Set-ClusterAffinityRule` 命令行工具会将该亲和规则的类型更改为 `DifferentNode`。

## 参数

### -AsJob

将cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Enabled

启用或禁用亲和性规则。该参数的可接受值为：

- `0` or `$false`. The affinity rule is disabled.
- `1` or `$true`. The affinity rule is enabled.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定要更改的亲和规则对象。该值必须是一个表示亲和规则的对象，类似于 `Get-ClusterAffinityRule` 命令返回的输出结果。

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

需要更改的亲和性规则的名称。

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

返回传递给该命令的原始对象。默认情况下，此cmdlet不会生成任何输出。

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

### -RuleType

用于设置规则的亲和性类型。该参数的有效值包括：

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

该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，PowerShell 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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

当一个字符串通过管道传递给此cmdlet时，该字符串的值将被用作要更改的亲和性规则的名称。

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

[Get-ClusterAffinityRule](Get-ClusterAffinityRule.md)

[New-ClusterAffinityRule](New-ClusterAffinityRule.md)

[Remove-ClusterAffinityRule](Remove-ClusterAffinityRule.md)
