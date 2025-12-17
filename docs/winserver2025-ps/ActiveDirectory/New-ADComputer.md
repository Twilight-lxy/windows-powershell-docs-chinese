---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adcomputer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADComputer
---

# 新的AD计算机

## 摘要
创建一个新的 Active Directory 计算机对象。

## 语法

```
New-ADComputer [-WhatIf] [-Confirm] [-AccountExpirationDate <DateTime>] [-AccountNotDelegated <Boolean>]
 [-AccountPassword <SecureString>] [-AllowReversiblePasswordEncryption <Boolean>]
 [-AuthenticationPolicy <ADAuthenticationPolicy>] [-AuthenticationPolicySilo <ADAuthenticationPolicySilo>]
 [-AuthType <ADAuthType>] [-CannotChangePassword <Boolean>] [-Certificates <X509Certificate[]>]
 [-ChangePasswordAtLogon <Boolean>] [-CompoundIdentitySupported <Boolean>] [-Credential <PSCredential>]
 [-Description <String>] [-DisplayName <String>] [-DNSHostName <String>] [-Enabled <Boolean>]
 [-HomePage <String>] [-Instance <ADComputer>] [-KerberosEncryptionType <ADKerberosEncryptionType>]
 [-Location <String>] [-ManagedBy <ADPrincipal>] [-Name] <String> [-OperatingSystem <String>]
 [-OperatingSystemHotfix <String>] [-OperatingSystemServicePack <String>] [-OperatingSystemVersion <String>]
 [-OtherAttributes <Hashtable>] [-PassThru] [-PasswordNeverExpires <Boolean>] [-PasswordNotRequired <Boolean>]
 [-Path <String>] [-PrincipalsAllowedToDelegateToAccount <ADPrincipal[]>] [-SAMAccountName <String>]
 [-Server <String>] [-ServicePrincipalNames <String[]>] [-TrustedForDelegation <Boolean>]
 [-UserPrincipalName <String>] [<CommonParameters>]
```

## 描述
`New-ADComputer` cmdlet 用于创建一个新的 Active Directory 计算机对象。该 cmdlet 不会将计算机加入域中。您可以使用 cmdlet 参数来设置常用的计算机属性值；未与 cmdlet 参数关联的属性值可以通过 `OtherAttributes` 参数进行修改。

您可以使用此cmdlet在计算机加入域之前为其创建一个账户。这些预先创建的计算机对象可用于离线加入域、不安全方式加入域以及通过RODC（远程操作系统目录）加入域的场景中。

`Path` 参数用于指定新计算机的容器或组织单位（OU）。如果不指定 `Path` 参数，该 cmdlet 会在域中计算机对象的默认容器内创建一个计算机账户。

以下方法介绍了使用该cmdlet创建对象的不同方式。

方法1：使用 `New-ADComputer` cmdlet，指定所需的参数，并通过该 cmdlet 的参数来设置任何额外的属性值。

方法 2：使用模板来创建新的对象。为此，可以创建一个新的计算机对象或获取现有计算机对象的副本，并将 *Instance* 参数设置为该对象。提供给 *Instance* 参数的对象将被用作新对象的模板。您可以通过设置 cmdlet 参数来覆盖模板中的属性值。

方法 3：使用 `Import-Csv` cmdlet 与 `Add-ADComputerServiceAccount` cmdlet 来创建多个 Active Directory 计算机对象。具体操作如下：首先使用 `Import-Csv` cmdlet 从包含对象属性列表的逗号分隔值（CSV）文件中导入这些自定义对象；然后通过管道运算符将这些对象传递给 `New-ADComputer` cmdlet，从而生成相应的计算机对象。

## 示例

### 示例 1：在组织单元中创建一个新的计算机账户
```
PS C:\> New-ADComputer -Name "USER02-SRV2" -SamAccountName "USER02-SRV2" -Path "OU=ApplicationServers,OU=ComputerAccounts,OU=Managed,DC=USER02,DC=COM"
```

此命令在以下组织单元（OU）中创建一个新的计算机账户：  
OU=ApplicationServers, OU=ComputerAccounts, OU=Managed, DC=USER02, DC=COM。

### 示例 2：在指定区域内的某个组织单元下创建一个新的计算机账户
```
PS C:\> New-ADComputer -Name "USER01-SRV3" -SamAccountName "USER01-SRV3" -Path "OU=ApplicationServers,OU=ComputerAccounts,OU=Managed,DC=USER01,DC=COM" -Enabled $True -Location "Redmond,WA"
```

