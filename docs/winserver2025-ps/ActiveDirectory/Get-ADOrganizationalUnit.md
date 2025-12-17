---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADOrganizationalUnit
---

# Get-ADOrganizationalUnit

## 摘要
获取一个或多个 Active Directory 组织单位（Organizational Units）。

## 语法

### 过滤器（默认设置）
```
Get-ADOrganizationalUnit [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Filter <String>
 [-Properties <String[]>] [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>]
 [-SearchScope <ADSearchScope>] [-Server <String>] [<CommonParameters>]
```

### 身份
```
Get-ADOrganizationalUnit [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADOrganizationalUnit> [-Partition <String>] [-Properties <String[]>] [-Server <String>]
 [<CommonParameters>]
```

### LdapFilter
```
Get-ADOrganizationalUnit [-AuthType <ADAuthType>] [-Credential <PSCredential>] -LDAPFilter <String>
 [-Properties <String[]>] [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>]
 [-SearchScope <ADSearchScope>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADOrganizationalUnit` cmdlet 可以获取一个组织单元（Organizational Unit，简称 OU）对象，或者执行搜索以获取多个 OU 对象。

`Identity` 参数用于指定要获取的 Active Directory 组（Organizational Unit，简称 OU）。您可以通过该组的 distinguished name 或 GUID 来识别它。此外，您还可以将此参数设置为一个 OU 对象变量（例如 `$<localOrganizationalUnitObject>`），或者通过管道将一个 OU 对象传递给 `Identity` 参数。

要搜索并检索多个组织单元（OU），请使用 *Filter* 或 *LDAPFilter* 参数。*Filter* 参数利用 PowerShell 表达式语言来编写 Active Directory 的查询字符串。PowerShell 表达式语言语法为 *Filter* 参数接收到的值类型提供了丰富的类型转换支持。有关 *Filter* 参数语法的更多信息，可以输入 `Get-Help about_ActiveDirectory_filter` 命令查看。如果您已有现有的轻量级目录访问协议（LDAP）查询字符串，可以使用 *LDAPFilter* 参数。

这个cmdlet会获取一组默认的OU对象属性。如果需要获取更多属性，可以使用*Properties*参数。有关如何确定计算机对象属性的更多信息，请参阅*Properties*参数的描述。

## 示例

#### 示例 1：获取一个域中的所有组织单位（Organizations, OU）
```powershell
PS C:\> Get-ADOrganizationalUnit -Filter 'Name -like "*"' | Format-Table Name, DistinguishedName -A
```
```output
Name                 DistinguishedName
----                 -----------------
Domain Controllers   OU=Domain Controllers,DC=FABRIKAM,DC=COM
UserAccounts         OU=UserAccounts,DC=FABRIKAM,DC=COM
Sales                OU=Sales,OU=UserAccounts,DC=FABRIKAM,DC=COM
Marketing            OU=Marketing,OU=UserAccounts,DC=FABRIKAM,DC=COM
Production           OU=Production,OU=UserAccounts,DC=FABRIKAM,DC=COM
HumanResources       OU=HumanResources,OU=UserAccounts,DC=FABRIKAM,DC=COM
NorthAmerica         OU=NorthAmerica,OU=Sales,OU=UserAccounts,DC=FABRIKAM,DC=COM
SouthAmerica         OU=SouthAmerica,OU=Sales,OU=UserAccounts,DC=FABRIKAM,DC=COM
Europe               OU=Europe,OU=Sales,OU=UserAccounts,DC=FABRIKAM,DC=COM
AsiaPacific          OU=AsiaPacific,OU=Sales,OU=UserAccounts,DC=FABRIKAM,DC=COM
Finance              OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM
Corporate            OU=Corporate,OU=UserAccounts,DC=FABRIKAM,DC=COM
ApplicationServers   OU=ApplicationServers,DC=FABRIKAM,DC=COM
Groups               OU=Groups,OU=Managed,DC=FABRIKAM,DC=COM
PasswordPolicyGroups OU=PasswordPolicyGroups,OU=Groups,OU=Managed,DC=FABRIKAM,DC=COM
Managed              OU=Managed,DC=FABRIKAM,DC=COM
ServiceAccounts      OU=ServiceAccounts,OU=Managed,DC=FABRIKAM,DC=COM
```

