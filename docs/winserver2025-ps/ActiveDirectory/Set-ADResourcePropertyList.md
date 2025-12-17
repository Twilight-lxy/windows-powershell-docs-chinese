---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adresourcepropertylist?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADResourcePropertyList
---

# Set-ADResourcePropertyList

## 摘要
修改 Active Directory 中的资源属性列表。

## 语法

### 身份
```
Set-ADResourcePropertyList [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AuthType <ADAuthType>] [-Clear <String[]>]
 [-Credential <PSCredential>] [-Description <String>] [-Identity] <ADResourcePropertyList> [-PassThru]
 [-ProtectedFromAccidentalDeletion <Boolean>] [-Remove <Hashtable>] [-Replace <Hashtable>] [-Server <String>]
 [<CommonParameters>]
```

### 实例
```
Set-ADResourcePropertyList [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -Instance <ADResourcePropertyList> [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-ADResourcePropertyList` cmdlet 可用于修改 Active Directory 中的资源属性列表。

## 示例

### 示例 1：修改资源属性列表
```
PS C:\> Set-ADResourcePropertyList -Identity "Corporate Resource Property List" -Description "For corporate documents."
```

此命令设置了一个名为“Corporate Resource Property List”的资源属性列表，其描述为：“用于企业文档。”

### 示例 2：获取资源属性列表并对其进行修改
```
PS C:\> Get-ADResourcePropertyList -Name "Corporate Resource Property List" | Set-ADResourcePropertyList -Description "For corporate documents."
```

这个命令会获取名为“Corporate Resource Property List”的资源属性列表，然后设置其描述信息。

## 参数

### -Add
用于指定要添加到对象属性中的值。使用此参数，可以为无法通过 cmdlet 参数修改的属性添加一个或多个值。若要修改对象属性，必须使用轻量级目录访问协议（LDAP）显示名称。可以通过提供用逗号分隔的值列表来为单个属性指定多个值；如果需要为多个属性分别指定值，则可以使用分号进行分隔。该参数的格式如下：

`-添加 @{Attribute1LDAPDisplayName=value1, value2, ...; Attribute2LDAPDisplayName=value1, value2, ...; AttributeNLDAPDisplayName=value1, value2, ...}`

当你同时使用“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）这四个参数时，这些操作将按照以下顺序执行：

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
Specifies an array of object properties that will be cleared in the directory.
Use this parameter to clear one or more values of a property that cannot be modified using a cmdlet parameter.
To modify an object property, you must use the LDAP display name.
You can modify more than one property by specifying a comma-separated list.
The format for this parameter is:

`-Clear Attribute1LDAPDisplayName, Attribute2LDAPDisplayName`

当你同时使用“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）这四个参数时，这些操作将按照以下顺序执行：

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
The LDAP Display Name (**ldapDisplayName**) for this property is description.

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

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

```yaml
Type: ADResourcePropertyList
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Instance
Specifies an instance of a resource property list object to use as a template for a new resource property list object.

You can use an instance of an existing resource property list object as a template or you can construct a resource property list object by using the Windows PowerShell command line or by using a script.

Method 1: Use an existing resource property list object as a template for a new object.
To retrieve an instance of an existing resource property list object, use a cmdlet such as **Get-ADResourcePropertyList**.
Then provide this object to the Instance parameter of the **New-ADResourcePropertyList** cmdlet to create a new resource property list object.
You can override property values of the new object by setting the appropriate parameters.

Method 2: Create a new **ADResourcePropertyList** and set the property values by using the Windows PowerShell command line interface.
Then pass this object to the Instance parameter of the **New-ADResourcePropertyList** cmdlet to create the new resource property list object.

Note: Specified attributes are not validated, so attempting to set attributes that do not exist or cannot be set will raise an error.

```yaml
Type: ADResourcePropertyList
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
You can modify more than one property by specifying a comma-separated list.
The format for this parameter is:

`-Replace @{Attribute1LDAPDisplayName=value[],   Attribute2LDAPDisplayName=value[]}`

当你同时使用“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）这四个参数时，这些操作将按照以下顺序执行：

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
`-添加 @{Attribute1LDAPDisplayName=value1, value2, ...; Attribute2LDAPDisplayName=value1, value2, ...; AttributeNLDAPDisplayName=value1, value2, ...}`

当你同时使用“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）这四个参数时，这些操作将按照以下顺序执行：

- **Remove**
- **Add**
- **Replace**
- **Clear**

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

### None or Microsoft.ActiveDirectory.Management.ADClaimTypeList

## 输出

### None or Microsoft.ActiveDirectory.Management.ADClaimTypeList

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADResourcePropertyList](./Get-ADResourcePropertyList.md)

[New-ADResourcePropertyList](./New-ADResourcePropertyList.md)

[Remove-ADResourcePropertyList](./Remove-ADResourcePropertyList.md)

