---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterStorageSpacesDirect.cdxml-help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/set-clusterstoragespacesdirect?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ClusterStorageSpacesDirect
---

# 设置集群存储空间（直接方式）

## 摘要
设置S2D缓存参数。

## 语法

```
Set-ClusterStorageSpacesDirect [-CacheState <CacheStateType>] [-CacheModeHDD <CacheModeType>]
 [-CacheModeSSD <CacheModeType>] [-Nodes <String[]>] [-SkipEligibilityChecks]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

`Set-ClusterStorageSpacesDirect` cmdlet 用于设置 Storage Spaces Direct (S2D) 的缓存参数。

## 示例

### 示例 1：设置 S2D 缓存参数

```powershell
Set-ClusterStorageSpacesDirect -CimSession "cluster01.contoso.com" -CacheModeHDD ReadWrite
```

以下命令将名为 `cluster01.contoso.com` 的集群中的 S2D 缓存参数设置为“读写”（ReadWrite）模式。

## 参数

### -AsJob

将 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -CacheModeHDD

指定硬盘驱动器的缓存模式。该参数的可接受值包括：

- `ReadOnly`
- `WriteOnly`
- `ReadWrite`

```yaml
Type: CacheModeType
Parameter Sets: (All)
Aliases:
Accepted values: ReadOnly, WriteOnly, ReadWrite

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CacheModeSSD

Specifies the cache mode of the solid state drive. The acceptable values for this parameter are:

- `ReadOnly`
- `WriteOnly`
- `ReadWrite`

```yaml
Type: CacheModeType
Parameter Sets: (All)
Aliases:
Accepted values: ReadOnly, WriteOnly, ReadWrite

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CacheState

Specifies the S2D cache state. The acceptable values for this parameter are: `Enabled` or
`Disabled`. The default value is `Enabled`.

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

Runs the cmdlet in a remote session or on a remote computer. Enter a computer name or a session
object, such as the output of a [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)
or [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet. The default is the
current session on the local computer.

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

### -Nodes

Specifies, as a string array, the nodes on which this operation takes place.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SkipEligibilityChecks

Indicates that the cmdlet skips cache eligibility checks. If cache stores are found with data
partitions on them, then you can use `Enable-ClusterStorageSpacesDirect` with the cache state as
Disabled but not as ReadOnly or ReadWrite.

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

该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或整个计算机。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Disable-ClusterStorageSpacesDirect](./Disable-ClusterStorageSpacesDirect.md)

[Enable-ClusterStorageSpacesDirect](./Enable-ClusterStorageSpacesDirect.md)

[Get-ClusterStorageSpacesDirect](./Get-ClusterStorageSpacesDirect.md)
