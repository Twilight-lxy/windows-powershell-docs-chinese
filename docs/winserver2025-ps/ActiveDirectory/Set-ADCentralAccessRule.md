---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adcentralaccessrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADCentralAccessRule
---

# 设置 ADCentralAccessRule 规则

## 摘要
修改 Active Directory 中的一个核心访问规则。

## 语法

### 身份
```
Set-ADCentralAccessRule [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AuthType <ADAuthType>] [-Clear <String[]>]
 [-Credential <PSCredential>] [-CurrentAcl <String>] [-Description <String>] [-Identity] <ADCentralAccessRule>
 [-PassThru] [-ProposedAcl <String>] [-ProtectedFromAccidentalDeletion <Boolean>] [-Remove <Hashtable>]
 [-Replace <Hashtable>] [-ResourceCondition <String>] [-Server <String>] [<CommonParameters>]
```

### 实例
```
Set-ADCentralAccessRule [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -Instance <ADCentralAccessRule> [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-ADCentralAccessRule` cmdlet 可用于修改存储在 Active Directory 中的中央访问策略中的中央访问规则。

## 示例

### 示例 1：在中央访问规则上设置条件
```
PS C:\> $departmentResourceProperty = Get-ADResourceProperty -Identity Department
PS C:\> $resourceCondition = "(@RESOURCE." + $departmentResourceProperty.Name + " Contains {`"Finance`"})"
PS C:\> Set-ADCentralAccessRule -Identity "Finance Documents Rule" -ResourceCondition $resourceCondition
```

该命令使用一个新的资源条件来设置名为“Finance Documents Rule”的中央访问规则。这个资源条件的适用范围是那些在其“Department”资源属性中包含“Finance”值的资源。

### 示例 2：为中央访问规则设置资源条件和新权限
```
PS C:\> $CountryClaimType = Get-ADClaimType -Identity Country
PS C:\> $DepartmentClaimType = Get-ADClaimType -Identity Department
PS C:\> $CountryResourceProperty = Get-ADResourceProperty -Identity Country
PS C:\> $DepartmentResourceProperty = Get-ADResourceProperty -Identity Department
PS C:\> $FinanceException = Get-ADGroup -Identity FinanceException
PS C:\> $FinanceAdmin = Get-ADGroup -Identity FinanceAdmin
PS C:\> $ResourceCondition = "(@RESOURCE." + $departmentResourceProperty.Name + " Contains {`"Finance`"})"
PS C:\> $CurrentAcl = "O:SYG:SYD:AR(A;;FA;;;OW)(A;;FA;;;BA)(A;;0x1200a9;;;" + $financeException.SID.Value + ")(A;;0x1301bf;;;" + $FinanceAdmin.SID.Value + ")(A;;FA;;;SY)(XA;;0x1200a9;;;AU;((@USER." + $CountryClaimType.Name + " Any_of @RESOURCE." + $CountryResourceProperty.Name + ") && (@USER." + $DepartmentClaimType.Name + " Any_of @RESOURCE." + $DepartmentResourceProperty.Name + ")))"
PS C:\> Set-ADCentralAccessRule -Identity "Finance Documents Rule" -ResourceCondition $ResourceCondition -CurrentAcl $currentAcl
```

这个示例设置了一个名为“Finance Documents Rule”的中心访问规则，为其配置了新的资源条件和新的权限。

新规则规定，文件仅应由财务部门的成员阅读。财务部门的成员只能访问他们自己所在国家/地区的文件。只有财务管理员才具有写入文件的权限。不过，对于属于“FinanceException”组的成员，该规则允许例外情况——这些成员将拥有读取文件的权限。

目标定位：

- Resource.Department Contains Finance
- Allow Full control User.MemberOf(FinanceAdmin)

Access rules:

- Allow Read User.Country=Resource.Country AND User.department = Resource.Department
- Allow Full control User.MemberOf(FinanceAdmin)
- Allow Read User.Country=Resource.Country AND User.department = Resource.Department
- Allow Read User.MemberOf(FinanceException)

### 示例 3：为中央访问规则设置描述
```
PS C:\> Get-ADCentralAccessRule -Identity "Finance Documents Rule" | Set-ADCentralAccessRule -Description "For finance documents."
```

这条命令用于获取名为“Finance Documents Rule”的中央访问规则，并将其描述设置为“For finance documents”（用于财务文件）。

## 参数

### -Add
用于指定要添加到对象属性中的值。您可以使用此参数向无法通过 cmdlet 参数修改的属性中添加一个或多个值。要修改对象属性，必须使用轻量级目录访问协议（LDAP）显示名称。您可以通过指定用逗号分隔的值列表来为一个属性指定多个值；如果要为多个属性指定值，则需要使用分号将它们分开。此参数的格式如下：

请帮我将以下Markdown格式的内容转换为中文：  

```  
-Add @{Attribute1LDAPDisplayName=value1, value2, ...; Attribute2LDAPDisplayName=value1, value2, ...; AttributeNLDAPDisplayName=value1, value2, ...}  
```

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

当你同时使用“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）这些参数时，操作将按照以下顺序执行：

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

### -CurrentAcl
Specifies the currently effective access control list (ACL) of the rule.
The current ACL grants access to target resources once the central access policy containing this rule is published.

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
Type: ADCentralAccessRule
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Instance
Specifies a modified copy of an central access rule object to use to update the actual central access rule object.
When this parameter is used, any modifications made to the modified copy of the object are also made to the corresponding central access rule object.
The cmdlet only updates the object properties that have changed.

The *Instance* parameter can only update central access rule objects that have been retrieved by using the **Get-ADCentralAccessRule** cmdlet.
When you specify the *Instance* parameter, you cannot specify other parameters that set properties on the object.

```yaml
Type: ADCentralAccessRule
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

### -ProposedAcl
Specifies the proposed ACL of the central access rule.
The proposed ACL allows an administrator to audit the results of access requests to target resources specified in the resource condition without affecting the current system.
To view the logs, go to Event Viewer or other audit tools to view the logs.

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

When you use the *Add*, *Remove*, *Replace*, and *Clear* parameters together, the parameters are applied in the following sequence:

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

### -ResourceCondition
Specifies the resource condition of the central access rule.
The resource condition specifies a list of criteria to scope the resources.

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

### None or Microsoft.ActiveDirectory.Management.ADCentralAccessPolicyEntry
An **ADCentralAccessPolicyEntry** object is received by the *Identity* parameter.

An **ADCentralAccessPolicyEntry** object that was retrieved by using the **Get-ADCentralAccessPolicyEntry** cmdlet and then modified is received by the *Instance* parameter.

## 输出

### None or Microsoft.ActiveDirectory.Management.ADCentralAccessPolicyEntry
Returns the modified **ADCentralAccessPolicyEntry** object when the *PassThru* parameter is specified.
By default, this cmdlet does not generate any output.

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADCentralAccessRule](./Get-ADCentralAccessRule.md)

[New-ADCentralAccessRule](./New-ADCentralAccessRule.md)

[Remove-ADCentralAccessRule](./Remove-ADCentralAccessRule.md)

[Windows PowerShell中的AD DS管理Cmdlet](./activedirectory.md)

