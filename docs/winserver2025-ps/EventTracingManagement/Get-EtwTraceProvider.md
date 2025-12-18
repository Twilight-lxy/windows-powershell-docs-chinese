---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_EtwTraceProvider_v1.0.cdxml-help.xml
Module Name: EventTracingManagement
ms.date: 01/05/2017
online version: https://learn.microsoft.com/powershell/module/eventtracingmanagement/get-etwtraceprovider?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-EtwTraceProvider
---

# Get-EtwTraceProvider

## 摘要
列出现有的AutoLogger会话配置。

## 语法

### 由 Autologger （默认设置）生成
```
Get-EtwTraceProvider [[-Guid] <String[]>] [-AutologgerName <String[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 按会话（BySession）
```
Get-EtwTraceProvider [[-Guid] <String[]>] [-SessionName <String[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-EtwTraceProvider` cmdlet 用于枚举现有的 AutoLogger 会话配置。

## 示例

### 示例 1：查看所有可用的跟踪提供者
```
PS C:\> Get-NetEventProvider -ShowInstalled | Select-Object -Property *
```

此命令使用 **Get-NetEventProvider** cmdlet 获取当前计算机上所有可用的 ETW（事件跟踪）提供程序及其 GUID 的列表。有关更多信息，请输入 `Get-Help Get-NetEventProvider`。

### 示例 2：获取 ETW 会话的跟踪提供程序
```
PS C:\> Get-EtwTraceProvider -SessionName "NtfsLog"
SessionName     : NtfsLog
AutologgerName  :
Guid            : {9C88041D-349D-4647-8BFD-2C0A167BFE58}
Level           : 4
MatchAnyKeyword : 0xFFFFFFFFFFFFFFFF
MatchAllKeyword : 0x0
Property        : 0

SessionName     : NtfsLog
AutologgerName  :
Guid            : {5EEFEBDB-E90C-423A-8ABF-0241E7C5B87D}
Level           : 0
MatchAnyKeyword : 0x0
MatchAllKeyword : 0x0
Property        : 0
```

这个命令会获取名为“NtfsLog”的ETW会话的所有跟踪提供者（trace providers）。

### 示例 3：获取 AutoLogger 配置的跟踪提供者
```
PS C:\> Get-EtwTraceProvider -AutologgerName "WdiContextLog"
SessionName     :
AutologgerName  : WdiContextLog
Guid            : 1D75856D-36A7-4ECB-A3F5-B13152222D29
Level           : 0
MatchAnyKeyword : 0x0
MatchAllKeyword : 0x0
Property        : 0

SessionName     :
AutologgerName  : WdiContextLog
Guid            : {1D75856D-36A7-4ECB-A3F5-B13152222D29}
Level           : 0
MatchAnyKeyword : 0x0
MatchAllKeyword : 0x0
Property        : 0
```

这个命令会获取名为 WdiContextLog 的 AutoLogger 配置的所有跟踪提供者（trace providers）。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -Guid
指定提供者ID。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算一个最优的限流值。这个限流值仅适用于当前的 cmdlet，而不适用于整个会话或整个计算机。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[配置并启动自动记录器会话](https://msdn.microsoft.com/library/windows/desktop/aa363687.aspx)

[配置并启动事件追踪会话](https://msdn.microsoft.com/library/windows/desktop/aa363688.aspx)

[Add-EtwTraceProvider](./Add-EtwTraceProvider.md)

[Remove-EtwTraceProvider](./Remove-EtwTraceProvider.md)

[Set-EtwTraceProvider](./Set-EtwTraceProvider.md)

