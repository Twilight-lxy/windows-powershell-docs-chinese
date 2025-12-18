---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DedupSchedule.cdxml-help.xml
Module Name: Deduplication
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/deduplication/new-dedupschedule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-DedupSchedule
---

# 新的去重计划

## 摘要
创建一个数据去重计划。

## 语法

```
New-DedupSchedule [-Name] <String> [-Type] <Type> [-DurationHours <UInt32>] [-Disable]
 [-StopWhenSystemBusy] [-Memory <UInt32>] [-Cores <UInt32>] [-Priority <Priority>]
 [-InputOutputThrottle <UInt32>] [-InputOutputThrottleLevel <InputOutputThrottleLevel>]
 [-Start <DateTime>] [-Days <DayOfWeek[]>] [-Full] [-ReadOnly]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

`New-DedupSchedule` cmdlet 用于创建数据去重计划。该 cmdlet 返回一个 **DeduplicationSchedule** 对象，您可以使用这个对象来自定义数据去重计划。对于未指定的参数，该 cmdlet 会使用默认设置来创建数据去重计划。

您可以创建一个计划来运行以下类型的数据去重任务：

- `Optimization` This job performs both deduplication and compression of files according data
  deduplication policy for the volume. After initial optimization of a file, if that file is then
  modified and again meets the data deduplication policy threshold for optimization, the file is
  optimized again.
- `GarbageCollection` This job processes deleted or modified data on the volume so that any data
  chunks that are no longer referenced are cleaned up. Garbage collection jobs process previously
  deleted or logically overwritten optimized content to create usable volume free space. When an
  optimized file is deleted or overwritten by new data, the old data in the chunk store is not
  immediately deleted. Garbage collection is scheduled to run weekly by default. Garbage collection
  is a processing-intensive operation, so you should allow the deletion load to reach a threshold
  and then manually run this job type, or schedule it for off hours.
- `Scrubbing` This job processes data corruptions it finds during data integrity validation,
  performs possible corruption repair, and generates a scrubbing report.
- `Unoptimization` This job undoes data deduplication on all of the optimized files on the volume.
  At the end of a successful unoptimization job, the server deletes all of the data deduplication
  metadata from the volume.

有关更多信息，请参阅 TechNet 上的 [安装和配置数据去重](https://technet.microsoft.com/library/hh831434.aspx)。

## 示例

### 示例 1：为垃圾回收作业创建数据去重计划

```powershell
$params = @{
    Days          = 'Sunday'
    DurationHours = 5
    Name          = 'OffHoursGC'
    Priority      = 'Normal'
    Start         = '08:00'
    Type          = 'GarbageCollection'
}
New-DedupSchedule @params
```

该命令创建了一个数据去重计划，其名称为 `OffHoursGC`。去重任务的类型为 `GarbageCollection`。根据 `Days` 参数的设置，该任务计划每周日运行。任务将在上午 8:00 开始，并以常规优先级（Normal Priority）执行。命令指定了任务的持续时间为 5 小时（`DurationHours = 5`），因此如果任务在 5 小时后仍未完成，服务器会自动取消该任务。

### 示例 2：为数据清洗任务创建数据去重计划

```powershell
$params = @{
    Days               = @(
        'Monday'
        'Tuesday'
        'Wednesday'
        'Thursday'
        'Friday'
    )
    DurationHours      = 6
    Name               = 'OffHoursScrub'
    Priority           = 'Normal'
    Start              = '23:00'
    StopWhenSystemBusy = $true
    Type               = 'Scrubbing'
}
New-DedupSchedule @params
```

此命令为名为 `OffHoursScrub` 的 “清洗” 类型作业创建了一个数据去重计划。该命令会在每周一至周五的晚上 11:00（23:00）启动清洗作业。`StopWhenSystemBusy` 参数表示：当系统繁忙时，服务器会暂停作业，并稍后重新尝试执行。`DurationHours` 参数规定：如果作业在 6 小时后仍未完成，服务器将取消该作业。该作业将以 “正常”（Normal）优先级运行。

### 示例 3：为优化任务创建数据去重计划

```powershell
$params = @{
    Days          = @(
        'Mon'
        'Tues'
        'Wed'
        'Thurs'
        'Fri'
    )
    DurationHours = 9
    Name          = 'MyWeekdayOptimization'
    Start         = '08:00'
    Type          = 'Optimization'
}
New-DedupSchedule @params
```

此命令为名为“MyWeekdayOptimization”的`优化`类型作业创建了一个数据去重计划。该优化作业以正常的优先级（Priority）在每个工作日的晚上8点运行。`DurationHours`参数指定：如果作业进程在9小时后仍未完成，服务器将取消该作业。

## 参数

### -AsJob

将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: Microsoft.Management.Infrastructure.CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Cores

指定一个数组，该数组包含了作业可以使用的物理核心的最大百分比值。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: MaximumCoresPercentage

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Days

指定一周中服务器执行数据去重任务的日期数组。该参数的可接受值为：

- `Monday`
- `Tuesday`
- `Wednesday`
- `Thursday`
- `Friday`
- `Saturday`
- `Sunday`

```yaml
Type: System.DayOfWeek[]
Parameter Sets: (All)
Aliases:
Accepted values: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Disable

