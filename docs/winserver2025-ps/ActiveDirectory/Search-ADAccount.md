---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/search-adaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Search-ADAccount
---

# 搜索 AD 账户

## 摘要
获取 Active Directory 用户账户、计算机账户或服务账户信息。

## 语法

### AccountDisabled
```
Search-ADAccount [-AccountDisabled] [-AuthType <ADAuthType>] [-ComputersOnly] [-Credential <PSCredential>]
 [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>] [-SearchScope <ADSearchScope>]
 [-Server <String>] [-UsersOnly] [<CommonParameters>]
```

### 账户已过期
```
Search-ADAccount [-AccountExpired] [-AuthType <ADAuthType>] [-ComputersOnly] [-Credential <PSCredential>]
 [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>] [-SearchScope <ADSearchScope>]
 [-Server <String>] [-UsersOnly] [<CommonParameters>]
```

### 账户即将过期
```
Search-ADAccount [-AccountExpiring] [-AuthType <ADAuthType>] [-ComputersOnly] [-Credential <PSCredential>]
 [-DateTime <DateTime>] [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>]
 [-SearchScope <ADSearchScope>] [-Server <String>] [-TimeSpan <TimeSpan>] [-UsersOnly] [<CommonParameters>]
```

### AccountInactive
```
Search-ADAccount [-AccountInactive] [-AuthType <ADAuthType>] [-ComputersOnly] [-Credential <PSCredential>]
 [-DateTime <DateTime>] [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>]
 [-SearchScope <ADSearchScope>] [-Server <String>] [-TimeSpan <TimeSpan>] [-UsersOnly] [<CommonParameters>]
```

### 被锁在外面（无法进入）
```
Search-ADAccount [-AuthType <ADAuthType>] [-ComputersOnly] [-Credential <PSCredential>] [-LockedOut]
 [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>] [-SearchScope <ADSearchScope>]
 [-Server <String>] [-UsersOnly] [<CommonParameters>]
```

### 密码已过期
```
Search-ADAccount [-AuthType <ADAuthType>] [-ComputersOnly] [-Credential <PSCredential>] [-PasswordExpired]
 [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>] [-SearchScope <ADSearchScope>]
 [-Server <String>] [-UsersOnly] [<CommonParameters>]
```

### PasswordNeverExpires
```
Search-ADAccount [-AuthType <ADAuthType>] [-ComputersOnly] [-Credential <PSCredential>] [-PasswordNeverExpires]
 [-ResultPageSize <Int32>] [-ResultSetSize <Int32>] [-SearchBase <String>] [-SearchScope <ADSearchScope>]
 [-Server <String>] [-UsersOnly] [<CommonParameters>]
```

## 描述
**Search-ADAccount** cmdlet 可以检索一个或多个符合参数所指定条件的用户账户、计算机账户或服务账户。搜索条件包括账户的状态和密码的状态。例如，你可以通过指定 *AccountExpired* 参数来查找所有已过期的账户；同样地，你也可以通过指定 *PasswordExpired* 参数来查找所有密码已过期的账户。你还可以通过指定 *UsersOnly* 参数将搜索范围限制在用户账户上；而当指定 *ComputersOnly* 参数时，该 cmdlet 仅会检索计算机账户。

某些搜索参数（如 *AccountExpiring* 和 *AccountInactive*）会使用一个默认的时间值，您可以通过指定 *DateTime* 或 *TimeSpan* 参数来更改这个时间值。*DateTime* 参数用于指定一个具体的时间点；而 *TimeSpan* 参数则用于指定从当前时间开始的一个时间范围。例如，要搜索所有在 10 天后到期的账户，只需指定 *AccountExpiring* 和 *TimeSpan* 参数，并将 *TimeSpan* 的值设置为 10.00:00:00；如果要搜索所有在 2012 年 12 月 31 日之前到期的账户，则需要将 *DateTime* 参数设置为 12/31/2012。

## 示例

### 示例 1：获取所有被禁用的用户、计算机和服务账户
```
PS C:\> Search-ADAccount -AccountDisabled | FT Name,ObjectClass -A
Name            ObjectClass
----            -----------
Guest           user
Pattith         user
PattiFul_51399   user
PattyFul-LPTOP   computer
PattyFul-DSKTOP  computer
```

此命令会返回所有被禁用的用户、计算机和服务账户的信息。

### 示例 2：获取所有被禁用的用户
```
PS C:\> Search-ADAccount -AccountDisabled -UsersOnly | FT Name,ObjectClass -A
Name         ObjectClass
----         -----------
Guest         user
PattiFul       user
PattiFul_51399 user
```

这个命令会返回所有被禁用的用户。

### 示例 3：获取所有已过期的用户、计算机和服务账户
```
PS C:\> Search-ADAccount -AccountExpired | FT Name,ObjectClass -A
Name            ObjectClass
----            -----------
Evan Narvaez    user
Patti Fuller    user
David Chew      user
```

