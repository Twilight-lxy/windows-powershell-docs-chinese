---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.DeviceHealthAttestation.PowerShell.dll-Help.xml
Module Name: DeviceHealthAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/devicehealthattestation/install-devicehealthattestation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-DeviceHealthAttestation
---

# 安装设备健康证明（Install-DeviceHealthAttestation）

## 摘要
安装设备健康证明服务。

## 语法

### 安装（默认设置）
```
Install-DeviceHealthAttestation -EncryptionCertificateThumbprint <String>
 -SigningCertificateThumbprint <String> -SupportedAuthenticationSchema <String> [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 安装并添加 SSL 绑定
```
Install-DeviceHealthAttestation -EncryptionCertificateThumbprint <String>
 -SigningCertificateThumbprint <String> -SslCertificateThumbprint <String>
 [-SslCertificateStoreName <StoreName>] -SupportedAuthenticationSchema <String> [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Install-DeviceHealthAttestation` cmdlet 用于安装设备健康认证（Device Health Attestation）服务并配置其依赖项。在安装该服务之前，必须先添加相应的角色（即 Device Health Attestation 服务角色）。

安装过程会完成以下操作：

- Creates an application pool.
- Creates a web application.
- Adds a firewall rule for incoming requests.
- Sets the initial configuration.
- Registers user access logging.

您必须具有管理员权限才能运行此cmdlet。

## 示例

### 示例 1：安装设备健康证明服务
```
PS C:\> Install-DeviceHealthAttestation -EncryptionCertificateThumbprint "0123456789ABCDEF0123456789ABCDEF01234567" -SigningCertificateThumbprint "0123456789ABCDEF0123456789ABCDEF01234567" -SupportedAuthenticationSchema "AikPub,EkCertificate"
```

此命令用于安装设备健康认证（Device Health Attestation）服务。

### 示例 2：使用 SSL 安装设备健康认证服务
```
PS C:\> Install-DeviceHealthAttestation -EncryptionCertificateThumbprint "0123456789ABCDEF0123456789ABCDEF01234567" -SigningCertificateThumbprint "0123456789ABCDEF0123456789ABCDEF01234567" -SupportedAuthenticationSchema "AikPub,EkCertificate" -SslCertificateThumbprint "0123456789ABCDEF0123456789ABCDEF01234567" -SslCertificateStoreName "My"
```

该命令安装了带有SSL绑定的设备健康证明（Device Health Attestation）服务。

## 参数

### -Confirm
在运行cmdlet之前会提示您进行确认。

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

### -EncryptionCertificateThumbprint
指定加密证书的指纹（thumbprint）。该值必须仅包含十六进制数字（0-9、A-F），且长度为40个字符。此值不区分大小写。

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

### -Force
强制命令运行，而不会请求用户确认。

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

### -SigningCertificateThumbprint
指定签名证书的指纹（thumbprint）。该值必须仅包含十六进制数字（0-9、A-F），长度为40个字符。此值的大小写不敏感。

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

### -SslCertificateStoreName
指定包含由*SslCertificateThumbprint*参数引用的证书的证书存储库。该参数的可接受值为：

- AddressBook
- AuthRoot
- CertificateAuthority
- Disallowed
- My
- Root
- TrustedPeople
- TrustedPublisher

```yaml
Type: StoreName
Parameter Sets: InstallAndAddSslBinding
Aliases:
Accepted values: AddressBook, AuthRoot, CertificateAuthority, Disallowed, My, Root, TrustedPeople, TrustedPublisher

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SslCertificateThumbprint
指定用于服务器SSL绑定的证书的“指纹”（即证书的唯一标识符）。该值必须仅包含十六进制数字（0-9、A-F），且长度为40个字符。此值不区分大小写。

如果您指定了*SslCertificateThumbprint*参数，该cmdlet会在默认网站上创建一个SSL绑定。如果您指定了此参数，还必须指定*SslCertificateStoreName*参数。

```yaml
Type: String
Parameter Sets: InstallAndAddSslBinding
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SupportedAuthenticationSchema
以逗号分隔的列表形式指定设备健康认证服务支持的认证方案。该参数的可接受值为：

- AikPub
- AikCertificate
- EkCertificate

You cannot specify both AikCertificate and EkCertificate in the same command.

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[卸载设备健康认证功能](./Uninstall-DeviceHealthAttestation.md)

