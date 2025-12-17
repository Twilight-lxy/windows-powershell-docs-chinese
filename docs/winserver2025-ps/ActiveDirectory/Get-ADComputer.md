---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adcomputer?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADComputer
---

# Get-ADComputer

## 摘要

获取一台或多台 Active Directory 电脑。

## 语法

### 过滤器（默认设置）

```powershell
Get-ADComputer [-AuthType <ADAuthType>] [-Credential <PSCredential>]
  -Filter  <String> [-Properties <String[]>] [-ResultPageSize <Int32>]
  [-ResultSetSize <Int32>] [-SearchBase <String>] [-SearchScope <ADSearchScope>]
  [-Server <String>] [<CommonParameters>]
```

### 身份

```powershell
Get-ADComputer [-AuthType <ADAuthType>] [-Credential <PSCredential>]
  [-Identity] <ADComputer> [-Partition <String>] [-Properties <String[]>]
  [-Server <String>] [<CommonParameters>]
```

### LdapFilter

```powershell
Get-ADComputer [-AuthType <ADAuthType>] [-Credential <PSCredential>] -LDAPFilter <String>
  [-Properties <String[]>] [-ResultPageSize <Int32>] [-ResultSetSize <Int32>]
  [-SearchBase <String>] [-SearchScope <ADSearchScope>] [-Server <String>]
  [<CommonParameters>]
```

## 描述

`Get-ADComputer` cmdlet 可以获取一台计算机信息，或者执行搜索以检索多台计算机的信息。

`Identity` 参数用于指定要检索的 Active Directory 计算机。您可以通过计算机的唯一名称（Distinguished Name）、GUID、安全标识符（Security Identifier，SID）或安全账户管理器（Security Accounts Manager，SAM）账户名称来识别该计算机。此外，您还可以将此参数设置为某个计算机对象变量（例如 `$<localComputerobject>`），或者通过管道将该计算机对象传递给 `Identity` 参数。

要搜索并获取多台计算机，可以使用 **Filter** 或 **LDAPFilter** 参数。**Filter** 参数使用 PowerShell 表达式语言来为 Active Directory 编写查询字符串。PowerShell 表达式语言的语法为 **Filter** 参数接收的值类型提供了丰富的类型转换支持。有关 **Filter** 参数语法的更多信息，请输入 `Get-Help [about_ActiveDirectory_filter](/previous-versions/windows/server/hh531527(v=ws.10))`。如果您已有现有的轻量级目录访问协议 (LDAP) 查询字符串，可以使用 **LDAPFilter** 参数。

此cmdlet用于检索计算机对象的一组默认属性。若要检索更多属性，请使用**Properties**参数。有关如何确定计算机对象的属性的详细信息，请参阅**Properties**参数的相关描述。

## 示例

#### 示例 1：获取显示所有属性的特定计算机

```powershell
Get-ADComputer -Identity "User01-SRV1" -Properties *
```

