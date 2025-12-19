---
external help file: Microsoft.ReFsDedup.Commands.dll-Help.xml
Module Name: Microsoft.ReFsDedup.Commands
ms.date: 11/20/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.refsdedup.commands/get-refsdedupschedule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ReFSDedupSchedule
---

# 获取ReFS数据去重计划

## 摘要
检索指定 ReFS 卷上的去重计划信息。

## 语法

```
Get-ReFSDedupSchedule [-Volume] <String> [<CommonParameters>]
```

## 描述

`Get-ReFSDedupSchedule` cmdlet 可以检索指定 ReFS 卷的重复数据删除计划。

## 示例

### 示例 1

```powershell
Get-ReFSDedupSchedule -Volume "D:"
```

这个示例检索了名为`D:`的ReFS卷的去重计划。

## 参数

### -Volume

指定用于检索去重计划的 ReFS 卷。可以输入一个或多个卷 ID、驱动器字母或卷 GUID 路径。对于驱动器字母，请使用格式 `D:`；对于卷 GUID 路径，请使用格式 `\\?\Volume{{GUID}}`。多个卷之间用逗号分隔。

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

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Clear-ReFSDedupSchedule](Clear-ReFSDedupSchedule.md)

[ Resume-ReFSDedupSchedule](Resume-ReFSDedupSchedule.md)

[Set-ReFSDedupSchedule](Set-ReFSDedupSchedule.md)

[暂停ReFSD去重计划](Suspend-ReFSDedupSchedule.md)
