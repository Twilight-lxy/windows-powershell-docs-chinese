---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerResourceRecord_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/remove-dnsserverresourcerecord?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DnsServerResourceRecord
---

# 删除DNS服务器资源记录

## 摘要
从某个区域中删除指定的DNS服务器资源记录。

## 语法

### InputObject（默认值）
```
Remove-DnsServerResourceRecord [-ZoneName] <String> [-PassThru] [-ComputerName <String>] [-Force]
 [-ZoneScope <String>] [-VirtualizationInstance <String>] -InputObject <CimInstance>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 未知
```
Remove-DnsServerResourceRecord [-ZoneName] <String> [-PassThru] [-ComputerName <String>] [-Force]
 [-ZoneScope <String>] [-VirtualizationInstance <String>] [-RecordData <String[]>] [-Name] <String>
 [-Type] <UInt16> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 名称
```
Remove-DnsServerResourceRecord [-ZoneName] <String> [-PassThru] [-ComputerName <String>] [-Force]
 [-ZoneScope <String>] [-VirtualizationInstance <String>] [-RRType] <String> [-RecordData <String[]>]
 [-Name] <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-DnsServerResourceRecord` cmdlet 用于从域名系统（DNS）区域中删除资源记录对象。

你可以使用 `Get-DnsServerResourceRecord` cmdlet 来指定要操作的对象，或者直接指定你想删除的资源记录的 `RRtype`（资源记录类型）、`Name`（名称）和 `RecordData`（记录数据）。如果你指定了 `RRtype` 或名称，并且存在多个匹配的资源记录，那么你还可以通过指定 `RecordData` 来删除特定的记录。如果你不指定 `RecordData`，该 cmdlet 会删除指定区域内所有与 `RRtype` 和 `Name` 匹配的资源记录。

## 示例

### 示例 1：移除所有的根提示（root hints）
```
PS C:\> Get-DnsServerResourceRecord -ZoneName "..roothints" | Remove-DnsServerResourceRecord -Force -ZoneName "..roothints"
```

此命令会删除DNS服务器的所有根提示（root hints）。

### 示例 2：删除多个 A 记录
```
PS C:\> Remove-DnsServerResourceRecord -ZoneName "contoso.com" -RRType "A" -Name "Host01"

Confirm
Removing DNS resource record Host01 of type A from zone contoso.com on ROOT server. Do you want to continue?
[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): n
```

此命令会删除contoso.com区域中所有名称为Host01的A资源记录。

### 示例 3：删除一个 A 记录
```
PS C:\> Remove-DnsServerResourceRecord -ZoneName "contoso.com" -RRType "A" -Name "Host01" -RecordData "10.17.1.41"
```

该命令会从名为 contoso.com 的区域中删除 A 类资源记录。该区域的名称为 Host01，IP 地址为 10.17.1.41。

### 示例 4：删除多个 SRV 记录
```
PS C:\> Remove-DnsServerResourceRecord -RRType SRV -Name "_misc._tcp" -ZoneName "_msdcs.contoso.com" -RecordData "0","10","1234","1.1.1.1."
```

此命令会删除_msdcs.contoso.com区域中所有名称为_misc._tcp的SRV记录。

## 参数

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
用于指定一个 DNS 服务器。如果您不指定此参数，命令将在本地系统上运行。您可以指定一个 IP 地址，或者任何能够解析为 IP 地址的值，例如完全限定域名（FQDN）、主机名或 NETBIOS 名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Cn, ForwardLookupPrimaryServer

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

### -Force
该命令会直接删除一条或多条记录，而不会先提示您进行确认。默认情况下，此 cmdlet 在执行操作前会先请求您的确认。

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

### -InputObject
指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给此 cmdlet。

```yaml
Type: CimInstance
Parameter Sets: InputObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name
指定DNS服务器资源记录对象的名称。

```yaml
Type: String
Parameter Sets: Unknown, Name
Aliases: RecordName

Required: True
Position: 2
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

### -RRType
指定资源记录的类型。

该参数的可接受值包括：  
- HInfo  
- Afsdb  
- Atma  
- Isdn  
- Key  
- Mb  
- Md  
- Mf  
- Mg  
- MInfo  
- Mr  
- Mx  
- NsNxt  
- Rp  
- Rt  
- Wks  
- X25  
- A  
- AAAA  
- CName  
- Ptr  
- Srv  
- Txt  
- Wins  
- WinsR  
- Ns  
- Soa  
- NasP  
- NasPtr  
- DName  
- Gpos  
- Loc  
- DhcId  
- Naptr  
- RRSig  
- DnsKey  
- DS  
- NSec  
- NSec3  
- NSec3Param

```yaml
Type: String
Parameter Sets: Name
Aliases:
Accepted values: HInfo, Afsdb, Atma, Isdn, Key, Mb, Md, Mf, Mg, MInfo, Mr, Mx, NsNxt, Rp, Rt, Wks, X25, A, AAAA, CName, Ptr, Srv, Txt, Wins, WinsR, Ns, Soa, NasP, NasPtr, DName, Gpos, Loc, DhcId, Naptr, RRSig, DnsKey, DS, NSec, NSec3, NSec3Param, Tlsa

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RecordData
指定您想要删除的资源记录中包含的数据。

```yaml
Type: String[]
Parameter Sets: Unknown, Name
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -Type
指定要删除的记录类型。

```yaml
Type: UInt16
Parameter Sets: Unknown
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -VirtualizationInstance
指定该区域将被添加到的虚拟化实例。虚拟化实例是DNS服务器中的逻辑分区，它能够独立托管多个区域及其相关范围。具有相同名称的区域和区域范围可以托管在不同的虚拟化实例中。此参数是可选的；如果未提供该参数，则系统会将区域添加到默认的虚拟化实例中，而这个默认实例在功能上等同于一个标准的DNS服务器。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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

### -ZoneName
指定一个DNS区域的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ForwardLookupZone

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ZoneScope
指定区域范围的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerResourceRecord[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerResourceRecord[]

## 备注

## 相关链接

[Get-DnsServerResourceRecord](./Get-DnsServerResourceRecord.md)

[Set-DnsServerResourceRecord](./Set-DnsServerResourceRecord.md)

[Add-DnsServerResourceRecord](./Add-DnsServerResourceRecord.md)
