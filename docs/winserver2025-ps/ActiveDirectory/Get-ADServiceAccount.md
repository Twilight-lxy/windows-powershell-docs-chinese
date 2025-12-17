---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adserviceaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADServiceAccount
---

# Get-ADServiceAccount

## 摘要
获取一个或多个由 Active Directory 管理的服务账户，或者由组管理的服务账户。

## 语法

### 过滤器（默认设置）
```
Get-ADServiceAccount [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Filter <String>
 [-Properties <String[]>] [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>]
 [-SearchScope <ADSearchScope>] [-Server <String>] [<CommonParameters>]
```

### 身份
```
Get-ADServiceAccount [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADServiceAccount>
 [-Partition <String>] [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

### LdapFilter
```
Get-ADServiceAccount [-AuthType <ADAuthType>] [-Credential <PSCredential>] -LDAPFilter <String>
 [-Properties <String[]>] [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>]
 [-SearchScope <ADSearchScope>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADServiceAccount` cmdlet 可以获取一个托管服务账户，或者执行搜索以找到多个托管服务账户。

`Identity` 参数用于指定要获取的 Active Directory 管理服务账户。您可以通过该账户的唯一名称（Distinguished Name）、GUID、安全标识符（Security Identifier，SID）或安全账户管理器（Security Account Manager，SAM）帐户名称来识别该管理服务账户。您还可以将此参数设置为某个管理服务账户对象变量（例如 `$<localServiceAccountObject>`），或者通过管道将该管理服务账户对象传递给 `Identity` 参数。

要搜索并检索多个托管服务账户，请使用 **Filter** 或 **LDAPFilter** 参数。**Filter** 参数使用 PowerShell 表达式语言来为 Active Directory 编写查询字符串。PowerShell 表达式语言语法为 **Filter** 参数接收的值类型提供了丰富的类型转换支持。有关 **Filter** 参数语法的更多信息，可以输入 `Get-Help about_ActiveDirectory_Filter`。如果您已有现有的轻量级目录访问协议 (LDAP) 查询字符串，则可以使用 **LDAPFilter** 参数。

此cmdlet会获取一组默认的托管服务账户对象属性。若要获取更多属性，请使用**Properties**参数。有关如何确定服务账户对象的属性的更多信息，请参阅**Properties**参数的描述。

## 示例

### 示例 1：通过安全管理账户管理器的名称获取托管服务账户
```powershell
PS C:\> Get-ADServiceAccount -Identity service1
```
```output
Enabled           : True
Name              : service1
UserPrincipalName :
SamAccountName    : service1$
ObjectClass       : msDS-ManagedServiceAccount
SID               : S-1-5-21-159507390-2980359153-3438059098-29770
ObjectGUID        : eaa435ee-6ebc-44dd-b4b6-dc1bb5bcd23a
HostComputers     :
DistinguishedName : CN=service1,CN=Managed Service Accounts,DC=contoso,DC=com
```

这个命令会获取一个管理型服务账户，其SAM账户名称为“service1”。

### 示例 2：通过服务账户的 SID 获取其管理账号信息
```powershell
PS C:\> Get-ADServiceAccount -Identity S-1-5-21-159507390-2980359153-3438059098-29770
```
```output
Enabled           : True
Name              : service1
UserPrincipalName :
SamAccountName    : service1$
ObjectClass       : msDS-ManagedServiceAccount
SID               : S-1-5-21-159507390-2980359153-3438059098-29770
ObjectGUID        : eaa435ee-6ebc-44dd-b4b6-dc1bb5bcd23a
HostComputers     :
DistinguishedName : CN=service1,CN=Managed Service Accounts,DC=contoso,DC=com
```

此命令用于获取具有SID `S-1-5-21-159507390-2980359153-3438059098-29770` 的托管服务账户。

### 示例 3：获取经过过滤的管理服务账户列表
```powershell
PS C:\> Get-ADServiceAccount -Filter "HostComputers -eq 'CN=SQL-Server-1, DC=contoso,DC=com'"
```
```output
Enabled           : True
Name              : service1
UserPrincipalName :
SamAccountName    : service1$
ObjectClass       : msDS-ManagedServiceAccount
SID               : S-1-5-21-159507390-2980359153-3438059098-29770
ObjectGUID        : eaa435ee-6ebc-44dd-b4b6-dc1bb5bcd23a
HostComputers     : {CN=SQL-Server-1, DC=contoso,DC=com}
DistinguishedName : CN=service1,CN=Managed Service Accounts,DC=contoso,DC=com
```

此命令用于获取被允许在计算机 `CN=SQL-Server-1,DC=contoso,DC=com` 上使用的托管服务账户。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值为：

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

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01\User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行该任务的账号没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
指定一个用于检索 Active Directory 对象的查询字符串。该字符串使用 PowerShell 表达式语言（PowerShell Expression Language）的语法。PowerShell 表达式语言为 **Filter** 参数接收到的值类型提供了丰富的类型转换支持。其语法采用“按顺序排列”的表示方式，即运算符位于操作数和值之间。有关 **Filter** 参数的更多信息，请输入 `Get-Help about_ActiveDirectory_Filter` 命令。

语法：

以下语法使用了Backus-Naur形式来说明如何使用PowerShell表达式语言来处理这个参数。

<filter> ::= "{" <FilterComponentList> "}"

<FilterComponentList> ::= <FilterComponent> | <FilterComponent><JoinOperator><FilterComponent> | <FilterComponent><NotOperator><FilterComponent>

<FilterComponent> ::= <attr> <FilterOperator> <value> | ("<FilterComponent>")

<FilterOperator> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

<JoinOperator> ::= "-and" | "-or"

\<NotOperator\> ::= "-not"

\<attr\> ::= \<propertyName\> | \<attribute的LDAPDisplayName\>

<value>::= <使用指定的<FilterOperator>将此值与<attr>进行比较>

要查看 `<value>` 支持的数据类型列表，请输入 `Get-Help about_ActiveDirectory_ObjectModel`。

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
通过提供以下属性值之一来指定一个 Active Directory 账户对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

该 cmdlet 会在默认的命名上下文或分区中搜索以找到相应的对象。如果找到了两个或多个对象，该 cmdlet 会返回一个无法终止的错误信息。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

```yaml
Type: ADServiceAccount
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -LDAPFilter
指定一个用于过滤 Active Directory 对象的 LDAP 查询字符串。您可以使用此参数来执行现有的 LDAP 查询。`Filter` 参数的语法支持与 LDAP 语法相同的功能。有关更多信息，请参阅 `Filter` 参数的描述，或输入 `Get-Help about_ActiveDirectory_filter` 命令。

```yaml
Type: String
Parameter Sets: LdapFilter
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Partition
指定一个 Active Directory 分区的独特名称（distinguished name）。该唯一名称必须是当前目录服务器上的命名上下文之一。此 cmdlet 会在此分区中搜索由 **Identity** 参数定义的对象。

在许多情况下，如果未指定 `Partition` 参数的值，系统会使用默认值。确定默认值的规则如下所示。请注意，首先列出的规则会被优先评估；一旦确定了默认值，后续的规则将不再被评估。

在 Active Directory Domain Services (AD DS) 环境中，**Partition** 的默认值会在以下情况下被设置：

- If the **Identity** parameter is set to a distinguished name, the default value of **Partition** is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of **Partition** is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of **Partition** will be set to the default partition or naming context of the target domain.

In AD LDS environments, a default value for Partition will be set in the following cases:

- If the **Identity** parameter is set to a distinguished name, the default value of **Partition** is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of **Partition** is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of **Partition** will be set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent (DSA) object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the **Partition** parameter will not take any default value.

```yaml
Type: String
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Properties
指定从服务器检索的输出对象的属性。使用此参数可以获取默认集合中未包含的属性。

为该参数指定属性，可以使用逗号分隔的名称列表。若要显示对象上设置的所有属性，请使用 *（星号）。

要指定某个特定的扩展属性，请使用该属性的名称。对于非默认属性或扩展属性而言，必须指定该属性的LDAP显示名称。

要检索某个对象的属性并将其显示出来，你可以使用与该对象关联的 `Get-*` cmdlet，并将输出结果传递给 `Get-Member` cmdlet。有关更多信息，请输入 `Get-Help Get-Member`。

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

### -ResultPageSize
指定在Active Directory域服务查询中每页应显示的对象数量。

默认情况下，每页显示256个对象。

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
该参数用于指定 Active Directory 域服务查询返回的最大对象数量。如果您希望接收所有对象，请将此参数设置为 `$Null$`（空值）。您可以使用 Ctrl+C 来停止查询和对象返回过程。

默认值是 `$Null`。

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

### -SearchBase
指定一个用于搜索的 Active Directory 路径。

当你从 Active Directory 提供程序驱动器运行一个cmdlet时，该参数的默认值是该驱动器的当前路径。

当你在非 Active Directory 提供程序驱动器的环境中运行某个 Cmdlet 并将其应用于 AD DS 目标对象时，该参数的默认值就是目标域的默认命名上下文。

当你在非 Active Directory 提供者驱动器的情况下运行 cmdlet 以针对 AD LDS 目标进行操作时，其默认值将是该目标 ADSLS 实例的默认命名上下文（前提是已通过设置 Active Directory 目录服务代理（DSA）对象（**nTDSDSA**）的 **msDS-defaultNamingContext** 属性来指定该默认命名上下文）。如果未为目标 AD LDS 实例指定任何默认命名上下文，则此参数将没有默认值。

当 **SearchBase** 参数的值被设置为空字符串，并且您连接到的是垃圾回收（GC）端口时，所有分区都会被搜索。如果 **SearchBase** 参数的值被设置为空字符串，但您没有连接到 GC 端口，则会抛出错误。

```yaml
Type: String
Parameter Sets: Filter, LdapFilter
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SearchScope
指定 Active Directory 搜索的范围。该参数的可接受值包括：

- Base or 0
- OneLevel or 1
- Subtree or 2

基础查询（Base query）仅搜索当前路径或对象。一级查询（OneLevel query）搜索该路径或对象的直接子节点。子树查询（Subtree query）则同时搜索当前路径或对象及其所有子节点。

```yaml
Type: ADSearchScope
Parameter Sets: Filter, LdapFilter
Aliases:
Accepted values: Base, OneLevel, Subtree

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot instance）。

域名值：

- Fully qualified domain name (FQDN)
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

**Server** 参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

- By using **Server** value from objects passed through the pipeline.
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
此 cmdlet 支持以下常见参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft.ActiveDirectory.Management.ADServiceAccount
一个托管服务账户对象通过 **Identity** 参数被接收。

## 输出

### Microsoft.ActiveDirectory.Management.ADServiceAccount
返回一个或多个托管服务账户（MSA）对象。

此cmdlet返回一组默认的ADService账户属性值。若要获取更多的ADService账户属性信息，请使用**Properties**参数。

## 备注
* This cmdlet does not work with AD LDS.

## 相关链接

[安装 AD 服务账户](./Install-ADServiceAccount.md)

[New-ADServiceAccount](./New-ADServiceAccount.md)

[Remove-ADServiceAccount](./Remove-ADServiceAccount.md)

[Set-ADServiceAccount](./Set-ADServiceAccount.md)

[卸载AD服务账户](./Uninstall-ADServiceAccount.md)

