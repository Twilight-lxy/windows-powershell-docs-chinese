---
description: 检查本地证书颁发机构（CA）是否信任用于身份密钥验证的安全硬件。
external help file: Microsoft.CertificateServices.Administration.Commands.dll-Help.xml
Module Name: ADCSAdministration
online version: https://learn.microsoft.com/powershell/module/adcsadministration/confirm-caattestationidentitykeyinfo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Confirm-CAAttestationIdentityKeyInfo
---

# 确认 CA 证书身份验证密钥信息

## 摘要
检查本地证书颁发机构（CA）是否信任用于身份密钥验证的安全硬件。

## 语法

### PublicKeyHash
```
Confirm-CAAttestationIdentityKeyInfo [-PublicKeyHash] <String> [<CommonParameters>]
```

### 证书
```
Confirm-CAAttestationIdentityKeyInfo [-Certificate] <X509Certificate2> [<CommonParameters>]
```

## 描述
`Confirm-CAAttestationIdentityKeyInfo` cmdlet 用于检查本地证书颁发机构（CA）是否信任安全硬件（如受信任的平台模块（TPM））来执行身份密钥的认证。认证身份密钥（AIK，Attestation Identity Key）取代了传统的“认可密钥”（Endorsement Key），成为 TPM 的身份标识。该密钥被永久性地嵌入到安全硬件中；其公钥部分有助于识别真正的安全硬件设备。

此cmdlet用于验证AIK公钥证书是否通过证书链连接到CA（证书颁发机构）所信任的根证书。请使用**Certificate**参数指定一个X509证书。

此cmdlet用于检查AIK公钥是否作为文件存在于本地CA（证书颁发机构）配置的文件夹中，该文件夹用于密钥验证。请使用**PublicKeyHash**参数来指定公钥。

## 示例

### 示例 1：检查证书
```
Confirm-CAAttestationIdentityKeyInfo -Certificate Contoso87.cer

True
```

此命令通过使用证书链来检查`Contoso87.cer`证书是否能够连接到某个受信任的根证书（即“可信锚点”）。在这个例子中，返回的结果是`$True`。

### 示例 2：检查一个键
```
Confirm-CAAttestationIdentityKeyInfo -PublicKeyHash "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"

False
```

该命令用于检查以 SHA-256 哈希码形式指定的公共证书。在这个示例中，返回的值是 `$False`，说明该证书颁发机构（CA）并不拥有这个公共密钥。

## 参数

### -Certificate
用于指定一份为保护硬件而颁发的 X509 公钥证书。

```yaml
Type: X509Certificate2
Parameter Sets: Certificate
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PublicKeyHash
指定安全硬件生成的证明身份密钥（Attestation Identity Key，简称AIK）的公钥，该公钥是通过SHA-256哈希算法计算得到的。该值是一个64个字符的十六进制字符串。

```yaml
Type: String
Parameter Sets: PublicKeyHash
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.security.Cryptography.X509Certificates.X509Certificate2

## 输出

### SystemBoolean

## 备注

## 相关链接

[Confirm-CAEndorsementKeyInfo](Confirm-CAEndorsementKeyInfo.md)

[Add-CAAuthorityInformationAccess](Add-CAAuthorityInformationAccess.md)

[Add-CACrlDistributionPoint](Add-CACrlDistributionPoint.md)

[Backup-CARoleService](Backup-CARoleService.md)

[Confirm-CAEndorsementKeyInfo](Confirm-CAEndorsementKeyInfo.md)
