---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 02/15/2024
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adserviceaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADServiceAccount
---

# 新的 ADService 账户

## 摘要
创建一个新的 Active Directory 管理服务账户或组管理服务账户对象。

## 语法

### 组（默认设置）

```
New-ADServiceAccount [-WhatIf] [-Confirm] [-AccountExpirationDate <DateTime>]
 [-AccountNotDelegated <Boolean>] [-AuthenticationPolicy <ADAuthenticationPolicy>]
 [-AuthenticationPolicySilo <ADAuthenticationPolicySilo>] [-AuthType <ADAuthType>]
 [-Certificates <String[]>] [-CompoundIdentitySupported <Boolean>] [-Credential <PSCredential>]
 [-Description <String>] [-DisplayName <String>] -DNSHostName <String> [-Enabled <Boolean>]
 [-HomePage <String>] [-Instance <ADServiceAccount>]
 [-KerberosEncryptionType <ADKerberosEncryptionType>] [-ManagedPasswordIntervalInDays <Int32>]
 [-Name] <String> [-OtherAttributes <Hashtable>] [-PassThru] [-Path <String>]
 [-CreateDelegatedServiceAccount] [-PrincipalsAllowedToDelegateToAccount <ADPrincipal[]>]
 [-PrincipalsAllowedToRetrieveManagedPassword <ADPrincipal[]>] [-SamAccountName <String>]
 [-Server <String>] [-ServicePrincipalNames <String[]>] [-TrustedForDelegation <Boolean>]
 [<CommonParameters>]
```

### 仅限单台计算机使用

```
New-ADServiceAccount [-WhatIf] [-Confirm] [-AccountExpirationDate <DateTime>]
 [-AccountNotDelegated <Boolean>] [-AccountPassword <SecureString>]
 [-AuthenticationPolicy <ADAuthenticationPolicy>]
 [-AuthenticationPolicySilo <ADAuthenticationPolicySilo>] [-AuthType <ADAuthType>]
 [-Certificates <String[]>] [-Credential <PSCredential>] [-Description <String>]
 [-DisplayName <String>] [-Enabled <Boolean>] [-HomePage <String>] [-Instance <ADServiceAccount>]
 [-KerberosEncryptionType <ADKerberosEncryptionType>] [-Name] <String>
 [-OtherAttributes <Hashtable>] [-PassThru] [-Path <String>] [-RestrictToSingleComputer]
 [-SamAccountName <String>] [-Server <String>] [-ServicePrincipalNames <String[]>]
 [-TrustedForDelegation <Boolean>] [<CommonParameters>]
```

### 只允许使用外出身份验证（RestrictedToOutboundAuthenticationOnly）

```
New-ADServiceAccount [-WhatIf] [-Confirm] [-AccountExpirationDate <DateTime>]
 [-AccountNotDelegated <Boolean>] [-AuthenticationPolicy <ADAuthenticationPolicy>]
 [-AuthenticationPolicySilo <ADAuthenticationPolicySilo>] [-AuthType <ADAuthType>]
 [-Certificates <String[]>] [-Credential <PSCredential>] [-Description <String>]
 [-DisplayName <String>] [-Enabled <Boolean>] [-HomePage <String>] [-Instance <ADServiceAccount>]
 [-KerberosEncryptionType <ADKerberosEncryptionType>] [-Name] <String>
 [-OtherAttributes <Hashtable>] [-PassThru] [-Path <String>]
 [-RestrictToOutboundAuthenticationOnly] [-SamAccountName <String>] [-Server <String>]
 [-ServicePrincipalNames <String[]>] [-TrustedForDelegation <Boolean>] [<CommonParameters>]
```

## 描述

`New-ADServiceAccount` cmdlet 用于创建一个新的 Active Directory 管理服务账户。默认情况下，该 cmdlet 创建的是一个组管理服务账户。若要创建一个委托管理的服务账户，请使用 **CreateDelegatedServiceAccount** 参数。委托管理的服务账户可用于迁移那些原本需要普通用户账户来运行的服务。如果要创建一个与特定计算机关联的独立管理服务账户，请使用 **RestrictToSingleComputer** 参数；若要创建一个仅能在客户端角色中使用的组管理服务账户，则使用 **RestrictToOutboundAuthenticationOnly** 参数——这种类型的账户只能用于出站连接，任何尝试使用该账户连接到服务的操作都会失败（因为该账户缺乏必要的身份验证信息）。您可以通过 cmdlet 的参数来设置常用的管理服务账户属性值；而那些未与 cmdlet 参数关联的属性值，则可以通过 **OtherAttributes** 参数进行配置。

