---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adauthenticationpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADAuthenticationPolicy
---

# Set-ADAuthenticationPolicy

## 摘要
修改 Active Directory 域服务（Active Directory Domain Services）的身份验证策略对象。

## 语法

### 身份证明
```
Set-ADAuthenticationPolicy [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AuthType <ADAuthType>] [-Clear <String[]>]
 [-ComputerAllowedToAuthenticateTo <String>] [-ComputerTGTLifetimeMins <Int32>] [-Credential <PSCredential>]
 [-Description <String>] [-Enforce <Boolean>] [-Identity] <ADAuthenticationPolicy> [-PassThru]
 [-ProtectedFromAccidentalDeletion <Boolean>] [-Remove <Hashtable>] [-Replace <Hashtable>]
 [-RollingNTLMSecret <ADStrongNTLMPolicyType>] [-Server <String>] [-ServiceAllowedToAuthenticateFrom <String>]
 [-ServiceAllowedToAuthenticateTo <String>] [-ServiceAllowedNTLMNetworkAuthentication <Boolean>]
 [-ServiceTGTLifetimeMins <Int32>] [-UserAllowedToAuthenticateFrom <String>]
 [-UserAllowedToAuthenticateTo <String>] [-UserAllowedNTLMNetworkAuthentication <Boolean>]
 [-UserTGTLifetimeMins <Int32>] [<CommonParameters>]
```

### 实例
```
Set-ADAuthenticationPolicy [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -Instance <ADAuthenticationPolicy> [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-ADAuthenticationPolicy` cmdlet 用于修改 Active Directory® Domain Services 认证策略的属性。该 cmdlet 的参数可以指定对象中常用的属性；未与 cmdlet 参数关联的属性则可以通过 `Add`、`Remove`、`Replace` 和 `Clear` 参数来进行修改。

`Identity` 参数用于指定要修改的 Active Directory 域服务（Domain Services）身份验证策略。您可以使用唯一名称（distinguished name）、GUID 或普通名称来指定身份验证策略对象。此外，还可以使用 `Identity` 参数来引用包含身份验证策略对象的变量，或者通过管道运算符（pipeline operator）将该对象传递给 `Identity` 参数。若要获取身份验证策略对象，请使用 `Get-ADAuthenticationPolicy` cmdlet。

使用 `Instance` 参数来指定一个身份验证策略对象，作为被修改对象的模板。请不要同时指定 `Instance` 参数和 `Identity` 参数。

## 示例

### 示例 1：修改指定身份验证策略的属性
```
PS C:\> Set-ADAuthenticationPolicy -Identity AuthenticationPolicy01 -Description "TestDescription" -UserTGTLifetimeMins 45
```

此命令会修改指定身份验证策略的描述属性以及 **UserTGTLifetimeMins** 属性。

### 示例 2：通过使用实例来修改身份验证策略的属性。
```
PS C:\> $AuthPolicy = Get-ADAuthenticationPolicy -Identity AuthenticationPolicy02
PS C:\> $AuthPolicy.Description = 'testDescription'
PS C:\> $AuthPolicy.UserTGTLifetimeMins = 60
PS C:\> Set-ADAuthenticationPolicy -Instance $AuthPolicy
```

这个示例首先使用 **Get-ADAuthenticationPolicy** cmdlet 获取名为 AuthenticationPolicy02 的身份验证策略。该身份验证策略对象被存储在名为 $authPolicy 的变量中。

接下来的命令会修改变量中对象的属性，而最后一个命令则会指定“Instance”参数，以便将这些更改应用到存储在 `$authPolicy` 变量中的认证策略中。

### 示例 3：修改多个身份验证策略
```
PS C:\> Get-ADAuthenticationPolicy -Filter 'UserTGTLifetimeMins -le 50' | Set-ADAuthenticationPolicy -UserTGTLifetimeMins 60
```

此命令使用 **Get-ADAuthenticationPolicy** cmdlet 和 *Filter* 参数来获取所有将 **UserTGTLifetimeMins** 值设置为低于 50 分钟的认证策略。随后，管道运算符会将过滤后的结果传递给 **Set-AdAuthenticationPolicy**，该命令会将新的 **UserTGTLifetimeMins** 值设置为 60 分钟。

### 示例 4：替换现有的属性值
```
PS C:\> Set-ADAuthenticationPolicy -Identity AuthenticationPolicy03 -Replace @{description="New Description"}
```

该命令会用 *Replace* 参数指定的新描述内容替换 **AuthenticationPolicy03** 对象中现有的 `description` 属性。

## 参数

### -Add
用于指定要添加到对象属性中的一组值。此参数可用于向无法通过参数进行修改的属性中添加一个或多个值。要标识某个属性，请使用在 Active Directory 域服务架构中为其定义的轻量级目录访问协议（LDAP）显示名称。

请按照以下格式指定属性及其值：@{'AttributeLDAPDisplayName'=value}。

要为某个属性指定多个值，请使用逗号分隔这些值。如果需要为多个属性指定值，可以使用分号来分隔各个属性值对。

当同时指定“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）参数时，这些操作将按照以下顺序执行：

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

### -Clear
Specifies an array of object properties that are cleared in the directory.
Use this parameter to clear one or more values of a property that cannot be modified using a parameter.
To modify an object property, you must specify the LDAP display name.
You can modify more than one property by specifying a comma-separated list.

当同时指定“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）参数时，这些操作将按照以下顺序执行：

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

