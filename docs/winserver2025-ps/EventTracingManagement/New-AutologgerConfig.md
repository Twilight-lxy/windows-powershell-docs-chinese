---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_AutologgerConfig_v1.0.cdxml-help.xml
Module Name: EventTracingManagement
ms.date: 01/05/2017
online version: https://learn.microsoft.com/powershell/module/eventtracingmanagement/new-autologgerconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-AutologgerConfig
---

# New-AutologgerConfig

## 摘要
在注册表中创建一个自动记录器会话配置。

## 语法

```
New-AutologgerConfig -Name <String> [-BufferSize <UInt32>] [-ClockType <ClockType>]
 [-DisableRealtimePersistence <UInt32>] [-FileCount <UInt32>] [-LocalFilePath <String>] [-FileMax <UInt32>]
 [-FlushTimer <UInt32>] [-Guid <String>] [-LogFileMode <UInt32>] [-MaximumFileSize <UInt32>]
 [-MaximumBuffers <UInt32>] [-MinimumBuffers <UInt32>] [-Start <Enabled>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-AutologgerConfig` cmdlet 会在注册表中创建一个自动记录器会话配置。

## 示例

### 示例 1：创建配置
```
PS C:\> New-AutoLoggerConfig -Name "WFP-IPsec Trace"
```

此命令创建了一个名为“WFP-IPsec Trace”的AutoLogger配置文件。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
指定ETW会话缓冲区的大小（以千字节为单位）。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定将用于记录到此ETW会话中的每个事件的时间戳类型。

这是一个高级的会话配置选项，不建议设置这个参数。

有关更多信息，请参阅[WNODE_HEADER结构](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364160.aspx)中**ClientContext**字段的描述，其中介绍了时钟类型的相关信息。

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

### -DisableRealtimePersistence
该设置用于控制实时会话中未发送的事件在Windows下次启动时是会被发送还是被丢弃。

有关更多信息，请参阅 MSDN 中的 [配置和启动自动记录器会话](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363687.aspx)。

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

### -FileCount
指定文件计数器的值。

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

### -FileMax
指定 AutoLogger 会话可以创建的最大日志文件数量。

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

### -FlushTimer
设置此参数后，会以指定的秒数为间隔刷新会话中所有处于活动状态的缓冲区（buffer）。

这是一个高级的会话配置选项，不建议设置这个参数。

如果该参数未设置，ETW将根据 *LogFileMode* 选择一个合适的默认值。

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

### -Guid
为这个自动记录器（AutoLogger）会话指定一个唯一的 GUID。

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

### -LocalFilePath
指定 ETW 会话应写入的文件的完整路径。仅适用于非缓冲模式的会话。

在创建一个新文件模式会话时，文件路径中的文件名必须包含一个 `%d`。

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
指定 ETW 会话日志记录模式。该值是 ETW 日志记录模式常量对应的位掩码（bitmap）。

有关更多信息，请参阅 MSDN 中的 [日志记录模式常量](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364080.aspx)。

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

ETW会话最多使用(* bufferSize* * *MaximumBuffers*)千字节的内存。根据指定的*LogFileMode*，这些内存可能是分页的，也可能不是分页的。

如果会话因缓冲区无法快速刷新而丢失事件（即刷新速度跟不上事件的生成速率），可以尝试增加这个数值。

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

该参数必须设置为用于循环文件、新文件或顺序文件模式的 ETW（Event Tracking Windows）会话。

对于循环进行的会话，一旦文件大小达到这个限制，最旧的缓冲区将会被新的缓冲区覆盖。

对于新文件会话（new-file sessions），当文件大小达到某个阈值时，系统会创建一个新文件，并将所有新的事件数据写入这个新文件中。

对于顺序文件会话而言，一旦文件大小达到这个限制，该会话就会停止。

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
指定ETW会话应使用的缓冲区的最小数量。

ETW会话将至少使用(*BufferSize* * *MinimumBuffers*)千字节的内存。根据指定的*LogFileMode*，这些内存可能是分页的，也可能是非分页的。

如果会话因缓冲区无法快速刷新而丢失事件（即刷新速度跟不上事件的生成速率），可以尝试增加这个数值。

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

### -Name
指定新的 AutoLogger 会话的名称。该名称将作为由此 AutoLogger 创建的 ETW（事件跟踪）会话的名称被使用。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Start
如果设置为“Enabled”，则当Windows启动时，将为这个AutoLogger创建一个ETW（事件跟踪）会话。

```yaml
Type: Enabled
Parameter Sets: (All)
Aliases:
Accepted values: Disabled, Enabled

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[配置并启动自动日志记录会话](https://msdn.microsoft.com/library/windowsdesktop/aa363687.aspx)

[日志模式常量](https://msdn.microsoft.com/library/windowsdesktop/aa364080.aspx)

[WNODE_HEADER 结构](https://msdn.microsoft.com/library/windows/desktop/aa364160.aspx)

[Get-AutologgerConfig](./Get-AutologgerConfig.md)

[Remove-AutologgerConfig](./Remove-AutologgerConfig.md)

[更新自动记录器配置](./Update-AutologgerConfig.md)