`Path` 参数用于指定新托管服务账户对象的容器或组织单位（Organizational Unit，简称 OU）。当不指定 `Path` 参数时，该cmdlet会在域中的默认托管服务账户容器中创建该对象。

以下方法介绍了使用该cmdlet创建对象的不同方式。

- Method 1: Use the `New-ADServiceAccount` cmdlet, specify the required parameters, and set any
  additional property values by using the cmdlet parameters.

- Method 2: Use a template to create the new object. To do this, create a new managed service
  account object or retrieve a copy of an existing managed service account object and set the
  **Instance** parameter to this object. The object provided to the **Instance** parameter is used
  as a template for the new object. You can override property values from the template by setting
  cmdlet parameters. For examples and more information, see the **Instance** parameter description
  for this cmdlet.

- Method 3: Use the `Import-Csv` cmdlet with the `New-ADServiceAccount` cmdlet to create
  multiple Active Directory managed service account objects. To do this, use the `Import-CSV`
  cmdlet to create the custom objects from a comma-separated value (CSV) file that contains a list
  of object properties. For more information, type `Get-Help Import-CSV`. Then pass these objects
  through the pipeline to the `New-ADServiceAccount` cmdlet to create the managed service account
  objects.

## 示例

### 示例 1：创建一个已启用的托管服务账户

```powershell
New-ADServiceAccount -Name "Service01" -DNSHostName "Service01.contoso.com" -Enabled $True
```

此命令会在 Active Directory 域服务（AD DS）中创建一个已启用的托管服务账户。

### 示例 2：创建一个托管服务账户并注册其服务主体名称

```powershell
$params = @{
    Name = "Service01"
    ServicePrincipalNames = "MSSQLSVC/Machine3.corp.contoso.com"
    DNSHostName = "Service01.contoso.com"
}
New-ADServiceAccount @params
```

此命令创建一个托管服务账户，并注册其服务主体名称（service principal name）。

### 示例 3：为单台计算机创建一个托管服务账户

```powershell
New-ADServiceAccount -Name "Service01" -RestrictToSingleComputer
```

此命令创建一个托管服务账户，并将其使用限制在单台计算机上。

### 示例 4：仅创建用于出站身份验证的管理服务账户

```powershell
New-ADServiceAccount -Name "Service01" -RestrictToOutboundAuthenticationOnly
```

这个命令创建了一个托管服务账户，并将其用途限制为仅用于外出身份验证（即从该账户发起的身份验证请求）。

### 示例 5：创建一个新的托管服务账户，并注册多个服务主体名称

```powershell
$params = @{
    Name = "Service01"
    ServicePrincipalNames = "HTTP/Machine3.corp.contoso.com","HTTP/Machine3.corp.contoso.com/contoso"
    DNSHostName = "Service01.contoso.com"
}
New-ADServiceAccount @params
```

此命令创建一个委托管理的服务账户。

### 示例 6：创建一个已启用的委托管理服务账户，用于迁移操作

```powershell
$params = @{
    Name = "Service01"
    DNSHostName = "Service01.contoso.com"
    Enabled = $True
    CreateDelegatedServiceAccount = $True
}
New-ADServiceAccount @params
```

## 参数

### -AccountExpirationDate

用于指定账户的到期日期。此参数会设置账户对象的 **AccountExpirationDate** 属性。该属性在 LDAP 显示名称（**ldapDisplayName**）中的显示方式为 “accountExpires”。

在指定此参数时，请使用 **DateTime** 的语法。除非另有说明，否则时间默认为本地时间。如果没有指定时间值，则时间默认为当天的凌晨 12:00:00（本地时间）。如果没有指定日期，则日期默认为当前日期。

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

该参数用于指示用户的安全上下文是否被委托给某个服务。当此参数设置为 `true` 时，即使服务账户已被配置为支持 Kerberos 委托功能，用户的账户安全上下文也不会被委托给该服务。该参数会为 Active Directory 账户设置 `AccountNotDelegated` 属性，并同时修改 Active Directory 用户账户控制（UAC）属性中的 `ADS_UF_NOT_DELEGATED` 标志。

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

为服务账户指定一个新的密码值。该密码值以加密字符串的形式存储。

以下条件根据密码参数的使用方式而适用：

- $Null password is specified. Random password is set and the account is enabled unless it's
  requested to be disabled.
- No password is specified. Random password is set and the account is enabled unless it's
  requested to be disabled.
- User password is specified. Password is set and the account is enabled unless it's requested to
  be disabled, unless the password you provided doesn't meet password policy or was not set for
  other reasons, at which point the account is disabled.

