---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerStubZone_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverstubzone?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerStubZone
---

# Set-DnsServerStubZone

## 摘要
修改DNS服务器存根区域的设置。

## 语法

### 参数（默认值）
```
Set-DnsServerStubZone [-Name] <String> [-ComputerName <String>] [-PassThru] [-MasterServers <IPAddress[]>]
 [-LocalMasters <IPAddress[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### ADZone
```
Set-DnsServerStubZone [-Name] <String> [-ComputerName <String>] [-PassThru] [-DirectoryPartitionName <String>]
 -ReplicationScope <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-DnsServerStubZone` cmdlet 用于更改现有存根区域（stub zone）的设置。存根区域是域名系统（DNS）区域的副本，其中仅包含用于标识该区域权威 DNS 服务器的资源记录。

存根区域（stub zone）可以是一个正向查找区域（forward lookup zone），也可以是一个反向查找区域（reverse lookup zone）。它既可以是一个与 Active Directory 集成的区域（Active Directory-integrated zone），也可以是一个基于文件的区域（file-backed zone）。

## 示例

### 示例 1：更改存根区域（stub zone）的主服务器
```
PS C:\> Set-DnsServerStubZone -Name "west03.contoso.com" -MasterServers 172.23.90.124,2001:4898:7020:f100:458f:e6a2:fcaf:698c
```

此命令用于更改名为 west03.contoso.com 的存根区域的 Master 服务器。

### 示例 2：更改存根区域的复制范围
```
PS C:\> Set-DnsServerStubZone  -Name "west04.contoso.com" -ReplicationScope "Domain" -PassThru

ZoneName                            ZoneType        IsAutoCreated   IsDsIntegrated  IsReverseLookupZone  IsSigned
--------                            --------        -------------   --------------  -------------------  --------
west04.contoso.com                  Stub            False           True            False
```

此命令将名为 west04.contoso.com 的存根区域的复制范围更改为该域中的所有 DNS 服务器。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，随后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -ComputerName
用于指定一个DNS服务器。如果您不指定此参数，该命令将在本地系统上运行。您可以指定一个IP地址，或者任何能够解析为IP地址的数值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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
在运行cmdlet之前会提示您进行确认。

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

### -DirectoryPartitionName
指定用于存储区域（zone）的目录分区。当 *ReplicationScope* 参数的值为 “Custom” 时，请使用此参数。

```yaml
Type: String
Parameter Sets: ADZone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LocalMasters
指定一个区域的主DNS服务器的IP地址列表，该列表仅由当前DNS服务器在本地使用。如果未配置此参数，则会使用“MasterServers”值；否则，将使用这个IP地址列表来替代“Master Servers”值。当区域类型不是“stub”类型时，此参数将被忽略。

```yaml
Type: IPAddress[]
Parameter Sets: Parameter
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MasterServers
用于指定一个区域的主要DNS服务器的IP地址列表。对于任何需要主要DNS服务器的区域（无论是辅助类型、存根类型还是转发器类型），该值都必须是非空的。

```yaml
Type: IPAddress[]
Parameter Sets: Parameter
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定一个区域的名称。该 cmdlet 会修改此区域的设置。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ZoneName

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -ReplicationScope
指定用于存储与 Active Directory 集成的区域的分区。该参数的可接受值为：

- Custom.
Any custom directory partition that a user creates.
Specify a custom directory partition by using the *DirectoryPartitionName* parameter.
- Domain.
The domain directory partition.
- Forest.
The ForestDnsZone directory partition.
- Legacy.
A legacy directory partition.

```yaml
Type: String
Parameter Sets: ADZone
Aliases:
Accepted values: Forest, Domain, Legacy, Custom

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的命令行操作（cmdlet）的最大数量。如果省略了此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算一个最优的限制值。这个限制仅适用于当前执行的 cmdlet，而不影响整个会话或整个计算机。

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
展示了如果该cmdlet运行会发生什么情况。但实际上这个cmdlet并没有被运行。

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

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerStubZone

## 备注

## 相关链接

[Add-DnsServerStubZone](./Add-DnsServerStubZone.md)

