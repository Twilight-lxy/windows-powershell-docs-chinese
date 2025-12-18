---
external help file: MSFT_MpPerformanceRecording.psm1-help.xml
Module Name: DefenderPerformance
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/defenderperformance/get-mpperformancereport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-MpPerformanceReport
---

# 获取 MP 性能报告

## 摘要
此cmdlet会报告对Microsoft Defender Antivirus扫描影响最大的文件路径、文件扩展名以及相关进程。

## 语法

```
Get-MpPerformanceReport [-Path] <String> [-TopFiles <Int32>] [-TopScansPerFile <Int32>]
 [-TopProcessesPerFile <Int32>] [-TopScansPerProcessPerFile <Int32>] [-TopPaths <Int32>]
 [-TopPathsDepth <Int32>] [-TopScansPerPath <Int32>] [-TopFilesPerPath <Int32>]
 [-TopScansPerFilePerPath <Int32>] [-TopExtensionsPerPath <Int32>]
 [-TopScansPerExtensionPerPath <Int32>] [-TopProcessesPerPath <Int32>]
 [-TopScansPerProcessPerPath <Int32>] [-TopExtensions <Int32>] [-TopScansPerExtension <Int32>]
 [-TopPathsPerExtension <Int32>] [-TopScansPerPathPerExtension <Int32>]
 [-TopFilesPerExtension <Int32>] [-TopScansPerFilePerExtension <Int32>]
 [-TopProcessesPerExtension <Int32>] [-TopScansPerProcessPerExtension <Int32>]
 [-TopProcesses <Int32>] [-TopScansPerProcess <Int32>] [-TopFilesPerProcess <Int32>]
 [-TopScansPerFilePerProcess <Int32>] [-TopExtensionsPerProcess <Int32>]
 [-TopScansPerExtensionPerProcess <Int32>] [-TopPathsPerProcess <Int32>]
 [-TopScansPerPathPerProcess <Int32>] [-TopScans <Int32>] [-MinDuration <String>]
 [-MinStartTime <DateTime>] [-MinEndTime <DateTime>] [-MaxStartTime <DateTime>]
 [-MaxEndTime <DateTime>] [-Overview] [-Raw] [<CommonParameters>]
```

## 描述

这个cmdlet用于分析之前收集的Microsoft Defender Antivirus性能记录，并报告对Microsoft Defender Antivirus扫描影响最大的文件路径、文件扩展名以及相关进程。

性能分析工具可以帮助识别可能导致微软Defender防病毒软件性能下降的问题文件。该工具按“现状”提供，不旨在提供建议来指导哪些文件应该被排除在防护范围之外。排除某些文件可能会降低终端设备的安全保护水平；因此，如果有需要排除的文件，应谨慎操作。

## 示例

### 示例 1

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopFiles:10 -TopExtensions:10 -TopProcesses:10 -TopScans:10
```

### 示例 2

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopFiles:10 -TopExtensions:10 -TopProcesses:10 -TopScans:10 -Raw | ConvertTo-Json
```

### 示例 3

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopScans:10
```

### 示例 4

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopFiles:10
```

### 示例 5

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopFiles:10 -TopScansPerFile:3
```

### 示例 6

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopFiles:10 -TopProcessesPerFile:3
```

### 示例 7

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopFiles:10 -TopProcessesPerFile:3 -TopScansPerProcessPerFile:3
```

### 示例 8

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10
```

### 示例 9

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10 -TopPathsDepth:3
```

### 示例 10

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10 -TopPathsDepth:3 -TopScansPerPath:3
```

### 示例 11

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10 -TopScansPerPath:3
```

### 示例 12

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10 -TopPathsDepth:3 -TopFilesPerPath:3
```

### 示例 13

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10 -TopFilesPerPath:3
```

### 示例 14

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10 -TopPathsDepth:3 -TopFilesPerPath:3 -TopScansPerFilePerPath:3
```

### 示例 15

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10 -TopFilesPerPath:3 -TopScansPerFilePerPath:3
```

### 示例 16

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10 -TopPathsDepth:3 -TopExtensionsPerPath:3
```

### 示例 17

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10 -TopExtensionsPerPath:3
```

### 示例 18

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10 -TopPathsDepth:3 -TopExtensionsPerPath:3 -TopScansPerExtensionPerPath:3
```