此命令会返回所有已过期的用户、计算机和服务账户信息。

### 示例 4：获取所有将在指定时间内过期的用户、计算机和服务账户
```
PS C:\> Search-ADAccount -AccountExpiring -TimeSpan 6.00:00:00 | FT Name,ObjectClass -A
Name           ObjectClass
----           -----------
David Chew     user
Evan Narvaez   user
Patti Fuller   user
```

该命令会返回所有在接下来6天内到期的用户、计算机和服务账户信息。

### 示例 5：获取所有已过期的账户
```
PS C:\> Search-ADAccount -PasswordExpired | FT Name,ObjectClass -A
Name                        ObjectClass
----                        -----------
David Chew                  user
Evan Narvaez                user
Patti Fuller                user
```

此命令会返回所有密码已过期的账户信息。

### 示例 6：获取所有被锁定的账户
```
PS C:\> Search-ADAccount -LockedOut | FT Name,ObjectClass -A
Name           ObjectClass
----           -----------
Patti Fuller       user
```

此命令会返回所有被锁定的账户。

## 参数

### -AccountDisabled
指定搜索被禁用的账户。当 ADAccount 的 **Enabled** 属性被设置为 false 时，该账户即被视为被禁用的账户。

```yaml
Type: SwitchParameter
Parameter Sets: AccountDisabled
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AccountExpired
用于搜索已过期的账户。当账户的 `ADAccount` 结构中的 `AccountExpirationDate` 属性被设置为一个过去的时间点时，该账户就被视为已过期。轻量级目录访问协议（LDAP）中用于表示 `AccountExpirationDate` 属性的显示名称是 `accountExpires`。

```yaml
Type: SwitchParameter
Parameter Sets: AccountExpired
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AccountExpiring
表示此 cmdlet 会搜索在指定时间段内或到指定时间为止即将过期的账户。要指定一个时间段，请使用 *AccountExpiring* 参数与 *TimeSpan* 参数组合；要指定一个具体时间，则使用 *AccountExpiring* 参数与 *DateTime* 参数组合。

```yaml
Type: SwitchParameter
Parameter Sets: AccountExpiring
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AccountInactive
表示此 cmdlet 用于搜索在指定时间范围内或自指定时间以来未登录的账户。要指定时间范围，请使用 *TimeSpan* 参数；要指定具体时间，则使用 *DateTime* 参数。请注意，此属性仅在使用 Windows Server 2003 域功能级别（Domain Functional Level）或更高版本时才有效，因此该参数也仅在该模式下可用。

```yaml
Type: SwitchParameter
Parameter Sets: AccountInactive
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AuthType
指定要使用的认证方法。该参数的可接受值为：

- Negotiate or 0
- Basic or 1

默认的认证方法是“Negotiate”。

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

### -ComputersOnly
表示此cmdlet仅搜索计算机账户。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果该执行任务的账户没有目录级别的权限，那么用于 Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

指定用于执行任务的安全上下文的凭据。如果该安全上下文没有执行任务所需的目录级权限，那么目录会返回错误信息。如果在 Windows PowerShell 提供程序的 Active Directory 模块的上下文中运行，则使用与该模块关联的凭据信息作为默认值；否则，将使用当前登录用户的 security context（安全上下文）。

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

### -DateTime
为 **Search-ADAccount** 参数（如 *AccountExpiring*、*AccountInactive* 和 *PasswordExpired*）指定一个明确的时间值。

除非另有说明，否则时间默认为当地时间。当未指定时间值时，时间默认为当地的午夜时间；如果未指定日期，则日期默认为当前日期。以下示例展示了用于指定 `DateTime` 对象的常用语法。

- "4/17/2006"
- "Monday, April 17, 2006"
- "2:22:45 PM"
- "Monday, April 17, 2006 2:22:45 PM"

这些示例指定了相同的日期和时间（不包含秒数）。

- "4/17/2006 2:22 PM"
- "Monday, April 17, 2006 2:22 PM"
- "2:22 PM"

以下示例展示了如何使用RFC1123标准来指定日期和时间。该示例以格林尼治标准时间（GMT）作为时间的基准来进行定义。

- "Mon, 17 Apr 2006 21:22:48 GMT"

以下示例展示了如何将某个值指定为协调世界时（UTC）。该示例表示的是2006年4月17日星期一下午2点22分48秒（UTC时间）。

- "2006-04-17T14:22:48.0000000"

以下示例展示了如何将 *AccountExpiring* 参数设置为日期时间为 2012 年 6 月 18 日凌晨 2:00:00 的 *DateTime* 类型值。

`-AccountExpiring -DateTime "2012年6月18日 上午2:00"`

