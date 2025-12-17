---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adclaimtransformpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADClaimTransformPolicy
---

# Set-ADClaimTransformPolicy

## 摘要
用于设置 Active Directory 中索赔转换策略的属性。

## 语法

### DenyAllExcept
```
Set-ADClaimTransformPolicy [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AuthType <ADAuthType>] [-Clear <String[]>]
 [-Credential <PSCredential>] -DenyAllExcept <ADClaimType[]> [-Description <String>]
 [-Identity] <ADClaimTransformPolicy> [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>]
 [-Remove <Hashtable>] [-Replace <Hashtable>] [-Server <String>] [<CommonParameters>]
```

### DenyAll
```
Set-ADClaimTransformPolicy [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AuthType <ADAuthType>] [-Clear <String[]>]
 [-Credential <PSCredential>] [-DenyAll] [-Description <String>] [-Identity] <ADClaimTransformPolicy>
 [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>] [-Remove <Hashtable>] [-Replace <Hashtable>]
 [-Server <String>] [<CommonParameters>]
```

### 身份
```
Set-ADClaimTransformPolicy [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AuthType <ADAuthType>] [-Clear <String[]>]
 [-Credential <PSCredential>] [-Description <String>] [-Identity] <ADClaimTransformPolicy> [-PassThru]
 [-ProtectedFromAccidentalDeletion <Boolean>] [-Remove <Hashtable>] [-Replace <Hashtable>] [-Rule <String>]
 [-Server <String>] [<CommonParameters>]
```

### AllowAll
```
Set-ADClaimTransformPolicy [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AllowAll] [-AuthType <ADAuthType>]
 [-Clear <String[]>] [-Credential <PSCredential>] [-Description <String>] [-Identity] <ADClaimTransformPolicy>
 [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>] [-Remove <Hashtable>] [-Replace <Hashtable>]
 [-Server <String>] [<CommonParameters>]
```

### AllowAllExcept
```
Set-ADClaimTransformPolicy [-WhatIf] [-Confirm] [-Add <Hashtable>] -AllowAllExcept <ADClaimType[]>
 [-AuthType <ADAuthType>] [-Clear <String[]>] [-Credential <PSCredential>] [-Description <String>]
 [-Identity] <ADClaimTransformPolicy> [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>]
 [-Remove <Hashtable>] [-Replace <Hashtable>] [-Server <String>] [<CommonParameters>]
```

### 实例
```
Set-ADClaimTransformPolicy [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -Instance <ADClaimTransformPolicy> [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-ADClaimTransformPolicy` cmdlet 可用于设置 Active Directory 中的声明转换策略的属性。声明转换策略对象包含一组用转换规则语言编写的规则。

## 示例

#### 示例 1：在指定的索赔处理政策上设置转换规则
```
PS C:\> Set-ADClaimTransformPolicy -Identity DenyAllPolicy -DenyAll
```

此命令为名为“DenyAllPolicy”的声明转换策略设置了转换规则，该规则用于拒绝所有声明，无论是发送的还是接收的声明。

#### 示例 2：在特定的索赔处理策略上设置转换规则，并允许某些例外情况
```
PS C:\> Set-ADClaimTransformPolicy -Identity AllowAllExceptCompanyAndDepartmentPolicy -AllowAllExcept Company,Department
```

此命令为名为“AllowAllExceptCompanyAndDepartmentPolicy”的声明转换策略设置了转换规则，允许发送或接收所有声明，除了“Company”和“Department”这两个声明之外。

### 示例 3：在现有的索赔处理政策上设置转换规则
```
PS C:\> Set-ADClaimTransformPolicy -Identity HumanResourcesToHrPolicy -Rule 'C1:[Type=="ad://ext/Department:88ce6e1cc00e9524", Value=="Human Resources", ValueType=="string"] => issue(Type=C1.Type, Value="HR", ValueType=C1.ValueType);'
```

此命令将转换规则应用于名为“HumanResourcesToHrPolicy”的声明转换策略中，以便将声明 ad://ext/Department:88ce6e1cc00e9524 中的 “Human Resources” 字段值转换为 “HR”。

### 示例 4：在文件中指定的索赔处理策略上设置转换规则
```
PS C:\> $Rule = Get-Content -Path C:\rule.txt
PS C:\> Set-ADClaimTransformPolicy MyRule -Rule $Rule
```

该命令将转换规则设置到名为“MyRule”的声明转换策略中，所使用的规则内容位于文件C:\rule.txt中。

## 参数

### -Add
用于指定要添加到对象属性中的值。使用此参数，可以为无法通过 cmdlet 参数修改的属性添加一个或多个值。若要修改对象属性，必须使用轻量级目录访问协议（LDAP）显示名称。可以通过提供用逗号分隔的值列表来为某个属性指定多个值；如果需要为多个属性指定值，则可以使用分号将它们分开。该参数的格式如下：

`-添加 @{Attribute1LDAPDisplayName=value1, value2, ...; Attribute2LDAPDisplayName=value1, value2, ...; AttributeNLDAPDisplayName=value1, value2, ...}`

