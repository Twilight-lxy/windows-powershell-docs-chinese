---
external help file: Microsoft.ReFsDedup.Commands.dll-Help.xml
Module Name: Microsoft.ReFsDedup.Commands
ms.date: 11/20/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.refsdedup.commands/enable-refsdedup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-ReFSDedup
---

# 启用 ReFSD Dedup（重复数据删除功能）

## 摘要
启用对指定 ReFS 卷的数据去重功能。

## 语法

```
Enable-ReFSDedup [-Volume] <String> [-Type] <DedupVolumeType> [<CommonParameters>]
```

## 描述

`Enable-ReFSDedup` cmdlet 可以在指定的 ReFS 卷上启用数据去重功能。您可以使用 `-Type` 参数来指定要使用的去重类型。

## 示例

### 示例 1

```powershell
Enable-ReFSDedup -Volume "D:" -Type DedupAndCompress
```

这个示例可以在`D:` ReFS卷上同时实现数据去重和压缩功能。

### 示例 2

```powershell
Enable-ReFSDedup -Volume "E:, F:" -Type DedupAndCompress
```

这个示例可以在`E:`和`F:`这两个ReFS卷上同时实现数据去重和压缩功能。

## 参数

### -Type

指定要使用的去重类型。可接受的值有：

- `Compress`
- `Dedup`
- `DedupAndCompress`

```yaml
Type: DedupVolumeType
Parameter Sets: (All)
Aliases:
Accepted values: Dedup, DedupAndCompress, Compress

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Volume

Specifies the volume or volumes to enable ReFS data deduplication. Enter one or more volume IDs,
drive letters, or volume GUID paths. For drive letters, use the format `D:`. For volume GUID paths,
use the format `\\?\Volume{{GUID}}\`. Separate multiple volumes with a comma.

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

This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable,
-InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose,
-WarningAction, and -WarningVariable. For more information, see
[about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters).

## 输入

### None

## 输出

### System.Object

## 备注

## 相关链接

[Disable-ReFSDedup](Disable-ReFSDedup.md)
