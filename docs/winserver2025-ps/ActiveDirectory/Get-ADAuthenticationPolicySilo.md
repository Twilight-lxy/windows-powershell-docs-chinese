---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adauthenticationpolicysilo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADAuthenticationPolicySilo
---

# 获取 AD 认证策略信息

## 摘要
获取一个或多个 Active Directory 域服务（AD DS）身份验证策略孤岛（即各自独立、互不关联的身份验证策略集合）。

## 语法

### 过滤器（默认值）

```
Get-ADAuthenticationPolicySilo [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -Filter <String> [-Properties <String[]>] [-ResultPageSize <Int32>]
 [-ResultSetSize <Int32>] [-Server <String>] [<CommonParameters>]
```

### 身份

```
Get-ADAuthenticationPolicySilo [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADAuthenticationPolicySilo> [-Properties <String[]>] [-Server <String>]
 [<CommonParameters>]
```

### LdapFilter

```
Get-ADAuthenticationPolicySilo [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -LDAPFilter <String> [-Properties <String[]>] [-ResultPageSize <Int32>]
 [-ResultSetSize <Int32>] [-Server <String>] [<CommonParameters>]
```

## 描述

`Get-ADAuthenticationPolicySilo` cmdlet 可以获取一个身份验证策略集合（即“authentication policy silo”），或者执行搜索以查找多个这样的身份验证策略集合。

`Identity` 参数用于指定要获取的 Active Directory 域服务（AD DS）身份验证策略信息。您可以通过该策略的唯一名称（DN，即 Distinguished Name）、GUID 或名称来识别它。此外，您还可以使用 `Identity` 参数来指定一个包含身份验证策略信息的变量，或者通过管道操作符将相应的对象直接传递给该参数。

你可以通过指定 **Filter** 参数或 **LDAPFilter** 参数来搜索并使用多种身份验证策略。**Filter** 参数使用 Windows PowerShell 表达式语言来为 Active Directory 域服务编写查询字符串。Windows PowerShell 表达式语言语法为 **Filter** 参数接收的值类型提供了丰富的类型转换支持。有关 **Filter** 参数语法的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter`。如果你已经有现有的轻量级目录访问协议（LDAP）查询字符串，那么可以使用 **LDAPFilter** 参数。

## 示例

### 示例 1：获取身份验证策略对象

```powershell
Get-ADAuthenticationPolicySilo -Identity AuthenticationPolicySilo01
```

这个命令获取一个名为 AuthenticationPolicySilo01 的身份验证策略对象。

### 示例 2：获取所有符合过滤条件的身份验证策略对象

```powershell
Get-ADAuthenticationPolicySilo -Filter 'Name -like "*AuthenticationPolicySilo*"' |
    Format-Table Name, Enforce -AutoSize
```

```output
Name  Enforce
----  -------
silo     True
silos   False
```

该命令会获取所有与 **Filter** 参数指定的筛选条件相匹配的认证策略。获取到的结果随后会被传递给 `Format-Table` cmdlet，以便显示每个策略的名称以及“Enforce”设置的值。

### 示例 3：获取特定身份认证策略的所有属性

```powershell
Get-ADAuthenticationPolicySilo -Identity AuthenticationPolicySilo02 -Properties *
```

这个命令可以获取名为`AuthenticationPolicySilo02`的身份验证策略（authentication policy）的所有属性信息。

## 参数

### -AuthType

指定要使用的认证方法。该参数的可接受值包括：

- `Negotiate` or `0`
- `Basic` or `1`

默认的身份验证方法是“Negotiate”。

对于“基本”（Basic）认证方法来说，需要使用安全套接字层（SSL）连接。

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

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从此类驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01\User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

您也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，可以将该 **Credential** 参数设置为这个 **PSCredential** 对象。

如果该执行任务的账户没有目录级别的权限，那么用于 Windows PowerShell 的 Active Directory 模块会返回一个终止错误（即程序会立即退出）。

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

指定一个用于检索 Active Directory 域服务对象的查询字符串。该字符串使用 Windows PowerShell 表达式语言语法。Windows PowerShell 表达式语言语法为 **Filter** 参数接收到的值类型提供了强大的类型转换支持。

请以以下格式之一指定 **Filter** 参数：

- To match a single filter element: `{Attribute operator "value"}`
- To match multiple filter elements:
  `{(Attribute1 operator1 "value1") joinOperator (Attribute2 operator2 "value2")}`

Windows PowerShell 中除了 `*` 之外的通配符（例如 `?`）不支持 `Filter` 语法。

有效的过滤器操作符包括：

 `-eq`、`-le`、`-ge`、`-ne`、`-lt`、`-gt`、`-approx`、`-bor`、`-band`、`-recursivematch`、`-like`、`-notlike`

有效的连接操作符有：

`-and`、`-or`

“not”运算符是 `-not`。

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

指定一个 Active Directory 域服务身份验证策略对象。请使用以下格式之一来指定该身份验证策略对象：

- A distinguished name
- A GUID
- A Name

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

此cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止执行的错误（即程序会持续运行而不会停止）。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADAuthenticationPolicySilo
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -LDAPFilter

使用 RFC2254 中定义的 LDAP 搜索过滤器语法来指定一个过滤器，以便过滤 Active Directory 域服务对象。

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

请以逗号分隔的名称列表形式指定要获取的属性。对于非默认属性或扩展属性，必须指定该属性的LDAP显示名称。如果要显示对象上设置的所有属性，请使用通配符（`*`）。

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

该参数用于指定在 Active Directory 域服务查询中返回的对象的最大数量。如果您希望获取所有对象，请将此参数设置为 `$null`。您可以使用 Ctrl+C 来停止查询及对象的返回过程。

默认值为 `$null`。

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

用于指定要连接的 Active Directory 域服务实例，可通过提供相应的域名或目录服务器之一的值来实现连接。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下是指定 Active Directory 域服务实例的几种方法：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法之一确定的，确定顺序按列出的顺序进行：

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft.ActiveDirectory.Management.ADAuthenticationPolicySilo

此cmdlet接受一个身份验证策略对象（authentication policy object）。

## 输出

### Microsoft.ActiveDirectory.Management.ADAuthenticationPolicySilo

返回一个或多个身份验证策略对象。此cmdlet会返回一组默认的**ADAuthenticationPolicySilo**属性值。若要获取额外的**ADAuthenticationPolicySilo**属性，请使用**Properties**参数。

## 备注

## 相关链接

[New-ADAuthenticationPolicySilo](./New-ADAuthenticationPolicySilo.md)

[Remove-ADAuthenticationPolicySilo](./Remove-ADAuthenticationPolicySilo.md)

[Set-ADAuthenticationPolicySilo](./Set-ADAuthenticationPolicySilo.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)