新的 **ADServiceAccount** 对象要么处于禁用状态，要么使用由用户指定的密码或随机生成的密码。无法创建一个启用的服务账户对象，并且该对象的密码不能违反域的密码策略（例如，不能使用空密码）。

```yaml
Type: SecureString
Parameter Sets: RestrictedToSingleComputer
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AuthenticationPolicy

指定一个 Active Directory 域服务（Active Directory Domain Services）身份验证策略对象。请使用以下格式之一来指定该身份验证策略对象：

- Distinguished name
- GUID
- Name

This parameter can also get this object through the pipeline or you can set this parameter to an
object instance.

The cmdlet searches the default naming context or partition to find the object. If the cmdlet finds
two or more objects, the cmdlet returns a non-terminating error.

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

Specifies an Active Directory Domain Services authentication policy silo object. Specify the
authentication policy silo object in one of the following formats:

- Distinguished name
- GUID
- Name

This parameter can also get this object through the pipeline or you can set this parameter to an
object instance.

The cmdlet searches the default naming context or partition to find the object. If the cmdlet finds
two or more objects, the cmdlet returns a non-terminating error.

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

Specifies the authentication method to use. The acceptable values for this parameter are:

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

### -Certificates

指定一个证书数组。此 cmdlet 会修改与该账户关联的、采用 DER 编码格式的 X.509v3 证书。这些证书包括由 Microsoft Certificate Service 颁发给该账户的公钥证书。该参数用于设置账户对象的 **Certificates** 属性，其 LDAP 显示名称（**ldapDisplayName**）为 userCertificate。

要添加值：

`-Certificates @{Add=value1,value2,...}`

要删除某些值：

`-Certificates @{Remove=value3,value4,...}`

要替换值：

`-Certificates @{Replace=value1,value2,...}`

要清除所有值：

`-Certificates $Null`

您可以使用由分号分隔的列表来指定多个操作。例如，使用以下语法来添加和删除证书值：

`-Certificates @{Add=value1,value2,...};@{Remove=value3,value4,...}`

操作符按照以下顺序应用：

- Remove
- Add
- Replace

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

### -CompoundIdentitySupported

Indicates whether an account supports Kerberos service tickets which includes the authorization
data for the user's device. This value sets the compound identity supported flag of the Active
Directory `msDS-SupportedEncryptionTypes` attribute. The acceptable values for this parameter
are:

- $False or 0
- $True or 1

Warning: Domain-joined Windows systems and services such as clustering manage their own
`msDS-SupportedEncryptionTypes` attribute. Therefore any changes to the flag on the
`msDS-SupportedEncryptionTypes` attribute will be overwritten by the service or system which
manages the setting.

```yaml
Type: Boolean
Parameter Sets: Group
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

Specifies the service account credentials to use to perform this task. The default credentials are
the credentials of the currently logged on user unless the cmdlet is run from an Active Directory
PowerShell provider drive. If the cmdlet is run from such a provider drive, the account associated
with the drive is the default.

To specify this parameter, you can type an administrative account name, such as `Admin1` or
`Contoso\Admin1` or you can specify a **PSCredential** object. If you specify a service account name
for this parameter, the cmdlet prompts for a password.

You can also create a **PSCredential** object by using a script or by using the `Get-Credential`
cmdlet. You can then set the *Credential* parameter to the **PSCredential** object.

If the acting credentials don't have directory-level permission to perform the task, Active
Directory PowerShell returns a terminating error.

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

Specifies a description of the object. This parameter sets the value of the **Description**
property for the object. The LDAP Display Name (**ldapDisplayName**) for this property is
description.

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

Specifies the display name of the object. This parameter sets the **DisplayName** property of the
object. The LDAP Display Name (**ldapDisplayName**) for this property is displayName.

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

Specifies the DNS host name of Service Account.

```yaml
Type: String
Parameter Sets: Group
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Enabled

Indicates whether an account is enabled. An enabled account requires a password. This parameter
sets the **Enabled** property for an account object. This parameter also sets the
**ADS_UF_ACCOUNTDISABLE** flag of the Active Directory UAC attribute.

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

Specifies the URL of the home page of the object. This parameter sets the **homePage** property of
an Active Directory object. The LDAP Display Name (**ldapDisplayName**) for this property is
wWWHomePage.

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

Specifies an instance of a service account object to use as a template for a new service account
object.

You can use an instance of an existing service account object as a template or you can construct a
new service account object for template use. You can construct a new service account using the
Windows PowerShell command line or by using a script.

Note: Specified attributes aren't validated, so attempting to set attributes that Don�t exist or
can't be set raises an error.

```yaml
Type: ADServiceAccount
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -KerberosEncryptionType

