---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adreplicationsubnet?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADReplicationSubnet
---

# Get-ADReplicationSubnet

## 摘要
获取一个或多个 Active Directory 子网。

## 语法

### 过滤器（默认设置）
```
Get-ADReplicationSubnet [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Filter <String>
 [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

### 身份证明
```
Get-ADReplicationSubnet [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADReplicationSubnet>
 [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

## 描述
**Get-ADReplicationSubnet** cmdlet 可根据指定的过滤器获取某个特定的 Active Directory 子网或一组子网。子网对象（类 subnet）用于在 Active Directory 中定义网络子网。网络子网是指 TCP/IP 网络中的一个部分，该部分被分配了一组逻辑 IP 地址。子网通过某种方式对计算机进行分组，从而标识它们在网络中的物理位置。Active Directory 中的子网对象用于将计算机映射到相应的站点上。

## 示例

### 示例 1：获取所有子网
```
PS C:\> Get-ADReplicationSubnet -Filter *
```

这个命令可以获取所有的子网信息。

### 示例 2：获取指定区域内的子网
```
PS C:\> Get-ADReplicationSubnet -Filter "Location -like '*Japan'"
```

这个命令可以获取日本所有的子网信息。

### 示例 3：获取具有指定名称的子网
```
PS C:\> Get-ADReplicationSubnet -Identity "10.0.0.0/25"
```

这个命令用于获取名称为“10.0.0.0/25”的子网。

### 示例 4：获取指定子网的属性
```
PS C:\> Get-ADReplicationSubnet -Identity "10.0.0.0/25" -Properties *
```

这个命令会获取被标识为 10.0.0.0/25 的子网的所有属性。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值为：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”（协商）。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Active Directory PowerShell提供程序驱动器运行的。如果该cmdlet是从此类提供程序驱动器运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01>User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为该 **PSCredential** 对象。

如果执行任务的代理（agent）没有目录级别的权限，Active Directory PowerShell 会返回一个终止错误（terminating error）。

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
指定一个用于检索 Active Directory 对象的查询字符串。该字符串使用 PowerShell 表达式语言（PowerShell Expression Language）的语法。PowerShell 表达式语言为 *Filter* 参数接收到的值类型提供了丰富的类型转换支持。其语法采用“按顺序排列”的表示方式，即运算符位于操作数和值之间。有关 *Filter* 参数的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter` 命令查看帮助文档。

语法：

以下语法使用了巴克斯-诺尔（Backus-Naur）形式来说明如何使用 PowerShell 表达式语言来处理这个参数。

<filter> ::= "{" <FilterComponentList> "}"

\<FilterComponentList\> ::= \<FilterComponent\> | \<FilterComponent\> \<JoinOperator\> \<FilterComponent\> | \<NotOperator\> \<FilterComponent\>

\<FilterComponent\> ::= \<attr\> \<FilterOperator\> \<value\> | "(" \<FilterComponent\> )"

<FilterOperator> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

\<JoinOperator\> ::= "-and" | "-or"

\<NotOperator\> ::= "-not"

<attr> ::= <PropertyName> | <LDAPDisplayName of the attribute>

<value>::= <使用指定的<FilterOperator>将此值与<attr>进行比较>

有关 `<value>` 所支持类型的列表，请参阅 `about_ActiveDirectory_ObjectModel`。

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
通过提供以下属性值之一来指定一个 Active Directory 对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)

该cmdlet会在默认的命名上下文或分区中搜索目标对象。如果找到两个或多个对象，cmdlet会返回一个非终止性的错误（即无法继续执行的错误）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

```yaml
Type: ADReplicationSubnet
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

为此参数指定属性，可以使用逗号分隔的名称列表。如果要显示对象上设置的所有属性，请使用星号（*）。

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

### -Server
用于指定要连接的 Active Directory 域服务实例，需为相应的域名或目录服务器提供以下值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot instance）。

域名值：

- Fully qualified domain name (FQDN)
- NetBIOS name

Directory server values:

- Fully qualified domain name (FQDN)
- NetBIOS name

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft ActiveDirectory.Management.ADReplicationSubnet
子网对象是通过 *Identity* 参数接收到的。

## 输出

### Microsoft.ActiveDirectory.Management_ADReplicationSubnet

## 备注

## 相关链接

[New-ADReplicationSubnet](./New-ADReplicationSubnet.md)

[Remove-ADReplicationSubnet](./Remove-ADReplicationSubnet.md)

[Set-ADReplicationSubnet](./Set-ADReplicationSubnet.md)

