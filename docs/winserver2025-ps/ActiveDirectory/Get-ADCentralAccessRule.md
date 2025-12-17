---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adcentralaccessrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADCentralAccessRule
---

# 获取 ADCentral 访问规则

## 摘要
从 Active Directory 中检索中央访问规则。

## 语法

### 过滤器（默认设置）

```
Get-ADCentralAccessRule [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -Filter <String> [-Properties <String[]>] [-ResultPageSize <Int32>]
 [-ResultSetSize <Int32>] [-Server <String>] [<CommonParameters>]
```

### 身份证明

```
Get-ADCentralAccessRule [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADCentralAccessRule> [-Properties <String[]>] [-Server <String>]
 [<CommonParameters>]
```

### LdapFilter

```
Get-ADCentralAccessRule [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -LDAPFilter <String> [-Properties <String[]>] [-ResultPageSize <Int32>]
 [-ResultSetSize <Int32>] [-Server <String>] [<CommonParameters>]
```

## 描述

`Get-ADCentralAccessRule` cmdlet 用于从 Active Directory 中检索中央访问规则（central access rules）。

## 示例

### 示例 1：获取所有中央访问规则的列表

```powershell
Get-ADCentralAccessRule -Filter *
```

这个命令会检索所有中央访问规则的列表。

### 示例 2：获取具有特定资源条件的中心访问规则

```powershell
Get-ADCentralAccessRule -Filter "ResourceCondition -like '*Department*'"
```

此命令用于检索那些在资源条件中包含“Department”（部门）这一信息的中央访问规则。

#### 示例 3：按名称获取特定的中央访问规则

```powershell
Get-ADCentralAccessRule -Identity "Financial Documents Rule"
```

此命令检索一个名为“Finance Documents Rule”的中心访问规则。

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

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01\User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 **Credential** 参数设置为这个 **PSCredential** 对象。

如果执行该任务的代理程序没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

指定一个用于检索 Active Directory 域服务对象的查询字符串。该字符串使用 Windows PowerShell 表达式语言的语法。Windows PowerShell 表达式语言为 **Filter** 参数接收的值类型提供了强大的类型转换支持。

请按照以下格式之一指定 `Filter` 参数：

- To match a single filter element: `{Attribute operator "value"}`
- To match multiple filter elements:
  `{(Attribute1 operator1 "value1") joinOperator (Attribute2 operator2 "value2")}`

Windows PowerShell 中除了 `*` 之外的通配符（例如 `?`）不支持 `Filter` 语法。

有效的过滤器操作符包括：

 `-eq`、`-le`、`-ge`、`-ne`、`-lt`、`-gt`、`-approx`、`-bor`、`-band`、`-recursivematch`、`-like`、`-notlike`

有效的连接运算符包括：

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

通过提供以下属性值之一来指定一个 Active Directory 对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (**objectGUID**)
- A security identifier (**objectSid**)
- A SAM account name (**sAMAccountName**)

这个参数也可以通过管道获取该对象，或者你可以将该参数设置为一个对象实例。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADCentralAccessRule
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

请以逗号分隔的形式列出需要获取的属性名称。若要显示对象上设置的所有属性，请使用通配符“*”。

要指定某个特定的扩展属性，请使用该属性的名称。对于非默认属性或扩展属性，您必须指定该属性的 LDAP 显示名称。

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

指定 Active Directory 域服务查询返回的对象的最大数量。如果您希望获取所有对象，请将此参数设置为 `$null`。您可以使用 Ctrl+C 来停止查询及对象的返回过程。

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

指定要连接的 Active Directory 域服务实例，为此需提供以下值之一（对应于相应的域名或目录服务器）。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务、Active Directory 域服务或 Active Directory 快照实例。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无，或为 `Microsoft.ActiveDirectory.Management.ADCentralAccessPolicyEntry`

`Identity` 参数接收了一个 `ADCentralAccessPolicyEntry` 对象。

## 输出

### Microsoft.ActiveDirectory.Management.ADCentralAccessRule

返回一个或多个 **ADCentralAccessRule** 对象。

此 cmdlet 返回一组默认的 **ADCentralAccessRule** 属性值。若要获取更多的 **ADCentralAccessRule** 属性信息，可以使用该 cmdlet 的 **Properties** 参数。

## 备注

## 相关链接

[New-ADCentralAccessRule](./New-ADCentralAccessRule.md)

[Remove-ADCentralAccessRule](./Remove-ADCentralAccessRule.md)

[Set-ADCentralAccessRule](./Set-ADCentralAccessRule.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)