```Output


AccountExpirationDate              :
accountExpires                     : 9223372036854775807
AccountLockoutTime                 :
AccountNotDelegated                : False
AllowReversiblePasswordEncryption  : False
BadLogonCount                      :
CannotChangePassword               : False
CanonicalName                      : fabrikam.com/Computers/User01-srv1
Certificates                       : {}
CN                                 : User01-srv1
codePage                           : 0
countryCode                        : 0
Created                            : 3/16/2009 4:15:00 PM
createTimeStamp                    : 3/16/2009 4:15:00 PM
Deleted                            :
Description                        : DisplayName                        :
DistinguishedName                  : CN= User01-srv1,CN=Computers,DC=fabrikam,DC=com
DNSHostName                        : User01-srv1
DoesNotRequirePreAuth              : False
dSCorePropagationData              : {3/16/2009 4:21:51 PM, 12/31/1600 4:00:01 PM}
Enabled                            : True
HomedirRequired                    : False
HomePage                           :
instanceType                       : 0
IPv4Address                        :
IPv6Address                        :
isCriticalSystemObject             : False
isDeleted                          :
LastBadPasswordAttempt             :
LastKnownParent                    :
LastLogonDate                      :
localPolicyFlags                   : 0
Location                           : NA/HQ/Building A
LockedOut                          : False
ManagedBy                          : CN=SQL Administrator 01,OU=UserAccounts,OU=Managed,DC=fabrikam,DC=com
MemberOf                           : {}
MNSLogonAccount                    : False
Modified                           : 3/16/2009 4:23:01 PM
modifyTimeStamp                    : 3/16/2009 4:23:01 PM
msDS-User-Account-Control-Computed : 0
Name                               : User01-srv1
nTSecurityDescriptor               : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                     : CN=Computer,CN=Schema,CN=Configuration,DC=fabrikam,DC=com
ObjectClass                        : computer
ObjectGUID                         : 828306a3-8ccd-410e-9537-e6616662c0b0
objectSid                          : S-1-5-21-41432690-3719764436-1984117282-1130
OperatingSystem                    :
OperatingSystemHotfix              :
OperatingSystemServicePack         :
OperatingSystemVersion             :
PasswordExpired                    : False
PasswordLastSet                    :
PasswordNeverExpires               : False
PasswordNotRequired                : False
PrimaryGroup                       : CN=Domain Computers,CN=Users,DC=fabrikam,DC=com
primaryGroupID                     : 515
ProtectedFromAccidentalDeletion    : False
pwdLastSet                         : 0
SamAccountName                     : User01-srv1$
sAMAccountType                     : 805306369
sDRightsEffective                  : 0
ServiceAccount                     : {}
servicePrincipalName               : {MSOLAPSVC.3/User01-SRV1.fabrikam.com:analyze, MSSQLSVC/User01-SRV1.fabrikam.com:1456}
ServicePrincipalNames              : {MSOLAPSVC.3/User01-SRV1.fabrikam.com:analyze, MSSQLSVC/User01-SRV1.fabrikam.com:1456}
SID                                : S-1-5-21-41432690-3719764436-1984117282-1130
SIDHistory                         : {}
TrustedForDelegation               : False
TrustedToAuthForDelegation         : False
UseDESKeyOnly                      : False
userAccountControl                 : 4096
userCertificate                    : {}
UserPrincipalName                  :
uSNChanged                         : 36024
uSNCreated                         : 35966
whenChanged                        : 3/16/2009 4:23:01 PM
whenCreated                        : 3/16/2009 4:15:00 PM
```

这个命令可以获取特定计算机的所有属性信息。

### 示例 2：获取所有名称以特定字符串开头的计算机

```powershell
Get-ADComputer -Filter 'Name -like "User01*"' -Properties IPv4Address |
    Format-Table Name, DNSHostName, IPv4Address -AutoSize
```

```Output
name        dnshostname            ipv4address
----        -----------            -----------
User01-SRV1 User01-SRV1.User01.com 10.194.99.181
User01-SRV2 User01-SRV2.User01.com 10.194.100.3
```

这个命令会获取所有名称以某个特定字符串开头的计算机，并显示这些计算机的名称、DNS主机名以及IPv4地址。

### 示例 3：获取在特定时间范围内更改过密码的所有计算机

```powershell
$Date = [DateTime]::Today.AddDays(-90)
Get-ADComputer -Filter 'PasswordLastSet -ge $Date' -Properties PasswordLastSet |
    Format-Table Name, PasswordLastSet
```

```Output
Name                                                      PasswordLastSet
----                                                      ---------------
USER01-SRV4                                               3/12/2009 6:40:37 PM
USER01-SRV5                                               3/12/2009 7:05:45 PM
```

这个命令可以获取所有在过去的90天内更改了密码的计算机信息。

### 示例 4：使用 LDAPFilter 获取特定位置的计算机账户

```powershell
Get-ADComputer -LDAPFilter "(name=*laptop*)" -SearchBase "CN=Computers,DC= User01,DC=com"
```

```Output
name
----
pattiful-laptop
davidche-laptop
```

这个命令使用 **LDAPFilter** 来获取位于 `CN=Computers,DC/User01,DC=com` 这一位置中的、被标记为笔记本电脑的计算机账户。

### 示例 5：使用过滤器获取所有计算机账户

```powershell
Get-ADComputer -Filter *
```

这个命令可以获取所有的计算机账户信息。

### 示例 6：获取所有名称以 “Computer01” 或 “Computer02” 开头的计算机

```powershell
Get-ADComputer -Filter 'Name -like "Computer01*" -or Name -like "Computer02*"' -Properties IPv4Address |
    Format-Table Name, DNSHostName, IPv4Address -AutoSize
```

```Output
name        dnshostname            ipv4address
----        -----------            -----------
Computer01-SRV1 Computer01-SRV1.Computer01.com 10.194.99.181
Computer02-SRV2 Computer02-SRV2.Computer02.com 10.194.100.3
```

