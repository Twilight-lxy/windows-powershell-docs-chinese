---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerSecondaryZone_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserversecondaryzone?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerSecondaryZone
---

# Add-DnsServerSecondaryZone

## 摘要
添加一个DNS服务器的辅助区域（secondary zone）。

## 语法

### ForwardLookupZone（默认值）
```
Add-DnsServerSecondaryZone [-LoadExisting] [-MasterServers] <IPAddress[]> [-ComputerName <String>] [-PassThru]
 [-Name] <String> [-ZoneFile] <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### ReverseLookupZone
```
Add-DnsServerSecondaryZone [-LoadExisting] [-MasterServers] <IPAddress[]> [-ComputerName <String>] [-PassThru]
 [-ZoneFile] <String> -NetworkId <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DnsServerSecondaryZone` cmdlet 可用于在域名系统（DNS）服务器上添加指定的辅助区域。您可以创建正向查找区域或反向查找区域。要创建反向查找区域，可以使用 `NetworkID` 参数指定网络 ID，或者使用 `Name` 参数指定完整的反向查找区域名称。

## 示例

### 示例 1：添加一个辅助 DNS 服务器区域
```
PS C:\> Add-DnsServerSecondaryZone -Name "western.contoso.com" -ZoneFile "western.contoso.com.dns" -MasterServers 172.23.90.124
```

这个命令创建了一个名为 western.contoso.com 的辅助 DNS 区域，并指定了主服务器。该区域采用文件备份机制进行数据存储。

### 示例 2：创建辅助区域
```
PS C:\> Get-DnsServerZone -ComputerName win-olpn33s5q3m.mytest.contoso.com | where {("Primary" -eq $_.ZoneType) -and ($False -eq $_.IsAutoCreated) -and ("TrustAnchors" -ne $_.ZoneName)} | %{ $_ | Add-DnsServerSecondaryZone -MasterServers 172.23.90.136 -ZoneFile "$($_.ZoneName).dns"}
```

这个示例从服务器 win-olpn33s5q3m.mytest.contoso.com 获取主区域，并在本地系统上创建辅助区域（除了 TrustAnchors 和 AutoCreated 类型的区域）。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
用于指定一个 DNS 服务器。如果不指定此参数，命令将在本地系统上运行。您可以指定一个 IP 地址，或者任何能够解析为 IP 地址的字符串，例如完全限定域名（FQDN）、主机名或 NETBIOS 名称。

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

### -LoadExisting
表示服务器会加载该区域的现有文件。如果您不指定此参数，此cmdlet会自动创建默认的区域记录。此参数仅适用于基于文件的区域。

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
指定该区域的主服务器 IP 地址数组。您可以同时使用 IPv4 和 IPv6。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定一个区域的名称。

```yaml
Type: String
Parameter Sets: ForwardLookupZone
Aliases: ZoneName

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetworkId
用于指定反向查找区域的网络ID和前缀长度。对于IPv4地址，使用格式A.B.C.D/prefix；对于IPv6地址，使用格式1111:2222:3333:4444::/prefix。

对于 IPv4，该命令仅能创建 A 类、B 类、C 类或 D 类的反向查找区域。如果您指定的前缀位于两个类别之间，命令会使用能够被 8 整除的较长前缀。例如，当输入前缀 “10.2.10.0/23” 时，系统会创建 “10.2.10.0/24” 反向查找区域，而不会创建 “10.2.11.0/24” 反向查找区域。如果您输入的长度超过 /24 的 IPv4 前缀，命令将创建一个 /32 类型的反向查找区域。

对于 IPv6，该 cmdlet 会为前缀范围在 /16 到 /128 之间且能被 4 整除的地址创建 ip6.arpa 区域。如果您指定的前缀位于这两个范围之外，cmdlet 会使用长度更长但仍然能被 4 整除的前缀。例如，输入 AAAA::/58 时，会创建 AAAA::/60 这个 ip6.arpa 区域；如果没有指定前缀，cmdlet 会使用默认的前缀值 /128。

```yaml
Type: String
Parameter Sets: ReverseLookupZone
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

### -ThrottleLimit
该参数用于指定可以同时执行的并发操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
指定区域文件的名称。此参数仅适用于基于文件的DNS系统。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerSecondaryZone

## 备注

## 相关链接

[将 zone 转换为 DNS 服务器的辅助区域](./ConvertTo-DnsServerSecondaryZone.md)

[Restore-DnsServerSecondaryZone](./Restore-DnsServerSecondaryZone.md)

[Set-DnsServerSecondaryZone](./Set-DnsServerSecondaryZone.md)

