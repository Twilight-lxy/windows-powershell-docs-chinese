---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerCache_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsservercache?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerCache
---

# Set-DnsServerCache

## 摘要
修改DNS服务器的缓存设置。

## 语法

```
Set-DnsServerCache [-StoreEmptyAuthenticationResponse <Boolean>] [-MaxKBSize <UInt32>]
 [-PollutionProtection <Boolean>] [-ComputerName <String>] [-LockingPercent <UInt32>]
 [-MaxNegativeTtl <TimeSpan>] [-MaxTtl <TimeSpan>] [-PassThru] [-IgnorePolicies <Boolean>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsServerCache` cmdlet 用于修改域名系统（DNS）服务器的缓存设置。

## 示例

#### 示例 1：在 DNS 服务器上设置最大缓存大小
```
PS C:\> Set-DnsServerCache -MaxKBSize 10240 -ComputerName "Win12S-05.DNSServer-01.Contoso.com"
```

此命令将DNS服务器（其FQDN为Win12S-05.DNSServer-01.Contoso.com）的最大缓存大小设置为10,240 KB。

### 示例 2：设置最大生存时间（Time-To-Live）
```
PS C:\> Set-DnsServerCache -MaxTTL 02.00:00:00 -MaxNegativeTtl 00.00:20:00
```

此命令将最大TTL值设置为2天，最大负TTL值设置为20分钟。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该 cmdlet。请输入计算机名称或会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
用于指定一个 DNS 服务器。该参数的可接受值包括：IPv4 地址、IPv6 地址，以及任何能够解析为 IP 地址的其他值（例如完全限定域名（FQDN）、主机名或 NETBIOS 名）。

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

### -IgnorePolicies
表示是否忽略与此缓存相关的策略。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LockingPercent
指定缓存可以使用的原始“生存时间”（Time to Live，TTL）值的一个百分比。

缓存锁定是通过一个百分比值来配置的。例如，如果将缓存锁定值设置为 50，则 DNS 服务器在 TTL 持续时间的一半期间内不会覆盖已缓存的条目。默认情况下，缓存锁定的百分比为 100，这意味着 DNS 服务器在整个 TTL 持续时间内都不会覆盖已缓存的条目。

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

### -MaxKBSize
指定DNS服务器内存缓存的最大大小（以千字节为单位）。

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

### -MaxNegativeTtl
该参数用于指定记录对查询的否定响应的条目在DNS缓存中存储的时间长度（范围为1至2592000秒）。值必须以`TimeSpan`形式提供，默认设置为15分钟。

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

### -MaxTtl
该参数用于指定记录在缓存中保存的时间长度（范围为 0 到 2592000 秒）。值必须以 `TimeSpan` 的形式提供。如果将 `TimeSpan` 设置为 0 秒，DNS 服务器将不会缓存任何记录。默认设置为一天（86,400 秒）。

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

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -PollutionProtection
用于指定DNS过滤器是否缓存名称服务（NS）资源记录。有效值为：  
- `0`：缓存所有对名称查询的响应，这是默认值；  
- `1`：仅缓存属于同一DNS子树的记录。

当你将此参数值设置为 `False` 时，缓存污染保护功能将被禁用。DNS服务器会缓存其所在区域内的所有主机（A）记录以及被查询的NS资源。在这种情况下，DNS服务器也可能缓存未经授权的DNS服务器的NS记录。这会导致名称解析失败，或者导致后续对该域名的查询无法正常进行。

当你将此参数的值设置为 `True` 时，DNS 服务器会启用缓存污染防护功能，并忽略 `Host (A)` 记录。如果名称服务器（NS）位于 DNS 服务器所在区域的之外，DNS 服务器会执行一次缓存更新查询来解析该 NS 的地址。这种额外的查询对 DNS 服务器的性能影响很小。

有关DNS缓存锁定的更多信息，请参阅[DNS缓存锁定](https://technet.microsoft.com/en-us/library/ee683892.aspx)。有关缓存污染防护的更多信息，请参阅[保护DNS服务器服务](https://technet.microsoft.com/en-us/library/cc731367)。有关NS资源记录的更多信息，请参阅[管理资源记录](https://technet.microsoft.com/en-us/library/cc783389.aspx)。

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

### -StoreEmptyAuthenticationResponse
指定DNS服务器是否会在缓存中存储空的权威响应（RFC-2308）。默认值为True。

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

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果运行该cmdlet会发生什么情况。不过实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerCache

## 备注

## 相关链接

[RFC 2308](http://www.rfc-editor.org/rfc/rfc2308.txt)

[Clear-DnsServerCache](./Clear-DnsServerCache.md)

[Get-DnsServerCache](./Get-DnsServerCache.md)

[显示DNS服务器缓存](./Show-DnsServerCache.md)

