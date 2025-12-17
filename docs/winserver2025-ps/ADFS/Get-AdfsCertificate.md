---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfscertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsCertificate
---

# 获取 Adfs 证书

## 摘要
从 AD FS 中检索证书。

## 语法

### 按类型（默认值）
```
Get-AdfsCertificate [[-CertificateType] <String[]>] [<CommonParameters>]
```

### ByReference
```
Get-AdfsCertificate [-Thumbprint] <String[]> [<CommonParameters>]
```

## 描述
`Get-AdfsCertificate` cmdlet 可以检索 Active Directory Federation Services (AD FS) 用于令牌签名、令牌解密、卡片签名以及保护服务通信的证书。

## 示例

### 示例 1：获取令牌签名证书
```
PS C:\> Get-AdfsCertificate -CertificateType "Token-Signing"
```

此命令用于检索用于 AD FS（Active Directory Federation Services）的令牌签名证书。

## 参数

### -CertificateType
指定要检索的证书类型。该参数的可接受值包括：

- Infocard-Signing
- Service-Communications
- Token-Encryption
- Token-Signing

```yaml
Type: String[]
Parameter Sets: ByType
Aliases:
Accepted values: Service-Communications, Token-Decrypting, Token-Signing

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Thumbprint
指定要检索的证书的“指纹”（即用于唯一标识该证书的信息）。

```yaml
Type: String[]
Parameter Sets: ByReference
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### MicrosoftIdentityServer.PowerShell.Resources.ServiceCertificate

返回一个或多个 ServiceCertificate 对象，这些对象代表了 AD FS 的证书信息。

## 备注
* You can use the **Get-AdfsCertificate** cmdlet without any parameters to get all the certificates.

## 相关链接

[Add-AdfsCertificate](./Add-AdfsCertificate.md)

[Remove-AdfsCertificate](./Remove-AdfsCertificate.md)

[Set-AdfsCertificate](./Set-AdfsCertificate.md)

[更新 AdfsCertificate](./Update-AdfsCertificate.md)

