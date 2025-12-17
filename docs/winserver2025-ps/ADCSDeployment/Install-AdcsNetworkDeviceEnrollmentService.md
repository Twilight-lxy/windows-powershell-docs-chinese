---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Deployment.Commands.dll-Help.xml
Module Name: ADCSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsdeployment/install-adcsnetworkdeviceenrollmentservice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-AdcsNetworkDeviceEnrollmentService
---

# 安装 AdcsNetworkDeviceEnrollmentService

## 摘要
安装NDES角色服务。

## 语法

### DefaultParameterSet（默认值）

```
Install-AdcsNetworkDeviceEnrollmentService [-ApplicationPoolIdentity]
 [-RAName <String>] [-RAEmail <String>]  [-RACompany <String>]
 [-RADepartment <String>] [-RACity <String>] [-RAState <String>]
 [-RACountry <String>]  [-SigningProviderName <String>]
 [-SigningKeyLength <Int32>] [-EncryptionProviderName <String>]
 [-EncryptionKeyLength <Int32>] [-CAConfig <String>] [-Force]
 [-Credential <PSCredential>] [-WhatIf] [-Confirm]  [<CommonParameters>]
```

### ServiceAccountParameterSet

```
Install-AdcsNetworkDeviceEnrollmentService -ServiceAccountName <String>
 -ServiceAccountPassword <SecureString> [-RAName <String>]
 [-RAEmail <String>] [-RACompany <String>] [-RADepartment <String>]
 [-RACity <String>] [-RAState <String>] [-RACountry <String>]
 [-SigningProviderName <String>] [-SigningKeyLength <Int32>]
 [-EncryptionProviderName <String>] [-EncryptionKeyLength <Int32>]
 [-CAConfig <String>] [-Force] [-Credential <PSCredential>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Install-AdcsNetworkDeviceEnrollmentService` cmdlet 用于配置网络设备注册服务（Network Device Enrollment Service，简称 NDES）的角色服务。

要删除 NDES 角色服务，请使用 `Uninstall-AdcsNetworkDeviceEnrollmentService` cmdlet。

你可以通过在 Windows PowerShell 中运行以下命令来导入该 cmdlet：

- `Import-Module ServerManager`
- `Add-WindowsFeature Adcs-Device-Enrollment`

在[.NET Framework]中，`Int`等同于`Int32`（参见：https://msdn.microsoft.com/en-us/library/ya5y69ds.aspx）。

## 示例

### 示例 1：显示默认的 NDES 设置

```powershell
Install-AdcsNetworkDeviceEnrollmentService -ApplicationPoolIdentity -WhatIf
```

这个命令会显示默认的NDES设置信息；如果NDES被安装的话，这些设置将会被应用到系统中。

### 示例 2：使用服务账户名称和密码显示默认的 NDES 设置

```powershell
$params = @{
    ServiceAccountName     = "CONTOSO\svcNDES"
    ServiceAccountPassword = (Read-Host "Set user password" -AsSecureString)
    WhatIf                 = $true
}
Install-AdcsNetworkDeviceEnrollmentService @params
```

此命令用于在 NDES 使用服务账户时显示默认设置，而不会对配置进行任何修改。该命令使用名为 `CONTOSO\svcNDES` 的服务账户，该账户是本地计算机 `IIS_USRS` 组的成员。

### 示例 3：使用应用程序池身份安装 NDES

```powershell
$params = @{
    ApplicationPoolIdentity = $true
    CAConfig                = "<CAComputerName>\<CACommonName>"
}
Install-AdcsNetworkDeviceEnrollmentService @params
```

此命令使用应用程序池的身份来安装 NDES，并利用由 CA 服务器 `<CAComputerName>\<CACommonName>` 指定的远程 CA（证书颁发机构）进行身份验证。请将 `<CAComputerName>` 和 `<CACommonName>` 替换为实际的 CA 服务器名称和通用名称。

### 示例 4：使用特定的服务账户安装 NDES

