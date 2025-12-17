---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adobject?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADObject
---

# Set-ADObject

## 摘要
修改一个 Active Directory 对象。

## 语法

### 身份证明
```
Set-ADObject [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AuthType <ADAuthType>] [-Clear <String[]>]
 [-Credential <PSCredential>] [-Description <String>] [-DisplayName <String>] [-Identity] <ADObject>
 [-Partition <String>] [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>] [-Remove <Hashtable>]
 [-Replace <Hashtable>] [-Server <String>] [<CommonParameters>]
```

### 实例
```
Set-ADObject [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Instance <ADObject>
 [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-ADObject` cmdlet 用于修改 Active Directory 对象的属性。您可以使用 cmdlet 的参数来修改常用的属性值；对于那些未与 cmdlet 参数关联的属性值，则可以通过使用 `Add`、`Replace`、`Clear` 和 `Remove` 参数来进行修改。

`Identity` 参数用于指定要修改的 Active Directory 对象。您可以通过该对象的唯一名称（Distinguished Name）或 GUID 来识别它。您也可以将 `Identity` 参数设置为一个对象变量（例如 `$<localObject>`），或者通过管道将该对象传递给 `Identity` 参数。例如，您可以使用 **Get-ADObject** cmdlet 获取一个对象，然后通过管道将该对象传递给 **Set-ADObject** cmdlet。

`Instance` 参数提供了一种通过应用对对象副本所做的更改来更新该对象的方法。当您将 `Instance` 参数设置为已修改的 Active Directory 对象的副本时，`Set-ADObject` cmdlet 会对原始对象进行相同的更改。要获取用于修改的对象副本，请使用 `Get-ADObject` 命令。在使用 `Instance` 参数时，不允许同时使用 `Identity` 参数。有关 `Instance` 参数的更多信息，请参阅其官方文档说明。

对于 Active Directory 轻量目录服务（AD LDS）环境，除非满足以下两种情况，否则必须指定 *Partition* 参数：

- The cmdlet is run from an Active Directory provider drive.
- A default naming context or partition is defined for the AD LDS environment.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (nTDSDSA) for the AD LDS instance.

## 示例

#### 示例 1：通过唯一名称为对象设置属性
```
PS C:\> Set-ADObject -Identity 'CN=PattiFu Direct Reports,OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM' -Description "Distribution List of Patti Fuller Direct Reports"
```

该命令为名为“CN=PattiFu Direct Reports,OU=Finance,OU>UserAccounts,DC=FABRIKAM,DC=COM”的对象设置了**Description**属性。

### 示例 2：为某个对象的地块添加一个站点
```
PS C:\> Set-ADObject -Identity 'CN=DEFAULTIPSITELINK,CN=IP,CN=Inter-Site Transports,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM' -Add @{siteList='CN=BO3,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM'} -Partition 'CN=Configuration,DC=FABRIKAM,DC=COM'
```

此命令将站点 CN=BO3、CN=Sites、CN=Configuration、DC=FABRIKAM、DC=COM 添加到具有唯一名称 CN=DEFAULTIPSITELINK、CN=IP、CN=Inter-Site Transports、CN=Sites、CN=Configuration、DC=FABRIKAM、DC=COM 的对象的属性 **siteList** 中。

### 示例 3：将 URL 添加到对象属性中
```
PS C:\> $UrlValues = @()
PS C:\> $UrlValues += "www.contoso.com"
PS C:\> $UrlValues += "www.fabrikam.com"
PS C:\> Set-ADObject -Identity "cdadd380-d3a8-4fd1-9d30-5cf72d94a056" -Add @{url=$UrlValues}
```

该命令将两个新的 URL 添加到具有 GUID `cdadd380-d3a8-4fd1-9d30-5cf72d94a056` 的对象的 `urlValues` 属性中。

