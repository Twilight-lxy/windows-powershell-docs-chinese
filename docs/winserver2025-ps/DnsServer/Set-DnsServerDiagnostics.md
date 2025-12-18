---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerDiagnostics_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverdiagnostics?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerDiagnostics
---

# Set-DnsServerDiagnostics

## 摘要
设置调试和日志记录参数。

## 语法

### 参数（默认值）
```
Set-DnsServerDiagnostics [-ComputerName <String>] [-PassThru] [-Answers <Boolean>] [-EventLogLevel <UInt32>]
 [-FullPackets <Boolean>] [-IPFilterList <IPAddress[]>] [-LogFilePath <String>] [-MaxMBFileSize <UInt32>]
 [-EnableLoggingForRemoteServerEvent <Boolean>] [-EnableLoggingForPluginDllEvent <Boolean>]
 [-UseSystemEventLog <Boolean>] [-EnableLogFileRollover <Boolean>]
 [-EnableLoggingForZoneLoadingEvent <Boolean>] [-EnableLoggingForLocalLookupEvent <Boolean>]
 [-EnableLoggingToFile <Boolean>] [-EnableLoggingForZoneDataWriteEvent <Boolean>]
 [-EnableLoggingForTombstoneEvent <Boolean>] [-EnableLoggingForRecursiveLookupEvent <Boolean>]
 [-UdpPackets <Boolean>] [-UnmatchedResponse <Boolean>] [-Updates <Boolean>] [-WriteThrough <Boolean>]
 [-SaveLogsToPersistentStorage <Boolean>] [-EnableLoggingForServerStartStopEvent <Boolean>]
 [-Notifications <Boolean>] [-Queries <Boolean>] [-QuestionTransactions <Boolean>] [-ReceivePackets <Boolean>]
 [-SendPackets <Boolean>] [-TcpPackets <Boolean>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

###LogLevel
```
Set-DnsServerDiagnostics [-ComputerName <String>] [-PassThru] [-DebugLogging <UInt32>]
 [-OperationLogLevel2 <UInt32>] [-OperationLogLevel1 <UInt32>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 所有
```
Set-DnsServerDiagnostics [-ComputerName <String>] [-PassThru] -All <Boolean> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsServerDiagnostics` cmdlet 用于设置域名系统（DNS）服务器的调试和日志记录参数。

要启用调试日志记录，请为 *FullPackets* 参数指定一个值为 $True 的值，并执行以下操作：

- Set the *ReceivePackets* parameter or the *SendPackets* parameter to $True.
- Set the *TcpPackets* parameter or the *UdpPackets* parameter to $True.
- Set the *Notifications* parameter, the *Queries* parameter, or the *Updates* parameter to $True.
- Set the *QuestionTransactions* parameter or the *Answers* parameter to $True.

如果您使用的是“Parameters”参数集，那么必须在以下每对参数中至少指定一个选项：

- **ReceivePackets**, **SendPackets**
- **TcpPackets**, **UdpPackets**
- **Notifications**, **Updates**, **Queries**
- **QuestionTransactions**, **Answers**

“All”参数组合会启用除以下选项之外的所有选项：**LogFilePath**、**MaxMBFileSize**、**EventLogLevel**、**FilterIpAddrList**、**UseSystemEventLog** 和 **EnableLogFileRollover**。

使用 `LogLevel` 参数可以在更详细的级别上启用诊断功能。

## 示例

### 示例 1：为更新请求中的出站 TCP 响应启用诊断功能
```
PS C:\> Set-DnsServerDiagnostics -SendPackets $True -TcpPackets $True -Answers $True -Updates $True
```

此命令可启用对出站TCP响应的诊断功能，以便进行更新操作。

### 示例 2：启用所有诊断选项，除了 LogFilePath
```
PS C:\> Set-DnsServerDiagnostics -All $True
```

此命令启用了DNS服务器诊断的所有选项，除了**LogFilePath**之外。

### 示例 3：日志发送数据包
```
PS C:\> Set-DnsServerDiagnostics -DebugLogging 0x10000
```

这个命令用于记录发送的数据包信息。

### 示例 4：重置调试设置
```
PS C:\> Get-DnsServerDiagnostics -ComputerName "DNSServer01" | select -TcpPackets, -UdpPackets | Set-DnsServerDiagnostics -ComputerName "DNSServer02"
```

这个命令将 DNSServer02 上的 TCP 数据包调试和 UDP 数据包调试选项重置为与 DNSServer01 相同的值。

## 参数

### -All
指定DNS服务器是否记录所有事件。

```yaml
Type: Boolean
Parameter Sets: All
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Answers
指定是否启用DNS响应的日志记录功能。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -ComputerName
用于指定一个DNS服务器。该参数的可接受值包括：IPv4地址、IPv6地址，以及任何能够解析为IP地址的其他值（如完全限定域名（FQDN）、主机名或NETBIOS名称）。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Cn

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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

### -DebugLogging
用于指定调试日志记录的位掩码（bitmask）。有效值包括：

- 0x00000001. The server logs query packet exchanges.
- 0x00000010. The server logs packet exchanges that are related to zone exchanges.
- 0x00000020. The server logs packet exchanges that are related to zone updates.
- 0x00000100. The server logs packets that contain questions.
- 0x00000200. The server logs packets that contain answers.
- 0x00001000. The server logs packets that it sends.
- 0x00002000. The server logs packets that it receives.
- 0x00004000. The server logs User Datagram Protocol (UDP) packet exchanges.
- 0x00008000. The server logs Transmission Control Protocol (TCP) packet exchanges.
- 0x0000FFFF. The server logs operations if you set the following fields to $True: 0x00001000, 0x00002000, 0x00008000, 0x00004000, 0x00000001, 0x00000001, 0x00000020, 0x00000100, and 0x00000200S.
- 0x00010000. Independent of other field values, this bitmap logs Active Directory write operations.
- 0x00020000. Independent of other field values, this bitmap logs Active Directory polling operations and operations that occur during DNS updates (secure and not secure) on Active Directory-integrated zones.
- 0x01000000. If other field values allow it, the server logs the entire packet to the log file.
- 0x02000000. If other field values allow it, the server logs response packets that do not match any outstanding queries.
- 0x80000000. If other field values allow it, the server saves packet logging information to persistent storage.

```yaml
Type: UInt32
Parameter Sets: LogLevel
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableLogFileRollover
指定是否启用日志文件的滚动（即当日志文件满时自动创建新的日志文件）。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableLoggingForLocalLookupEvent
指定DNS服务器是否记录本地查询事件。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableLoggingForPluginDllEvent
指定DNS服务器是否记录动态链接库（DLL）插件事件。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableLoggingForRecursiveLookupEvent
指定DNS服务器是否记录递归查询事件。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableLoggingForRemoteServerEvent
指定DNS服务器是否记录远程服务器的事件。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableLoggingForServerStartStopEvent
指定DNS服务器是否记录服务器启动和停止事件。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableLoggingForTombstoneEvent
指定DNS服务器是否记录“墓碑事件”（tombstone events）。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableLoggingForZoneDataWriteEvent
该选项用于指定DNS服务器是否记录区域数据写入事件。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableLoggingForZoneLoadingEvent
指定DNS服务器是否记录区域加载事件。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableLoggingToFile
指定DNS服务器是否将日志记录到文件中。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EventLogLevel
指定事件日志的级别。有效值为：

- 0: No Events
- 1: Errors Only
- 2: Errors and warnings
- 3-7: All Events

```yaml
Type: UInt32
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -FullPackets
指定DNS服务器是否记录完整的数据包（即数据包中的所有内容）。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IPFilterList
指定一个用于过滤的 IP 地址数组。当启用日志记录功能时，这些 IP 地址之间的网络流量会被记录下来。如果您没有指定任何 IP 地址，那么所有 IP 地址之间的网络流量都会被记录。

```yaml
Type: IPAddress[]
Parameter Sets: Parameters
Aliases: FilterIPAddressList

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LogFilePath
指定一个日志文件的路径。

```yaml
Type: String
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MaxMBFileSize
指定日志文件的最大大小。如果您将 **EnableLogFileRollover** 和 **EnableLoggingToFile** 设置为 $True，则此参数非常有用。

```yaml
Type: UInt32
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Notifications
指定DNS服务器是否记录通知信息。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -OperationLogLevel1
用于指定日志记录级别的位标志。有效值包括：

- 0x00000001. The DNS server saves operational logging information to persistent storage.
- 0x00000010. The DNS server logs event logging information to a log file.
- 0x00000020. The DNS server logs operational logging information for server start and stop activities to the log file.
- 0x00002000. The DNS server logs operational logging information for activities that are related to loading a zone from a directory server to the log file.
- 0x00004000. The DNS server logs operational logging information for activities that are related to writing zone data to the directory server to the log file.
- 0x00020000. The DNS server logs operational logging information for activities that are related to updating nodes that have exceeded the tombstone lifetime to the log file.
- 0x00100000. The DNS server logs operational logging information for local resource lookup activities to the log file.
- 0x00200000. The DNS server logs operational logging information for activities that occur during recursive query lookup to the log file.
- 0x00400000. The DNS server logs operational logging information for activities that are related to interaction with remote name servers to the log file.

```yaml
Type: UInt32
Parameter Sets: LogLevel
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -OperationLogLevel2
指定DNS服务器需要记录的额外操作。默认的有效值为：

0x01000000。该参数的有效值为：0x01、0x02 和 0x03。DNS 服务器会将与插件 DLL 相关的操作活动日志信息记录到日志文件中。

```yaml
Type: UInt32
Parameter Sets: LogLevel
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -Queries
指定DNS服务器是否允许查询数据包通过内容过滤器（例如*IPFilterList*参数）进行传输。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -QuestionTransactions
指定DNS服务器是否记录查询日志。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReceivePackets
指定DNS服务器日志是否接收数据包。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SaveLogsToPersistentStorage
指定DNS服务器是否将日志保存到持久存储中。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SendPackets
指定DNS服务器日志是否记录数据包的发送情况。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TcpPackets
指定DNS服务器是否记录TCP数据包。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或整个计算机。

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

### -UdpPackets
指定DNS服务器是否记录UDP数据包。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -UnmatchedResponse
指定DNS服务器是否记录未匹配的响应。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Updates
指定DNS服务器是否记录更新日志。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -UseSystemEventLog
指定DNS服务器是否使用系统事件日志进行记录。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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

### -WriteThrough
指定DNS服务器是否记录所有数据写入操作（即“写通”方式）。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerDiagnostics

## 相关链接

[Get-DnsServerDiagnostics](./Get-DnsServerDiagnostics.md)

