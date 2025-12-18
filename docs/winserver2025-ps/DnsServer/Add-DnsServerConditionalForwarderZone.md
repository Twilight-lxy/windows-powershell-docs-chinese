---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerConditionalForwarder_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserverconditionalforwarderzone?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerConditionalForwarderZone
---

# Add-DnsServerConditionalForwarderZone

## 摘要
向DNS服务器添加一个条件转发器。

## 语法

### FileForward LookupZone（默认值）
```
Add-DnsServerConditionalForwarderZone [-LoadExisting] [-MasterServers] <IPAddress[]> [-ComputerName <String>]
 [-UseRecursion] [[-ForwarderTimeout] <UInt32>] [-PassThru] [-Name] <String> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ADForward LookupZone
```
Add-DnsServerConditionalForwarderZone [-LoadExisting] [-MasterServers] <IPAddress[]> [-ComputerName <String>]
 [-UseRecursion] [[-ForwarderTimeout] <UInt32>] [-PassThru] [-DirectoryPartitionName <String>]
 [-ReplicationScope <String>] [-Name] <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DnsServerConditionalForwarderZone` cmdlet 用于在域名系统（DNS）服务器上添加条件转发器。您可以指定该条件转发器的主服务器、转发超时设置、递归处理方式、主机计算机、复制范围以及目录分区等信息。条件转发器以 zone 的形式存储在 DNS 服务器上。

## 示例

#### 示例 1：创建一个未与 Active Directory 集成的转发器
```
PS C:\> Add-DnsServerConditionalForwarderZone -Name "contoso.com" -MasterServers 2001:4898:7020:f100:458f:e6a2:fcaf:698c,172.23.90.124 -PassThru

ZoneName                            ZoneType        IsAutoCreated   IsDsIntegrated  IsReverseLookupZone  IsSigned
--------                            --------        -------------   --------------  -------------------  --------
contoso.com                         Forwarder       False           False           False
```

这个命令创建了一个名为“contoso.com”的条件转发器区域（conditional forwarder zone）。相关配置信息被存储在注册表中。该命令包含一个或多个主DNS服务器的IP地址，并使用了*PassThru*参数。

### 示例 2：创建一个与 Active Directory 集成的转发器
```
PS C:\> Add-DnsServerConditionalForwarderZone -Name "contoso.com" -ReplicationScope "Forest" -MasterServers 2001:4898:7020:f100:458f:e6a2:fcaf:698c,172.23.90.124
```

此命令为 contoso.com 创建一个与 Active Directory 集成的条件转发器区域。该命令指定了一个或多个主 DNS 服务器的 IP 地址。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中执行其他操作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
用于指定 DNS 服务器。此 cmdlet 会将转发器配置到该服务器上。如果未指定此参数，命令将在本地系统上执行。您可以指定一个 IP 地址，或者任何能够解析为 IP 地址的值，例如完全 qualified domain name (FQDN)、主机名或 NETBIOS 名称。

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
指定用于存储转发器的目录分区。条件转发器在内部是以“区域（zones）”的形式进行存储的。当*ReplicationScope*参数的值为“Custom”时，请使用此参数。

```yaml
Type: String
Parameter Sets: ADForwardLookupZone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ForwarderTimeout
指定 DNS 服务器等待主服务器解析查询所需的时间长度（以秒为单位）。如果某个服务器未能解析请求，系统会继续查询列表中的下一个服务器，直到所有主服务器都被查询过为止。在此时间过后，DNS 服务器可以尝试自行解析该查询。此参数仅适用于转发器区域（forwarder zone）。最小值为 0，最大值为 15。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LoadExisting
表示服务器从注册表中为转发器加载现有的数据。条件转发器在内部是以区域（zones）的形式存储的。此参数不适用于与 Active Directory 集成的区域。

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
指定该区域的主服务器的IP地址数组。针对被转发区域的DNS查询会发送到这些主服务器。你可以使用IPv4和IPv6地址。你必须至少指定一个主服务器。

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
指定一个区域的名称。该cmdlet会为该区域添加一个条件转发器（conditional forwarder）。

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
指定条件转发器的复制范围。条件转发器在内部是作为区域（zones）存储的。该参数的可接受值包括：

- Custom.
Replicate the conditional forwarder to all DNS servers running on domain controllers enlisted in a custom directory partition.
- Domain.
Replicate the conditional forwarder to all DNS servers that run on domain controllers in the domain.
- Forest.
Replicate the conditional forwarder to all DNS servers that run on domain controllers in the forest.
- Legacy.
Replicate the conditional forwarder to all domain controllers in the domain.

```yaml
Type: String
Parameter Sets: ADForwardLookupZone
Aliases:
Accepted values: Forest, Domain, Legacy, Custom

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该命令的最佳限制值。这个限制仅适用于当前正在运行的命令，而不适用于整个会话或整个计算机。

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

### -UseRecursion
该参数用于指定：当转发器无法解析某个DNS查询时，DNS服务器是否仍会尝试进行解析。如果值为 `$False`，则DNS服务器将不会使用其他DNS服务器来继续解析该查询。此参数会覆盖DNS服务器的“Use Recursion”设置。

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

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerConditionalForwarderZone

## 备注

## 相关链接

[Set-DnsServerConditionalForwarderZone](./Set-DnsServerConditionalForwarderZone.md)

