---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adreplicationsitelinkbridge?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADReplicationSiteLinkBridge
---

# Get-ADReplicationSiteLinkBridge

## 摘要
根据指定的筛选条件获取特定的 Active Directory 站点链接桥接器（Site Link Bridge）或一组站点链接桥接器对象。

## 语法

### 过滤器（默认设置）
```
Get-ADReplicationSiteLinkBridge [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Filter <String>
 [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

### 身份识别
```
Get-ADReplicationSiteLinkBridge [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADReplicationSiteLinkBridge> [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADReplicationSiteLinkBridge` cmdlet 可以根据指定的过滤条件获取一个特定的 Active Directory 站点链接桥（site link bridge），或者获取一组站点链接桥对象。站点链接桥用于连接两个或多个站点链接，并实现这些站点链接之间的数据传输功能。桥中的每个站点链接都必须与桥内的另一个站点链接具有相同的关联目标站点（即它们都指向同一个 Active Directory 网域或站点）。

## 示例

### 示例 1：获取所有站点链接桥接（site link bridges）
```
PS C:\> Get-ADReplicationSiteLinkBridge -Filter *
```

这个命令可以获取所有站点链接桥接（site link bridges）的信息。

### 示例 2：获取筛选后的站点链接桥接器列表
```
PS C:\> Get-ADReplicationSiteLinkBridge -Filter "SiteLinksIncluded -eq 'NorthAmerica-Europe'" | FT Name,SiteLinksIncluded -A
```

这个命令会获取所有包含“NorthAmerica-Europe”站点链接的站点链接桥接（site link bridges）。

### 示例 3：获取指定的网站链接桥接（site link bridge）
```
PS C:\> Get-ADReplicationSiteLinkBridge -Identity "NorthAmerica-Asia"
```

这个命令用于获取名为“NorthAmerica-Europe”的站点链接桥接（site link bridge）。

### 示例 4：获取站点链接桥的属性
```
PS C:\> Get-ADReplicationSiteLinkBridge -Identity "NorthAmerica-Asia" -Properties *
```

这个命令可以获取名为“NorthAmerica-Europe”的站点链接桥的所有属性信息。

## 参数

### -AuthType
指定要使用的身份验证方法。此参数的可接受值包括：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Windows PowerShell提供程序的Active Directory模块驱动器中运行的。如果该cmdlet是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

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
指定一个用于检索 Active Directory 对象的查询字符串。该字符串使用 PowerShell 表达式语言（PowerShell Expression Language）的语法。PowerShell 表达式语言为 *Filter* 参数接收的值类型提供了丰富的类型转换支持。其语法采用“按顺序排列”的表示方式，即运算符位于操作数和值之间。有关 *Filter* 参数的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter` 命令。

语法：

以下语法采用了巴克斯-诺尔（Backus-Naur）形式来演示如何使用 PowerShell 表达式语言来处理这个参数。

\<filter\>  ::= "{" \<FilterComponentList\> "}"

<FilterComponentList> ::= <FilterComponent> | <FilterComponent> <JoinOperator> <FilterComponent> | <NotOperator> <FilterComponent>

\<FilterComponent\> ::= \<attr\> \<FilterOperator\> \<value\> | "(<FilterComponent\>)"

<FilterOperator> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

\<JoinOperator\> ::= "-and" | "-or"

\<NotOperator\> ::= "-not"

\<attr\> ::= \<propertyName\> | \<attribute的LDAPDisplayName\>

<value>::= <使用指定的<FilterOperator>将此值与<attr>进行比较>

要查看 `<value>` 支持的类型列表，请输入 `Get-Help about_ActiveDirectory_ObjectModel`。

注意：PowerShell中的通配符（除了*之外，例如?）不支持*Filter*语法。

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

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止的错误（即程序会一直处于错误状态而无法继续执行）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

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

### -Properties
指定从服务器检索的输出对象的属性。使用此参数可以获取默认集合中未包含的属性。

请以逗号分隔的名称列表形式为该参数指定属性。若要显示对象上设置的所有属性，请使用 *（星号）。

要指定某个特定的扩展属性，请使用该属性的名称。对于非默认属性或扩展属性而言，必须指定该属性的 LDAP 显示名称。

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
默认的身份验证方法是“Negotiate”。

基本认证方法需要使用安全套接字层（SSL）连接。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或为 Microsoft.ActiveDirectory.Management_ADReplicationSiteLinkBridge
一个站点链接桥接对象是通过“身份”（Identity）参数接收到的。

## 输出

### Microsoft.ActiveDirectory.Management_ADReplicationSiteLinkBridge

## 备注
* By default, the following site link bridge properties are returned:

- Name
- Description
- SiteLinksIncluded
- DN

## 相关链接

[New-ADReplicationSiteLinkBridge](./New-ADReplicationSiteLinkBridge.md)

[Remove-ADReplicationSiteLinkBridge](./Remove-ADReplicationSiteLinkBridge.md)

[Set-ADReplicationSiteLinkBridge](./Set-ADReplicationSiteLinkBridge.md)

