---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adcomputer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADComputer
---

# Set-ADComputer

## 摘要
修改 Active Directory 中的计算机对象。

## 语法

### 身份证明
```
Set-ADComputer [-WhatIf] [-Confirm] [-AccountExpirationDate <DateTime>] [-AccountNotDelegated <Boolean>]
 [-Add <Hashtable>] [-AllowReversiblePasswordEncryption <Boolean>]
 [-AuthenticationPolicy <ADAuthenticationPolicy>] [-AuthenticationPolicySilo <ADAuthenticationPolicySilo>]
 [-AuthType <ADAuthType>] [-CannotChangePassword <Boolean>] [-Certificates <Hashtable>]
 [-ChangePasswordAtLogon <Boolean>] [-Clear <String[]>] [-CompoundIdentitySupported <Boolean>]
 [-Credential <PSCredential>] [-Description <String>] [-DisplayName <String>] [-DNSHostName <String>]
 [-Enabled <Boolean>] [-HomePage <String>] [-Identity] <ADComputer>
 [-KerberosEncryptionType <ADKerberosEncryptionType>] [-Location <String>] [-ManagedBy <ADPrincipal>]
 [-OperatingSystem <String>] [-OperatingSystemHotfix <String>] [-OperatingSystemServicePack <String>]
 [-OperatingSystemVersion <String>] [-Partition <String>] [-PassThru] [-PasswordNeverExpires <Boolean>]
 [-PasswordNotRequired <Boolean>] [-PrincipalsAllowedToDelegateToAccount <ADPrincipal[]>] [-Remove <Hashtable>]
 [-Replace <Hashtable>] [-SAMAccountName <String>] [-Server <String>] [-ServicePrincipalNames <Hashtable>]
 [-TrustedForDelegation <Boolean>] [-UserPrincipalName <String>] [<CommonParameters>]
```

### 实例
```
Set-ADComputer [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -Instance <ADComputer> [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-ADComputer` cmdlet 用于修改 Active Directory 计算机对象的属性。您可以通过使用 cmdlet 参数来修改常用的属性值；对于那些未与 cmdlet 参数关联的属性值，可以使用 `Add`、`Replace`、`Clear` 和 `Remove` 参数来进行修改。

`Identity` 参数用于指定要修改的 Active Directory 计算机。您可以通过计算机的唯一名称（Distinguished Name）、GUID、安全标识符（Security Identifier，SID）或安全账户管理器（Security Accounts Manager，SAM）账户名称来识别该计算机。您也可以将 `Identity` 参数设置为一个对象变量（例如 `$<localComputerObject>`），或者通过管道将该对象传递给 `Identity` 参数。例如，您可以使用 **Get-ADComputer** cmdlet 获取一个计算机对象，然后通过管道将该对象传递给 `Set-ADComputer`。

`Instance` 参数提供了一种通过应用对计算机对象副本所做的更改来更新计算机的方法。当您将 `Instance` 参数设置为一个已被修改的 Active Directory 计算机对象的副本时，`Set-ADComputer` cmdlet 会将对原始计算机对象进行相同的更改。要获取用于修改的对象副本，请使用 `Get-ADComputer` 命令。在指定 `Instance` 参数时，不应同时传递 `Identity` 参数。有关 `Instance` 参数的更多信息，请参阅其相关描述。

## 示例

#### 示例 1：修改指定 Active Directory 计算机的 SPN 值
```
PS C:\> Set-ADComputer -Identity "USER01-SRV1" -ServicePrincipalName @{Replace="MSSQLSVC/USER01-SRV1.USER01.COM:1456","MSOLAPSVC.3/USER01-SRV1.USER01.COM:analyze"}
```

此命令会修改由*Identity*参数指定的计算机的服务主体名称（Service Principal Name，简称SPN）值。

### 示例 2：为指定的 Active Directory 计算机设置位置
```
PS C:\> Set-ADComputer -Identity "USER02-SRV1" -Location "NA/HQ/Building A"
```

此命令用于设置由*Identity*参数指定的计算机的位置。

### 示例 3：使用 SAM 账户名称为指定的 Active Directory 计算机设置属性
```
PS C:\> Set-ADComputer -Identity "USER03-SRV1" -ManagedBy "CN=SQL Administrator 01,OU=UserAccounts,OU=Managed,DC=USER03,DC=COM"
```

此命令使用用户的SAM账户名称，为由*Identity*参数指定的计算机设置**ManagedBy**属性值。