```yaml
Type: DateTime
Parameter Sets: AccountExpiring, AccountInactive
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LockedOut
表示此 cmdlet 用于查找被锁定（无法使用）的账户。

```yaml
Type: SwitchParameter
Parameter Sets: LockedOut
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PasswordExpired
表示此cmdlet会搜索密码已过期的账户。

```yaml
Type: SwitchParameter
Parameter Sets: PasswordExpired
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PasswordNeverExpires
表示此cmdlet会搜索那些密码永远不会过期的账户。

```yaml
Type: SwitchParameter
Parameter Sets: PasswordNeverExpires
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResultPageSize
指定在一页中显示的 Active Directory 域服务查询结果的对象数量。

默认情况下，每页显示256个对象。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResultSetSize
该参数用于指定 Active Directory 域服务查询返回的对象的最大数量。如果您希望接收所有对象，请将此参数设置为 $Null（空值）。您可以使用 Ctrl+C 来停止查询及对象的返回过程。默认值为 $Null。

以下示例展示了如何设置该参数，以便您能够接收所有返回的对象：

`- ResultSetSize $Null`

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SearchBase
指定一个用于搜索的 Active Directory 路径。

当你从 Active Directory 提供程序驱动器中运行一个 cmdlet 时，该参数的默认值是该驱动器的当前路径。

当你在非 Active Directory 提供程序驱动器的情况下运行一个 cmdlet，并且该 cmdlet 需要针对 Active Directory 域服务（AD DS）目标进行操作时，此参数的默认值就是目标域的默认命名上下文。

当你在非 Active Directory 提供程序驱动器的情况下，针对 Active Directory Lightweight Directory Services (AD LDS) 目标运行某个 cmdlet 时，默认值就是该目标 AD LDS 实例的默认命名上下文（前提是已通过设置 Active Directory 服务代理对象 **nTDSDSA** 的 **msDS-defaultNamingContext** 属性来指定该默认命名上下文）。如果未为目标 AD LDS 实例指定任何默认命名上下文，则此参数没有默认值。

以下示例展示了如何设置该参数以便在某个组织单位内进行搜索。

`-SearchBase "ou=mfg,dc=noam,dc=corp,dc=contoso,dc=com"`

当 *SearchBase* 参数的值被设置为空字符串，并且您连接到的是全局目录端口时，将会搜索所有分区。如果 *SearchBase* 参数的值被设置为空字符串，但您没有连接到全局目录端口，则会生成一个错误。

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

### -SearchScope
指定 Active Directory 搜索的范围。此参数的可接受值为：

- Base or 0
- OneLevel or 1
- Subtree or 2

基本查询（Base query）仅搜索当前路径或对象。一级查询（OneLevel query）搜索该路径或对象的直接子节点。子树查询（Subtree query）则同时搜索当前路径或对象及其所有子节点。

```yaml
Type: ADSearchScope
Parameter Sets: (All)
Aliases:
Accepted values: Base, OneLevel, Subtree

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器对应的值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法中的一种来确定的，具体采用哪种方法取决于它们的排列顺序：

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

### -TimeSpan
用于指定时间间隔。该参数用于为 **Search-ADAccount** 参数（例如 *AccountExpiring*）指定时间值。请按照以下格式指定时间间隔：

\[-\]D.H:M:S.F

`where:`

- D = Days (0 to 10675199)
- H = Hours (0 to 23)
- M = Minutes (0 to 59)
- S = Seconds (0 to 59)
- F = Fractions of a second (0 to 9999999)

注意：时间值必须在以下范围内：-10675199:02:48:05.4775808 到 10675199:02:48:05.4775807。

以下示例展示了如何设置这个参数。

将时间设置为2天后。

`-TimeSpan "2.00:00:00"`

将时间范围设置为过去的两天

`-TimeSpan "-2.00:00.00"`

将时间设置为4小时。

`-TimeSpan "4:00"`

例如，要搜索所有在10天后到期的账户，请按照以下方式指定*AccountExpiring*和*TimeSpan*参数。

`-AccountExpiring -TimeSpan "10.00:00.00"`

```yaml
Type: TimeSpan
Parameter Sets: AccountExpiring, AccountInactive
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UsersOnly
表示此 cmdlet 仅搜索用户账户。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft ActiveDirectory.Management.ADAccount
此cmdlet返回一个或多个符合参数所设定条件的账户对象。

## 备注

## 相关链接

[Clear-ADAccountExpiration](./Clear-ADAccountExpiration.md)

[禁用 AD 账户](./Disable-ADAccount.md)

[Enable-ADAccount](./Enable-ADAccount.md)

[Get-ADAccountResultantPasswordReplicationPolicy](./Get-ADAccountResultantPasswordReplicationPolicy.md)

[Set-ADAccountControl](./Set-ADAccountControl.md)

[Set-ADAccountExpiration](./Set-ADAccountExpiration.md)

[Set-ADAccountPassword](./Set-ADAccountPassword.md)

[解锁 AD 账户](./Unlock-ADAccount.md)

