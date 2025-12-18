---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerResourceRecordDnsKey_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserverresourcerecorddnskey?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerResourceRecordDnsKey
---

# Add-DnsServerResourceRecordDnsKey

## 摘要
向DNS区域添加一种类型的DNSKEY资源记录。

## 语法

```
Add-DnsServerResourceRecordDnsKey [-Name] <String> [-CryptoAlgorithm] <String> [-ZoneName] <String>
 [-TimeToLive <TimeSpan>] [-AgeRecord] [-Base64Data] <String> [-KeyProtocol <String>] [-ComputerName <String>]
 [-SecureEntryPoint] [-ZoneKey] [-PassThru] [-ZoneScope <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DnsServerResourceRecordDNSKEY` cmdlet 用于向域名系统（DNS）服务器添加 DNSKEY 资源记录。DNSKEY 是 DNS 安全扩展（DNSSEC）中的一个元素，用于存储公钥。您通常使用此 cmdlet 将 DNSKEY 记录添加到 TrustAnchors 区域中。

*AgeRecord* 参数与 DS 资源记录无关。

如果你没有指定 **SecureEntryPoint** 或 **ZoneSigningKey**，该 cmdlet 会创建一个带有 Secure Entry Point (SEP) 标志的信任锚点。

## 示例

### 示例 1：向另一台计算机添加 DNSKEY 资源记录
```
PS C:\> $DNSKEYS = Get-DnsServerResourceRecord -RRType DnsKey -ZoneName "contoso.com" -ComputerName "dnsserver.contoso.com"
PS C:\> $DNSKEYS | %{ $_.RecordData | Add-DnsServerResourceRecordDnsKey -ZoneName "TrustAnchors" -Name  "contoso.com"  -ComputerName "dnsresolver.contoso.com" }
```

这个示例将名为 contoso.com 的区域的 DNSKEY 资源记录从名为 dnsserver.contoso.com 的服务器添加到名为 dnsResolver.contoso.com 的服务器上。

第一个命令用于获取 DNSKEY 资源记录，并将其存储在名为 **$DNSKEYS** 的变量中。

第二个命令从 `$DSNKEYS` 中获取 DNSKEY 资源记录，并将该资源记录存储在名为 `TrustAnchors` 的区域中，该区域位于服务器 `dnsResolver.contoso.com` 上。

## 参数

### -AgeRecord
表示DNS服务器会为该cmdlet添加的资源记录使用时间戳。DNS服务器可以根据时间戳来清理那些已经过期的资源记录。

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

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -Base64Data
指定此资源记录的关键数据。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

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
用于指定一个 DNS 服务器。如果您不指定此参数，命令将在本地系统上运行。您可以指定一个 IP 地址，或者任何能够解析为 IP 地址的数值，例如完全限定域名（FQDN）、主机名或 NETBIOS 名称。

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
在运行该cmdlet之前，会提示您确认是否要执行该操作。

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

### -CryptoAlgorithm
指定服务器用于生成密钥的加密算法。该参数的可接受值如下：

- RsaSha1
- RsaSha256
- RsaSha512
- RsaSha1NSec3
- ECDsaP256Sha256
- ECDsaP384Sha384

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: RsaSha1, RsaSha256, RsaSha512, RsaSha1NSec3, ECDsaP256Sha256, ECDsaP384Sha384

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -KeyProtocol
指定此资源记录的关键协议。该参数的唯一取值为 Dnssec。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: DnsSec

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定此cmdlet添加到DNS服务器中的资源记录的名称。

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

### -SecureEntryPoint
指定该密钥是否是一个安全的入口点（如 RFC 3757 中所定义）。

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

### -ThrottleLimit
指定可以同时运行的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -TimeToLive
用于指定资源记录的生存时间（Time to Live，简称TTL）值，单位为秒。其他DNS服务器会依据这个时间长度来决定记录的缓存时长。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上，这个cmdlet并没有被执行。

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

### -ZoneKey
指定是否可以使用该密钥来签署区域（zone）。该密钥可以是区域签名密钥（Zone Signing Key，简称ZSK），也可以是密钥签名密钥（Key Signing Key，简称KSK）。

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

### -ZoneName
指定一个DNS区域的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ZoneScope
指定区域范围（zone scope）的名称。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerResourceRecord

## 备注

## 相关链接