### 示例 4：设置 Active Directory 计算机的多个属性
```
PS C:\> $Comp = Get-ADComputer -Identity "USER04-SRV1"
PS C:\> $Comp.Location = "NA/HQ/Building A"
PS C:\> $Comp.ManagedBy = "CN=SQL Administrator 01,OU=UserAccounts,OU=Managed,DC=USER04,DC=COM"
PS C:\> Set-ADComputer -Instance $Comp
```

此命令用于设置计算机的 **Location**（位置）和 **ManagedBy**（管理者）属性。

## 参数

### -AccountExpirationDate
用于指定账户的到期日期。此参数会设置账户对象的 **AccountExpirationDate** 属性。在 Active Directory 轻量级目录服务（LDAP）中，该属性的显示名称为 **accountExpires**。

在指定此参数时，请使用 **DateTime** 语法。除非另有说明，否则时间默认为当地时间。如果未指定时间值，则时间默认为当天的凌晨 12:00:00（当地时间）。如果未指定日期，则日期默认为当前日期。

```yaml
Type: DateTime
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AccountNotDelegated
指定是否将用户的安全上下文委托给某个服务。当此参数设置为 `true` 时，即使该服务账户被配置为支持 Kerberos 委托，用户的身份验证信息也不会被委托给该服务。该参数会为 Active Directory 账户设置 `AccountNotDelegated` 属性，并同时修改 Active Directory 用户账户控制（UAC）属性中的 `ADS_UF_NOT_DELEGATED` 标志。此参数的可接受值包括：

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Add
Specifies values to add to an object property.
Use this parameter to add one or more values to a property that cannot be modified using a cmdlet parameter.
To modify an object property, you must use the LDAP display name.
You can specify multiple values to a property by specifying a comma-separated list of values and more than one property by separating them using a semicolon..
The format for this parameter is:

`-Add @{Attribute1LDAPDisplayName=value1, value2, ...;   Attribute2LDAPDisplayName=value1, value2, ...; AttributeNLDAPDisplayName=value1, value2, ...}`

当你同时使用“添加”（Add）、“替换”（Replace）、“清除”（Clear）和“删除”（Remove）这些参数时，操作的执行顺序如下：

- **Remove**
- **Add**
- **Replace**
- **Clear**

```yaml
Type: Hashtable
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```



### -AuthenticationPolicy
Specifies an Active Directory Domain Services authentication policy object.
Specify the authentication policy object in one of the following formats:

- distinguished name
- GUID
- Name

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

The cmdlet searches the default naming context or partition to find the object.
If the cmdlet finds two or more objects, the cmdlet returns a non-terminating error.

```yaml
Type: ADAuthenticationPolicy
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AuthenticationPolicySilo
Specifies an Active Directory Domain Services authentication policy silo object.
Specify the authentication policy silo object in one of the following formats:

- Distinguished Name
- GUID
- Name

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

The cmdlet searches the default naming context or partition to find the object.
If the cmdlet finds two or more objects, the cmdlet returns a non-terminating error.

```yaml
Type: ADAuthenticationPolicySilo
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Certificates
Modifies the DER-encoded X.509v3 certificates of the account.
These certificates include the public key certificates issued to this account by the Microsoft Certificate Service.
This parameter sets the **Certificates** property of the account object.
The LDAP Display Name (**ldapDisplayName**) for this property is userCertificate.

Syntax:

To add values:

`-Certificates @{Add=value1,value2,...}`

To remove values:

`-Certificates @{Remove=value3,value4,...}`

To replace values:

`-Certificates @{Replace=value1,value2,...}`

To clear all values:

`-Certificates $null`

You can specify more than one operation by using a list separated by semicolons.
For example, use the following syntax to add and remove Certificate values

`-Certificates @{Add=value1,value2,...;Remove=value3,value4,...}`

The operators are applied in the following sequence:

..Remove

..Add

..Replace

```yaml
Type: Hashtable
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Clear
Specifies an array of object properties that are cleared in the directory.
Use this parameter to clear one or more values of a property that cannot be modified using a cmdlet parameter.
To modify an object property, you must use the LDAP display name.
You can modify more than one property by specifying a comma-separated list.
The format for this parameter is:

-Clear Attribute1LDAPDisplayName, Attribute2LDAPDisplayName

当你同时使用“添加”（Add）、“替换”（Replace）、“清除”（Clear）和“删除”（Remove）这些参数时，操作的执行顺序如下：

- **Remove**
- **Add**
- **Replace**
- **Clear**

```yaml
Type: String[]
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisplayName
Specifies the display name of the object.
This parameter sets the **DisplayName** property of the object.
The LDAP display name (**ldapDisplayName**) for this property is displayName.

```yaml
Type: String
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DNSHostName
Specifies the fully qualified domain name (FQDN) of the computer.
This parameter sets the **DNSHostName** property for a computer object.
The LDAP display name for this property is dNSHostName.

