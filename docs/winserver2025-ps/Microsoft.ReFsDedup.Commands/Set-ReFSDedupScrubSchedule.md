---
external help file: Microsoft.ReFsDedup.Commands.dll-Help.xml
Module Name: Microsoft.ReFsDedup.Commands
ms.date: 11/20/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.refsdedup.commands/set-refsdedupscrubschedule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ReFSDedupScrubSchedule
---

# 设置 ReFSDedupScrubSchedule 的计划

## 摘要
在指定的 ReFS 卷上设置去重清理计划。

## 语法

```
Set-ReFSDedupScrubSchedule [-Volume] <String> -Start <DateTime> -Days <DaysOfWeek>
 -WeeksInterval <UInt16> [-DedupDataOnly <Boolean>] [<CommonParameters>]
```

## 描述

`Set-ReFSDedupScrubSchedule` cmdlet 用于设置指定 ReFS 卷的重复数据删除（deduplication）清理计划。该清理计划决定了在卷上运行清理任务的时间和频率。

## 示例

### 示例 1

```powershell
$params = @{
    Volume        = "D:"
    Start         = "12/01/2024 8:00 AM"
    Days          = "Monday,Thursday"
    WeeksInterval = 2
}
Set-ReFSDedupScrubSchedule @params
```

这个示例将去重清理任务的调度设置为在 `D:` ReFS 卷上每逢周一和周四的早上 8:00 运行，从 2024 年 12 月 1 日开始，并且每周运行两次。

## 参数

### -Days

指定每周哪些天要运行数据清洗任务。可接受的值包括：

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

### -DedupDataOnly

指定是否仅在数据清洗计划中包含已去重的数据。

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

### -Start

指定用于开始数据清洗计划的日期和时间。

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

指定用于设置去重清理计划的 ReFS 卷。可以输入一个或多个卷 ID、驱动器字母或卷 GUID 路径。对于驱动器字母，请使用格式 `D:`；对于卷 GUID 路径，请使用格式 `\\?\Volume{{GUID}}`。多个卷之间用逗号分隔。

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

### -WeeksInterval

指定每次执行数据清洗（scrub）任务之间的时间间隔（以周为单位）。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Clear-ReFSDedupScrubSchedule](Clear-ReFSDedupScrubSchedule.md)

[Get-ReFSDedupScrubSchedule](Get-ReFSDedupScrubSchedule.md)
