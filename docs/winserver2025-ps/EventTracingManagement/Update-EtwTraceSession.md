---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_EtwTraceSession_v1.0.cdxml-help.xml
Module Name: EventTracingManagement
ms.date: 01/05/2017
online version: https://learn.microsoft.com/powershell/module/eventtracingmanagement/update-etwtracesession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-EtwTraceSession
---

# 更新 EtwTraceSession

## 摘要
修改现有的ETW会话。

## 语法

### 按名称排序（默认值）
```
Update-EtwTraceSession [-Name] <String[]> [-LogFileMode <UInt32>] [-LocalFilePath <String>]
 [-MaximumFileSize <UInt32>] [-BufferSize <UInt32>] [-MaximumBuffers <UInt32>] [-FlushTimer <UInt32>]
 [-ClockType <ClockType>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Update-EtwTraceSession -InputObject <CimInstance[]> [-LogFileMode <UInt32>] [-LocalFilePath <String>]
 [-MaximumFileSize <UInt32>] [-BufferSize <UInt32>] [-MaximumBuffers <UInt32>] [-FlushTimer <UInt32>]
 [-ClockType <ClockType>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Update-EtwTraceSession` cmdlet 用于修改现有的 Windows 事件跟踪（ETW）会话。

## 示例


## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后会显示命令提示符。在该作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -BufferSize
指定 ETW 会话缓冲区的大小，单位为千字节（kilobytes）。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -ClockType
指定将用于记录到此 ETW 会话中的每个事件的时间戳类型。

这是一个高级的会话配置选项，不建议设置这个参数。

有关更多信息，请参阅[WNODE_HEADER结构](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364160.aspx)中**ClientContext**字段的描述，该描述涵盖了可用的各种时钟类型。

```yaml
Type: ClockType
Parameter Sets: (All)
Aliases:
Accepted values: Performance, System, Cycle

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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

### -FlushTimer
设置该参数后，会以指定的秒数为间隔刷新当前会话中所有处于活动状态的缓冲区（buffer）。

这是一个高级的会话配置选项，不建议设置这个参数。

如果该值没有被设置，ETW将根据 *LogFileMode* 选择合适的默认值。

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

### -InputObject
指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给该 cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -LocalFilePath
指定 ETW 会话应写入文件的完整路径。仅适用于非缓冲模式的会话。

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
指定 ETW（Events Tracing Wizard）会话日志记录模式。该值是 ETW 日志记录模式常量对应的位掩码（bitmask）。有关有效的值，请参阅[日志记录模式常量](https://msdn.microsoft.com/library/windows/desktop/aa364080.aspx)。

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
指定 ETW 会话应使用的最大缓冲区数量。

ETW会话最多使用（bufferSize * MaximumBuffers）千字节的内存。根据指定的*logFileMode*，这些内存可能是分页内存，也可能不是分页内存。

如果会话因为缓冲区无法快速刷新而丢失事件（即缓冲区的处理速度跟不上传入事件的数量），可以尝试增加这个数值。

配置会话时使用过多的缓冲区可能会影响系统性能。

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

该参数必须设置为圆形文件、新文件或顺序文件模式的ETW会话。

对于循环进行的会话（即会话不断重复进行），一旦文件大小达到这个限制，最旧的缓冲区数据将被新的缓冲区数据覆盖。

对于新文件会话来说，一旦文件大小达到这个阈值，系统就会创建一个新文件，并将所有新的事件都写入到这个新文件中。

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

### -Name
指定 ETW 会话的名称。

```yaml
Type: String[]
Parameter Sets: ByName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
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

### -ThrottleLimit
该参数用于指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-EtwTraceSession](./Get-EtwTraceSession.md)

[New-EtwTraceSession](./New-EtwTraceSession.md)

[Save-EtwTraceSession](./Save-EtwTraceSession.md)

[Send-EtwTraceSession](./Send-EtwTraceSession.md)

[开始 ETW 跟踪会话](./Start-EtwTraceSession.md)

[Stop-EtwTraceSession](./Stop-EtwTraceSession.md)

