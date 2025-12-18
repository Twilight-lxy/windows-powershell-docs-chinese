---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_EtwTraceProvider_v1.0.cdxml-help.xml
Module Name: EventTracingManagement
ms.date: 01/05/2017
online version: https://learn.microsoft.com/powershell/module/eventtracingmanagement/add-etwtraceprovider?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-EtwTraceProvider
---

# 添加 TraceProvider

## 摘要
将一个 ETW（事件跟踪）跟踪提供程序添加到 ETW 跟踪会话或 AutoLogger 会话配置中。

## 语法

### BySession
```
Add-EtwTraceProvider [-Guid] <String> [-Level <Byte>] [-MatchAnyKeyword <UInt64>] [-MatchAllKeyword <UInt64>]
 [-Property <UInt32>] -SessionName <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 作者：ByAutologger
```
Add-EtwTraceProvider [-Guid] <String> -AutologgerName <String> [-Level <Byte>] [-MatchAnyKeyword <UInt64>]
 [-MatchAllKeyword <UInt64>] [-Property <UInt32>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-EtwTraceProvider` cmdlet 根据指定的参数，将一个 Event Tracing for Windows (ETW) 追踪提供者添加到指定的 ETW 追踪会话或 AutoLogger 会话配置中。

## 示例

### 示例 1：向 AutoLogger 配置中添加一个 ETW 跟踪提供者
```
PS C:\> Add-EtwTraceProvider -Guid "{5EEFEBDB-E90C-423A-8ABF-0241E7C5B87D}" -AutologgerName "WFP-IPsec Trace"
SessionName     :
AutologgerName  : WFP-IPsec Trace
Guid            : {5EEFEBDB-E90C-423A-8ABF-0241E7C5B87D}
Level           : 0
MatchAnyKeyword : 0x0
MatchAllKeyword : 0x0
Property        : 0
```

此命令将具有指定GUID的ETW跟踪提供程序添加到名为“WFP-IPsec Trace”的AutoLogger配置中。

### 示例 2：向 ETW 会话中添加一个 ETW 跟踪提供者
```
PS C:\> Add-EtwTraceProvider -Guid "{5EEFEBDB-E90C-423A-8ABF-0241E7C5B87D}" -SessionName "VMM"
SessionName     : VMM
AutologgerName  :
Guid            : {5EEFEBDB-E90C-423A-8ABF-0241E7C5B87D}
Level           : 0
MatchAnyKeyword : 0x0
MatchAllKeyword : 0x0
Property        : 0
```

此命令将具有指定GUID的ETW跟踪提供程序添加到名为VMM的会话中。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
Type: String
Parameter Sets: ByAutologger
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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
在运行 cmdlet 之前，会提示您确认是否要执行该操作。

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
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Level
指定允许收集事件的最大级别。

有关更多信息，请参阅 MSDN 上的 [EnableTraceEx2 函数](https://msdn.microsoft.com/en-us/library/windows/desktop/dd392305.aspx)。

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
指定一个关键字位掩码（bitmap），事件必须与该位掩码匹配才能被记录到会话中。

一个事件必须与该参数设置的每个关键词都匹配。在大多数情况下，使用*MatchAnyKeyword*参数更为合适。

有关更多信息，请参阅 MSDN 上的 [EnableTraceEx2 函数](https://msdn.microsoft.com/en-us/library/windows/desktop/dd392305.aspx)。

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
指定一个关键字位掩码（bitmap），事件必须与该位掩码匹配才能被记录到会话中。

一个事件必须至少与该参数设置的一个关键词集合相匹配。

有关更多信息，请参阅 MSDN 上的 [EnableTraceEx2 函数](https://msdn.microsoft.com/en-us/library/windows/desktop/dd392305.aspx)。

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

### -Property
指定用于从该提供者记录到会话中的事件的“Enable”属性。

有关更多信息，请参阅[配置和启动自动记录会话](https://msdn.microsoft.com/en-us/library/windowsdesktop/aa363687.aspx)。

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
Type: String
Parameter Sets: BySession
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 0，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[配置并启动自动记录器会话](https://msdn.microsoft.com/library/windows/desktop/aa363687.aspx)

[配置并启动事件追踪会话](https://msdn.microsoft.com/library/windowsdesktop/aa363688.aspx)

[Get-EtwTraceProvider](./Get-EtwTraceProvider.md)

[Remove-EtwTraceProvider](./Remove-EtwTraceProvider.md)

[Set-EtwTraceProvider](./Set-EtwTraceProvider.md)

