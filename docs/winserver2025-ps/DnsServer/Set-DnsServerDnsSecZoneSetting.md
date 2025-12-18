---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerDnsSecZoneSetting_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverdnsseczonesetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerDnsSecZoneSetting
---

# Set-DnsServerDnsSecZoneSetting

## 摘要
更改某个区域的DNSSEC设置。

## 语法

### DnsSecSetting（默认值）
```
Set-DnsServerDnsSecZoneSetting [-ZoneName] <String> [[-DenialOfExistence] <String>]
 [-NSec3HashAlgorithm <String>] [-NSec3Iterations <UInt16>] [-NSec3OptOut <Boolean>]
 [-NSec3RandomSaltLength <Byte>] [-NSec3UserSalt <String>] [-DistributeTrustAnchor <String[]>]
 [-EnableRfc5011KeyRollover <Boolean>] [-DSRecordGenerationAlgorithm <String[]>] [-DSRecordSetTtl <TimeSpan>]
 [-DnsKeyRecordSetTtl <TimeSpan>] [-SignatureInceptionOffset <TimeSpan>]
 [-SecureDelegationPollingPeriod <TimeSpan>] [-PropagationTime <TimeSpan>]
 [-ParentHasSecureDelegation <Boolean>] [-ComputerName <String>] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SigningMetadata
```
Set-DnsServerDnsSecZoneSetting [-ZoneName] <String> [-ComputerName <String>] [-PassThru]
 [[-InputObject] <CimInstance>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsServerDnsSecZoneSetting` cmdlet 用于更改域名系统（DNS）服务器上指定区域的域名系统安全扩展（DNSSEC）设置。

您可以选择使用哪个版本的 Next Secure (NSEC) 来实现经过身份验证的“不存在性拒绝”（authenticated denial of existence）功能。将 *DenialOfExistence* 参数设置为 NSec 或 NSec3。如果您使用 NSec3，可以选择使用随机生成的盐值（random salt）或用户自定义的盐值（user-defined salt）。

在使用 *SigningMetadata* 参数集时，该cmdlet会将 **CimInstance#DnsServerZone SigningMetadata** 作为输入对象。您可以将此cmdlet与 Get-DnsServerDnsSecZoneSetting 结合使用，以便将一个DNS服务器上的DNSSEC元数据导入到另一个DNS服务器中。

## 示例

### 示例 1：修改 RFC 5011 的设置
```
PS C:\> Set-DnsServerDnsSecZoneSetting -ZoneName "west01.contoso.com" -EnableRfc5011KeyRollover $True -PassThru -Verbose

VERBOSE: Modifies the DNSSEC properties for the zone west01.contoso.com on server Server01.
VERBOSE: RFC5011KeyRollovers successfully set on server Server01.
ZoneName                      : west01.contoso.com
IsKeyMasterServer             : True
KeyMasterServer               : Server01.west01.contoso.com
KeyMasterStatus               : Online
DenialOfExistence             : NSec3
NSec3HashAlgorithm            : RsaSha1
NSec3Iterations               : 50
NSec3OptOut                   : False
IsNSec3SaltConfigured         : True
NSec3RandomSaltLength         : 8
NSec3UserSalt                 : -
DnsKeyRecordSetTTL            : 01:00:00
DSRecordSetTTL                : 01:00:00
DSRecordGenerationAlgorithm   : {Sha1, Sha256}
DistributeTrustAnchor         : {None}
EnableRfc5011KeyRollover      : True
ParentHasSecureDelegation     : False
SecureDelegationPollingPeriod : 12:00:00
PropagationTime               : 2.00:00:00
SignatureInceptionOffset      : 01:00:00
```

此命令用于修改名为 west01.contoso.com 的区域的 RFC 5011 设置。示例中使用了 *PassThru* 参数来生成输出结果，并使用 *verbose* 参数来显示所有输出内容。

### 示例 2：导入 DNSSEC 签名元数据
```
PS C:\> Get-DnsServerDnsSecZoneSetting -SigningMetadata -ZoneName "contoso.com" -IncludeKSKMetadata -ComputerName "KeyMaster01" | Set-DnsServerDnsSecZoneSetting -ComputerName "EdgeServer01"
```

此命令使用 **Get-DnsServerDnsSecZoneSetting** cmdlet 从名为 contoso.com 的区域中的 DNS 服务器 KeyMaster01 获取 DNSSEC 签名元数据（包括 KSK 元数据）。该命令通过管道运算符将 DNSSEC 签名元数据传递给当前的 cmdlet，并将这些元数据设置到名为 EdgeServer01 的非关键主服务器上。如果该服务器上的区域尚未进行签名处理，命令会使用区域签名密钥在该服务器上启动签名过程。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称或会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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

### -DSRecordGenerationAlgorithm
用于指定域服务记录的加密算法数组。该参数的可接受值包括：

- Sha1
- Sha256
- Sha384

```yaml
Type: String[]
Parameter Sets: DnsSecSetting
Aliases:
Accepted values: None, Sha1, Sha256, Sha384

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DSRecordSetTtl
为这组域名服务记录指定一个TTL时间跨度。默认值与该区域的TTL值相同。

```yaml
Type: TimeSpan
Parameter Sets: DnsSecSetting
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DenialOfExistence
指定要使用哪个版本的NSEC（Name Server Extensions）。DNS服务器利用此设置来提供未经注册的名称的签名验证。

此参数的可接受值包括：

- NSec
- NSec3

```yaml
Type: String
Parameter Sets: DnsSecSetting
Aliases:
Accepted values: NSec, NSec3

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DistributeTrustAnchor
Specifies an array of trust anchors that a DNS server distributes in Active Directory® Domain Services.
DNS servers do not distribute trust anchors by default.
If the DNS server is not also a domain controller, it adds trust anchors only to the local trust anchor store.

```yaml
Type: String[]
Parameter Sets: DnsSecSetting
Aliases:
Accepted values: None, DnsKey

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DnsKeyRecordSetTtl
Specifies a time-span object that represents the Time to Live (TTL) value of a DNS key record.

```yaml
Type: TimeSpan
Parameter Sets: DnsSecSetting
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableRfc5011KeyRollover
Specifies whether a server uses RFC 5011 key rollover.

```yaml
Type: Boolean
Parameter Sets: DnsSecSetting
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InputObject
Specifies the input to this cmdlet.
You can use this parameter, or you can pipe the input to this cmdlet.

```yaml
Type: CimInstance
Parameter Sets: SigningMetadata
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -NSec3HashAlgorithm
Specifies an NSEC3 hash algorithm.
The only possible value is RsaSha1.

```yaml
Type: String
Parameter Sets: DnsSecSetting
Aliases:
Accepted values: RsaSha1

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NSec3Iterations
Specifies a number of NSEC3 hash iterations to perform when it signs a DNS zone.
The default value is 50.

```yaml
Type: UInt16
Parameter Sets: DnsSecSetting
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NSec3OptOut
Specifies whether to sign the DNS zone by using NSEC opt-out.
The default value is $False.

```yaml
Type: Boolean
Parameter Sets: DnsSecSetting
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NSec3RandomSaltLength
Specifies the length of a salt value.
The default length is 8.

```yaml
Type: Byte
Parameter Sets: DnsSecSetting
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NSec3UserSalt
Specifies a user salt string.
The default value is Null or -.

```yaml
Type: String
Parameter Sets: DnsSecSetting
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ParentHasSecureDelegation
Specifies whether a parent has secure delegation for a zone.
The default value is $False.

```yaml
Type: Boolean
Parameter Sets: DnsSecSetting
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

### -PropagationTime
Specifies a propagation time as a time-span object.
This is the expected time required to propagate zone changes.
The default value is 2 days.

```yaml
Type: TimeSpan
Parameter Sets: DnsSecSetting
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SecureDelegationPollingPeriod
Specifies a delegation polling period as a time-span object.
This is the time between polling attempts for key rollovers for child zones.
The default value is 12 hours.

```yaml
Type: TimeSpan
Parameter Sets: DnsSecSetting
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SignatureInceptionOffset
Specifies the signature inception as a time-span object.
This value is how far in the past DNSSEC signature validity periods begin.
The default value is one hour.

```yaml
Type: TimeSpan
Parameter Sets: DnsSecSetting
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行该cmdlet的最大操作数量。如果省略此参数或输入`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算一个最佳的限制值（即并发操作的上限）。这个限制仅适用于当前正在执行的cmdlet，而不影响整个会话或计算机本身的运行状态。

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被执行。

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
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerDnsSecZoneSetting
`DnsServerDnsSecZoneSetting` 对象包含以下字段：

- DenialOfExistence
- DistributeTrustAnchor
- DnsKeyRecordSetTtl
- DSRecordGenerationAlgorithm
- DSRecordSetTtl
- EnableRfc5011KeyRollover
- IsKeyMasterServer
- KeyMasterServer
- KeyMasterStatus
- NSec3HashAlgorithm
- NSec3Iterations
- NSec3OptOut
- NSec3RandomSaltLength
- NSec3UserSalt
- ParentHasSecureDelegation
- PropagationTime
- SecureDelegationPollingPeriod
- SignatureInceptionOffset
- ZoneName

## 备注

## 相关链接

[Get-DnsServerDnsSecZoneSetting](./Get-DnsServerDnsSecZoneSetting.md)

[测试 DNS 服务器的 DNS 安全区域设置](./Test-DnsServerDnsSecZoneSetting.md)

