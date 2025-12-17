---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfscertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsCertificate
---

# 添加 AdFS 证书

## 摘要
向 AD FS 添加新的证书，用于签名、解密或保护通信安全。

## 语法

```
Add-AdfsCertificate -CertificateType <String> -Thumbprint <String> [-IsPrimary] [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Add-AdfsCertificate` cmdlet 用于向 Active Directory Federation Services (AD FS) 添加新的证书，这些证书可用于令牌签名、令牌解密、卡片签名或保护通信安全。

## 示例

### 示例 1：添加一个令牌签名证书
```powershell
PS C:\> Add-AdfsCertificate -CertificateType "Token-Signing" -Thumbprint ‎"fedd995b45e633d4ef30fcbc8f3a48b627e9a28b"
```

此命令添加了一个用于令牌签名的证书，其指纹（thumbprint）为`fedd995b45e633d4ef30fcbc8f3a48b627e9a28b`。

## 参数

### -CertificateType
指定证书的类型和用途。该参数的可接受值如下：

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Token-Decrypting, Token-Signing

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsPrimary
该标记用于指示证书是否为“主要证书”。主要的令牌签名证书用于对发出的声明进行数字签名；主要的令牌加密证书会发布在联盟元数据中，供可信的声明提供者使用。服务通信证书始终属于主要证书。

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
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

*Thumbprint* 参数接收一个字符串对象作为参数。

## 输出

### Microsoft.IdentityServer POWERShell.Resources.ServiceCertificate

当指定*PassThru*参数时，该命令会返回一个新的ServiceCertificate对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* Active Directory Federation Services (AD FS) uses certificates for issuing and receiving tokens, publishing federation metadata, and communication through Secure Sockets Layer (SSL).

## 相关链接

[Get-AdfsCertificate](./Get-AdfsCertificate.md)

[Remove-AdfsCertificate](./Remove-AdfsCertificate.md)

[Set-AdfsCertificate](./Set-AdfsCertificate.md)

[更新 AdfsCertificate](./Update-AdfsCertificate.md)

