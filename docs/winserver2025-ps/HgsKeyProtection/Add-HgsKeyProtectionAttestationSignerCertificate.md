---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.KpsServer.Administration.dll-Help.xml
Module Name: HgsKeyProtection
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgskeyprotection/add-hgskeyprotectionattestationsignercertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-HgsKeyProtectionAttestationSignerCertificate
---

# 使用 `Add-HgsKeyProtectionAttestationSignerCertificate` 命令

## 摘要
为密钥保护服务（Key Protection Service）中的受信任证书添加一个证明签名者证书。

## 语法

```
Add-HgsKeyProtectionAttestationSignerCertificate -Certificate <X509Certificate2> [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-HgsKeyProtectionAttestationSignerCertificate` cmdlet 将证明服务器的签名证书添加到 Key Protection Service（密钥保护服务）所信任的证书列表中。Key Protection Service 使用这些签名证书来验证健康状态证书的签名。若要修改某个签名证书的相关策略，请使用 `Set-HgsKeyProtectionAttestationSignerCertificatePolicy` cmdlet。

## 示例

### 示例 1：添加证书
```
PS C:\> Add-HgsKeyProtectionAttestationSignerCertificate -Certificate $Certificate
```

此命令将存储在 `$Certificate` 变量中的证书添加到受信任的认证签名者证书列表中。

## 参数

### -Certificate
用于指定一个 **X509Certificate2** 证书。此cmdlet会将该参数指定的证书添加到密钥保护服务（Key Protection Service）所信任的认证签名者证书列表中。请指定一个存储 **X509Certificate2** 对象的变量，或一个用于获取该证书的表达式。

```yaml
Type: X509Certificate2
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需请求用户确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无
您无法将输入数据通过管道传递给此cmdlet。

## 输出

### 无
这个cmdlet不会生成任何输出。

## 备注

## 相关链接

[Get-HgsKeyProtectionAttestationSignerCertificate](./Get-HgsKeyProtectionAttestationSignerCertificate.md)

[Remove-HgsKeyProtectionAttestationSignerCertificate](./Remove-HgsKeyProtectionAttestationSignerCertificate.md)

[Set-HgsKeyProtectionAttestationSignerCertificatePolicy](./Set-HgsKeyProtectionAttestationSignerCertificatePolicy.md)

