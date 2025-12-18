---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerPrimaryZone_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverprimaryzone?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerPrimaryZone
---

# Set-DnsServerPrimaryZone

## 摘要
修改DNS主区域的设置。

## 语法

### 参数（默认值）
```
Set-DnsServerPrimaryZone [-Name] <String> [-ComputerName <String>] [-PassThru]
 [-AllowedDcForNsRecordsAutoCreation <String[]>] [-DynamicUpdate <String>] [-Notify <String>]
 [-NotifyServers <IPAddress[]>] [-SecondaryServers <IPAddress[]>] [-SecureSecondaries <String>]
 [-IgnorePolicies <Boolean>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### FileZone
```
Set-DnsServerPrimaryZone [-Name] <String> [-ComputerName <String>] [-PassThru] -ZoneFile <String>
 [-VirtualizationInstance <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### ADZone
```
Set-DnsServerPrimaryZone [-Name] <String> [-ComputerName <String>] [-PassThru] -ReplicationScope <String>
 [-DirectoryPartitionName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsServerPrimaryZone` cmdlet 用于更改现有域名系统（DNS）主区域的设置。您可以修改与 Active Directory 集成区域或基于文件的区域相关的各种参数。

## 示例

### 示例 1：更改动态更新设置
```
PS C:\> Set-DnsServerPrimaryZone -Name "western.contoso.com" -DynamicUpdate "NonsecureAndSecure" -PassThru

ZoneName                            ZoneType        IsAutoCreated   IsDsIntegrated  IsReverseLookupZone  IsSigned
--------                            --------        -------------   --------------  -------------------  --------
western.contoso.com                 Primary         False           True            False                False
```

此命令将名为western.contoso.com的区域的动态更新设置更改为“NonsecureAndSecure”。示例中使用了*PassThru*参数来返回输出结果。

#### 示例 2：更改复制范围
```
PS C:\> Set-DnsServerPrimaryZone -Name "western.contoso.com" -ReplicationScope "Forest" -PassThru

ZoneName                            ZoneType        IsAutoCreated   IsDsIntegrated  IsReverseLookupZone  IsSigned
--------                            --------        -------------   --------------  -------------------  --------
western.contoso.com                 Primary         False           True            False                False
```

此命令用于更改名为 western.contoso.com 的区域的复制范围。示例中使用了 *PassThru* 参数来返回输出结果。

### 示例 3：更改区域文件（zone file）的名称
```
PS C:\> Set-DnsServerPrimaryZone -Name "western.contoso.com" -ZoneFile "tet23.dns" -PassThru

ZoneName                            ZoneType        IsAutoCreated   IsDsIntegrated  IsReverseLookupZone  IsSigned
--------                            --------        -------------   --------------  -------------------  --------
western.contoso.com                 Primary         False           False           False                False
```

这个命令用于更改名为western.contoso.com的区域的区域文件的文件名。示例中使用了*PassThru*参数来返回输出结果。

## 参数

### -AllowedDcForNsRecordsAutoCreation
指定那些将自身名称添加到该区域名称服务器（NS）资源记录中的域控制器的IP地址。

```yaml
Type: String[]
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 获得的会话对象）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
用于指定一个DNS服务器。如果您不指定此参数，命令将在本地系统上运行。您可以指定一个IP地址，或者任何能够解析为IP地址的字符串，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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
在运行该cmdlet之前，会提示您进行确认。

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
Parameter Sets: ADZone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DynamicUpdate
指定一个区域如何接受动态更新。可以接收动态更新的服务器能够处理客户端注册请求。此参数的可接受值为：

- None
- Secure
- NonsecureAndSecure

DNS update security is available only for Active Directory-integrated zones.

```yaml
Type: String
Parameter Sets: Parameters
Aliases:
Accepted values: None, Secure, NonsecureAndSecure

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IgnorePolicies
Indicates whether to ignore policies for this zone.

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
Specifies the name of a zone.

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

### -Notify
Specifies how a DNS master server notifies secondary servers of changes to resource records.
此参数的可接受值包括：

- NoNotify.
The zone does not send change notifications to secondary servers.
- Notify.
The zone sends change notifications to all secondary servers.
- NotifyServers.
The zone sends change notifications to some secondary servers.
If you choose this option, specify the list of secondary servers in the *NotifyServers* parameter.

```yaml
Type: String
Parameter Sets: Parameters
Aliases:
Accepted values: NoNotify, Notify, NotifyServers

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NotifyServers
Specifies an array of IP addresses of secondary DNS servers that the DNS master server notifies of changes to resource records.
You need this parameter only if you selected the value NotifyServers for the *Notify* parameter.

```yaml
Type: IPAddress[]
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
Returns an object representing the item with which you are working.
By default, this cmdlet does not generate any output.

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
Specifies a partition on which to store an Active Directory-integrated zone.
此参数的可接受值包括：

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

### -SecondaryServers
Specifies an array of IP addresses of DNS servers that are allowed to receive this zone through zone transfers.

```yaml
Type: IPAddress[]
Parameter Sets: Parameters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SecureSecondaries
指定DNS主服务器如何允许将区域数据传输到从属服务器。您可以配置DNS服务器，使其仅向特定的服务器发送区域数据传输请求；如果其他服务器尝试请求区域数据传输，DNS服务器将会拒绝这些请求。

此参数的可接受值包括：

- NoTransfer.
Zone transfers are not allowed on this DNS server for this zone.
- TransferAnyServer.
Zone transfers are allowed to any DNS server.
- TransferToZoneNameServer.
Zone transfers are allowed only to servers in the name servers (NS) records for this zone.
- TransferToSecureServers.
Zone transfers are allowed only for secondary servers.

```yaml
Type: String
Parameter Sets: Parameters
Aliases:
Accepted values: NoTransfer, TransferAnyServer, TransferToZoneNameServer, TransferToSecureServers

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -VirtualizationInstance
指定将要添加区域的虚拟化实例。虚拟化实例是DNS服务器中的逻辑分区，它能够独立托管多个区域及其相关范围。具有相同名称的区域和区域范围可以托管在不同的虚拟化实例中。此参数是可选的；如果未提供该参数，则系统会将区域添加到默认的虚拟化实例中，该默认实例在功能上等同于一个标准的DNS服务器。

```yaml
Type: String
Parameter Sets: FileZone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行时会发生什么情况。但实际上这个cmdlet并没有被运行。

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
指定区域文件的名称。此参数仅适用于基于文件的DNS系统。

```yaml
Type: String
Parameter Sets: FileZone
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerPrimaryZone

## 备注

## 相关链接

[Add-DnsServerPrimaryZone](./Add-DnsServerPrimaryZone.md)

[将 zone 转换为 DNS 服务器的主区域](./ConvertTo-DnsServerPrimaryZone.md)

[Restore-DnsServerPrimaryZone](./Restore-DnsServerPrimaryZone.md)

