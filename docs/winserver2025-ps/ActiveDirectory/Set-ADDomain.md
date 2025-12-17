---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-addomain?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADDomain
---

# Set-ADDomain

## 摘要
修改一个 Active Directory 域名。

## 语法

### 身份（Identity）
```
Set-ADDomain [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AllowedDNSSuffixes <Hashtable>] [-AuthType <ADAuthType>]
 [-Clear <String[]>] [-Credential <PSCredential>] [-Identity] <ADDomain>
 [-LastLogonReplicationInterval <TimeSpan>] [-ManagedBy <ADPrincipal>] [-PassThru]
 [-PublicKeyRequiredPasswordRolling <Boolean>] [-Remove <Hashtable>] [-Replace <Hashtable>] [-Server <String>]
 [<CommonParameters>]
```

### 实例
```
Set-ADDomain [-WhatIf] [-Confirm] [-AllowedDNSSuffixes <Hashtable>] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] -Instance <ADDomain> [-LastLogonReplicationInterval <TimeSpan>]
 [-ManagedBy <ADPrincipal>] [-PassThru] [-PublicKeyRequiredPasswordRolling <Boolean>] [-Server <String>]
 [<CommonParameters>]
```

## 描述
`Set-ADDomain` cmdlet 可以修改 Active Directory 域的属性。您可以使用该 cmdlet 的参数来修改常用的属性值。对于那些未与 cmdlet 参数关联的属性值，可以通过使用 `Add`、`Replace`、`Clear` 和 `Remove` 参数来进行修改。

`Identity` 参数用于指定要修改的域。您可以通过该域的独特名称、GUID、安全标识符（SID）、DNS 域名或 NetBIOS 名称来识别该域。您还可以将 `Identity` 参数设置为一个对象变量（例如 `$<localDomainObject>`），或者通过管道将该对象传递给 `Identity` 参数。例如，您可以使用 `Get-ADDomain` cmdlet 获取一个域对象，然后通过管道将该对象传递给 `Set-ADDomain` cmdlet。

`Instance` 参数提供了一种通过应用对域对象副本所做的更改来更新该域对象的方法。当您将 `Instance` 参数设置为已修改的 Active Directory 域对象的副本时，`Set-ADDomain` cmdlet 会对原始域对象进行相同的更改。要获取用于修改的对象副本，请使用 `Get-ADDomain` 命令。在指定 `Instance` 参数时，不应同时传递 `Identity` 参数。有关 `Instance` 参数的更多信息，请参阅其相关描述。

## 示例

### 示例 1：设置域中某个属性的值
```
PS C:\> Set-ADDomain -Identity USER01 -AllowedDNSSuffixes @{Replace="USER01.com","corp.USER01.com"}
```

此命令将域USER01中的**AllowedDNSSuffixes**的值设置为{"USER01.com","corp.USER01.com"}。

### 示例 2：设置域中某个属性的值
```
PS C:\> Set-ADDomain -Identity USER01 -AllowedDNSSuffixes @{Add="corp.USER01.com"}
```

此命令将值 “corp.USER01.com” 添加到域 USER01 中的 **AllowedDNSSuffixes** 列表中。

### 示例 3：在域中设置 ManagedBy 属性
```
PS C:\> Set-ADDomain -Identity USER01 -ManagedBy 'CN=Domain Admins,CN=Users,DC=USER01,DC=COM'
```

此命令将域 USER01 中的 **ManagedBy** 属性设置为 CN=Domain Admins,CN=Users,DC=USER01,DC=COM。

### 示例 4：为当前登录的用户设置复制操作的间隔时间（以天为单位）
```
PS C:\> Get-ADDomain | Set-ADDomain -LastLogonReplicationInterval "10"
```

此命令将当前登录用户的域的 **LastLogonReplicationInterval** 设置为 10。

#### 示例 5：为某个域名设置 ManagedBy 属性
```
PS C:\> $Domain = Get-ADDomain -Identity London
PS C:\> $Domain.ManagedBy = PattiFuller
PS C:\> Set-ADDomain -Instance $Domain
```

此命令会修改伦敦域的 **ManagedBy** 属性。示例中首先修改了伦敦域的一个本地实例，然后将该本地实例指定为当前 cmdlet 的 *Instance* 参数。

#### 示例 6：启用密码过期机制，并为用于登录的公钥设置密码轮换规则
```
PS C:\> Set-ADDomain -Identity FABRIKAM -PublicKeyRequiredPasswordRolling $True
```

此命令将 FABRIKAM 域的 **msDS-ExpirePasswordsOnSmartCardOnlyAccounts** 属性设置为 $True。该设置允许需要使用公钥进行登录的用户账户的密码过期和自动更新功能。

## 参数

