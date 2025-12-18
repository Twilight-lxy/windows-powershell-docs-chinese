---
description: 使用此主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServer_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/test-dnsserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-DnsServer
---

# 测试DNS服务器

## 摘要
测试指定的计算机是否能够正常运行作为DNS服务器的功能。

## 语法

### 上下文（默认值）
```yaml
Test-DnsServer [-IPAddress] <IPAddress[]> [-ComputerName <String>] [[-Context] <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ZoneMaster
```yaml
Test-DnsServer [-IPAddress] <IPAddress[]> [-ComputerName <String>] -ZoneName <String>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Test-DnsServer` cmdlet用于检测一台计算机是否能够正常运行作为域名系统（DNS）服务器。该DNS服务器必须安装Windows Server® 2008 R2或更高版本的操作系统。

当您仅通过计算机的 IP 地址来指定该计算机时，此 cmdlet 会测试该计算机是否为 DNS 服务器。如果您同时指定了一个区域名称，该 cmdlet 还会验证该 DNS 服务器是否能够解析指定的区域。

## 示例

### 示例 1：测试 DNS 服务器是否正常工作
```Powershell
PS C:\> Test-DnsServer -IPAddress 10.123.183.155

IPAddress               Result                  RoundTripTime           TcpTried                UdpTried
---------               --------                 ------------           --------                --------
10.123.183.155           Success                 00:00:11                False                  True
```

这个命令用于测试IP地址为10.123.183.155的计算机是否是一台功能正常的DNS服务器。

### 示例 2：测试 DNS 服务器是否正常工作，并且其配置的前向转发器是否有效
```Powershell
PS C:\> Test-DnsServer -IPAddress 10.123.183.155 -Context Forwarder

IPAddress               Result                  RoundTripTime           TcpTried                UdpTried
---------               --------                 ------------           --------                --------
10.123.183.155           Success                 00:00:11                False                    True
```

这个命令用于测试IP地址为10.123.183.155的计算机是否是一个功能正常的DNS服务器，并且该服务器是否配置了有效的转发器。

### 示例 3：测试 DNS 服务器是否正常运行，并且其配置的根提示（root hints）是否有效
```Powershell
PS C:\> Test-DnsServer -IPAddress 10.123.183.155 -Context RootHints

IPAddress               Result                  RoundTripTime           TcpTried                UdpTried
---------               --------                 ------------           --------                --------
10.123.183.155           NoResponse              00:00:12                False                   True
```

这个命令用于测试IP地址为10.123.183.155的计算机是否是一个功能正常的DNS服务器，并且该服务器配置了有效的根提示（root hints）。

### 示例 4：测试 DNS 服务器是否正常工作以及是否托管了 Contoso.com 域名
```
PS C:\> Test-DnsServer -IPAddress 10.123.183.155 -ZoneName "Contoso.com"

IPAddress               Result                  RoundTripTime           TcpTried                UdpTried
---------               --------                 ------------           --------                --------
10.123.183.155           Success                 00:00:00                False                   True
```

这个命令用于测试IP地址为10.123.183.155的计算机是否是一个能够正常运行DNS服务器，并且该服务器是否托管着Contoso.com域名区域。

## 参数

### -AsJob
将该cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（about_Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Context
指定要测试的功能。有效值包括：DnsServer、Forwarder 和 RootHints。

```yaml
Type: String
Parameter Sets: Context
Aliases:
Accepted values: DnsServer, Forwarder, RootHints

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPAddress
指定一个DNS服务器IP地址数组。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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

### -ZoneName
指定服务器所托管的区域名称。

```yaml
Type: String
Parameter Sets: ZoneMaster
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerValidity[]

## 备注

## 相关链接

[Get-DnsServer](./Get-DnsServer.md)

[Set-DnsServer](./Set-DnsServer.md)

