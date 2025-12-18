---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerDiagnostics_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/get-dnsserverdiagnostics?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsServerDiagnostics
---

# Get-DnsServerDiagnostics

## 摘要
检索DNS事件日志记录的详细信息。

## 语法

```
Get-DnsServerDiagnostics [-ComputerName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsServerDiagnostics` cmdlet 可用于检索域名系统（DNS）服务器的诊断信息及日志记录相关参数。

## 示例

### 示例 1：获取 DNS 事件日志记录详细信息
```
PS C:\> Get-DnsServerDiagnostics

SaveLogsToPersistentStorage          : False
Queries                              : False
Answers                              : False
Notifications                        : False
Update                               : False
QuestionTransactions                 : False
UnmatchedResponse                    : False
SendPackets                          : False
ReceivePackets                       : False
TcpPackets                           : False
UdpPackets                           : False
FullPackets                          : False
FilterIPAddressList                  :
EventLogLevel                        : 4
UseSystemEventLog                    : False
EnableLoggingToFile                  : True
EnableLogFileRollover                : False
LogFilePath                          :
MaxMBFileSize                        : 500000000
WriteThrough                         : False
EnableLoggingForLocalLookupEvent     : False
EnableLoggingForPluginDllEvent       : False
EnableLoggingForRecursiveLookupEvent : False
EnableLoggingForRemoteServerEvent    : False
EnableLoggingForServerStartStopEvent : False
EnableLoggingForTombstoneEvent       : False
EnableLoggingForZoneDataWriteEvent   : False
EnableLoggingForZoneLoadingEvent     : False
```

这个命令可以获取本地DNS服务器的DNS事件日志记录详情。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
用于指定一个DNS服务器。该参数的可接受值包括：IPv4地址；IPv6地址；以及任何能够解析为IP地址的其他值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算一个最优的节流限制（即同时允许运行的操作数量）。这个节流限制仅适用于当前的 cmdlet，而不适用于整个会话或整个计算机。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerDiagnostics

## 备注

## 相关链接

[Set-DnsServerDiagnostics](./Set-DnsServerDiagnostics.md)

