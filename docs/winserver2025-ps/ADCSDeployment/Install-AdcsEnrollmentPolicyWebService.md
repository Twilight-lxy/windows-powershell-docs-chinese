---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Deployment.Commands.dll-Help.xml
Module Name: ADCSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsdeployment/install-adcsenrollmentpolicywebservice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-AdcsEnrollmentPolicyWebService
---

# 安装 AdcsEnrollmentPolicyWebService

## 摘要
执行证书注册策略（Certificate Enrollment Policy）Web服务的配置工作。

## 语法

```
Install-AdcsEnrollmentPolicyWebService
 [-AuthenticationType <AuthenticationType>] [-SSLCertThumbprint <String>]
 [-KeyBasedRenewal] [-Force] [-Credential <PSCredential>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Install-AdcsEnrollmentPolicyWebService` cmdlet 用于配置证书注册策略 Web 服务（Certificate Enrollment Policy Web Service）。它还可以在现有安装环境中创建和配置该服务的更多实例。若要删除证书颁发机构（CA）角色服务，请使用 `Uninstall-AdcsEnrollmentPolicyWebService` cmdlet。

你可以通过在 Windows PowerShell 中运行以下命令来导入该 cmdlet：

- `Import-Module ServerManager`
- `Add-WindowsFeature Adcs-Enroll-Web-Pol`

## 示例

### 示例 1：使用 Kerberos 安装证书注册策略 Web 服务

```powershell
$params = @{
    AuthenticationType = Kerberos
    SSLCertThumbprint  = "a909502dd82ae41433e6f83886b00d4277a32a7b"
}
Install-AdcsEnrollmentPolicyWebService @params
```

此命令使用 Kerberos 进行身份验证来安装“证书注册策略Web服务”。有关如何使用 Windows PowerShell 获取证书摘要的信息，请参阅[证书提供程序](https://go.microsoft.com/fwlink/?LinkId=225044)。

### 示例 2：安装证书注册策略 Web 服务，并指定用户名和密码

```powershell
$params = @{
    AuthenticationType = Username
    SSLCertThumbprint  = "a909502dd82ae41433e6f83886b00d4277a32a7b"
}
Install-AdcsEnrollmentPolicyWebService @params
```

该命令用于安装“证书注册策略Web服务”，并指定使用用户名和密码进行身份验证。

### 示例 3：安装证书注册策略Web服务，并指定基于密钥的续期的用户名和密码

```powershell
$params = @{
    AuthenticationType = Username
    SSLCertThumbprint  = "a909502dd82ae41433e6f83886b00d4277a32a7b"
    KeyBasedRenewal    = $true
}
Install-AdcsEnrollmentPolicyWebService @params
```

此命令用于安装“证书注册策略Web服务”，该服务规定使用用户名和密码进行身份验证，并配置证书的基于密钥的续期功能。

## 参数

### -AuthenticationType

指定证书注册策略Web服务所使用的认证类型。该参数的可接受值为：

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

### -Confirm

在运行该cmdlet之前，会提示您确认是否要继续执行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential

指定用于安装“注册策略Web服务”（Enrollment Policy Web Service）的凭据。要获取凭据对象，请使用`Get-Credential` cmdlet。有关更多信息，请输入`Get-Help Get-Credential`。该“注册策略Web服务”必须安装在属于Active Directory Domain Services (AD DS)域的服务器上。安装此服务时，必须使用属于“Domain Admins”组的帐户。

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

### -KeyBasedRenewal

这表示该cmdlet配置了“证书注册策略Web服务”，使其以基于密钥的更新模式运行。基于密钥的更新允许证书客户端使用其现有证书的密钥来进行身份验证，从而续签证书。在基于密钥的更新模式下，该服务只会返回那些设置为支持基于密钥更新的证书模板。

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

用于指定 Internet Information Service (IIS) 所使用的证书的“指纹”（即该证书的唯一标识信息），以便支持所需的安全套接字层/传输层安全协议 (SSL/TLS)。

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

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被执行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.CertificateServices.Deployment.CommonAuthenticationType

### System.String

### System.ManagementAutomation.SwitchParameter

### System.Management.Automation.PSCredential

## 输出

### Microsoft.CertificateServices.Deployment COMMON.CEP.EnrollmentPolicyServiceResult

## 备注

- Ensure you run Windows PowerShell as an administrator. You can use the **Force** parameter to
  bypass the prompt for confirmation. To see parameters, run the following command:
    `Install-AdcsEnrollmentPolicyWebService -?`

- You can get the CA configuration, which is the computer name and CA name by running certutil
  without any parameters. You can see the certificate SSL certificate thumbprints assigned to the
  local computer by running the following commands:
  - `cd cert:\LocalMachine\My`
  - `dir | format-list`

## 相关链接

[卸载 AdcsEnrollmentPolicyWebService](./Uninstall-AdcsEnrollmentPolicyWebService.md)
