---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerTrustAnchor_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsservertrustanchor?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerTrustAnchor
---

# Add-DnsServerTrustAnchor

## 摘要
向DNS服务器添加一个信任锚点。

## 语法

### DnsKey（默认值）
```
Add-DnsServerTrustAnchor [-Name] <String> [-KeyProtocol <String>] -Base64Data <String> [-ComputerName <String>]
 [-CryptoAlgorithm] <String> [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### DS
```
Add-DnsServerTrustAnchor [-Name] <String> [-ComputerName <String>] [-CryptoAlgorithm] <String> [-PassThru]
 -KeyTag <UInt16> -DigestType <String> -Digest <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 根目录（Root）
```
Add-DnsServerTrustAnchor [-ComputerName <String>] [-PassThru] [-Root] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DnsServerTrustAnchor` cmdlet 用于向域名系统（DNS）服务器添加信任锚点（DNSKEY 记录或 DS 记录）。如果当前没有信任锚点，该 cmdlet 会创建一个。如果您指定了 *DigestType* 参数，那么它还会添加一个信任锚点委托签名者（DS）记录。

如果您指定了*Root*参数，该cmdlet将从DNS服务器的RootTrustAnchorsURL属性中指定的URL获取信任锚点。

## 示例

### 示例 1：向 DNS 服务器添加信任锚点
```
PS C:\> Get-DnsServerResourceRecord -ZoneName "sec.contoso.com" -RRType "dnskey" -ComputerName DNS1 | %{ $_.RecordData | Add-DnsServerTrustAnchor -PassThru -Verbose -Name "sec.contoso.com"}
VERBOSE: Adding trust anchor for trust point sec.contoso.com of type DNSKEY on server Server01.
TrustAnchorName             TrustAnchorType      TrustAnchorState     TrustAnchorData
---------------              ---------------      ----------------     ---------------
sec.contoso.com             DNSKEY               Valid                [23600][DnsSec][RsaSha256][AwEAAbZvBTiMzoqK...
VERBOSE: Adding trust anchor for trust point sec.contoso.com of type DNSKEY on server Server01.
sec.contoso.com             DNSKEY               Valid                [53180][DnsSec][RsaSha256][AwEAAbsS7NnziyRY...
VERBOSE: Adding trust anchor for trust point sec.contoso.com of type DNSKEY on server Server01.

sec.contoso.com             DNSKEY               Valid                [50272][DnsSec][RsaSha256][AwEAAe1EkxNj6M1b...
VERBOSE: Adding trust anchor for trust point sec.contoso.com of type DNSKEY on server Server01.
sec.contoso.com             DNSKEY               Valid                [37436][DnsSec][RsaSha256][AwEAAa1PJyk2lITB...
VERBOSE: Adding trust anchor for trust point sec.contoso.com of type DNSKEY on server Server01.
sec.contoso.com             DNSKEY               Valid                [2895][DnsSec][RsaSha1NSec3][AwEAAbOk5nl41M...
VERBOSE: Adding trust anchor for trust point sec.contoso.com of type DNSKEY on server Server01.
sec.contoso.com             DNSKEY               Valid                [62250][DnsSec][RsaSha1NSec3][AwEAAci9Ayfjg...
VERBOSE: Adding trust anchor for trust point sec.contoso.com of type DNSKEY on server Server01.
sec.contoso.com             DNSKEY               Valid                [47244][DnsSec][RsaSha1NSec3][AwEAAcFv94ne6...
```

此命令使用 **Get-DnsServerResourceRecord** cmdlet 从名为 sec.contoso.com 的区域的 DNS 服务器 DNS1 中获取一个 DnsKey 资源记录。然后，该命令通过管道运算符将该资源记录传递给 **Add-DnsServerTrustAnchor** cmdlet，以便为当前 DNS 服务器添加与此区域相关的信任锚点（trust anchor）。

### 示例 2：从 RootTrustAnchorsURL 属性中添加一个信任锚点
```
PS C:\> Add-DnsServerTrustAnchor -Root
```

此命令会添加来自DNS服务器的**RootTrustAnchorsURL**属性所指定的URL中的信任锚点。

## 参数

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -Base64Data
指定关键数据。

```yaml
Type: String
Parameter Sets: DnsKey
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个远程DNS服务器。该参数的可接受值为：IP地址，或任何能够解析为IP地址的字符串，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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

### -CryptoAlgorithm
指定cmdlet用于生成密钥的加密算法。该参数的可接受值包括：

- RsaSha1
- RsaSha256
- RsaSha512
- RsaSha1NSec3
- ECDsaP256Sha256
- ECDsaP384Sha384

```yaml
Type: String
Parameter Sets: DnsKey, DS
Aliases:
Accepted values: RsaSha1, RsaSha256, RsaSha512, RsaSha1NSec3, ECDsaP256Sha256, ECDsaP384Sha384

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Digest
指定DS摘要数据。

```yaml
Type: String
Parameter Sets: DS
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DigestType
指定区域签名密钥用于创建 DNS 记录的算法类型。有效值包括以下一个或多个：  
- Sha1  
- Sha256  
- Sha384

```yaml
Type: String
Parameter Sets: DS
Aliases:
Accepted values: Sha1, Sha256, Sha384

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -KeyProtocol
指定密钥协议，默认值为 Dnssec。

```yaml
Type: String
Parameter Sets: DnsKey
Aliases:
Accepted values: DnsSec

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -KeyTag
指定 DNS 服务器用于标识某个密钥的唯一键标签。

```yaml
Type: UInt16
Parameter Sets: DS
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定DNS服务器上一个信任锚点的名称。

```yaml
Type: String
Parameter Sets: DnsKey, DS
Aliases: TrustAnchorName

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不生成任何输出。

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

### -Root
表示该 cmdlet 会从 DNS 服务器的 **RootTrustAnchorsURL** 属性指定的 URL 中添加根区域的信任锚点。

```yaml
Type: SwitchParameter
Parameter Sets: Root
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerTrustAnchor
DnsServerTrustAnchor对象包含以下字段：

- EnteredStateTime
- KeyTag
- NextStateTime
- TrustAnchorData
- TrustAnchorName
- TrustAnchorState
- TrustAnchorType

## 备注

## 相关链接

[Get-DnsServerTrustAnchor](./Get-DnsServerTrustAnchor.md)

[Import-DnsServerTrustAnchor](./Import-DnsServerTrustAnchor.md)

[Remove-DnsServerTrustAnchor](./Remove-DnsServerTrustAnchor.md)

[Get-DnsServerResourceRecord](./Get-DnsServerResourceRecord.md)

