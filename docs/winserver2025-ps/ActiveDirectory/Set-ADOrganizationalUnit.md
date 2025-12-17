---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADOrganizationalUnit
---

# Set-ADOrganizationalUnit

## 摘要
修改一个Active Directory组织单元（Organizational Unit）。

## 语法

### 身份
```
Set-ADOrganizationalUnit [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AuthType <ADAuthType>] [-City <String>]
 [-Clear <String[]>] [-Country <String>] [-Credential <PSCredential>] [-Description <String>]
 [-DisplayName <String>] [-Identity] <ADOrganizationalUnit> [-ManagedBy <ADPrincipal>] [-Partition <String>]
 [-PassThru] [-PostalCode <String>] [-ProtectedFromAccidentalDeletion <Boolean>] [-Remove <Hashtable>]
 [-Replace <Hashtable>] [-Server <String>] [-State <String>] [-StreetAddress <String>] [<CommonParameters>]
```

### 实例
```
Set-ADOrganizationalUnit [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -Instance <ADOrganizationalUnit> [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-ADOrganizationalUnit` cmdlet 用于修改 Active Directory 组织单元（OU）的属性。您可以使用该 cmdlet 的参数来修改常用的属性值。对于那些未与 cmdlet 参数关联的属性值，可以使用 `Add`、`Remove`、`Replace` 和 `Clear` 参数来进行修改。

`Identity` 参数用于指定要修改的 Active Directory 组织单元。您可以通过其唯一名称（Distinguished Name）或 GUID 来识别该组织单元。

您还可以将 *Identity* 参数设置为某个对象变量（例如 `$<localADOrganizationalUnitObject>`），或者通过管道将该对象传递给 *Identity* 参数。例如，您可以使用 **Get-ADOrganizationalUnit** cmdlet 来获取一个组织单元对象，然后通过管道将该对象传递给 **Set-ADOrganizationalUnit** cmdlet。

`Instance` 参数提供了一种通过应用对对象副本所做的更改来更新组织单元对象的方法。当您将 `Instance` 参数设置为一个已被修改的 Active Directory 组织单元对象的副本时，`Set-ADOrganizationalUnit` cmdlet 会对原始的组织单元对象执行相同的更改。要获取用于修改的对象副本，请使用 `Get-ADOrganizationalUnit` 命令。在指定 `Instance` 参数时，不应同时传递 `Identity` 参数。有关 `Instance` 参数的更多信息，请参阅其参数描述。

对于 Active Directory 轻量级目录服务（AD LDS）环境，必须指定 *Partition* 参数，以下两种情况除外：

- The cmdlet is run from an Active Directory provider drive.
- A default naming context or partition is defined for the AD LDS environment.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.

## 示例

### 示例 1：为某个组织单元（OU）设置描述
```
PS C:\> Set-ADOrganizationalUnit -Identity "OU=UserAccounts,DC=FABRIKAM,DC=COM" -Description "This Organizational Unit holds all of the users accounts of FABRIKAM.COM"
```

此命令用于设置具有以下唯一名称（Distinguished Name）的组织单位（Organizational Unit，简称OU）的描述：OU>UserAccounts,DC=FABRIKAM,DC=COM。

#### 示例 2：为某个组织单位（OU）设置 `ProtectedFromAccidentalDeletion` 属性
```
PS C:\> Set-ADOrganizationalUnit -Identity "OU=UserAccounts,DC=FABRIKAM,DC=COM" -ProtectedFromAccidentalDeletion $false
```

此命令将具有唯一名称“OU/UserAccounts,DC=FABRIKAM,DC=COM”的组织单元（Organizational Unit，简称OU）的 **ProtectedFromAccidentalDeletion** 属性设置为 $False。

### 示例 3：为组织单元（OU）设置位置属性
```
PS C:\> Set-ADOrganizationalUnit -Identity "OU=AsiaPacific,OU=Sales,OU=UserAccounts,DC=FABRIKAM,DC=COM" -Country "AU" -StreetAddress "45 Martens Place" -City Balmoral -State QLD -PostalCode 4171 -Replace @{co="Australia"}
```

此命令为以下组织单元（OU）设置相应的属性：**Country**、**City**、**State**、**PostalCode**：  
OU=AsiaPacific  
OU=Sales  
OU>UserAccounts  
DC=FABRIKAM  
DC=COM

### 示例 4：在 AD LDS 实例中为某个组织单元（OU）设置属性
```
PS C:\> Set-ADOrganizationalUnit -Identity "OU=Managed,DC=AppNC" -Server "FABRIKAM-SRV1:60000" -Country "UK"
```

此命令用于设置 AD LDS 实例中名为 “OU=Managed,DC=AppNC” 的组织单元（Organizational Unit，简称 OU）的 **Country** 属性。

### 示例 5：为管道连接的组织单元（OU）设置属性
```
PS C:\> Get-ADOrganizationalUnit -Identity "AccountingDepartment" | Set-ADOrganizationalUnit -ManagedBy "PattiFullerGroup"
```

这个命令会修改“AccountingDepartment”组织单元（OU）的**ManagedBy**属性。该命令首先使用**Get-ADOrganizationalUnit** cmdlet来获取“AccountingDepartment” OU，然后通过管道运算符将该对象传递给当前的cmdlet。

