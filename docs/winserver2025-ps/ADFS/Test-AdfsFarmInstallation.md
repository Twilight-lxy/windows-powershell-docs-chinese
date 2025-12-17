---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Deployment.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/test-adfsfarminstallation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-AdfsFarmInstallation
---

# 测试 AdfsFarm 的安装过程

## 摘要
运行安装新的联邦服务器集群所需的先决条件检查。

## 语法

### ADFSFarmCreateLocalDatabase（默认值）
```
Test-AdfsFarmInstallation [-CertificateThumbprint <String>] [-Credential <PSCredential>]
 -FederationServiceName <String> [-FederationServiceDisplayName <String>]
 -ServiceAccountCredential <PSCredential> [-OverwriteConfiguration] [-SSLPort <Int32>] [-TlsClientPort <Int32>]
 [-AdminConfiguration <Hashtable>] [<CommonParameters>]
```

### ADFSFarmCreateLocalDatabaseDisableAutoCertRollover
```
Test-AdfsFarmInstallation [-CertificateThumbprint <String>] [-Credential <PSCredential>]
 -DecryptionCertificateThumbprint <String> -FederationServiceName <String>
 [-FederationServiceDisplayName <String>] -ServiceAccountCredential <PSCredential>
 -SigningCertificateThumbprint <String> [-OverwriteConfiguration] [-SSLPort <Int32>] [-TlsClientPort <Int32>]
 [-AdminConfiguration <Hashtable>] [<CommonParameters>]
```

### ADFSFarmCreateSharedDatabase DisableAutoCertRollover
```
Test-AdfsFarmInstallation [-CertificateThumbprint <String>] [-Credential <PSCredential>]
 -DecryptionCertificateThumbprint <String> -FederationServiceName <String>
 [-FederationServiceDisplayName <String>] -ServiceAccountCredential <PSCredential>
 -SigningCertificateThumbprint <String> -SQLConnectionString <String> [-OverwriteConfiguration]
 [-SSLPort <Int32>] [-TlsClientPort <Int32>] [-AdminConfiguration <Hashtable>] [<CommonParameters>]
```

### AdfsFarmCreateLocalDatabase DisableAutoCertRolloverGmsa
```
Test-AdfsFarmInstallation [-CertificateThumbprint <String>] [-Credential <PSCredential>]
 -DecryptionCertificateThumbprint <String> -FederationServiceName <String>
 [-FederationServiceDisplayName <String>] -GroupServiceAccountIdentifier <String>
 -SigningCertificateThumbprint <String> [-OverwriteConfiguration] [-SSLPort <Int32>] [-TlsClientPort <Int32>]
 [-AdminConfiguration <Hashtable>] [<CommonParameters>]
```

### AdfsFarmCreateSharedDatabaseDisableAutoCertRolloverGmsa
```
Test-AdfsFarmInstallation [-CertificateThumbprint <String>] [-Credential <PSCredential>]
 -DecryptionCertificateThumbprint <String> -FederationServiceName <String>
 [-FederationServiceDisplayName <String>] -GroupServiceAccountIdentifier <String>
 -SigningCertificateThumbprint <String> -SQLConnectionString <String> [-OverwriteConfiguration]
 [-SSLPort <Int32>] [-TlsClientPort <Int32>] [-AdminConfiguration <Hashtable>] [<CommonParameters>]
```

### ADFSFarmCreateSharedDatabase
```
Test-AdfsFarmInstallation [-CertificateThumbprint <String>] [-Credential <PSCredential>]
 -FederationServiceName <String> [-FederationServiceDisplayName <String>]
 -ServiceAccountCredential <PSCredential> -SQLConnectionString <String> [-OverwriteConfiguration]
 [-SSLPort <Int32>] [-TlsClientPort <Int32>] [-AdminConfiguration <Hashtable>] [<CommonParameters>]
```

### AdfsFarmCreateLocalDatabaseGmsa
```
Test-AdfsFarmInstallation [-CertificateThumbprint <String>] [-Credential <PSCredential>]
 -FederationServiceName <String> [-FederationServiceDisplayName <String>]
 -GroupServiceAccountIdentifier <String> [-OverwriteConfiguration] [-SSLPort <Int32>] [-TlsClientPort <Int32>]
 [-AdminConfiguration <Hashtable>] [<CommonParameters>]
```

### AdfsFarmCreateSharedDatabaseGmsa
```
Test-AdfsFarmInstallation [-CertificateThumbprint <String>] [-Credential <PSCredential>]
 -FederationServiceName <String> [-FederationServiceDisplayName <String>]
 -GroupServiceAccountIdentifier <String> -SQLConnectionString <String> [-OverwriteConfiguration]
 [-SSLPort <Int32>] [-TlsClientPort <Int32>] [-AdminConfiguration <Hashtable>] [<CommonParameters>]
```

## 描述
`Test-AdfsFarmInstallation` 这个 cmdlet 会执行一些检查，这些检查是在你运行 `Install-AdfsFarm` cmdlet 以安装新的联合服务器场之前必须完成的。

## 示例

### 示例 1：测试在联邦服务器群中创建节点的功能
```
PS C:\> $Cred = Get-Credential
PS C:\> Test-AdfsFarmInstallation -CertificateThumbprint 8169c52b4ec6e77eb2ae17f028fe5da4e35c0bed -FederationServiceName "FS.Corp.Contoso.com" -ServiceAccountCredential $Cred
```

