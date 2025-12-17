---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adclaimtransformpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADClaimTransformPolicy
---

# Get-ADClaimTransformPolicy

## 摘要
根据指定的过滤器返回一个或多个 Active Directory 主张转换对象（Active Directory Claim Transform Objects）。

## 语法

### 过滤器（默认设置）

```
Get-ADClaimTransformPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -Filter <String> [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

### 身份

```
Get-ADClaimTransformPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [[-Identity] <ADClaimTransformPolicy>] [-Properties <String[]>] [-Server <String>]
 [<CommonParameters>]
```

### LdapFilter

```
Get-ADClaimTransformPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -LDAPFilter <String> [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

## 描述

`Get-ADClaimTransformPolicy` cmdlet 根据指定的筛选条件返回一个或多个 Active Directory 权限声明转换对象。

## 示例

### 示例 1：获取所有索赔转换政策的列表

```powershell
Get-ADClaimTransformPolicy -Filter *
```

此命令用于检索所有声明转换策略的列表。

### 示例 2：获取应用于特定信任机制的所有声明转换策略

```powershell
$trust = Get-ADTrust -Identity "corp.contoso.com"
$filter = "IncomingTrust -eq '$trust' -or OutgoingTrust -eq '$trust'"
Get-ADClaimTransformPolicy -Filter $filter
```

这个示例获取了所有应用于使用 `corp.contoso.com` 创建的信托的所有声明转换策略。

### 示例 3：使用指定的政策名称获取理赔处理策略

```powershell
Get-ADClaimTransformPolicy -Identity DenyAllPolicy
```

这个命令用于获取名为`DenyAllPolicy`的声明转换策略。

### 示例 4：使用基于 LDAP 的查询过滤器获取索赔信息

```powershell
Get-ADClaimTransformPolicy -LDAPFilter "(name=DenyAll*)"
```

该命令使用基于LDAP的查询过滤器来获取有关任何声明转换策略的信息。该过滤器会查找那些策略名称以“DenyAll”开头的记录。

## 参数

### -AuthType

指定要使用的认证方法。此参数的可接受值包括：

- `Negotiate` or `0`
- `Basic` or `1`

默认的身份验证方法是“Negotiate”。

对于“基本”（Basic）身份验证方法来说，需要建立安全套接字层（SSL）连接。

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

要指定这个参数，你可以输入一个用户名，例如 `User1` 或 `Domain01\User01`；或者你可以指定一个 **PSCredential** 对象。如果你为这个参数指定了一个用户名，该 cmdlet 会提示你输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将该 **Credential** 对象设置为相应的参数值。

如果执行该任务的账号没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

Windows PowerShell 中除了 `*` 之外的通配符（例如 `?`）不支持 `Filter` 语法。

有效的过滤操作符包括：

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

通过提供以下属性值之一来指定一个 Active Directory 对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name

该cmdlet会在默认的命名上下文或分区中搜索目标对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止的错误（即程序会无限循环执行，而无法完成任何操作）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADClaimTransformPolicy
Parameter Sets: Identity
Aliases:

Required: False
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

指定从服务器获取的输出对象的属性。使用此参数可以获取默认属性集合中未包含的属性。

请以逗号分隔的形式列出您想要获取的属性名称。如果您想显示对象上设置的所有属性，可以使用通配符“*”。

要指定某个特定的扩展属性，请使用该属性的名称。对于非默认属性或扩展属性来说，您必须指定该属性的 LDAP 显示名称。

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

### -Server

指定要连接的 Active Directory 域服务实例，为此需要提供以下值之一（对应于相应的域名或目录服务器）。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务、Active Directory 域服务或 Active Directory 快照实例。

以下是几种指定 Active Directory 域服务实例的方法：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

该参数的默认值是根据以下方法之一确定的，确定顺序按照列出的顺序进行：

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

### 无值或 Microsoft.ActiveDirectory.Management.ADClaimTransformPolicy

通过**Identity**参数接收到一个声明转换策略对象（claim transform policy object）。

## 输出

### Microsoft ActiveDirectory.Management.AdClaimTransformPolicy

## 备注

## 相关链接

[New-ADClaimTransformPolicy](./New-ADClaimTransformPolicy.md)

[Remove-ADClaimTransformPolicy](./Remove-ADClaimTransformPolicy.md)

[Set-ADClaimTransformPolicy](./Set-ADClaimTransformPolicy.md)

[Windows PowerShell 中的 AD DS 管理命令集](./activedirectory.md)
