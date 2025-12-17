---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Deployment.Commands.dll-Help.xml
Module Name: ADCSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsdeployment/install-adcscertificationauthority?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-AdcsCertificationAuthority
---

# 安装 AdcsCertificationAuthority

## 摘要
负责安装和配置 Active Directory 证书服务（AD CS）中的“认证机构”（CA）角色服务。

## 语法

### NewKeyParameterSet（默认值）

```
Install-AdcsCertificationAuthority [-AllowAdministratorInteraction]
 [-ValidityPeriod <ValidityPeriod>] [-ValidityPeriodUnits <Int32>]
 [-CACommonName <String>] [-CADistinguishedNameSuffix <String>]
 [-CAType <CAType>] [-CryptoProviderName <String>]
 [-DatabaseDirectory <String>] [-HashAlgorithmName <String>]
 [-IgnoreUnicode] [-KeyLength <Int32>] [-LogDirectory <String>]
 [-OutputCertRequestFile <String>] [-OverwriteExistingCAinDS]
 [-OverwriteExistingKey] [-ParentCA <String>] [-OverwriteExistingDatabase]
 [-Credential <PSCredential>] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ExistingCertificateParameterSet

```
Install-AdcsCertificationAuthority [-AllowAdministratorInteraction]
 [-CertFilePassword <SecureString>] [-CertFile <String>] [-CAType <CAType>]
 [-CertificateID <String>] [-DatabaseDirectory <String>]
 [-LogDirectory <String>] [-OverwriteExistingKey]
 [-OverwriteExistingDatabase] [-Credential <PSCredential>] [-Force]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ExistingKeyParameterSet

```
Install-AdcsCertificationAuthority [-AllowAdministratorInteraction]
 [-ValidityPeriod <ValidityPeriod>] [-ValidityPeriodUnits <Int32>]
 [-CADistinguishedNameSuffix <String>] [-CAType <CAType>]
 [-CryptoProviderName <String>] [-DatabaseDirectory <String>]
 [-HashAlgorithmName <String>] [-IgnoreUnicode] [-KeyContainerName <String>]
 [-LogDirectory <String>] [-OutputCertRequestFile <String>]
 [-OverwriteExistingCAinDS] [-ParentCA <String>]
 [-OverwriteExistingDatabase] [-Credential <PSCredential>] [-Force]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Install-AdcsCertificationAuthority` cmdlet 用于安装和配置 Active Directory 证书服务（AD CS）中的认证机构（CA）角色服务。要删除该认证机构角色服务，请使用 `Uninstall-AdcsCertificationAuthority` cmdlet。

您可以通过在 Windows PowerShell 中运行以下命令来导入该 cmdlet：

- `Install-WindowsFeature Adcs-Cert-Authority`

To include the Certification Authority and Certificate Templates consoles in a CA installation, you
must use the **IncludeManagementTools** parameter at the end of the
`Install-WindowsFeature Adcs-Cert-Authority` command.

在 [.NET Framework](/dotnet/csharp/language-reference/builtin-types/built-in-types)中，`Int` 相当于 `Int32`。

## 示例

#### 示例 1：安装一个新的独立根证书颁发机构（Root CA），并使用默认设置

```powershell
Install-AdcsCertificationAuthority -CAType StandaloneRootCa
```

此命令会安装一个新的独立根证书颁发机构（Root CA），并使用默认设置。

### 示例 2：使用特定的提供商和密钥长度安装新的企业根证书颁发机构（Enterprise Root CA）

```powershell
$params = @{
    CAType             = EnterpriseRootCa
    CryptoProviderName = "ECDSA_P256#Microsoft Software Key Storage Provider"
    KeyLength          = 256
    HashAlgorithmName  = SHA256
}
Install-AdcsCertificationAuthority @params
```

此命令使用名为“ECDSA_P256 Microsoft Software Key Storage Provider”的提供者来安装一个新的企业根证书颁发机构（Enterprise Root CA），该提供者的密钥长度为256位，使用的哈希算法为SHA-256。

