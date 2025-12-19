---
external help file: Microsoft.ReFsDedup.Commands.dll-Help.xml
Module Name: Microsoft.ReFsDedup.Commands
ms.date: 11/20/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.refsdedup.commands/suspend-refsdedupschedule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Suspend-ReFSDedupSchedule
---

# 暂停 ReFSDedup 计划的执行

## 摘要
暂停指定ReFS卷上的去重操作计划。

## 语法

```
Suspend-ReFSDedupSchedule [-Volume] <String> [<CommonParameters>]
```

## 描述

`Suspend-ReFSDedupSchedule` cmdlet 用于暂停指定 ReFS 卷上的去重计划。当您暂停该计划时，在恢复计划之前将不会启动新的去重任务。

## 示例

### 示例 1

```powershell
Suspend-ReFSDedupSchedule -Volume "D:"
```

这个示例会暂停`D:` ReFS卷上的去重任务调度。

## 参数

### -Volume

指定要暂停 ReFS 去重计划的卷。可以输入一个或多个卷 ID、驱动器字母或卷 GUID 路径。使用驱动器字母时，格式为 `D:`；使用卷 GUID 路径时，格式为 `\\?\Volume{{GUID}}`。多个卷之间用逗号分隔。

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

[Resume-ReFSDedupSchedule](Resume-ReFSDedupSchedule.md)

[Set-ReFSDedupSchedule](Set-ReFSDedupSchedule.md)
