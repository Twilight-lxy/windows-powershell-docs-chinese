---
external help file: Microsoft.ReFsDedup.Commands.dll-Help.xml
Module Name: Microsoft.ReFsDedup.Commands
ms.date: 11/20/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.refsdedup.commands/clear-refsdedupschedule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-ReFSDedupSchedule
---

# 清除 ReFS 的重复数据调度任务

## 摘要
清除指定 ReFS 卷上用于去重操作的计划任务。

## 语法

```
Clear-ReFSDedupSchedule [-Volume] <String> [<CommonParameters>]
```

## 描述

`Clear-ReFSDedupSchedule` cmdlet 会清除在指定的 ReFS 卷上用于去重操作的定时任务，包括该定时任务本身。

## 示例

### 示例 1

```powershell
Clear-ReFSDedupSchedule -Volume "D:"
```

这个示例会清除为卷 `D` 安排好的任务。

## 参数

### -Volume

指定要清除计划优化任务的卷。输入一个或多个卷ID、驱动器字母或卷GUID路径。对于驱动器字母，请使用格式“D:”。对于卷GUID路径，请使用格式“\\?\Volume{{GUID}}”。用逗号分隔多个卷。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Get-ReFSDedupSchedule](Get-ReFSDedupSchedule.md)

[Resume-ReFSDedupSchedule]( Resume-ReFSDedupSchedule.md)

[Set-ReFSDedupSchedule](Set-ReFSDedupSchedule.md)

[暂停ReFSD去重计划](Suspend-ReFSDedupSchedule.md)
