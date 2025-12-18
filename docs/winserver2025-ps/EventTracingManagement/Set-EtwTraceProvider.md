---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_EtwTraceProvider_v1.0.cdxml-help.xml
Module Name: EventTracingManagement
ms.date: 01/05/2017
online version: https://learn.microsoft.com/powershell/module/eventtracingmanagement/set-etwtraceprovider?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-EtwTraceProvider
---

# 设置 EtwTraceProvider

## 摘要
在 ETW 或 AutoLogger 会话中修改提供者的启用设置。

## 语法

### 由 Autologger（默认设置）生成
```
Set-EtwTraceProvider [[-Guid] <String[]>] [-AutologgerName <String[]>] [-Level <Byte>]
 [-MatchAnyKeyword <UInt64>] [-MatchAllKeyword <UInt64>] [-Property <UInt32>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 按会话（BySession）
```
Set-EtwTraceProvider [[-Guid] <String[]>] [-SessionName <String[]>] [-Level <Byte>] [-MatchAnyKeyword <UInt64>]
 [-MatchAllKeyword <UInt64>] [-Property <UInt32>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-EtwTraceProvider -InputObject <CimInstance[]> [-Level <Byte>] [-MatchAnyKeyword <UInt64>]
 [-MatchAllKeyword <UInt64>] [-Property <UInt32>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-EtwTraceProvider` cmdlet 用于修改在 Event Tracing for Windows (ETW) 或 AutoLogger 会话中某个提供者的启用设置。

## 示例

#### 示例 1：修改 ETW 跟踪提供程序
```
PS C:\> set-EtwTraceProvider -Guid "{106B464A-8043-46B1-8CB8-E92A0CD7A560}" -AutologgerName "WFP-IPsec Trace" -Level 2
SessionName     :
AutologgerName  : WFP-IPsec Trace
Guid            : {106B464A-8043-46B1-8CB8-E92A0CD7A560}
Level           : 2
MatchAnyKeyword : 0xFFFFFFFF
MatchAllKeyword : 0x0
Property        :
```

此命令用于修改具有指定 GUID 的 ETW（事件跟踪）追踪提供者。该提供者与名为 “WFP-IPsec Trace” 的自动记录器（AutoLogger）配置相关联。该命令将追踪提供者的 *Level* 属性设置为值 2（即 TRACE_LEVEL_ERROR）。

## 参数

### -AsJob
将该 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -AutologgerName
指定目标 AutoLogger 会话的名称。

```yaml
Type: String[]
Parameter Sets: ByAutologger
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。您可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -Guid
指定提供者ID。

```yaml
Type: String[]
Parameter Sets: ByAutologger, BySession
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InputObject
指定要传递给此cmdlet的输入数据。你可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

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

### -Level
指定可以为某个集合启用的最高事件级别。

有关事件级别的更多信息，请参阅 MSDN 中的 [EnableTraceEx2 函数](https://msdn.microsoft.com/en-us/library/windows/desktop/dd392305.aspx)。

```yaml
Type: Byte
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MatchAllKeyword
指定一个关键字位掩码（bitmask），事件必须与该掩码匹配才能被记录到会话中。

一个事件必须与该参数设置的每个关键词都匹配。

大多数情况下，*MatchAnyKeyword* 参数更为合适。

有关关键词的更多信息，请参阅[EnableTraceEx2函数](https://msdn.microsoft.com/en-us/library/windows/desktop/dd392305.aspx)。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MatchAnyKeyword
指定一个关键字位掩码（bitmask），事件必须与该掩码匹配才能被记录到会话中。

某个事件必须至少与该参数所设置的一个关键词集合相匹配。

有关关键词的更多信息，请参阅[EnableTraceEx2函数](https://msdn.microsoft.com/en-us/library/windowsdesktop/dd392305.aspx)。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
表示该 cmdlet 返回一个对象，该对象代表其所操作的项目。默认情况下，此 cmdlet 不会生成任何输出。

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

### -Property
指定用于从该提供者记录到会话中的事件的 **EnableProperty** 属性。

有关**EnableProperty**的更多信息，请参阅MSDN中的[配置和启动AutoLogger会话](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363687.aspx)。

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

### -SessionName
指定目标 ETW 会话的名称。

```yaml
Type: String[]
Parameter Sets: BySession
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前正在执行的 cmdlet，而不影响整个会话或整个计算机。

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
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[配置并启动自动日志记录会话](https://msdn.microsoft.com/library/windows/desktop/aa363687.aspx)

[配置并启动事件跟踪会话](https://msdn.microsoft.com/library/windows/desktop/aa363688.aspx)

[Add-EtwTraceProvider](./Add-EtwTraceProvider.md)

[Get-EtwTraceProvider](./Get-EtwTraceProvider.md)

[Remove-EtwTraceProvider](./Remove-EtwTraceProvider.md)

