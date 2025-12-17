---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adobject?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADObject
---

# Get-ADObject

## 摘要
获取一个或多个Active Directory对象。

## 语法

### 过滤器（默认设置）
```
Get-ADObject [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Filter <String> [-IncludeDeletedObjects]
 [-Properties <String[]>] [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>]
 [-SearchScope <ADSearchScope>] [-Server <String>] [<CommonParameters>]
```

### 身份
```
Get-ADObject [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADObject>
 [-IncludeDeletedObjects] [-Partition <String>] [-Properties <String[]>] [-Server <String>]
 [<CommonParameters>]
```

### LdapFilter
```
Get-ADObject [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-IncludeDeletedObjects]
 -LDAPFilter <String> [-Properties <String[]>] [-ResultPageSize <Int32>] [-ResultSetSize <Int32>]
 [-SearchBase <String>] [-SearchScope <ADSearchScope>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADObject` cmdlet 可以获取一个 Active Directory 对象，或者执行搜索来获取多个对象。

`Identity` 参数用于指定要获取的 Active Directory 对象。您可以通过该对象的唯一名称（Distinguished Name）或全局唯一标识符（GUID）来识别目标对象。此外，您还可以将这个参数设置为一个 Active Directory 对象变量（例如 `$<localADObject>`），或者通过管道将某个对象传递给 `Identity` 参数。

要搜索并获取多个对象，请使用 *Filter* 或 *LDAPFilter* 参数。*Filter* 参数使用 PowerShell 表达式语言来为 Active Directory 编写查询字符串。PowerShell 表达式语言的语法为 *Filter* 参数接收的值类型提供了丰富的类型转换支持。有关 *Filter* 参数语法的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter`。如果您已有现有的轻量级目录访问协议（LDAP）查询字符串，可以使用 *LDAPFilter* 参数。

这个cmdlet可以获取Active Directory对象的一组默认属性。如果要获取更多属性，可以使用*Properties*参数。有关如何确定计算机对象的属性的更多信息，请参阅*Properties*参数的描述。

## 示例

### 示例 1：使用 LDAP 过滤语法获取某个域名的网站列表
```
PS C:\> Get-ADObject -LDAPFilter "(objectClass=site)" -SearchBase 'CN=Configuration,DC=Fabrikam,DC=Com' -Properties CanonicalName | FT Name,CanonicalName -A
Name CanonicalName
---- -------------
HQ   FABRIKAM.COM/Configuration/Sites/HQ
BO1  FABRIKAM.COM/Configuration/Sites/BO1
BO2  FABRIKAM.COM/Configuration/Sites/BO2
BO3  FABRIKAM.COM/Configuration/Sites/BO3
```

该命令使用LDAP过滤语法显示Fabrikam公司的站点列表。

### 示例 2：从配置命名上下文中获取站点信息
```
PS C:\> Get-ADObject -Filter 'ObjectClass -eq "site"' -SearchBase 'CN=Configuration,DC=Fabrikam,DC=Com' -Properties siteObjectBL | foreach {$_.siteObjectBL}
CN=192.167.1.0/26,CN=Subnets,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM
CN=192.166.1.0/26,CN=Subnets,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM
CN=192.168.1.0/26,CN=Subnets,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM
CN=192.165.1.0/26,CN=Subnets,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM
CN=192.164.1.0/26,CN=Subnets,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM
CN=192.163.1.0/26,CN=Subnets,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM
CN=192.162.1.0/26,CN=Subnets,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM
CN=192.161.1.0/26,CN=Subnets,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM
CN=192.160.1.0/26,CN=Subnets,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM
CN=192.159.1.0/26,CN=Subnets,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM
CN=192.158.1.0/26,CN=Subnets,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM
CN=192.157.1.0/26,CN=Subnets,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM
```

这个命令从配置命名上下文中获取**Site**对象，并显示**siteObjectBL**属性的列表。

### 示例 3：获取具有指定属性的所有对象
```
PS C:\> $ChangeDate = New-Object DateTime(2008, 11, 18, 1, 40, 02)
PS C:\> Get-ADObject -Filter 'whenChanged -gt $ChangeDate' -IncludeDeletedObjects
```

这个命令会获取所有对象（包括已被删除的对象），这些对象的 `whenChanged` 属性值大于指定的日期。请注意，符合过滤条件的对象无论是否已被删除或未被回收，都会被返回出来。

#### 示例 4：获取具有指定属性的已删除对象
```
PS C:\> $ChangeDate = New-Object DateTime(2008, 11, 18, 1, 40, 02)
PS C:\> Get-ADObject -Filter 'whenChanged -gt $ChangeDate -and isDeleted -eq $True -and -not (isRecycled -eq $True) -and name -ne "Deleted Objects"' -IncludeDeletedObjects


