---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADGroup
---

# Get-ADGroup

## 摘要
获取一个或多个 Active Directory 组。

## 语法

### 过滤器（默认设置）
```
Get-ADGroup [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Filter <String> [-Properties <String[]>]
 [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>] [-SearchScope <ADSearchScope>]
 [-Server <String>] [-ShowMemberTimeToLive] [<CommonParameters>]
```

### 身份
```
Get-ADGroup [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADGroup> [-Partition <String>]
 [-Properties <String[]>] [-Server <String>] [-ShowMemberTimeToLive] [<CommonParameters>]
```

### LdapFilter
```
Get-ADGroup [-AuthType <ADAuthType>] [-Credential <PSCredential>] -LDAPFilter <String> [-Properties <String[]>]
 [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>] [-SearchScope <ADSearchScope>]
 [-Server <String>] [-ShowMemberTimeToLive] [<CommonParameters>]
```

## 描述
`Get-ADGroup` cmdlet 可以获取一个组，或者执行搜索操作以从 Active Directory 中检索多个组。

`Identity` 参数用于指定要获取的 Active Directory 组。您可以通过该组的唯一名称（DN）、GUID、安全标识符（SID）或安全账户管理器（SAM）帐户名来识别该组。此外，您还可以指定组对象变量，例如 `$<localGroupObject>`。

要搜索并检索多个组，请使用 *Filter* 或 *LDAPFilter* 参数。*Filter* 参数利用 PowerShell 表达式语言来为 Active Directory 编写查询字符串。PowerShell 表达式语言语法为 *Filter* 参数接收的值类型提供了丰富的类型转换支持。有关 *Filter* 参数语法的更多信息，可以输入 `Get-Help about_ActiveDirectory_filter` 命令查看。如果您已经有现有的轻型目录访问协议（LDAP）查询字符串，那么可以使用 *LDAPFilter* 参数。

此cmdlet可获取一组默认的组对象属性。若要获取更多属性，请使用*Properties*参数。有关如何确定组对象属性的详细信息，请参阅*Properties*参数的说明。

## 示例

### 示例 1：根据 SAM 账户名称获取一个组
```
PS C:\> Get-ADGroup -Identity Administrators
DistinguishedName : CN=Administrators,CN=Builtin,DC=Fabrikam,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : Administrators
ObjectClass       : group
ObjectGUID        : 02ce3874-dd86-41ba-bddc-013f34019978
SamAccountName    : Administrators
SID               : S-1-5-32-544
```

这个命令用于获取名为“Administrators”的SAM账户所属的组。

### 示例 2：根据 SID 获取一个组
```
PS C:\> Get-ADGroup -Identity S-1-5-32-544 -Properties member
DistinguishedName : CN=Administrators,CN=Builtin,DC=Fabrikam,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
member            : {CN=Domain Admins,CN=Users,DC=Fabrikam,DC=com, CN=Enterprise Admins,CN=Users,DC=Fabrikam,DC=com, CN=LabAdmin,CN=Users,DC=Fabrikam,DC=com, C
N=Administrator,CN=Users,DC=Fabrikam,DC=com}
Name              : Administrators
ObjectClass       : group
ObjectGUID        : 02ce3874-dd86-41ba-bddc-013f34019978
SamAccountName    : Administrators
SID               : S-1-5-32-544
```

这个命令用于获取SID为S-1-5-32-544的组及其属性成员。

### 示例 3：获取一个群组并过滤结果
```
PS C:\> Get-ADGroup -Filter 'GroupCategory -eq "Security" -and GroupScope -ne "DomainLocal"'
```

这个命令会获取所有属于“Security”组类别（GroupCategory）但组范围（GroupScope）不是“DomainLocal”的群组。

### 示例 4：从指定的搜索库中获取一组数据，并对结果进行过滤
```
PS C:\> Get-ADGroup -Server localhost:60000 -Filter "GroupScope -eq 'DomainLocal'" -SearchBase "DC=AppNC"


DistinguishedName : CN=AlphaGroup,OU=AccountDeptOU,DC=AppNC
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : AlphaGroup
ObjectClass       : group
ObjectGUID        : 6498c9fb-7c62-48fe-9972-1461f7f3dec2
SID               : S-1-510474493-936115905-2475435479-1276657127-1006239422-938965137

DistinguishedName : CN=BranchOffice1,OU=AccountDeptOU,DC=AppNC
GroupCategory     : Security
GroupScope        : DomainLocal
Name              : BranchOffice1
ObjectClass       : group
ObjectGUID        : 0b7504c5-482b-4a73-88f5-8a76960e4568
SID               : S-1-510474493-936115905-2534227223-1194883713-3669005192-3746664089

DistinguishedName : CN=AccountLeads,OU=AccountDeptOU,DC=AppNC
GroupCategory     : Distribution
GroupScope        : DomainLocal
Name              : AccountLeads
ObjectClass       : group
ObjectGUID        : b20c032b-2de9-401a-b48c-341854a37254
SID               : S-1-510474493-936115905-2813670187-1179675302-2001457839-270172950
```

