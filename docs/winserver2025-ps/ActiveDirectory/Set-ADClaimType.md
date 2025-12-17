---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adclaimtype?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADClaimType
---

# Set-ADClaimType

## 摘要
在 Active Directory 中修改一种声明类型（claim type）。

## 语法

### 身份验证（默认设置）
```
Set-ADClaimType [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AppliesToClasses <String[]>] [-AuthType <ADAuthType>]
 [-Clear <String[]>] [-Credential <PSCredential>] [-Description <String>] [-DisplayName <String>]
 [-Enabled <Boolean>] [-Identity] <ADClaimType> [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>]
 [-Remove <Hashtable>] [-Replace <Hashtable>] [-RestrictValues <Boolean>] [-Server <String>]
 [-SuggestedValues <ADSuggestedValueEntry[]>] [<CommonParameters>]
```

### SourceTransformPolicy
```
Set-ADClaimType [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AppliesToClasses <String[]>] [-AuthType <ADAuthType>]
 [-Clear <String[]>] [-Credential <PSCredential>] [-Description <String>] [-DisplayName <String>]
 [-Enabled <Boolean>] [-Identity] <ADClaimType> [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>]
 [-Remove <Hashtable>] [-Replace <Hashtable>] [-RestrictValues <Boolean>] [-Server <String>]
 [-SourceTransformPolicy] [-SuggestedValues <ADSuggestedValueEntry[]>] [<CommonParameters>]
```

### SourceAttribute
```
Set-ADClaimType [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AppliesToClasses <String[]>] [-AuthType <ADAuthType>]
 [-Clear <String[]>] [-Credential <PSCredential>] [-Description <String>] [-DisplayName <String>]
 [-Enabled <Boolean>] [-Identity] <ADClaimType> [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>]
 [-Remove <Hashtable>] [-Replace <Hashtable>] [-RestrictValues <Boolean>] [-Server <String>]
 -SourceAttribute <String> [-SuggestedValues <ADSuggestedValueEntry[]>] [<CommonParameters>]
```

### SourceOID
```
Set-ADClaimType [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AppliesToClasses <String[]>] [-AuthType <ADAuthType>]
 [-Clear <String[]>] [-Credential <PSCredential>] [-Description <String>] [-DisplayName <String>]
 [-Enabled <Boolean>] [-Identity] <ADClaimType> [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>]
 [-Remove <Hashtable>] [-Replace <Hashtable>] [-RestrictValues <Boolean>] [-Server <String>]
 -SourceOID <String> [<CommonParameters>]
```

### 实例
```
Set-ADClaimType [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -Instance <ADClaimType> [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-ADClaimType` cmdlet 可用于修改 Active Directory 中的声明类型（claim type）。

## 示例

### 示例 1：将用户声明显示名称设置为来自 Active Directory 的来源值
```
PS C:\> Set-ADClaimType -Identity Title -SourceAttribute "title"
```

此命令将用户声明类型设置为“Title”（显示名称为“标题”），并将其数据来源设定为 Active Directory 中的 **title** 属性。

### 示例 2：设置用户声明的建议值
```
PS C:\> $FullTime = New-Object Microsoft.ActiveDirectory.Management.ADSuggestedValueEntry("FTE", "Full-Time", "Full-time employee")
PS C:\> $Intern = New-Object Microsoft.ActiveDirectory.Management.ADSuggestedValueEntry("Intern", "Intern", "Student employee")
PS C:\> $Contractor = New-Object Microsoft.ActiveDirectory.Management.ADSuggestedValueEntry("Contractor", "Contractor", "Contract employee")
PS C:\> Set-ADClaimType -Identity "Employee Type" -SuggestedValues $FullTime,$Intern,$Contractor
```

此命令将用户声明类型（显示名称为“Employee Type”）的建议值设置为“FTE”、“Intern”和“Contractor”。使用该声明类型的应用程序将允许其用户从这些建议值中选择一个作为该声明类型的实际值。

### 示例 3：设置某种索赔类型的源 OID（Object Identifier），然后将其禁用
```
PS C:\> Set-ADclaimType -Identity "Bitlocker Enabled" -SourceOID "1.3.6.1.4.1.311.67.1.1" -Enabled $False
```

这个示例将显示名称为“Bitlocker Enabled”的声明类型的源OID设置为1.3.6.1.4.1.311.67.1.1，并禁用了该声明类型。

### 示例 4：将一种命名过的声明类型设置为来自声明转换策略引擎的数据源
```
PS C:\> Set-ADClaimType -Identity SourceForest -SourceTransformPolicy
```

该命令将名为“SourceForest”的声明类型设置为从声明转换策略引擎中获取数据。

## 参数

### -Add
用于指定要添加到对象属性中的值。此参数可用于向无法通过 cmdlet 参数修改的属性中添加一个或多个值。若要修改对象属性，必须使用轻量级目录访问协议（LDAP）显示名称。可以通过提供用逗号分隔的值列表来为某个属性指定多个值；如果需要为多个属性指定值，则可以使用分号将它们分开。该参数的格式如下：

请帮我将以下Markdown内容转换为中文：  

`-Add @{Attribute1LDAPDisplayName=value1, value2, ...; Attribute2LDAPDisplayName=value1, value2, ...; AttributeNLDAPDisplayName=value1, value2, ...}`

