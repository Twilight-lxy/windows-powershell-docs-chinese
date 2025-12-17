---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adresourceproperty?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADResourceProperty
---

# Get-ADResourceProperty

## 摘要
获取一个或多个资源属性。

## 语法

### 过滤器（默认值）
```
Get-ADResourceProperty [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Filter <String>
 [-Properties <String[]>] [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-Server <String>]
 [<CommonParameters>]
```

### 身份证明
```
Get-ADResourceProperty [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADResourceProperty>
 [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

### LdapFilter
```
Get-ADResourceProperty [-AuthType <ADAuthType>] [-Credential <PSCredential>] -LDAPFilter <String>
 [-Properties <String[]>] [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-Server <String>]
 [<CommonParameters>]
```

## 描述
`Get-ADResourceProperty` cmdlet 可以获取一个或多个资源属性。

## 示例

### 示例 1：获取过滤后的资源属性
```
PS C:\> Get-ADResourceProperty -Filter "SharesValuesWith -eq 'Country'"
```

这个命令会获取所有与名为“Country”的资源类型相关的属性，并为其提供建议值。

### 示例 2：获取指定的资源属性
```
PS C:\> Get-ADResourceProperty -Identity Authors
```

这个命令用于获取名为“Authors”的资源属性。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值为：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Active Directory PowerShell提供程序驱动器运行的。如果该cmdlet是从这样的提供程序驱动器运行的，则默认使用与该驱动器关联的账户的凭据。

要指定这个参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

如果执行该任务的代理账户没有目录级别的权限，Active Directory PowerShell 将返回一个终止错误。

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
指定一个用于检索 Active Directory 对象的查询字符串。该字符串使用 PowerShell 表达式语言（PowerShell Expression Language）的语法。PowerShell 表达式语言为 *Filter* 参数接收到的值类型提供了丰富的类型转换支持。其语法采用“按顺序排列”的表示方式，即操作符位于操作数和值之间。有关 *Filter* 参数的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter`。

语法：

以下语法使用了巴克斯-诺尔（Backus-Naur）形式来说明如何使用 PowerShell 表达式语言来处理这个参数。

\<filter\>  ::= "{" \<FilterComponentList\> "}"

\<FilterComponentList\> ::= \<FilterComponent\> | \<FilterComponent\> \<JoinOperator\> \<FilterComponent\> | \<NotOperator\> \<FilterComponent\>

\<FilterComponent\> ::= \<attr\> \<FilterOperator\> \<value\> | (" \<FilterComponent\> )"

\<FilterOperator\> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

<JoinOperator> ::= "-and" | "-or"

\<NotOperator\> ::= "-not"

\<attr\> ::= \<PropertyName\> | \<attribute的LDAPDisplayName\>

<value>::= <使用指定的<FilterOperator>将此值与<attr>进行比较>

要查看 `<value>` 支持的数据类型列表，请输入 `Get-Help about_ActiveDirectory_ObjectModel`。

注意：PowerShell中的通配符（除了*之外，例如?）不被*Filter*语法支持。

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

这个参数也可以通过管道获取该对象，或者你可以将该参数设置为一个对象实例。

```yaml
Type: ADResourceProperty
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
指定用于从服务器检索的输出对象的属性。使用此参数可以获取默认集合中未包含的属性。

请为该参数指定属性，将这些属性名称以逗号分隔的列表形式提供。如果要显示对象上设置的所有属性，请使用星号（*）。

要指定某个特定的扩展属性，请使用该属性的名称。对于非默认属性或扩展属性而言，您必须指定该属性在LDAP中的显示名称。

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
该参数用于指定 Active Directory 域服务查询返回的对象的最大数量。如果您希望接收所有对象，请将此参数设置为 `$Null`（空值）。您可以使用 Ctrl+C 来停止查询及对象的返回过程。

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

### -Server
指定要连接的 Active Directory 域服务（AD DS）实例，为此请提供相应的域名或目录服务器之一的值。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（AD LDS）、AD DS 或 Active Directory 快照实例。

以下是指定 Active Directory 域服务实例的几种方式：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

该参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

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

### 无或 Microsoft ActiveDirectory.Management.AdResourceProperty

## 输出

### Microsoft.ActiveDirectory.Management.ADResourceProperty

## 备注

## 相关链接

[New-ADResourceProperty](./New-ADResourceProperty.md)

[Remove-ADResourceProperty](./Remove-ADResourceProperty.md)

[Set-ADResourceProperty](./Set-ADResourceProperty.md)