### 示例 4：为多值属性设置值
```
PS C:\> $UrlValues = @()
PS C:\> $UrlValues += "www.contoso.com"
PS C:\> $UrlValues += "www.fabrikam.com"
PS C:\> Set-ADObject -Identity "cdadd380-d3a8-4fd1-9d30-5cf72d94a056" -Replace @{url=$UrlValues;description="Patti Fuller"}
```

该命令将多值属性 **url** 的旧值替换为新值，并设置属性 **description** 的值。

### 示例 5：从属性中删除一个值
```
PS C:\> Set-ADObject -Identity "cdadd380-d3a8-4fd1-9d30-5cf72d94a056" -Remove @{url="www.contoso.com"} -Replace @{description="Patti Fuller (European Manager)"}
```

该命令会从 **url** 属性中删除指定的值，并设置 **description** 属性的值。

### 示例 6：在对象上设置 UAC 位
```
PS C:\> $MyComp = Get-ADObject -Identity "cdadd380-d3a8-4fd1-9d30-5cf72d94a056" -Properties "userAccountControl","description"
PS C:\> $MyComp.userAccountControl = $MyComp.userAccountControl -bor 50
PS C:\> $MyComp.description = "Setting a new UAC on the object"
PS C:\> Set-ADObject -Instance $MyComp
```

此命令通过更新 **userAccountControl** 属性来为某个对象设置一个新的用户访问控制（UAC）位，并同时设置 **description** 属性的值。

### 示例 7：保护对象免遭意外删除
```
PS C:\> Set-ADObject -Identity "CN=InternalApps,DC=AppNC" -protectedFromAccidentalDeletion $True -Server "FABRIKAM-SRV1:60000"
```

此命令将容器中的CN属性设置为“InternalApps”，DC属性设置为“AppNC”，以便在AD LDS实例中保护该容器免于被意外删除。

### 示例 8：获取一个对象并修改其属性
```
PS C:\> Get-ADObject -Identity "SecurityLevel2AccessGroup" | Set-ADObject -DisplayName "Security Level 2"
```

此命令修改了 **SecurityLevel2AccessGroup** 对象的 **DisplayName** 属性。该命令使用 **Get-ADObject** cmdlet 来获取该对象，然后通过管道运算符将对象传递给当前的 cmdlet。

## 参数

### -Add
用于指定要添加到对象属性中的值。使用此参数可以为无法通过 cmdlet 参数修改的属性添加一个或多个值。若要修改对象属性，必须使用轻量级目录访问协议（LDAP）显示名称。您可以通过指定用逗号分隔的值列表来为某个属性设置多个值；如果需要为多个属性设置值，则可以使用分号将它们分开。该参数的格式如下：

请将以下内容翻译成中文：

`-添加 @{Attribute1LDAPDisplayName=value1, value2, ...; Attribute2LDAPDisplayName=value1, value2, ...; AttributeNLDAPDisplayName=value1, value2, ...}`

例如，如果您想从 `Phone-Office-Other` 属性（LDAP 显示名称 `otherTelephone`）中删除值 `555-222-2222`，并将值 `555-222-1111` 和 `555-222-3333` 添加到该属性中；同时将值 `555-222-9999` 添加到 `Phone-Mobile-Other` 属性（LDAP 显示名称 `otherMobile`）中，那么请按照以下方式设置 `Add` 和 `Remove` 参数：

`-添加 @{otherTelephone='555-222-1111', '555-222-3333'; otherMobile='555-222-9999' } -删除 @{otherTelephone='555-222-2222'}`

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

For example, if you want to clear the value for the Phone-Office-Other attribute (LDAP display name otherTelephone) set the *Clear* parameter as follows:

`-Clear otherTelephone`

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

### -Description
Specifies a description of the object.
This parameter sets the value of the **Description** property for the object.
The LDAP display name (**ldapDisplayName**) for this property is description.

The following example shows how to set this parameter to a sample description.

`-Description "Description of the object"`

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

The following example shows how to set this parameter:

`-DisplayName "Patti Fuller Laptop"`

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

- Distinguished name
- GUID (objectGUID)

