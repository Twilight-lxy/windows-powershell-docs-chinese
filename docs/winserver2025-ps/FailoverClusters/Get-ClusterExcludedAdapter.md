---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 08/28/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusterexcludedadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterExcludedAdapter
---

# Get-ClusterExcludedAdapter

## 摘要
从被排除的适配器列表中检索一个网络适配器。

## 语法

```
Get-ClusterExcludedAdapter -ExclusionType <AdapterExclusionType> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

`Get-ClusterExcludedAdapter` cmdlet 用于从应被故障转移集群排除使用的网络适配器列表中检索某个网络适配器。默认情况下，集群会使用所有可用的网络适配器；但在某些情况下，您可能需要将某些适配器预留出来作为备用或用于管理用途，例如 Dell iDRAC 或 HPE iLO。

## 示例

### 示例 1

```powershell
Get-ClusterExcludedAdapter -ExclusionType "FriendlyName" 
```

这个示例根据友好名称（friendly name）检索出一列已被集群排除在使用范围之外的网络适配器。

## 参数

### -AsJob

将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，你可以继续在该会话中工作。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](/powershell/module/microsoft.powershell.core/about/about_jobs)。

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

在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如 `[New-CimSession](/powershell/module/cimcmdlets/new-cimsession)` 或 `[Get-CimSession](/powershell/module/cimcmdlets/get-cimsession)` cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -ExclusionType

指定要从集群中检索的排除类型的值。可选的值有：

- `IPPrefix`: Excludes a network adapter based on its IP address.
- `Description`: Excludes a network adapter based on its description.
- `FriendlyName`: Excludes a network adapter based on its friendly name.

```yaml
Type: AdapterExclusionType
Parameter Sets: (All)
Aliases:
Accepted values: IPPrefix, Description, FriendlyName

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit

指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，PowerShell 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或计算机本身。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.String[]

## 备注

## 相关链接

[Add-ClusterExcludedAdapter](add-clusterexcludedadapter.md)

[Remove-ClusterExcludedAdapter](remove-clusterexcludedadapter.md)

[修复-集群名称账户](repair-clusternameaccount.md)

[Set-ClusterExcludedAdapter](set-clusterexcludedadapter.md)
