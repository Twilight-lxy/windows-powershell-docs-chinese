---
description: 修改现有的AutoLogger会话配置。
external help file: MSFT_AutologgerConfig_v1.0.cdxml-help.xml
Module Name: EventTracingManagement
ms.date: 10/01/2021
online version: https://learn.microsoft.com/powershell/module/eventtracingmanagement/update-autologgerconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-AutologgerConfig
---

# 更新 Autologger 配置

## 摘要
修改现有的AutoLogger会话配置。

## 语法

### 按名称排序（默认值）
```
Update-AutologgerConfig [-Name] <String[]> [-BufferSize <UInt32>] [-ClockType <ClockType>]
 [-DisableRealtimePersistence <UInt32>] [-LocalFilePath <String>] [-FileMax <UInt32>] [-FlushTimer <UInt32>]
 [-Guid <String>] [-LogFileMode <UInt32>] [-MaximumFileSize <UInt32>] [-MaximumBuffers <UInt32>]
 [-MinimumBuffers <UInt32>] [-Start <UInt32>] [-InitStatus <UInt32>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject（cdxml）
```
Update-AutologgerConfig -InputObject <CimInstance[]> [-BufferSize <UInt32>] [-ClockType <ClockType>]
 [-DisableRealtimePersistence <UInt32>] [-LocalFilePath <String>] [-FileMax <UInt32>] [-FlushTimer <UInt32>]
 [-Guid <String>] [-LogFileMode <UInt32>] [-MaximumFileSize <UInt32>] [-MaximumBuffers <UInt32>]
 [-MinimumBuffers <UInt32>] [-Start <UInt32>] [-InitStatus <UInt32>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Update-AutologgerConfig` cmdlet 用于修改现有的 AutoLogger 会话配置。

## 示例

### 示例 1：修改配置
```
PS C:\> Update-AutologgerConfig -Name "WFP-IPsec Trace" -MaximumBuffers 8 -ClockType Cycle
```

此命令用于修改名为“WFP-IPsec Trace”的AutoLogger配置文件。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -BufferSize
指定 Windows 事件跟踪（ETW）跟踪会话缓冲区的大小，单位为 KB。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，使用的是本地计算机上的当前会话。

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

有关更多信息，请参阅[WNODE_HEADER结构](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364160.aspx)中**ClientContext**字段的描述，以了解时钟类型的详细信息。

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

### -DisableRealtimePersistence
该参数用于指定是否要保留那些在计算机关闭之前未能成功发送的实时事件。被保留的事件会在消费者下次连接到会话时再次发送给该消费者。若要禁用实时事件的保留功能，请设置值为 1；若要保持事件的历史记录，请设置值为 0。默认值为 0。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
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
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -FlushTimer
指定用于 ETW（事件跟踪）会话刷新捕获缓冲区的超时值。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -Guid
Specifies an AutoLogger session configuration ID.
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

### -InitStatus
Specifies the initial status of the AutoLogger configuration.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
Specifies the input to this cmdlet.
You can use this parameter, or you can pipe the input to this cmdlet.

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
Specifies the full path for an ETW log file.

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
Specify one or more log modes, such as **EVENT_TRACE_REAL_TIME_MODE** 0x100.
Each mode is a bit field.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumBuffers
Specifies the maximum number of buffers for an ETW trace session.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumFileSize
Specifies the maximum size, in MB, of a log file before a new one is created.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinimumBuffers
Specifies the minimum number of buffers for an ETW trace session.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
Specifies the name of the AutoLogger session.

```yaml
Type: String[]
Parameter Sets: ByName
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
Indicates that this cmdlet returns an object that represents the item on which it operates.
By default, this cmdlet does not generate any output.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Start
By default, the AutoLogger session is configured to start at boot time.

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#ROOT\Microsoft\Windows_EVENTTracingManagement\MSFT_AutologgerConfig

## 备注

## 相关链接

[配置和启动自动日志记录会话](https://msdn.microsoft.com/library/windowsdesktop/aa363687.aspx)

[日志记录模式常量](https://msdn.microsoft.com/library/windowsdesktop/aa364080.aspx)

[WNODE_HEADER 结构](https://msdn.microsoft.com/library/windows/desktop/aa364160.aspx)

[Get-AutologgerConfig](./Get-AutologgerConfig.md)

[New-AutologgerConfig](./New-AutologgerConfig.md)

[Remove-AutologgerConfig](./Remove-AutologgerConfig.md)
