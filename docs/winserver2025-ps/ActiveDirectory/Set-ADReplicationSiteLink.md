---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adreplicationsitelink?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADReplicationSiteLink
---

# 设置 ADReplicationSiteLink

## 摘要
用于设置 Active Directory 站点链接的属性。

## 语法

### 身份
```
Set-ADReplicationSiteLink [-WhatIf] [-Confirm] [-Add <Hashtable>] [-AuthType <ADAuthType>] [-Clear <String[]>]
 [-Cost <Int32>] [-Credential <PSCredential>] [-Description <String>] [-Identity] <ADReplicationSiteLink>
 [-PassThru] [-Remove <Hashtable>] [-Replace <Hashtable>] [-ReplicationFrequencyInMinutes <Int32>]
 [-ReplicationSchedule <ActiveDirectorySchedule>] [-Server <String>] [-SitesIncluded <Hashtable>]
 [<CommonParameters>]
```

### 实例
```
Set-ADReplicationSiteLink [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Instance <ADReplicationSiteLink>] [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-ADReplicationSiteLink` cmdlet 用于设置 Active Directory 站点链接的属性。站点链接用于连接两个或多个站点。复制站点链接决定了站点之间的交互方式以及用于传输复制数据流量的方法。必须使用站点链接来连接各个站点，以便每个站点的域控制器能够相互复制 Active Directory 的更改信息。

## 示例

### 示例 1：向复制站点链接中添加和删除站点
```
PS C:\> Set-ADReplicationSiteLink -Identity "Europe-Asia" -SitesIncluded @{Add="Asia2";Remove="Asia"}
```

此命令将 Asia2 站点添加到复制站点链接 Europe-Asia 中，并移除 Asia 站点。

### 示例 2：为经过过滤的网站设置某个属性
```
PS C:\> Get-ADReplicationSiteLink -Filter "ReplicationFrequencyInMinutes -ge 60" -Properties Cost | % {Set-ADReplicationSiteLink $_ -Cost 200}
```

这个命令会获取目录中所有复制频率大于或等于60分钟的站点链接，然后将这些站点链接对象的**Cost**属性设置为200。

### 示例 3：为复制站点链接设置每日复制计划
```
PS C:\> $Schedule = New-Object -TypeName System.DirectoryServices.ActiveDirectory.ActiveDirectorySchedule
PS C:\> $Schedule.ResetSchedule()
PS C:\> $Schedule.SetDailySchedule("Twenty","Zero","TwentyTwo","Thirty")
PS C:\> Set-ADReplicationSiteLink -Identity "NorthAmerica-SouthAmerica" -ReplicationSchedule $Schedule
```

此命令用于设置名为“NorthAmerica-SouthAmerica”的站点链接的每日复制计划。

### 示例 4：为复制站点链接启用变更通知功能
```
PS C:\> Set-ADReplicationSiteLink -Identity "Europe-Asia" -Replace @{'options'=1}
```

此命令会为名为“Europe-Asia”的站点链接启用变更通知功能。

## 参数

### -Add
用于指定要添加到对象属性中的值。此参数可用于向无法通过 cmdlet 参数修改的属性中添加一个或多个值。若要修改对象属性，必须使用轻型目录访问协议（LDAP）显示名称。可以通过提供一个用逗号分隔的值列表来为某个属性指定多个值；如果需要为多个属性分别设置值，则可以使用分号进行分隔。该参数的格式如下：

`- 添加 @{Attribute1LDAPDisplayName=value1, value2, ...; Attribute2LDAPDisplayName=value1, value2, ...; AttributeNLDAPDisplayName=value1, value2, ...}`

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

### -Clear
Specifies an array of object properties that will be cleared in the directory.
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

### -Cost
Specifies the cost to be placed on the site link.
For more information on determining the cost, see [Determining the Cost](https://go.microsoft.com/fwlink/?LinkId=221871) in the TechNet Library: http://go.microsoft.com/fwlink/?LinkId=221871.

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
Type: ADReplicationSiteLink
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Instance
Specifies an instance of a site link object to use as a template for a new site link object.

You can use an instance of an existing site link object as a template or you can construct a new site link object by using the Windows PowerShell command line or by using a script.

Method 1: Use an existing site link object as a template for a new object.
To retrieve an instance of an existing site link object, use a cmdlet such as **Get-ADReplicationSiteLink**.
Then provide this object to the *Instance* parameter of the **New-ADReplicationSiteLink** cmdlet to create a new site link object.
You can override property values of the new object by setting the appropriate parameters.

Method 2: Create a new **ADReplicationSiteLink** and set the property values by using the Windows PowerShell command line interface.
Then pass this object to the *Instance* parameter of the **New-ADReplicationSiteLink** cmdlet to create the new Active Directory object.

Note: Specified attributes are not validated, so attempting to set attributes that do not exist or cannot be set will raise an error.

```yaml
Type: ADReplicationSiteLink
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

### -ReplicationFrequencyInMinutes
Species the frequency, in minutes, for which replication will occur where this site link is in use between sites.
Active Directory preserves bandwidth between sites by minimizing the frequency of replication and by allowing you to schedule the availability of site links for replication.
By default, intersite replication across each site link occurs every 180 minutes (3 hours).
You can adjust this frequency to match your specific needs.
Be aware that increasing this frequency increases the amount of bandwidth used by replication.

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

### -ReplicationSchedule
Specifies the default replication schedule for any connections within this site link (intra-site replication).
This allows you to schedule the availability of site links for use by replication.
By default, a site link is available to carry replication traffic 24 hours a day, 7 days a week.
You can limit this schedule to specific days of the week and times of day.
You can, for example, schedule intersite replication so that it only occurs after normal business hours.

```yaml
Type: ActiveDirectorySchedule
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
The service may be any of the following: Active Directory Lightweight Domain Services, Active Directory Domain Services or Active Directory Snapshot instance.

Domain name values:

- Fully qualified domain name (FQDN)
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

The default value for the *Server* parameter is determined by one of the following methods in the order that they are listed:

- By using *Server* value from objects passed through the pipeline.
- By using the server information associated with the Active Directory PowerShell provider drive, when running under that drive.
- By using the domain of the computer running PowerShell.

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

### -SitesIncluded
Specifies the list of sites included in the site link.
For **Set-ADReplicationSiteLink** operations, you can add or include new sites within an existing site link by specifying them using this parameter.
You do not have to specify all previously listed sites already within this link.

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

### None or Microsoft.ActiveDirectory.Management.ADReplicationSiteLink
A site link object is received by the *Identity* parameter.

A site link object that was retrieved by using the **Get-ADReplicationSiteLink** cmdlet and then modified is received by the *Instance* parameter.

## 输出

### None or Microsoft.ActiveDirectory.Management.ADReplicationSiteLink

## 备注

## 相关链接

[Get-ADReplicationSiteLink](./Get-ADReplicationSiteLink.md)

[New-ADReplicationSiteLink](./New-ADReplicationSiteLink.md)

[Remove-ADReplicationSiteLink](./Remove-ADReplicationSiteLink.md)

