---
external help file: Microsoft.ReFsDedup.Commands.dll-Help.xml
Module Name: Microsoft.ReFsDedup.Commands
ms.date: 11/20/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.refsdedup.commands/get-refsdedupstatus?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ReFSDedupStatus
---

# 获取ReFS去重状态信息

## 摘要
检索指定ReFS卷上的数据去重状态。

## 语法

```
Get-ReFSDedupStatus [-Volume] <String> [<CommonParameters>]
```

## 描述

`Get-ReFSDedupStatus` cmdlet 可以获取指定 ReFS 卷上的数据去重状态。

## 示例

### 示例 1

```powershell
Get-ReFSDedupStatus -Volume "D:"
```

这个示例用于检索`D:` ReFS卷的去重状态。

### 示例 2

```powershell
$Volumes = "E:", "F:"
foreach ($Volume in $Volumes) {
   Get-ReFSDedupStatus -Volume $Volume
}
```

这个示例会检索 `E:` 和 `F:` 类型的 ReFS 卷的去重状态。

## 参数

### -Volume

指定要获取去重状态的 ReFS 卷。可以输入一个或多个卷 ID、驱动器字母或卷 GUID 路径。对于驱动器字母，使用格式 `D:`；对于卷 GUID 路径，使用格式 `\\?\Volume{{GUID}}\`。多个卷之间用逗号分隔。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接