### 示例 3：使用特定的提供商和有效期来安装新的企业根证书颁发机构（Enterprise Root CA）

```powershell
$params = @{
    CAType              = EnterpriseRootCa
    CryptoProviderName  = "RSA#Microsoft Software Key Storage Provider"
    KeyLength           = 2048
    HashAlgorithmName   = SHA1
    ValidityPeriod      = Years
    ValidityPeriodUnits = 3
}
Install-AdcsCertificationAuthority @params
```

此命令使用名为“Microsoft Software Key Storage Provider”的提供者，安装一个新的企业级根证书颁发机构（Enterprise Root CA）。该证书采用RSA算法进行加密，密钥长度为2048位，哈希算法为SHA-1，有效期为三年。

### 示例 4：使用上级证书颁发机构（CA）安装新的企业级从属证书颁发机构

```powershell
$params = @{
    CAType   = EnterpriseSubordinateCa
    ParentCA = "SERVER75.corp.contoso.com\SERVER75-CA"
}
Install-AdcsCertificationAuthority @params
```

此命令用于安装一个新的企业级从属CA（Certificate Authority，证书颁发机构）。该从属CA的父CA是`SERVER75`，位于Contoso.com公司的CORP域名域内。

### 示例 5：使用现有的证书安装一个新的企业级从属CA（Certificate Authority）

```powershell
$params = @{
    CAType           = EnterpriseSubordinateCa
    CertFile         = "C:\Cert\SERVER80-CA.p12"
    CertFilePassword = (Read-Host "Set user password" -AsSecureString)
}
Install-AdcsCertificationAuthority @params
```

此命令使用一个来自PFX/P12文件的现有证书来安装企业级从属CA（Enterprise Subordinate CA）。该证书位于本地`C:\Cert`文件夹中，文件名为`SERVER80-CA.p12`。

## 参数

### -AllowAdministratorInteraction

这表示该cmdlet在访问私钥时启用提示功能。对于Microsoft的所有默认提供程序来说，这一功能都不是必需的。对于增强型安全组件（如硬件安全模块（HSM）），请查阅相关供应商提供的文档以获取更多信息。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CACommonName

指定认证机构的通用名称。

```yaml
Type: String
Parameter Sets: NewKeyParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CADistinguishedNameSuffix

指定认证机构的可分辨名称后缀。

```yaml
Type: String
Parameter Sets: NewKeyParameterSet, ExistingKeyParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CAType

指定此 cmdlet 安装的证书颁发机构的类型。该参数的可接受值包括：

- EnterpriseRootCA
- EnterpriseSubordinateCA
- StandaloneRootCA
- StandaloneSubordinateCA

```yaml
Type: CAType
Parameter Sets: (All)
Aliases:
Accepted values: EnterpriseRootCA, EnterpriseSubordinateCA, StandaloneRootCA, StandaloneSubordinateCA

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CertFile

指定证书颁发机构（CA）生成的PKCS #12格式证书文件的文件名。

```yaml
Type: String
Parameter Sets: ExistingCertificateParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CertFilePassword

指定用于认证机构证书文件的密码。

```yaml
Type: SecureString
Parameter Sets: ExistingCertificateParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CertificateID

指定证书颁发机构证书的指纹（thumbprint）或序列号（serial number）。

```yaml
Type: String
Parameter Sets: ExistingCertificateParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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

### -Credential

用于指定一个 **PSCredential** 对象，以便连接到 Active Directory Domain Services (AD DS)。要获取该凭据对象，请使用 `Get-Credential` cmdlet。有关更多信息，请输入 `Get-Help Get-Credential`。  