ObjectGUID        : 98118958-91c7-437d-8ada-ba0b66db823b
Deleted           : True
DistinguishedName : CN=Andrew Ma\0ADEL:98118958-91c7-437d-8ada-ba0b66db823b,CN=Deleted Objects,DC=FABRIKAM,DC=COM
Name              : Andrew Ma
DEL:98118958-91c7-437d-8ada-ba0b66db823b
ObjectClass       : user
```

这个示例会获取所有被删除的对象，这些对象的`whenChanged`属性大于指定的日期。`name -ne "Deleted Objects"`这条子句确保不会返回“已删除对象”容器（即包含被删除对象的集合）。该示例仅返回那些可以被恢复的对象。

### 示例 5：获取在指定日期之后被删除的特定对象
```
PS C:\> $ChangeDate = New-Object DateTime(2008, 11, 18, 1, 40, 02)
PS C:\> Get-ADObject -Filter 'whenChanged -gt $ChangeDate -and isDeleted -eq $True -and -not (isRecycled -eq $True) -and lastKnownParent -eq "OU=Accounting,DC=Fabrikam,DC=com"' -IncludeDeletedObjects


ObjectGUID        : 12d53e7f-aaf7-4790-b41a-da19044504db
Deleted           : True
DistinguishedName : CN=Craig Dewar\0ADEL:12d53e7f-aaf7-4790-b41a-da19044504db,CN=Deleted Objects,DC=Fabrikam,DC=com
Name              : Craig Dewar
DEL:12d53e7f-aaf7-4790-b41a-da19044504db
ObjectClass       : user
```

这个示例会获取所有被删除的对象，这些对象的 `whenChanged` 属性值大于指定的日期，并且在被删除时是指定组织单位的子对象。

#### 示例 6：获取 LDS 实例中指定对象的信息
```
PS C:\> Get-ADObject -Identity "DC=AppNC" -Server "FABRIKAM-SRV1:60000"
ObjectGUID                    DistinguishedName             Name                          ObjectClass
----------                    -----------------             ----                          -----------
62b2e185-9322-4980-9c93-cf... DC=AppNC                      AppNC                         domainDNS
```

这个命令用于获取LDS实例中**domainDNS**对象的相关信息。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的认证方法是“Negotiate”。

基本认证方法需要使用安全套接字层（SSL）连接。

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

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从此类提供程序驱动器中运行的，则使用与该驱动器关联的账户作为默认凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果该执行任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

### -Filter
指定一个用于检索 Active Directory 对象的查询字符串。该字符串使用 PowerShell 表达式语言（PowerShell Expression Language）的语法。PowerShell 表达式语言为 *Filter* 参数接收到的值类型提供了丰富的类型转换支持。其语法采用“按顺序排列”的方式，即运算符位于操作数和值之间。有关 *Filter* 参数的更多信息，请输入 `Get-Help about_ActiveDirectory_filter`。

语法：

以下语法使用了巴克斯-诺尔（Backus-Naur）形式来说明如何使用 PowerShell 表达式语言来处理这个参数。

<filter> ::= "{" <FilterComponentList> "}"

\<FilterComponentList\> ::= \<FilterComponent\> | \<FilterComponent\> \<JoinOperator\> \<FilterComponent\> | \<NotOperator\> \<FilterComponent\>

<FilterComponent> ::= <attr> <FilterOperator> <value> | ("<FilterComponent>)"

\<FilterOperator\> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

<JoinOperator> ::= "-and" | "-or"

\<NotOperator\> ::= "-not"

\<attr\> ::= \<PropertyName\> | \<该属性的 LDAP 显示名称\>

<value>::= <使用指定的<FilterOperator>将此值与<attr>进行比较>

要查看 `<value>` 支持的数据类型列表，请输入 `Get-Help about_ActiveDirectory_ObjectModel`。

注意：PowerShell中的通配符（除了*之外的其他符号，例如?）不支持*Filter*语法。

注意：要使用 LDAP 查询字符串进行查询，请使用 *LDAPFilter* 参数。

```yaml
Type: String
Parameter Sets: Filter
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity
通过提供以下属性值之一来指定一个 Active Directory 对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)

此cmdlet会在默认的命名上下文或分区中搜索该对象。如果找到两个或多个对象，该cmdlet会返回一个非终止性错误（即不会停止执行的错误）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

也接受派生类型，例如以下这些类型：

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy**
- **Microsoft.ActiveDirectory.Management.ADDomain**

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

