---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adfinegrainedpasswordpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADFineGrainedPasswordPolicy
---

# Get-ADFineGrainedPasswordPolicy

## 摘要
获取一个或多个 Active Directory 细粒度密码策略。

## 语法

### 过滤器（默认值）
```
Get-ADFineGrainedPasswordPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>] -Filter <String>
 [-Properties <String[]>] [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>]
 [-SearchScope <ADSearchScope>] [-Server <String>] [<CommonParameters>]
```

### 身份
```
Get-ADFineGrainedPasswordPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADFineGrainedPasswordPolicy> [-Properties <String[]>] [-Server <String>] [<CommonParameters>]
```

### LdapFilter
```
Get-ADFineGrainedPasswordPolicy [-AuthType <ADAuthType>] [-Credential <PSCredential>] -LDAPFilter <String>
 [-Properties <String[]>] [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>]
 [-SearchScope <ADSearchScope>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADFineGrainedPasswordPolicy` cmdlet 可以获取一个详细的密码策略，或者执行搜索以检索多个详细的密码策略。

`Identity` 参数用于指定要获取的 Active Directory 细粒度密码策略。您可以通过其唯一名称（Distinguished Name）、GUID 或名称来识别某个细粒度密码策略。此外，您还可以将该参数设置为某个细粒度密码策略对象变量（例如 `$<localFineGrainedPasswordPolicyObject>`），或者通过管道操作符将细粒度密码策略对象传递给 `Identity` 参数。

要搜索并获取多个细粒度的密码策略，可以使用 *Filter* 或 *LDAPFilter* 参数。*Filter* 参数使用 Windows PowerShell 表达式语言来为 Active Directory 编写查询字符串。Windows PowerShell 表达式语言语法为 *Filter* 参数接收到的值类型提供了丰富的类型转换支持。有关 *Filter* 参数语法的更多信息，请输入 `Get-Help about_ActiveDirectory_filter`。如果您已经有现有的轻量级目录访问协议 (LDAP) 查询字符串，可以使用 *LDAPFilter* 参数。

此cmdlet用于检索一组默认的细粒度密码策略对象属性。若要检索更多属性，请使用*Properties*参数。有关如何确定**FineGrainedPasswordPolicy**对象的属性的详细信息，请参阅*Properties*参数的描述。

## 示例

### 示例 1：使用名称获取细粒度的策略
```
PS C:\> Get-ADFineGrainedPasswordPolicy -Identity AdminsPSO
Name                        : AdminsPSO
ComplexityEnabled           : True
LockoutThreshold            : 0
ReversibleEncryptionEnabled : True
LockoutDuration             : 00:30:00
LockoutObservationWindow    : 00:30:00
MinPasswordLength           : 10
Precedence                  : 200
ObjectGUID                  : ba1061f0-c947-4018-a399-6ad8897d26e3
ObjectClass                 : msDS-PasswordSettings
PasswordHistoryCount        : 24
MinPasswordAge              : 1.00:00:00
MaxPasswordAge              : 15.00:00:00
AppliesTo                   : {}
DistinguishedName           : CN=AdminsPSO,CN=Password Settings Container,CN=System,DC=USER01,DC=COM
```

这个命令用于获取名为“AdminsPSO”的细粒度密码策略。

