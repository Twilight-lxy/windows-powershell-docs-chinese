---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adoptionalfeature?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADOptionalFeature
---

# Get-ADOptionalFeature

## 摘要
获取一个或多个 Active Directory 可选功能。

## 语法

### 过滤器（默认设置）
```
Get-ADOptionalFeature [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Filter <String>
 [-Properties <String[]>] [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>]
 [-SearchScope <ADSearchScope>] [-Server <String>] [<CommonParameters>]
```

### 身份
```
Get-ADOptionalFeature [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADOptionalFeature>
 [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

### LdapFilter
```
Get-ADOptionalFeature [-AuthType <ADAuthType>] [-Credential <PSCredential>] -LDAPFilter <String>
 [-Properties <String[]>] [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>]
 [-SearchScope <ADSearchScope>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADOptionalFeature` cmdlet 可以获取一个可选功能，或者执行搜索以从 Active Directory 中检索多个可选功能。

`Identity` 参数用于指定您想要获取的 Active Directory 可选功能。您可以通过该功能的唯一名称（distinguished name）、功能 GUID 或对象 GUID 来识别它。此外，您还可以将该参数设置为某个可选功能对象变量（例如 `$<localOptionalFeatureObject>`），或者通过管道将一个可选功能对象传递给 `Identity` 参数。

要搜索并检索多个可选功能，请使用 *Filter* 或 *LDAPFilter* 参数。*Filter* 参数使用 PowerShell 表达式语言来为 Active Directory 编写查询字符串。PowerShell 表达式语言语法为 *Filter* 参数接收的值类型提供了丰富的类型转换支持。有关 *Filter* 参数语法的更多信息，可以输入 `Get-Help about_ActiveDirectory_Filter`。如果您已经有现有的轻量级目录访问协议 (LDAP) 查询字符串，可以使用 *LDAPFilter* 参数。

这个cmdlet会获取一组默认的可选特性对象属性。如果要获取更多属性，可以使用*Properties*参数。有关如何确定计算机对象的属性的更多信息，请参阅*Properties*参数的描述。

## 示例

### 示例 1：获取森林中所有可用的特征
```
PS C:\> Get-ADOptionalFeature -Filter *
```

这个命令可以获取当前森林中所有可用的可选功能。

### 示例 2：获取指定的可选功能
```
PS C:\> Get-ADOptionalFeature -Identity 'Recycle Bin Feature'
```

这个命令用于获取一个名为“回收站功能”（Recycle Bin Feature）的可选组件/特性。

### 示例 3：通过特征的唯一标识符（GUID）获取该特征
```
PS C:\> Get-ADOptionalFeature -Identity 766ddcd8-acd0-445e-f3b9-a7f9b6744f2a
```

这个命令用于获取具有特征GUID 766ddcd8-acd0-445e-f3b9-a7f9b6744f2a的可选功能。

### 示例 4：在 AD LDS 实例中获取指定的特征
```
PS C:\> Get-ADOptionalFeature -Identity 'Recycle Bin Feature' -Server server1:50000
```

此命令用于在 AD LDS 实例中启用可选的“回收站功能”。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Windows PowerShell提供程序的Active Directory模块驱动器中运行的。如果该cmdlet是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行该任务的账号没有目录级权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
指定一个用于检索 Active Directory 对象的查询字符串。该字符串使用 PowerShell 表达式语言（PowerShell Expression Language）的语法。PowerShell 表达式语言为 *Filter* 参数接收到的值类型提供了丰富的类型转换支持。其语法采用“按顺序排列”的表示方式，即操作符位于操作数和值之间。有关 *Filter* 参数的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter` 命令。

语法：

以下语法使用了 Backus-Naur 表示法来说明如何使用 PowerShell 表达式语言来处理这个参数。

<filter> ::= "{" <FilterComponentList> "}"

<FilterComponentList> ::= <FilterComponent> | <FilterComponent> <JoinOperator> <FilterComponent> | <NotOperator> <FilterComponent>

<FilterComponent> ::= <attr> <FilterOperator> <value> | ("<FilterComponent>)"

\<FilterOperator\> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

\<JoinOperator\> ::= "-and" | "-or"

\<NotOperator\> ::= "-not"

\<attr\> ::= \<propertyName\> | \<该属性的 LDAP 显示名称\>

<value>::= <使用指定的<FilterOperator>将此值与<attr>进行比较>

要查看 `<value>` 支持的数据类型列表，请输入 `Get-Help about_ActiveDirectory_ObjectModel`。

注意：PowerShell 中除了星号（*）之外的通配符（例如问号（?））不支持 *Filter* 语法。

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
通过提供以下值之一来指定一个 Active Directory 可选功能对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A fully qualified domain name
- A GUID (objectGUID)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个无法终止的错误信息。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个可选的功能对象实例。

```yaml
Type: ADOptionalFeature
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
指定在一个Active Directory域服务（AD DS）查询的结果页面中应显示的对象数量。

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
指定 AD DS 查询返回的对象的最大数量。如果您希望接收所有对象，请将此参数设置为 $Null（空值）。您可以使用 Ctrl+C 来停止查询和对象返回过程。

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
指定一个要在其中进行搜索的 Active Directory 路径。

当你从 Active Directory 提供程序驱动器运行某个 Cmdlet 时，该参数的默认值是该驱动器的当前路径。

当你在非 Active Directory 提供程序驱动器的环境下运行某个 Cmdlet 并针对 AD DS 目标进行操作时，该参数的默认值就是目标域的默认命名上下文。

当你在非 Active Directory 提供者驱动器环境下运行 cmdlet 且目标为 AD LDS 实例时，该参数的默认值将是目标 AD LDS 实例的默认命名上下文（前提是已通过设置 Active Directory 目录服务代理对象（**nTDSDSA**）的 **msDS-defaultNamingContext** 属性来指定该默认命名上下文）。如果未为目标 AD LDS 实例指定任何默认命名上下文，则此参数没有默认值。

当 `SearchBase` 参数的值被设置为空字符串，并且您连接到了全局目录（GC）端口时，系统会搜索所有分区。如果 `SearchBase` 参数的值被设置为空字符串，但您并未连接到 GC 端口，则会抛出错误。

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
用于指定 Active Directory 搜索的范围。此参数的可接受值为：

- Base or 0
- OneLevel or 1
- Subtree or 2

基础查询（Base query）仅搜索当前路径或对象。一级查询（OneLevel query）会搜索该路径或对象的直接子节点。子树查询（Subtree query）则会搜索当前路径或对象以及该路径或对象的所有子节点。

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
指定要连接的 Active Directory 域服务（AD DS）实例，方法是为相应的域名或目录服务器提供一个以下值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（AD LDS）、AD DS 或 Active Directory 快照实例。

请以下列方式之一指定 AD DS 实例：

域名值：

- FQDN
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们在列表中的排列顺序：

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft.ActiveDirectoryManagement.ADOptionalFeature
*Identity* 参数接收一个可选的功能对象。

## 输出

### Microsoft.ActiveDirectory.Management_ADOptionalFeature
返回一个或多个可选的功能对象。

此cmdlet返回一组默认的**ADOptionalFeature**属性值。若要检索更多的**ADOptionalFeature**属性，请使用*Properties*参数。

要查看 **ADOptionalFeature** 对象的属性，请参考以下示例。运行这些示例时，需要将 `<optional feature>` 替换为可选功能的标识符（例如该可选功能的唯一名称）。

要获取 `ADOptionalFeature` 对象的默认属性列表，请使用以下命令：

`Get-ADOptionalFeature `<可选功能>` | Get-Member`

要获取一个 **ADOptionalFeature** 对象的所有属性列表，请使用以下命令：

```powershell
Get-ADOptionalFeature <optional feature> -Properties ALL | Get-Member
```

## 备注

## 相关链接

[禁用 AD 可选功能](./Disable-ADOptionalFeature.md)

[Enable-ADOptionalFeature](./Enable-ADOptionalFeature.md)