#### 示例 6：为本地组织单元（OU）设置属性，以修改 Active Directory 中的组织单元
```
PS C:\> $OrganizationalUnit = Get-ADOrganizationalUnit -Identity "AccountingDepartment"
PS C:\> $OrganizationalUnit.ManagedBy = "PattiFullerGroup"
PS C:\> Set-ADOrganizationalUnit -Instance $OrganizationalUnit
```

这个示例修改了“AccountingDepartment”组织单元（OU）的**ManagedBy**属性。首先，该示例会修改“AccountingDepartment” OU 的本地实例；接着，在使用 **Set-ADOrganizationalUnit** 命令时，将 *Instance* 参数设置为该本地实例的值。

## 参数

### -Add
用于指定要添加到对象属性中的值。该参数可用于向无法通过 cmdlet 参数修改的属性中添加一个或多个值。若要修改对象属性，必须使用轻量级目录访问协议（LDAP）显示名称。可以通过提供以逗号分隔的值列表来为单个属性指定多个值；如果需要为多个属性分别设置值，则可以使用分号进行分隔。此参数的格式如下：

```
-添加以下内容：
@{Attribute1LDAPDisplayName=value1, value2, ...;  
Attribute2LDAPDisplayName=value1, value2, ...;  
AttributeNLDAPDisplayName=value1, value2, ...}
```

当你同时使用“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）这些参数时，操作的执行顺序如下：

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

### -City
Specifies the town or city.
This parameter sets the **City** property of an OU object.
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
Specifies an array of object properties that are cleared in the directory.
Use this parameter to clear one or more values of a property that cannot be modified using a cmdlet parameter.
To modify an object property, you must use the LDAP display name.
You can modify more than one property by specifying a comma-separated list.
The format for this parameter is:

`-Clear Attribute1LDAPDisplayName, Attribute2LDAPDisplayName`

当你同时使用“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）这些参数时，操作的执行顺序如下：

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

### -Country
Specifies the country or region code.
This parameter sets the **Country** property of an OU object.
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
This parameter sets the value of the **Description** property for the OU object.
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
This parameter sets the **DisplayName** property of the OU object.
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

### -Identity
Specifies an Active Directory object by providing one of the following property values.
The identifier in parentheses is the LDAP display name for the attribute.
The acceptable values for this parameter are:

- A distinguished name
- A GUID (objectGUID)

The cmdlet searches the default naming context or partition to find the object.
If two or more objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

Derived types, such as the following are also accepted:

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy**
- **Microsoft.ActiveDirectory.Management.ADDomain**

```yaml
Type: ADOrganizationalUnit
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Instance
Specifies a modified copy of an OU object to use to update the actual Active Directory OU object.
When this parameter is used, any modifications made to the modified copy of the object are also made to the corresponding Active Directory object.
The cmdlet only updates the object properties that have changed.

The *Instance* parameter can only update organizational unit objects that have been retrieved by using the **Get-ADOrganizationalUnit** cmdlet.
When you specify the *Instance* parameter, you cannot specify other parameters that set properties on the object.

```yaml
Type: ADOrganizationalUnit
Parameter Sets: Instance
Aliases:

Required: True
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
Note that rules listed first are evaluated first and when a default value can be determined, no further rules are evaluated.

In AD DS environments, a default value for *Partition* are set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In AD LDS environments, a default value for *Partition* will be set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Partition* parameter does not take any default value.

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

### -PostalCode
Specifies the postal code or zip code.
This parameter sets the **PostalCode** property of an OU object.
The LDAP display name (**ldapDisplayName**) of this property is postalCode.

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

### -ProtectedFromAccidentalDeletion
Specifies whether to prevent the object from being deleted.
When this property is set to $True, you cannot delete the corresponding object without changing the value of the property.
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
Specifies that the cmdlet remove values of an object property.
Use this parameter to remove one or more values of a property that cannot be modified using a cmdlet parameter.
To remove an object property, you must use the LDAP display name.
You can remove more than one property by specifying a semicolon-separated list.
The format for this parameter is:

`-Remove @{Attribute1LDAPDisplayName=value[];   Attribute2LDAPDisplayName=value[]}`

当你同时使用“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）这些参数时，操作的执行顺序如下：

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

The default value for this parameter is determined by one of the following methods in the order that they are listed:

- By using the *Server* value from objects passed through the pipeline
- By using the server information associated with the AD DS Windows PowerShell provider drive, when the cmdlet runs in that drive
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

### -State
Specifies the state or province.
This parameter sets the **State** property of an OU object.
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
Specifies the street address.
This parameter sets the **StreetAddress** property of an OU object.
The LDAP display name (**ldapDisplayName**) of this property is street.

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

### None or Microsoft.ActiveDirectory.Management.ADOrganizationalUnit
An OU object is received by the *Identity* parameter.

An organizational unit object that was retrieved by using the **Get-ADOrganizationalUnit** cmdlet and then modified is received by the *Instance* parameter.

## 输出

### None or Microsoft.ActiveDirectory.Management.ADOrganizationalUnit
Returns the modified OU object when the *PassThru* parameter is specified.
By default, this cmdlet does not generate any output.

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADOrganizationalUnit](./Get-ADOrganizationalUnit.md)

[New-ADOrganizationalUnit](./New-ADOrganizationalUnit.md)

[Remove-ADOrganizationalUnit](./Remove-ADOrganizationalUnit.md)