### 示例 2：使用唯一名称（Distinguished Name）获取细粒度密码策略的所有属性
```
PS C:\> Get-ADFineGrainedPasswordPolicy -Identity 'CN=DlgtdAdminsPSO,CN=Password Settings Container,CN=System,DC=USER01,DC=COM' -Properties *
msDS-LockoutDuration                     : -18000000000
msDS-PasswordSettingsPrecedence          : 300
ObjectCategory                           : CN=ms-DS-Password-Settings,CN=Schema,CN=Configuration,DC=USER01,DC=COM
DistinguishedName                        : CN=DlgtdAdminsPSO,CN=Password Settings Container,CN=System,DC=USER01,DC=COM
ExpireOn                                 :
msDS-MinimumPasswordAge                  : -864000000000
dSCorePropagationData                    : {12/31/1600 4:00:00 PM}
msDS-LockoutThreshold                    : 0
Description                              : The Delegated Administrators Password Policy
LockoutThreshold                         : 0
instanceType                             : 4
msDS-PasswordComplexityEnabled           : True
MaxPasswordAge                           : 20.00:00:00
whenCreated                              : 8/15/2008 12:47:43 AM
Name                                     : DlgtdAdminsPSO
ObjectClass                              : msDS-PasswordSettings
ReversibleEncryptionEnabled              : True
msDS-PasswordReversibleEncryptionEnabled : True
Dynamic                                  : False
LockoutDuration                          : 00:30:00
msDS-PSOAppliesTo                        : {CN=Kim Abercrombie,OU=Finance,OU=UserAccounts,DC=USER01,DC=COM, CN=Bob Kelly,OU=AsiaPacific,OU=Sales,OU=UserAccounts,DC=USER01,DC=COM}
DisplayName                              : Delegated Administrators PSO
uSNCreated                               : 16395
Modified                                 : 8/20/2008 12:21:15 AM
MinPasswordAge                           : 1.00:00:00
ProtectedFromAccidentalDeletion          : False
Created                                  : 8/15/2008 12:47:43 AM
sDRightsEffective                        : 15
ComplexityEnabled                        : True
PasswordHistoryCount                     : 24
msDS-MaximumPasswordAge                  : -17280000000000
MinPasswordLength                        : 10
Precedence                               : 300
ObjectGUID                               : 75cf8c7a-9c93-4e81-b611-851803372cb2
msDS-MinimumPasswordLength               : 10
Deleted                                  :
Orphaned                                 : False
CN                                       : DlgtdAdminsPSO
LastKnownParent                          :
CanonicalName                            : USER01.COM/System/Password Settings Container/DlgtdAdminsPSO
modifyTimeStamp                          : 8/20/2008 12:21:15 AM
msDS-LockoutObservationWindow            : -18000000000
LockoutObservationWindow                 : 00:30:00
whenChanged                              : 8/20/2008 12:21:15 AM
createTimeStamp                          : 8/15/2008 12:47:43 AM
msDS-PasswordHistoryLength               : 24
nTSecurityDescriptor                     : System.DirectoryServices.ActiveDirectorySecurity
AppliesTo                                : {CN=JeffPrice,OU=Finance,OU=UserAccounts,DC=USER01,DC=COM, CN=GlenJohn,OU=AsiaPacific,OU=Sales,OU=UserAccounts,DC=USER01,DC=COM}
uSNChanged                               : 72719
```

该命令可以获取与以下细粒度密码策略相关的所有属性：  
DistinguishedName：CN=DlgtdAdminsPSO,CN=Password Settings Container,CN=System,DC=USER01,DC=COM

### 示例 3：使用过滤器获取所有细粒度的密码策略对象
```
PS C:\> Get-ADFineGrainedPasswordPolicy -Filter "name -like '*admin*'"
AppliesTo                   : {CN=GlenJohn,CN=Users,DC=USER01,DC=com, CN=JeffPrice,CN=Users,DC=USER01,DC=com, CN=Administrator,CN=Users,DC=USER01,DC=com}
ComplexityEnabled           : True
DistinguishedName           : CN=DlgtdAdminsPSO,CN=Password Settings Container,CN=System,DC=USER01,DC=com
LockoutDuration             : 00:30:00
LockoutObservationWindow    : 00:30:00
LockoutThreshold            : 0
MaxPasswordAge              : 42.00:00:00
MinPasswordAge              : 1.00:00:00
MinPasswordLength           : 7
Name                        : DlgtdAdminsPSO
ObjectClass                 : msDS-PasswordSettings
ObjectGUID                  : b7de4e6e-c291-4ce6-bb47-6bf8f807df53
PasswordHistoryCount        : 24
Precedence                  : 100
ReversibleEncryptionEnabled : True
```

这个命令会获取所有名称以 “admin” 开头的细粒度密码策略对象。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值包括：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果是从此类驱动器中运行 cmdlet，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

如果执行该任务的代理凭据没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
指定一个用于检索 Active Directory 对象的查询字符串。该字符串使用 PowerShell 表达式语言（PowerShell Expression Language）的语法。PowerShell 表达式语言为 *Filter* 参数接收的值类型提供了丰富的类型转换支持。其语法采用“按顺序排列”的表示方式，即运算符位于操作数和值之间。有关 *Filter* 参数的更多信息，请输入 `Get-Help about_ActiveDirectory_filter` 命令查看帮助文档。

语法：

以下语法使用了巴克斯-诺尔（Backus-Naur）形式来说明如何使用 PowerShell 表达式语言来处理这个参数。

<filter> ::= "{" <FilterComponentList> "}"

\<FilterComponentList\> ::= \<FilterComponent\> | \<FilterComponent\> \<JoinOperator\> \<FilterComponent\> | \<NotOperator\> \<FilterComponent\>

\<FilterComponent\> ::= \<attr\> \<FilterOperator\> \<value\> | ("(<FilterComponent\>)")

\<FilterOperator\> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" | "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" | "-notlike"

\<JoinOperator\> ::= "-and" | "-or"

\<NotOperator\> ::= "-not"

\<attr\> ::= \<PropertyName\> | \<attribute的LDAP显示名称\>

\<value\>::= 使用指定的\<FilterOperator\>，将此值与\<attr\>进行比较