当你同时使用“添加”（Add）、“替换”（Replace）、“清除”（Clear）和“删除”（Remove）这些参数时，操作会按照以下顺序进行：

- **Remove**
- **Add**
- **Replace**
- **Clear**

```yaml
Type: Hashtable
Parameter Sets: Identity, SourceTransformPolicy, SourceAttribute, SourceOID
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AppliesToClasses
Specifies the names, GUIDs, or distinguished names of the schema classes to which this claim type is applied.

```yaml
Type: String[]
Parameter Sets: Identity, SourceTransformPolicy, SourceAttribute, SourceOID
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

-Clear Attribute1LDAPDisplayName, Attribute2LDAPDisplayName

当你同时使用“添加”（Add）、“替换”（Replace）、“清除”（Clear）和“删除”（Remove）这些参数时，操作会按照以下顺序进行：

- **Remove**
- **Add**
- **Replace**
- **Clear**

```yaml
Type: String[]
Parameter Sets: Identity, SourceTransformPolicy, SourceAttribute, SourceOID
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
Parameter Sets: Identity, SourceTransformPolicy, SourceAttribute, SourceOID
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisplayName
Specifies the display name of the claim type.
The display name of the claim type must be unique.
The display name of a claim type can be used as an identity in other Active Directory cmdlets.

```yaml
Type: String
Parameter Sets: Identity, SourceTransformPolicy, SourceAttribute, SourceOID
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Enabled
Specifies if the claim type is enabled.

```yaml
Type: Boolean
Parameter Sets: Identity, SourceTransformPolicy, SourceAttribute, SourceOID
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
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

```yaml
Type: ADClaimType
Parameter Sets: Identity, SourceTransformPolicy, SourceAttribute, SourceOID
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
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
Then pass this object to the *Instance* parameter of the New-ADClaimType cmdlet to create the new claim type object.

Note: Specified attributes are not validated, so attempting to set attributes that do not exist or cannot be set will raise an error.

```yaml
Type: ADClaimType
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
Specifies whether to prevent the object from being deleted.
When this property is set to true, you cannot delete the corresponding object without changing the value of the property.
The acceptable values for this parameter are:

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: Identity, SourceTransformPolicy, SourceAttribute, SourceOID
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
Parameter Sets: Identity, SourceTransformPolicy, SourceAttribute, SourceOID
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
You can modify more than one property by specifying a comma-separated list.
The format for this parameter is:

`-Replace @{Attribute1LDAPDisplayName=value[],   Attribute2LDAPDisplayName=value[]}`

当你同时使用“添加”（Add）、“替换”（Replace）、“清除”（Clear）和“删除”（Remove）这些参数时，操作会按照以下顺序进行：

- **Remove**
- **Add**
- **Replace**
- **Clear**

```yaml
Type: Hashtable
Parameter Sets: Identity, SourceTransformPolicy, SourceAttribute, SourceOID
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RestrictValues
This parameter is used to specify whether the claim type may have values outside of the *SuggestedValues* parameter.
If this is set to $True, then the claim should only have values specified in the *SuggestedValues* parameter.
Note that Active Directory does not enforce this restriction.
It is up to the applications that use these claims to enforce the restriction.

```yaml
Type: Boolean
Parameter Sets: Identity, SourceTransformPolicy, SourceAttribute, SourceOID
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务实例，为此需要提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下是指定 Active Directory 域服务实例的几种方法：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的列出顺序：

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
指定一个 Active Directory 属性，该属性类型基于此属性，并从中获取声明值。输入必须是该属性在模式中的唯一名称（Distinguished Name）、名称（Name）或 GUID。

可接受的值包括以下模式类对象的属性：**User**、**InetOrgPerson**、**Computer**、**ManagedServiceAccount**、**GroupManagedServiceAccount** 和 **Auxiliary**，但不包括以下属性：

在模式中被标记为“已废弃”的属性：  
- 被阻止使用的属性，例如 **dBCSPwd**、**lmPwdHistory** 和 **unicodePwd**；  
- 不被复制的属性；  
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
Accept pipeline input: False
Accept wildcard characters: False
```

### -SourceOID
用于指定一个字符串，以便配置基于证书的声明类型源。例如，在您希望使用智能卡登录声明来进行授权决策时，可以使用此参数来创建基于证书的声明类型。该参数使用了来自证书中的发行策略以及在使用 Active Directory Certificate Services 时的证书模板中的对象标识符（OID）的字符串表示形式。一个 OID 的示例是 1.3.6.1.4.1.311.47.2.5。

```yaml
Type: String
Parameter Sets: SourceOID
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SourceTransformPolicy
表示该索赔类型的来源是索赔转换策略引擎（claims transformation policy engine）。

```yaml
Type: SwitchParameter
Parameter Sets: SourceTransformPolicy
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SuggestedValues
为声明类型指定一个或多个建议的值。应用程序可以选择向用户展示这个建议值列表，供用户从中进行选择。当 *RestrictValues* 被设置为 $True 时，应用程序应仅允许用户从这个列表中选取值。

```yaml
Type: ADSuggestedValueEntry[]
Parameter Sets: Identity, SourceTransformPolicy, SourceAttribute
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft ActiveDirectory.Management.ADClaimType

## 输出

### 无或 Microsoft ActiveDirectory.Management.ADClaimType

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADClaimType](./Get-ADClaimType.md)

[New-ADClaimType](./New-ADClaimType.md)

