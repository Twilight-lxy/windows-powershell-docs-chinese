---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-aduser?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADUser
---

# Set-ADUser

## 摘要

修改一个 Active Directory 用户。

## 语法

### 身份

```
Set-ADUser [-WhatIf] [-Confirm] [-AccountExpirationDate <DateTime>] [-AccountNotDelegated <Boolean>]
 [-Add <Hashtable>] [-AllowReversiblePasswordEncryption <Boolean>]
 [-AuthenticationPolicy <ADAuthenticationPolicy>] [-AuthenticationPolicySilo <ADAuthenticationPolicySilo>]
 [-AuthType <ADAuthType>] [-CannotChangePassword <Boolean>] [-Certificates <Hashtable>]
 [-ChangePasswordAtLogon <Boolean>] [-City <String>] [-Clear <String[]>] [-Company <String>]
 [-CompoundIdentitySupported <Boolean>] [-Country <String>] [-Credential <PSCredential>] [-Department <String>]
 [-Description <String>] [-DisplayName <String>] [-Division <String>] [-EmailAddress <String>]
 [-EmployeeID <String>] [-EmployeeNumber <String>] [-Enabled <Boolean>] [-Fax <String>] [-GivenName <String>]
 [-HomeDirectory <String>] [-HomeDrive <String>] [-HomePage <String>] [-HomePhone <String>]
 [-Identity] <ADUser> [-Initials <String>] [-KerberosEncryptionType <ADKerberosEncryptionType>]
 [-LogonWorkstations <String>] [-Manager <ADUser>] [-MobilePhone <String>] [-Office <String>]
 [-OfficePhone <String>] [-Organization <String>] [-OtherName <String>] [-Partition <String>] [-PassThru]
 [-PasswordNeverExpires <Boolean>] [-PasswordNotRequired <Boolean>] [-POBox <String>] [-PostalCode <String>]
 [-PrincipalsAllowedToDelegateToAccount <ADPrincipal[]>] [-ProfilePath <String>] [-Remove <Hashtable>]
 [-Replace <Hashtable>] [-SamAccountName <String>] [-ScriptPath <String>] [-Server <String>]
 [-ServicePrincipalNames <Hashtable>] [-SmartcardLogonRequired <Boolean>] [-State <String>]
 [-StreetAddress <String>] [-Surname <String>] [-Title <String>] [-TrustedForDelegation <Boolean>]
 [-UserPrincipalName <String>] [<CommonParameters>]
```

### 实例

```
Set-ADUser [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Instance <ADUser>
 [-PassThru] [-SamAccountName <String>] [-Server <String>] [<CommonParameters>]
```

## 描述

`Set-ADUser` cmdlet 可以修改 Active Directory 用户的属性。您可以使用该 cmdlet 的参数来修改常用的属性值；对于那些未与 cmdlet 参数关联的属性值，则可以使用 `Add`、`Remove`、`Replace` 和 `Clear` 参数来进行设置。

`Identity` 参数用于指定要修改的 Active Directory 用户。您可以通过该用户的唯一名称（Distinguished Name）、GUID、安全标识符（Security Identifier，SID）或安全帐户管理器（Security Account Manager，SAM）账户名来识别用户。您也可以将 `Identity` 参数设置为一个对象变量（例如 `$<localUserObject>`），或者通过管道将该对象传递给 `Identity` 参数。例如，您可以使用 **Get-ADUser** cmdlet 获取一个用户对象，然后通过管道将该对象传递给 **Set-ADUser** cmdlet。

`Instance` 参数提供了一种通过应用对用户对象副本所做的更改来更新该用户对象的方法。当您将 `Instance` 参数设置为已修改的 Active Directory 用户对象的副本时，`Set-ADUser` cmdlet 会对原始用户对象执行相同的更改。要获取用于修改的对象副本，请使用 `Get-ADUser` cmdlet。在使用 `Instance` 参数时，不允许同时使用 `Identity` 参数。有关 `Instance` 参数的更多信息，请参阅其官方文档说明。

