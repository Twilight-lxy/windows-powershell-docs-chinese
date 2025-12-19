---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FSRMClassification.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/set-fsrmclassification?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-FsrmClassification
---

# Set-FsrmClassification

## 摘要
更改分类相关的配置设置。

## 语法

```
Set-FsrmClassification [-InputObject <CimInstance[]>] [-ExcludeNamespace <String[]>] [-Schedule <CimInstance>]
 [-Continuous] [-ContinuousLog] [-ContinuousLogSize <UInt64>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-FsrmClassification` cmdlet 用于更改分类相关的配置设置。

## 示例

### 示例 1：设置分类任务以连续运行
```
PS C:\> Set-FsrmClassification -Continuous -ContinuousLog
```

此命令将分类任务设置为持续运行，并启用连续分类日志的功能。如果您之前没有创建过分类计划（即分类任务的调度配置），则该命令会引发错误。

### 示例 2：为分类任务设置时间安排
```
The first command gets a **DateTime** object and stores it in the variable $D.
PS C:\> $D = Get-Date "12:00am"

The second command creates a **FsrmScheduledTask** object that defines a schedule for the task of once a month on the first day of the month at midnight. The command stores the **FsrmScheduledTask** object in the $Task variable.
PS C:\> $Task = New-FsrmScheduledTask -Time $D.ToFileTimeUtc() -Monthly 1

The third command sets the schedule for classification to the schedule stored in the $Task variable.
PS C:\> Set-FsrmClassification -Schedule $Task
```

这个例子将分类任务的调度设置为每月的第一个日期（即月初）的午夜时分运行一次。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Continuous
表示服务器在后台持续对文件进行分类处理。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ContinuousLog
这表示服务器会记录连续的分类活动。要记录分类活动，必须指定“Continuous”参数。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ContinuousLogSize
指定包含连续分类活动的日志的最大大小。要记录分类活动，必须设置“Continuous”参数。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExcludeNamespace
指定一个字符串数组，其中包含不应包含在分类中的文件夹列表（无论是计划性分类还是连续性分类）。

你可以在路径的开头为每个文件夹添加 `[AllVolumes]`，以表示该命名空间在所有卷上都被排除。你还可以在每个命名空间后面加上 `/s` 这个字符串，以便排除该命名空间下的所有文件夹和文件。如果未在命名空间后添加 `/s`，则只会排除指定文件夹中的文件。如果某个字符串是 `[Default]`，服务器会将该默认值添加到需要排除的命名空间列表中。无论如何，启动卷总是会被排除在外。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定要传递给此cmdlet的输入数据。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Schedule
用于指定一个文件服务器资源管理器（FSRM）的计划任务对象，该对象描述了执行持续分类操作的日程安排。可以使用 **New-FsrmScheduledTask** cmdlet 来创建计划任务对象。

```yaml
Type: CimInstance
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行该 cmdlet 的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#Root/Microsoft/Windows/FSRM/MSFT_FSRMClassification

## 备注

## 相关链接

[Get-FsrmClassification](./Get-FsrmClassification.md)

[New-FsrmScheduledTask](./New-FsrmScheduledTask.md)

[Start-FsrmClassification](./Start-FsrmClassification.md)

[Stop-FsrmClassification](./Stop-FsrmClassification.md)

[Wait-FsrmClassification](./Wait-FsrmClassification.md)

