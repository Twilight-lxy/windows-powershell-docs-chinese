---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfscertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsCertificate
---

# 设置 Adfs 证书

## 摘要
用于设置现有证书的属性，这些属性被 Active Directory Federation Services (AD FS) 用来签名、解密或保护通信安全。

## 语法

```
Set-AdfsCertificate -CertificateType <String> -Thumbprint <String> [-IsPrimary] [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsCertificate` cmdlet 用于设置现有证书的属性，该证书由 Active Directory Federation Services (AD FS) 使用来签名、解密或保护通信安全。

## 示例

### 示例 1：设置证书
```
PS C:\> Set-AdfsCertificate -IsPrimary -CertificateType "Token-Signing" -Thumbprint ‎"fedd995b45e633d4ef30fcbc8f3a48b627e9a28b"
```

此命令用于设置主要的令牌签名证书。

## 参数

### -CertificateType
指定证书类型（即联邦服务使用该证书的方式）。此参数的可接受值包括：

- Service-Communications
- Token-Decrypting
- Token-Signing

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Service-Communications, Token-Decrypting, Token-Signing

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsPrimary
这表示该证书是主证书（primary certificate）。主令牌签名证书用于对发出的声明（claims）进行数字签名；主令牌加密证书则会被发布在联合身份验证系统的元数据中，供可信的声明提供者使用。信息卡签名证书和服务通信证书始终属于主证书类型。

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

### -PassThru
返回一个表示您当前正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -Thumbprint
指定要使用的证书的“指纹”（即用于唯一标识该证书的信息）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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

### -WhatIf
展示了如果该cmdlet运行会发生的结果。但实际上该cmdlet并没有被运行。

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

### System.String

*Thumbprint* 参数接收的是一个 String 对象。

## 输出

### MicrosoftIdentityServer.PowerShellResources.ServiceCertificate

当指定*PassThru*参数时，会返回更新后的ServiceCertificate对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* Use the **Set-AdfsRelyingPartyTrust** or **Set-AdfsClaimsProviderTrust** cmdlets, as appropriate, to modify the certificates that are associated with a relying party or a claims provider.

## 相关链接

[Add-AdfsCertificate](./Add-AdfsCertificate.md)

[Get-AdfsCertificate](./Get-AdfsCertificate.md)

[Remove-AdfsCertificate](./Remove-AdfsCertificate.md)

[更新 AdfsCertificate](./Update-AdfsCertificate.md)