```powershell
$params = @{
    ServiceAccountName     = "CONTOSO\svcNDES"
    ServiceAccountPassword = (Read-Host "Set user password" -AsSecureString)
    CAConfig               = "CAComputerName\CAName"
    RAName                 = "Contoso-NDES-RA"
    RACountry              = "US"
    RACompany              = "Contoso"
    SigningProviderName    = "Microsoft Strong Cryptographic Provider"
    SigningKeyLength       = 4096
    EncryptionProviderName = "Microsoft Strong Cryptographic Provider"
    EncryptionKeyLength    = 4096
}
Install-AdcsNetworkDeviceEnrollmentService @params
```

该命令使用一个名为 `CONTOSO\svcNDES` 的服务账户来安装 NDES，该账户是本地计算机上的 `IIS_USRS` 组的成员。此外，该命令还指定了几个非默认参数。

## 参数

### -ApplicationPoolIdentity

该参数表示网络设备注册服务（Network Device Enrollment Service，简称NDES）在与证书颁发机构（Certificate Authority，简称CA）通信时所使用的身份信息。只有当NDES使用远程CA时，此参数才有效；如果CA是本地的，则无法使用应用程序池的身份账户。

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

### -CAConfig

指定网络设备注册服务（Network Device Enrollment Service）所使用的远程证书颁发机构（CA）。当该参数与 **ApplicationPoolIdentity** 参数一起使用时，它是必需的。如果已安装了本地证书颁发机构，则请不要使用此参数。

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

在运行 cmdlet 之前会提示您进行确认。

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

指定一个 `PSCredential` 对象，该对象用于此 cmdlet 连接到 NDES 角色服务。要获取凭据对象，请使用 `Get-Credential` cmdlet。有关更多信息，请输入 `Get-Help Get-Credential`。NDES 必须安装在属于 Active Directory 域服务 (AD DS) 域的服务器上。如果 NDES 配置为使用独立 CA（Standalone CA），则需要使用属于该 CA 的本地管理员组 (Local Administrators) 的账户；如果 NDES 配置为使用企业级 CA (Enterprise CA)，则需要使用属于域管理员组 (Domain Admins) 的账户。

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

### -EncryptionKeyLength

指定加密密钥的长度。如果您在安装过程中使用现有的密钥，则此选项无效。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EncryptionProviderName

指定加密提供商的名称，例如加密服务提供商（CSP）的名称。

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

强制命令运行，而不会询问用户确认。

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

### -RACity

指定注册机构所在的城市。

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

### -RACompany

指定注册机构所代表的组织或公司。

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

### -RACountry

指定注册机构所在的国家/地区。

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

### -RADepartment

指明了注册机构的所属部门。

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

### -RAEmail

指定注册机构的电子邮件地址。

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

### -RAName

指定 NDES 注册机构的名称。

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

### -RAState

指定注册机构所处的州或省（即地理政治边界），如适用的话。

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

指定网络设备注册服务（Network Device Enrollment Service）所使用的账户名称。

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

指定网络设备注册服务（Network Device Enrollment Service）所使用的服务账户的密码。

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

### -SigningKeyLength

指定签名密钥的长度。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SigningProviderName

指定签名设备的名称。

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

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.ManagementAutomation.SwitchParameter

### System.String

### System.Security.SecureString

### System.Int32

### System.Management.Automation.PSCredential

## 输出

### Microsoft.CertificateServices.Deployment.Common.NDES.NetworkDeviceEnrollmentServiceResult

## 备注

- Ensure you run Windows PowerShell as an administrator. You can use the **Force** parameter to bypass
  the prompt for confirmation. To see parameters, run the following command:

    `Install-AdcsNetworkDeviceEnrollmentService -?`

## 相关链接

[卸载 AdcsNetworkDeviceEnrollmentService](./Uninstall-AdcsNetworkDeviceEnrollmentService.md)

[使用 Get-Credential 命令获取凭据](https://go.microsoft.com/fwlink/?LinkID=293936)
