---
external help file: Microsoft.ReFsDedup.Commands.dll-Help.xml
Module Name: Microsoft.ReFsDedup.Commands
ms.date: 11/20/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.refsdedup.commands/clear-refsdedupscrubschedule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-ReFSDedupScrubSchedule
---

# 清除 ReFSD 的重复数据扫描计划

## 摘要
清除指定 ReFS 卷上的去重清理计划。

## 语法

```
Clear-ReFSDedupScrubSchedule [-Volume] <String> [<CommonParameters>]
```

## 描述

`Clear-ReFSDedupScrubSchedule` cmdlet 用于清除指定 ReFS 卷上的去重扫描计划。清除该计划后，所有待处理的扫描任务都将被取消，并且该计划会被重置。

## 示例

### 示例 1

```powershell
Clear-ReFSDedupScrubSchedule -Volume "D:"
```

这个示例清除了`D:` ReFS卷上的去重清洗计划（deduplication scrub schedule）。

## 参数

### -Volume

指定要清除 ReFS 重复数据删除扫描计划（deduplication scrub schedule）的卷。可以输入一个或多个卷 ID、驱动器字母或卷 GUID 路径。对于驱动器字母，请使用格式 `D:`；对于卷 GUID 路径，请使用格式 `\\?\Volume{{GUID}}`。多个卷之间用逗号分隔。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Get-ReFSDedupScrubSchedule](Get-ReFSDedupScrubSchedule.md)

[Set-ReFSDedupScrubSchedule](Set-ReFSDedupScrubSchedule.md)
