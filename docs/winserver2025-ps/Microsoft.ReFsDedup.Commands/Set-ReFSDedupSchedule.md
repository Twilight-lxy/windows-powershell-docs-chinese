---
external help file: Microsoft.ReFsDedup.Commands.dll-Help.xml
Module Name: Microsoft.ReFsDedup.Commands
ms.date: 11/20/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.refsdedup.commands/set-refsdedupschedule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ReFSDedupSchedule
---

# 设置 ReFSD 的去重计划（Set-ReFSDedupSchedule）

## 摘要
为指定的 ReFS 卷设置去重计划。

## 语法

```
Set-ReFSDedupSchedule [-Volume] <String> -Start <DateTime> [-Duration <TimeSpan>] -Days <DaysOfWeek>
 [-CpuPercentage <UInt32>] [-ConcurrentOpenFiles <UInt32>] [-MinimumLastModifiedTimeHours <Int32>]
 [-ExcludeFileExtension <String[]>] [-ExcludeFolder <String[]>] [-CompressionFormat <Format>]
 [-CompressionLevel <UInt16>] [-CompressionChunkSize <UInt32>] [-CompressionTuning <UInt32>]
 [-RecompressionTuning <UInt32>] [-DecompressionTuning <UInt32>] [<CommonParameters>]
```

## 描述

`Set-ReFSDedupSchedule` cmdlet 用于设置指定 ReFS 卷的重复数据删除（deduplication）计划。您可以使用此 cmdlet 来指定重复数据删除应在何时以及多久执行一次。

## 示例

### 示例 1

```powershell
Set-ReFSDedupSchedule -Volume "D:" -Start "10:00 PM" -Days Monday,Wednesday,Friday -Duration 4:00:00
```

这个示例将 `D:` ReFS 卷的去重计划设置为在每周一、周三和周五晚上 10 点运行，每次运行时间为 4 小时。

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

指定在去重过程中使用的压缩格式。可接受的值有：

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

指定在去重过程中使用的压缩级别。

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

指定在去重过程中使用的压缩调整参数。

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

指定在进行去重操作时可以同时打开的最大文件数量。

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

指定去重操作所占用的CPU使用量的最大百分比。

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

### -Days

指定每周应执行数据去重操作的日子。可接受的值包括：

- `None`
- `EveryDay`
- `Monday`
- `Tuesday`
- `Wednesday`
- `Thursday`
- `Friday`
- `Saturday`
- `Sunday`

```yaml
Type: DaysOfWeek
Parameter Sets: (All)
Aliases:
Accepted values: None, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, EveryDay

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DecompressionTuning

指定在去重过程中使用的解压调整参数。

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

指定卷上的去重操作应运行的持续时间。

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

指定一个或多个文件扩展名，以排除在去重操作之外。

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

指定一个或多个要排除在去重操作之外的文件夹。

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

### -MinimumLastModifiedTimeHours

指定文件在被去重之前必须经过的最少时间（以小时为单位）。

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

### -Start

指定卷上应开始运行去重操作的日期和时间。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Volume

指定要设置去重计划的 ReFS 卷。输入一个或多个卷 ID、驱动器字母或卷 GUID 路径。对于驱动器字母，使用格式 `D:`；对于卷 GUID 路径，使用格式 `\\?\Volume{{GUID}}`。多个卷之间用逗号分隔。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Clear-ReFSDedupSchedule](Clear-ReFSDedupSchedule.md)

[Get-ReFSDedupSchedule](Get-ReFSDedupSchedule.md)

[ Resume-ReFSDedupSchedule](Resume-ReFSDedupSchedule.md)

[暂停ReFSD去重计划](Suspend-ReFSDedupSchedule.md)
