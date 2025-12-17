---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adauthenticationpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADAuthenticationPolicy
---

# Get-ADAuthenticationPolicy

## 摘要
获取一个或多个 Active Directory 域服务（AD DS）身份验证策略。

## 语法

### 过滤器（默认值）

```
Get-ADAuthenticationPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -Filter <String> [-Properties <String[]>] [-ResultPageSize <Int32>]
 [-ResultSetSize <Int32>] [-Server <String>] [<CommonParameters>]
```

### 身份（Identity）

```
Get-ADAuthenticationPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADAuthenticationPolicy> [-Properties <String[]>] [-Server <String>]
 [<CommonParameters>]
```

### LdapFilter

```
Get-ADAuthenticationPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -LDAPFilter <String> [-Properties <String[]>] [-ResultPageSize <Int32>]
 [-ResultSetSize <Int32>] [-Server <String>] [<CommonParameters>]
```

## 描述

`Get-ADAuthenticationPolicy` cmdlet 可以获取一个身份验证策略，或者执行搜索以查找多个身份验证策略。

`Identity` 参数用于指定要获取的 Active Directory 域服务（AD DS）身份验证策略。您可以通过该策略的 distinguished name、GUID 或名称来识别它。此外，您还可以使用 `Identity` 参数来指定一个包含身份验证策略对象的变量，或者利用管道运算符将身份验证策略对象直接传递给该参数。

您可以通过指定 **Filter** 参数或 **LDAPFilter** 参数来搜索并使用多种身份验证策略。**Filter** 参数使用 Windows PowerShell 表达式语言为 Active Directory 域服务编写查询字符串。Windows PowerShell 表达式语言语法为 **Filter** 参数接收的值类型提供了丰富的类型转换支持。有关 **Filter** 参数语法的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter`。如果您已有现有的轻量级目录访问协议（LDAP）查询字符串，可以使用 **LDAPFilter** 参数。

## 示例

#### 示例 1：获取身份验证策略

```powershell
Get-ADAuthenticationPolicy -Identity AuthenticationPolicy01
```

此命令通过指定对象名称来获取一个身份验证策略对象。

### 示例 2：使用 LDAP 过滤器获取身份验证策略

```powershell
Get-ADAuthenticationPolicy -LDAPFilter "(name=AuthenticationPolicy*)" -Server Server01
```

此命令会获取所有与 **LDAPFilter** 参数指定的 LDAP 过滤条件相匹配的身份验证策略。

### 示例 3：使用过滤器获取身份验证策略

```powershell
Get-ADAuthenticationPolicy -Filter "Name -like 'AuthenticationPolicy*'" -Server Server02
```

此命令会获取所有与 **Filter** 参数指定的过滤条件相匹配的身份验证策略。

### 示例 4：获取所有符合过滤条件的身份验证策略对象

```powershell
Get-ADAuthenticationPolicy -Filter * | Format-Table Name, Enforce -AutoSize
```

```output
Name                   Enforce
----                   -------
AuthenticationPolicy1   False
AuthenticationPolicy2   False
```

这个命令会获取所有可用的身份验证策略。获取到的输出结果会被传递给 `Format-Table` cmdlet，以便显示每个策略的名称以及该策略中 “Enforce” 字段的值。

### 示例 5：获取认证策略的所有属性

```powershell
Get-ADAuthenticationPolicy -Identity "AuthenticationPolicy01" -Properties "*"
```

此命令会获取由 **Identity** 参数指定的身份验证策略的所有属性。

## 参数

### -AuthType

指定要使用的身份验证方法。此参数的可接受值为：

- `Negotiate` or `0`
- `Basic` or `1`

默认的身份验证方法是“Negotiate”。

对于“基本”（Basic）认证方法而言，需要使用安全套接字层（Secure Sockets Layer，简称SSL）进行连接。

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

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的提供程序驱动器中运行的，则默认凭据将是与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01\User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会要求您输入密码。

您也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，可以将这个 **Credential** 对象设置为相应的参数。

如果该执行任务的用户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

指定一个用于检索 Active Directory 域服务对象的查询字符串。该字符串使用 Windows PowerShell 表达式语言的语法。Windows PowerShell 表达式语言为 **Filter** 参数接收的值类型提供了丰富的类型转换支持。

请按照以下格式之一指定 `Filter` 参数：

- To match a single filter element: `{Attribute operator "value"}`
- To match multiple filter elements:
  `{(Attribute1 operator1 "value1") joinOperator (Attribute2 operator2 "value2")}`

Windows PowerShell 中除了 `*` 以外的通配符（例如 `?`）不支持 `Filter` 语法。

有效的过滤操作符包括：

 `-eq`, `-le`, `-ge`, `-ne`, `-lt`, `-gt`, `-approx`, `-bor`, `-band`, `-recursivematch`, `-like`, `-notlike`

有效的连接操作符包括：

`-and`, `-or`

`not` 运算符是 `-not`。

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

指定一个 Active Directory 域服务（Active Directory Domain Services）的身份验证策略对象。请使用以下格式之一来指定该身份验证策略对象：

- A distinguished name
- GUID
- Name

This parameter can also get this object through the pipeline or you can set this parameter to an
object instance.

The cmdlet searches the default naming context or partition to find the object. If the cmdlet finds
two or more objects, the cmdlet returns a non-terminating error.

```yaml
Type: Microsoft.ActiveDirectory.Management.ADAuthenticationPolicy
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -LDAPFilter

Specifies a filter using the LDAP search filter syntax defined in RFC2254 to filter Active Directory
Domain Services objects.

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

请以逗号分隔的形式列出需要获取的属性名称。对于非默认属性或扩展属性，必须指定该属性的 LDAP 显示名称。如果要显示对象上设置的所有属性，可以使用通配符“*”。

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

该参数用于指定Active Directory域服务查询返回的对象的最大数量。如果您想获取所有对象，请将此参数设置为`$null`。您可以使用Ctrl+C来停止查询及对象的返回过程。

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

指定要连接的 Active Directory 域服务实例，方法是为相应的域名或目录服务器提供一个以下值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下是指定 Active Directory 域服务实例的几种方式：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，确定顺序按照列出的顺序进行：

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft.ActiveDirectory.Management.ADAuthenticationPolicy

此cmdlet接受一个身份验证策略对象。

## 输出

### Microsoft ActiveDirectory.Management.AdAuthenticationPolicy

此cmdlet返回一个或多个身份验证策略对象。它同时会返回一组默认的**ADAuthenticationPolicy**属性值。若要获取更多的**ADAuthenticationPolicy**属性信息，请使用**Properties**参数。

## 备注

## 相关链接

[New-ADAuthenticationPolicy](./New-ADAuthenticationPolicy.md)

[Remove-ADAuthenticationPolicy](./Remove-ADAuthenticationPolicy.md)

[Set-ADAuthenticationPolicy](./Set-ADAuthenticationPolicy.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)
