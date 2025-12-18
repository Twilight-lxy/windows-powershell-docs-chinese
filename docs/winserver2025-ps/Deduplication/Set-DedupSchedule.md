---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DedupSchedule.cdxml-help.xml
Module Name: Deduplication
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/deduplication/set-dedupschedule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DedupSchedule
---

# Set-DedupSchedule

## 摘要
更改数据去重计划的配置设置。

## 语法

### 查询（cdxml）（默认设置）

```
Set-DedupSchedule [-Name] <String[]> [-Type <Type[]>] [-DurationHours <UInt32>]
 [-Enabled <Boolean>] [-StopWhenSystemBusy <Boolean>] [-Memory <UInt32>] [-Cores <UInt32>]
 [-Priority <Priority>] [-InputOutputThrottle <UInt32>]
 [-InputOutputThrottleLevel <InputOutputThrottleLevel>] [-Start <DateTime>]
 [-Days <DayOfWeek[]>] [-Full <Boolean>] [-ReadOnly <Boolean>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru]
 [<CommonParameters>]
```

### InputObject (cdxml)

```
Set-DedupSchedule -InputObject <CimInstance[]> [-DurationHours <UInt32>]
 [-Enabled <Boolean>] [-StopWhenSystemBusy <Boolean>] [-Memory <UInt32>] [-Cores <UInt32>]
 [-Priority <Priority>] [-InputOutputThrottle <UInt32>]
 [-InputOutputThrottleLevel <InputOutputThrottleLevel>] [-Start <DateTime>]
 [-Days <DayOfWeek[]>] [-Full <Boolean>] [-ReadOnly <Boolean>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru]
 [<CommonParameters>]
```

## 描述

`Set-DedupSchedule` cmdlet 用于更改一个或多个数据去重计划的配置设置。

## 示例

### 示例 1：更改数据去重计划的设置，以用于垃圾收集任务

```powershell
$params = @{
    Days          = 'Sunday'
    DurationHours = 5
    Name          = 'OffHoursGC'
    Priority      = 'Normal'
    Start         = '08:00'
    Type          = 'GarbageCollection'
}
Set-DedupSchedule @params
```

该命令用于修改名为 `OffHoursGC` 的垃圾收集作业的数据去重调度设置。该作业被安排在每周日的 08:00 运行，优先级为 **Normal**（普通）。命令还指定：如果作业进程在 5 小时后仍未完成，服务器将自动取消该作业。

### 示例 2：更改用于数据清洗任务的数据去重计划的设置

```powershell
$params = @{
    Days = Monday,Tuesday,Wednesday,Thursday,Friday
    DurationHours = 6
    Name = "OffHoursScrub"
    Priority = Normal
    Start = 23:00
    StopWhenSystemBusy = $true
    Type = Scrubbing
}
Set-DedupSchedule @params
```

此命令用于更改名为 `OffHoursScrub` 的 “Scrubbing” 类型作业的数据去重调度设置。该命令会在每周一至周五的晚上 11 点（23:00）以正常优先级启动清洗作业。`StopWhenSystemBusy` 参数指定：当系统繁忙时，服务器会暂停作业并稍后重新尝试；`DurationHours` 参数则规定：如果作业在 6 小时后仍未完成，服务器将取消该作业。

### 示例 3：修改数据去重计划的设置以优化作业

```powershell
$params = @{
    Days          = @(
        'Monday'
        'Tuesday'
        'Wednesday'
        'Thursday'
        'Friday'
    )
    DurationHours = 9
    Name          = 'MyWeekendOptimization'
    Start         = '08:00'
    Type          = 'Optimization'
}
Set-DedupSchedule @params
```

此命令用于更改名为 `MyWeekdayOptimization` 的优化任务的数据去重计划设置。该优化任务每天工作日的晚上 8 点以 “正常”（Normal）优先级（Priority）运行。参数 **DurationHours** 指定：如果任务在 9 小时后仍未完成，服务器将取消该任务。

