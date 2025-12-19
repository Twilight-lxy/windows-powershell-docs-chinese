---
external help file: Microsoft.ReFsDedup.Commands.dll-Help.xml
Module Name: Microsoft.ReFsDedup.Commands
ms.date: 11/20/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.refsdedup.commands/start-refsdedupjob?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-ReFSDedupJob
---

# 启动 ReFSDedupJob 任务

## 摘要
在指定的 ReFS 卷上启动一个去重任务。

## 语法

```
Start-ReFSDedupJob [-Volume] <String> [-Duration <TimeSpan>] [-FullRun] [-CpuPercentage <UInt32>]
 [-ConcurrentOpenFiles <UInt32>] [-MinimumLastModifiedTimeHours <Int32>]
 [-ExcludeFileExtension <String[]>] [-ExcludeFolder <String[]>] [-CompressionFormat <Format>]
 [-CompressionLevel <UInt16>] [-CompressionChunkSize <UInt32>] [-CompressionTuning <UInt32>]
 [-RecompressionTuning <UInt32>] [-DecompressionTuning <UInt32>] [<CommonParameters>]
```

## 描述

`Start-ReFSDedupJob` cmdlet 会在指定的 ReFS 卷上启动一个去重任务，或者恢复之前被暂停或停止的现有去重任务。

## 示例

### 示例 1

```powershell
Start-ReFSDedupJob -Volume "D:"
```

这个示例使用默认设置，在`D:`驱动器上启动了一个去重任务。

## 参数

### -CompressionChunkSize

指定在压缩过程中使用的块大小。

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

### -CompressionFormat

指定在任务执行过程中使用的压缩格式。可接受的值包括：

- `LZ4`
- `Uncompressed`
- `Unknown`
- `ZSTD`

```yaml
Type: Format
Parameter Sets: (All)
Aliases:
Accepted values: Unknown, Uncompressed, LZ4, ZSTD

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CompressionLevel

指定在作业过程中使用的压缩级别。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CompressionTuning

指定在作业执行过程中使用的压缩调整参数。

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

### -ConcurrentOpenFiles

指定在任务执行过程中可以同时打开的最大文件数量。

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

### -CpuPercentage

指定在执行作业期间允许使用的最大CPU利用率（以百分比表示）。

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

### -DecompressionTuning

指定在作业执行过程中使用的解压优化参数（即解压调优设置）。

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

### -Duration

指定作业的持续时间。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExcludeFileExtension

指定一个或多个文件扩展名，以排除在作业处理之外。

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

### -ExcludeFolder

指定一个或多个要从任务中排除的文件夹。

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

### -FullRun

该参数用于指示是否对指定的 ReFS 卷执行完整的去重操作。如果未指定此参数，作业将以增量模式运行，仅处理新文件或已更改的文件。

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

### -MinimumLastModifiedTimeHours

指定文件在可以被去重之前必须经过的最短时间（以小时为单位）。

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

### -RecompressionTuning

指定在去重过程中使用的重新压缩调整参数。

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

### -Volume

指定用于运行任务的 ReFS 卷。可以输入一个或多个卷 ID、驱动器字母或卷 GUID 路径。对于驱动器字母，请使用格式 `D:`；对于卷 GUID 路径，请使用格式 `\\?\Volume{{GUID}}`。多个卷之间用逗号分隔。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
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

[Stop-ReFSDedupJob](Stop-ReFSDedupJob.md)
