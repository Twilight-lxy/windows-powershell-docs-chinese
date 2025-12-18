---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerStubZone_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserverstubzone?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerStubZone
---

# Add-DnsServerStubZone

## 摘要
添加一个DNS存根区域（stub zone）。

## 语法

### FileForwardLookupZone（默认值）
```
Add-DnsServerStubZone [-LoadExisting] [-MasterServers] <IPAddress[]> [-ComputerName <String>] [-PassThru]
 [-Name] <String> [-ZoneFile <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### FileReverseLookupZone
```
Add-DnsServerStubZone [-LoadExisting] [-MasterServers] <IPAddress[]> [-ComputerName <String>] [-PassThru]
 -NetworkId <String> [-ZoneFile <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ADReverseLookupZone
```
Add-DnsServerStubZone [-LoadExisting] [-MasterServers] <IPAddress[]> [-ComputerName <String>] [-PassThru]
 [-ReplicationScope] <String> [[-DirectoryPartitionName] <String>] -NetworkId <String>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ADForward LookupZone
```
Add-DnsServerStubZone [-LoadExisting] [-MasterServers] <IPAddress[]> [-ComputerName <String>] [-PassThru]
 [-ReplicationScope] <String> [-Name] <String> [[-DirectoryPartitionName] <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DnsServerStubZone` cmdlet 用于添加一个存根区域（stub zone）。存根区域是域名系统（DNS）区域的副本，其中仅包含用于标识该区域对应的 DNS 服务器的资源记录。

你可以添加正向查找区域（forward lookup zone）或反向查找区域（reverse lookup zone）。同时，你也可以选择添加与 Active Directory 集成的区域（Active Directory-integrated zone）或基于文件的区域（file-backed zone）。

## 示例

#### 示例 1：添加一个基于文件的存根区域（stub zone）
```
PS C:\> Add-DnsServerStubZone -Name "west02.contoso.com" -MasterServers "172.23.90.124" -PassThru -ZoneFile "west02_contoso.dns"
```

此命令将 west02.contoso.com 添加为一个基于文件的存根区域（stub zone）。该命令指定了一个主服务器，并使用 *PassThru* 参数来生成输出结果。

#### 示例 2：添加一个与 Active Directory 集成的存根区域（stub zone）
```
PS C:\> Add-DnsServerStubZone -Name "west03.contoso.com" -MasterServers 172.23.90.124 -PassThru -ReplicationScope "Forest"
```

此命令将 west03.contoso.com 添加为一个存根区域（stub zone），并复制到森林中的所有 DNS 服务器上。

### 示例 3：添加一个与 Active Directory 集成的反向查找区域
```
PS C:\> Add-DnsServerStubZone -NetworkId 10.1.2.0/24 -MasterServers 172.23.90.124 -PassThru -ReplicationScope Forest
```

此命令为网络 2.1.10.in-addr.arpa 添加了一个存根区域（stub zone），该区域会被复制到森林中的所有 DNS 服务器上。

## 参数

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中操作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该 cmdlet。请输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
用于指定一个 DNS 服务器。如果您不指定此参数，命令将在本地系统上运行。您可以指定一个 IP 地址，或者任何能够解析为 IP 地址的值，例如完全合格的域名（FQDN）、主机名或 NETBIOS 名称。

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
在运行该cmdlet之前，会提示您确认是否要继续执行操作。

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
指定用于存储区域（zone）的目录分区。当*ReplicationScope*参数的值为“Custom”时，请使用此参数。

```yaml
Type: String
Parameter Sets: ADReverseLookupZone, ADForwardLookupZone
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LoadExisting
表示服务器会加载该区域对应的现有文件；否则，此命令行工具（cmdlet）会自动创建默认的区域记录。此参数仅适用于基于文件的区域（file-backed zones）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MasterServers
指定该区域主服务器的IP地址数组。你可以同时使用IPv4和IPv6地址。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定一个区域（zone）的名称。

```yaml
Type: String
Parameter Sets: FileForwardLookupZone, ADForwardLookupZone
Aliases: ZoneName

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetworkId
指定反向查找区域的网络ID和前缀长度。对于IPv4，使用格式A.B.C.D/prefix；对于IPv6，使用格式1111:2222:3333:4444::/prefix。

对于 IPv4，该cmdlet仅能创建A类、B类、C类或D类的反向查找区域。如果您指定的前缀位于两个类别之间，cmdlet会使用能够被8整除的较长前缀。例如，当输入前缀“10.2.10.0/23”时，系统会创建“10.2.10.0/24”反向查找区域，而不会创建“10.2.11.0/24”反向查找区域。如果您输入的长度超过“/24”的IPv4前缀，cmdlet会创建一个“/32”类型的反向查找区域。

对于 IPv6，该 cmdlet 会为前缀范围从 /16 到 /128（且这些前缀能被 4 整除）创建 ip6.arpa 区域。如果您指定了一个位于该范围内的前缀，cmdlet 会使用其中长度较长、且能被 4 整除的前缀。例如，输入值 AAAA::/58 时，系统会创建 AAAA::/60 这个 ip6.arpa 区域；如果您没有指定前缀，cmdlet 会使用默认的前缀值 /128。

```yaml
Type: String
Parameter Sets: FileReverseLookupZone, ADReverseLookupZone
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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
Parameter Sets: ADReverseLookupZone, ADForwardLookupZone
Aliases:
Accepted values: Forest, Domain, Legacy, Custom

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -ZoneFile
指定区域文件的名称。此参数仅适用于基于文件的DNS（File-Based DNS）配置。

```yaml
Type: String
Parameter Sets: FileForwardLookupZone, FileReverseLookupZone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerStubZone

## 备注

## 相关链接

[Set-DnsServerStubZone](./Set-DnsServerStubZone.md)

