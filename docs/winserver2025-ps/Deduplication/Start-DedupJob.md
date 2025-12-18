---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DedupJob.cdxml-help.xml
Module Name: Deduplication
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/deduplication/start-dedupjob?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-DedupJob
---

# 启动去重作业

## 摘要
启动一个数据去重作业。

## 语法

```
Start-DedupJob [-Type] <Type> [[-Volume] <String[]>] [-StopWhenSystemBusy]
 [-Memory <UInt32>] [-Cores <UInt32>] [-Priority <Priority>]
 [-InputOutputThrottle <UInt32>] [-InputOutputThrottleLevel <InputOutputThrottleLevel>]
 [-Preempt] [-Wait] [-Full] [-ReadOnly] [-Timestamp <DateTime>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

`Start-DedupJob` 命令用于为一个或多个卷启动新的数据去重任务。如果服务器正在同一卷上执行其他任务，或者计算机的资源不足以运行该任务，则数据去重任务可能会被放入队列中等待执行。使用此命令启动的任务会被服务器标记为“手动任务”，并且这类任务会优先于计划好的任务得到处理。对于每个通过该命令启动的任务，服务器都会返回一个 `DeduplicationJob` 对象。

对于多卷数据去重任务，您可以使用 **Preempt** 参数将任务移到任务队列的顶端，并取消当前正在运行的任务。

## 示例

### 示例 1：启动一个优化任务

```powershell
Start-DedupJob -Volume "D:" -Type Optimization -Memory 50
```

此命令会在驱动器 `D:` 上启动一个去重优化任务，并最多占用 50% 的内存（RAM）。

## 参数

### -AsJob

将此cmdlet作为后台作业运行。使用该参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个代表该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者提供一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

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

指定作业最多可以使用物理核心的比例（以百分比表示）。

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

### -Full

这表示：如果您为**Type**参数指定了`GarbageCollection`值，垃圾收集作业将会释放卷上所有被删除或未被引用的数据。如果您没有指定该参数，垃圾收集作业则会在系统删除数据的阈值被超过后自动释放空间。我们建议您定期运行垃圾收集（无需指定该参数），然后每月指定一次该参数并再次运行垃圾收集。

如果您为**Type**参数指定值`Scrubbing`，则表示该擦除作业会验证卷上所有数据的完整性。如果您不指定此参数，则擦除作业仅会验证关键元数据以及数据去重过程中之前发现的数据完整性问题。我们建议您定期运行擦除操作（此时无需指定该参数），然后每月再指定一次该参数并重新执行擦除操作。

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

### -InputOutputThrottle

指定应用于去重作业的输入/输出限流程度。限流可以确保去重操作不会干扰其他对I/O要求较高的进程。该参数的可接受值为：`0` 到 `100` 之间的整数。如果您同时指定了此参数和 **InputOutputThrottleLevel** 参数，那么 **InputOutputThrottle** 的设置将具有优先级。

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

### -InputOutputThrottleLevel

指定作业提供的I/O限制程度，以确保该作业不会干扰其他对I/O要求较高的进程。此参数的可接受值为：

- `None`
- `Low`
- `Medium`
- `High`

If you specify this parameter and the **InputOutputThrottle** parameter, **InputOutputThrottle**
takes precedence.

```yaml
Type: InputOutputThrottleLevel
Parameter Sets: (All)
Aliases:
Accepted values: None, Low, Medium, High, Maximum

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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

### -Preempt

Indicates that the deduplication engine moves the job to the top of the job queue and cancels the
current job. After the server cancels the current job, the deduplication engine cannot run the
preempting job if the server does not have enough memory to run the job.

This parameter applies to manual data deduplication jobs only and is ignored for scheduled jobs. You
can preempt only deduplication jobs on multiple volumes.

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

Sets the CPU and I/O priority for the optimization job run that you run by using this cmdlet. For
jobs that you run when you specify the **StopWhenSystemBusy** parameter, we recommend that you set
this parameter to `Low`. For typical optimization jobs, we recommend that you set this parameter to
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

Indicates that the scrubbing job process and report on corruptions that it finds but does not run
any repair actions.

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

### -StopWhenSystemBusy

Indicates that the server stops the job when the system is busy and retries later. We recommend that
you specify this parameter when you set a low priority for the job.

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

Specifies the maximum number of concurrent operations that can be established to run the cmdlet. If
this parameter is omitted or a value of `0` is entered, then Windows PowerShell® calculates an
optimum throttle limit for the cmdlet based on the number of CIM cmdlets that are running on the
computer. The throttle limit applies only to the current cmdlet, not to the session or to the
computer.

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Timestamp

Specifies a date and time. This parameter applies only to unoptimization jobs. The deduplication
engine unoptimizes only files that it optimized or reoptimized since the **System.DateTime** value
that you specify.

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

### -Type

Specifies the type of data deduplication job. The acceptable values for this parameter are:

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
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Volume

Specifies an array of system volumes for which you want to manually queue data deduplication jobs.
Enter one or more volume IDs, drive letters, or volume GUID paths. For drive letters, use the format
`D:`. For volume GUID paths, use the format `\\?\Volume{{GUID}}\`. Separate multiple volumes with a
comma.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: Path, Name, DeviceId

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Wait

Indicates that the cmdlet waits for the job to complete and provides progress information to the
client.

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

### CommonParameters

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.Management.Automation.SwitchParameter

### System.String[]

### System.UInt32

### Microsoft.PowerShell CmdletizationGeneratedTypes.DedupJob.Priority

### Microsoft.PowerShell Cmdletization.GenerateTypes.DedupJob.Type

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名称。

## 备注

## 相关链接

[Get-DedupJob](./Get-DedupJob.md)

[Stop-DedupJob](./Stop-DedupJob.md)
