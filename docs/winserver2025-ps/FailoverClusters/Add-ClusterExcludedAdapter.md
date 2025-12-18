---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 08/28/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clusterexcludedadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterExcludedAdapter
---

# 添加被排除在集群外的适配器

## 摘要
将一个网络适配器添加到被排除的适配器列表中。

## 语法

```
Add-ClusterExcludedAdapter -ExclusionType <AdapterExclusionType> -ExclusionValue <String[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

`Add-ClusterExcludedAdapter` cmdlet 将一个网络适配器添加到应被故障转移集群排除使用的网络适配器列表中。默认情况下，集群会使用所有可用的网络适配器，但在某些情况下，您可能希望将某些适配器保留用于备份或管理用途，例如 Dell iDRAC 或 HPE iLO。

## 示例

### 示例 1

```powershell
Add-ClusterExcludedAdapter -ExclusionType "IPPrefix" -ExclusionValue "10.10.20.25"
```

这个示例会将基于 IP 地址 `10.10.20.25` 的网络适配器从集群的使用中排除出去。

## 参数

### -AsJob

以后台作业的形式运行该cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](/powershell/module/microsoft.powershell.core/about/about_jobs)。

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

在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如[New-CimSession](/powershell/module/cimcmdlets/new-cimsession)或[Get-CimSession](/powershell/module/cimcmdlets/get-cimsession) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

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

指定要添加到集群中的排除类型。可接受的值有：

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

### -ExclusionValue

指定用于排除的值。该参数的值取决于 `-ExclusionType` 参数的值。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，PowerShell 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值（即并发操作的数量）。此限制仅适用于当前正在运行的 cmdlet，而不影响整个会话或计算机本身。

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

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Get-ClusterExcludedAdapter](get-clusterexcludedadapter.md)

[Remove-ClusterExcludedAdapter](remove-clusterexcludedadapter.md)

[修复-ClusterNameAccount](repair-clusternameaccount.md)

[Set-ClusterExcludedAdapter](set-clusterexcludedadapter.md)