此命令会在某个特定的组织单元（OU）下创建一个新的计算机账户，该账户已被启用，并位于华盛顿州的雷德蒙德市。

### 示例 3：根据模板创建一个新的计算机账户
```
PS C:\> $TemplateComp = Get-ADComputer -Name "LabServer-00" -Properties "Location","OperatingSystem","OperatingSystemHotfix","OperatingSystemServicePack","OperatingSystemVersion"
PS C:\> New-ADComputer -Instance $TemplateComp -Name "LabServer-01"
```

这个示例从一个模板对象创建一个新的计算机账户。

## 参数

### -AccountExpirationDate
用于指定账户的过期日期。此参数会设置账户对象的 **AccountExpirationDate** 属性。该属性在轻量级目录访问协议（LDAP）中的显示名称（**ldapDisplayName**）为 “accountExpires”。

在指定此参数时，请使用 **DateTime** 语法。除非另有说明，否则时间默认为当地时间。当未指定时间值时，时间被假设为当天的凌晨 12:00:00（当地时间）。当未指定日期时，日期被假定为当前日期。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AccountNotDelegated
该参数用于指定是否将用户的安全上下文委托给某个服务。当此参数设置为 `true` 时，即使该服务账户被设置为支持 Kerberos 委托的受信任账户，用户的身份验证信息也不会被委托给该服务。此参数会为 Active Directory 账户设置 `AccountNotDelegated` 属性，并同时修改 Active Directory 用户帐户控制（UAC）属性中的 `ADS_UF_NOT_DELEGATED` 标志。该参数的可接受取值包括：

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AccountPassword
Specifies a new password value for an account.
This value is stored as an encrypted string.

The following conditions apply based on the manner in which the password parameter is used:

- $Null password is specified: random password is set and the account is enabled unless it is requested to be disabled.
- No password is specified: random password is set and the account is enabled unless it is requested to be disabled.
- User password is specified: password is set and the account is enabled unless it is requested to be disabled, unless the password you provided does not meet password policy or was not set for other reasons, at which point the account is disabled.

Notes:  Computer accounts, by default, are created with a 240-character random password.
If you provide a password, an attempt is made to set that password.
However, this can fail due to password policy restrictions.
The computer account is created and you can use Set-ADAccountPassword to set the password on that account.
In order to ensure that accounts remain secure, computer accounts will never be enabled unless a valid password is set (either a randomly-generated or user-provided one) or **PasswordNotRequired** is set to $True.

The account is created if the password fails for any reason.

The new **ADComputer** object will always either be disabled or have a user-requested or randomly-generated password.
There is no way to create an enabled computer account object with a password that violates domain password policy, such as an empty password.

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AllowReversiblePasswordEncryption
Specifies whether reversible password encryption is allowed for the account.
This parameter sets the **AllowReversiblePasswordEncryption** property of the account.
This parameter also sets the **ADS_UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED** flag of the Active Directory User Account Control (UAC) attribute.
The acceptable values for this parameter are:

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AuthenticationPolicy
Specifies an Active Directory Domain Services authentication policy object.
Specify the authentication policy object in one of the following formats:

- A distinguished Name
- A GUID
- A name

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

The cmdlet searches the default naming context or partition to find the object.
If the cmdlet finds two or more objects, the cmdlet returns a non-terminating error.

```yaml
Type: ADAuthenticationPolicy
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AuthenticationPolicySilo
Specifies an Active Directory Domain Services authentication policy silo object.
Specify the authentication policy silo object in one of the following formats:

- A distinguished name
- A GUID
- A name

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

The cmdlet searches the default naming context or partition to find the object.
If the cmdlet finds two or more objects, the cmdlet returns a non-terminating error.

```yaml
Type: ADAuthenticationPolicySilo
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AuthType
Specifies the authentication method to use.
The acceptable values for this parameter are:

- Negotiate or 0
- Basic or 1

The default authentication method is Negotiate.

A Secure Sockets Layer (SSL) connection is required for the Basic authentication method.