此命令从 AD LDS 实例的 AppNC 分区中获取所有 DomainLocal 组。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的提供程序驱动器中运行的，则默认凭据将是与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行该任务的代理（agent）没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误（terminating error）。

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
指定一个用于检索 Active Directory 对象的查询字符串。该字符串使用 PowerShell 表达式语言语法。PowerShell 表达式语言语法为 *Filter* 参数接收到的值类型提供了丰富的类型转换支持。该语法采用“按顺序排列”的表示方式，即运算符被放置在操作数和值之间。有关 *Filter* 参数的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter`。

语法：

以下语法使用了巴克斯-诺尔形式（Backus-Naur Form）来说明如何使用 PowerShell 表达式语言来处理这个参数。

<filter> ::= "{" <FilterComponentList> "}"

\<FilterComponentList\> ::= \<FilterComponent\> | \<FilterComponent\> \<JoinOperator\> \<FilterComponent\> | \<NotOperator\>  \<FilterComponent\>

\<FilterComponent\> ::= \<attr\> \<FilterOperator\> \<value\> | (" \<FilterComponent\> ")"

\<FilterOperator\> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

<JoinOperator> ::= "-and" | "-or"

\<NotOperator\> ::= "-not"

\<attr\> ::= \<propertyName\> | \<该属性的 LDAP 显示名称\>

\<value\>::= 使用指定的 \<FilterOperator\> 将此值与 \<attr\> 进行比较

要获取 `<value>` 支持的数据类型列表，请输入 `Get-Help about_ActiveDirectory_ObjectModel`。

注意：PowerShell中的通配符（除了`\*`之外，例如`?`）不支持`*Filter`语法。

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
通过提供以下值之一来指定一个 Active Directory 组对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A security accounts manager account name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索该对象。如果找到两个或多个对象，cmdlet会返回一个非终止性的错误（即无法继续执行的错误）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

```yaml
Type: ADGroup
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -LDAPFilter
指定一个用于过滤 Active Directory 对象的 LDAP 查询字符串。您可以使用此参数来运行现有的 LDAP 查询。`Filter` 参数的语法支持与 LDAP 语法相同的功能。有关更多信息，请参阅 `Filter` 参数的描述，或输入 `Get-Help about_ActiveDirectory_filter` 命令进行查询。

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
指定一个 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器上支持的命名上下文之一。此 cmdlet 会在该分区中搜索由 *Identity* 参数所定义的对象。

在许多情况下，如果未指定`Partition`参数的值，则会使用默认值。确定默认值的规则如下所示。请注意，首先列出的规则会被优先评估；一旦确定了默认值，就不会再继续评估其他规则了。

在 Active Directory 域服务（AD DS）环境中，以下情况下会为“分区”（Partition）设置默认值：

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* will be set to the default naming context.
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

### -Properties
指定要从服务器检索的输出对象的属性。使用此参数可以获取默认集合中未包含的属性。

为此参数指定属性值，可以使用逗号分隔的名称列表。如果要显示对象上设置的所有属性，请使用星号（*）。

要指定某个特定的扩展属性，请使用该属性的名称。对于非默认属性或扩展属性而言，必须指定该属性的 LDAP 显示名称。

要获取某个对象的属性并将其显示出来，你可以使用与该对象关联的 `Get-*` cmdlet，并将输出结果传递给 `Get-Member` cmdlet。

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
指定在 AD DS 查询中每页显示的对象数量。

默认情况下，每页显示256个对象。

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
指定 AD DS 查询返回的对象的最大数量。如果您希望接收所有对象，请将此参数设置为 $Null（空值）。您可以使用 Ctrl+C 来停止查询和对象的返回过程。

默认值是 $Null。

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
指定一个用于搜索的 Active Directory 路径。

当你从 Active Directory 提供程序驱动器运行一个 cmdlet 时，此参数的默认值是该驱动器的当前路径。

当你在非 Active Directory 提供程序驱动器的情况下运行一个 cmdlet 并将其用于 AD DS 目标对象时，该参数的默认值就是目标域的默认命名上下文。

当你在非 Active Directory 提供者驱动器的情况下运行 cmdlet 时，如果为 AD LDS 实例设置了 Active Directory 目录服务代理对象（**nTDSDSA**）的 **msDS-defaultNamingContext** 属性来指定命名上下文，则默认值就是该目标 ADSLS 实例的默认命名上下文。如果没有为目标 AD LDS 实例指定任何默认命名上下文，那么这个参数就没有默认值。

当 *SearchBase* 参数的值被设置为空字符串，并且您连接到了垃圾回收（GC）端口时，系统会搜索所有分区。如果 *SearchBase* 参数的值被设置为空字符串，但您没有连接到 GC 端口，则会抛出错误。

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
指定 Active Directory 搜索的范围。此参数的可接受值为：

- Base or 0
- OneLevel or 1
- Subtree or 2

基础查询（Base query）仅搜索当前路径或对象。一级查询（OneLevel query）搜索该路径或对象的直接子节点。子树查询（Subtree query）则同时搜索当前路径或对象以及该路径或对象的所有子节点。

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
指定要连接的 Active Directory 域服务实例，为此需要提供相应的域名或目录服务器对应的值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot instance）。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

该参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

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

### -ShowMemberTimeToLive
表示此cmdlet会显示组成员的生存时间（Time to Live，简称TTL）值。

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

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft.ActiveDirectory.Management_ADGroup
一个组对象是通过*Identity*参数接收到的。

## 输出

### Microsoft ActiveDirectory.Management.AdGroup
返回一个或多个组对象。

`Get-ADGroup` cmdlet 返回一组默认的 `ADGroup` 属性值。若要检索更多的 `ADGroup` 属性，请使用 `Properties` 参数。

要查看 **ADGroup** 对象的属性，请参考以下示例。运行这些示例时，请将 `<group>` 替换为组标识符（例如 Administrators）。

要获取一个 **ADGroup** 对象的默认属性列表，请使用以下命令：

`Get-ADGroup "<group>" | Get-Member`

要获取一个 **ADGroup** 对象的所有属性列表，请使用以下命令：

```
Get-ADGroup "<group>" -Properties * | Get-Member
```

## 备注

## 相关链接

[New-ADGroup](./New-ADGroup.md)

[Remove-ADGroup](./Remove-ADGroup.md)

[Set-ADGroup](./Set-ADGroup.md)

