---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 09/27/2022
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/get-caureport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-CauReport
---

# 获取Cau报告

## 摘要
获取所有已知的“更新运行”（Updating Runs）的报告，或者获取符合指定日期或其他指定参数的所有“更新运行”的报告。

## 语法

### AllParamsSet（默认值）

```
Get-CauReport [[-ClusterName] <String>] [-Detailed] [-Credential <PSCredential>] [<CommonParameters>]
```

### RangeParamSet

```
Get-CauReport [[-ClusterName] <String>] [[-StartDate] <DateTime>] [[-EndDate] <DateTime>] [-Detailed]
 [-Credential <PSCredential>] [<CommonParameters>]
```

### LastParamSet

```
Get-CauReport [[-ClusterName] <String>] [-Last] [-Detailed] [-Credential <PSCredential>] [<CommonParameters>]
```

### SpecificReportParamSet

```
Get-CauReport [[-ClusterName] <String>] [-Report <CauReportSummary>] [-Credential <PSCredential>]
 [<CommonParameters>]
```

## 描述

`Get-CauReport` cmdlet 可以获取所有已知的 “Updating Run” 操作的报告，或者仅获取符合指定日期或其他参数条件的 “Updating Run” 操作的报告。该 cmdlet 可以返回在指定的 **StartDate** 和 **EndDate** 之间的所有 “Updating Run” 报告列表；如果使用的是 **Last** 参数而非具体的日期，则会返回最新的 “Updating Run” 报告。默认情况下，报告仅包含摘要信息，但可以通过设置 **Detailed** 参数或使用 **Report** 参数并指定一个 “Cluster-Aware Updating (CAU)” 报告摘要对象来获取更详细的详细信息。

## 示例

### 示例 1：从指定的集群中获取更新运行的详细列表

```powershell
Get-CauReport -ClusterName Contoso-FC1 -StartDate 01/01/2012 -Detailed
```

此命令可获取在名为 Contoso-FC1 的集群上于 2012 年 1 月 1 日或之后执行的更新操作的详细列表。

### 示例 2：从指定的集群中获取指定日期范围内的更新运行详细列表

```powershell
Get-CauReport -ClusterName "Contoso-FC1" -StartDate 01/01/2012 -EndDate 04/01/2012 -Detailed
```

此命令可获取在名为 Contoso-FC1 的集群上执行的更新操作的详细列表，这些更新操作的时间范围是从 2012 年 1 月 1 日开始到 2012 年 4 月 1 日结束。

### 示例 3：从指定的集群中获取最后一次更新运行的摘要

```powershell
$CauReportSummary = Get-CauReport "Contoso-FC1" -Last
Get-CauReport "Contoso-FC1" -Report $CauReportSummary
```

第一个命令从名为 Contoso-FC1 的集群中获取最后一次更新运行的报告摘要，并将结果存储在名为 `$CauReportSummary` 的变量中。

第二个命令从存储在 `$CauReportSummary` 变量中的信息中获取详细报告。

## 参数

### -ClusterName

指定该cmdlet获取报告的集群名称。只有当此cmdlet不在故障转移集群节点上运行，或者用于引用与当前执行位置不同的故障转移集群时，才需要这个参数。

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

### -Credential

指定目标集群的管理凭据。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Detailed

指定该 cmdlet 会获取一次或多次运行时的完整结果，而不仅仅是摘要信息。

```yaml
Type: SwitchParameter
Parameter Sets: AllParamsSet, RangeParamSet, LastParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EndDate

指定该cmdlet仅获取在此时间之前的运行所产生的报告。

```yaml
Type: DateTime
Parameter Sets: RangeParamSet
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Last

表示此 cmdlet 只获取最新的运行报告。

```yaml
Type: SwitchParameter
Parameter Sets: LastParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Report

指定此cmdlet获取详细运行结果的报告摘要。

```yaml
Type: CauReportSummary
Parameter Sets: SpecificReportParamSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -StartDate

指定此cmdlet仅获取在该时间之后运行的报告。

```yaml
Type: DateTime
Parameter Sets: RangeParamSet
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ClusterAware Updating.CauReportSummary

## 输出

### Microsoft-cluster Aware-updating.CauReport

### Microsoft.ClusterAware Updating.CauReportSummary

## 备注

## 相关链接

[Export-CauReport](./Export-CauReport.md)

