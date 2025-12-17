---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adreplicationsitelink?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADReplicationSiteLink
---

# Get-ADReplicationSiteLink

## 摘要
根据指定的过滤器返回特定的 Active Directory 站点链接或一组站点链接。

## 语法

### 过滤器（默认设置）
```
Get-ADReplicationSiteLink [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Filter <String>
 [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

### 身份
```
Get-ADReplicationSiteLink [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADReplicationSiteLink> [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADReplicationSiteLink` cmdlet 可用于根据指定的过滤条件返回某个特定的 Active Directory 站点链接或一组站点链接。站点链接用于连接两个或多个站点，它们体现了关于站点之间互联方式以及复制流量传输方法的管理员策略。必须通过站点链接将各个站点连接起来，以便每个站点上的域控制器能够复制 Active Directory 的更改。

## 示例

### 示例 1：获取所有复制站点链接
```
PS C:\> Get-ADReplicationSiteLink -Filter *
```

这个命令可以获取所有网站链接。

### 示例 2：获取所有指定的复制站点链接
```
PS C:\> Get-ADReplicationSiteLink -Filter "SitesIncluded -eq 'NorthAmerica'" | Format-Table Name,SitesIncluded -A
```

这个命令可以获取所有包含“NorthAmerica”字样的网站链接。

### 示例 3：获取过滤后的复制站点链接
```
PS C:\> Get-ADReplicationSiteLink -Filter "Cost -gt 100 -and ReplicationFrequencyInMinutes -lt 15"
```

这个命令会获取所有成本大于100且复制频率小于15分钟的站点链接。

### 示例 4：通过名称获取复制站点链接
```
PS C:\> Get-ADReplicationSiteLink -Identity "Europe-Asia"
```

这个命令可以获取名为“Europe-Asia”的网站链接。

### 示例 5：获取复制站点链接的指定属性
```
PS C:\> Get-ADReplicationSiteLink -Identity "Europe-Asia" -Properties ReplicationSchedule
```

这个命令用于获取名为“Europe-Asia”的站点链接的**ReplicationSchedule**属性。

## 参数

### -AuthType
指定要使用的身份验证方法。此参数的可接受值为：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从此类驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

如果该执行任务的账户没有目录级别的权限，那么适用于 Windows PowerShell 的 Active Directory 模块将会返回一个终止错误（即程序会立即退出）。

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

以下语法使用了巴克斯-诺尔（Backus-Naur）形式来展示如何使用 PowerShell 表达式语言来处理这个参数。

<filter> ::= "{" <FilterComponentList> """

<FilterComponentList> ::= <FilterComponent> | <FilterComponent> <JoinOperator> <FilterComponent> | <NotOperator> <FilterComponent>

\<FilterComponent\> ::= \<attr\> \<FilterOperator\> \<value\> | ("(<FilterComponent\>)")

<FilterOperator> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

<JoinOperator> ::= "-and" | "-or"

\<NotOperator\> ::= "-not"

<attr> ::= <PropertyName> | <LDAPDisplayName of the attribute>

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

- A distinguished name
- A GUID (objectGUID)

该 cmdlet 会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它将返回一个非终止性的错误（即无法继续执行的错误）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

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

### -Properties
指定用于从服务器检索的输出对象的属性。使用此参数可以获取默认集合中未包含的属性。

请以逗号分隔的形式列出该参数的属性名称。如果要显示对象上设置的所有属性，请使用 *（星号）。

要指定某个特定的扩展属性，请使用该属性的名称。对于非默认属性或扩展属性，必须指定该属性的LDAP显示名称。

要检索对象的属性并显示它们，你可以使用与该对象关联的 `Get-*` cmdlet，并将输出结果传递给 `Get-Member` cmdlet。

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
指定要连接的 Active Directory 域服务（AD DS）实例，为此提供相应的域名或目录服务器之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（AD LDS）、AD DS 或 Active Directory 快照实例。

以下是指定 Active Directory 域服务实例的几种方式：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft ActiveDirectory.Management.AdReplicationSiteLink
站点链接对象是通过“Identity”参数接收到的。

## 输出

### Microsoft ActiveDirectory.Management ADReplicationSiteLink

## 备注

## 相关链接

[New-ADReplicationSiteLink](./New-ADReplicationSiteLink.md)

[Remove-ADReplicationSiteLink](./Remove-ADReplicationSiteLink.md)

[Set-ADReplicationSiteLink](./Set-ADReplicationSiteLink.md)