使用 **New-ADUser** cmdlet 创建的账户如果没有提供密码，则会被禁用。

对于 AD LDS 环境来说，必须指定 *Partition* 参数，以下两种情况除外：

- The cmdlet is run from an Active Directory provider drive.
- A default naming context or partition is defined for the AD LDS environment.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.

## 示例

### 示例 1：为用户设置属性

```powershell
$params = @{
    Identity          = 'ChewDavid'
    HomePage          = 'http://fabrikam.com/employees/ChewDavid'
    LogonWorkstations = 'ChewDavid-DSKTOP,ChewDavid-LPTOP'
}
Set-ADUser @params
```

此命令将指定用户的“主页”属性设置为 http://fabrikam.com/employees/ChewDavid，并将“登录工作站”属性设置为 ChewDavid-DSKTOP、ChewDavid-LPTOP。

### 示例 2：为多个用户设置属性

```powershell
PS C:\> Get-ADUser -Filter 'Name -like "*"' -SearchBase 'OU=HumanResources,OU=UserAccounts,DC=FABRIKAM,DC=COM' -Properties DisplayName | % {Set-ADUser $_ -DisplayName ($_.Surname + ' ' + $_.GivenName)}
```

这条命令会获取位于组织单元（OU）“HumanResources, OU/UserAccounts, DC=FABRIKAM, DC=COM”中的所有用户。同时，该命令会将这些用户对象的 **DisplayName** 属性设置为用户的 **Surname**（姓氏）和 **GivenName**（名字）的拼接结果。

### 示例 3：设置属性

```powershell
PS C:\> Set-ADUser -Identity GlenJohn -Replace @{title="director";mail="glenjohn@fabrikam.com"}
```

这个命令将指定用户的 **title** 属性设置为 “director”，并将 **mail** 属性设置为 “glenjohn@fabrikam.com”。

### 示例 4：修改用户的 otherMailbox 属性

```powershell
PS C:\> Set-ADUser -Identity GlenJohn -Remove @{otherMailbox="glen.john"} -Add @{url="fabrikam.com"} -Replace @{title="manager"} -Clear description
```

此命令会修改使用SAM账户名“GlenJohn”的用户对象：从`otherMailbox`属性中删除“glen.john”；在`url`属性中添加“fabrikam.com”；将`title`属性替换为“manager”；并清除`description`属性的内容。

### 示例 5：将用户属性设置到本地实例

```powershell
PS C:\> $User = Get-ADUser -Identity GlenJohn -Properties mail,department
PS C:\> $User.mail = "glen@fabrikam.com"
PS C:\> $User.department = "Accounting"
PS C:\> Set-ADUser -Instance $User
```

这个示例使用 *Instance* 参数，为名为 GlenJohn 的 SAM 账户的用户对象设置 **mail** 和 **department** 属性。

### 示例 6：为用户设置属性

```powershell
PS C:\> $Hours = New-Object byte[] 21
PS C:\> $Hours[5] = 255; $Hours[8] = 255; $Hours[11] = 255; $Hours[14] = 255; $Hours[17] = 255;
PS C:\> $Hours[6] = 1; $Hours[9] = 1; $Hours[12] = 1; $Hours[15] = 1; $Hours[18] = 1;
PS C:\> $ReplaceHashTable = New-Object HashTable
PS C:\> $ReplaceHashTable.Add("logonHours", $Hours)
PS C:\> $ReplaceHashTable.Add("description", "Sarah Davis can only logon from Monday through Friday from 8:00 AM to 5:00 PM")
PS C:\> Set-ADUser -Identity "SarahDavis" -Replace $ReplaceHashTable
```

这个示例将用户的登录时间设置为周一至周五的上午8点至下午5点，并添加了一段描述。它使用指定的字节数组更新了`loginHours`属性，同时使用指定的字符串更新了`description`属性。

### 示例 7：为用户设置一个属性

