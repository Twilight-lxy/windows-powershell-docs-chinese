---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsServer-help.xml
Module Name: HgsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsserver/initialize-hgsserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Initialize-HgsServer
---

# 初始化 HGS 服务器

## 摘要
初始化Host Guardian服务服务器。

## 语法

### PrimaryServer_HgsDomain（默认值）
```
Initialize-HgsServer [-HgsServiceName] <String> [-UseHgsDomain] [-LogDirectory <String>] [-Http] [-Https]
 [-HttpPort <UInt16>] [-HttpsPort <UInt16>] [-HttpsCertificatePath <String>]
 [-HttpsCertificatePassword <SecureString>] [-HttpsCertificateThumbprint <String>] [-TrustActiveDirectory]
 [-TrustTpm] [-EncryptionCertificateThumbprint <String>] [-EncryptionCertificatePath <String>]
 [-EncryptionCertificatePassword <SecureString>] [-SigningCertificateThumbprint <String>]
 [-SigningCertificatePath <String>] [-SigningCertificatePassword <SecureString>] [-HgsVersion <HgsVersion>]
 [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### PrimaryServer_SecureDomain
```
Initialize-HgsServer [-HgsServiceName] <String> [-UseExistingDomain] [-LogDirectory <String>]
 -JeaAdministratorsGroup <ADGroup> -JeaReviewersGroup <ADGroup> -ServiceAccount <ADServiceAccount>
 [-ClusterName <String>] [-Http] [-Https] [-HttpPort <UInt16>] [-HttpsPort <UInt16>]
 [-HttpsCertificatePath <String>] [-HttpsCertificatePassword <SecureString>]
 [-HttpsCertificateThumbprint <String>] [-TrustActiveDirectory] [-TrustTpm]
 [-EncryptionCertificateThumbprint <String>] [-EncryptionCertificatePath <String>]
 [-EncryptionCertificatePassword <SecureString>] [-SigningCertificateThumbprint <String>]
 [-SigningCertificatePath <String>] [-SigningCertificatePassword <SecureString>] [-HgsVersion <HgsVersion>]
 [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### AdditionalServer
```
Initialize-HgsServer [-HgsServerIPAddress] <String> [-LogDirectory <String>] [-Http] [-Https]
 [-HttpPort <UInt16>] [-HttpsPort <UInt16>] [-HttpsCertificatePath <String>]
 [-HttpsCertificatePassword <SecureString>] [-HttpsCertificateThumbprint <String>] [-Force] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Initialize-HgsServer` cmdlet 在主机保护服务（Host Guardian Service，简称 HGS）重新启动后，配置所需的基础设施组件。

此 cmdlet 对第一个 HGS 节点的基础设施组件执行以下配置操作：

- Creates one-node failover cluster.
- Configures a failover cluster with a distributed network name resource corresponding to the fully qualified domain name of the HGS name: \<HgsServerName\>.\<LocalDomain\>.
- Registers and configures the Attestation service web application with the IIS service.
- Registers and configures the Key Protection service web application with the IIS service.
- Configures the Attestation service signer certificate with the Key Protection service.
- Enables Just Enough Administration on the local node.

This cmdlet makes the following configuration changes to components on an additional HGS node:

- Adds the local node to the existing failover cluster on a node specified by the **HgsServerIPAddress** parameter using the credential specified in the **HgsDomainCredential** parameter.

- Registers and configures the Attestation service web application with the IIS service.
- Registers and configures the Key Protection service web application with the IIS service.
- Configures the Attestation service signer certificate with the Key Protection service.
- Enables Just Enough Administration on the local node.

有关场景术语的更多信息，请参阅[安全与保障](https://go.microsoft.com/fwlink/?LinkId=699209)。

## 示例

### 示例 1：在主节点上以 TPM 模式初始化 HGS
```
PS C:\> Initialize-HgsServer -HgsServiceName "SecureFabricHgs" -EncryptionCertificateThumbprint $EncryptionCert.Thumbprint -SigningCertificateThumbprint $SigningCert.Thumbprint
```

此命令用于初始化主节点上的HGS服务器。默认情况下，该服务器可通过HTTP端口80进行访问，并且认证服务被设置为TPM模式。指定的证书将由密钥保护服务使用。

### 示例 2：在 TPM 模式下，在辅助节点上初始化 HGS
```
PS C:\> $Cred = Get-Credential
PS C:\> Initialize-HgsServer -HgsServerIPAddress "100.100.100.1" -HgsDomainCredential $Cred
```

此命令用于在辅助节点上初始化HGS服务器。默认情况下，该服务器可以通过HTTP端口80进行访问，并且认证服务（Attestation service）被设置为TPM模式。密钥保护服务（Key Protection service）使用由主服务器设置的加密和签名证书。

### 示例 3：在 Active Directory 模式下初始化主节点上的 HGS
```
PS C:\> Initialize-HgsServer -TrustActiveDirectory -HgsServiceName "SecureFabricHgs" -EncryptionCertificateThumbprint $EncryptionCert.Thumbprint -SigningCertificateThumbprint $SigningCert.Thumbprint
```

此命令用于在主节点上初始化HGS服务器，并将认证服务设置为Active Directory（AD）模式。默认情况下，该服务器可通过HTTP端口80进行访问。Key Protection服务会使用指定的证书。

### 示例 4：在主节点上以 TPM 模式初始化 HGS 并启用 HTTPS
```
PS C:\> Initialize-HgsServer -HgsServiceName "SecureFabricHgs" -EncryptionCertificateThumbprint $EncryptionCert.Thumbprint -SigningCertificateThumbprint $SigningCert.Thumbprint -http -https -HttpsCertificatePath $PathToPfx -HttpsCertificatePassword $PfxSecureString
```

此命令用于初始化主节点上的HGS服务器。该服务器可以通过HTTP和HTTPS在默认端口上进行访问，并使用指定的证书进行HTTPS通信。默认情况下，服务器通过HTTP端口80提供服务，且认证服务（Attestation service）设置为TPM模式。Key Protection服务会使用这些指定的证书。

## 参数

### -ClusterName
指定一个集群名称。

```yaml
Type: String
Parameter Sets: PrimaryServer_SecureDomain
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EncryptionCertificatePassword
指定用于 **EncryptionCertificatePath** 中指定的证书文件的密码。

```yaml
Type: SecureString
Parameter Sets: PrimaryServer_HgsDomain, PrimaryServer_SecureDomain
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EncryptionCertificatePath
指定密钥保护服务所使用的加密证书的路径。

```yaml
Type: String
Parameter Sets: PrimaryServer_HgsDomain, PrimaryServer_SecureDomain
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EncryptionCertificateThumbprint
指定密钥保护服务所使用的加密证书的“指纹”（即用于唯一标识该证书的信息）。

```yaml
Type: String
Parameter Sets: PrimaryServer_HgsDomain, PrimaryServer_SecureDomain
Aliases:

Required: False
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

### -HgsServerIPAddress
指定作为所选 HGS 域域名控制器的 HGS 服务器的 IP 地址。

```yaml
Type: String
Parameter Sets: AdditionalServer
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HgsServiceName
指定HGS名称。

```yaml
Type: String
Parameter Sets: PrimaryServer_HgsDomain, PrimaryServer_SecureDomain
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HgsVersion
保留以供将来使用。

```yaml
Type: HgsVersion
Parameter Sets: PrimaryServer_HgsDomain, PrimaryServer_SecureDomain
Aliases:
Accepted values: HgsVersion1503, HgsVersion1704

Required: False
Position: Named
Default value: $script:HgsSupportedLevels[0]
Accept pipeline input: False
Accept wildcard characters: False
```

### -Http
表示可以通过 HTTP 访问 HGS 服务器。

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

### -HttpPort
指定HGS服务器的HTTP端口。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Https
表示可以通过 HTTPS 访问 HGS 服务器。

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

### -HttpsCertificatePassword
指定由 **HttpsCertificatePath** 指定的证书文件对应的密码。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HttpsCertificatePath
指定 HTTPS 证书文件（.pfx）的路径。

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

### -HttpsCertificateThumbprint
表示HTTPS证书的“指纹”（即用于唯一标识该证书的特征信息）。

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

### -HttpsPort
指定 HGS 服务器的 HTTPS 端口。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -JeaAdministratorsGroup
识别可以通过“Just Enough Administration”（JEA）来管理HGS的用户所属的Active Directory组。

```yaml
Type: ADGroup
Parameter Sets: PrimaryServer_SecureDomain
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -JeaReviewersGroup
识别出那些可以通过“Just Enough Administration”（JEA）查看但不能更改HGS设置的用户所属的Active Directory组。

```yaml
Type: ADGroup
Parameter Sets: PrimaryServer_SecureDomain
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogDirectory
指定输出日志文件的目录。

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

### -ServiceAccount
确定将用于密钥保护服务的组托管服务账户（Group Managed Service Account）。指定的账户必须已经安装并配置好，以便在此机器上使用。

```yaml
Type: ADServiceAccount
Parameter Sets: PrimaryServer_SecureDomain
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SigningCertificatePassword
指定由 **SigningCertificatePath** 指定的证书文件所需的密码。

```yaml
Type: SecureString
Parameter Sets: PrimaryServer_HgsDomain, PrimaryServer_SecureDomain
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SigningCertificatePath
指定用于密钥保护服务的签名证书的路径。

```yaml
Type: String
Parameter Sets: PrimaryServer_HgsDomain, PrimaryServer_SecureDomain
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SigningCertificateThumbprint
指定签名证书的“指纹”（即唯一标识符），供密钥保护服务使用。

```yaml
Type: String
Parameter Sets: PrimaryServer_HgsDomain, PrimaryServer_SecureDomain
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TrustActiveDirectory
```yaml
Type: SwitchParameter
Parameter Sets: PrimaryServer_HgsDomain, PrimaryServer_SecureDomain
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TrustTpm
```yaml
Type: SwitchParameter
Parameter Sets: PrimaryServer_HgsDomain, PrimaryServer_SecureDomain
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseExistingDomain
这表示 HGS 已被添加到现有的域中，并且没有使用 `Install-HgsServer` 命令来创建自己的独立域。为了继续操作，HGS 必须已经处于该现有域的范围内。

```yaml
Type: SwitchParameter
Parameter Sets: PrimaryServer_SecureDomain
Aliases:

Required: True
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseHgsDomain
这表示使用 `Install-HgsServer` cmdlet 为 HGS 设置了专用的 Active Directory 林（即独立的 Active Directory 环境）。

```yaml
Type: SwitchParameter
Parameter Sets: PrimaryServer_HgsDomain
Aliases:

Required: False
Position: Named
Default value: False
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[HGS 服务器 cmdlet](./hgsserver.md)

