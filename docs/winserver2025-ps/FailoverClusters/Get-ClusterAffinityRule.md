---
description: Get-ClusterAffinityRule
external help file: ClusterAffinityRule.cdxml-help.xml
Module Name: FailoverClusters
ms.date: 07/27/2023
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusteraffinityrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterAffinityRule
---

# Get-ClusterAffinityRule

## 摘要
此cmdlet用于显示给定的规则及其类型。

## 语法

```
Get-ClusterAffinityRule [[-Name] <String[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

## 描述

此cmdlet用于显示给定的规则及其类型。默认情况下，该cmdlet会列出所有规则。可以使用**Name**参数来返回特定的规则或多个特定规则。

## 示例

#### 示例 1 - 获取特定的亲和性规则

```powershell
Get-ClusterAffinityRule -Name AffinityRule1 -Cluster Cluster1
```

这个示例从 `Cluster1` 中返回名为 `Rule1` 的集群亲和性规则的相关信息。

## 参数

### -AsJob

将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

所需亲和性规则的名称。如果未指定此参数，该cmdlet会列出所有规则。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时运行的命令行脚本（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，PowerShell 会根据计算机上正在运行的 CIM 命令行脚本的数量来计算一个最优的限制值。此限制仅适用于当前正在运行的命令行脚本，而不适用于整个会话或整个计算机。

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

当一个字符串被传递给此 cmdlet 时，该值将用作要获取的亲和性规则的名称。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#root/MSCLUSTER/MSCluster_AffinityRule

该 cmdlet 返回一个对象，该对象表示一条亲和性规则，并以 CIM 实例的形式存在于 `root/MSCLUSTER/MSCluster_AffinityRule` 路径下。

## 备注

## 相关链接

[New-ClusterAffinityRule](New-ClusterAffinityRule.md)

[Remove-ClusterAffinityRule](Remove-ClusterAffinityRule.md)

[Set-ClusterAffinityRule](Set-ClusterAffinityRule.md)