### 示例 19

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10 -TopExtensionsPerPath:3 -TopScansPerExtensionPerPath:3
```

### 示例 20

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10 -TopPathsDepth:3 -TopProcessesPerPath:3
```

### 示例 21

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10 -TopProcessesPerPath:3
```

### 示例 22

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10 -TopPathsDepth:3 -TopProcessesPerPath:3 -TopScansPerProcessPerPath:3
```

### 示例 23

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopPaths:10 -TopProcessesPerPath:3 -TopScansPerProcessPerPath:3
```

### 示例 24

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopExtensions:10
```

### 示例 25

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopExtensions:10 -TopScansPerExtension:3
```

### 示例 26

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopExtensions:10 -TopPathsPerExtension:3
```

### 示例 27

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopExtensions:10 -TopPathsPerExtension:3 -TopPathsDepth:3
```

### 示例 28

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopExtensions:10 -TopPathsPerExtension:3 -TopPathsDepth:3 -TopScansPerPathPerExtension:3
```

### 示例 29

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopExtensions:10 -TopPathsPerExtension:3 -TopScansPerPathPerExtension:3
```

### 示例 30

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopExtensions:10 -TopFilesPerExtension:3
```

### 示例 31

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopExtensions:10 -TopFilesPerExtension:3 -TopScansPerFilePerExtension:3
```

### 示例 32

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopExtensions:10 -TopProcessesPerExtension:3
```

### 示例 33

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopExtensions:10 -TopProcessesPerExtension:3 -TopScansPerProcessPerExtension:3
```

### 示例 34

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopProcesses:10
```

### 示例 35

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopProcesses:10 -TopScansPerProcess:3
```

### 示例 36

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopProcesses:10 -TopExtensionsPerProcess:3
```

### 示例 37

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopProcesses:10 -TopExtensionsPerProcess:3 -TopScansPerExtensionPerProcess:3
```

### 示例 38

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopProcesses:10 -TopFilesPerProcess:3
```

### 示例 39

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopProcesses:10 -TopFilesPerProcess:3 -TopScansPerFilePerProcess:3
```

### 示例 40

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopProcesses:10 -TopPathsPerProcess:3
```

### 示例 41

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopProcesses:10 -TopPathsPerProcess:3 -TopPathsDepth:3
```

### 示例 42

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopProcesses:10 -TopPathsPerProcess:3 -TopPathsDepth:3 -TopScansPerPathPerProcess:3
```

### 示例 43

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopProcesses:10 -TopPathsPerProcess:3 -TopScansPerPathPerProcess:3
```

### 示例 44

找出持续时间最长（从开始到结束都在指定的 `MinStartTime` 和 `MaxEndTime` 范围内）的前 10 次扫描记录。

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopScans:10 -MinStartTime:"5/14/2022 7:01:11 AM" -MaxEndTime:"5/14/2022 7:01:41 AM"
```

### 示例 45

找出在 `MinEndTime` 和 `MaxStartTime` 之间持续时间最长的前 10 次扫描记录（这些扫描记录可能部分重叠在这个时间段内）。

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopScans:10 -MinEndTime:"5/14/2022 7:01:11 AM" -MaxStartTime:"5/14/2022 7:01:41 AM"
```

### 示例 46

找到在 `MinStartTime` 和 `MaxStartTime` 之间持续时间最长的前 10 次扫描记录（这些扫描记录可能部分重叠于该时间范围内）。

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopScans:10 -MinStartTime:"5/14/2022 7:01:11 AM" -MaxStartTime:"5/14/2022 7:01:41 AM"
```

### 示例 47

找到在 `MinStartTime` 或更晚时间开始的、持续时间最长的前 10 次扫描记录：

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopScans:10 -MinStartTime:"5/14/2022 7:01:11 AM"
```

### 示例 48

找出在 MaxStartTime 之前或等于 MaxStartTime 开始、且扫描时长最长的前 10 个扫描记录。

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopScans:10 -MaxStartTime:"5/14/2022 7:01:11 AM"
```

### 示例 49

找出持续时间最长、且结束时间不早于 `MinEndTime` 的前 10 次扫描记录：

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopScans:10 -MinEndTime:"5/14/2022 7:01:11 AM"
```

### 示例 50

找出扫描时长最长、且在 MaxEndTime 之前或恰好在 MaxEndTime 时结束的前 10 次扫描记录：

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopScans:10 -MaxEndTime:"5/14/2022 7:01:11 AM"
```

### 示例 51

