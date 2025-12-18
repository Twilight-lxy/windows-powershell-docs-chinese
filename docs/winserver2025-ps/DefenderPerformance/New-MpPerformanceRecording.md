---
external help file: MSFT_MpPerformanceRecording.psm1-help.xml
Module Name: DefenderPerformance
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/defenderperformance/new-mpperformancerecording?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-MpPerformanceRecording
---

# New-MpPerformanceRecording

## 摘要
这个cmdlet用于收集Microsoft Defender Antivirus扫描的性能记录数据。

## 语法

### 交互式（默认设置）

```
New-MpPerformanceRecording -RecordTo <String> [-Session <PSSession[]>] [-WPRPath <String>]
 [<CommonParameters>]
```

### 定时（Timed）

```
New-MpPerformanceRecording -RecordTo <String> -Seconds <Int32> [-Session <PSSession[]>]
[-WPRPath <String>] [<CommonParameters>]
```

## 描述

此cmdlet用于收集Microsoft Defender Antivirus扫描的性能记录。这些性能记录包含了与Microsoft-Antimalware-Engine及NT内核进程相关的事件，可以通过使用Get-MpPerformanceReport cmdlet在收集后对这些记录进行进一步分析。

此cmdlet需要提升的管理员权限才能执行。

性能分析器可以帮助您识别可能导致 Microsoft Defender 防病毒软件性能下降的问题文件。该工具按“现状”提供，不旨在为您提供关于如何进行文件排除（即不再将某些文件视为潜在威胁）的建议。进行文件排除操作可能会降低终端设备的安全保护级别；因此，如果确实需要排除某些文件，请务必谨慎操作。

## 示例

### 示例 1

```
New-MpPerformanceRecording -RecordTo:.\Defender-scans.etl
```

## 参数

### -RecordTo

指定用于保存 Microsoft Defender Antivirus 性能记录文件的位置。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Seconds

以秒为单位指定表演录制的持续时间。

```yaml
Type: System.Int32
Parameter Sets: Timed
Aliases:

Required: True
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -Session

指定用于创建和保存 Microsoft Defender Antivirus 性能记录的 PSSession 对象。使用此参数时，RecordTo 参数指的是远程机器上的本地路径。

```yaml
Type: System.Management.Automation.Runspaces.PSSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WPRPath

可选参数用于指定用于记录追踪数据的不同工具。默认值为 wpr.exe。当使用 $Session 参数时，该路径表示远程机器上的一个位置。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接
