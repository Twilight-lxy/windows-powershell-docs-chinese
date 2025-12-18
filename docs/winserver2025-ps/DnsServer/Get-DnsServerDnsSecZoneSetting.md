---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerDnsSecZoneSetting_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/get-dnsserverdnsseczonesetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsServerDnsSecZoneSetting
---

# 获取 DNS 服务器的 DNS 安全区域设置

## 摘要
获取某个区域的DNSSEC设置信息。

## 语法

### DnsSecSetting（默认值）
```
Get-DnsServerDnsSecZoneSetting [-ZoneName] <String[]> [-ComputerName <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### SigningMetadata
```
Get-DnsServerDnsSecZoneSetting [-ZoneName] <String[]> [-ComputerName <String>] [-SigningMetadata]
 [-IncludeKSKMetadata] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsServerDnsSecZoneSetting` cmdlet 可以获取域名系统（DNS）服务器上某个区域的域名系统安全扩展（DNSSEC）设置。

如果您指定了 *SigningMetaData* 参数，该 cmdlet 会输出一个签名元数据对象，其中包含有关区域签名的所有配置信息。您可以使用这个对象，通过执行 **Set-DnsServerDnsSecZoneSetting** cmdlet 将区域签名的配置导入到另一台服务器上。

## 示例

### 示例 1：获取 DNSSEC 设置
```
PS C:\> Get-DnsServerDnsSecZoneSetting -ZoneName "western.contoso.com"
ZoneName                      : western.contoso.com
IsKeyMasterServer             : True
KeyMasterServer               : root
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
DSRecordGenerationAlgorithm   : {Sha1, Sha256请帮我将这段Markdown格式的文本转换为中文。
DistributeTrustAnchor         : {None请帮我将这段Markdown格式的文本转换为中文。
EnableRfc5011KeyRollover      : False
ParentHasSecureDelegation     : False
SecureDelegationPollingPeriod : 12:00:00
PropagationTime               : 00:00:00
SignatureInceptionOffset      : 01:00:00
```

这个命令用于获取名为 western.contoso.com 的区域的 DNS 安全扩展（DNS Security Extensions）。

### 示例 2：获取包含签名元数据的 DNSSEC 设置
```
PS C:\> Get-DnsServerDnsSecZoneSetting -SigningMetadata -ZoneName western.contoso.com
DnsSecResourceRecords         : {DnsServerResourceRecord, DnsServerResourceRecord, DnsServerResourceRecord, DnsServerResourceRecord...请帮我将这段Markdown格式的文本转换为中文。
DnsSecZoneSetting             : DnsServerDnsSecZoneSetting
KeyExtendedInformation        : {DnsServerSigningKeyExtendedInformation请帮我将这段Markdown格式的文本转换为中文。
PSComputerName                :
ZoneName                      : western.contoso.com
IsSigned                      : True
DenialOfExistence             : NSec3
NSec3HashAlgorithm            : RsaSha1
NSec3Iterations               : 50
NSec3OptOut                   : False
NSec3RandomSaltLength         : 8
NSec3UserSalt                 : -
DistributeTrustAnchor         : None
EnableRfc5011KeyRollover      : True
DSRecordGenerationAlgorithm   : {Sha1, Sha256请帮我将这段Markdown格式的文本转换为中文。
DSRecordSetTtl                : 01:00:00
DnsKeyRecordSetTtl            : 01:00:00
SignatureInceptionOffset      : 01:00:00
SecureDelegationPollingPeriod : 12:00:00
PropagationTime               : 00:00:00
ParentHasSecureDelegation     : False
NSec3CurrentSalt              : 64A9522428558341
CurrentRollingSkdGuid         : 92491d13-f777-4d48-a9b6-6625cfd5cb9e
```

此命令用于获取名为 western.contoso.com 的区域的 DNS 安全扩展（DNS Security Extensions）签名元数据。返回的元数据可以导入到非密钥托管服务器上，以便开始使用增强的密钥管理功能来为基于文件的区域进行签名操作。

### 示例 3：获取包含签名元数据和密钥签名信息在内的 DNSSEC 设置
```
PS C:\> Get-DnsServerDnsSecZoneSetting -SigningMetadata -ZoneName "western.contoso.com" -IncludeKSKMetadata
DnsSecResourceRecords         : {DnsServerResourceRecord, DnsServerResourceRecord, DnsServerResourceRecord, DnsServerResourceRecord...请帮我将这段Markdown格式的文本转换为中文。
DnsSecZoneSetting             : DnsServerDnsSecZoneSetting
KeyExtendedInformation        : {DnsServerSigningKeyExtendedInformation, DnsServerSigningKeyExtendedInformation请帮我将这段Markdown格式的文本转换为中文。
PSComputerName                :
ZoneName                      : western.contoso.com
IsSigned                      : True
DenialOfExistence             : NSec3
NSec3HashAlgorithm            : RsaSha1
NSec3Iterations               : 50
NSec3OptOut                   : False
NSec3RandomSaltLength         : 8
NSec3UserSalt                 : -
DistributeTrustAnchor         : None
EnableRfc5011KeyRollover      : True
DSRecordGenerationAlgorithm   : {Sha1, Sha256请帮我将这段Markdown格式的文本转换为中文。
DSRecordSetTtl                : 01:00:00
DnsKeyRecordSetTtl            : 01:00:00
SignatureInceptionOffset      : 01:00:00
SecureDelegationPollingPeriod : 12:00:00
PropagationTime               : 00:00:00
ParentHasSecureDelegation     : False
NSec3CurrentSalt              : 64A9522428558341
CurrentRollingSkdGuid         : 92491d13-f777-4d48-a9b6-6625cfd5cb9e
```

此命令用于获取名为 western.contoso.com 的区域的 DNS 安全扩展（DNS Security Extensions）签名元数据和密钥签名键信息。返回的元数据可以导入到非密钥主服务器上，以便为基于文件的区域启用增强的密钥管理功能并进行签名操作。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
用于指定一个DNS服务器。如果您不指定此参数，命令将在本地系统上运行。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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

### -IncludeKSKMetadata
表示该 cmdlet 在输出对象中包含了 KSK（Key Signing Key）元数据。您可以将包含 KSK 元数据的输出对象导入到另一台服务器上。如果导入输入对象的服务器需要具备“Key Master”角色，那么该服务器可以获取“Key Master”角色。如果输出对象不包含 KSK 元数据，那么导入该输出对象的服务器将无法在保留现有密钥的情况下获取“Key Master”角色；此时您必须使用新的密钥重新生成整个区域的密钥配置。

```yaml
Type: SwitchParameter
Parameter Sets: SigningMetadata
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SigningMetadata
表示该cmdlet会在输出对象中包含所有的签名元数据。

```yaml
Type: SwitchParameter
Parameter Sets: SigningMetadata
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最优限制值。该限制仅适用于当前执行的 cmdlet，而不影响整个会话或整个计算机。

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

### -ZoneName
指定一个DNS区域名称数组。

```yaml
Type: String[]
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

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerDnsSecZoneSetting[]
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

If you specify the *SigningMetadata* parameter, the object returned is of type DnsServerZoneSigningMetadata
{

- DnsServerDnsSecZoneSetting DnsSecZoneSetting
- DnsServerSigningKeyExtendedInformation \[\] KeyExtendedInformation
- DnsServerResourceRecord\[\] DnsSecRecords

请帮我将这段Markdown格式的文本转换为中文。

DnsServerDnsSecZoneSetting
{

- String ZoneName
- Bool DenialOfExistence
- Bool NSec3HashAlgorithm
- Integer NSec3Iterations
- Bool NSec3OptOut
- Integer NSec3RandomSaltLength
- String NSec3UserSalt
- String\[\] DistributeTrustAnchor
- Bool EnableRfc5011KeyRollover
- String\[\] DSRecordGenerationAlgorithm
- Bool ParentHasSecureDelegation
- DateTime DsRecordSetTtl
- DateTime DnsKeyRecordSetTtl
- DateTime SignatureInceptionOffset
- DateTime SecureDelegationPollingPeriod
- DateTime PropagationTime
- Bool IsKeyMasterServer
- String KeyMasterServer
- String KeyMasterStatus
- Bool IsSigned
- String NSec3CurrentSalt
- String CurrentRollingSkdGuid

请帮我将这段Markdown格式的文本转换为中文。

DnsServerSigningKeyOpState
{

- Integer CurrentRolloverState
- Bool ManualTrigger
- Integer PreRollEventFired
- TimeSpan NextKeyGenerationTime
- DnsServerResourceRecordDnsKey\[\] RevokedOrSwappedDnsKeys
- DnsServerResourceRecordDnsKey\[\] FinalDnsKeys
- Integer ActiveKeyScope
- Integer StandbyKeyScope
- Integer NextKeyScope

请帮我将这段Markdown格式的文本转换为中文。

DnsServerSigningKeyExtendedInformation
{

- DnsServerSigningKey SigningKey
- DnsServerSigningKeyOpState SigningKeyOpState
请帮我将这段Markdown格式的文本转换为中文。

## 备注

## 相关链接

[Set-DnsServerDnsSecZoneSetting](./Set-DnsServerDnsSecZoneSetting.md)

[Test-DnsServerDnsSecZoneSetting](./Test-DnsServerDnsSecZoneSetting.md)

