---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Deployment.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/install-adfsfarm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-AdfsFarm
---

# 安装 AdfsFarm

## 摘要
创建一个新的联邦服务器群的第一个节点。

## 语法

### ADFSFarmCreateLocalDatabase（默认值）
```
Install-AdfsFarm [-CertificateThumbprint <String>] [-Credential <PSCredential>] -FederationServiceName <String>
 [-FederationServiceDisplayName <String>] -ServiceAccountCredential <PSCredential> [-OverwriteConfiguration]
 [-SSLPort <Int32>] [-TlsClientPort <Int32>] [-AdminConfiguration <Hashtable>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ADFSFarmCreateLocalDatabase DisableAutoCertRollover
```
Install-AdfsFarm [-CertificateThumbprint <String>] [-Credential <PSCredential>]
 -DecryptionCertificateThumbprint <String> -FederationServiceName <String>
 [-FederationServiceDisplayName <String>] -ServiceAccountCredential <PSCredential>
 -SigningCertificateThumbprint <String> [-OverwriteConfiguration] [-SSLPort <Int32>] [-TlsClientPort <Int32>]
 [-AdminConfiguration <Hashtable>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ADFSFarmCreateSharedDatabaseDisableAutoCertRollover
```
Install-AdfsFarm [-CertificateThumbprint <String>] [-Credential <PSCredential>]
 -DecryptionCertificateThumbprint <String> -FederationServiceName <String>
 [-FederationServiceDisplayName <String>] -ServiceAccountCredential <PSCredential>
 -SigningCertificateThumbprint <String> -SQLConnectionString <String> [-OverwriteConfiguration]
 [-SSLPort <Int32>] [-TlsClientPort <Int32>] [-AdminConfiguration <Hashtable>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### AdfsFarmCreateLocalDatabaseDisableAutoCertRolloverGmsa
```
Install-AdfsFarm [-CertificateThumbprint <String>] [-Credential <PSCredential>]
 -DecryptionCertificateThumbprint <String> -FederationServiceName <String>
 [-FederationServiceDisplayName <String>] -GroupServiceAccountIdentifier <String>
 -SigningCertificateThumbprint <String> [-OverwriteConfiguration] [-SSLPort <Int32>] [-TlsClientPort <Int32>]
 [-AdminConfiguration <Hashtable>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### AdfsFarmCreateSharedDatabaseDisableAutoCertRolloverGmsa
```
Install-AdfsFarm [-CertificateThumbprint <String>] [-Credential <PSCredential>]
 -DecryptionCertificateThumbprint <String> -FederationServiceName <String>
 [-FederationServiceDisplayName <String>] -GroupServiceAccountIdentifier <String>
 -SigningCertificateThumbprint <String> -SQLConnectionString <String> [-OverwriteConfiguration]
 [-SSLPort <Int32>] [-TlsClientPort <Int32>] [-AdminConfiguration <Hashtable>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ADFSFarmCreateSharedDatabase
```
Install-AdfsFarm [-CertificateThumbprint <String>] [-Credential <PSCredential>] -FederationServiceName <String>
 [-FederationServiceDisplayName <String>] -ServiceAccountCredential <PSCredential>
 -SQLConnectionString <String> [-OverwriteConfiguration] [-SSLPort <Int32>] [-TlsClientPort <Int32>]
 [-AdminConfiguration <Hashtable>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### AdfsFarmCreateLocalDatabaseGmsa
```
Install-AdfsFarm [-CertificateThumbprint <String>] [-Credential <PSCredential>] -FederationServiceName <String>
 [-FederationServiceDisplayName <String>] -GroupServiceAccountIdentifier <String> [-OverwriteConfiguration]
 [-SSLPort <Int32>] [-TlsClientPort <Int32>] [-AdminConfiguration <Hashtable>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### AdfsFarmCreateSharedDatabaseGmsa
```
Install-AdfsFarm [-CertificateThumbprint <String>] [-Credential <PSCredential>] -FederationServiceName <String>
 [-FederationServiceDisplayName <String>] -GroupServiceAccountIdentifier <String> -SQLConnectionString <String>
 [-OverwriteConfiguration] [-SSLPort <Int32>] [-TlsClientPort <Int32>] [-AdminConfiguration <Hashtable>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Install-AdfsFarm` cmdlet 用于创建新的联合服务器群中的第一个节点。

## 示例

### 示例 1：在本地服务器上使用 WID 创建联邦服务器群中的第一个节点
```
PS C:\> $fscredential = Get-Credential
PS C:\> Install-AdfsFarm -CertificateThumbprint 8169c52b4ec6e77eb2ae17f028fe5da4e35c0bed -FederationServiceName fs.corp.contoso.com -ServiceAccountCredential $fscredential
```

在联邦服务器群中创建第一个节点，该节点使用本地服务器计算机上的 Windows 内部数据库（WID）。

在这个例子中，为 *CertificateThumbprint* 参数提供了一个证书指纹值。该证书将用作 SSL 证书以及服务通信证书。用于令牌签名和令牌解密的证书将是自动生成的、自我签名的证书。

要指定用于令牌签名和令牌解密的证书，请为 *SigningCertificateThumbprint* 和 *DecryptionCertificateThumbprint* 参数提供相应的指纹值。

### 示例 2：使用组托管服务账户在联合服务器群中创建第一个节点
```
PS C:\> Install-AdfsFarm -CertificateThumbprint 8169c52b4ec6e77eb2ae17f028fe5da4e35c0bed -FederationServiceName fs.corp.contoso.com -GroupServiceAccountIdentifier CONTOSO\GroupAccount01
```

这个示例创建了一个联邦服务器群组中的第一个节点，该群组使用一个由组管理的服务账户（Group Managed Service Account）作为服务账户。在此示例中，为 *CertificateThumbprint* 参数提供了一个证书指纹值。该证书将用作 SSL 证书以及服务通信证书。系统会自动生成自签名证书，这些证书将用于令牌签名和令牌解密过程。如果要指定用于令牌签名和令牌解密的证书，请分别为 *SigningCertificateThumbprint* 和 *DecryptionCertificateThumbprint* 参数提供相应的证书指纹值。

### 示例 3：在联邦服务器集群中创建第一个节点，该集群使用远程计算机上的 SQL Server
```
PS C:\> $fscredential = Get-Credential
PS C:\> Install-AdfsFarm -CertificateThumbprint 8169c52b4ec6e77eb2ae17f028fe5da4e35c0bed -FederationServiceName fs.corp.contoso.com -ServiceAccountCredential $fscredential -SQLConnectionString "Data Source=SQLHost;Integrated Security=True"
```

在联邦服务器群中创建第一个节点，该节点使用位于名为 SQLHost 的远程计算机上的 Microsoft SQL Server 数据库。

在这个例子中，为 *CertificateThumbprint* 参数提供了一个证书指纹值。该证书将用作 SSL 证书以及服务通信证书。用于令牌签名和令牌解密的证书将是自动生成的、自我签名的证书。

要指定用于令牌签名和令牌解密的证书，请为 *SigningCertificateThumbprint* 和 *DecryptionCertificateThumbprint* 参数提供相应的指纹值。

### 示例 4：覆盖 AD FS 配置，并在联合服务器群中创建第一个节点
```
PS C:\> $fscredential = Get-Credential
PS C:\> Install-AdfsFarm -CertificateThumbprint 8169c52b4ec6e77eb2ae17f028fe5da4e35c0bed -FederationServiceName fs.corp.contoso.com -ServiceAccountCredential $fscredential -SQLConnectionString "Data Source=SQLHost;Integrated Security=True" -OverwriteConfiguration -SigningCertificateThumbprint 8169c52b4ec6e77eb2ae17f028fe5da4e35c0bed -DecryptionCertificateThumbprint cf2e5064c521d625c8d53536bc98aa8e08f5f2ad
```

此操作会覆盖现有的 AD FS 配置数据库，并在名为 SQLHost 的远程计算机上创建第一个使用 Microsoft SQL Server 数据库的联邦服务器群节点。

在这个例子中，分别使用 *SigningCertificateThumbprint* 和 *DecryptionCertificateThumbprint* 参数为令牌签名证书和令牌加密证书指定了证书指纹值。



## 参数

### -AdminConfiguration (Currently not supported)
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
指定具有执行此操作权限的用户账户所使用的数字公钥（X.509证书）的证书指纹。

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
指定一个 **PSCredential** 对象。

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
指定用于令牌解密的证书的指纹值。如果使用了此参数，则将禁用自动证书轮换功能，并且还必须使用 *SigningCertificateThumbprint* 参数来指定一个用于签名令牌的证书。该值应与本地计算机证书存储中有效证书的指纹相匹配。

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
指定一个显示名称。

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
指定一个联邦服务的名称。

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
指定用于运行 Active Directory Federation Services (AD FS) 服务的组托管服务账户（Group Managed Service Account）。

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
用一个新的数据库替换现有的 AD FS 配置数据库。

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
指定用于运行 AD FS 服务的 Active Directory 账户。

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
指定用于令牌签名的证书的摘要（thumbprint）值。如果使用了此参数，自动证书更新功能将被禁用，并且还需要使用 *DecryptionCertificateThumbprint* 参数来指定一个用于解密令牌的证书。该值应与“本地计算机”证书存储中有效证书的摘要相匹配。

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
指定用于存储 AD FS 配置设置的 SQL Server 数据库。如果未指定，则 AD FS 安装程序会使用 Windows 内部数据库来存储配置设置。

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
指定一个 SSL 端口。

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
指定一个TLS客户端端口。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

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

