---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adreplicationconnection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADReplicationConnection
---

# Get-ADReplicationConnection

## 摘要
根据指定的过滤条件返回一个特定的 Active Directory 复制连接对象，或一组 Active Directory 复制连接对象。

## 语法

### 过滤器（默认设置）
```
Get-ADReplicationConnection [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Filter <String>]
 [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

### 身份
```
Get-ADReplicationConnection [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADReplicationConnection> [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

## 描述
**Get-ADReplicationConnection** cmdlet 根据指定的筛选条件返回一个特定的 Active Directory 复制连接，或一组 Active Directory 复制连接对象。这些连接用于使域控制器之间能够进行数据复制。每个连接定义了一条从某个域控制器（源）到另一个域控制器（目标）的单向数据传输路径。知识一致性检查器（Knowledge Consistency Checker，KCC）会在可能的情况下重用现有的连接；删除未使用的连接；如果不存在满足当前需求的连接，则会创建新的连接。

## 示例

### 示例 1：获取所有复制连接
```
PS C:\> Get-ADReplicationConnection -Filter *
```

这个命令可以获取所有的复制连接信息。

### 示例 2：从指定的域控制器获取所有复制连接
```
PS C:\> Get-ADReplicationConnection -Filter "ReplicateFromDirectoryServer -eq 'corp-DC01'"
```

这个命令会获取所有从 corp-DC01 复制的复制连接信息。

### 示例 3：获取指定的复制连接
```
PS C:\> Get-ADReplicationConnection -Identity "5f98e288-19e0-47a0-9677-57f05ed54f6b"
```

这个命令用于获取复制连接，其对应的GUID为5f98e288-19e0-47a0-9677-57f05ed54f6b。

### 示例 4：获取复制连接的属性
```
PS C:\> Get-ADReplicationConnection -Identity "5f98e288-19e0-47a0-9677-57f05ed54f6b" -Properties *
```

这个命令可以获取GUID为5f98e288-19e0-47a0-9677-57f05ed54f6b的复制连接的所有属性。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Active Directory PowerShell 提供程序驱动器运行的。如果是从这样的提供程序驱动器运行 cmdlet，则默认使用与该驱动器关联的帐户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

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
指定一个用于检索 Active Directory 对象的查询字符串。该字符串使用 PowerShell 表达式语言（PowerShell Expression Language）的语法。PowerShell 表达式语言为 *Filter* 参数接收到的值类型提供了强大的类型转换支持。其语法采用“按顺序排列”的方式，即运算符位于操作数和值之间。有关 *Filter* 参数的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter`。

语法：

以下语法使用了巴克斯-诺尔（Backus-Naur）形式来说明如何使用 PowerShell 表达式语言来处理这个参数。

\<filter\>  ::= "{" \<FilterComponentList\> "}"

\<FilterComponentList\> ::= \<FilterComponent\> | \<FilterComponent\> \<JoinOperator\> \<FilterComponent\> | \<NotOperator\> \<FilterComponent\>

<FilterComponent> ::= <attr> <FilterOperator> <value> | ("<FilterComponent>")

<FilterOperator> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

\<JoinOperator\> ::= "-and" | "-or"

<NotOperator> ::= "-not"

<attr> ::= <PropertyName> | <LDAPDisplayName of the attribute>

<value>::= <使用指定的<FilterOperator>将此值与<attr>进行比较>

有关 `<value>` 支持类型的列表，请参阅 `about_ActiveDirectory_ObjectModel`。

注意：PowerShell中的通配符（除了*之外，例如?）不被*Filter*语法所支持。

注意：要使用 LDAP 查询字符串进行查询，请使用 *LDAPFilter* 参数。

```yaml
Type: String
Parameter Sets: Filter
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity
通过提供以下属性值之一来指定一个 Active Directory 对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个表示错误的状态（即程序无法继续执行）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

```yaml
Type: ADReplicationConnection
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

为该参数指定属性，可以使用逗号分隔的名称列表。如果要显示对象上设置的所有属性，请使用 *（星号）。

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

### -Server
默认的身份验证方法是“Negotiate”。

基本身份验证方法需要使用安全套接字层（SSL）连接。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft ActiveDirectory.Management_ADReplicationConnection
连接对象是通过*Identity*参数接收到的。

## 输出

### Microsoft.ActiveDirectory.Management_ADReplicationConnection

## 备注

## 相关链接

[Set-ADReplicationConnection](./Set-ADReplicationConnection.md)
