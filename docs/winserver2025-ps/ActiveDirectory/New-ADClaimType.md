---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adclaimtype?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADClaimType
---

# 新的广告声明类型（New-ADClaimType）

## 摘要
在 Active Directory 中创建一个新的声明类型（claim type）。

## 语法

### SourceAttribute（默认值）
```
New-ADClaimType [-WhatIf] [-Confirm] [-AppliesToClasses <String[]>] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Description <String>] [-DisplayName] <String> [-Enabled <Boolean>]
 [-ID <String>] [-Instance <ADClaimType>] [-IsSingleValued <Boolean>] [-OtherAttributes <Hashtable>]
 [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>] [-RestrictValues <Boolean>] [-Server <String>]
 -SourceAttribute <String> [-SuggestedValues <ADSuggestedValueEntry[]>] [<CommonParameters>]
```

### SourceOID
```
New-ADClaimType [-WhatIf] [-Confirm] [-AppliesToClasses <String[]>] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Description <String>] [-DisplayName] <String> [-Enabled <Boolean>]
 [-ID <String>] [-Instance <ADClaimType>] [-IsSingleValued <Boolean>] [-OtherAttributes <Hashtable>]
 [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>] [-RestrictValues <Boolean>] [-Server <String>]
 -SourceOID <String> [<CommonParameters>]
```

### SourceTransformPolicy
```
New-ADClaimType [-WhatIf] [-Confirm] [-AppliesToClasses <String[]>] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Description <String>] [-DisplayName] <String> [-Enabled <Boolean>]
 [-ID <String>] [-Instance <ADClaimType>] [-IsSingleValued <Boolean>] [-OtherAttributes <Hashtable>]
 [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>] [-RestrictValues <Boolean>] [-Server <String>]
 [-SourceTransformPolicy] [-SuggestedValues <ADSuggestedValueEntry[]>] -ValueType <ADClaimValueType>
 [<CommonParameters>]
```

## 描述
`New-ADClaimType` cmdlet 可以在 Active Directory 中创建一个新的声明类型（claim type）。

## 示例

### 示例 1：创建一种新的用户声明类型，并为其指定一个显示名称
```
PS C:\> New-ADClaimType -DisplayName "Title" -SourceAttribute "title"
```

该命令创建了一种新的用户声明类型，其显示名称为“Title”，该名称来源于 Active Directory 中的 “Title” 属性。

### 示例 2：创建一种新的用户声明类型，并为其指定一个显示名称
```
PS C:\> $FullTime = New-Object Microsoft.ActiveDirectory.Management.ADSuggestedValueEntry("FTE", "Full-Time", "Full-time employee")
PS C:\> $Intern = New-Object Microsoft.ActiveDirectory.Management.ADSuggestedValueEntry("Intern", "Intern", "Student employee")
PS C:\> $Contractor = New-Object Microsoft.ActiveDirectory.Management.ADSuggestedValueEntry("Contractor", "Contractor", "Contract employee")
PS C:\> New-ADClaimType -DisplayName "Employee Type" -SourceAttribute "employeeType" -SuggestedValues $FullTime,$Intern,$Contractor
```

这个示例创建了一种新的用户声明类型，其显示名称为“Employee Type”（员工类型），该类型的值来源于 Active Directory 的 **employeeType** 属性。建议的取值为 FTE（全职员工）、Intern（实习生）和 Contractor（承包商）。使用这种声明类型的应用程序将允许用户从中选择一个作为该声明类型的实际值。

### 示例 3：创建一种新的设备声明类型，该类型具有显示名称以及源和目标信息
```
PS C:\> New-ADClaimType -DisplayName "Bitlocker Enabled" -SourceOID "1.3.6.1.4.1.311.67.1.1" -Enabled $False
```

此命令创建了一种新的设备声明类型，其显示名称为“BitLocker 已启用”，对应的源 OID 为 1.3.6.1.4.1.311.67.1.1。该声明类型的默认状态被设置为“禁用”（disabled）。

### 示例 4：创建一种新的用户声明类型，其显示名称来源于 Active Directory 的某个属性
```
PS C:\> New-ADClaimType -DisplayName "Title" -SourceAttribute "title" -ID "ad://ext/title"
```

该命令创建了一种新的用户声明类型，其显示名称为“Title”，该名称来源于 Active Directory 中的 “Title” 属性；同时，该类型的 ID 被设置为 ad://ext/title。

在多森林环境中，只有当需要让相同的声明类型在所有森林中都能正常工作时，才应该手动设置该声明类型的ID。默认情况下，New-ADClaimType会自动生成声明类型的ID。为了让不同森林中的声明类型被视为相同，它们的ID必须是一致的。

## 参数

### -AppliesToClasses
此参数用于指定该声明适用的安全主体类别。该参数的可能取值包括以下内容，或任何从这些基础类型派生的 Active Directory 类型：

- User
- Computer
- InetOrgPerson
- msDS-ManagedServiceAccount
- msDS-GroupManagedServiceAccount

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
The Lightweight Directory Access Protocol (LDAP) display name (**ldapDisplayName**) for this property is description.

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
Specifies the display name of the claim type, which must be unique.
The display name of a claim type can be used as an identity in other Active Directory cmdlets.
For example, if the display name of a claim type is Employee Type, then you can use the Get-ADClaimType cmdlet to retrieve the Employee Type claim type.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Enabled
Specifies whether the claim type is enabled.

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

