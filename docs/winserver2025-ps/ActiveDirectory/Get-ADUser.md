---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-aduser?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADUser
---

# Get-ADUser

## 摘要
获取一个或多个 Active Directory 用户。

## 语法

### 过滤器（默认值）
```
Get-ADUser [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Filter <String> [-Properties <String[]>]
 [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>] [-SearchScope <ADSearchScope>]
 [-Server <String>] [<CommonParameters>]
```

### 身份
```
Get-ADUser [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADUser> [-Partition <String>]
 [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

### LdapFilter
```
Get-ADUser [-AuthType <ADAuthType>] [-Credential <PSCredential>] -LDAPFilter <String> [-Properties <String[]>]
 [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>] [-SearchScope <ADSearchScope>]
 [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADUser` cmdlet 可以获取指定的用户对象，或者执行搜索以获取多个用户对象。

`Identity` 参数用于指定要获取的 Active Directory 用户。您可以通过用户的唯一名称（DN）、GUID、安全标识符（SID）或安全账户管理器（SAM）帐户名来识别该用户。此外，您还可以将该参数设置为某个用户对象变量（例如 `$<localUserObject>`），或者通过管道将用户对象传递给 `Identity` 参数。

要搜索并获取多个用户，可以使用 *Filter* 或 *LDAPFilter* 参数。*Filter* 参数使用 PowerShell 表达式语言来为 Active Directory 编写查询字符串。PowerShell 表达式语言语法为 *Filter* 参数接收的值类型提供了丰富的类型转换支持。有关 *Filter* 参数语法的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter`。如果您已经有现有的轻量级目录访问协议（LDAP）查询字符串，可以使用 *LDAPFilter* 参数。

此cmdlet用于获取一组默认的用户对象属性。若要获取更多属性，请使用 `_Properties_` 参数。有关如何确定用户对象的属性的更多信息，请参阅 `_Properties_` 参数的描述。

## 示例

#### 示例 1：获取容器中的所有用户
```powershell
PS C:\> Get-ADUser -Filter * -SearchBase "OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM"
```

这个命令会获取容器中所有属于以下组织单元（OU）的用户：OU=Finance、OU/UserAccounts，以及域控制器（DC）FABRIKAM和DC=COM。

### 示例 2：获取过滤后的用户列表
```powershell
PS C:\> Get-ADUser -Filter 'Name -like "*SvcAccount"' | Format-Table Name,SamAccountName -A
```

```Output
Name             SamAccountName
----             --------------
SQL01 SvcAccount SQL01
SQL02 SvcAccount SQL02
IIS01 SvcAccount IIS01
```

这个命令可以获取所有名字以 “SvcAccount” 结尾的用户。

### 示例 3：获取指定用户的所有属性
```powershell
PS C:\> Get-ADUser -Identity ChewDavid -Properties *
```

```Output
Surname           : David
Name              : Chew David
UserPrincipalName :
GivenName         : David
Enabled           : False
SamAccountName    : ChewDavid
ObjectClass       : user
SID               : S-1-5-21-2889043008-4136710315-2444824263-3544
ObjectGUID        : e1418d64-096c-4cb0-b903-ebb66562d99d
DistinguishedName : CN=Chew David,OU=NorthAmerica,OU=Sales,OU=UserAccounts,DC=FABRIKAM,DC=COM
```

这个命令可以获取使用SAM账户名称“ChewDavid”的用户的所有属性信息。

#### 示例 4：获取指定的用户
```powershell
PS C:\> Get-ADUser -Filter "Name -eq 'ChewDavid'" -SearchBase "DC=AppNC" -Properties "mail" -Server lds.Fabrikam.com:50000
```

此命令用于在 Active Directory 轻量级目录服务（AD LDS）实例中查找名为 ChewDavid 的用户。

### 示例 5：获取所有已启用的用户账户
```powershell
C:\PS> Get-ADUser -LDAPFilter '(!userAccountControl:1.2.840.113556.1.4.803:=2)'
```

这个命令使用LDAP过滤器来获取Active Directory中所有已启用的用户账户。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值包括：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Active Directory PowerShell 提供程序驱动器运行的。如果该 cmdlet 是从这样的提供程序驱动器运行的，则默认凭据将是与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，可以将 *Credential* 参数设置为该 **PSCredential** 对象。

如果执行该任务的账户没有目录级别的权限，Active Directory PowerShell 会返回一个终止错误。

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
指定一个用于检索 Active Directory 对象的查询字符串。该字符串使用 PowerShell 表达式语言（PowerShell Expression Language）的语法。PowerShell 表达式语言为 *Filter* 参数接收的值类型提供了丰富的类型转换支持。其语法采用“按顺序排列”的表示方式，即操作符位于操作数和值之间。有关 *Filter* 参数的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter` 命令。

语法：

以下语法使用了巴克斯-诺尔（Backus-Naur）形式来说明如何使用 PowerShell 表达式语言来处理这个参数。

<filter> ::= "{" <FilterComponentList> "}"

<FilterComponentList> ::= <FilterComponent> | <FilterComponent> <JoinOperator> <FilterComponent> | <NotOperator> <FilterComponent>

\<FilterComponent\> ::= \<attr\> \<FilterOperator\> \<value\> | ("(<FilterComponent\>)")

<FilterOperator> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

<JoinOperator> ::= "-and" | "-or"

\<NotOperator\> ::= "-not"

\<attr\> ::= \<PropertyName\> | \<LDAPDisplayName of the attribute\>

<value>::= <使用指定的<FilterOperator>将此值与<attr>进行比较>

要查看 `<value>` 支持的数据类型列表，请输入 `Get-Help about_ActiveDirectory_ObjectModel`。

注意：对于字符串类型的参数，PowerShell 在处理命令时会将过滤查询转换为字符串。当使用字符串变量作为过滤组件的值时，请确保该变量符合 [PowerShell 引用规则](/powershell/module/microsoft.powershell.core/about/about_quoting_rules)。例如，如果过滤表达式使用了双引号，则变量应使用单引号来括起来：**Get-ADUser -Filter "Name -like '$UserName'"**。相反，如果过滤表达式使用了大括号，则根本不需要对变量进行引用：**Get-ADUser -Filter {Name -like $UserName}**。

注意：PowerShell中的通配符（除了\*之外，例如?）不被*Filter*语法支持。

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
通过提供以下属性值之一来指定一个 Active Directory 用户对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索要查找的对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止的错误（即程序会一直处于错误状态而无法继续执行）。

这个参数也可以通过管道获取该对象，或者你可以将该参数设置为一个对象实例。

```yaml
Type: ADUser
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
指定 Active Directory 分区的唯一名称（Distinguished Name）。该唯一名称必须是当前目录服务器上支持的命名上下文之一。此 cmdlet 会在该分区中查找由 *Identity* 参数定义的对象。

在许多情况下，如果未指定“Partition”参数的值，则会使用默认值。确定默认值的规则如下所示。请注意，首先列出的规则会被优先评估；一旦确定了默认值，就不会再继续评估其他规则了。

在 Active Directory Domain Services (AD DS) 环境中，以下情况下会为“Partition”（分区）设置默认值：

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In AD LDS environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
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
指定从服务器检索的输出对象的属性。使用此参数可以获取默认集合中未包含的属性。

为该参数指定属性，可以使用逗号分隔的名称列表。若要显示对象上设置的所有属性，请使用 *（星号）。

要指定某个特定的扩展属性，请使用该属性的名称。对于非默认属性或扩展属性，您必须指定该属性的 LDAP 显示名称。

要检索对象的属性并将其显示出来，你可以使用与该对象关联的 `Get-*` cmdlet，并将输出结果传递给 `Get-Member` cmdlet。

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
指定在Active Directory域服务查询中每页显示的对象数量。

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
该参数用于指定 Active Directory 域服务查询返回的最大对象数量。如果您希望接收所有对象，请将此参数设置为 $Null（空值）。您可以使用 Ctrl+C 来停止查询及对象的返回过程。

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
指定一个用于在 Active Directory 中进行搜索的路径。

当您从 Active Directory 提供程序驱动器运行 cmdlet 时，此参数的默认值是该驱动器的当前路径。

当你在非 Active Directory 提供者驱动器的环境下运行一个 cmdlet 并针对 AD DS 目标执行操作时，该参数的默认值就是目标域的默认命名上下文。

当你在非 Active Directory 提供者驱动器的情况下运行 cmdlet 时，如果已经通过设置 Active Directory 目录服务代理（DSA）对象（**nTDSDSA**）的 **msDS-defaultNamingContext** 属性为 AD LDS 实例指定了命名上下文，则默认值就是该目标 ADSLS 实例的默认命名上下文。如果没有为目标 AD LDS 实例指定任何默认命名上下文，那么这个参数就没有默认值。

当 `SearchBase` 参数的值被设置为空字符串，并且您连接到的是 GC 端口时，系统会搜索所有分区。如果 `SearchBase` 参数的值被设置为空字符串，但您没有连接到 GC 端口，则会抛出一个错误。

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

`SearchScope` 类型中，当 `Base` 值被设置为特定用户时，查询将仅针对该用户进行。如果在 `SearchBase` 参数中指定了一个组织单元（OU），那么即使使用特定的过滤条件（如 `Filter` 语句），也不会返回任何结果。`OneLevel` 查询会搜索该路径或对象的直接子对象；此选项仅在 `SearchBase` 指定为组织单元时有效。如果查询的是某个具体用户，同样不会返回任何结果。`Subtree` 查询则会搜索当前路径或对象及其所有子对象。

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
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot instance）。

域名值：

- Fully qualified domain name (FQDN)
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

*Server* 参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们在列表中的排列顺序：

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无，或为 Microsoft.ActiveDirectory.Management_ADUser
用户对象是通过*Identity*参数接收到的。

## 输出

### Microsoft ActiveDirectory.Management.AdUser
返回一个或多个用户对象。

此cmdlet返回一组默认的**ADUser**属性值。若要获取额外的**ADUser**属性，请使用*Properties*参数。

要获取一个 **ADUser** 对象的默认属性列表，请使用以下命令：

`Get-ADUser `<user>` | Get-Member`

要获取 ADUser 对象中最常用属性的列表，请使用以下命令：

`Get-ADUser `<用户名称>` -Properties Extended | Get-Member`

要获取一个 **ADUser** 对象的所有属性列表，请使用以下命令：

`Get-ADUser "<用户>" -Properties * | Get-Member`

## 备注
* This cmdlet does not work with an Active Directory snapshot.

## 相关链接

[New-ADUser](./New-ADUser.md)

[Remove-ADUser](./Remove-ADUser.md)

[Set-ADUser](./Set-ADUser.md)
