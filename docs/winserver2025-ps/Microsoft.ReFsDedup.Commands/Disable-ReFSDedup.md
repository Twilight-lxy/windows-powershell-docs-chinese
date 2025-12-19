---
external help file: Microsoft.ReFsDedup.Commands.dll-Help.xml
Module Name: Microsoft.ReFsDedup.Commands
ms.date: 11/20/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.refsdedup.commands/disable-refsdedup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-ReFSDedup
---

# 禁用 ReFS SD Dedup 功能

## 摘要
禁用指定 ReFS 卷上的数据去重功能。

## 语法

```
Disable-ReFSDedup [-Volume] <String> [<CommonParameters>]
```

## 描述

` Disable-ReFSDedup` cmdlet 用于禁用指定 ReFS 卷上的数据去重功能。该 cmdlet 不会影响卷上已存在的去重文件或文件夹，但会阻止新文件或文件夹被进行去重处理。

## 示例

### 示例 1

```powershell
Disable-ReFSDedup -Volume "D:"
```

这个示例禁用了`D:` ReFS卷上的数据去重功能。

## 参数

### -Volume

指定要禁用 ReFS 数据去重功能的卷。可以输入一个或多个卷 ID、驱动器字母或卷 GUID 路径。对于驱动器字母，请使用格式 `D:`；对于卷 GUID 路径，请使用格式 `\\?\Volume{{GUID}}`。多个卷之间请用逗号分隔。

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

[启用ReFS去重功能](Enable-ReFSDedup.md)
