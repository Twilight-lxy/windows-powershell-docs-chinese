---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfscertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsCertificate
---

# 删除 Adfs 证书

## 摘要
从 AD FS 中删除证书。

## 语法

### TargetCertificate（默认值）
```
Remove-AdfsCertificate [-TargetCertificate] <ServiceCertificate> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ByProperties
```
Remove-AdfsCertificate -CertificateType <String> -Thumbprint <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-AdfsCertificate` cmdlet 用于从 Active Directory Federation Services (AD FS) 中删除证书。

## 示例

### 示例 1：移除令牌签名证书
```
PS C:\> Remove-AdfsCertificate -CertificateType "Token-Signing" -Thumbprint ‎"fedd995b45e633d4ef30fcbc8f3a48b627e9a28b"
```

此命令会从 AD FS 中删除用于令牌签名的证书。

## 参数

### -CertificateType
指定要删除的证书的类型。此参数的可接受值为：

- Infocard-Signing
- Service-Communications
- Token-Encryption
- Token-Signing

```yaml
Type: String
Parameter Sets: ByProperties
Aliases:
Accepted values: Token-Decrypting, Token-Signing

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetCertificate
指定要删除的证书。该值通常来自处理流程（pipeline）。

```yaml
Type: ServiceCertificate
Parameter Sets: TargetCertificate
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Thumbprint
指定要删除的证书的“指纹”（即用于唯一标识该证书的信息）。

```yaml
Type: String
Parameter Sets: ByProperties
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftIdentityServer POWERShell.Resources.ServiceCertificate

`*TargetCertificate*` 参数接收一个 `ServiceCertificate` 对象。

### System.String

*Thumbprint* 参数接收一个字符串对象作为参数值。

## 输出

### 无

## 备注
* Removing a certificate removes it only from the AD FS configuration data. It does not remove or delete the certificate from the local certificate store on the server computer.

## 相关链接

[Add-AdfsCertificate](./Add-AdfsCertificate.md)

[Get-AdfsCertificate](./Get-AdfsCertificate.md)

[Set-AdfsCertificate](./Set-AdfsCertificate.md)

[更新 AdfsCertificate](./Update-AdfsCertificate.md)

