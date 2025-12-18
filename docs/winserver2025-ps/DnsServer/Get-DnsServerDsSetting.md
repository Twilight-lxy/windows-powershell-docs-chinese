---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerDsSetting_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/get-dnsserverdssetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsServerDsSetting
---

# Get-DnsServerDsSetting

## 摘要
检索DNS服务器在Active Directory中的配置信息

## 语法

```
Get-DnsServerDsSetting [-ComputerName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-DnsServerDsSetting` cmdlet 可以检索以下域名系统（DNS）服务器的 Active Directory 设置：`PollingInterval`、`DirectoryPartitionAutoEnlistInterval`、`LazyUpdateInterval`、`MinimumBackgroundLoadThreads` 和 `RemoteReplicationDelay`。

## 示例

### 示例 1：获取 Active Directory 服务设置
```
PS C:\> Get-DnsServerDsSetting

PollingInterval(s)                   : 180
TombstoneInterval                    : 14.00:00:00
DirectoryPartitionAutoEnlistInterval : 1.00:00:00
LazyUpdateInterval(s)                : 3
MinimumBackgroundLoadThreads         : 1
RemoteReplicationDelay(s)            : 30
```

此命令用于获取DNS服务器的Active Directory服务设置信息。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的任务。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
指定一个DNS服务器。该参数的可接受值包括：IP V4地址；IP V6地址；以及任何可以解析为IP地址的其他值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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
该参数用于指定可以同时运行的命令（cmdlet）的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该命令的最佳限制值。这个限制仅适用于当前执行的命令，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerDsSetting

## 备注

## 相关链接

[Set-DnsServerDsSetting](./Set-DnsServerDsSetting.md)