这个命令可以获取一个域中的所有组织单位（Organizational Units，简称OU）。

### 示例 2：通过其唯一名称获取组织单元（OU）
```powershell
PS C:\> Get-ADOrganizationalUnit -Identity 'OU=AsiaPacific,OU=Sales,OU=UserAccounts,DC=FABRIKAM,DC=COM' | Format-Table Name,Country,PostalCode,City,StreetAddress,State -A
```
```output
Name        Country PostalCode City     StreetAddress    State
----        ------- ---------- ----     -------------    -----
AsiaPacific AU      4171       Balmoral 45 Martens Place QLD
```

这个命令会获取具有以下唯一名称（Distinguished Name）的组织单元（Organizational Unit，简称OU）：  
OU=AsiaPacific,OU=Sales,OU>UserAccounts,DC=FABRIKAM,DC=COM。

### 示例 3：获取子组织（OU）
```powershell
PS C:\> Get-ADOrganizationalUnit -LDAPFilter '(name=*)' -SearchBase 'OU=Sales,OU=UserAccounts,DC=FABRIKAM,DC=COM' -SearchScope OneLevel | Format-Table Name,Country,PostalCode,City,StreetAddress,State
```
```output
Name                    Country                 PostalCode             City                   StreetAddress          State
----                    -------                 ----------             ----                   -------------          -----
AsiaPacific             AU                      4171                   Balmoral               45 Martens Place       QLD
Europe                  UK                      NG34 0NI               QUARRINGTON            22 Station Rd
NorthAmerica            US                      02142                  Cambridge              1634 Randolph Street   MA
```

该命令使用LDAP过滤器来获取属于“Sales”组织单元（OU）下的其他组织单元。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值为：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”。

基本身份验证方法需要使用安全套接字层（SSL）连接。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Windows PowerShell提供程序的Active Directory模块驱动器中运行的。如果该cmdlet是从此类驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该cmdlet会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
指定一个用于检索 Active Directory 对象的查询字符串。该字符串使用 PowerShell 表达式语言语法。PowerShell 表达式语言语法为 *Filter* 参数接收到的值类型提供了丰富的类型转换支持。这种语法采用“按顺序排列”的表示方式，即操作符被放置在操作数和值之间。有关 *Filter* 参数的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter`。

语法：

以下语法使用了巴克斯-诺尔形式（Backus-Naur form）来说明如何使用 PowerShell 表达式语言来处理这个参数。

\<filter\>  ::= "{" \<FilterComponentList\> "}"

\<FilterComponentList\> ::= \<FilterComponent\> | \<FilterComponent\> \<JoinOperator\> \<FilterComponent\> | \<NotOperator\> \<FilterComponent\>

\<FilterComponent\> ::= \<attr\> \<FilterOperator\> \<value\> | ("(<FilterComponent\>)")

<FilterOperator> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

<JoinOperator> ::= "-and" | "-or"

\<NotOperator\> ::= "-not"

<attr> ::= <PropertyName> | <LDAPDisplayName of the attribute>

<value>::= <使用指定的<FilterOperator>将此值与<attr>进行比较>

要查看 `<value>` 支持的类型列表，请输入 `Get-Help about_ActiveDirectory_ObjectModel`。

注意：PowerShell中的通配符（除了*之外，例如?）不支持*Filter*语法。

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
通过提供以下值之一来指定一个 Active Directory 组织单元对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A Security Account Manager account name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个非终止性错误（即不会停止执行的错误）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

```yaml
Type: ADOrganizationalUnit
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -LDAPFilter
指定一个用于过滤 Active Directory 对象的 LDAP 查询字符串。您可以使用此参数来运行现有的 LDAP 查询。`Filter` 参数的语法支持与 LDAP 语法相同的功能。有关更多信息，请参阅 `Filter` 参数的描述，或输入 `Get-Help about_ActiveDirectory_filter` 命令。

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
指定 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器上支持的命名上下文之一。此 cmdlet 会在此分区中搜索由 *Identity* 参数定义的对象。