```powershell
PS C:\> $Manager = Get-ADUser -Identity GlenJohn -Server Corp-DC01
PS C:\> Set-ADUser -Identity ChewDavid -Manager $Manager -Server Branch-DC02
```

这个示例为使用SAM账户名“ChewDavid”的用户设置了**Manager**属性，该用户的经理GlenJohn属于另一个域的用户。

### 示例 8：获取用户并设置一个属性

```powershell
PS C:\> Get-ADUser -Identity "DavidChew" | Set-ADUser -Manager "ElisaDaugherty"
```

该命令修改了名为DavidChew的用户对应的“Manager”属性。首先，使用`Get-ADUser` cmdlet来获取DavidChew用户的信息，然后通过管道运算符（pipeline operator）将该用户对象传递给当前的cmdlet进行处理。

## 参数

### -AccountExpirationDate

指定账户的过期日期。此参数用于设置账户对象的 `AccountExpirationDate` 属性。该属性在 LDAP 显示名称（`ldapDisplayName`）中显示为 `accountExpires`。

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

该参数用于指示用户的安全上下文是否被委托给某个服务。当此参数设置为 $True 时，即使服务账户已被设置为支持 Kerberos 委托的受信任账户，该账户的安全上下文也不会被委托给该服务。此参数会为 Active Directory 账户设置 **AccountNotDelegated** 属性，并同时修改 Active Directory 用户账户控制（UAC）属性中的 **ADS_UF_NOT_DELEGATED** 标志。该参数的可接受值包括：

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

Specifies values to add to an object property. Use this parameter to add one or more values to a
property that cannot be modified using a cmdlet parameter. To modify an object property, you must
use the LDAP display name. You can specify multiple values to a property by specifying a
comma-separated list of values, and more than one property by separating them using a semicolon. If
any of the properties have a null or empty value the cmdlet will return an error. The format for
this parameter is:

`-Add @{Attribute1LDAPDisplayName=value1, value2, ...;   Attribute2LDAPDisplayName=value1, value2, ...; AttributeNLDAPDisplayName=value1, value2, ...}`

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

### -AllowReversiblePasswordEncryption

Indicates whether reversible password encryption is allowed for the account. This parameter sets the
**AllowReversiblePasswordEncryption** property of the account. This parameter also sets the
**ADS_UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED** flag of the Active Directory User Account Control (UAC)
attribute. The acceptable values for this parameter are:

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

- Distinguished name
- GUID
- Name

This parameter can also get this object through the pipeline or you can set this parameter to an
object instance.

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

- Distinguished name
- GUID
- Name

This parameter can also get this object through the pipeline or you can set this parameter to an
object instance.

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

Indicates whether the account password can be changed.
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

Specifies an array of certificates. The cmdlet modifies the DER-encoded X.509v3 certificates of the
account. These certificates include the public key certificates issued to this account by the
Microsoft Certificate Service. This parameter sets the **Certificates** property of the account
object. The Lightweight Directory Access Protocol (LDAP) display name (**ldapDisplayName**) for this
property is userCertificate.

To add values:

`-Certificates @{Add=value1,value2,...}`

To remove values:

`-Certificates @{Remove=value3,value4,...}`

To replace values:

`-Certificates @{Replace=value1,value2,...}`

To clear all values:

`-Certificates $Null`

You can specify more than one operation by using a list separated by semicolons.
For example, use the following syntax to add and remove **Certificates** values:

`-Certificates @{Add=value1;Remove=value3}`

The operators are applied in the following sequence:

- Remove
- Add
- Replace

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

Indicates whether a password must be changed during the next logon attempt.
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

### -City

Specifies the user's town or city.
This parameter sets the **City** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is l.

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

### -Clear

Specifies an array of object properties that are cleared in the directory. Use this parameter to
clear one or more values of a property that cannot be modified using a cmdlet parameter. To modify
an object property, you must use the LDAP display name. You can modify more than one property by
specifying a comma-separated list. The format for this parameter is:

`-Clear Attribute1LDAPDisplayName, Attribute2LDAPDisplayName`

When you use the **Add**, **Remove**, **Replace**, and **Clear** parameters together, the
operations are performed in the following order:

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

### -Company

Specifies the user's company.
This parameter sets the **Company** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is company.

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

### -CompoundIdentitySupported

Indicates whether an account supports Kerberos service tickets which includes the authorization data
for the user's device. This value sets the compound identity supported flag of the Active Directory
**msDS-SupportedEncryptionTypes** attribute. The acceptable values for this parameter are:

- $False or 0
- $True or 1

> [!WARNING]
> Domain-joined Windows systems and services such as clustering manage their own
> **msDS-SupportedEncryptionTypes** attribute. Therefore any changes to the flag on the
> **msDS-SupportedEncryptionTypes** attribute are overwritten by the service or system that manages
> the setting.

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

### -Country

Specifies the country or region code for the user's language of choice.
This parameter sets the **Country** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is c.
This value is not used by Windows 2000.

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

### -Credential

Specifies the user account credentials to use to perform this task. The default credentials are the
credentials of the currently logged on user unless the cmdlet is run from an Active Directory
PowerShell provider drive. If the cmdlet is run from such a provider drive, the account associated
with the drive is the default.

To specify this parameter, you can type a user name, such as `User1` or `Domain01\User01` or you can specify a **PSCredential** object.
If you specify a user name for this parameter, the cmdlet prompts for a password.

You can also create a **PSCredential** object by using a script or by using the `Get-Credential`
cmdlet. You can then set the **Credential** parameter to the **PSCredential** object.

If the acting credentials do not have directory-level permission to perform the task, Active
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

### -Department

Specifies the user's department.
This parameter sets the **Department** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is department.

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

### -Description

Specifies a description of the object.
This parameter sets the value of the **Description** property for the user object.
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
This parameter sets the **DisplayName** property of the user object.
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

### -Division

Specifies the user's division.
This parameter sets the **Division** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is division.

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

### -EmailAddress

Specifies the user's e-mail address.
This parameter sets the **EmailAddress** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is mail.

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

### -EmployeeID

Specifies the user's employee ID.
This parameter sets the **EmployeeID** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is employeeID.

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

### -EmployeeNumber

Specifies the user's employee number.
This parameter sets the **EmployeeNumber** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is employeeNumber.

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

Indicates whether an account is enabled. An enabled account requires a password. This parameter sets
the **Enabled** property for an account object. This parameter also sets the
**ADS_UF_ACCOUNTDISABLE** flag of the Active Directory User Account Control (UAC) attribute. The
acceptable values for this parameter are:

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

### -Fax

Specifies the user's fax phone number.
This parameter sets the **Fax** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is facsimileTelephoneNumber.

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

### -GivenName

Specifies the user's given name.
This parameter sets the **GivenName** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is givenName.

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

### -HomeDirectory

Specifies a user's home directory.
This parameter sets the **HomeDirectory** property of a user object.
The LDAP display name (**ldapDisplayName**) for this property is homeDirectory.

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

### -HomeDrive

Specifies a drive that is associated with the UNC path defined by the **HomeDirectory** property.
The drive letter is specified as `<DriveLetter>`: where `<DriveLetter>` indicates the letter of the
drive to associate. The `<DriveLetter>` must be a single, uppercase letter and the colon is
required. This parameter sets the **HomeDrive** property of the user object. The LDAP display name
(**ldapDisplayName**) for this property is homeDrive.

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

### -HomePhone

Specifies the user's home telephone number.
This parameter sets the **HomePhone** property of a user.
The LDAP display name (**ldapDisplayName**) of this property is homePhone.

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

Specifies an Active Directory user object by providing one of the following property values.
The identifier in parentheses is the LDAP display name for the attribute.
The acceptable values for this parameter are:

- A distinguished name
- A GUID (**objectGUID**)
- A security identifier (**objectSid**)
- A SAM account name (**sAMAccountName**)