Indicates whether an account supports Kerberos encryption types which are used during creation of
service tickets. This value sets the encryption types supported flags of the Active Directory
`msDS-SupportedEncryptionTypes` attribute. The acceptable values for this parameter are:

- None
- DES
- RC4
- AES128
- AES256

None will remove all encryption types from the account may result in the KDC being unable to issue
service tickets for services using the account.

DES is a weak encryption type that'sn't supported by default since Windows 7 and Windows Server
2008 R2.

Warning: Domain-joined Windows systems and services such as clustering manage their own
`msDS-SupportedEncryptionTypes` attribute. Therefore any changes to the flag on the
`msDS-SupportedEncryptionTypes` attribute will be overwritten by the service or system which
manages the setting.

```yaml
Type: ADKerberosEncryptionType
Parameter Sets: (All)
Aliases:
Accepted values: None, DES, RC4, AES128, AES256

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagedPasswordIntervalInDays

Specifies the number of days for the password change interval. If set to 0 then the default is
used. This can only be set on object creation. After that the setting is read only. This value
returns the `msDS-ManagedPasswordInterval` of the group managed service account object.

```yaml
Type: Int32
Parameter Sets: Group
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name

Specifies the name of the object. This parameter sets the **Name** property of the Active Directory
object. The LDAP Display Name (**ldapDisplayName**) of this property is name.

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

### -OtherAttributes

Specifies object attribute values for attributes that aren't represented by cmdlet parameters. You
can set one or more parameters at the same time with this parameter. If an attribute takes more
than one value, you can assign multiple values. To identify an attribute, specify the LDAP Display
Name (**ldapDisplayName**) defined for it in the Active Directory schema.

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

Returns an object representing the item with which you're working. By default, this cmdlet does
not generate any output.

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

### -Path

Specifies the X.500 path of the organizational unit (OU) or container where the new object is
created.

In many cases, a default value will be used for the **Path** parameter if no value is specified.
The rules for determining the default value are given below. Note that rules listed first are
evaluated first and once a default value can be determined, no further rules are evaluated.

In AD DS environments, a default value for **Path** is set in the following cases:

- If the cmdlet is run from an Active Directory PowerShell provider drive, the parameter is set to
  the current path of the provider drive.
- If the cmdlet has a default path, this is used.
  For example: in `New-ADUser`, the **Path** parameter defaults to the Users container.
- If none of the previous cases apply, the default value of **Path** is set to the default
  partition or naming context of the target domain.

In AD LDS environments, a default value for **Path** is set in the following cases:

- If the cmdlet is run from an Active Directory PowerShell provider drive, the parameter is set to
  the current path of the provider drive.
- If the cmdlet has a default path, this is used.
  For example: in `New-ADUser`, the **Path** parameter defaults to the Users container.