找出在当前时间间隔内影响最大的、扫描时长最长的前10个扫描任务，这些任务的开始或结束时间都不在 `MaxStartTime` 和 `MinEndTime` 的范围内。

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopScans:10 -MaxStartTime:"5/14/2022 7:01:11 AM" -MinEndTime:"5/14/2022 7:01:41 AM"
```

### 示例 52

找出在当前时间区间内影响最大的、扫描时长最长的前10个扫描任务。这些任务的开始时间应在 `MinStartTime` 和 `MaxStartTime` 之间，结束时间应晚于 `MinEndTime`。

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopScans:10 -MinStartTime:"5/14/2022 7:00:00 AM" -MaxStartTime:"5/14/2022 7:01:11 AM" -MinEndTime:"5/14/2022 7:01:41 AM"
```

### 示例 53

找出在前一个最大开始时间（MaxStartTime）之前开始，在最小结束时间（MinEndTime）和最大结束时间（MaxEndTime）之间结束的、对当前时间段影响最大的扫描任务，这些扫描任务的持续时间最长，并将它们排列在前三十名中。

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopScans:10 -MaxStartTime:"5/14/2022 7:01:11 AM" -MinEndTime:"5/14/2022 7:01:41 AM" -MaxEndTime:"5/14/2022 7:02:00 AM"
```

### 示例 54

找出在当前时间区间内影响最大的、扫描时长最长的前10个扫描记录。这些扫描记录的开始时间应在 MinStartTime 和 MaxStartTime 之间，结束时间应在 MinEndTime 和 MaxEndTime 之间。

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopScans:10 -MinStartTime:"5/14/2022 7:00:00 AM" -MaxStartTime:"5/14/2022 7:01:11 AM" -MinEndTime:"5/14/2022 7:01:41 AM" -MaxEndTime:"5/14/2022 7:02:00 AM"
```

### 示例 55

找到持续时间最长的前10个扫描记录，这些扫描记录的开始时间和结束时间都必须在 `MinStartTime` 和 `MaxEndTime` 之间。请使用 `DateTime` 类型，并以 `FILETIME` 格式表示时间（即原始数字形式）。例如，来自“-Raw”报告格式的数据：

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopScans:10 -MinStartTime:([DateTime]::FromFileTime(132969744714304340)) -MaxEndTime:([DateTime]::FromFileTime(132969745000971033))
```

### 示例 56

使用 DateTime（以 FILETIME 格式表示的原始数字）找出在 MinEndTime 和 MaxStartTime 之间持续时间最长的前 10 次扫描记录，这些扫描记录可能部分覆盖了该时间范围。例如，数据来源于 -Raw 报告格式：

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl -TopScans:10 -MinEndTime:([DateTime]::FromFileTime(132969744714304340)) -MaxStartTime:([DateTime]::FromFileTime(132969745000971033))
```

### 示例 57

除了通过其他参数定期显示的信息外，还展示在跟踪中捕获的扫描结果的摘要或概览。输出结果会受到时间间隔参数 `MinStartTime` 和 `MaxEndTime` 的影响。

```powershell
Get-MpPerformanceReport -Path:.\Defender-scans.etl [other arguments] -Overview
```

## 参数

### -MaxEndTime

指定报告中包含的扫描任务的最大结束时间。仅接受有效的 DateTime 类型值。

```yaml
Type: System.DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: [DateTime]::MaxValue
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaxStartTime

指定报告中包含的扫描任务的最大开始时间。必须输入有效的 DateTime 值。

```yaml
Type: System.DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: [DateTime]::MaxValue
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinDuration

指定报告中包含的文件、扩展名和进程的所有扫描操作的最短持续时间或总扫描时间。接受的值格式有 ‘0.1234567sec’、‘0.1234ms’、‘0.1us’ 或有效的 TimeSpan 类型。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0us
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinEndTime

指定报告中包含的扫描任务的最晚结束时间。必须输入一个有效的 DateTime 对象。