当你同时使用“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）这些参数时，操作将按照以下顺序进行：

- **Remove**
- **Add**
- **Replace**
- **Clear**

```yaml
Type: Hashtable
Parameter Sets: DenyAllExcept, DenyAll, Identity, AllowAll, AllowAllExcept
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowAll
Indicates whether the policy sets a claims transformation rule that allows all claims to be sent or received.

```yaml
Type: SwitchParameter
Parameter Sets: AllowAll
Aliases:
Accepted values: true

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowAllExcept
Specifies an array of claim types.
When this parameter is specified, the policy sets a claims transformation rule that allows all claims to be sent or received except for the specified claim types.

```yaml
Type: ADClaimType[]
Parameter Sets: AllowAllExcept
Aliases:

Required: True
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

当你同时使用“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）这些参数时，操作将按照以下顺序进行：

- **Remove**
- **Add**
- **Replace**
- **Clear**

```yaml
Type: String[]
Parameter Sets: DenyAllExcept, DenyAll, Identity, AllowAll, AllowAllExcept
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
Specifies a user account that has permission to perform this action.
The default is the current user.

Type a user name, such as User01" or Domain01\User01, or enter a **PSCredential** object, such as one generated by the **Get-Credential** cmdlet.
If you type a user name, you are prompted for a password.

This parameter is not supported by any providers installed with Windows PowerShell.

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

### -DenyAll
Indicates that the policy sets a claims transformation rule that denies all claims to be sent or received.

```yaml
Type: SwitchParameter
Parameter Sets: DenyAll
Aliases:
Accepted values: true

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DenyAllExcept
Specifies an array of claim types.
When this parameter is specified, the claims transformation policy sets a claims transformation rule that denies all claims to be sent or received except for the specified claim types.

```yaml
Type: ADClaimType[]
Parameter Sets: DenyAllExcept
Aliases:

Required: True
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
Parameter Sets: DenyAllExcept, DenyAll, Identity, AllowAll, AllowAllExcept
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity
Specifies one of the following as valid identities for the ADClaimTransformPolicy object:

- A distinguished name
- A GUID (objectGUID)

The cmdlet searches the default naming context or partition to find the object.
If two or more objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

```yaml
Type: ADClaimTransformPolicy
Parameter Sets: DenyAllExcept, DenyAll, Identity, AllowAll, AllowAllExcept
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Instance
Specifies an instance of an Active Directory object to use as a template for a new claims transformation policy object.

You can use an instance of an existing claims transformation policy object as a template or you can construct a new claims transformation policy object by using the Windows PowerShell command line or by using a script.

Method 1: Use an existing claims transformation policy object as a template for a new object.
To retrieve an instance of an existing claims transformation policy object, use a cmdlet such as **Get-ADClaimTransformPolicy**.
Then provide this object to the Instance parameter of the New-ADClaimTransformPolicy cmdlet to create a new claims transformation policy object.
You can override property values of the new object by setting the appropriate parameters.

Method 2: Create a new **ADClaimTransformPolicy** and set the property values by using the Windows PowerShell command line interface.
Then pass this object to the *Instance* parameter of the **New-ADClaimTransformPolicy** cmdlet to create the new Active Directory object.

Note: Specified attributes are not validated, so attempting to set attributes that do not exist or cannot be set will raise an error.

```yaml
Type: ADClaimTransformPolicy
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
Parameter Sets: DenyAllExcept, DenyAll, Identity, AllowAll, AllowAllExcept
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

When you use the *Add*, *Remove*, *Replace*, and *Clear* parameters together, the parameters are applied in the following sequence:

- **Remove**
- **Add**
- **Replace**
- **Clear**

```yaml
Type: Hashtable
Parameter Sets: DenyAllExcept, DenyAll, Identity, AllowAll, AllowAllExcept
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
The format for this parameter is

`-Replace @{Attribute1LDAPDisplayName=value[],   Attribute2LDAPDisplayName=value[]}`

当你同时使用“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）这些参数时，操作将按照以下顺序进行：

- **Remove**
- **Add**
- **Replace**
- **Clear**

```yaml
Type: Hashtable
Parameter Sets: DenyAllExcept, DenyAll, Identity, AllowAll, AllowAllExcept
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Rule
Specifies the claims transformation rule.
To specify the rule, you can either type the rule in a text file, and then pass the file to the cmdlet (recommended), or type the rule inline.

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

### None or Microsoft.ActiveDirectory.Management.ADClaimTransformPolicy
A claim transform policy object is received by the *Identity* parameter.

A claim transform policy object that was retrieved by using the Get-ADClaimTransformPolicy cmdlet and then modified is received by the *Instance* parameter.

## 输出

### None or Microsoft.ActiveDirectory.Management.ADClaimTransformPolicy
Returns the modified claim transform policy object when the *PassThru* parameter is specified.
By default, this cmdlet does not generate any output.

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADClaimTransformPolicy](./Get-ADClaimTransformPolicy.md)

[New-ADClaimTransformPolicy](./New-ADClaimTransformPolicy.md)

[Remove-ADClaimTransformPolicy](./Remove-ADClaimTransformPolicy.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