The cmdlet searches the default naming context or partition to find the object.
If two or more objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to an
object instance.

```yaml
Type: ADUser
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Initials

Specifies the initials that represent part of a user's name.
You can use this value for the user's middle initial.
This parameter sets the **Initials** property of a user.
The LDAP display name (**ldapDisplayName**) of this property is initials.

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

### -Instance

Specifies an **ADUser** object that identifies the Active Directory user object that should be
modified and the set of changes that should be made to that object. When this parameter is
specified, any modifications made to the **ADUser** object are also made to the corresponding Active
Directory object. The cmdlet only updates the object properties that have changed.

The **ADUser** object specified as the value of the **Instance** parameter must have been retrieved
by using the `Get-ADUser` cmdlet. When you specify the **Instance** parameter, you cannot specify
other parameters that set individual properties on the object.

```yaml
Type: ADUser
Parameter Sets: Instance
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -KerberosEncryptionType

Specifies whether an account supports Kerberos encryption types which are used during creation of
service tickets. This value sets the encryption types supported flags of the Active Directory
**msDS-SupportedEncryptionTypes** attribute. The acceptable values for this parameter are:

- `None`
- `DES`
- `RC4`
- `AES128`
- `AES256`

`None` removes all encryption types from the account, resulting in the KDC being unable to issue
service tickets for services using the account.

DES is a weak encryption type that is not supported by default since Windows 7 and Windows Server
2008 R2.

> [!WARNING]
> Domain-joined Windows systems and services such as clustering manage their own
> **msDS-SupportedEncryptionTypes** attribute. Therefore any changes to the flag on the
> **msDS-SupportedEncryptionTypes** attribute are overwritten by the service or system that manages
> the setting.

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

### -LogonWorkstations

Specifies the computers that the user can access. To specify more than one computer, create a
single comma-separated list. You can identify a computer by using the Security Account Manager
(SAM) account name (**sAMAccountName**) or the DNS host name of the computer. The SAM account name
is the same as the NetBIOS name of the computer.

The LDAP display name (**ldapDisplayName**) for this property is userWorkStations.

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

### -Manager

Specifies the user's manager.
This parameter sets the **Manager** property of a user object.
This parameter is set by providing one of the following property values.
Note: The identifier in parentheses is the LDAP display name for the property.
The acceptable values for this parameter are:

- A distinguished name
- A GUID (**objectGUID**)
- A security identifier (**objectSid**)
- A SAM account name (**sAMAccountName**)

The LDAP display name (**ldapDisplayName**) of this property is manager.