### -IncludeDeletedObjects
Indicates that this cmdlet retrieves deleted objects and the deactivated forward and backward links.
When this parameter is specified, the cmdlet uses the following LDAP controls:

- Show Deleted Objects (1.2.840.113556.1.4.417)
- Show Deactivated Links (1.2.840.113556.1.4.2065)

Note: If this parameter is not specified, the cmdlet does not return or operate on deleted objects.

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

### -LDAPFilter
Specifies an LDAP query string that is used to filter Active Directory objects.
You can use this parameter to run your existing LDAP queries.
The *Filter* parameter syntax supports the same functionality as the LDAP syntax.
For more information, see the *Filter* parameter description or type `Get-Help about_ActiveDirectory_Filter`.

```yaml
Type: String
Parameter Sets: LdapFilter
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

In many cases, a default value is used for the *Partition* parameter if no value is specified.
The rules for determining the default value are given below.
Note that rules listed first are evaluated first and once a default value can be determined, no further rules are evaluated.

In Active Directory Domain Services (AD DS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Partition* parameter does not take a default value.

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

### -Properties
Specifies the properties of the output object to retrieve from the server.
Use this parameter to retrieve properties that are not included in the default set.

Specify properties for this parameter as a comma-separated list of names.
To display all of the attributes that are set on the object, specify * (asterisk).

To specify an individual extended property, use the name of the property.
For properties that are not default or extended properties, you must specify the LDAP display name of the attribute.

To retrieve properties and display them for an object, you can use the Get-* cmdlet associated with the object and pass the output to the **Get-Member** cmdlet.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: Property

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResultPageSize
Specifies the number of objects to include in one page for an AD DS query.

The default is 256 objects per page.

```yaml
Type: Int32
Parameter Sets: Filter, LdapFilter
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResultSetSize
Specifies the maximum number of objects to return for an AD DS query.
If you want to receive all of the objects, set this parameter to $Null (null value).
You can use Ctrl+C to stop the query and return of objects.

The default is $Null.

```yaml
Type: Int32
Parameter Sets: Filter, LdapFilter
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SearchBase
Specifies an Active Directory path to search.

When you run a cmdlet from an Active Directory provider drive, the default value of this parameter is the current path of the drive.

When you run a cmdlet outside of an Active Directory provider drive against an AD DS target, the default value of this parameter is the default naming context of the target domain.

When you run a cmdlet outside of an Active Directory provider drive against an AD LDS target, the default value is the default naming context of the target AD LDS instance if one has been specified by setting the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.
If no default naming context has been specified for the target AD LDS instance, then this parameter has no default value.

When the value of the *SearchBase* parameter is set to an empty string and you are connected to a global catalog (GC) port, all partitions are searched.
If the value of the *SearchBase* parameter is set to an empty string and you are not connected to a GC port, an error is thrown.

```yaml
Type: String
Parameter Sets: Filter, LdapFilter
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SearchScope
Specifies the scope of an Active Directory search.
The acceptable values for this parameter are:

- Base or 0
- OneLevel or 1
- Subtree or 2

A Base query searches only the current path or object.
A OneLevel query searches the immediate children of that path or object.
A Subtree query searches the current path or object and all children of that path or object.

```yaml
Type: ADSearchScope
Parameter Sets: Filter, LdapFilter
Aliases:
Accepted values: Base, OneLevel, Subtree

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

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### None or Microsoft.ActiveDirectory.Management.ADObject
An Active Directory object is received by the *Identity* parameter.
也接受派生类型，例如以下这些类型：

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADOrganizationalUnit**
- **Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy**
- **Microsoft.ActiveDirectory.Management.ADDomain**

## 输出

### Microsoft.ActiveDirectory.Management.ADObject
Returns one or more Active Directory objects.

The **Get-ADObject** cmdlet returns a default set of ADObject property values.
To retrieve additional **ADObject** properties, use the *Properties* parameter of the cmdlet.

To view the properties for an **ADObject** object, see the following examples.
To run these examples, replace \<object\> with an Active Directory object identifier.

To get a list of the default set of properties of an ADObject object, use the following command:

`Get-ADObject`\<object\>`| Get-Member`

To get a list of all the properties of an **ADObject** object, use the following command:

`Get-ADObject `<对象>` -Properties ALL | Get-Member`

## 备注

## 相关链接

[Move-ADObject](./Move-ADObject.md)

[New-ADObject](./New-ADObject.md)

[Remove-ADObject](./Remove-ADObject.md)

[重命名 AD 对象](./Rename-ADObject.md)

[恢复AD对象](./Restore-ADObject.md)

[Set-ADObject](./Set-ADObject.md)

[Sync-ADObject](./Sync-ADObject.md)

