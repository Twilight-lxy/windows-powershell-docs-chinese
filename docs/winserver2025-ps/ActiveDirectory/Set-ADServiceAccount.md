---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adserviceaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADServiceAccount
---

# Set-ADServiceAccount

## 摘要
修改一个由 Active Directory 管理的服务账户对象或组管理服务账户对象。

## 语法

### 身份证明
```
Set-ADServiceAccount [-WhatIf] [-Confirm] [-AccountExpirationDate <DateTime>] [-AccountNotDelegated <Boolean>]
 [-Add <Hashtable>] [-AuthenticationPolicy <ADAuthenticationPolicy>]
 [-AuthenticationPolicySilo <ADAuthenticationPolicySilo>] [-AuthType <ADAuthType>] [-Certificates <String[]>]
 [-Clear <String[]>] [-CompoundIdentitySupported <Boolean>] [-Credential <PSCredential>]
 [-Description <String>] [-DisplayName <String>] [-DNSHostName <String>] [-Enabled <Boolean>]
 [-HomePage <String>] [-Identity] <ADServiceAccount> [-KerberosEncryptionType <ADKerberosEncryptionType>]
 [-Partition <String>] [-PassThru] [-PrincipalsAllowedToDelegateToAccount <ADPrincipal[]>]
 [-PrincipalsAllowedToRetrieveManagedPassword <ADPrincipal[]>] [-Remove <Hashtable>] [-Replace <Hashtable>]
 [-SamAccountName <String>] [-Server <String>] [-ServicePrincipalNames <Hashtable>]
 [-TrustedForDelegation <Boolean>] [<CommonParameters>]
```

### 实例
```
Set-ADServiceAccount [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -Instance <ADServiceAccount> [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-ADServiceAccount` cmdlet 用于修改 Active Directory 管理的服务账户（MSA）的属性。您可以通过使用 cmdlet 参数来修改常用的属性值；对于那些未与 cmdlet 参数关联的属性值，则可以使用 `Add`、`Remove`、`Replace` 和 `Clear` 参数来进行修改。

`Identity` 参数用于指定要修改的 Active Directory MSA（Microsoft Service Account）。您可以通过 MSA 的唯一名称（Distinguished Name）、GUID、安全标识符（Security Identifier，SID）或安全帐户管理器（Security Account Manager，SAM）帐户名称来识别它。您还可以将 `Identity` 参数设置为一个对象变量（例如 `$<localServiceAccountObject>`），或者通过管道将该对象传递给 `Identity` 参数。例如，您可以使用 **Get-ADServiceAccount** cmdlet 获取一个 MSA 对象，然后通过管道将该对象传递给 **Set-ADServiceAccount** cmdlet。

`Instance` 参数提供了一种通过应用对对象副本所做的更改来更新 MSA 对象的方法。当你将 `Instance` 参数设置为已修改的 Active Directory MSA 对象的副本时，`Set-ADServiceAccount` cmdlet 会将对原始 MSA 对象进行相同的更改。要获取用于修改的对象副本，请使用 `Get-ADServiceAccount` 命令。在指定 `Instance` 参数时，不应同时传递 `Identity` 参数。有关 `Instance` 参数的更多信息，请参阅其参数描述。

## 示例

### 示例 1：为多服务架构（MSA）设置描述
```
PS C:\> Set-ADServiceAccount -Identity Service1 -Description "Secretive Data Server"
```

此命令将标识为Service1的MSA的描述设置为“Secretive Data Server”。

### 示例 2：替换多租户架构（MSA）中某个属性的值
```
PS C:\> Set-ADServiceAccount -Identity Mongol01ADAM -ServicePrincipalNames @{replace="ADAMwdb/a.contoso.com", "ADAMbdb/a.contoso.com"}
```

此命令将属性 **ServicePrincipalNames** 的值替换为 ADAMwdb/a.contoso.com 和 ADAMbdb/a.contoso.com。

### 示例 3：设置允许获取 MSA 密码的 principal（主体）
```
PS C:\> Set-ADServiceAccount -Identity Service1 -PrincipalsAllowedToRetrieveManagedPassword "MsaAdmins.corp.contoso.com"
```

此命令将允许检索该 MSA 密码的用户范围限制为指定 Active Directory 组账户的成员。

### 示例 4：设置 ServicePrincipalNames 属性
```
PS C:\> Set-ADServiceAccount -Identity AccessTSQA -ServicePrincipalNames @{Add=ACCESSAPP/TSQA.contoso.com}
```

此命令通过指定 *Identity* 和 *ServicePrincipalNames* 参数来修改 AccessTSQA MSA 的 **ServicePrincipalNames** 属性。

### 示例 5：获取指定的 MSA 并修改其 ServicePrincipalNames 属性
```
PS C:\> Get-ADServiceAccount -Identity "AccessTSQA" | Set-ADServiceAccount -ServicePrincipalNames @{Add=ACCESSAPP/TSQA.contoso.com}
```

