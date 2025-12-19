---
external help file: Microsoft.ReFsDedup.Commands.dll-Help.xml
Module Name: Microsoft.ReFsDedup.Commands
ms.date: 11/20/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.refsdedup.commands/get-refsdedupscrubschedule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ReFSDedupScrubSchedule
---

# 获取 ReFSD 重复数据删除和清理计划

## 摘要
检索指定 ReFS 卷上的去重清理计划。

## 语法

```
Get-ReFSDedupScrubSchedule [-Volume] <String> [<CommonParameters>]
```

## 描述

`Get-ReFSDedupScrubSchedule` cmdlet 用于检索指定 ReFS 卷上的重复数据删除清理计划。

## 示例

### 示例 1

```powershell
Get-ReFSDedupScrubSchedule -Volume "D:"
```

这个示例用于获取`D:` ReFS卷上的去重清理计划（即去重操作的执行时间表）。

## 参数

### -Volume

用于指定要从中检索 ReFS 去重清理计划的卷。可以输入一个或多个卷 ID、驱动器字母或卷 GUID 路径。对于驱动器字母，请使用格式 `D:`；对于卷 GUID 路径，请使用格式 `\\?\Volume{{GUID}}`。多个卷之间用逗号分隔。

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

[Clear-ReFSDedupScrubSchedule](Clear-ReFSDedupScrubSchedule.md)

[Set-ReFSDedupScrubSchedule](Set-ReFSDedupScrubSchedule.md)