### -Add
用于指定要添加到对象属性中的值。使用此参数可以为无法通过 cmdlet 参数修改的属性添加一个或多个值。若要修改对象属性，必须使用轻量级目录访问协议（LDAP）显示名称。可以通过提供用逗号分隔的值列表来为单个属性指定多个值；如果需要为多个属性指定值，则可以使用分号将它们分开。该参数的格式如下：

请帮我将以下Markdown格式转换为中文：  

`-添加 @{Attribute1LDAPDisplayName=value1, value2, ...; Attribute2LDAPDisplayName=value1, value2, ...; AttributeNLDAPDisplayName=value1, value2, ...}`

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

### -AllowedDNSSuffixes
Modifies the list of domain name server (DNS) suffixes that are allowed in a domain.
This parameter sets the value of the **msDS-AllowedDNSSuffixes** attribute of the **domainDNS** object.
This parameter uses the following syntax to add, remove, replace, or clear DNS suffix values.

To add values:

`-AllowedDNSSuffixes @{Add=value1,value2,...}`

To remove values:

``-AllowedDNSSuffixes @{Remove=value3,value4,...}

To replace values:

`-AllowedDNSSuffixes @{Replace=value1,value2,...}`

To clear all values:

`-AllowedDNSSuffixes $Null`

You can specify more than one change by using a list separated by semicolons.
For example, use the following syntax to add and remove DNS suffix values:

`@{Add=value1,value2,...};@{Remove=value3,value4,...}`

当你同时使用“添加”（Add）、“替换”（Replace）、“清除”（Clear）和“删除”（Remove）这些参数时，操作的执行顺序如下：

- **Remove**
- **Add**
- **Replace**
- **Clear**

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
Use this parameter to clear one or more values of a property that cannot be modified using a cmdlet parameter.
To modify an object property, you must use the LDAP display name.
You can modify more than one property by specifying a comma-separated list.
The format for this parameter is:

`-Clear Attribute1LDAPDisplayName, Attribute2LDAPDisplayName`

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

### -Identity
Specifies an Active Directory domain object by providing one of the following property values.
The identifier in parentheses is the LDAP display name for the attribute.
All values are for the **domainDNS** object that represents the domain.
The acceptable values for this parameter are:

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A DNS domain name
- A NetBIOS domain name

The cmdlet searches the default naming context or partition to find the object.
If two or more objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to a domain object instance.

```yaml
Type: ADDomain
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Instance
Specifies a modified copy of a domain object to use to update the actual Active Directory domain object.
When this parameter is used, any modifications made to the modified copy of the object are also made to the corresponding Active Directory object.
The cmdlet only updates the object properties that have changed.

The *Instance* parameter can only update domain objects that have been retrieved by using the Get-ADDomain cmdlet.
When you specify the *Instance* parameter, you cannot specify other parameters that set properties on the object.

```yaml
Type: ADDomain
Parameter Sets: Instance
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LastLogonReplicationInterval
Specifies the time, in days, within which the last logon time of an account must be replicated across all domain controllers in the domain.
This parameter sets the **LastLogonReplicationInterval** property for a domain.
The LDAP display name (**ldapDisplayName**) for this property is **msDS-LogonTimeSyncInterval**.
The last logon replication interval must be at least one day.
Setting the last logon replication interval to a low value can significantly increase domain-wide replication.

```yaml
Type: TimeSpan
Parameter Sets: (All)
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

### -PublicKeyRequiredPasswordRolling
Specifies whether the domain enables password expiration and rolling for user account that require a smart card for interactive sign in.

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

### -Remove
Specifies that the cmdlet remove values of an object property.
Use this parameter to remove one or more values of a property that cannot be modified using a cmdlet parameter.
To remove an object property, you must use the LDAP display name.
You can remove more than one property by specifying a semicolon-separated list.
The format for this parameter is:

`-Remove @{Attribute1LDAPDisplayName=value[];   Attribute2LDAPDisplayName=value[]}`

When you use the *Add*, *Replace*, *Clear*, and *Remove* parameters together, the operations will be performed in the following order:

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

### -Server
指定要连接的 Active Directory 域服务实例，为此需要提供一个相应的域名或目录服务器的名称。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法之一确定的，确定顺序按照它们在列表中的排列顺序进行：

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft.ActiveDirectory.Management ADDomain
域对象通过“Identity”参数被接收。

通过使用 `Get-ADDomain` cmdlet 获取到的域对象在经过修改后，会被传递给 `Instance` 参数。

## 输出

### 无或 Microsoft.ActiveDirectory.Management ADDomain
当指定*PassThru*参数时，此cmdlet会返回修改后的域对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* This cmdlet does not work with Active Directory Lightweight Directory Services (AD LDS).
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADDomain](./Get-ADDomain.md)

[Get-ADDomainController](./Get-ADDomainController.md)

