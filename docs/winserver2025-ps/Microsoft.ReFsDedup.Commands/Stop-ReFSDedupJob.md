---
external help file: Microsoft.ReFsDedup.Commands.dll-Help.xml
Module Name: Microsoft.ReFsDedup.Commands
ms.date: 11/20/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.refsdedup.commands/stop-refsdedupjob?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-ReFSDedupJob
---

# 停止 ReFSD DedupJob 任务

## 摘要
停止在指定的 ReFS 卷上正在运行的去重作业。

## 语法

```
Stop-ReFSDedupJob [-Volume] <String> [<CommonParameters>]
```

## 描述

`Stop-ReFSDedupJob` cmdlet 用于停止正在指定的 ReFS 卷上运行的去重作业。

## 示例

### 示例 1

```powershell
Stop-ReFSDedupJob -Volume "D:"
```

这个示例会停止对 `D:` ReFS 卷进行的去重操作。

## 参数

### -Volume

指定要停止去重操作的 ReFS 卷。输入一个或多个卷 ID、驱动器字母或卷 GUID 路径。对于驱动器字母，使用格式 `D:`；对于卷 GUID 路径，使用格式 `\\?\Volume{{GUID}}`。多个卷之间用逗号分隔。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[开始ReFSDedupJob任务](Start-ReFSDedupJob.md)
