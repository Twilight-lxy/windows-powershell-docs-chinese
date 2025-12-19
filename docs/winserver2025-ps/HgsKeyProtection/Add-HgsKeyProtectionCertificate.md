---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.KpsServer.Administration.dll-Help.xml
Module Name: HgsKeyProtection
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgskeyprotection/add-hgskeyprotectioncertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-HgsKeyProtectionCertificate
---

# Add-HgsKeyProtectionCertificate

## 摘要
将一个密钥证书添加到密钥保护服务中。

## 语法

### CertificateReference（默认值）
```
Add-HgsKeyProtectionCertificate -CertificateType <KeyCertificateType> -Thumbprint <String>
 [-NoCertificateReplication] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### FullCertificate
```
Add-HgsKeyProtectionCertificate -CertificateType <KeyCertificateType> -CertificatePath <String>
 [-CertificatePassword <SecureString>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-HgsKeyProtectionCertificate` cmdlet 用于将证书添加到 Key Protection Service（密钥保护服务）中。您可以添加加密证书或签名证书；也可以添加存储在 Windows 证书库中的证书的引用。在添加证书引用之前，必须先将该证书添加到 `LocalMachine\My` 证书库中。该 cmdlet 会通过使用证书的指纹来从 `LocalMachine\My` 证书库中查找相应的证书。此外，您还可以直接将存储在文件中的完整证书（以 pfx 格式）添加进来。如果包含 pfx 文件的文件需要密码保护，则必须指定相应的密码。

## 示例

### 示例 1：添加加密证书
```
PS C:\> Add-HgsKeyProtectionCertificate -CertificateType Encryption -Thumbprint "d39203a3b3544743ad552afe0615dc1f"
```

此命令将一个证书引用添加到密钥保护服务中，以便用作加密证书。

### 示例 2：添加一个带有密码的加密证书文件
```
PS C:\> Add-HgsKeyProtectionCertificate -CertificateType Encryption -CertificatePath "C:\example.pfx" -CertificatePassword $Password
```

这个命令将一个证书文件添加到密钥保护服务（Key Protection Service）中，用作加密证书。在这个例子中，该证书文件受到一个密码的保护，而这个密码以 `SecureString` 的形式存储在变量 `$Password` 中。

## 参数

### -CertificatePassword
指定用于保护证书文件的密码。如果证书文件需要通过密码进行保护，那么就必须提供这个密码值。

```yaml
Type: SecureString
Parameter Sets: FullCertificate
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertificatePath
指定要将证书添加到密钥保护服务（Key Protection Service）中的路径。

```yaml
Type: String
Parameter Sets: FullCertificate
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertificateType
指定此 cmdlet 所添加的证书的类型。该参数的可接受值为：

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
强制命令运行，而不需要用户确认。

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

### -NoCertificateReplication
这仅适用于您使用 `-Thumbprint` 选项来指定证书的情况。该选项通常用于基于硬件安全模块（HSM）的证书，但也可以用于其他类型的证书。设置 `NoCertificateReplication` 会禁用从 `LocalMachine\MyCertificates` 存储库自动将证书复制到集群中所有其他节点的相同存储库的功能。此时，HSM 管理员需要负责手动将该证书复制到集群中的所有其他节点上。

```yaml
Type: SwitchParameter
Parameter Sets: CertificateReference
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Thumbprint
指定要添加的证书的“指纹”（即证书的唯一标识符）。在运行当前cmdlet之前，必须先将该证书添加到LocalMachine\My Certificate Store文件夹中。

```yaml
Type: String
Parameter Sets: CertificateReference
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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
您不能将输入数据通过管道（pipe）传递给此cmdlet。

## 输出

### 无
这个cmdlet不会生成任何输出。

## 备注

## 相关链接

[Get-HgsKeyProtectionCertificate](./Get-HgsKeyProtectionCertificate.md)

[Remove-HgsKeyProtectionCertificate](./Remove-HgsKeyProtectionCertificate.md)

[Set-HgsKeyProtectionCertificate](./Set-HgsKeyProtectionCertificate.md)