要查看 `<value>` 支持的数据类型列表，请输入 `Get-Help about_ActiveDirectory_ObjectModel`。

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
通过提供以下属性值之一来指定一个 Active Directory 细粒化的密码策略对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)

该 cmdlet 会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个非终止性的错误（即无法继续执行的错误）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个细粒度的密码策略对象实例。

```yaml
Type: ADFineGrainedPasswordPolicy
Parameter Sets: Identity
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -LDAPFilter
指定一个用于过滤 Active Directory 对象的 LDAP 查询字符串。您可以使用此参数来运行现有的 LDAP 查询。`Filter` 参数的语法支持与 LDAP 语法相同的功能。有关更多信息，请参阅 `Filter` 参数的描述，或输入 `Get-Help about_ActiveDirectory_filter` 命令。

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

### -Properties
指定从服务器检索的输出对象的属性。使用此参数可以获取默认集合中未包含的属性。

请以逗号分隔的名称列表形式为该参数指定属性。如果要显示对象上设置的所有属性，请使用 *（星号）。

要指定某个特定的扩展属性，请使用该属性的名称。对于非默认属性或扩展属性，必须指定该属性的 LDAP 显示名称。

要检索对象的属性并显示它们，你可以使用与该对象关联的 `Get-*` cmdlet，并将输出结果传递给 `Get-Member` cmdlet。

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
该参数用于指定在 Active Directory 域服务查询中返回的对象的最大数量。如果您希望接收所有对象，请将此参数设置为 $Null（空值）。您可以使用 Ctrl+C 来停止查询和对象的返回过程。

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

当您从 Active Directory 提供程序驱动器运行一个 cmdlet 时，该参数的默认值是该驱动器的当前路径。

当你在非 Active Directory 提供程序驱动器的情况下运行一个 cmdlet，并且该 cmdlet 需要操作 Active Directory 域服务目标时，此参数的默认值就是目标域的默认命名上下文。

当你在非 Active Directory 提供程序驱动器环境下，针对 Active Directory 轻量级目录服务（AD LDS）目标运行 cmdlet 时，默认值是该目标 ADSLS 实例的默认命名上下文（前提是已通过设置 Active Directory 目录服务代理（DSA）对象（**nTDSDSA**）的 **msDS-defaultNamingContext** 属性来指定该默认命名上下文）。如果未为目标 AD LDS 实例指定任何默认命名上下文，则此参数没有默认值。

当 *SearchBase* 参数的值被设置为空字符串，并且您连接到的是全局目录端口时，将会搜索所有分区。如果 *SearchBase* 参数的值被设置为空字符串，但您并没有连接到全局目录端口，那么系统会抛出错误。

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
用于指定 Active Directory 搜索的范围。该参数的可接受值为：

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
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下是指定 Active Directory 域服务实例的几种方式之一：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

- By using the *Server* value from objects passed through the pipeline
- By using the server information associated with the Active Directory Domain Services Windows PowerShell provider drive, when the cmdlet runs in that drive
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无，或使用 `Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy`
细粒度的密码策略通过*Identity*参数传递。

## 输出

### Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy
此cmdlet返回一个或多个详细的密码策略对象。

此 cmdlet 返回一组默认的 **ADFineGrainedPasswordPolicy** 属性值。若要检索更多的 **ADFineGrainedPasswordPolicy** 属性，可以使用 *Properties* 参数。

要查看 **ADFineGrainedPasswordPolicy** 对象的属性，请参考以下示例。运行这些示例时，将 `<fine grained password policy>` 替换为具体的细粒度密码策略标识符（例如您本地使用的细粒度密码策略的名称）。

要获取 `ADFineGrainedPasswordPolicy` 对象的默认属性列表，请使用以下命令：

`Get-ADFineGrainedPasswordPolicy` \<细粒度密码策略\> | `Get-Member`

要获取一个 **ADFineGrainedPasswordPolicy** 对象的所有属性列表，请使用以下命令：

```
Get-ADFineGrainedPasswordPolicy <细粒度密码策略> -Properties * | Get-Member
```

## 备注
* This cmdlet does not work with AD LDS.
* This cmdlet does not work when targeting a snapshot using the *Server* parameter.

## 相关链接

[Add-ADFineGrainedPasswordPolicySubject](./Add-ADFineGrainedPasswordPolicySubject.md)

[New-ADFineGrainedPasswordPolicy](./New-ADFineGrainedPasswordPolicy.md)

[Remove-ADFineGrainedPasswordPolicy](./Remove-ADFineGrainedPasswordPolicy.md)

[Remove-ADFineGrainedPasswordPolicySubject](./Remove-ADFineGrainedPasswordPolicySubject.md)

[Set-ADFineGrainedPasswordPolicy](./Set-ADFineGrainedPasswordPolicy.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

