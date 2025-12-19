---
external help file: Microsoft.ReFsDedup.Commands.dll-Help.xml
Module Name: Microsoft.ReFsDedup.Commands
ms.date: 11/20/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.refsdedup.commands/resume-refsdedupschedule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Resume-ReFSDedupSchedule
---

# Resume-ReFSDedupSchedule

## 摘要
在指定的ReFS卷上恢复去重调度功能。

## 语法

```
Resume-ReFSDedupSchedule [-Volume] <String> [<CommonParameters>]
```

## 描述

`Resume-ReFSDedupSchedule` cmdlet 用于恢复已暂停或停止的指定 ReFS 卷上的去重计划。

## 示例

### 示例 1

```powershell
Resume-ReFSDedupSchedule -Volume "D:"
```

这个示例恢复了`D:` ReFS卷的去重计划。

## 参数

### -Volume

指定要恢复去重计划操作的 ReFS 卷。可以输入一个或多个卷 ID、驱动器字母或卷 GUID 路径。使用驱动器字母时，格式应为 `D:`；使用卷 GUID 路径时，格式应为 `\\?\Volume{{GUID}}`。多个卷之间用逗号分隔。

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

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Clear-ReFSDedupSchedule](Clear-ReFSDedupSchedule.md)

[Get-ReFSDedupSchedule](Get-ReFSDedupSchedule.md)

[Set-ReFSDedupSchedule](Set-ReFSDedupSchedule.md)

[Suspend-ReFSDedupSchedule](Suspend-ReFSDedupSchedule.md)