此命令用于修改 AccessTSQA MSA 的 **ServicePrincipalNames** 属性。该命令首先使用 **Get-ADServiceAccount** cmdlet 获取 AccessTSQA MSA，然后通过管道运算符将该 MSA 传递给当前的 cmdlet。

### 示例 6：从本地实例设置 MSA
```
PS C:\> $ServiceAccount = Get-ADServiceAccount -Identity "AccessTSQA"
PS C:\> $ServiceAccount.ServicePrincipalNames = @{Add=ACCESSAPP/TSQA.contoso.com}
PS C:\> Set-ADServiceAccount -Instance $ServiceAccount
```

这个示例修改了 AccessTSQA MSA 的 **ServicePrincipalNames** 属性。它首先修改 AccessTSQA MSA 的本地实例，然后将当前 cmdlet 的 *Instance* 参数设置为该本地实例。

## 参数

### -AccountExpirationDate
用于指定账户的到期日期。此参数会设置账户对象的 **AccountExpirationDate** 属性。该属性在轻量级目录访问协议（LDAP）中的显示名称（**ldapDisplayName**）为 “accountExpires”。

在指定此参数时，请使用 **DateTime** 语法。除非另有说明，否则时间默认为本地时间。当未指定时间值时，时间默认为当天的凌晨 12:00:00（本地时间）。当未指定日期时，日期默认为当前日期。

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
该参数用于指示用户的安全上下文是否被委托给某个服务。当该参数设置为 `true` 时，即使服务账户已被配置为支持 Kerberos 委托功能，用户的账户安全上下文也不会被委托给该服务。该参数会为 Active Directory 账户设置 `AccountNotDelegated` 属性，并同时修改 Active Directory 用户帐户控制（UAC）属性中的 `ADS_UF_NOT_DELEGATED` 标志。

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
用于指定要添加到对象属性中的值。此参数可用于向无法通过 cmdlet 参数修改的属性中添加一个或多个值。若要修改对象属性，必须使用 LDAP 显示名称。您可以通过提供以逗号分隔的值列表来为单个属性指定多个值；如果需要为多个属性指定值，则可以使用分号进行分隔。该参数的格式如下：

帮我将以下Markdown内容转换成中文：  

`-添加 @{Attribute1LDAPDisplayName=value1, value2, ...; Attribute2LDAPDisplayName=value1, value2, ...; AttributeNLDAPDisplayName=value1, value2, ...}`

当你同时使用“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）这些参数时，操作将按照以下顺序执行：

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


### -AuthenticationPolicy
Specifies an Active Directory Domain Services (AD DS) authentication policy object.
Specify the authentication policy object in one of the following formats:

- Distinguished name
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
Specifies an AD DS authentication policy silo object.
Specify the authentication policy silo object in one of the following formats:

- Distinguished name
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

### -Certificates
Specifies an array of certificates.
The cmdlet modifies the DER-encoded X.509v3 certificates of the account.
These certificates include the public key certificates issued to this account by the Microsoft Certificate Service.
This parameter sets the **Certificates** property of the account object.
The Lightweight Directory Access Protocol (LDAP) display name (**ldapDisplayName**) for this property is userCertificate.

要添加值：

`-Certificates @{Add=value1,value2,...}`

要删除值：

`-Certificates @{Remove=value3,value4,...}`

要替换值：

`-Certificates @{Replace=value1,value2,...}`

要清除所有值：

`-Certificates $Null`

You can specify more than one operation by using a list separated by semicolons.
For example, use the following syntax to add and remove **Certificates** values:

`-Certificates @{Add=value1,value2,...};@{Remove=value3,value4,...}`

这些操作符按照以下顺序应用：

- Remove
- Add
- Replace

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

### -Clear
Specifies an array of object properties that are cleared in the directory.
Use this parameter to clear one or more values of a property that cannot be modified using a cmdlet parameter.
To modify an object property, you must use the LDAP display name.
You can modify more than one property by specifying a comma-separated list.
The format for this parameter is:

`-Clear Attribute1LDAPDisplayName, Attribute2LDAPDisplayName`

When you use the *Add*, *Remove*, *Replace*, and *Clear* parameters together, the operations are performed in the following order:

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
Indicates whether an account supports Kerberos service tickets which includes the authorization data for the user's device.
This value sets the compound identity supported flag of the Active Directory **msDS-SupportedEncryptionTypes** attribute.

Warning: Domain-joined Windows systems and services such as clustering manage their own **msDS-SupportedEncryptionTypes** attribute.
Therefore any changes to the flag on the **msDS-SupportedEncryptionTypes** attribute will be overwritten by the service or system which manages the setting.

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
Specifies the DNS host name.

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
Specifies an Active Directory account object by providing one of the following property values.
The identifier in parentheses is the LDAP display name for the attribute.
The acceptable values for this parameter are:

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

The cmdlet searches the default naming context or partition to find the object.
If two or more objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

