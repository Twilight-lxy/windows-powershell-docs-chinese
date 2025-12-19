---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.KpsServer.Administration.dll-Help.xml
Module Name: HgsKeyProtection
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgskeyprotection/get-hgskeyprotectionattestationsignercertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-HgsKeyProtectionAttestationSignerCertificate
---

# 获取 HGS 密钥保护证明签名者证书

## 摘要
获取密钥保护服务所信任的认证签名者证书。

## 语法

```
Get-HgsKeyProtectionAttestationSignerCertificate [-Thumbprint <String>] [<CommonParameters>]
```

## 描述
`Get-HgsKeyProtectionAttestationSignerCertificate` cmdlet 可以获取密钥保护服务（Key Protection Service）所信任的认证签名者证书。

## 示例

#### 示例 1：获取所有证明证书
```
PS C:\> Get-HgsKeyProtectionAttestationSignerCertificate
```

该命令获取密钥保护服务（Key Protection Service）所信任的所有认证证书签署者信息。

### 示例 2：获取单个认证证书
```
PS C:\> Get-HgsKeyProtectionAttestationSignerCertificate -Thumbprint "d39203a3b3544743ad552afe0615dc1f"
```

该命令获取一个密钥保护服务（Key Protection Service）所信任的认证证书签名者。命令通过使用“指纹”（thumbprint）来查找该证书签名者。

## 参数

### -Thumbprint
指定要获取的认证签名者证书的“指纹”（即该证书的唯一标识信息）。如果未为此参数指定值，此cmdlet将获取所有受信任的认证服务器的认证签名者证书。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无
你不能将输入内容通过管道（pipe）传递给这个cmdlet。

## 输出

### Microsoft.Windows.KpsServer.Common.Store.Data.AttestationCertificate
此 cmdlet 返回一个 **AttestationCertificate** 对象，该对象代表一个证明签名者的证书。该对象包含以下字段：

- Certificate.
The **X509Certificate2** object.
- AttestationCertificatePolicy.
The policy that describes further limitations on which health certificates signed by this signer certificate are trusted by the Key Protection Service.

## 备注

## 相关链接

[Add-HgsKeyProtectionAttestationSignerCertificate](./Add-HgsKeyProtectionAttestationSignerCertificate.md)

[Remove-HgsKeyProtectionAttestationSignerCertificate](./Remove-HgsKeyProtectionAttestationSignerCertificate.md)

