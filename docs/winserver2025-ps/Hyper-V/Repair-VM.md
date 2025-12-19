---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/repair-vm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Repair-VM
---

# 修复虚拟机

## 摘要
修复一台或多台虚拟机。

## 语法

```
Repair-VM [-CompatibilityReport] <VMCompatibilityReport> [-SnapshotFilePath <String>] [-Path <String>]
 [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Repair-VM` cmdlet 可以修复一些可能会影响虚拟机导入或迁移操作的问题。如果 `Compare-VM` 确定某个虚拟机的导入或迁移操作会失败，它会返回一系列需要解决的不兼容性问题，只有解决了这些问题后，该操作才能成功执行。大多数这类不兼容性问题可以通过使用 `Set-VM` 来修复。不过，`Set-VM` 并不会修改存储虚拟机配置文件的路径或存储快照文件的路径。而 `Repair-VM` 则专门用于处理这两种特定的问题。

## 示例

### 示例 1
```
PS C:\> Repair-VM -CompatibilityReport $VMCompatReport -Path C:\Test
```

这个示例修改了用于生成虚拟机兼容性报告的配置路径。

### 示例 2
```
PS C:\> Repair-VM -CompatibilityReport $VMCompatReport -SnapshotFilePath C:\Snapshots
```

这个示例用于为虚拟机兼容性报告添加缺失的快照。

## 参数

### -CompatibilityReport
指定一份兼容性报告，其中包含在修复过程中需要进行的调整措施。

```yaml
Type: VMCompatibilityReport
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定将某个对象传递给管道，该管道用于表示新修改后的兼容性报告。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定需要修复的虚拟机的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SnapshotFilePath
指定用于搜索虚拟机快照的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases: CheckpointFileLocation, SnapshotFileLocation

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生的结果。但实际上，这个cmdlet并没有被执行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.CompatibilityReport
如果指定了**-PassThru**选项……

## 备注

## 相关链接

