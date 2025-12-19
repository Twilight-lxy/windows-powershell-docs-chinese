---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.KpsServer.Administration.dll-Help.xml
Module Name: HgsKeyProtection
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgskeyprotection/set-hgskeyprotectioncertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-HgsKeyProtectionCertificate
---

# Set-HgsKeyProtectionCertificate

## 摘要
修改密钥保护服务中某个密钥证书的属性。

## 语法

```
Set-HgsKeyProtectionCertificate -CertificateType <KeyCertificateType> -Thumbprint <String>
 [-IsEnabled <Boolean>] [-IsPrimary] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-HgsKeyProtectionCertificate` cmdlet 用于修改 Key Protection Service 中密钥证书的属性。你可以将某个证书设置为主证书；主证书用于签署和加密新的密钥保护器（key protector）。你还可以启用或禁用某个证书，已启用的证书可用于签署或加密操作，而已禁用的证书无法成为主证书。

## 示例

#### 示例 1：禁用一个密钥证书
```
PS C:\> Set-HgsKeyProtectionCertificate -CertificateType Signing -Thumbprint "a0e2650e25084961a24da956d132a5fa" -IsEnabled $False
```

此命令会禁用一个签名密钥证书。

### 示例 2：将某证书指定为默认证书
```
PS C:\> Set-HgsKeyProtectionCertificate -CertificateType Encryption -Thumbprint "a17dd68f4ecc499bbe65ee18718123da" -IsPrimary
```

此命令将某个证书指定为主要证书。

## 参数

### -CertificateType
指定此cmdlet所修改的证书的类型。该参数的可接受值包括：

- Signing
- Encryption

```yaml
Type: KeyCertificateType
Parameter Sets: (All)
Aliases:
Accepted values: Signing, Encryption

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需询问用户的确认。

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

### -IsEnabled
用于指示是否启用某个证书。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsPrimary
表示该cmdlet会将某个证书设置为主要证书。

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
指定要修改的证书的“指纹”（即证书的唯一标识符）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无
您不能将输入数据通过管道（pipe）传递给这个cmdlet。

## 输出

### 无
这个cmdlet不会生成任何输出。

## 备注

## 相关链接

[Add-HgsKeyProtectionCertificate](./Add-HgsKeyProtectionCertificate.md)

[Get-HgsKeyProtectionCertificate](./Get-HgsKeyProtectionCertificate.md)

[Remove-HgsKeyProtectionCertificate](./Remove-HgsKeyProtectionCertificate.md)

