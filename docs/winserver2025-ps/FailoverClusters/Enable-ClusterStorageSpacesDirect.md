---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Storage Spaces Direct。
external help file: ClusterStorageSpacesDirect.cdxml-help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/enable-clusterstoragespacesdirect?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-ClusterStorageSpacesDirect
---

# 启用 ClusterStorageSpacesDirect 功能

## 摘要
在故障转移集群上启用“Storage Spaces Direct”功能。

## 语法

### 自动

```
Enable-ClusterStorageSpacesDirect [-PoolFriendlyName <String>] [-Autoconfig <Boolean>]
 [-CacheState <CacheStateType>] [-CacheMetadataReserveBytes <UInt64>]
 [-CachePageSizeKBytes <UInt32>] [-SkipEligibilityChecks] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### WithXML

```
Enable-ClusterStorageSpacesDirect [-PoolFriendlyName <String>] [-Autoconfig <Boolean>]
 [-CacheState <CacheStateType>] [-CacheMetadataReserveBytes <UInt64>]
 [-CachePageSizeKBytes <UInt32>] [-SkipEligibilityChecks] -XML <String> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### WithCacheDeviceModel

```
Enable-ClusterStorageSpacesDirect [-PoolFriendlyName <String>] [-Autoconfig <Boolean>]
 [-CacheState <CacheStateType>] [-CacheMetadataReserveBytes <UInt64>]
 [-CachePageSizeKBytes <UInt32>] [-SkipEligibilityChecks] -CacheDeviceModel <String[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Enable-ClusterStorageSpacesDirect` cmdlet 可以在集群上启用高可用性的存储空间（Storage Spaces），这些存储空间直接使用直接附加的存储技术——即 Storage Spaces Direct (S2D)。

## 示例

### 示例 1：启用 Storage Spaces Direct 功能

```powershell
Enable-ClusterStorageSpacesDirect
```

此命令在集群上启用S2D功能。

### 示例 2：通过指定友好名称来启用“Storage Spaces Direct”功能

```powershell
Enable-ClusterStorageSpacesDirect -PoolFriendlyName 'Sales'
```

此命令在集群上启用S2D功能，并为Storage Spaces Direct池设置一个易于识别的名称。

## 参数

### -AsJob

将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个代表该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -Autoconfig

此参数表示应自动创建并配置存储池。如果在启用 Storage Spaces Direct 之前该存储池已经存在，那么 **AutoConfig** 参数将不起作用（即不会执行任何操作）。默认情况下，**AutoConfig** 的值为 true。如果您不希望存储池被自动创建，而希望手动创建它，应将 **AutoConfig** 设置为 false。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CacheDeviceModel

指定一组应被 Storage Spaces Direct 缓存使用的磁盘型号。如果省略此参数，系统会自动确定用于该操作的磁盘。

```yaml
Type: String[]
Parameter Sets: WithCacheDeviceModel
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CacheMetadataReserveBytes

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CachePageSizeKBytes

指定用于 Storage Spaces Direct 缓存的页面大小。此参数有助于控制用于管理这些页面所需的内存占用。为了降低拥有大量存储空间的系统的内存开销，可以将页面大小增加到 32 千字节（KB）甚至 64 KB。默认值为 16 KB，在大多数系统中这代表了较好的折中方案。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:
Accepted values: 8, 16, 32, 64

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CacheState

用于指定 Storage Spaces Direct 的缓存状态。该参数的可接受值为：`Enabled`（启用）或 `Disabled`（禁用）。默认值为 `Enabled`。

```yaml
Type: CacheStateType
Parameter Sets: (All)
Aliases:
Accepted values: Disabled, Enabled

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession

在远程会话或远程计算机上运行该cmdlet。输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -Confirm

在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -PoolFriendlyName

指定在创建 Storage Spaces Direct 池时使用的友好名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SkipEligibilityChecks

表示此cmdlet会跳过缓存资格检查。

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

该参数用于指定可以同时运行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell 会根据计算机上正在运行的 CIM 命令的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的命令，而不适用于整个会话或计算机本身。

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

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -XML

指定包含存储支持配置信息的XML文件。

```yaml
Type: String
Parameter Sets: WithXML
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[ Disable-ClusterStorageSpacesDirect](./Disable-ClusterStorageSpacesDirect.md)

[Get-ClusterStorageSpacesDirect](./Get-ClusterStorageSpacesDirect.md)

[Set-ClusterStorageSpacesDirect](./Set-ClusterStorageSpacesDirect.md)

[Get-Cluster](./Get-Cluster.md)
