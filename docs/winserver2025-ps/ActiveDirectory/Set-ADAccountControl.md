---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adaccountcontrol?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADAccountControl
---

# Set-ADAccountControl

## 摘要
修改 Active Directory 账户的用户账户控制（UAC）设置值。

## 语法

```
Set-ADAccountControl [-WhatIf] [-Confirm] [-AccountNotDelegated <Boolean>]
 [-AllowReversiblePasswordEncryption <Boolean>] [-AuthType <ADAuthType>] [-CannotChangePassword <Boolean>]
 [-Credential <PSCredential>] [-DoesNotRequirePreAuth <Boolean>] [-Enabled <Boolean>]
 [-HomedirRequired <Boolean>] [-Identity] <ADAccount> [-MNSLogonAccount <Boolean>] [-Partition <String>]
 [-PassThru] [-PasswordNeverExpires <Boolean>] [-PasswordNotRequired <Boolean>] [-Server <String>]
 [-TrustedForDelegation <Boolean>] [-TrustedToAuthForDelegation <Boolean>] [-UseDESKeyOnly <Boolean>]
 [<CommonParameters>]
```

## 描述
`Set-ADAccountControl` cmdlet 可以修改 Active Directory 用户或计算机账户的用户账户控制（UAC）设置。UAC 设置通过 cmdlet 参数来表示。例如，可以通过设置 `PasswordNeverExpires` 参数来决定账户密码是否可以过期，并从而修改相应的 **ADS_UF_DONT_EXPIRE_PASSWD** UAC 值。

*Identity* 参数指定了要修改的 Active Directory 账户。

您可以通过账户的独特名称、GUID（全局唯一标识符）、安全标识符（SID）或安全账户管理器（SAM）账户名称来识别该账户。您还可以将“Identity”参数设置为某个对象变量（例如 `$<localADAccountObject>`），或者通过管道将一个账户对象传递给“Identity”参数。例如，您可以使用 **Search-ADAccount** cmdlet 来检索一个账户对象，然后将该对象通过管道传递给 **Set-ADAccountControl** cmdlet。同样地，您也可以使用 **Get-ADUser**、**Get-ADComputer** 或 **Get-ADServiceAccount** cmdlets 来检索账户对象，并将这些对象通过管道传递给相应的 cmdlet。

对于 Active Directory 轻量级目录服务（AD LDS）环境来说，必须指定 *Partition* 参数，以下两种情况除外：

- The cmdlet is run from an Active Directory provider drive.
- A default naming context or partition is defined for the AD LDS environment.

要为 AD LDS 环境指定一个默认的命名上下文，请设置该 AD LDS 实例对应的 Active Directory 目录服务代理（DSA）对象（**nTDSDSA**）的 **msDS-defaultNamingContext** 属性。

## 示例

### 示例 1：要求用户使用密码登录
```
PS C:\> Set-ADAccountControl -Identity ElisaD -PasswordNotRequired $False
```

此命令将 userAccountControl 标志设置为“需要密码才能登录”。

### 示例 2：禁用用户账户的密码更改功能
```
PS C:\> Set-ADAccountControl -Identity 'CN=Elisa Daugherty,OU=HumanResources,OU=UserAccounts,DC=FABRIKAM,DC=COM' -CannotChangePassword $True
```

这个命令设置了用户的安全描述符，以确保他们无法更改自己的密码。

### 示例 3：禁用用户账户的委托功能
```
PS C:\> Set-ADAccountControl -Identity SQLAdmin1 -AccountNotDelegated $True
```

此命令将 userAccountControl 的标志设置为“true”，以确保该账户无法被委托给其他人使用。

#### 示例 4：将一个用户账户设置为受信任的账户，以便进行委托身份验证
```
PS C:\> Set-ADAccountControl -Identity 'CN=IIS01 SvcAccount,OU=ServiceAccounts,OU=Managed,DC=FABRIKAM,DC=COM' -TrustedToAuthForDelegation $True
```

此命令将 userAccountControl 的标志设置为“已启用”，以确保该账户现在可以被信任用于身份验证和授权（即 delegations）。

### 示例 5：将指定的计算机设置为可信任的代理服务器
```
PS C:\> Set-ADAccountControl -Identity "FABRIKAM-SRV1" -TrustedForDelegation $True
```

此命令将指定的计算机设置为可信赖的代理服务器（即允许其接受其他计算机的委托操作）。

### 示例 6：设置一个永远不会过期的用户密码
```
PS C:\> Set-ADAccountControl -Identity EvanNa -PasswordNeverExpires $True
```

该命令将用户的密码设置为“永不过期”。

### 示例 7：设置用户账户必须拥有主目录
```
PS C:\> Set-ADAccountControl -Identity 'CN=Evan Narvaez,OU=HumanResources,OU=UserAccounts,DC=FABRIKAM,DC=COM' -HomedirRequired $True
```

此命令将用户账户设置为需要使用“主目录”（Home Directory）。

## 参数

