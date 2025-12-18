---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: EventTracingManagement-help.xml
Module Name: EventTracingManagement
ms.date: 01/05/2017
online version: https://learn.microsoft.com/powershell/module/eventtracingmanagement/start-etwtracesession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-EtwTraceSession
---

# 启动 EtwTraceSession

## 摘要
使用指定的名称和设置启动一个ETW会话。

## 语法

```
Start-EtwTraceSession [-Name] <String> [-LogFileMode <UInt32>] [-LocalFilePath <String>]
 [-MaximumFileSize <UInt32>] [-BufferSize <UInt32>] [-MinimumBuffers <UInt32>] [-MaximumBuffers <UInt32>]
 [-FlushTimer <UInt32>] [-ClockType <String>] [-FileMode <String>] [-Compress] [-RealTime] [-NonPaged]
 [-CimSession <CimSession>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Start-EtwTraceSession` cmdlet 会使用指定的名称和设置来启动一个 ETW（事件跟踪）会话。

## 示例


## 参数

### -BufferSize
指定 Windows 事件跟踪（ETW）会话缓冲区的大小，单位为千字节。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ClockType
指定将用于记录到此ETW会话中的每个事件的时间戳类型。

这是一个高级的会话配置选项，不建议设置这个参数。

有关更多信息，请参阅[WNODE_HEADER结构](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364160.aspx)中**ClientContext**字段的描述，了解可用的不同时钟类型。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Performance, System, Cycle

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Compress
该参数用于控制 ETW（Event Tracing for Windows）是否应在缓冲区被填充时对其进行压缩。启用此参数会设置 *LogFileMode* 参数中的 **EVENT_TRACE_COMPRESSED_MODE** 位。

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

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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

### -FileMode
指定会话接收到的事件应如何被保存。`FileMode` 为常见的日志记录模式常量提供了相应的命名值；设置 `FileMode` 将会影响在创建会话时传递给 ETW 的 `LogFileMode` 的值。

如果您指定了此参数，请不要在*logFileMode*参数中指定任何文件或缓冲模式相关位。

有关可用模式的更多信息，请参阅 MSDN 中的 [日志记录模式常量](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364080.aspx)。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: File, Buffering, Sequential, Circular

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FlushTimer
设置此参数后，会以指定的秒数为间隔刷新会话中所有处于活动状态的缓冲区（buffer）的内容。

这是一个高级的会话配置选项，不建议设置这个参数。

如果该值没有被设置，ETW会根据*LogFileMode*选择一个合适的默认值。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LocalFilePath
指定 ETW 会话应写入的文件的完整路径。仅适用于非缓冲模式的会话。

在创建一个新的文件模式会话时，文件路径中的文件名必须包含一个 `%d`。

如果会话被配置为缓冲模式会话，请不要使用此参数。相反，应使用 **Save-EtwTraceSession** 将缓冲模式会话保存到磁盘上。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogFileMode
指定 ETW 会话日志记录模式。该值是 ETW 日志记录模式常量对应的位掩码（bitmask）。

有关更多信息，请参阅 MSDN 中的[日志记录模式常量](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364080.aspx)。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumBuffers
指定 ETW 会话应使用的缓冲区的最大数量。

ETW会话最多使用(*BufferSize* * *MaximumBuffers*)千字节的内存。根据指定的*LogFileMode*，这些内存可能是分页的，也可能不是分页的。

如果会话因为缓冲区无法快速刷新而丢失事件（即缓冲区的处理速度跟不上事件的生成速率），可以尝试增加这个数值。

配置会话以使用过多的缓冲区可能会影响系统性能。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumFileSize
指定输出.etl文件的最大文件大小（以兆字节为单位）。

该参数必须设置为循环文件模式、新建文件模式或顺序文件模式的ETW会话。

对于循环会话来说，一旦文件大小达到这个阈值，最旧的缓冲区将被新的缓冲区覆盖。

对于新文件会话来说，一旦文件大小达到这个限制，系统就会创建一个新文件，并将所有新的事件都写入到这个新文件中。

对于顺序文件会话来说，一旦文件大小达到这个限制，会话就会停止。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinimumBuffers
指定 ETW 会话应使用的缓冲区的最小数量。

ETW会话将至少使用(*BufferSize* * *MinimumBuffers*)千字节的内存。根据所指定的*logFileMode*，这些内存可能是分页的，也可能是非分页的。

如果会话因为缓冲区无法快速刷新而丢失事件（即缓冲区的处理速度跟不上事件的生成速率），可以尝试增加这个数值。

配置会话以使用过多的缓冲区可能会影响系统性能。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定 ETW（Event Tracing for Windows）跟踪会话的名称。

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

### -NonPaged
控制 ETW 是否应使用非分页内存池中的内存来存储会话缓冲区的数据。启用此参数会清除 *LogFileMode* 参数中的 **EVENT_TRACE_USE_PAGED_memory** 位。

只有当要发送到会话中的某些事件是从内核或驱动程序以高调度级别记录下来的时候，才需要使用非分页池中的内存来存储会话缓冲区。否则不应设置此参数。

从非分页内存池中分配过多的内存会严重降低系统性能。

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

### -RealTime
控制 ETW 是否允许实时消费者连接到会话中。启用此参数会在 *LogFileMode* 参数中设置 **EVENT_TRACEREAL_TIME_MODE** 位。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-EtwTraceSession](./Get-EtwTraceSession.md)

[New-EtwTraceSession](./New-EtwTraceSession.md)

[Save-EtwTraceSession](./Save-EtwTraceSession.md)

[Send-EtwTraceSession](./Send-EtwTraceSession.md)

[Stop-EtwTraceSession](./Stop-EtwTraceSession.md)

[更新 EtwTraceSession](./Update-EtwTraceSession.md)

