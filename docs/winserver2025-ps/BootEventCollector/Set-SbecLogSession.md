---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/set-sbeclogsession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-SbecLogSession
---

# Set-SbecLogSession

## 摘要
更新日志会话的设置。

## 语法

### 对象
```
Set-SbecLogSession -Session <TraceSessionInfo[]> [-Path <Object>] [-ClockType <Object>] [-BufferSize <Object>]
 [-MinimumBufferCount <UInt32>] [-MaximumBufferCount <UInt32>] [-MaximumFileSize <Object>]
 [-FlushSeconds <UInt32>] [-LogFileMode <Object>] [-KernelEnableFlags <Object>] [-EnableKd] [-DisableKd]
 [-SimulateError <Int32>] [<CommonParameters>]
```

### 名称
```
Set-SbecLogSession -Name <String[]> [-Path <Object>] [-ClockType <Object>] [-BufferSize <Object>]
 [-MinimumBufferCount <UInt32>] [-MaximumBufferCount <UInt32>] [-MaximumFileSize <Object>]
 [-FlushSeconds <UInt32>] [-LogFileMode <Object>] [-KernelEnableFlags <Object>] [-EnableKd] [-DisableKd]
 [-SimulateError <Int32>] [<CommonParameters>]
```

## 描述
`Set-SbecLogSession` cmdlet 用于更新日志会话的设置。

你可以在将对象作为参数传递给此cmdlet之前，先修改对象的属性。在这种情况下，请确保直接在对象本身中设置属性，而不是通过其`Trace`字段来设置（PowerShell会忽略对`Trace`字段的任何修改）。

未使用的或被设置为 `$Null` 的 cmdlet 参数将保持不变。

您无法更新会话名称。

操作系统可能会拒绝更改某些参数，或者默默地忽略这些更新。

## 示例


## 参数

### -BufferSize
指定会话的缓冲区大小（以千字节为单位）。这是一个缓冲区的大小，而缓冲区的数量由 *MinimumBufferCount* 和 *MaximumBufferCount* 参数来控制。

```yaml
Type: Object
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ClockType
指定用于本次会话收集的事件的时间戳类型。该参数的可接受值包括：

- QueryPerformanceCounter.
The high-resolution (period of 100 nanoseconds) clock that is typically used for performance measurement.
- SystemTime.
The lower-resolution system time similar to FILETIME (period of 10 milliseconds).
This value is most typical for the data collection through SBEC.
- CpuCycleCounter.
The highest-resolution, with the frequency of the CPU, but may be unreliable depending on the CPU model and the thermal and power modes.

```yaml
Type: Object
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableKd
将 `LogFileMode` 标志设置为禁用通过内核传输将实时日志会话的数据转发给收集器。`EnableKd` 和 `DisableKd` 这两个选项是互斥的（即只能选择一个处于启用状态）。

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

### -EnableKd
这些更改用于调整 `LogFileMode` 标志，以启用通过内核传输将实时日志会话数据转发到收集器的功能。`EnableKd` 和 `DisableKd` 这两个开关是互斥的（即只能选择其中一个进行启用）。

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

### -FlushSeconds
指定会话缓冲区自动清空的超时时间（以秒为单位）。您可以通过将此参数设置为 0 来禁用超时时的缓冲区清除功能；在这种情况下，缓冲区只有在满载时或通过显式命令清除时才会被写入。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: FlushTimer

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -KernelEnableFlags
用于指定 NT 内核日志记录器的标志，以启用内核事件记录功能。在系统设置和启动监控过程中，唯一合理的标志是 “Process”（进程相关）。该枚举类型定义在文件 $PsHome\Modules\BootEventCollector\SbecTraceHelpers.psm1 中。此参数的可接受取值为：

- Process
- Thread
- ImageLoad
- ProcessCounters
- ContextSwitch
- Dpc
- Interrupt
- SystemCall
- DiskIO
- DiskFileIO
- DiskIOInit
- Dispatcher
- MemoryPageFaults
- MemoryHardFaults
- VirtualAlloc
- NetworkTCPIP
- Registry
- Alpc
- SplitIO
- Driver
- FileIO
- FileIOInit
- Profile

```yaml
Type: Object
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogFileMode
Specifies the new flags for the log file mode.
The parameters *EnableKd* and *DisableKd* are applied on top of these flags.
This enumeration type is defined in $PsHome\Modules\BootEventCollector\SbecTraceHelpers.psm1.
The most used bit values in it are:

- FileSequential.
Write events to a log file sequentially; stops when the file reaches its maximum size.
- FileCircular.
Write events to a log file.
After the file reaches the maximum size, replace the oldest events with incoming events.
- FileAppend.
Append events to an existing sequential log file.
- FileNewFile.
Automatically switch to a new log file when the file reaches the maximum size.
- FilePreallocate.
Reserve the MaximumFileSize of disk space for the log files in advance.
- Secure.
Restrict who can log events to the session to those with TRACELOG_LOG_EVENT permission.
- RealTime.
Deliver the events to consumers in real-time instead of writing them to a file.
This mode is required for sending the events to the event collector.
- KdFilter.
Forward the events though the kernel channel to the event collector or to the debugger.
- UsePagedMemory.
Use the paged memory for the buffers.
- NoPerProcessorBuffering.
Write the events from all processors to the same buffer.
This preserves the order of the events, and is recommended for sending the events to the event collector.

```yaml
Type: Object
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumBufferCount
Specifies the maximum number of buffers to allocate for this session.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: MaximumBuffers, maxbuf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumFileSize
Specifies the maximum file size after which the session may switch to the next file, in megabytes.
Use 0 for no limit.

```yaml
Type: Object
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinimumBufferCount
Specifies the minimum number of buffers to allocate for this session.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: MinimumBuffers, minbuf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
Specifies the name of the session to create.

```yaml
Type: String[]
Parameter Sets: Name
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
Specifies the ETL file where the session will write its log.
The session must have the file mode enabled to write to a file; a session in the real-time mode ignores the file.

```yaml
Type: Object
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Session
指定会话的 GUID（全局唯一标识符）。

```yaml
Type: TraceSessionInfo[]
Parameter Sets: Object
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -SimulateError
模拟在会话创建过程中出现的Windows错误，导致该函数抛出异常。您可以指定此参数来测试错误处理机制。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### SbecEtwTrace.TraceSessionInfo
该类定义在文件 `$PsHomeModules\BootEventCollector\SbecTrace Helpers.psm1` 中。

## 输出

### 没有（需要处理的内容）。

## 备注

## 相关链接

[Get-SbecLogSession](./Get-SbecLogSession.md)

[Save-SbecLogSession](./Save-SbecLogSession.md)

[Start-SbecLogSession](./Start-SbecLogSession.md)

[开始 SbecNtKernelLogSession 会话](./Start-SbecNtKernelLogSession.md)

[开始 SbecSimpleLogSession 会话](./Start-SbecSimpleLogSession.md)

[Stop-SbecLogSession](./Stop-SbecLogSession.md)

