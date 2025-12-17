---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adreplicationsitelinkbridge?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADReplicationSiteLinkBridge
---

# 设置 ADReplicationSiteLinkBridge

## 摘要
用于设置 Active Directory 中复制站点链接桥的属性。

## 语法

### 身份
```
Set-ADReplicationSiteLinkBridge [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AuthType <ADAuthType>]
 [-Clear <String[]>] [-Credential <PSCredential>] [-Description <String>]
 [-Identity] <ADReplicationSiteLinkBridge> [-PassThru] [-Remove <Hashtable>] [-Replace <Hashtable>]
 [-Server <String>] [-SiteLinksIncluded <Hashtable>] [<CommonParameters>]
```

### 实例
```
Set-ADReplicationSiteLinkBridge [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Instance <ADReplicationSiteLinkBridge>] [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-ADReplicationSiteLinkBridge` cmdlet 用于设置 Active Directory 中复制站点链接桥的属性。站点链接桥用于连接两个或多个站点链接，并实现这些站点链接之间的传输性（即数据可以在它们之间自由流动）。桥中的每个站点链接都必须与桥中的另一个站点链接有共同的站点作为关联目标。

## 示例

### 示例 1：在站点链接桥中配置一个站点链接
```
PS C:\> Set-ADReplicationSiteLinkBridge -Identity "NorthAmerica-Asia" -SiteLinksIncluded @{Add='NorthAmerica-Europe2','Europe2-Asia';Remove='NorthAmerica-Europe','Europe-Asia'}
```

此命令将站点链接桥接“NorthAmerica-Asia”更新为使用“Europe2”代替“Europe”。

### 示例 2：配置一个过滤后的站点链接桥接列表
```
PS C:\> Get-ADReplicationSiteLinkBridge -Filter "SiteLinksIncluded -eq 'NorthAmerica-Europe' -and SiteLinksIncluded -eq 'Europe-Asia'" -Properties SiteLinksIncluded | % {Set-ADReplicationSiteLinkBridge $_ -SiteLinksIncluded @{Add='NorthAmerica-Europe2','Europe2-Asia';Remove='NorthAmerica-Europe','Europe-Asia'}}
```

这个命令会获取目录中所有包含“NorthAmerica-Europe”和“Europe-Asia”站点链接的站点链接桥接对象，然后更新这些站点链接桥接对象的配置，使其使用“Europe2”代替“Europe”作为目标区域。

## 参数

### -Add
用于指定要添加到对象属性中的值。使用此参数，可以为无法通过 cmdlet 参数修改的属性添加一个或多个值。若要修改对象属性，则必须使用轻量级目录访问协议（LDAP）显示名称。您可以通过指定用逗号分隔的值列表来为一个属性设置多个值；如果需要为多个属性设置值，则可以使用分号将它们分开。该参数的格式如下：

请帮我将以下Markdown内容转换为中文：  

```
-Add @{Attribute1LDAPDisplayName=value1, value2, ...; Attribute2LDAPDisplayName=value1, value2, ...; AttributeNLDAPDisplayName=value1, value2, ...}
```

当你同时使用“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）这些参数时，操作将按照以下顺序进行：

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

当你同时使用“添加”（Add）、“删除”（Remove）、“替换”（Replace）和“清除”（Clear）这些参数时，操作将按照以下顺序进行：

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
The default credentials are the credentials of the currently logged on user unless the cmdlet is run from an Active Directory PowerShell provider drive.
If the cmdlet is run from such a provider drive, the account associated with the drive is the default.

To specify this parameter, you can type a user name, such as User1 or Domain01\User01 or you can specify a **PSCredential** object.
If you specify a user name for this parameter, the cmdlet prompts for a password.

You can also create a **PSCredential** object by using a script or by using the **Get-Credential** cmdlet.
You can then set the *Credential* parameter to the **PSCredential** object.

If the acting credentials do not have directory-level permission to perform the task, Active Directory PowerShell returns a terminating error.

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

The cmdlet searches the default naming context or partition to find the object.
If two or more objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

```yaml
Type: ADReplicationSiteLinkBridge
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Instance
Specifies an instance of a site link bridge object to use as a template for a new site link bridge object.

You can use an instance of an existing site link bridge object as a template or you can construct a new site link bridge object by using the Windows PowerShell command line or by using a script.

Method 1: Use an existing site link bridge object as a template for a new object.
To retrieve an instance of an existing site link bridge object, use a cmdlet such as **Get-ADReplicationSiteLinkBridge**.
Then provide this object to the *Instance* parameter of the New-ADReplicationSiteLinkBridge cmdlet to create a new site link bridge object.
You can override property values of the new object by setting the appropriate parameters.

Method 2: Create a new **ADReplicationSiteLinkBridge** and set the property values by using the Windows PowerShell command line interface.
Then pass this object to the *Instance* parameter of the **New-ADReplicationSiteLinkBridge** cmdlet to create the new Active Directory object.

Note: Specified attributes are not validated, so attempting to set attributes that do not exist or cannot be set will raise an error.

```yaml
Type: ADReplicationSiteLinkBridge
Parameter Sets: Instance
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

### -SiteLinksIncluded
Specifies the list of site links that are included in this site link bridge.
Accepted values for this parameter are the distinguished name (DN), a GUID, or the name of a site link.

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

### None or Microsoft.ActiveDirectory.Management.ADReplicationSiteLinkBridge
A site link bridge object is received by the *Identity* parameter.

A site link bridge object that was retrieved by using the **Get-ADReplicationSiteLinkBridge** cmdlet and then modified is received by the **Instance** parameter.

## 输出

### None or Microsoft.ActiveDirectory.Management.ADReplicationSiteLinkBridge

## 备注

## 相关链接

[Get-ADReplicationSiteLinkBridge](./Get-ADReplicationSiteLinkBridge.md)

[New-ADReplicationSiteLinkBridge](./New-ADReplicationSiteLinkBridge.md)

[Remove-ADReplicationSiteLinkBridge](./Remove-ADReplicationSiteLinkBridge.md)

