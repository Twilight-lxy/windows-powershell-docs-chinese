---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 08/28/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusters/remove-clusterexcludedadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ClusterExcludedAdapter
---

# 移除被排除在集群之外的适配器

## 摘要
从被排除的适配器列表中移除一个网络适配器。

## 语法

```
Remove-ClusterExcludedAdapter -ExclusionType <AdapterExclusionType> -ExclusionValue <String[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

`Remove-ClusterExcludedAdapter` cmdlet 用于从不应被故障转移集群使用的网络适配器列表中删除某个网络适配器。默认情况下，集群会使用所有可用的网络适配器；但在某些情况下，您可能需要将某些适配器保留下来用作备份或管理工具，例如 Dell iDRAC 或 HPE iLO。

## 示例

### 示例 1

```powershell
Remove-ClusterExcludedAdapter -ExclusionType "IPPrefix" -ExclusionValue "10.10.20.25"
```

这个示例会将基于IP地址`10.10.20.25`的网络适配器从被排除的适配器列表中移除。

## 参数

### -AsJob

将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的任务。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成的过程中，您可以继续在该会话中工作。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务 (About Jobs)](/powershell/module/microsoft.powershell.core/about/about_jobs)。

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

在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称或会话对象（例如 `[New-CimSession](/powershell/module/cimcmdlets/new-cimsession)` 或 `[Get-CimSession](/powershell/module/cimcmdlets/get-cimsession)` cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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

指定要从集群中移除的排除类型。可接受的值包括：

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

指定用于排除的值。此参数的值取决于 `-ExclusionType` 参数的值。

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

指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值`0`，PowerShell将根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。此限制仅适用于当前运行的cmdlet，而不适用于整个会话或计算机。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Add-ClusterExcludedAdapter](add-clusterexcludedadapter.md)

[Get-ClusterExcludedAdapter](get-clusterexcludedadapter.md)

[修复-ClusterNameAccount](repair-clusternameaccount.md)

[Set-ClusterExcludedAdapter](set-clusterexcludedadapter.md)
