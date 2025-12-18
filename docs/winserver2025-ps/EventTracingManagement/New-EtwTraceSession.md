---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_EtwTraceSession_v1.0.cdxml-help.xml
Module Name: EventTracingManagement
ms.date: 01/05/2017
online version: https://learn.microsoft.com/powershell/module/eventtracingmanagement/new-etwtracesession?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-EtwTraceSession
---

# New-EtwTraceSession

## 摘要
创建一个ETW跟踪会话。

## 语法

```
New-EtwTraceSession [-Name] <String> [-LogFileMode <UInt32>] [-LocalFilePath <String>]
 [-MaximumFileSize <UInt32>] [-BufferSize <UInt32>] [-MinimumBuffers <UInt32>] [-MaximumBuffers <UInt32>]
 [-FlushTimer <UInt32>] [-ClockType <ClockType>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Start-EtwTraceSession` cmdlet 已取代了原有的 cmdlet，成为启动 ETW（事件跟踪）会话的推荐方法。它提供了一种更简便的方式来指定常见的 `LogFileMode` 设置和其他参数。

`New-EtwTraceSession` cmdlet 用于创建一个 Windows 事件跟踪（ETW）会话。

## 示例

### 示例 1：创建一个 ETW 跟踪会话
```
PS C:\> New-EtwTraceSession -Name "NetCfgTrace" -MaximumBuffers 24
```

此命令创建了一个名为 NetCfgTrace 的 ETW（事件跟踪）会话，该会话的 *MaximumBuffers* 参数值为 24。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，随后再显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `-*Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
指定 ETW 会话缓冲区的大小（单位：千字节）。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

这是一个高级会话配置选项，不建议设置该参数。

有关更多信息，请参阅[WNODE_HEADER结构](https://msdn.microsoft.com/en-us/library/windowsdesktop/aa364160.aspx)中**ClientContext**字段的描述，以了解可用的不同时钟类型。

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

### -FlushTimer
设置此值后，会以指定的秒数为间隔刷新会话中所有处于活动状态的缓冲区内容。

这是一个高级会话配置选项，不建议设置该参数。

如果该值没有被设置，ETW将根据 LogFileMode 选择一个合适的默认值。

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
指定 ETW 会话日志记录模式。该值是 ETW 日志记录模式常量对应的位掩码（bitmap）。有关有效值的详细信息，请参阅 [日志记录模式常量](https://msdn.microsoft.com/library/windows/desktop/aa364080.aspx)。

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

ETW会话最多使用`( bufferSize * MaximumBuffers)`千字节的内存。根据指定的`LogFileMode`，这些内存可能是分页的，也可能是非分页的。

如果会话因为缓冲区无法快速刷新而导致事件丢失（即缓冲区的处理速度跟不上传入事件的速度），可以尝试增加这个数值。

配置一个会话以使用过多的缓冲区可能会影响系统性能。

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

该参数必须设置为圆形文件模式、新文件模式或顺序文件模式的ETW会话。

对于循环会话来说，一旦文件大小达到这个限制，最旧的缓冲区将被新的缓冲区覆盖。

对于新文件会话而言，当文件大小达到这个阈值时，系统会创建一个新文件，并将所有新的事件都写入到这个新文件中。

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

ETW会话将至少使用`( bufferSize * MinimumBuffers)`千字节的内存。根据指定的`LogFileMode`，这些内存可能是分页的，也可能是非分页的。

如果会话因为缓冲区无法足够快地刷新以跟上传入事件的速率而丢失事件，请尝试增加这个值。

配置一个会话以使用过多的缓冲区可能会影响系统性能。

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
指定新的 ETW （事件跟踪）会话的名称。

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

### -ThrottleLimit
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最优限制值。此限制仅适用于当前运行的cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-EtwTraceSession](./Get-EtwTraceSession.md)

[Save-EtwTraceSession](./Save-EtwTraceSession.md)

[Send-EtwTraceSession](./Send-EtwTraceSession.md)

[开始 ETW 跟踪会话](./Start-EtwTraceSession.md)

[Stop-EtwTraceSession](./Stop-EtwTraceSession.md)

[更新-EtwTraceSession](./Update-EtwTraceSession.md)

