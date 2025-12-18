---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerGlobalNameZone_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverglobalnamezone?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerGlobalNameZone
---

# Set-DnsServerGlobalNameZone

## 摘要
更改 GlobalNames 区域的配置设置。

## 语法

```
Set-DnsServerGlobalNameZone [-AlwaysQueryServer <Boolean>] [-BlockUpdates <Boolean>] [-Enable <Boolean>]
 [-EnableEDnsProbes <Boolean>] [-GlobalOverLocal <Boolean>] [-PreferAaaa <Boolean>] [-ComputerName <String>]
 [-SendTimeout <UInt32>] [-ServerQueryInterval <TimeSpan>] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsServerGlobalNameZone` cmdlet 可以启用或禁用单标签域名系统（DNS）查询功能，同时还可以更改 GlobalNames 区的配置设置。

GlobalNames 区域支持使用简短且易于记忆的名称，而无需使用完整的域名（FQDN）以及 Windows Internet Name Service (WINS) 技术。例如，DNS 可以查询 “SarahJonesDesktop”，而不需要查询 “SarahJonesDesktop.contoso.com”。

## 示例

### 示例 1：启用一个 GlobalNames 区域
```
PS C:\> Set-DnsServerGlobalNameZone -Enable $True -PassThru
```

此命令在当前服务器上启用一个名为“GlobalNames”的区域。

## 参数

### -AlwaysQueryServer
该参数用于指定DNS服务器是否尝试使用缓存值来更新DNS服务器列表。如果DNS服务器托管了GlobalNames区域，则此参数无效。

如果该值为 `$True`，DNS服务器会向远程DNS服务器请求更新列表，以便包含当前托管GlobalNames区域的远程DNS服务器信息。

如果值为 $False，则 DNS 服务器会尝试使用缓存的本地服务记录来获取 GlobalNames 区的更新信息。

默认值是 $False。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的任务。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` 类型的 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -BlockUpdates
该参数用于指定DNS服务器是否会阻止对权威区域（authoritative zones）中FQDN的更新，如果这些FQDN的标签与GlobalNames区域中的标签发生冲突。如果值为$True，则DNS服务器会在检测到冲突时阻止相应的更新；如果值为$False，则服务器不会进行此类检查。默认值为$True。

为了检查是否存在冲突，DNS服务器会删除区域名称（最右边的标签），然后在本地托管的GlobalNames区域中进行一次不区分大小写的搜索。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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
用于指定一个 DNS 服务器。如果您不指定此参数，命令将在本地系统上运行。您可以指定一个 IP 地址，或者任何能够解析为 IP 地址的字符串，例如完全限定域名（FQDN）、主机名或 NETBIOS 名称。

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

### -Enable
指定是否使用 GlobalNames 区域来解析单标签名称。$True 表示启用 GlobalNames 的使用；$False 表示禁用 GlobalNames 的使用。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableEDnsProbes
指定DNS服务器是否尊重远程GlobalNames区域的“EnableEDnsProbes”设置。DNS服务器可以允许或拒绝与扩展DNS（EDNS）信息相关的查询请求。

如果该值为 `$True`，则服务器会在远程全局名称（GlobalNames）区域允许的情况下尝试进行 DNS 查询。

如果该值为 `$False`，DNS服务器将不会尝试对远程的 GlobalNames 区域执行 ENDS 查询。

默认值是 $False。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -GlobalOverLocal
该参数用于指定DNS服务器是否首先尝试通过查询其具有权威性的区域来解析名称。如果值为 `$True`，则DNS服务器会先在本地进行查询，然后再查询 `GlobalNames` 区域；如果值为 `$False`，则服务器会先查询 `GlobalNames` 区域，之后再进行全局查询。默认值为 `$False`。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
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

### -PreferAaaa
该选项用于指定DNS服务器在查询托管有GlobalNames区域的远程DNS服务器时，是更倾向于使用IPv6（AAAA）地址记录还是IPv4（A）地址记录。

如果这个值为 `$True`，则 DNS 服务器会使用 IPv6 地址，除非没有可用的 IPv6 地址。

如果这个值为 `$False`，DNS服务器将使用 IPv4 地址，除非没有可用的 IPv4 地址。

默认值是 $False。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SendTimeout
指定DNS服务器在查询远程GlobalNames区域时等待响应的秒数。

最小值为1，最大值为15。

默认值为 3。DNS 服务器将值 0 解释为默认值 3。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ServerQueryInterval
指定一个时间间隔（以时间跨度对象的形式），用于在两次查询之间更新托管 GlobalNames 区的远程 DNS 服务器集合。

最小值为60秒，最大值为30天。

默认值是六小时。DNS服务器将数值0解读为默认值，即六小时。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerGlobalNameZone

## 备注

## 相关链接