在许多情况下，如果未指定`Partition`参数的值，则会使用默认值。确定默认值的规则如下所示。请注意，列出的规则会按顺序依次进行评估；一旦确定了默认值，后续的规则将不再被评估。

在 Active Directory 域服务环境中，*Partition* 的默认值会在以下情况下被设置：

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent (DSA) object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Partition* parameter will not take any default value.

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
指定要从服务器检索的输出对象的属性。使用此参数可以获取默认属性集未包含的属性。

为该参数指定属性，可以使用名称列表，并用逗号分隔各个属性值。如果要显示对象上设置的所有属性，请使用星号（*）。

要指定某个特定的扩展属性，请使用该属性的名称。对于非默认属性或扩展属性，您必须指定该属性的 LDAP 显示名称。

要获取对象的属性并将其显示出来，你可以使用与该对象关联的 `Get-*` cmdlet，并将输出结果传递给 `Get-Member` cmdlet。

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
指定 AD DS 查询返回的最大对象数量。如果您希望接收所有对象，请将此参数设置为 $Null（空值）。您可以使用 Ctrl+C 来停止查询和对象的返回过程。

默认值是 `$Null`。

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

当你从 Active Directory 提供程序驱动器运行某个 cmdlet 时，该参数的默认值是该驱动器的当前路径。

当你在非 Active Directory 提供程序驱动器的环境中运行一个 cmdlet 并针对 AD DS 目标进行操作时，该参数的默认值就是目标域的默认命名上下文。

当您在非 Active Directory 提供程序驱动器环境下运行 cmdlet 且目标为 AD LDS 实例时，其默认值将是该 AD LDS 实例的默认命名上下文（前提是已通过设置 Active Directory 目录服务代理对象（**nTDSDSA**）的 **msDS-defaultNamingContext** 属性来指定该默认命名上下文）。如果未为目标 AD LDS 实例指定任何默认命名上下文，则此参数将没有默认值。

当 `SearchBase` 参数的值被设置为空字符串，并且您连接到了全局目录（Global Catalog，简称 GC）端口时，将会搜索所有分区。如果 `SearchBase` 参数的值被设置为空字符串，但您没有连接到 GC 端口，则会抛出一个错误。

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
用于指定 Active Directory 搜索的范围。该参数的可接受值包括：

- Base or 0
- OneLevel or 1
- Subtree or 2

基础查询（Base query）仅搜索当前路径或对象。一级查询（OneLevel query）搜索该路径或对象的直接子节点。子树查询（Subtree query）则同时搜索当前路径或对象及其所有子节点。

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
指定要连接的 AD DS 实例，为此需要提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型中的任意一种：AD LDS、AD DS 或 Active Directory 快照实例。

以下列任意一种方式指定 AD DS 实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

该参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的列出顺序：

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft.ActiveDirectory.Management.ADOrganizationalUnit
一个OU（组织单位）对象通过*Identity*参数被接收。

## 输出

### Microsoft ActiveDirectory Management.ADOrganizationalUnit
返回一个或多个OU（组织单元）对象。

此 cmdlet 返回一组默认的 **ADOrganizational** 属性值。若要检索更多的 **ADOrganizational** 属性，请使用 *Properties* 参数。

要查看 **ADOrganizational** 对象的属性，请参阅以下示例。运行这些示例时，请将 `<organizational unit>` 替换为 OU 标识符（例如 OU 的唯一名称）。

要获取 **ADOrganizational** 对象的默认属性列表，请使用以下命令：

`Get-ADOrganizationalUnit <组织单位名称> | Get-Member`

要获取一个 **ADOrganizational** 对象的所有属性列表，请使用以下命令：

```powershell
Get-ADOrganizationalUnit <组织单位名称> -Properties *
| Get-Member
```

## 备注

## 相关链接

[New-ADOrganizationalUnit](./New-ADOrganizationalUnit.md)

[Remove-ADOrganizationalUnit](./Remove-ADOrganizationalUnit.md)

[Set-ADOrganizationalUnit](./Set-ADOrganizationalUnit.md)

