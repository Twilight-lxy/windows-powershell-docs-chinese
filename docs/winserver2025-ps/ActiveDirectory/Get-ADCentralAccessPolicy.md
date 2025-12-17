---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adcentralaccesspolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADCentralAccessPolicy
---

# Get-ADCentralAccessPolicy

## 摘要
从 Active Directory 中检索中央访问策略。

## 语法

### 过滤器（默认设置）

```
Get-ADCentralAccessPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -Filter <String> [-Properties <String[]>] [-ResultPageSize <Int32>]
 [-ResultSetSize <Int32>] [-Server <String>] [<CommonParameters>]
```

### 身份证明

```
Get-ADCentralAccessPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADCentralAccessPolicy> [-Properties <String[]>] [-Server <String>]
 [<CommonParameters>]
```

### LdapFilter

```
Get-ADCentralAccessPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -LDAPFilter <String> [-Properties <String[]>] [-ResultPageSize <Int32>]
 [-ResultSetSize <Int32>] [-Server <String>] [<CommonParameters>]
```

## 描述

`Get-ADCentralAccessPolicy` cmdlet 用于从 Active Directory 中检索中央访问策略。

## 示例

### 示例 1：获取所有中央访问策略的列表

```powershell
Get-ADCentralAccessPolicy -Filter *
```

此命令用于检索所有中央访问策略的列表。

### 示例 2：使用过滤器获取特定的中央访问策略列表

```powershell
Get-ADCentralAccessPolicy -Filter "Members -eq 'Finance Documents Rule'"
```

这个命令用于获取那些以“Finance Documents Rule”为中心访问规则作为其成员的中心访问策略。

### 示例 3：获取特定 Active Directory 对象的中心访问策略的相关信息

```powershell
Get-ADCentralAccessPolicy -Identity "Finance Policy"
```

这个命令用于获取名为“Finance Policy”的中央访问策略的相关信息。

## 参数

### -AuthType

指定要使用的认证方法。该参数的可接受值包括：

- `Negotiate` or `0`
- `Basic` or `1`

默认的认证方法是`Negotiate`。

对于“基本”（Basic）身份验证方法而言，需要建立安全套接字层（Secure Sockets Layer，简称SSL）连接。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADAuthType
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

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01/User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 **Credential** 参数设置为这个 **PSCredential** 对象。

如果执行任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

```yaml
Type: System.Management.Automation.PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Filter

指定一个用于检索 Active Directory 域服务对象的查询字符串。该字符串使用 Windows PowerShell 表达式语言语法。Windows PowerShell 表达式语言语法为 **Filter** 参数接收的值类型提供了强大的类型转换支持。

请以以下格式之一指定 **Filter** 参数：

- To match a single filter element: `{Attribute operator "value"}`
- To match multiple filter elements:
  `{(Attribute1 operator1 "value1") joinOperator (Attribute2 operator2 "value2")}`

在 Windows PowerShell 中，除了 `*` 之外的通配符（例如 `?`）不支持 `Filter` 语法。

有效的过滤操作符包括：

`-eq`, `-le`, `-ge`, `-ne`, `-lt`, `-gt`, `-approx`, `-bor`, `-band`, `-recursivematch`, `-like`, `-notlike`

有效的连接操作符有：

`-and`, `-or`

“not”运算符是“-not”。

有关支持的值类型的列表，请参阅`about_ActiveDirectory_ObjectModel`。有关**Filter**参数的更多信息，请参阅`about_ActiveDirectory_filter`。

```yaml
Type: System.String
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
- A GUID (**objectGUID**)
- A Security Identifier (**objectSid**)
- A SAM account name (**sAMAccountName**)

```yaml
Type: Microsoft.ActiveDirectory.Management.ADCentralAccessPolicy
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -LDAPFilter

使用RFC2254中定义的LDAP搜索过滤器语法来指定一个过滤器，以便过滤Active Directory域服务对象。

```yaml
Type: System.String
Parameter Sets: LdapFilter
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Properties

指定从服务器获取的输出对象的属性。使用此参数可以获取默认集合中未包含的属性。

请以逗号分隔的形式列出需要获取的属性名称。如果要显示对象上设置的所有属性，请使用通配符星号（`*`）。

要指定某个特定的扩展属性，请使用该属性的名称。对于非默认属性或扩展属性而言，必须指定该属性的LDAP显示名称。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases: Property

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResultPageSize

指定在 Active Directory 域服务查询中每页显示的对象数量。默认值为每页显示 256 个对象。

```yaml
Type: System.Int32
Parameter Sets: Filter, LdapFilter
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResultSetSize

该参数用于指定 Active Directory 域服务查询返回的对象的最大数量。如果您希望获取所有对象，请将此参数设置为 `$null`。您可以使用 Ctrl+C 来停止查询及对象的返回过程。

默认值是 `$null`。

```yaml
Type: System.Int32
Parameter Sets: Filter, LdapFilter
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server

指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下列任意一种方式指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的列出的顺序：

- By using the **Server** value from objects passed through the pipeline
- By using the server information associated with the Active Directory Domain Services Windows
  PowerShell provider drive, when the cmdlet runs in that drive
- By using the domain of the computer running Windows PowerShell

```yaml
Type: System.String
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

### 无值或 Microsoft.ActiveDirectory.Management.ADCentralAccessPolicy

`Identity` 参数接收一个 `ADCentralAccessPolicy` 对象。

## 输出

### Microsoft ActiveDirectory.Management.ADCentralAccessPolicy

此cmdlet返回一个或多个**ADCentralAccessPolicy**对象。

该cmdlet返回一组默认的**ADCentralAccessPolicy**属性值。若要检索额外的**ADCentralAccessPolicy**属性，请使用cmdlet的**Properties**参数。

## 备注

## 相关链接

[New-ADCentralAccessPolicy](./New-ADCentralAccessPolicy.md)

[Remove-ADCentralAccessPolicy](./Remove-ADCentralAccessPolicy.md)

[Set-ADCentralAccessPolicy](./Set-ADCentralAccessPolicy.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)
