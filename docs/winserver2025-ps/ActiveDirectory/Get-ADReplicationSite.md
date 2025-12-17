---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adreplicationsite?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADReplicationSite
---

# 获取 AD 复制站点信息

## 摘要
根据指定的过滤器返回一个特定的 Active Directory 复制站点或一组复制站点对象。

## 语法

### 身份信息（默认值）
```
Get-ADReplicationSite [-AuthType <ADAuthType>] [-Credential <PSCredential>] [[-Identity] <ADReplicationSite>]
 [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

### 过滤器
```
Get-ADReplicationSite [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Filter <String>
 [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADReplicationSite` cmdlet 根据指定的筛选条件返回一个特定的 Active Directory 复制站点或一组复制站点对象。在 Active Directory 中，复制站点的作用是：使客户端能够发现位于其计算机物理位置附近的网络资源（已发布的共享资源、域控制器），或者减少通过广域网 (WAN) 链路传输的数据量。此外，复制站点还可以用于优化域控制器之间的数据复制过程。

## 示例

#### 示例 1：获取所有复制站点
```
PS C:\> Get-ADReplicationSite -Filter *
```

这个命令可以获取所有活动目录（Active Directory）复制站点（Replication sites）的信息。

### 示例 2：根据标志获取复制站点
```
PS C:\> Get-ADReplicationSite -Properties * -Filter "WindowsServer2003KCCSiteLinkBridgingEnabled -eq `$TRUE"
```

这个命令会获取所有启用了 `WindowsServer2003KCCBehaviorEnabled` 标志的网站。必须设置 `*Properties*` 参数，因为默认情况下系统不会检索 `**WindowsServer2003KCCSiteLinkBridgingEnabled**` 属性。

### 示例 3：通过名称获取复制站点
```
PS C:\> Get-ADReplicationSite -Identity NorthAmerica
```

这个命令用于获取名为“NorthAmerica”的网站。

### 示例 4：通过名称和属性获取复制站点
```
PS C:\> Get-ADReplicationSite -Identity NorthAmerica -Properties AutomaticInterSiteTopologyGenerationEnabled
```

这个命令用于获取名为“NorthAmerica”的站点的**AutomaticInterSiteTopologyGenerationEnabled**属性值。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

您也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，可以将 `Credential` 参数设置为该 `PSCredential` 对象。

如果执行该任务的账户没有目录级别的权限，Windows PowerShell的Active Directory模块会返回一个终止错误（即程序异常退出）。

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
指定一个用于检索 Active Directory 对象的查询字符串。该字符串使用 PowerShell 表达式语言（PowerShell Expression Language）的语法。PowerShell 表达式语言为 *Filter* 参数接收到的值类型提供了强大的类型转换支持。其语法采用“按顺序排列”的表示方式，即运算符被放在操作数和值之间。有关 *Filter* 参数的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter` 命令。

语法：

以下语法采用了巴克斯-诺尔（Backus-Naur）形式来说明如何使用 PowerShell 表达式语言来处理这个参数。

\<filter\>  ::= "{" \<FilterComponentList\> "}"

\<FilterComponentList\> ::= \<FilterComponent\> | \<FilterComponent\> \<JoinOperator\> \<FilterComponent\> | \<NotOperator\> \<FilterComponent\>

<FilterComponent> ::= <attr> <FilterOperator> <value> | ("<FilterComponent>)"

\<FilterOperator\> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

<JoinOperator> ::= "-and" | "-or"

\<NotOperator\> ::= "-not"

\<attr\> ::= \<PropertyName\> | \<LDAPAttributeName\>

<value>::= <使用指定的<FilterOperator>将此值与<attr>进行比较>

要查看 `<value>` 支持的数据类型列表，请输入 `Get-Help about_ActiveDirectory_ObjectModel`。

注意：PowerShell 中的通配符（除了 * 之外，例如 ?）不支持 *Filter* 语法。

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

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个非终止性的错误（即无法继续执行后续操作的错误）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

```yaml
Type: ADReplicationSite
Parameter Sets: Identity
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Properties
指定从服务器检索的输出对象的属性。使用此参数可以获取默认集合中未包含的属性。

为该参数指定属性，可以使用逗号分隔的名称列表。如果要显示对象上设置的所有属性，请使用星号（*）。

要指定某个特定的扩展属性，请使用该属性的名称。对于非默认属性或扩展属性，必须指定该属性的 LDAP 显示名称。

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
指定要连接的 Active Directory 域服务实例，为此需要提供相应的域名或目录服务器的值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot instance）。

域名值：

- Fully qualified domain name (FQDN)
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

*Server* 参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

没有相关设置，或者使用了 `Microsoft ActiveDirectory.Management.ADReplicationSite` 类。
一个站点对象是通过*Identity*参数接收到的。

## 输出

### Microsoft.ActiveDirectory.Management_ADReplicationSite

## 备注

## 相关链接

[New-ADReplicationSite](./New-ADReplicationSite.md)

[Remove-ADReplicationSite](./Remove-ADReplicationSite.md)

[Set-ADReplicationSite](./Set-ADReplicationSite.md)