```yaml
Type: ADAuthType
Parameter Sets: (All)
Aliases:
Accepted values: Negotiate, Basic

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CannotChangePassword
Specifies whether the account password can be changed.
This parameter sets the **CannotChangePassword** property of an account.
The acceptable values for this parameter are:

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Certificates
Specifies the DER-encoded X.509v3 certificates of the account.
These certificates include the public key certificates issued to this account by the Microsoft Certificate Service.
This parameter sets the **Certificates** property of the account object.
The LDAP display name (**ldapDisplayName**) for this property is userCertificate.

```yaml
Type: X509Certificate[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ChangePasswordAtLogon
Specifies whether a password must be changed during the next logon attempt.
The acceptable values for this parameter are:

- $False or 0
- $True or 1

This parameter cannot be set to $True or 1 for an account that also has the **PasswordNeverExpires** property set to $True.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CompoundIdentitySupported
Specifies whether an account supports Kerberos service tickets which includes the authorization data for the user's device.
This value sets the compound identity supported flag of the Active Directory **msDS-SupportedEncryptionTypes** attribute.
The acceptable values for this parameter are:

- $False or 0
- $True or 1

Warning: Domain-joined Windows systems and services such as clustering manage their own **msDS-SupportedEncryptionTypes** attribute.
Therefore any changes to the flag on the **msDS-SupportedEncryptionTypes** attribute is overwritten by the service or system which manages the setting.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
Prompts you for confirmation before running the cmdlet.

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
Specifies the user account credentials to use to perform this task.
The default credentials are the credentials of the currently logged on user unless the cmdlet is run from an Active Directory module for Windows PowerShell provider drive.
If the cmdlet is run from such a provider drive, the account associated with the drive is the default.

To specify this parameter, you can type a user name, such as User1 or Domain01\User01 or you can specify a **PSCredential** object.
If you specify a user name for this parameter, the cmdlet prompts for a password.

You can also create a **PSCredential** object by using a script or by using the **Get-Credential** cmdlet.
You can then set the *Credential* parameter to the **PSCredential** object.

If the acting credentials do not have directory-level permission to perform the task, Active Directory module for Windows PowerShell returns a terminating error.

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

### -Description
Specifies a description of the object.
This parameter sets the value of the **Description** property for the object.
The LDAP display name (**ldapDisplayName**) for this property is description.

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

### -DisplayName
Specifies the display name of the object.
This parameter sets the **DisplayName** property of the object.
The LDAP display name (**ldapDisplayName**) for this property is displayName.

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

### -DNSHostName
Specifies the fully qualified domain name (FQDN) of the computer.
This parameter sets the **DNSHostName** property for a computer object.
The LDAP display name for this property is dNSHostName.

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

### -Enabled
Specifies if an account is enabled.
An enabled account requires a password.
This parameter sets the **Enabled** property for an account object.
This parameter also sets the **ADS_UF_ACCOUNTDISABLE** flag of the Active Directory User Account Control (UAC) attribute.
The acceptable values for this parameter are:

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -HomePage
Specifies the URL of the home page of the object.
This parameter sets the **homePage** property of an Active Directory object.
The LDAP display name (**ldapDisplayName**) for this property is wWWHomePage.

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

### -Instance
Specifies an instance of a computer object to use as a template for a new computer object.

You can use an instance of an existing computer object as a template or you can construct a new computer object by using the Windows PowerShell command line or by using a script.

Method 1: Use an existing computer object as a template for a new object.
To retrieve an instance of an existing computer object use Get-ADComputer.
Then provide this object to the *Instance* parameter of the **New-ADComputer** cmdlet to create a new computer object.
You can override property values of the new object by setting the appropriate parameters.

Method 2: Create a new **ADcomputer** object and set the property values by using the Windows PowerShell command line interface.
Then pass this object to the *Instance* parameter of the **New-ADComputer** cmdlet to create the new Active Directory computer object.

Note: Specified attributes are not validated, so attempting to set attributes that do not exist or cannot be set will raise an error.

```yaml
Type: ADComputer
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -KerberosEncryptionType
Specifies whether an account supports Kerberos encryption types which are used during creation of service tickets.
This value sets the encryption types supported flags of the Active Directory **msDS-SupportedEncryptionTypes** attribute.
The acceptable values for this parameter are:

- None
- DES
- RC4
- AES128
- AES256

None will remove all encryption types from the account which may result in the KDC being unable to issue service tickets for services using the account.

DES is a weak encryption type which is not supported by default since Windows 7 and Windows Server 2008 R2.

Warning: Domain-joined Windows systems and services such as clustering manage their own **msDS-SupportedEncryptionTypes** attribute.
Therefore any changes to the flag on the **msDS-SupportedEncryptionTypes** attribute is overwritten by the service or system which manages the setting.

```yaml
Type: ADKerberosEncryptionType
Parameter Sets: (All)
Aliases:
Accepted values: None, DES, RC4, AES128, AES256

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Location
Specifies the location of the computer, such as an office number.
This parameter sets the **Location** property of a computer.
The LDAP display name (**ldapDisplayName**) of this property is location.

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

### -ManagedBy
Specifies the user or group that manages the object by providing one of the following property values.
Note: The identifier in parentheses is the LDAP display name for the property.
The acceptable values for this parameter are:

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

This parameter sets the Active Directory attribute with an LDAP display name of managedBy.

```yaml
Type: ADPrincipal
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
Specifies the name of the object.
This parameter sets the **Name** property of the Active Directory object.
The LDAP display name (**ldapDisplayName**) of this property is name.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -OperatingSystem
Specifies an operating system name.
This parameter sets the **OperatingSystem** property of the computer object.
The LDAP Display Name (**ldapDisplayName**) for this property is operatingSystem.

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

### -OperatingSystemHotfix
Specifies an operating system hotfix name.
This parameter sets the **operatingSystemHotfix** property of the computer object.
The LDAP display name for this property is operatingSystemHotfix.

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

### -OperatingSystemServicePack
Specifies the name of an operating system service pack.
This parameter sets the **OperatingSystemServicePack** property of the computer object.
The LDAP display name (**ldapDisplayName**) for this property is operatingSystemServicePack.

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

### -OperatingSystemVersion
Specifies an operating system version.
This parameter sets the **OperatingSystemVersion** property of the computer object.
The LDAP display name (**ldapDisplayName**) for this property is operatingSystemVersion.

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

### -OtherAttributes
Specifies object attribute values for attributes that are not represented by cmdlet parameters.
You can set one or more parameters at the same time with this parameter.
If an attribute takes more than one value, you can assign multiple values.
To identify an attribute, specify the LDAP display name (**ldapDisplayName**) defined for it in the Active Directory schema.

Syntax:

To specify a single value for an attribute:

`-OtherAttributes @{'AttributeLDAPDisplayName'=value}`

To specify multiple values for an attribute

`-OtherAttributes @{'AttributeLDAPDisplayName'=value1,value2,...}`

You can specify values for more than one attribute by using semicolons to separate attributes.
The following syntax shows how to set values for multiple attributes:

`-OtherAttributes @{'Attribute1LDAPDisplayName'=value; 'Attribute2LDAPDisplayName'=value1,value2;...}`

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

### -PassThru
Returns an object representing the item with which you are working.
By default, this cmdlet does not generate any output.

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

### -PasswordNeverExpires
Specifies whether the password of an account can expire.
This parameter sets the **PasswordNeverExpires** property of an account object.
This parameter also sets the **ADS_UF_DONT_EXPIRE_PASSWD** flag of the Active Directory User Account Control attribute.
The acceptable values for this parameter are:

- $False or 0
- $True or 1

Note: This parameter cannot be set to $True or 1 for an account that also has the **ChangePasswordAtLogon** property set to $True.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PasswordNotRequired
Specifies whether the account requires a password.
This parameter sets the **PasswordNotRequired** property of an account, such as a user or computer account.
This parameter also sets the **ADS_UF_PASSWD_NOTREQD** flag of the Active Directory User Account Control attribute.
The acceptable values for this parameter are:

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path
Specifies the X.500 path of the Organizational Unit (OU) or container where the new object is created.

In many cases, a default value is used for the *Path* parameter if no value is specified.
The rules for determining the default value are given below.
Note that rules listed first are evaluated first and once a default value can be determined, no further rules are evaluated.

In Active Directory Domain Services environments, a default value for Path is set in the following cases:

- If the cmdlet is run from an Active Directory module for Windows PowerShell provider drive, the parameter is set to the current path of the provider drive.
- If the cmdlet has a default path, this value is used.
For example: in New-ADUser, the *Path* parameter would default to the **Users** container.
- If none of the previous cases apply, the default value of *Path* is set to the default partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for Path is set in the following cases:

- If the cmdlet is run from an Active Directory module for Windows PowerShell provider drive, the parameter is set to the current path of the provider drive.
- If the cmdlet has a default path, this value is used.
For example: in **New-ADUser**, the *Path* parameter would default to the **Users** container.
- If the target AD LDS instance has a default naming context, the default value of *Path* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent (DSA) object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Path* parameter will not take any default value.

Note: The Active Directory Provider cmdlets, such as **New-Item**, **Remove-Item**, **Remove-ItemProperty**, **Rename-Item**, and **Set-ItemProperty**, also contain a *Path* property.
However, for the provider cmdlets, the *Path* parameter identifies the path of the actual object and not the container as with the Active Directory cmdlets.

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

### -PrincipalsAllowedToDelegateToAccount
Specifies the accounts which can act on the behalf of users to services running as this computer account.
This parameter sets the **msDS-AllowedToActOnBehalfOfOtherIdentity** attribute of a computer account object.

```yaml
Type: ADPrincipal[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SAMAccountName
Specifies the Security Account Manager (SAM) account name of the user, group, computer, or service account.
The maximum length of the description is 256 characters.
To be compatible with older operating systems, create a SAM account name that is 15 characters or less.
This parameter sets the **SAMAccountName** for an account object.
The LDAP display name (**ldapDisplayName**) for this property is sAMAccountName.

Note: If the **SAMAccountName** string provided does not end with a $, a $ will be appended if needed.

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

### -Server
Specifies the Active Directory Domain Services instance to connect to, by providing one of the following values for a corresponding domain name or directory server.
The service may be any of the following:  Active Directory Lightweight Domain Services, Active Directory Domain Services or Active Directory snapshot instance.

Specify the Active Directory Domain Services instance in one of the following ways:

Domain name values:

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

The default value for this parameter is determined by one of the following methods in the order that they are listed:

- By using the *Server* value from objects passed through the pipeline
- By using the server information associated with the Active Directory Domain Services Windows PowerShell provider drive, when the cmdlet runs in that drive
- By using the domain of the computer running Windows PowerShell

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

### -ServicePrincipalNames
Specifies the service principal names for the account.
This parameter sets the **ServicePrincipalNames** property of the account.
The LDAP display name (**ldapDisplayName**) for this property is servicePrincipalName.
To enter multiple values, use the following syntax: `<value1>,<value2>,...<valueX>`. If the values contain spaces or otherwise require quotation marks, use the following syntax: `"<value1>","<value2>",..."<valueX>"`."

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TrustedForDelegation
Specifies whether an account is trusted for Kerberos delegation.
A service that runs under an account that is trusted for Kerberos delegation can assume the identity of a client requesting the service.
This parameter sets the **TrustedForDelegation** property of an account object.
This value also sets the **ADS_UF_TRUSTED_FOR_DELEGATION** flag of the Active Directory User Account Control attribute.
The acceptable values for this parameter are:

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -UserPrincipalName
Specifies a user principal name (UPN) in the format `<user>@<DNS-domain-name>`.
A UPN is a friendly name assigned by an administrator that is shorter than the LDAP distinguished name used by the system and easier to remember.
The UPN is independent of the user object's distinguished name, so a user object can be moved or renamed without affecting the user logon name.
When logging on using a UPN, users no longer have to choose a domain from a list on the logon dialog box.

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
Shows what would happen if the cmdlet runs.
The cmdlet is not run.

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
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### 无值或 Microsoft.ActiveDirectory.Management.ADComputer
A computer object that is a template for the new computer object is received by the *Instance* parameter.

## 输出

### 无值或 Microsoft.ActiveDirectory.Management.ADComputer
当指定*PassThru*参数时，会返回一个新的计算机对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* This cmdlet does not work with AD LDS.
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Add-ADComputerServiceAccount](./Add-ADComputerServiceAccount.md)

[Get-ADComputer](./Get-ADComputer.md)

[Get-ADComputerServiceAccount](./Get-ADComputerServiceAccount.md)

[Remove-ADComputer](./Remove-ADComputer.md)

[Remove-ADComputerServiceAccount](./Remove-ADComputerServiceAccount.md)

[Set-ADComputer](./Set-ADComputer.md)

[Set-ADAccountPassword](./Set-ADAccountPassword.md)

[New-ADUser](./New-ADUser.md)

[Windows PowerShell 中的 AD DS 管理 cmdlet](./activedirectory.md)

