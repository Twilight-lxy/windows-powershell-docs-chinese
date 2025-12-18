---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/start-sbecntkernellogsession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-SbecNtKernelLogSession
---

# 启动 SbecNtKernelLogSession 会话

## 摘要
启动一个 NT 内核日志记录会话，并将事件转发到收集器（Collector）。

## 语法

```
Start-SbecNtKernelLogSession [[-ClockType] <ClientContext>] [[-BufferSize] <UInt32>]
 [[-MinimumBufferCount] <UInt32>] [[-MaximumBufferCount] <UInt32>] [[-FlushSeconds] <UInt32>]
 [[-KernelEnableFlags] <EventTraceFlag>] [-PassThru] [<CommonParameters>]
```

## 描述
`Start-SbecNtKernelLogSession` cmdlet 用于启动一个实时的 NT 内核日志记录会话，并将产生的事件转发到相应的收集器（Collector）。该会话的名称固定为 “NT Kernel Logger”，其 GUID 固定为 `{9e814aad-3204-11d2-9a82-006008a86939}`。

## 示例


## 参数

### -BufferSize
指定会话的缓冲区大小（以千字节为单位）。这表示一个缓冲区的大小，而缓冲区的数量由 *MinimumBufferCount* 和 *MaximumBufferCount* 参数来控制。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ClockType
指定用于本次会话收集的事件的时间戳类型（时钟类型）。该参数的可接受值包括：

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
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FlushSeconds
指定会话缓冲区自动清空的超时时间（以秒为单位）。您可以通过将此参数设置为 0 来禁用超时时的缓冲区清除功能；在这种情况下，缓冲区仅会在满载或手动执行清除操作时才会被写入。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: FlushTimer

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -KernelEnableFlags
用于指定 NT 内核日志记录器（NT Kernel Logger）的标志，这些标志可以启用内核事件记录功能。在系统设置和启动监控过程中，唯一合理的标志是 “Process”。这种枚举类型定义在文件 $PsHome\Modules\BootEventCollector\SbecTraceHelpers.psm1 中。该参数的可接受取值为：

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
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumBufferCount
指定为此会话分配的最大缓冲区数量。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: MaximumBuffers, maxbuf

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinimumBufferCount
指定为此会话分配的最小缓冲区数量。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: MinimumBuffers, minbuf

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个对象，该对象表示您正在操作的项。默认情况下，此 cmdlet 不会生成任何输出。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的内容）。

## 输出

### SbecEtwTrace.TraceSessionInfo
`SbecEtwTrace.TraceSessionInfo` 类定义在 `$PsHomeModules\BootEventCollector\SbecTracehelpers.psm1` 文件中。

## 备注

## 相关链接

[Get-SbecLogSession](./Get-SbecLogSession.md)

[开始 SbecLogSession 会话](./Start-SbecLogSession.md)

[Start-SbecSimpleLogSession](./Start-SbecSimpleLogSession.md)

[Stop-SbecLogSession](./Stop-SbecLogSession.md)

[Set-SbecLogSession](./Set-SbecLogSession.md)

[Save-SbecLogSession](./Save-SbecLogSession.md)