```yaml
Type: ADServiceAccount
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Instance
Specifies a modified copy of a service account object to use to update the actual Active Directory service account object.
When this parameter is used, any modifications made to the modified copy of the object are also made to the corresponding Active Directory object.
The cmdlet only updates the object properties that have changed.

The *Instance* parameter can only update service account objects that have been retrieved by using the **Get-ADServiceAccount** cmdlet.
When you specify the *Instance* parameter, you cannot specify other parameters that set properties on the object.

```yaml
Type: ADServiceAccount
Parameter Sets: Instance
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -KerberosEncryptionType
Specifies whether an account supports Kerberos encryption types that are used when creating service tickets.
This value sets the encryption types supported flags of the Active Directory **msDS-SupportedEncryptionTypes** attribute.
The acceptable values for this parameter are:

- None
- DES
- RC4
- AES128
- AES256

None removes all encryption types from the account, which may result in the KDC being unable to issue service tickets for services using the account.

DES is a weak encryption type that is not supported by default since Windows 7 and Windows Server 2008 R2.

Warning: Domain-joined Windows systems and services such as clustering manage their own **msDS-SupportedEncryptionTypes** attribute.
Therefore any changes to the flag on the **msDS-SupportedEncryptionTypes** attribute are overwritten by the service or system that manages the setting.

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

### -Partition
Specifies the distinguished name of an Active Directory partition.
The distinguished name must be one of the naming contexts on the current directory server.
The cmdlet searches this partition to find the object defined by the *Identity* parameter.

In many cases, a default value is used for the *Partition* parameter if no value is specified.
The rules for determining the default value are given below.
Note that rules listed first are evaluated first and once a default value can be determined, no further rules are evaluated.

In Active Directory Domain Services (AD DS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In AD LDS environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* will be set to the default naming context.
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

### -PrincipalsAllowedToDelegateToAccount
Specifies the accounts which can act on the behalf of users to services running as this Managed Service Account or Group Managed Service Account.
This parameter sets the **msDS-AllowedToActOnBehalfOfOtherIdentity** attribute of the object.

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

### -PrincipalsAllowedToRetrieveManagedPassword
Specifies the membership policy for systems which can use a group managed service account.
For a service to run under a group managed service account, the system must be in the membership policy of the account.
This parameter sets the **msDS-GroupMSAMembership** attribute of a group managed service account object.
This parameter should be set to the principals allowed to use this group managed service account.

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

When you use the *Add*, *Remove*, *Replace*, and *Clear* parameters together, the parameters will be applied in the following sequence:

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

当你同时使用“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）这些参数时，操作将按照以下顺序执行：

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
The service may be any of the following: Active Directory Lightweight Domain Services, Active Directory Domain Services or Active Directory Snapshot instance.

Domain name values:

- Fully qualified domain name (FQDN)
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

The default value for the *Server* parameter is determined by one of the following methods in the order that they are listed:

- By using *Server* value from objects passed through the pipeline.
- By using the server information associated with the Active Directory PowerShell provider drive, when running under that drive.
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
Specifies the service principal names for the account.
This parameter sets the **ServicePrincipalNames** property of the account.
The LDAP display name (**ldapDisplayName**) for this property is servicePrincipalName.
This parameter uses the following syntax to add, remove, replace, or clear service principal name values.

要添加值：

`-ServicePrincipalNames @{Add=value1,value2,...}`

要删除值：

`-ServicePrincipalNames @{Remove=value3,value4,...}`

要替换值：

`-ServicePrincipalNames @{Replace=value1,value2,...}`

要清除所有值：

`-ServicePrincipalNames $Null`

You can specify more than one change by using a list separated by semicolons.
For example, use the following syntax to add and remove service principal names.

`@{Add=value1,value2,...};@{Remove=value3,value4,...}`

这些操作符按照以下顺序应用：

- Remove
- Add
- Replace

The following example shows how to add and remove service principal names:

```powershell
 -ServicePrincipalNames @{Add="SQLservice\accounting.corp.contoso.com:1456"};{Remove="SQLservice\finance.corp.contoso.com:1456"}
```

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
Indicates whether an account is trusted for Kerberos delegation.
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

### None or Microsoft.ActiveDirectory.Management.ADServiceAccount
A managed service account object is received by the *Identity* parameter.

A managed service account object that was retrieved by using the **Get-ADServiceAccount** cmdlet and then modified is received by the *Instance* parameter.

## 输出

### None or Microsoft.ActiveDirectory.Management.ADServiceAccount
Returns the modified managed service account object when the *PassThru* parameter is specified.
By default, this cmdlet does not generate any output.

## 备注
* This cmdlet does not work with AD LDS.
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADServiceAccount](./Get-ADServiceAccount.md)

[Install-ADServiceAccount](./Install-ADServiceAccount.md)

[New-ADServiceAccount](./New-ADServiceAccount.md)

[Remove-ADServiceAccount](./Remove-ADServiceAccount.md)

[卸载 ADServiceAccount](./Uninstall-ADServiceAccount.md)

