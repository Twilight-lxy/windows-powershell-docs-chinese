---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/start-sbecsimplelogsession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-SbecSimpleLogSession
---

# 启动 SbecSimpleLogSession 会话

## 摘要
开始一个日志会话，并将事件转发给收集器（Collector）。

## 语法

```
Start-SbecSimpleLogSession [-Name] <String> [[-SessionGuid] <Guid>] [[-ProviderName] <String[]>]
 [[-ProviderGuid] <Guid[]>] [[-Level] <SeverityLevel>] [[-ClockType] <ClientContext>] [[-BufferSize] <UInt32>]
 [[-MinimumBufferCount] <UInt32>] [[-MaximumBufferCount] <UInt32>] [[-FlushSeconds] <UInt32>]
 [[-LogFileMode] <LoggingMode>] [[-KernelEnableFlags] <EventTraceFlag>] [-PassThru] [<CommonParameters>]
```

## 描述
`Start-SbecSimpleLogSession` cmdlet 使用一组更简单的参数，在启动事件模式下开始一个日志会话。

要使用更多参数启动日志会话，请使用 `Start-SbecLogSession` 命令。

## 示例


## 参数

### -BufferSize
指定会话的缓冲区大小（以千字节为单位）。这表示一个缓冲区的大小，而缓冲区的数量由 *MinimumBufferCount* 和 *MaximumBufferCount* 参数来控制。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 6
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ClockType
指定用于本次会话收集的事件的时间戳类型。该参数的可接受值为：

- Default.
- QueryPerformanceCounter.
  The high-resolution (period of 100 nanoseconds) clock that is typically used for performance measurement.
- SystemTime.
  The lower-resolution system time similar to FILETIME (period of 10 milliseconds).
  This value is most typical for the data collection through SBEC.
- CpuCycleCounter.
  The highest-resolution, with the frequency of the CPU, but may be unreliable depending on the CPU model and the thermal and power modes.

```yaml
Type: ClientContext
Parameter Sets: (All)
Aliases:
Accepted values: Default, QueryPerformanceCounter, SystemTime, CpuCycleCounter

Required: False
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FlushSeconds
指定会话缓冲区自动刷新的超时时间（以秒为单位）。您可以通过将此参数设置为 0 来禁用超时时的缓冲区刷新功能；此时，缓冲区仅会在满载或手动触发刷新时才会被写入。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: FlushTimer

Required: False
Position: 9
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -KernelEnableFlags
用于指定 NT 内核日志记录器的标志，这些标志可以启用内核事件记录功能。在设置和启动监控过程中，唯一合理的标志是 “Process”。这种枚举类型定义在文件 $PsHome\Modules\BootEventCollector\SbecTraceHelpers.psm1 中。该参数的可接受值包括：

- None
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
Type: EventTraceFlag
Parameter Sets: (All)
Aliases:
Accepted values: None, Process, Thread, ImageLoad, ProcessCounters, ContextSwitch, Dpc, Interrupt, SystemCall, DiskIO, DiskFileIO, DiskIOInit, Dispatcher, MemoryPageFaults, MemoryHardFaults, VirtualAlloc, NetworkTCPIP, Registry, Alpc, SplitIO, Driver, FileIO, FileIOInit, Profile

Required: False
Position: 11
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Level
Specifies the highest detail level value to enable for providers.
This enumeration type is defined in $PsHome\Modules\BootEventCollector\SbecTraceHelpers.psm1.
The acceptable values for this parameter are:

- Undefined
- Fatal
- Error
- Warning
- Information
- Verbose
- All

```yaml
Type: SeverityLevel
Parameter Sets: (All)
Aliases:
Accepted values: Undefined, Fatal, Error, Warning, Information, Verbose, All

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogFileMode
Specifies the new flags for the log file mode.
The EnableKd and DisableKd values parameters are applied on top of these flags.
This enumeration type is defined in $PsHome\Modules\BootEventCollector\SbecTraceHelpers.psm1.
The cmdlet automatically adds the RealTime and KdFilter values to this parameter.
Other frequently used flags for this context are:

- Secure.
Restricts who can log events to the session to those with TRACELOG_LOG_EVENT permission.
- UsePagedMemory.
Use the paged memory for the buffers.
- NoPerProcessorBuffering.
Write the events from all processors to the same buffer.
This preserves the order of the events, and is recommended for sending the events to the event collector.

The acceptable values for this parameter are:

- None
- FileNone
- FileSequential
- FileCircular
- FileAppend
- FileNewFile
- Reserved0x00000010
- FilePreallocate
- Nonstoppable
- Secure
- RealTime
- DelayOpenFile
- Buffering
- PrivateLogger
- AddHeader
- UseKilobytesForSize
- UseGlobalSequence
- Relog
- PrivateInProc
- BufferInterface
- KdFilter
- RealtimeRelog
- LostEventsDebug
- StopOnHybridShutdown
- PersistOnHybridShutdown
- UsePagedMemory
- SystemLogger
- Compressed
- IndependentSession
- NoPerProcessorBuffering
- Blocking
- Reserved0x40000000
- AddToTriageDump
- Fatal
- Error
- Warning
- Information
- Verbose
- All

```yaml
Type: LoggingMode
Parameter Sets: (All)
Aliases:
Accepted values: None, FileNone, FileSequential, FileCircular, FileAppend, FileNewFile, Reserved0x00000010, FilePreallocate, Nonstoppable, Secure, RealTime, DelayOpenFile, Buffering, PrivateLogger, AddHeader, UseKilobytesForSize, UseGlobalSequence, UseLocalSequence, Relog, PrivateInProc, BufferInterface, KdFilter, RealtimeRelog, LostEventsDebug, StopOnHybridShutdown, PersistOnHybridShutdown, UsePagedMemory, SystemLogger, Compressed, IndependentSession, NoPerProcessorBuffering, Blocking, Reserved0x40000000, AddToTriageDump

Required: False
Position: 10
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
Position: 8
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
Position: 7
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
Specifies the name of the session to create.

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

### -PassThru
Returns an object representing the item with which you are working.
By default, this cmdlet does not generate any output.

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

### -ProviderGuid
Specifies the provider GUIDs to subscribe this session to.
The providers are configured to include all events up to the level specified by the *Level* parameter.

```yaml
Type: Guid[]
Parameter Sets: (All)
Aliases: pg

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProviderName
Specifies the provider names to subscribe this session to.
The providers are configured to include all events up to the level specified by the *Level* parameter.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: pn

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SessionGuid
Specifies the GUID for the session.
By default the GUID gets generated and assigned automatically.

```yaml
Type: Guid
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### None.

## 输出

### SbecEtwTrace.TraceSessionInfo
`SbecEtwTrace.TraceSessionInfo` 类定义在 `$PsHome Modules\BootEventCollector\SbecTraceHelpers.psm1` 文件中。

## 备注

## 相关链接

[Get-SbecLogSession](./Get-SbecLogSession.md)

[Save-SbecLogSession](./Save-SbecLogSession.md)

[Set-SbecLogSession](./Set-SbecLogSession.md)

[Start-SbecLogSession](./Start-SbecLogSession.md)

[开始 SbecNtKernelLogSession 会话](./Start-SbecNtKernelLogSession.md)

[Stop-SbecLogSession](./Stop-SbecLogSession.md)