The cmdlet searches the default naming context or partition to find the object.
If two or more objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

Derived types, such as the following, are also accepted:

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy**
- **Microsoft.ActiveDirectory.Management.ADDomain**

This example shows how to set this parameter to an **ADObject** object instance named ADObjectInstance:

`-Identity $ADObjectInstance`

```yaml
Type: ADObject
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Instance
Specifies a modified copy of an Active Directory object to use to update the actual Active Directory object.
When you specify this parameter, any modifications made to the modified copy of the object are also made to the corresponding Active Directory object.
The cmdlet only updates the object properties that have changed.

The *Instance* parameter can only update Active Directory objects that have been retrieved by using the **Get-ADObject** cmdlet.
When you specify the *Instance* parameter, you cannot specify other parameters that set properties on the object.

The following is an example of how to use the **Get-ADObject** cmdlet to retrieve an instance of the object.
The object is modified by using the PowerShell command line.
Then the **Set-ADObject** cmdlet saves the changes to the Active Directory object.

Step 1: Get a local instance of the object:

`$ObjectInstance = Get-ADObject -Identity  "CN=someObject, DC=contoso,DC=com"`

Step 2: Modify one or more properties of the object instance:

`$ObjectInstance.Description = "New Description"`

Step3: Save your changes to the object:

`Set-ADObject -Instance $ObjectInstance`

```yaml
Type: ADObject
Parameter Sets: Instance
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Partition
Specifies the distinguished name of an Active Directory partition.
The distinguished name must be one of the naming contexts on the current directory server.
The cmdlet searches this partition to find the object defined by the *Identity* parameter.

The following two examples show how to specify a value for this parameter.

`-Partition "CN=Configuration,DC=EUROPE,DC=TEST,DC=CONTOSO,DC=COM"`

`-Partition "CN=Schema,CN=Configuration,DC=EUROPE,DC=TEST,DC=CONTOSO,DC=COM"`

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
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context. To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent (DSA) object (nTDSDSA) for the AD LDS instance.
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

### -ProtectedFromAccidentalDeletion
Specifies whether to prevent the object from being deleted.
When this property is set to true, you cannot delete the corresponding object without changing the value of the property.
The acceptable values for this parameter are:

- $False or 0
- $True or 1

The following example shows how to set this parameter to $True.

`-ProtectedFromAccidentalDeletion $True`

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

For example, if you want to add the values blue and green and remove the value pink from a property with a LDAP display name of FavColors, set the *Add* and *Remove* parameters as follows:

`-Add @{FavColors=Blue,Green} -Remove {FavColors=Pink}`

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

Domain name values:

- Fully qualified domain name (FQDN)
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- A NetBIOS name
- Fully qualified directory server name and port

The default value for the *Server* parameter is determined by one of the following methods in the order that they are listed:

- By using *Server* value from objects passed through the pipeline.
- By using the server information associated with the Active Directory PowerShell provider drive, when running under that drive.
- By using the domain of the computer running PowerShell.

The following example shows how to specify a FQDN as the parameter value.

`-Server "corp.contoso.com"`

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

### None or Microsoft.ActiveDirectory.Management.ADObject
An Active Directory object is received by the *Identity* parameter.
Derived types, such as the following are also accepted:

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADOrganizationalUnit**
- **Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy**
- **Microsoft.ActiveDirectory.Management.ADDomain**

An object that was retrieved by using the **Get-ADObject** cmdlet and then modified is received by the *Instance* parameter.

## 输出

### None or Microsoft.ActiveDirectory.Management.ADObject
Returns the modified object when the *PassThru* parameter is specified.
By default, this cmdlet does not generate any output.

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADObject](./Get-ADObject.md)

[Move-ADObject](./Move-ADObject.md)

[New-ADObject](./New-ADObject.md)

[Remove-ADObject](./Remove-ADObject.md)

[重命名 AD 对象](./Rename-ADObject.md)

[恢复 AD 对象](./Restore-ADObject.md)