这表示在您创建数据去重计划后，服务器会立即禁用该计划。在您通过 **Start** 参数指定的时间点，服务器不会执行该数据去重计划。一旦您禁用了某个数据去重计划，可以使用 **Set-DedupSchedule** cmdlet 来重新启用该计划。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DurationHours

指定服务器在取消任务之前运行该任务的小时数。值 `0` 表示服务器会将任务运行到完成为止。此 cmdlet 可以安全地停止数据去重任务，并且在取消任务时不会影响服务器正在处理的文件。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Full

这表示：如果您为**Type**参数指定值`GarbageCollection`，垃圾回收任务将释放卷上所有被删除或未被引用的数据。如果您不指定此参数，垃圾回收任务将在系统设定的数据删除阈值被超过后自动执行以释放空间。我们建议您定期运行垃圾回收操作（无需指定该参数），然后每月指定一次该参数并再次运行垃圾回收操作。

如果您为 **Type** 参数指定值 `Scrubbing`，则表示该擦除作业会验证卷上所有数据的完整性。如果不指定此参数，擦除作业仅会验证关键元数据以及数据去重过程中之前遇到的数据完整性问题。我们建议您定期运行擦除操作（无需指定此参数），然后每月再次指定该参数并重新执行擦除操作。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InputOutputThrottle

该参数用于指定应用于去重作业的输入/输出流量限制程度。通过实施流量限制，可以确保去重操作不会干扰其他对I/O操作要求较高的进程。该参数的可接受取值为0到100之间的整数。如果您同时指定了该参数和**InputOutputThrottleLevel**参数，则**InputOutputThrottle**的设置将具有优先级。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputOutputThrottleLevel

指定作业提供的I/O限制程度，以确保该作业不会干扰其他对I/O要求较高的进程。此参数的可接受值为：

- `None`
- `Low`
- `Medium`
- `High`

```yaml
Type: InputOutputThrottleLevel
Parameter Sets: (All)
Aliases:
Accepted values: None, Low, Medium, High, Maximum

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Memory

Specifies the maximum percentage of physical computer memory that the data deduplication job can
use.

For optimization jobs, we recommend that you set a range from `15` to `50`, and a higher memory
consumption for jobs that you schedule to run when you specify the **StopWhenSystemBusy** parameter.
For garbage collection and scrubbing jobs, which you typically schedule to run in off hours, you can
set a higher memory consumption, such as `50`.

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: MaximumMemoryPercentage

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name

Specifies a name for the data deduplication job schedule.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Priority

Sets the CPU and I/O priority for the optimization job that you run by using this cmdlet. For jobs
that you run when you specify the **StopWhenSystemBusy** parameter, we recommend that you set this
parameter to `Low`. For typical optimization jobs, we recommend that you set this parameter to
`Normal`.

```yaml
Type: Priority
Parameter Sets: (All)
Aliases:
Accepted values: Low, Normal, High

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReadOnly

表示该清洗任务会处理并报告发现的损坏情况，但不会执行任何修复操作。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Start

指定开始此任务的时间。默认值为凌晨1点45分。请按照系统区域设置的格式输入日期，例如 `dd-MM-dd`（德语\[德国\]）或 `MM/dd/yyyy`（英语\[美国\]）。

```yaml
Type: System.DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StopWhenSystemBusy

表示当系统繁忙时，服务器会停止该作业，并稍后重新尝试执行。我们建议在为该作业设置较低优先级时指定此参数。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit

指定可以同时建立的、用于运行该 cmdlet 的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -Type

用于指定数据去重作业的类型。该参数的可接受值包括：

- `Optimization`
- `GarbageCollection`
- `Scrubbing`
- `Unoptimization`

```yaml
Type: Type
Parameter Sets: (All)
Aliases:
Accepted values: Optimization, GarbageCollection, Scrubbing, Unoptimization

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.DateTime

### System-DayOfWeek[]

### System.ManagementAutomation.SwitchParameter

### System.UInt32

### Microsoft.PowerShell Cmdletization GeneratedTypes.DedupSchedule.Priority

### Microsoft.PowerShell CmdletizationGeneratedTypes.DedupSchedule.Type

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径指定了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DedupSchedule](./Get-DedupSchedule.md)

[Remove-DedupSchedule](./Remove-DedupSchedule.md)

[Set-DedupSchedule](./Set-DedupSchedule.md)
