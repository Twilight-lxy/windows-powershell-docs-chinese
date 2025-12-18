---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerSigningKey_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserversigningkey?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerSigningKey
---

# Add-DnsServerSigningKey

## 摘要
向已签名的区域添加KSK（Key Signing Key）或ZSK（Zone Signing Key）。

## 语法

```
Add-DnsServerSigningKey [-ZoneName] <String> [[-Type] <String>] [[-CryptoAlgorithm] <String>]
 [-ComputerName <String>] [[-KeyLength] <UInt32>] [-InitialRolloverOffset <TimeSpan>]
 [-DnsKeySignatureValidityPeriod <TimeSpan>] [-DSSignatureValidityPeriod <TimeSpan>]
 [-ZoneSignatureValidityPeriod <TimeSpan>] [-RolloverPeriod <TimeSpan>] [-ActiveKey <String>]
 [-StandbyKey <String>] [-NextKey <String>] [-KeyStorageProvider <String>] [-StoreKeysInAD <Boolean>]
 [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-DnsServerSigningKey` cmdlet 可用于将密钥签名键（KSK）或区域签名键（ZSK）添加到已签名的域名系统（DNS）区域中。

## 示例

#### 示例 1：向 DNS 区域中添加一个 KSK（密钥签名密钥）
```
PS C:\> Add-DnsServerSigningKey -ZoneName "corp.contoso.com" -Type "KeySigningKey" -CryptoAlgorithm "RsaSha1NSec3" -KeyLength 2048 -PassThru -Verbose
```

此命令将一个KSK添加到DNS签名区域corp.contoso.com中。

## 参数

### -ActiveKey
指定一个用于KSK活动密钥的签名密钥指针字符串。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
用于指定一个远程DNS服务器。您可以输入一个IP地址，或者任何能够解析为IP地址的字符串，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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
指定用于生成密钥的加密算法。该参数的可接受值包括：

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

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DSSignatureValidityPeriod
指定覆盖数据签名（DS）记录集的签名的有效时间长度。

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

### -DnsKeySignatureValidityPeriod
指定了覆盖DNSKEY记录集的签名的有效时间长度。

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

### -InitialRolloverOffset
指定延迟首次计划中的密钥轮换的时间长度。您可以使用 **InitialRolloverOffset** 来错开密钥轮换的时机。

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

### -KeyLength
指定密钥的位长度。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -KeyStorageProvider
指定DNS服务器用于生成密钥的密钥存储提供商。

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

### -NextKey
为下一个密钥指定一个签名密钥指针字符串。DNS服务器在下次密钥轮换事件中使用该密钥。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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

### -RolloverPeriod
指定计划中的密钥轮换之间的时间间隔。

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

### -StandbyKey
指定一个用于KSK备用密钥的签名密钥指针字符串。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StoreKeysInAD
指定是否将密钥存储在 Active Directory 域服务（AD DS）中。此设置仅适用于由 Microsoft 提供 KeyStorageProvider 服务的、与 Active Directory 集成的区域。

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

### -Type
指定一个密钥是 KSK（Key Signing Key）还是 ZSK（Zona Signing Key）。

```yaml
Type: String
Parameter Sets: (All)
Aliases: KeyType
Accepted values: KeySigningKey, ZoneSigningKey

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被运行。

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
指定执行 DNS 安全扩展（DNSSEC）操作的区域的名称。

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

### -ZoneSignatureValidityPeriod
指定那些能够覆盖所有其他记录集的签名的有效时间长度。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerSigningKey

## 备注

## 相关链接

[Disable-DnsServer SigningKeyRollover](./Disable-DnsServerSigningKeyRollover.md)

[Enable-DnsServerSigningKeyRollover](./Enable-DnsServerSigningKeyRollover.md)

[Get-DnsServerSigningKey](./Get-DnsServerSigningKey.md)

[Invoke-DnsServerSigningKeyRollover](./Invoke-DnsServerSigningKeyRollover.md)

[Remove-DnsServerSigningKey](./Remove-DnsServerSigningKey.md)

[Set-DnsServerSigningKey](./Set-DnsServerSigningKey.md)