### -AccountNotDelegated
该参数用于指示用户的安全上下文是否被委托给某个服务。当此参数设置为 `true` 时，即使服务账户已被配置为支持 Kerberos 委托功能，用户的账户安全上下文也不会被委托给该服务。此参数会为 Active Directory 账户设置 `AccountNotDelegated` 属性，并同时修改 Active Directory UAC（用户帐户控制）属性中的 `ADS_UF_NOT_DELEGATED` 标志。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowReversiblePasswordEncryption
该参数用于指示是否允许对该账户使用可逆的密码加密功能。它设置了账户的 **AllowReversiblePassword Encryption** 属性，同时也修改了 Active Directory 用户帐户控制（UAC）属性中的 **ADS_UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED** 标志。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”。

基本身份验证方法需要使用安全套接字层（SSL）连接。

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
该参数用于指示账户是否可以更改密码。如果希望禁止账户更改密码，请将其设置为 `$True`。此操作会修改账户的 `CannotChangePassword` 属性的布尔值。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前会提示您进行确认。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认凭据将是与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

如果执行该任务的代理程序没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

### -DoesNotRequirePreAuth
该参数用于指示使用用户账户或计算机账户登录时是否需要Kerberos预认证。它设置了Active Directory UAC属性中的**ADS_UF_DONT_require_PREAUTH**标志。此参数的可接受值包括：

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Enabled
Specifies whether an account is enabled.
An enabled account requires a password.
This parameter sets the **Enabled** property for an account object.
This parameter also sets the **ADS_UF_ACCOUNTDISABLE** flag of the Active Directory UAC attribute.The acceptable values for this parameter are:

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HomedirRequired
Indicates whether a home directory is required for the account.
This parameter sets the **ADS_UF_HOMEDIR_REQUIRED** flag of the Active Directory UAC attribute.The acceptable values for this parameter are:

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity
Specifies an Active Directory account object by providing one of the following property values.
The identifier in parentheses is the Lightweight Directory Access Protocol (LDAP) display name for the attribute.
The acceptable values for this parameter are:

- A distinguished name
- A GUID (objectGUID)
- A Security Identifier (objectSid)
- A SAM Account Name (sAMAccountName)

The cmdlet searches the default naming context or partition to find the object.
If two or more objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to an account object instance.

Derived types such as the following are also accepted:

- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADUser**

```yaml
Type: ADAccount
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -MNSLogonAccount
Indicates whether the account is a Majority Node Set (MNS) logon account.
This parameter also sets the **ADS_UF_MNS_LOGON_ACCOUNT** flag of the Active Directory UAC attribute.
The acceptable values for this parameter are:

- $False or 0
- $True or 1

You can use MNS logon accounts to configure a multi-node cluster without using a shared disk drive.

```yaml
Type: Boolean
Parameter Sets: (All)
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

In Active Directory Domain Services (AD DS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In AD LDS environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Partition* parameter will not take any default value.

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
Indicates whether the password of an account can expire.
This parameter sets the **PasswordNeverExpires** property of an account object.
This parameter also sets the **ADS_UF_DONT_EXPIRE_PASSWD** flag of the Active Directory UAC attribute.
The acceptable values for this parameter are:

- $False or 0
- $True or 1

Note: This parameter cannot be set to $True for an account that also has the **ChangePasswordAtLogon** property set to $True.

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PasswordNotRequired
Indicates whether the account requires a password.
This parameter sets the **PasswordNotRequired** property of an account, such as a user or computer account.
This parameter also sets the **ADS_UF_PASSWD_NOTREQD** flag of the Active Directory UAC attribute.
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
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
Specifies the Active Directory Domain Services instance to connect to, by providing one of the following values for a corresponding domain name or directory server.
The service may be any of the following: Active Directory Lightweight Domain Services, Active Directory Domain Services or Active Directory snapshot instance.

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

### -TrustedForDelegation
Indicates whether an account is trusted for Kerberos delegation.
A service that runs under an account that is trusted for Kerberos delegation can assume the identity of a client requesting the service.
This parameter sets the **TrustedForDelegation** property of an account object.
This value also sets the **ADS_UF_TRUSTED_FOR_DELEGATION** flag of the Active Directory UAC attribute.
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
Accept pipeline input: False
Accept wildcard characters: False
```

### -TrustedToAuthForDelegation
Indicates whether an account is enabled for delegation.
When this parameter is set to true, a service running under such an account can impersonate a client on other remote servers on the network.
This parameter sets the **ADS_UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION** flag of the Active Directory UAC attribute.
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
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseDESKeyOnly
Indicates whether an account is restricted to use only Data Encryption Standard encryption types for keys.
This parameter sets the **ADS_UF_USE_DES_KEY_ONLY** flag of the Active Directory UAC attribute.
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

### Microsoft.ActiveDirectory.Management.ADAccount
An account object is received by the *Identity* parameter.

Derived types, such as the following are also accepted:

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**

## 输出

### 无

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.
* This cmdlet does not work when connected to global catalog port.

## 相关链接

[Get-ADComputer](./Get-ADComputer.md)

[Get-ADServiceAccount](./Get-ADServiceAccount.md)

[Get-ADUser](./Get-ADUser.md)

[Windows PowerShell中的AD DS管理cmdlet](./activedirectory.md)

