---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.KpsServer.Administration.dll-Help.xml
Module Name: HgsKeyProtection
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgskeyprotection/remove-hgskeyprotectioncertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-HgsKeyProtectionCertificate
---

# 移除 HGS Key Protection 证书

## 摘要
从密钥保护服务中删除一个密钥证书。

## 语法

```
Remove-HgsKeyProtectionCertificate -CertificateType <KeyCertificateType> -Thumbprint <String> [-Force]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-HgsKeyProtectionCertificate` 这个 cmdlet 用于从 Key Protection Service 中删除某个密钥证书。如果被删除的证书引用了存储在 `LocalMachine\My` 证书库中的其他证书，那么该 cmdlet 不会从 `LocalMachine\My` 证书库中删除那些参考证书。

## 示例

#### 示例 1：移除加密证书
```
PS C:\> Remove-HgsKeyProtectionCertificate -CertificateType Encryption -Thumbprint "d39203a3b3544743ad552afe0615dc1f"
```

此命令会从密钥保护服务中删除一个加密证书。

## 参数

### -CertificateType
指定此cmdlet要删除的证书的类型。该参数的可接受值包括：

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

### -Thumbprint
指定要删除的证书的“指纹”（即该证书的唯一标识信息）。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无
您无法将输入数据通过管道传递给此cmdlet。

## 输出

### 无
此cmdlet不生成任何输出。

## 备注

## 相关链接

[Add-HgsKeyProtectionCertificate](./Add-HgsKeyProtectionCertificate.md)

[Get-HgsKeyProtectionCertificate](./Get-HgsKeyProtectionCertificate.md)

[Set-HgsKeyProtectionCertificate](./Set-HgsKeyProtectionCertificate.md)