```yaml
Type: ADUser
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MobilePhone

Specifies the user's mobile phone number.
This parameter sets the **MobilePhone** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is mobile.

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

### -Office

Specifies the location of the user's office or place of business.
This parameter sets the **Office** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is physicalDeliveryOfficeName.

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

### -OfficePhone

Specifies the user's office telephone number.
This parameter sets the **OfficePhone** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is telephoneNumber.

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

### -Organization

Specifies the user's organization.
This parameter sets the **Organization** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is o.

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

### -OtherName

Specifies a name in addition to a user's given name and surname, such as the user's middle name.
This parameter sets the **OtherName** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is middleName.

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
The cmdlet searches this partition to find the object defined by the **Identity** parameter.

In many cases, a default value is used for the **Partition** parameter if no value is specified.
The rules for determining the default value are given below. Note that rules listed first are
evaluated first and when a default value can be determined, no further rules are evaluated.

In AD DS environments, a default value for **Partition** are set in the following cases:

- If the **Identity** parameter is set to a distinguished name, the default value of **Partition**
  is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of **Partition** is
  automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of **Partition** is set to the default
  partition or naming context of the target domain.

In AD LDS environments, a default value for **Partition** will be set in the following cases:

- If the **Identity** parameter is set to a distinguished name, the default value of **Partition**
  is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of **Partition** is
  automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of **Partition** is
  set to the default naming context. To specify a default naming context for an AD LDS environment,
  set the **msDS-defaultNamingContext** property of the Active Directory directory service agent
  object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the **Partition** parameter does not take any default value.

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

Specifies whether the password of an account can expire. This parameter sets the
**PasswordNeverExpires** property of an account object. This parameter also sets the
**ADS_UF_DONT_EXPIRE_PASSWD** flag of the Active Directory User Account Control attribute. The
acceptable values for this parameter are:

- `$False` or `0`
- `$True` or `1`

> [!NOTE]
> This parameter cannot be set to `$True` or `1` for an account that also has the
> **ChangePasswordAtLogon** property set to `$True`.

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

Specifies whether the account requires a password. This parameter sets the **PasswordNotRequired**
property of an account, such as a user or computer account. This parameter also sets the
**ADS_UF_PASSWD_NOTREQD** flag of the Active Directory User Account Control attribute. The
acceptable values for this parameter are:

- `$False` or `0`
- `$True` or `1`

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

### -POBox

Specifies the user's post office box number.
This parameter sets the **POBox** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is postOfficeBox.

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

### -PostalCode

Specifies the postal code or zip code. This parameter sets the **PostalCode** property of a user
object. The LDAP display name (**ldapDisplayName**) of this property is `postalCode`.

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

### -PrincipalsAllowedToDelegateToAccount

Specifies an array of principal objects. This parameter sets the
**msDS-AllowedToActOnBehalfOfOtherIdentity** attribute of a computer account object.

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

### -ProfilePath

Specifies a path to the user's profile.
This value can be a local absolute path or a Universal Naming Convention (UNC) path.
This parameter sets the **ProfilePath** property of the user object.
The LDAP display name (**ldapDisplayName**) for this property is profilePath.

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

### -Remove

Specifies that the cmdlet remove values of an object property. Use this parameter to remove one or
more values of a property that cannot be modified using a cmdlet parameter. To remove an object
property, you must use the LDAP display name. You can specify multiple values to a property by
specifying a comma-separated list of values, and more than one property by separating them using a
semicolon. If any of the properties have a null or empty value the cmdlet will return an error. The
format for this parameter is:

`-Remove @{Attribute1LDAPDisplayName=value1, value2, ...;   Attribute2LDAPDisplayName=value1, value2, ...; AttributeNLDAPDisplayName=value1, value2, ...}`

When you use the **Add**, **Remove**, **Replace**, and **Clear** parameters together, the
parameters are applied in the following sequence:

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

Specifies values for an object property that will replace the current values. Use this parameter to
replace one or more values of a property that cannot be modified using a cmdlet parameter. To modify
an object property, you must use the LDAP display name. You can specify multiple values to a
property by specifying a comma-separated list of values, and more than one property by separating
them using a semicolon. If any of the properties have a null or empty value the cmdlet will return
an error. The format for this parameter is:

`-Replace @{Attribute1LDAPDisplayName=value1, value2, ...;   Attribute2LDAPDisplayName=value1, value2, ...; AttributeNLDAPDisplayName=value1, value2, ...}`

当你同时使用 **Add**（添加）、**Remove**（删除）、**Replace**（替换）和 **Clear**（清除）这些参数时，操作将按照以下顺序进行：

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

### -SamAccountName

Specifies the Security Account Manager (SAM) account name of the user, group, computer, or service
account. The maximum length of the description is 256 characters. To be compatible with older
operating systems, create a SAM account name that is 20 characters or less. This parameter sets the
**SAMAccountName** for an account object. The LDAP display name (**ldapDisplayName**) for this
property is `sAMAccountName`.

> [!NOTE]
> If the string value provided is not terminated with a `$` character, the system adds one if
> needed.

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

### -ScriptPath

Specifies a path to the user's log on script.
This value can be a local absolute path or a Universal Naming Convention (UNC) path.
This parameter sets the **ScriptPath** property of the user.
The LDAP display name (**ldapDisplayName**) for this property is scriptPath.

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

Specifies the AD DS instance to connect to, by providing one of the following values for a corresponding domain name or directory server.
The service may be any of the following: AD LDS, AD DS, or Active Directory snapshot instance.

Specify the AD DS instance in one of the following ways:

Domain name values:

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

The default value for this parameter is determined by one of the following methods in the order that
they are listed:

- By using the **Server** value from objects passed through the pipeline
- By using the server information associated with the AD DS Windows PowerShell provider drive, when
  the cmdlet runs in that drive
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

Specifies the service principal names for the account. This parameter sets the
**ServicePrincipalNames** property of the account. The LDAP display name (**ldapDisplayName**) for
this property is `servicePrincipalName`. This parameter uses the following syntax to add, remove,
replace or clear service principal name values.

Syntax:

To add values:

`-ServicePrincipalNames @{Add=value1,value2,...}`

To remove values:

`-ServicePrincipalNames @{Remove=value3,value4,...}`

To replace values:

`-ServicePrincipalNames @{Replace=value1,value2,...}`

To clear all values:

`-ServicePrincipalNames $null`

You can specify more than one change by using a list separated by semicolons. For example, use the
following syntax to add and remove service principal names.

`@{Add=value1,value2,...};@{Remove=value3,value4,...}`

The operators will be applied in the following sequence:

- Remove
- Add
- Replace

The following example shows how to add and remove service principal names.

`-ServicePrincipalNames-@{Add="SQLservice\accounting.corp.contoso.com:1456"};{Remove="SQLservice\finance.corp.contoso.com:1456"}`

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

### -SmartcardLogonRequired

Indicates whether a smart card is required to logon. This parameter sets the
**SmartCardLoginRequired** property for a user. This parameter also sets the
**ADS_UF_SMARTCARD_REQUIRED** flag of the Active Directory User Account Control attribute. The
acceptable values for this parameter are:

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

### -State

Specifies the user's state or province.
This parameter sets the **State** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is st.

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

### -StreetAddress

Specifies the user's street address.
This parameter sets the **StreetAddress** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is streetAddress.

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

### -Surname

Specifies the user's last name or surname.
This parameter sets the **Surname** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is sn.

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

### -Title

Specifies the user's title.
This parameter sets the **Title** property of a user object.
The LDAP display name (**ldapDisplayName**) of this property is title.

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

### -TrustedForDelegation

Specifies whether an account is trusted for Kerberos delegation. A service that runs under an
account that is trusted for Kerberos delegation can assume the identity of a client requesting the
service. This parameter sets the **TrustedForDelegation** property of an account object. This value
also sets the **ADS_UF_TRUSTED_FOR_DELEGATION** flag of the Active Directory User Account Control
attribute. The acceptable values for this parameter are:

- `$False` or `0`
- `$True` or `1`

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

Specifies a user principal name (UPN) in the format `<user>@<DNS-domain-name>`. A UPN is a friendly
name assigned by an administrator that is shorter than the LDAP distinguished name used by the
system and easier to remember. The UPN is independent of the user object's distinguished name, so a
user object can be moved or renamed without affecting the user logon name. When logging on using a
UPN, users don't have to choose a domain from a list on the logon dialog box.

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

This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable,
-InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose,
-WarningAction, and -WarningVariable. For more information, see
[about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### None or Microsoft.ActiveDirectory.Management.ADUser

A user object is received by the **Identity** parameter.

A user object that was retrieved by using the `Get-ADUser` cmdlet and then modified is received by
the **Instance** parameter.

## 输出

### None or Microsoft.ActiveDirectory.Management.ADUser

Returns the modified user object when the **PassThru** parameter is specified.
By default, this cmdlet does not generate any output.

## 备注

- This cmdlet does not work with an Active Directory snapshot.
- This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADUser](./Get-ADUser.md)

[New-ADUser](./New-ADUser.md)

[Remove-ADUser](./Remove-ADUser.md)

[Set-ADAccountControl](./Set-ADAccountControl.md)