- 要安装企业级证书颁发机构（Enterprise Certification Authority），计算机必须加入 AD DS 域，并且需要一个属于 “Enterprise Admin” 组的用户账户。  
- 要安装独立的证书颁发机构，计算机可以处于工作组或 AD DS 域中；如果计算机位于工作组中，则需要一个属于 “Administrators” 组的用户账户；如果计算机位于 AD DS 域中，则需要一个属于 “Domain Admins” 组的用户账户。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CryptoProviderName

指定用于生成或存储证书颁发机构（CA）私钥的加密服务提供商（CSP）或密钥存储提供商（KSP）的名称。

```yaml
Type: String
Parameter Sets: NewKeyParameterSet, ExistingKeyParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DatabaseDirectory

指定证书颁发机构数据库所在的文件夹位置。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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

### -HashAlgorithmName

指定证书颁发机构使用的签名哈希算法。

```yaml
Type: String
Parameter Sets: NewKeyParameterSet, ExistingKeyParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IgnoreUnicode

表示该cmdlet允许在证书颁发机构名称字符串中使用Unicode字符。

```yaml
Type: SwitchParameter
Parameter Sets: NewKeyParameterSet, ExistingKeyParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -KeyContainerName

指定一个现有私有密钥容器的名称。

```yaml
Type: String
Parameter Sets: ExistingKeyParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -KeyLength

指定新证书颁发机构（CA）密钥的位长度。

```yaml
Type: Int32
Parameter Sets: NewKeyParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LogDirectory

指定证书颁发机构数据库日志的文件夹位置。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -OutputCertRequestFile

指定证书请求文件的文件夹位置。

```yaml
Type: String
Parameter Sets: NewKeyParameterSet, ExistingKeyParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -OverwriteExistingCAinDS

表示该cmdlet会用具有相同计算机名称的对象来覆盖Active Directory域服务（AD DS）域中的相应计算机对象。

```yaml
Type: SwitchParameter
Parameter Sets: NewKeyParameterSet, ExistingKeyParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -OverwriteExistingDatabase

表示该cmdlet会覆盖现有的证书颁发机构数据库。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -OverwriteExistingKey

表示该cmdlet会用具有相同名称的新键容器覆盖现有的键容器。

```yaml
Type: SwitchParameter
Parameter Sets: NewKeyParameterSet, ExistingCertificateParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ParentCA

指定用于认证此证书颁发机构（CA）的父证书颁发机构的配置字符串。

```yaml
Type: String
Parameter Sets: NewKeyParameterSet, ExistingKeyParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ValidityPeriod

指定证书颁发机构（CA）证书的有效期，单位可以是小时、天、周、月或年。如果这是一个从属的CA（即由上级CA管理的CA），则不要使用此参数，因为其有效期由上级CA决定。

```yaml
Type: ValidityPeriod
Parameter Sets: NewKeyParameterSet, ExistingKeyParameterSet
Aliases:
Accepted values: Hours, Days, Weeks, Months, Years

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ValidityPeriodUnits

指定CA证书的有效期。如果这是一个从属CA，则不要设置此参数，因为其有效期由父CA决定。

```yaml
Type: Int32
Parameter Sets: NewKeyParameterSet, ExistingKeyParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf

展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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

### System.ManagementAutomation.SwitchParameter

### System.Security.SecureString

### System.String

### Microsoft.CertificateServices.Deployment(Common.CA ValidityPeriod

### System.Int32

### Microsoft.CertificateServices.Deployment.Common.CA.CAType

### System.Management.Automation.PSCredential

## 输出

### Microsoft.CertificateServices.Deployment(Common.CA.CertificationAuthoritySetupResult

## 备注

- Ensure you run Windows PowerShell as an administrator. You can use the **force** parameter to
  bypass the prompt for confirmation. To see parameters, run the following command:

      `Install-AdcsCertificationAuthority -?`
- If you have installation issues, try using the **verbose** parameter to get verbose output and
  review the information in the %windir%\cerocm.log file.

## 相关链接

[卸载 AdcsCertificationAuthority](./Uninstall-AdcsCertificationAuthority.md)