```yaml
Type: String
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HomePage
Specifies the URL of the home page of the object.
This parameter sets the **homePage** property of an Active Directory object.
The LDAP display name (**ldapDisplayName**) for this property is wWWHomePage.

```yaml
Type: String
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity
Specifies an Active Directory computer object by providing one of the following property values.
The identifier in parentheses is the LDAP display name for the attribute.
The acceptable values for this parameter are:

- A Distinguished Name
- A GUID (objectGUID)
- A Security Identifier (objectSid)
- A Security Accounts Manager Account Name (sAMAccountName)

The cmdlet searches the default naming context or partition to find the object.
If the identifier given is a distinguished name, the partition to search is computed from that distinguished name.
If two or more objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to a computer object instance.

```yaml
Type: ADComputer
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Instance
Specifies a modified copy of a computer object to use to update the actual Active Directory computer object.
When this parameter is used, any modifications made to the modified copy of the object are also made to the corresponding Active Directory object.
The cmdlet only updates the object properties that have changed.

The *Instance* parameter can only update computer objects that have been retrieved by using the **Get-ADComputer** cmdlet.
When you specify the *Instance* parameter, you cannot specify other parameters that set properties on the object.

```yaml
Type: ADComputer
Parameter Sets: Instance
Aliases:

Required: True
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

None will remove all encryption types from the account which may result in the Key Distribution Center (KDC) being unable to issue service tickets for services using the account.

Data Encryption Standard (DES) is a weak encryption type which is not supported by default since Windows 7 and Windows Server 2008 R2.

Warning: Domain-joined Windows systems and services such as clustering manage their own **msDS-SupportedEncryptionTypes** attribute.
Therefore any changes to the flag on the **msDS-SupportedEncryptionTypes** attribute is overwritten by the service or system which manages the setting.

```yaml
Type: ADKerberosEncryptionType
Parameter Sets: Identity
Aliases:
Accepted values: None, DES, RC4, AES128, AES256

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Location
Specifies the location of the computer, such as an office number.
This parameter sets the **Location** property of a computer.
The LDAP display name (**ldapDisplayName**) of this property is location.

```yaml
Type: String
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagedBy
Specifies the user or group that manages the object by providing one of the following property values.
Note: The identifier in parentheses is the LDAP display name for the property.
The acceptable values for this parameter are:

- A Distinguished Name
- A GUID (objectGUID)
- A Security Identifier (objectSid)
- A SAM Account Name (sAMAccountName)

This parameter sets the Active Directory attribute with an LDAP display name of managedBy.

```yaml
Type: ADPrincipal
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OperatingSystem
Specifies an operating system name.
This parameter sets the **OperatingSystem** property of the computer object.
The LDAP display name (**ldapDisplayName**) for this property is operatingSystem.

```yaml
Type: String
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OperatingSystemHotfix
Specifies an operating system hotfix name.
This parameter sets the **operatingSystemHotfix** property of the computer object.
The LDAP display name for this property is operatingSystemHotfix.

```yaml
Type: String
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OperatingSystemServicePack
Specifies the name of an operating system service pack.
This parameter sets the **OperatingSystemServicePack** property of the computer object.
The LDAP display name (**ldapDisplayName**) for this property is operatingSystemServicePack.

```yaml
Type: String
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OperatingSystemVersion
Specifies an operating system version.
This parameter sets the **OperatingSystemVersion** property of the computer object.
The LDAP display name (**ldapDisplayName**) for this property is operatingSystemVersion.

```yaml
Type: String
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Partition
Specifies the distinguished name of an Active Directory partition.
The distinguished name must be one of the naming contexts on the current directory server.
The cmdlet searches this partition to find the object defined by the *Identity* parameter.

In many cases, a default value is used for the *Partition* parameter if no value is specified.
The rules for determining the default value are given below.
Note that rules listed first are evaluated first and once a default value can be determined, no further rules are evaluated.

In Active Directory Domain Services environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent (DSA) object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Partition* parameter will not take any default value.

```yaml
Type: String
Parameter Sets: Identity
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

Note: This parameter cannot be set to $True or 1 for an account that also has the **ChangePasswordAtLogon** property set to &True.