### 示例 7：获取所有名称以某个字符串开头的计算机，并且这些计算机的密码是在 30 天前设置的

```powershell
$Date = [DateTime]::Today.AddDays(-30)
Get-ADComputer -Filter 'Name -like "Computer01*" -and PasswordLastSet -ge $Date' -Properties IPv4Address |
    Format-Table Name, DNSHostName, IPv4Address -AutoSize
```

```Output
name        dnshostname            ipv4address
----        -----------            -----------
Computer01-SRV1 Computer01-SRV1.Computer01.com 10.194.99.181
```

这个命令显示名称、DNS主机名和IPv4地址。

## 参数

### -AuthType

指定要使用的认证方法。该参数的可接受值如下：

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

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果是从此类驱动器运行 cmdlet，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01\User01`），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 **Credential** 参数设置为这个 **PSCredential** 对象。

如果执行任务的代理具有相应的权限（即目录级权限），那么该cmdlet将返回一个终止错误；否则，它将尝试执行任务。

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

用于指定一个查询字符串，以检索 Active Directory 对象。该字符串采用 Windows PowerShell 表达式语言（Windows PowerShell Expression Language）的语法。这种语法为 **Filter** 参数接收的值类型提供了强大的类型转换支持。其表达方式遵循“操作符位于操作数和值之间的顺序”规则。有关 **Filter** 参数的更多信息，请输入 `Get-Help [about_ActiveDirectory_Filter](/previous-versions/windows/server/hh531527(v=ws.10)`。

语法：

以下语法使用了巴克斯-诺尔（Backus-Naur）形式来说明如何使用 Windows PowerShell 表达式语言来处理这个参数。

\<filter\>  ::= "{" \<FilterComponentList\> "}"

\<FilterComponentList\> ::= \<FilterComponent\> | \<FilterComponent\> \<JoinOperator\> \<FilterComponent\> | \<NotOperator\> \<FilterComponent\>

<FilterComponent> ::= <attr> <FilterOperator> <value> | ("<FilterComponent>")

\<FilterOperator\> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

<JoinOperator> ::= "-and" | "-or"

\<NotOperator\> ::= "-not"

\<attr\> ::= \<AttributeName\> | \<LDAPDisplayName of the attribute\>

<value>::= <使用指定的<FilterOperator>将此值与<attr>进行比较>

要查看 `<value>` 支持的数据类型列表，请输入 `Get-Help about_ActiveDirectory_ObjectModel`。

> [!NOTE]
> Wildcards other than `*`, such as `?`, are not supported by the **Filter** syntax.

> [!NOTE]
> To query using LDAP query strings, use the **LDAPFilter** parameter.

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

通过提供以下属性值之一来指定一个 Active Directory 计算机对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (`objectGUID`)
- A security identifier (`objectSid`)
- A Security Accounts Manager account name (`sAMAccountName`)

该 cmdlet 会在默认的命名上下文或分区中搜索相应的对象。如果提供的标识符是一个“区分名称”（distinguished name），则会根据该名称来确定需要搜索的分区。如果找到两个或多个对象，cmdlet 会返回一个表示搜索失败的错误信息。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个计算机对象实例。

```yaml
Type: ADComputer
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -LDAPFilter

指定一个用于过滤 Active Directory 对象的 LDAP 查询字符串。您可以使用此参数来执行现有的 LDAP 查询。`Filter` 参数的语法支持与 LDAP 语法相同的功能。有关更多信息，请参阅 `Filter` 参数的描述，或输入 `Get-Help [about_ActiveDirectory_Filter](/previous-versions/windows/server/hh531527(v=ws.10))` 获取帮助。

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

指定一个 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器上支持的命名上下文之一。此 cmdlet 会在此分区中搜索由 **Identity** 参数所定义的对象。

在许多情况下，如果未指定 `Partition` 参数的值，则会使用默认值。确定默认值的规则如下所示。请注意，首先列出的规则会被优先评估；一旦确定了默认值，后续的规则将不再被评估。

在 Active Directory 域服务环境中，以下情况下会为 **Partition** 设置默认值：

- If the **Identity** parameter is set to a distinguished name, the default value of **Partition**
  is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of **Partition** is
  automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of **Partition** is set to the default
  partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a
default value for **Partition** is set in the following cases:

- If the **Identity** parameter is set to a distinguished name, the default value of **Partition**
  is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of **Partition** is
  automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of **Partition** is
  set to the default naming context. To specify a default naming context for an AD LDS environment,
  set the **msDS-defaultNamingContext** property of the Active Directory directory service agent
  (DSA) object (**nTDSDSA**) for the AD LDS instance.
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

为该参数指定属性，可以使用逗号分隔的名称列表。要显示对象上设置的所有属性，请使用星号（*）。

要指定某个特定的扩展属性，请使用该属性的名称。对于非默认属性或扩展属性，您必须指定该属性在LDAP中的显示名称。

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

### -ResultPageSize

指定在 Active Directory 域服务查询中每页应显示的对象数量。

默认情况下，每页显示 256 个对象。

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

该参数用于指定 Active Directory 域服务查询返回的最大对象数量。如果您希望接收所有对象，请将此参数设置为 $Null（空值）。您可以使用 Ctrl+C 来停止查询和对象返回过程。

默认值是 $Null。

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

指定一个要在其中进行搜索的 Active Directory 路径。

当您从 Active Directory 提供程序驱动器运行一个 cmdlet 时，此参数的默认值是该驱动器的当前路径。

当你在非 Active Directory 提供程序驱动器的情况下运行 cmdlet 并针对 Active Directory 域服务目标进行操作时，该参数的默认值就是目标域的默认命名上下文。

当你在非 Active Directory 提供程序驱动器环境下运行 cmdlet 且目标为 AD LDS 实例时，其默认值将是该 AD LDS 实例的默认命名上下文（前提是已通过设置 Active Directory 目录服务代理对象（**nTDSDSA**）的 **msDS-defaultNamingContext** 属性来指定默认命名上下文）。如果未为目标 AD LDS 实例指定任何默认命名上下文，则此参数将没有默认值。

当 **SearchBase** 参数的值被设置为空字符串，并且您连接到了全局目录端口时，系统会搜索所有分区。如果 **SearchBase** 参数的值被设置为空字符串，但您没有连接到全局目录端口，则会抛出错误。

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

用于指定 Active Directory 搜索的范围。该参数的可接受值包括：

- Base or 0
- OneLevel or 1
- Subtree or 2

基础查询（Base query）仅搜索当前路径或对象。一级查询（OneLevel query）搜索该路径或对象的直接子节点。子树查询（Subtree query）则同时搜索当前路径或对象以及该路径或对象的所有子节点。

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

指定要连接的 Active Directory 域服务实例，为此请提供相应的域名或目录服务器的以下值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体使用哪种方法取决于它们的排列顺序：

- By using the **Server** value from objects passed through the pipeline
- By using the server information associated with the Active Directory Domain
  Services Windows PowerShell provider drive, when the cmdlet runs in that drive
- By using the domain of the computer running Windows PowerShell

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft.ActiveDirectory.Management_ADComputer

计算机对象是通过**Identity**参数接收到的。

## 输出

### Microsoft.ActiveDirectory.Management.ADComputer

返回一个或多个计算机对象。

这个 `Get-ADComputer` cmdlet 会返回一组默认的 **ADComputer** 属性值。若要获取更多的 **ADComputer** 属性信息，请使用该 cmdlet 的 `Properties` 参数。

要查看 **ADComputer** 对象的属性，请参考以下示例。运行这些示例时，请将 `<computer>` 替换为计算机标识符（例如您本地计算机的 SAM 账户名称）。

要获取 ADComputer 对象的默认属性列表，请使用以下命令：

`Get-ADComputer <computer> | Get-Member`

要获取 ADComputer 对象的所有属性列表，请使用以下命令：

`Get-ADComputer <computer> > -Properties ALL | Get-Member`

## 备注

- This cmdlet doesn't work with AD LDS with its default schema. By default the AD LDS schema
  doesn't have a computer class, but if the schema is extended to include it, this cmdlet will work
  with LDS.

## 相关链接

[Add-ADComputerServiceAccount](./Add-ADComputerServiceAccount.md)

[Get-ADComputerServiceAccount](./Get-ADComputerServiceAccount.md)

[New-ADComputer](./New-ADComputer.md)

[Remove-ADComputer](./Remove-ADComputer.md)

[Remove-ADComputerServiceAccount](./Remove-ADComputerServiceAccount.md)

[Set-ADComputer](./Set-ADComputer.md)

[Windows PowerShell中的AD DS管理cmdlet](./activedirectory.md)
