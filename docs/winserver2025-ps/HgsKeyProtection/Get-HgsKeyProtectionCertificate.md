---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.KpsServer.Administration.dll-Help.xml
Module Name: HgsKeyProtection
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgskeyprotection/get-hgskeyprotectioncertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-HgsKeyProtectionCertificate
---

# 获取 HGS Key Protection 证书

## 摘要
在密钥保护服务中获取关键的证书。

## 语法

### GetMultipleCerts（默认值）
```
Get-HgsKeyProtectionCertificate [-CertificateType <KeyCertificateType>] [-IsEnabled <Boolean>]
 [-IsPrimary <Boolean>] [<CommonParameters>]
```

### GetOneCert
```
Get-HgsKeyProtectionCertificate -CertificateType <KeyCertificateType> -Thumbprint <String> [<CommonParameters>]
```

## 描述
`Get-HgsKeyProtectionCertificate` cmdlet 用于获取 Key Protection Service 中的密钥证书。

## 示例

#### 示例 1：获取所有密钥证书
```
PS C:\> Get-HgsKeyProtectionCertificate
```

这个命令可以从密钥保护服务（Key Protection Service）中获取所有的密钥证书。

### 示例 2：获取特定的密钥证书
```
PS C:\> Get-HgsKeyProtectionCertificate -CertificateType Encryption -Thumbprint "a17dd68f4ecc499bbe65ee18718123da"
```

这个命令会获取一个具有指定类型和指纹的密钥证书。

### 示例 3：获取已启用的非主键证书
```
PS C:\> Get-HgsKeyProtectionCertificate -IsEnabled $True -IsPrimary $False
```

这个命令会获取所有已启用但不是主键证书的文件。

## 参数

### -CertificateType
指定此cmdlet获取的证书的类型。该参数的可接受值如下：

- Signing
- Encryption

If you do not specify this parameter, the cmdlet gets both signing and encryption certificates.

```yaml
Type: KeyCertificateType
Parameter Sets: GetMultipleCerts
Aliases:
Accepted values: Signing, Encryption

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: KeyCertificateType
Parameter Sets: GetOneCert
Aliases:
Accepted values: Signing, Encryption

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsEnabled
指定是启用还是禁用密钥证书。如果指定值为 `$True`，则仅获取已启用的证书；如果指定值为 `$False`，则仅获取已被禁用的证书。如果不指定此参数，该 cmdlet 会同时获取已启用和已被禁用的证书。

```yaml
Type: Boolean
Parameter Sets: GetMultipleCerts
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsPrimary
指定是否获取主键证书。如果指定值为 `$True`，则仅获取主键证书；如果指定值为 `$False`，则仅获取非主键证书。如果不指定此参数，该 cmdlet 会同时获取主键证书和非主键证书。

```yaml
Type: Boolean
Parameter Sets: GetMultipleCerts
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Thumbprint
指定要获取的证书的“指纹”（即证书的唯一标识符）。如果您指定了此参数，则还必须指定 **CertificateType** 参数。

```yaml
Type: String
Parameter Sets: GetOneCert
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无
您无法将输入数据通过管道（pipe）传递给此cmdlet。

## 输出

### Microsoft.Windows.KpsServer COMMON.Store.Data.KeyCertificate
此cmdlet返回一个密钥证书。该对象包含以下字段：

- **Thumbprint**.
The thumbprint of the certificate.
- **CertificateType**.
The type of the certificate.
Valid values are: Encryption and Signing.
- **Enabled**.
Whether the certificate is enabled.
- **Primary**.
Whether this certificate is the primary certificate.
- **Certificate**.
The full **X509Certificate2** object associated with this key certificate.

## 备注

## 相关链接

[Add-HgsKeyProtectionCertificate](./Add-HgsKeyProtectionCertificate.md)

[Remove-HgsKeyProtectionCertificate](./Remove-HgsKeyProtectionCertificate.md)

[Set-HgsKeyProtectionCertificate](./Set-HgsKeyProtectionCertificate.md)

