---
description: 使用此主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Deployment.Commands.dll-Help.xml
Module Name: ADCSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsdeployment/install-adcsenrollmentwebservice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-AdcsEnrollmentWebService
---

# 安装 AdcsEnrollmentWebService

## 摘要
执行证书注册Web服务的初始配置。

## 语法

### DefaultParameterSet（默认设置）

```
Install-AdcsEnrollmentWebService [-CAConfig <String>]
 [-ApplicationPoolIdentity] [-AuthenticationType <AuthenticationType>]
 [-SSLCertThumbprint <String>] [-RenewalOnly] [-AllowKeyBasedRenewal]
 [-Force] [-Credential <PSCredential>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ServiceAccountParameterSet

```
Install-AdcsEnrollmentWebService [-CAConfig <String>]
-ServiceAccountName <String> -ServiceAccountPassword <SecureString>
[-AuthenticationType <AuthenticationType>] [-SSLCertThumbprint <String>]
[-RenewalOnly] [-AllowKeyBasedRenewal] [-Force] [-Credential <PSCredential>]
[-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Install-AdcsEnrollmentWebService` cmdlet 用于配置证书注册 Web 服务，并可用于在现有安装环境中创建和配置该服务的其他实例。若要卸载证书注册 Web 服务角色服务，请使用 `Uninstall-AdcsEnrollmentWebService` cmdlet。

你可以通过在 Windows PowerShell 中运行以下命令来导入该 cmdlet：

- `Import-Module ServerManager`
- `Add-WindowsFeature Adcs-Enroll-Web-Svc`

## 示例

### 示例 1：安装证书注册 Web 服务以使用该认证机构

```powershell
$params = @{
    ApplicationPoolIdentity = $true
    CAConfig                = "CA1.contoso.com\contoso-CA1-CA"
    SSLCertThumbprint       = "a909502dd82ae41433e6f83886b00d4277a32a7b"
    AuthenticationType      = Certificate
}
Install-AdcsEnrollmentWebService @params
```

此命令用于安装“证书注册Web服务”，以便使用名为`CA1.contoso.com`的计算机以及通用名称为`contoso-CA1-CA`的证书颁发机构（CA）。该“证书注册Web服务”的身份被设置为默认的应用程序池身份。其认证类型基于证书。

### 示例 2：安装证书注册Web服务以使用需要输入密码的认证机构

```powershell
$params = @{
    CAConfig               = "APP1.corp.contoso.com\corp-APP1-CA"
    SSLCertThumbprint      = "a909502dd82ae41433e6f83886b00d4277a32a7b"
    ServiceAccountName     = "Corp\CEPAcct1"
    ServiceAccountPassword = (Read-Host "Set user password" -AsSecureString)
}
Install-AdcsEnrollmentWebService @params
```

此命令用于安装证书注册Web服务，以便该服务能够使用名为`APP1.corp.contoso.com`的计算机以及名为`corp-APP1-CA`的证书颁发机构（CA）进行证书管理。证书注册Web服务的身份标识为`CEPAcct1`，属于`Corp`域名。执行此命令时系统会提示用户输入密码。

## 参数

### -AllowKeyBasedRenewal

表示该cmdlet接受基于密钥的更新请求，这些请求用于注册服务器；所提交的客户端证书可用于身份验证，但这些证书并不直接对应于任何安全主体（security principal）。

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

### -ApplicationPoolIdentity

该参数表示 cmdlet 配置了“证书注册Web服务”，使其在与认证机构（CA）通信时使用应用程序池的身份进行身份验证。此参数仅在“证书注册Web服务”针对远程认证机构（CA）的情况下有效；如果未指定该参数，则会使用本地应用程序池的身份进行身份验证。此外，此参数仅在使用“证书注册Web服务”的第一个实例进行安装时有效；如果是为该服务器上的另一个“证书注册Web服务”实例进行安装，则不应指定此参数。

```yaml
Type: SwitchParameter
Parameter Sets: DefaultParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AuthenticationType

指定认证类型。该参数的可接受值为：

- Certificate
- Kerberos
- UserName

```yaml
Type: AuthenticationType
Parameter Sets: (All)
Aliases:
Accepted values: Kerberos, UserName, Certificate

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CAConfig

指定证书注册Web服务用于处理注册请求的CA（证书颁发机构）的配置字符串。此参数取决于是否安装了本地CA：如果安装了本地CA，则该参数是可选的，在未指定的情况下默认使用本地CA；如果没有本地CA，则必须提供该参数。配置字符串的格式为 `<CAComputerName>\<CACommonName>`，其中 `<CAComputerName>` 表示CA的计算机名称，`<CACommonName>` 表示CA的通用名称。请根据实际情况替换这些占位符。

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

### -Credential

请指定用于安装“证书注册Web服务”（Certificate Enrollment Web Service）的凭据信息。要获取凭据对象，请使用`Get-Credential` cmdlet。有关更多详细信息，请输入`Get-Help Get-Credential`。该“证书注册Web服务”必须安装在属于Active Directory Domain Services (AD DS)域的服务器上。如果配置该服务使用独立的证书颁发机构（Standalone certification authority，简称CA），则需要使用属于该CA服务器上的“本地管理员”（Local Administrators）组的账户；如果配置该服务使用企业级的证书颁发机构（Enterprise CA），则需要使用属于“域管理员”（Domain Admins）组的账户。

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

### -RenewalOnly

表示该 cmdlet 仅支持启用更新模式（即只允许执行与更新相关的操作）。

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

### -SSLCertThumbprint

该参数用于指定网站所使用的 Secure Sockets Layer/Transport Layer Security (SSL/TLS) 证书的哈希值或“指纹”，表示方式为一个字符串。此参数是可选的。如果使用了该参数，它将帮助 Internet Information Server (IIS) 建立必要的绑定关系，从而支持 SSL/TLS 连接功能。如果 IIS 中已存在相应的绑定关系，则指定该参数会覆盖原有的绑定信息；如果没有指定该参数，系统会使用现有的绑定关系。即使没有绑定关系，安装过程仍然会成功完成，但相关服务在手动建立绑定关系之前将无法正常运行。

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

### -ServiceAccountName

指定用于该服务的域账户。输入字符串应采用 `<域名>\帐户名>` 的格式。例如，要指定 `Corp.contoso.com` 域中名为 `WebEnroll` 的账户，您需要输入 `CORP/WebEnroll`。

```yaml
Type: String
Parameter Sets: ServiceAccountParameterSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ServiceAccountPassword

指定用作服务账户的域账户的密码。

```yaml
Type: SecureString
Parameter Sets: ServiceAccountParameterSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.Security.SecuredString

### System.Management.Automation.SwitchParameter

### Microsoft.CertificateServices.Deployment/CommonAuthenticationType

### System.Management.Automation.PSCredential

## 输出

### Microsoft.CertificateServices.DeploymentCommon.CES.EnrollmentServiceResult

## 备注

- Ensure you run Windows PowerShell as an administrator. You can use the **Force** parameter to
  bypass the prompt for confirmation. To see parameters, run the following command:
    `Install-AdcsEnrollmentWebService cmdlet -?`
- You can get the CA configuration, which is the computer name and CA name by running certutil
  without any parameters. You can see the SSL certificate thumbprints assigned to the local computer
  by running the following commands:
  - `cd cert:\LocalMachine\My`
  - `dir | format-list`

## 相关链接

[卸载 AdcsEnrollmentWebService](./Uninstall-AdcsEnrollmentWebService.md)

[Get-Credential](https://go.microsoft.com/fwlink/?LinkID=293936)