- If the target AD LDS instance has a default naming context, the default value of **Path** is set
  to the default naming context. To specify a default naming context for an AD LDS environment, set
  the `msDS-defaultNamingContext` property of the Active Directory directory service agent object
  (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the **Path** parameter doesn't take any default value.

Note: The Active Directory Provider cmdlets, such as `New-Item`, `Remove-Item`,
`Remove-ItemProperty`, `Rename-Item`, and `Set-ItemProperty`, also contain a **Path**
property. However, for the provider cmdlets, the **Path** parameter identifies the path of the
actual object and not the container as with the Active Directory cmdlets.

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

Specifies the accounts that can act on the behalf of users to services running as this managed
service account or group-managed service account. This parameter sets the
`msDS-AllowedToActOnBehalfOfOtherIdentity` attribute of the object.

```yaml
Type: ADPrincipal[]
Parameter Sets: Group
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PrincipalsAllowedToRetrieveManagedPassword

Specifies the membership policy for systems that can use a group-managed service account. For a
service to run under a group managed service account, the system must be in the membership policy
of the account. This parameter sets the `msDS-GroupMSAMembership` attribute of a group-managed
service account object. This parameter should be set to the principals allowed to use this
group-managed service account.

```yaml
Type: ADPrincipal[]
Parameter Sets: Group
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RestrictToOutboundAuthenticationOnly

Indicates that the cmdlet creates a group-managed service account that on success can be used by a
service for successful outbound authentication requests only. This allows creating a group managed
service account without the parameters required for successful inbound authentication.

```yaml
Type: SwitchParameter
Parameter Sets: RestrictedToOutboundAuthenticationOnly
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RestrictToSingleComputer

Indicates that the cmdlet creates a managed service account that can be used only for a single
computer. Managed service accounts that are linked to a single computer account were introduced in
Windows Server 2008 R2.

```yaml
Type: SwitchParameter
Parameter Sets: RestrictedToSingleComputer
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CreateDelegatedServiceAccount

Indicates that the cmdlet creates a delegated managed service account that be used for migration.
Delegated managed service accounts were introduced in Windows Server 2025.

```yaml
Type: SwitchParameter
Parameter Sets: Group
Aliases:

Required: False
Position: Named
Default value: none
Accept pipeline input: False
Accept wildcard characters: False
```

### -SamAccountName

Specifies the Security Account Manager (SAM) account name of the user, group, computer, or service
account. The maximum length of the description is 256 characters. To be compatible with older
operating systems, create a SAM account name that's 15 characters or less. This parameter sets the
**SAMAccountName** for an account object. The LDAP display name (**ldapDisplayName**) for this
property is sAMAccountName.

Note: If the specified **SAMAccountName** string doesn't end with a $ (dollar sign), one is
appended if necessary.

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

Specifies the Active Directory Domain Services (AD DS) instance to connect to, by providing one of
the following values for a corresponding domain name or directory server. The service may be any of
the following: Active Directory Lightweight Domain Services (AD LDS), AD DS, or Active Directory
snapshot instance.

Domain name values:

- Fully qualified domain name (FQDN)
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

The default value for the *Server* parameter is determined by one of the following methods in the
order that they are listed:

- By using *Server* value from objects passed through the pipeline.
- By using the server information associated with the Active Directory PowerShell provider drive,
  when running under that drive.
- By using the domain of the computer running PowerShell.

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

Specifies the service principal names for the account. This parameter sets the
**ServicePrincipalNames** property of the account. The LDAP display name (**ldapDisplayName**) for
this property is servicePrincipalName. This parameter uses the following syntax to add remove,
replace or clear service principal name values.

要添加值：

`-ServicePrincipalNames @{Add=value1,value2,...}`

要删除某些值：

`-ServicePrincipalNames @{Remove=value3,value4,...}`

要替换值：

`-ServicePrincipalNames @{Replace=value1,value2,...}`

要清除所有值：

`-ServicePrincipalNames $Null`

You can specify more than one change by using a list separated by semicolons. For example, use the
following syntax to add and remove service principal names.

`@{Add=value1,value2,...};@{Remove=value3,value4,...}`

操作符按照以下顺序应用：

- Remove
- Add
- Replace

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

Indicates whether an account is trusted for Kerberos delegation. A service that runs under an
account that's trusted for Kerberos delegation can assume the identity of a client requesting the
service. This parameter sets the **TrustedForDelegation** property of an account object. This value
also sets the **ADS_UF_TRUSTED_FOR_DELEGATION** flag of the Active Directory User Account Control
attribute. The acceptable values for this parameter are:

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

### -WhatIf

Shows what would happen if the cmdlet runs. The cmdlet isn't run.

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

This cmdlet supports the common parameters: `-Debug`, `-ErrorAction`, `-ErrorVariable`,
`-InformationAction`, `-InformationVariable`, `-OutVariable`, `-OutBuffer`, `-PipelineVariable`,
`-Verbose`, `-WarningAction`, and `-WarningVariable`. For more information, see
[about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)

## 输入

### None or Microsoft.ActiveDirectory.Management.ADServiceAccount

You can pipe a managed service account object that's a template for the new managed service
account object to the **Instance** parameter.

## 输出

### None or Microsoft.ActiveDirectory.Management.ADServiceAccount

This cmdlet returns the new managed service account object when the **PassThru** parameter.is
specified. By default, this cmdlet doesn't generate any output.

## 备注

- This cmdlet doesn't work with AD LDS.
- This cmdlet doesn't work with an Active Directory snapshot.
- This cmdlet doesn't work with a read-only domain controller.
- This cmdlet requires that you create a Microsoft Group Key Distribution Service (GKDS) root key
  first to begin using group managed service accounts in your Active Directory deployment. For more
  information on how to create the GKDS root key using Windows PowerShell, see
  [Create the Key Distribution Services KDS Root Key](https://go.microsoft.com/fwlink/?LinkId=253584).

## 相关链接

[Get-ADServiceAccount](./Get-ADServiceAccount.md)

[Install-ADServiceAccount](./Install-ADServiceAccount.md)

[Remove-ADServiceAccount](./Remove-ADServiceAccount.md)

[Set-ADServiceAccount](./Set-ADServiceAccount.md)

[卸载 AD 服务账户](./Uninstall-ADServiceAccount.md)
