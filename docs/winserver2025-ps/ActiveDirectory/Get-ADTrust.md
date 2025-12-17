---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adtrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADTrust
---

# Get-ADTrust

## 摘要
获取目录中所有受信任的域名对象。

## 语法

### 过滤器（默认值）
```
Get-ADTrust [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Filter <String> [-Properties <String[]>]
 [-Server <String>] [<CommonParameters>]
```

### 身份
```
Get-ADTrust [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADTrust>
 [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

### InputObject
```
Get-ADTrust [-AuthType <ADAuthType>] [-Credential <PSCredential>] -InputObject <Object>
 [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

### LdapFilter
```
Get-ADTrust [-AuthType <ADAuthType>] [-Credential <PSCredential>] -LDAPFilter <String> [-Properties <String[]>]
 [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADTrust` cmdlet 会返回目录中所有的受信任域对象。

## 示例

#### 示例 1：获取林中所有受信任的域对象
```
PS C:\> Get-ADTrust -Filter *
```

这个命令可以获取森林中所有的受信任域对象。

### 示例 2：获取经过过滤的受信任域对象
```
PS C:\> Get-ADTrust -Filter "Target -eq 'corp.contoso.com'"
```

这个命令会获取所有以 corp.contoso.com 作为信任伙伴的可信域对象。

### 示例 3：获取指定的受信任域对象
```
PS C:\> Get-ADTrust -Identity "corp.contoso.com"
```

这个命令用于获取名为 corp.contoso.com 的受信任域对象。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值包括：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Active Directory PowerShell提供程序驱动器运行的。如果该cmdlet是从此类提供程序驱动器运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过脚本或使用 **Get-Credential** cmdlet 来创建一个 PSCredential 对象。之后，你可以将 *Credential* 参数设置为这个 PSCredential 对象。

如果执行任务的账户没有目录级别的权限，Active Directory PowerShell 会返回一个终止错误。

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
指定一个用于检索 Active Directory 对象的查询字符串。该字符串使用 PowerShell 表达式语言（PowerShell Expression Language）的语法。PowerShell 表达式语言为 *Filter* 参数接收到的值类型提供了丰富的类型转换支持。其语法采用“按顺序排列”的表示方式，即操作符位于操作数和值之间。有关 *Filter* 参数的更多信息，请输入 `Get-Help about_ActiveDirectory_filter` 命令。

语法：

以下语法使用了巴克斯-诺尔（Backus-Naur）表示法来说明如何使用 PowerShell 表达式语言来处理这个参数。

<filter> ::= "{" <FilterComponentList> "}"

<FilterComponentList> ::= <FilterComponent> | <FilterComponent> <JoinOperator> <FilterComponent> | <NotOperator> <FilterComponent>

\<FilterComponent\> ::= \<attr\> \<FilterOperator\> \<value\> | ("(<FilterComponent\>)")

<FilterOperator> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

\<JoinOperator\> ::= "-and" | "-or"

\<NotOperator\> ::= "-not"

\<attr\> ::= \<PropertyName\> | \<LDAPDisplayName of the attribute\>

<value>::= <使用指定的<FilterOperator>将此值与<attr>进行比较>

要查看 `<value>` 支持的数据类型列表，请输入 `Get-Help about_ActiveDirectory_ObjectModel`。

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

- A Distinguished Name
- A GUID (objectGUID)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个“非终止性错误”（即无法继续执行的错误）。

这个参数也可以通过数据流（pipeline）获取相应的对象，或者你可以将这个参数设置为某个对象的实例。

```yaml
Type: ADTrust
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定一个 Active Directory 输入对象。此参数可以接受以下对象类型中的一种：

- ADForest
- ADDomain
- ADObject

该cmdlet将根据指定的输入对象检索相应的**ADTrust**信息。

```yaml
Type: Object
Parameter Sets: InputObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -LDAPFilter
用于指定一个 LDAP 查询字符串，该字符串用于过滤 Active Directory 对象。您可以使用此参数来运行现有的 LDAP 查询。`Filter` 参数的语法支持与 LDAP 语法相同的功能。有关更多信息，请参阅 `Filter` 参数的描述，或输入 `Get-Help about_ActiveDirectory_Filter` 命令。

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
指定用于从服务器检索的输出对象的属性。使用此参数可以获取默认集合中未包含的属性。

请以逗号分隔的名称列表形式指定此参数的属性。若要显示对象上设置的所有属性，请使用星号（*）。

要指定某个特定的扩展属性，请使用该属性的名称。对于非默认属性或扩展属性，必须指定该属性的LDAP显示名称。

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

### -Server
指定要连接的 AD DS 实例，为此需要提供一个相应的域名或目录服务器的名称。该服务可以是以下类型之一：AD LDS、AD DS 或 Active Directory 快照实例。

以下是指定 AD DS 实例的几种方式：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft.ActiveDirectory.Management.ADTrust
一个受信任的域对象通过*Identity*参数被接收。

## 输出

### Microsoft.ActiveDirectory.Management.ADTrust

## 备注
* This cmdlet does not work with an Active Directory snapshot.

## 相关链接