### -ID
Specifies the claim type ID.
This is an optional parameter.
By default, New-ADClaimType generates the ID automatically.

The ID should only be set manually in a multi-forest environment where the same claim types need to work across forests.
For claim types to be considered identical across forests, their ID must be the same.

To specify the ID, the ID string must conform to the following format:

- The ID must have a maximum of 37 characters.
- The ID must have at least one slash (/).
- The ID must have at least one colon before the first slash.
- The ID must not have the slash as the last character.
- The ID must contain valid file characters only.

An example is ad://ext/BusinessImpact.

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
Specifies an instance of a claim type object to use as a template for a new claim type object.

You can use an instance of an existing claim type object as a template or you can construct a new claim type object by using the Windows PowerShell command line or by using a script.

Method 1: Use an existing claim type object as a template for a new object.
To retrieve an instance of an existing claim type object, use a cmdlet such as **Get-ADClaimType**.
Then provide this object to the *Instance* parameter of the **New-ADClaimType** cmdlet to create a new claim type object.
You can override property values of the new object by setting the appropriate parameters.

Method 2: Create a new claim type and set the property values by using the Windows PowerShell command line interface.
Then pass this object to the *Instance* parameter of the **New-ADClaimType** cmdlet to create the new claim type object.

Note: Specified attributes are not validated, so attempting to set attributes that do not exist or cannot be set will raise an error.

```yaml
Type: ADClaimType
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsSingleValued
Specifies whether the claim type is single valued or multi-valued.

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

### -OtherAttributes
Specifies object attribute values for attributes that are not represented by cmdlet parameters.
You can set one or more parameters at the same time with this parameter.
If an attribute takes more than one value, you can assign multiple values.
To identify an attribute, specify the LDAPDisplayName (**ldapDisplayName**) defined for it in the Active Directory schema.

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

### -ProtectedFromAccidentalDeletion
Specifies whether to prevent the object from being deleted.
When this property is set to $True, you cannot delete the corresponding object without changing the value of the property.
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

### -RestrictValues
This parameter is used to specify whether the claim type may have values outside of the *SuggestedValues* parameter.
If this is set to true, then the claim should only have values specified in the *SuggestedValues* parameter.

Note that Active Directory does not enforce this restriction.
It is up to the applications that use these claims to enforce the restriction.

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

### -SourceAttribute
Specifies an Active Directory attribute from which this claim type is based, and from which the claim value is obtained.
The input must be the distinguished name, Name, or GUID of the attribute definition in the schema.

Acceptable values include attributes of the following schema class objects: **User**, **InetOrgPerson**, **Computer**, **ManagedServiceAccount**, **GroupManagedServiceAccount**, and **Auxiliary**, except for the following attributes:

在模式中被标记为“已废弃”的属性：  
- 被阻止使用的属性，如 **dBCSPwd**、**lmPwdHistory** 和 **unicodePwd**；  
- 不会被复制的属性；  
- 在只读域控制器上不可用的属性；  
- 语法不符合以下规范的属性。

- String Object (DS-DN)
- String (Unicode)
- Boolean
- Integer
- Large Integer
- String (OID)
- String (SD)

```yaml
Type: String
Parameter Sets: SourceAttribute
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SourceOID
Specifies a string that can be used to configure a certificate-based claim type source.
For example, use this parameter to create certificate-based claim types when you want to use smartcard logon claims for authorization decisions.
The *SourceOID* parameter uses the string representation of an object identifier (OID) from the issuance policy found in the certificate and on the certificate template when using Active Directory Certificate Services.
An example of an OID is 1.3.6.1.4.1.311.47.2.5.

```yaml
Type: String
Parameter Sets: SourceOID
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SourceTransformPolicy
Indicates that the claim type is sourced from the claims transformation policy engine.

```yaml
Type: SwitchParameter
Parameter Sets: SourceTransformPolicy
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SuggestedValues
Specifies one or more suggested values for the claim type.
An application may choose to present this list of suggested values for the user to choose from.
When the *RestrictValues* parameter is set to a value of $True, the application should limit the user to selecting values from this list only.

```yaml
Type: ADSuggestedValueEntry[]
Parameter Sets: SourceAttribute, SourceTransformPolicy
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ValueType
Specifies the value type for this claim type.
The following are the valid value types:

- Int64
- UInt64
- String
- FQBN
- SID
- Boolean
- OctetString

```yaml
Type: ADClaimValueType
Parameter Sets: SourceTransformPolicy
Aliases:
Accepted values: Invalid, Int64, UInt64, String, FQBN, SID, Boolean, OctetString

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft ActiveDirectory.Management_ADClaimType

## 输出

### 无值或 Microsoft ActiveDirectory.Management_ADClaimType

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADClaimType](./Get-ADClaimType.md)

[Remove-ADClaimType](./Remove-ADClaimType.md)

[Set-ADClaimType](./Set-ADClaimType.md)

[Windows PowerShell中的AD DS管理命令集](./activedirectory.md)