```yaml
Type: Boolean
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PrincipalsAllowedToDelegateToAccount
Specifies the accounts which can act on the behalf of users to services running as this computer account.
This parameter sets the **msDS-AllowedToActOnBehalfOfOtherIdentity** attribute of a computer account object.

`Running Set-ADComputer without specifying the first principal will cause it to get overridden`

```yaml
Type: ADPrincipal[]
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Remove
Specifies that the cmdlet remove values of an object property.
Use this parameter to remove one or more values of a property that cannot be modified using a cmdlet parameter.
To remove an object property, you must use the LDAP display name.
You can remove more than one property by specifying a semicolon-separated list.
The format for this parameter is:

`-Remove @{Attribute1LDAPDisplayName=value[];   Attribute2LDAPDisplayName=value[]}`

When you use the *Add*, *Replace*, *Clear*, and *Remove* parameters together, the parameters are applied in the following sequence:

- **Remove**
- **Add**
- **Replace**
- **Clear**

```yaml
Type: Hashtable
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Replace
Specifies values for an object property that will replace the current values.
Use this parameter to replace one or more values of a property that cannot be modified using a cmdlet parameter.
To modify an object property, you must use the LDAP display name.
You can specify multiple values to a property by specifying a comma-separated list of values, and more than one property by separating them using a semicolon.
The format for this parameter is:

`-Replace @{Attribute1LDAPDisplayName=value1, value2, ...;   Attribute2LDAPDisplayName=value1, value2, ...; AttributeNLDAPDisplayName=value1, value2, ...}`

When you use the *Add*, *Remove*, *Replace*, and *Clear* parameters together, the operations will be performed in the following order:

- **Remove**
- **Add**
- **Replace**
- **Clear**

```yaml
Type: Hashtable
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SAMAccountName
Specifies the Security Account Manager (SAM) account name of the user, group, computer, or service account.
The maximum length of the description is 256 characters.
To be compatible with older operating systems, create a SAM account name that is 20 characters or less.
This parameter sets the **SAMAccountName** for an account object.
The LDAP display name (**ldapDisplayName**) for this property is sAMAccountName.

Note: If the string value provided is not terminated with a $ character, the system adds one if needed.

```yaml
Type: String
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
Specifies the Active Directory Domain Services instance to connect to, by providing one of the following values for a corresponding domain name or directory server.
The service may be any of the following: Active Directory Lightweight Domain Services, Active Directory Domain Services, or Active Directory snapshot instance.

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
This parameter uses the following syntax to add remove, replace or clear service principal name values:

Syntax:

To add values:

`-ServicePrincipalNames @{Add=value1,value2,...}`

To remove values:

`-ServicePrincipalNames @{Remove=value3,value4,...}`

To replace values:

`-ServicePrincipalNames @{Replace=value1,value2,...}`

To clear all values:

`-ServicePrincipalNames $null`

You can specify more than one change by using a list separated by semicolons.
For example, use the following syntax to add and remove service principal names.

`@{Add=value1,value2,...;Remove=value3,value4,...}`

The operators are applied in the following sequence:

..Remove

..Add

..Replace

The following example shows how to add and remove service principal names.

`-ServicePrincipalNames @{Add="SQLservice/accounting.corp.contoso.com:1456";Remove="SQLservice/finance.corp.contoso.com:1456"}`

```yaml
Type: Hashtable
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UserPrincipalName
Specifies a user principal name (UPN) in the format `<user>@<DNS-domain-name>`.
A user principal name (UPN) is a friendly name assigned by an administrator that is shorter than the LDAP distinguished name used by the system and easier to remember.
The UPN is independent of the user object's distinguished name, so a user object can be moved or renamed without affecting the user logon name.
When logging on using a UPN, users no longer have to choose a domain from a list on the logon dialog box.

```yaml
Type: String
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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

### Microsoft.ActiveDirectory.Management.ADComputer
A computer object is received by the *Identity* parameter.

A computer object that was retrieved by using the **Get-ADComputer** cmdlet and then modified is received by the *Instance* parameter.

## 输出

### None or Microsoft.ActiveDirectory.Management.ADComputer
Returns the modified computer object when the *PassThru* parameter is specified.
By default, this cmdlet does not generate any output.

## 备注
* This cmdlet does not work with AD LDS.
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.
* This cmdlet does not work when connected to Global Catalog port.

## 相关链接

[Add-ADComputerServiceAccount](./Add-ADComputerServiceAccount.md)

[Get-ADComputer](./Get-ADComputer.md)

[Get-ADComputerServiceAccount](./Get-ADComputerServiceAccount.md)

[New-ADComputer](./New-ADComputer.md)

[Remove-ADComputer](./Remove-ADComputer.md)

[Remove-ADComputerServiceAccount](./Remove-ADComputerServiceAccount.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