```yaml
Type: System.DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: [DateTime]::MinValue
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinStartTime

指定报告中包含的扫描任务的最小开始时间。必须输入有效的 DateTime 值。

```yaml
Type: System.DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: [DateTime]::MinValue
Accept pipeline input: False
Accept wildcard characters: False
```

### -Overview

在常规输出中添加对轨迹中所捕获的扫描结果的概述或总结。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path

指定用于分析的Microsoft Defender防病毒软件性能记录文件的位置。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Raw

指定输出内容应具有机器可读性，并且可以轻松转换为 JSON 等序列化格式。

- Collections and elements are not be formatted.
- TimeSpan values are represented as number of 100-nanosecond intervals.
- DateTime values are represented as number of 100-nanosecond intervals since January 1, 1601 (UTC).

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopExtensions

请求一份顶级扩展程序的报告，并指定要输出多少个顶级扩展程序，这些扩展程序需按照“持续时间”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopExtensionsPerPath

指定每个顶级路径应输出多少个最受欢迎的扩展名（按“使用时长”排序）。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopExtensionsPerProcess

指定为每个顶级进程输出多少个最常用的扩展程序（top extensions），并按照“持续时间”（Duration）进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopFiles

请求生成一个顶级文件报告，并指定要输出多少个顶级文件，这些文件需按照“时长”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopFilesPerExtension

指定每个顶级扩展名应输出多少个排名靠前的文件，并按照“时长”（Duration）进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopFilesPerPath

指定每个顶级路径应输出多少个排名靠前的文件，并按“持续时间”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopFilesPerProcess

指定每个顶级进程要输出多少个最“重要”的文件（即表现最好的文件），这些文件将按照“耗时”（Duration）进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopPaths

请求生成一个“顶级路径报告”，并指定需要输出多少条顶级路径记录，这些记录需按照“时长”进行排序。这一过程会递归地应用于每个目录项。扫描结果会按文件夹层次结构进行分组，并同样按照“时长”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopPathsDepth

当使用 $TopPaths 时，该参数指定了用于对扫描结果进行分组的最大深度（按路径计算）。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopPathsPerExtension

指定为每个顶级扩展名输出多少条顶级路径，并按照“时长”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopPathsPerProcess

指定为每个顶级进程输出多少条顶级路径，并按照“持续时间”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopProcesses

请求生成一个顶级进程报告，并指定要输出多少个顶级进程，这些进程需按照“持续时间”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopProcessesPerExtension

指定每个顶级扩展程序应输出多少个排名靠前的进程，并按“持续时间”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopProcessesPerFile

指定每个“顶级文件”要输出多少个最耗时的进程，并按照“耗时时间”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopProcessesPerPath

指定每个顶级路径应输出多少个顶级进程，并按照“持续时间”（Duration）进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopScans

请求一份“顶级扫描报告”，并指定需要输出多少份按“时长”排序的顶级扫描结果。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopScansPerExtension

指定每个顶级扩展程序应输出多少条扫描结果，并按“持续时间”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopScansPerExtensionPerPath

指定为每个顶级路径中的每个顶级扩展名输出多少条扫描结果，这些结果按照“持续时间”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopScansPerExtensionPerProcess

指定为每个顶级进程的每个顶级扩展程序输出多少条扫描结果，这些结果按“持续时间”（Duration）进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopScansPerFile

指定每个“热门文件”应输出多少条扫描结果，并按照“时长”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopScansPerFilePerExtension

指定为每个顶级文件（具有该顶级扩展名）输出多少条扫描结果，这些结果按“持续时间”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopScansPerFilePerPath

指定每个顶级路径下的每个顶级文件应输出多少条扫描结果，这些结果按照“时长”（Duration）进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopScansPerFilePerProcess

指定为每个顶级进程的每个顶级文件输出多少条扫描结果，这些结果按照“时长”（Duration）进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopScansPerPath

指定每个主要路径应输出多少条最高优先级的扫描结果，并按“时长”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopScansPerPathPerExtension

指定每个顶级扩展名的每个顶级路径应输出多少个扫描结果，并按“持续时间”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopScansPerPathPerProcess

指定为每个顶级进程的每条顶级路径输出多少条扫描结果，这些结果按照“持续时间”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopScansPerProcess

指定在“顶级进程”报告中为每个顶级进程输出多少条扫描结果，这些结果将按照“持续时间”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopScansPerProcessPerExtension

指定为每个顶级扩展程序中的每个顶级进程输出多少条扫描结果，并按照“时长”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopScansPerProcessPerFile

指定为每个顶级进程和每个顶级文件输出多少条扫描结果，这些结果按照“耗时”（Duration）进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -TopScansPerProcessPerPath

指定为每个顶级路径中的每个顶级进程输出多少个扫描结果，这些结果按照“持续时间”进行排序。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接