## 参数

### -AsJob

将此 cmdlet 作为后台作业运行。使用该参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在该作业完成之前，您可以继续在当前会话中操作。要管理该作业，请使用 `-*Job` 系列 cmdlets；要获取作业的结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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

指定作业可以使用的物理核心的最大百分比。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: MaximumCoresPercentage

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Days

指定服务器执行数据去重任务的每周工作日数组。此参数的允许值为：

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
Accept pipeline input: False
Accept wildcard characters: False
```

### -DurationHours

指定服务器在取消任务之前运行该任务的小时数。值 `0` 表示服务器会将该任务完整地执行完毕。此 cmdlet 可以安全地停止数据去重任务，在取消任务时不会影响服务器正在处理的文件。

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

### -Enabled

表示是否启用了数据去重计划。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Full

这表示：如果您为 **Type** 参数指定了值 `GarbageCollection`，垃圾回收操作将会清除卷上的所有已删除或未被引用的数据。如果您不指定该参数，垃圾回收操作则会在系统设定的数据删除阈值被超过后自动释放空间。我们建议您定期运行垃圾回收操作（无需指定该参数），之后每月再指定一次该参数并重新执行垃圾回收操作。

如果您为 **Type** 参数指定值 `Scrubbing`，则表示该擦除操作会验证卷上所有数据的完整性。如果不指定此参数，擦除操作仅会验证关键元数据以及数据去重过程中先前发现的数据完整性问题。我们建议您定期运行擦除操作（此时不指定该参数），然后每月指定一次该参数并重新执行擦除操作。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定该 cmdlet 的输入内容。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该 cmdlet。

```yaml
Type: Microsoft.Management.Infrastructure.CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -InputOutputThrottle

该参数用于指定应用于去重作业的输入/输出流量控制程度。通过实施流量控制，可以确保去重操作不会干扰其他对I/O操作要求较高的进程。此参数的可接受取值为0到100之间的整数。如果您同时指定了该参数和**InputOutputThrottleLevel**参数，则**InputOutputThrottle**的设置将具有优先权。

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

指定作业所提供的I/O限制程度，以确保该作业不会干扰其他对I/O需求较高的进程。此参数的可接受值为：

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
set higher memory consumption, such as `50`.

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: MaximumMemoryPercentage

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name

Specifies the name of a data deduplication job schedule.

```yaml
Type: System.String[]
Parameter Sets: Query (cdxml)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru

Returns an object representing the item with which you are working. By default, this cmdlet does not
generate any output.

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
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReadOnly

该选项表示清洗作业是否会处理和报告发现的损坏情况，但不会执行任何修复操作。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Start

指定开始执行此任务的时间。默认值为 `凌晨1点45分`。

请按照系统区域设置所使用的标准格式输入日期，例如 `dd-MM-yyyy`（德语\[德国\]）或 `MM/dd/yyyy`（英语\[美国\]）。

```yaml
Type: System.DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StopWhenSystemBusy

该参数用于指示当系统繁忙时服务器是否停止任务，并在稍后重新尝试执行该任务。我们建议在为任务设置较低优先级时指定此参数。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit

指定可以同时运行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该命令的最佳限制值。此限制仅适用于当前运行的命令，而不适用于会话或整个计算机。

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

指定数据去重作业类型的数组。该参数的可接受值为：

- `Optimization`
- `GarbageCollection`
- `Scrubbing`
- `Unoptimization`

```yaml
Type: Type[]
Parameter Sets: Query (cdxml)
Aliases:
Accepted values: Optimization, GarbageCollection, Scrubbing, Unoptimization

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft POWERShell Cmdletization GeneratedTypes.DedupSchedule.Type[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/Microsoft/Windows/Deduplication/MSFT_DedupJobSchedule

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DedupSchedule](./Get-DedupSchedule.md)

[New-DedupSchedule](./New-DedupSchedule.md)

[Remove-DedupSchedule](./Remove-DedupSchedule.md)
