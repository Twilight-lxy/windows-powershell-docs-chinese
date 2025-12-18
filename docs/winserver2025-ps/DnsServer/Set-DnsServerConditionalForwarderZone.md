---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerConditionalForwarder_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverconditionalforwarderzone?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerConditionalForwarderZone
---

# Set-DnsServerConditionalForwarderZone

## 摘要
修改DNS条件转发器的设置。

## 语法

### 参数（默认值）
```
Set-DnsServerConditionalForwarderZone [-Name] <String> [-ComputerName <String>] [-PassThru]
 [[-UseRecursion] <Boolean>] [[-MasterServers] <IPAddress[]>] [[-ForwarderTimeout] <UInt32>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ADZone
```
Set-DnsServerConditionalForwarderZone [-Name] <String> [-ComputerName <String>] [-PassThru]
 [-DirectoryPartitionName <String>] -ReplicationScope <String> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsServerConditionalForwarderZone` cmdlet 用于更改域名系统（DNS）服务器上现有条件转发器的设置。您可以修改条件转发器区域的主服务器、转发器超时时间、递归设置、递归范围以及目录分区名称等参数。

## 示例

### 示例 1：更改某个区域的转发器超时设置
```
PS C:\> Set-DnsServerConditionalForwarderZone -Name "contoso.com" -ForwarderTimeout 15
```

该命令用于更改名为 contoso.com 的转发器区域的转发器超时设置。

### 示例 2：更改某个区域的复制范围
```
PS C:\> Set-DnsServerConditionalForwarderZone -Name "contoso.com" -ReplicationScope "Domain" -PassThru
```

这个命令将 contoso.com 的复制范围更改为 “Domain”（即整个域），这意味着该域中的所有 DNS 服务器都会受到影响。在这个示例中，使用了 *PassThru* 参数来生成输出结果。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets系列命令；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

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
指定用于托管转发器的 DNS 服务器。如果未指定此参数，命令将在本地系统上运行。您可以指定一个 IP 地址，或者任何能够解析为 IP 地址的值，例如完全限定域名（FQDN）、主机名或 NETBIOS 名称。

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
在运行cmdlet之前，会提示您进行确认。

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
指定用于存储转发器的目录分区。条件转发器在内部是以“区域”（zones）的形式进行存储的。当*ReplicationScope*参数的值为“Custom”时，请使用此参数。

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

### -ForwarderTimeout
指定DNS服务器等待转发器解析查询的时间长度（以秒为单位）。在尝试了所有转发器后，DNS服务器可以自行尝试解析该查询。最小值为0，最大值为15。

```yaml
Type: UInt32
Parameter Sets: Parameters
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MasterServers
指定该区域的主服务器的IP地址数组。条件转发器也是以区域的形式存储的。您可以使用IPv4和IPv6地址。请至少指定一个主服务器。

```yaml
Type: IPAddress[]
Parameter Sets: Parameters
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定已配置条件转发功能的区域的名称。

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
指定条件转发器的复制范围。条件转发器在内部是以区域（zones）的形式存储的。该参数的可接受值包括：

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
该参数用于指定当转发器无法解析查询时，DNS服务器是否仍会尝试进行解析。如果设置为 `$False`，则DNS服务器将不会使用其他DNS服务器来进行解析。此设置会覆盖DNS服务器的“Use Recursion”（启用递归）配置。

```yaml
Type: Boolean
Parameter Sets: Parameters
Aliases:

Required: False
Position: 4
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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerConditionalForwarderZone

## 备注

## 相关链接

[Add-DnsServerConditionalForwarderZone](./Add-DnsServerConditionalForwarderZone.md)