### -ComputerAllowedToAuthenticateTo
Specifies the security descriptor definition language (SDDL) string of the security descriptor used to determine if the computer can authenticate to this account.

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

### -ComputerTGTLifetimeMins
Specifies the lifetime in minutes for non-renewable ticket granting tickets (TGTs) for computer accounts.

```yaml
Type: Int32
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
Specifies a user account that has permission to perform the task.
The default is the current user.
Type a user name, such as "User01" or "Domain01\User01", or enter a **PSCredential** object, such as one generated by the **Get-Credential** cmdlet.

By default, the cmdlet uses the credentials of the currently logged on user unless the cmdlet is run from an Active Directory Domain Services Windows PowerShell provider drive.
If you run the cmdlet in a provider drive, the account associated with the drive is the default.

If you specify credentials that do not have permission to perform the task, the cmdlet returns an error.

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
Specifies a description for the object.
This parameter sets the value of the description property for the object.
The LDAP display name (**ldapDisplayName**) for this property is "description".

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

### -Enforce
Indicates whether the authentication policy is enforced.
Specify $True to set the authentication policy to enforced.
Specify $False to set the authentication policy to not enforced.

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

### -Identity
Specifies an Active Directory Domain Services authentication policy object.
Specify the authentication policy object in one of the following formats:

- Distinguished Name
- GUID
- Name

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

The cmdlet searches the default naming context or partition to find the object.
If the cmdlet finds two or more objects, the cmdlet returns a non-terminating error.

```yaml
Type: ADAuthenticationPolicy
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Instance
Specifies a modified copy of an **ADAuthenticationPolicy** object to use to update the actual **ADAuthenticationPolicy** object.
When you specify this parameter, any modifications made to the modified copy of the object are also made to the corresponding **ADAuthenticationPolicy** object.
The cmdlet only updates the object properties that have changed.
When you specify the *Instance* parameter, you cannot specify other parameters that set properties on the object.

To get the **ADAuthenticationPolicy** object to use to update the **ADAuthenticationPolicy** on which the cmdlet runs, use the **Get-ADAuthenticationPolicy** cmdlet.

```yaml
Type: ADAuthenticationPolicy
Parameter Sets: Instance
Aliases:

Required: True
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

### -ProtectedFromAccidentalDeletion
Indicates whether to prevent the object from being deleted.
When this property is set to true, you cannot delete the corresponding object without changing the value of the property.
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

### -Remove
Specifies that the cmdlet remove the values of an object property.
Use this parameter to remove one or more values of a property that cannot be modified using a cmdlet parameter.
To remove an object property, you must specify the LDAP display name.

请按照以下格式指定属性及其值：@{'AttributeLDAPDisplayName'=value}。

要为某个属性指定多个值，请使用逗号分隔这些值。如果需要为多个属性指定值，可以使用分号来分隔各个属性值对。

当同时指定“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）参数时，这些操作将按照以下顺序执行：

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
Specifies a list of values for an object property that replaces the current values.
Use this parameter to replace one or more values of a property that cannot be modified using a cmdlet parameter.
To modify an object property, you must specify the LDAP display name.

请按照以下格式指定属性及其值：@{'AttributeLDAPDisplayName'=value}。

要为某个属性指定多个值，请使用逗号分隔这些值。如果需要为多个属性指定值，可以使用分号来分隔各个属性值对。

当同时指定“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）参数时，这些操作将按照以下顺序执行：

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

### -RollingNTLMSecret
Beginning with Windows 10, version 1703, this feature is deprecated and should not be configured in Active Directory.

```yaml
Type: ADStrongNTLMPolicyType
Parameter Sets: Identity
Aliases:
Accepted values: Disabled, Optional, Required

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
Specifies the Active Directory Domain Services instance to which to connect, by providing one of the following values for a corresponding domain name or directory server.
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

- By using the **Server** value from objects passed through the pipeline
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

### -ServiceAllowedNTLMNetworkAuthentication
Specifies that the policy allows NTLM network authentication if the service account has an access control expression specified by the *ServiceAllowedToAuthenticateFrom* parameter.

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

### -ServiceAllowedToAuthenticateFrom
Specifies an access control expression used to determine from which devices the service can authenticate.

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

### -ServiceAllowedToAuthenticateTo
Specifies the SDDL string of the security descriptor used to determine if the service can authenticate to this account.

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

### -ServiceTGTLifetimeMins
Specifies the lifetime in minutes for non-renewable TGTs for service accounts.

```yaml
Type: Int32
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UserAllowedNTLMNetworkAuthentication
Indicates that the policy allows NTLM network authentication if the user account has an access control expression specified by the *UserAllowedToAuthenticateFrom* parameter.

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

### -UserAllowedToAuthenticateFrom
Specifies an access control expression used to determine from which devices the users can authenticate.

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

### -UserAllowedToAuthenticateTo
Specifies the SDDL string of the security descriptor used to determine if the users can authenticate to this account.

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

### -UserTGTLifetimeMins
Specifies the lifetime in minutes for non-renewable TGTs for user accounts.

```yaml
Type: Int32
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

### None or Microsoft.ActiveDirectory.Management.ADAuthenticationPolicy
This cmdlet accepts an authentication policy object.

## 输出

### System.Object
Returns one or more objects.

## 备注

## 相关链接

[Get-ADAuthenticationPolicy](./Get-ADAuthenticationPolicy.md)

[New-ADAuthenticationPolicy](./New-ADAuthenticationPolicy.md)

[Remove-ADAuthenticationPolicy](./Remove-ADAuthenticationPolicy.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