第一个命令使用 **Get-Credential** cmdlet 为运行 AD FS 服务的 Active Directory 账户创建一个凭据对象。该命令将凭据对象存储在 `$Cred` 变量中。

第二条命令用于测试在联邦服务器集群中创建第一个节点的过程，该集群使用本地服务器计算机上的 Windows 内部数据库。该命令指定了证书的“指纹”（即证书的唯一标识符）。AD FS 使用该证书作为 SSL 证书以及服务通信证书。对于令牌签名和令牌解密操作，系统会自动生成自签名证书。此外，该命令还指定了存储在 `$Cred` 文件中的凭据信息，这些凭据用于运行 AD FS 服务的 Active Directory 账户。

## 参数

### -AdminConfiguration
指定管理员配置信息。

```yaml
Type: Hashtable
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertificateThumbprint
指定默认网站的安全套接字层（SSL）绑定在Internet Information Services（IIS）中使用的证书指纹值。该值必须与本地计算机证书存储库中有效证书的指纹相匹配。

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

### -Credential
指定一个基于用户名和密码的 **PSCredential** 对象。要获取一个 **PSCredential** 对象，请使用 **Get-Credential** cmdlet。有关更多信息，输入 `Get-Help Get-Credential`。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DecryptionCertificateThumbprint
该参数用于指定证书的“指纹”值，Active Directory Federation Services (AD FS) 使用该指纹值来进行令牌解密。如果您指定了此参数，AD FS 将禁用自动证书更新功能，并且您必须通过设置 **SigningCertificateThumbprint** 参数来指定一个用于签署令牌的证书。该值必须与本地计算机证书存储中有效证书的“指纹”相匹配。

```yaml
Type: String
Parameter Sets: ADFSFarmCreateLocalDatabaseDisableAutoCertRollover, ADFSFarmCreateSharedDatabaseDisableAutoCertRollover, AdfsFarmCreateLocalDatabaseDisableAutoCertRolloverGmsa, AdfsFarmCreateSharedDatabaseDisableAutoCertRolloverGmsa
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FederationServiceDisplayName
指定联邦服务的显示名称。该名称默认会出现在登录页面上。

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

### -FederationServiceName
指定联邦服务的域名系统（DNS）名称。该值必须与你在 IIS 的 SSL 绑定中配置的证书的主题名称相匹配。

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

### -GroupServiceAccountIdentifier
指定 AD FS 服务所使用的组托管服务帐户（Group Managed Service Account）的名称，该帐户将作为 AD FS Windows 服务的登录身份。

```yaml
Type: String
Parameter Sets: AdfsFarmCreateLocalDatabaseDisableAutoCertRolloverGmsa, AdfsFarmCreateSharedDatabaseDisableAutoCertRolloverGmsa, AdfsFarmCreateLocalDatabaseGmsa, AdfsFarmCreateSharedDatabaseGmsa
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OverwriteConfiguration
表示 AD FS 服务会删除现有的 AD FS 配置数据库，并用一个新的数据库替换它。

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

### -ServiceAccountCredential
该命令用于根据用户名和密码创建一个 **PSCredential** 对象，该对象对应于运行 AD FS 服务的 Active Directory® 域服务中的服务账户。要获取一个 **PSCredential** 对象，可以使用 **Get-Credential** cmdlet。有关更多信息，请输入 `Get-Help Get-Credential`。

```yaml
Type: PSCredential
Parameter Sets: ADFSFarmCreateLocalDatabase, ADFSFarmCreateLocalDatabaseDisableAutoCertRollover, ADFSFarmCreateSharedDatabaseDisableAutoCertRollover, ADFSFarmCreateSharedDatabase
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SigningCertificateThumbprint
指定 AD FS 服务用于令牌签名的证书的指纹值。如果您指定了此参数，AD FS 将禁用自动证书更新功能，并且还需要使用 **DecryptionCertificateThumbprint** 参数来指定一个令牌解密证书。该值必须与本地计算机证书存储中有效证书的指纹相匹配。

```yaml
Type: String
Parameter Sets: ADFSFarmCreateLocalDatabaseDisableAutoCertRollover, ADFSFarmCreateSharedDatabaseDisableAutoCertRollover, AdfsFarmCreateLocalDatabaseDisableAutoCertRolloverGmsa, AdfsFarmCreateSharedDatabaseDisableAutoCertRolloverGmsa
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SQLConnectionString
指定用于存储 AD FS 配置设置的 Microsoft SQL Server 数据库。如果未指定此参数，则 AD FS 安装程序会使用 Windows 内部数据库来存储配置设置。

```yaml
Type: String
Parameter Sets: ADFSFarmCreateSharedDatabaseDisableAutoCertRollover, AdfsFarmCreateSharedDatabaseDisableAutoCertRolloverGmsa, ADFSFarmCreateSharedDatabase, AdfsFarmCreateSharedDatabaseGmsa
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SSLPort
指定 AD FS 网站使用的 SSL 绑定的端口号的值。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TlsClientPort
指定 AD FS 服务用于用户证书客户端传输层安全（TLS）认证的端口号。默认值为 49443。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[使用 Get-Credential 命令获取凭据](https://go.microsoft.com/fwlink/?LinkID=293936)

[安装 AdfsFarm](./Install-AdfsFarm.md)

[Test-AdfsFarmJoin](./Test-AdfsFarmJoin.md)

