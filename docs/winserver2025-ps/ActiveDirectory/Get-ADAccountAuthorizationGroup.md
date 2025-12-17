---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adaccountauthorizationgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADAccountAuthorizationGroup
---

# Get-ADAccountAuthorizationGroup

## 摘要
获取账户令牌组信息。

## 语法

```
Get-ADAccountAuthorizationGroup [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADAccount> [-Partition <String>] [-Server <String>] [<CommonParameters>]
```

## 描述

`Get-ADAccountAuthorizationGroup` cmdlet 从指定的用户、计算机或服务账户令牌中获取安全组信息。该 cmdlet 需要全局目录来执行组搜索。如果包含该账户的 Active Directory 林中没有全局目录，该 cmdlet 将返回一个无法终止的错误。

**Identity** 参数用于指定用户、计算机或服务账户。您可以通过该对象的唯一名称（distinguished name）、GUID、安全标识符（Security Identifier, SID）、安全账户管理器（Security Account Manager, SAM）账户名或用户主体名称来识别相应的用户、计算机或服务账户对象。您还可以将 **Identity** 参数设置为某个账户对象变量（例如 `$<localAccountObject>`），或者通过管道将该账户对象传递给 **Identity** 参数。例如，您可以使用 `Get-ADUser`、`Get-ADComputer`、`Get-ADServiceAccount` 或 `Search-ADAccount` cmdlet 来检索一个账户对象，然后再将该对象通过管道传递给 `Get-ADAccountAuthorizationGroup` cmdlet。

## 示例

### 示例 1：获取指定账户的所有安全组

```powershell
Get-ADAccountAuthorizationGroup -Identity DavidCh
```

```output
GroupScope        : DomainLocal
objectGUID        : 00000000-0000-0000-0000-000000000000
GroupCategory     : Security
SamAccountName    : Everyone
name              : Everyone
objectClass       : SID               : S-1-1-0
distinguishedName : GroupScope        : DomainLocal
objectGUID        : 00000000-0000-0000-0000-000000000000
GroupCategory     : Security
SamAccountName    : Authenticated Users
name              : Authenticated Users
objectClass       : SID               : S-1-5-11
distinguishedName : GroupScope        : Global
objectGUID        : 86c0f0d5-8b4d-4f35-a867-85a006b92902
GroupCategory     : Security
SamAccountName    : Domain Users
name              : Domain Users
objectClass       : group
SID               : S-1-5-21-41432690-3719764436-1984117282-513
distinguishedName : CN=Domain Users,CN=Users,DC=Fabrikam,DC=com

GroupScope        : DomainLocal
objectGUID        : 869fb7ad-8cf2-4dd0-ac0f-4bd3bf324669
GroupCategory     : Security
SamAccountName    : Pre-Windows 2000 Compatible Access
name              : Pre-Windows 2000 Compatible Access
objectClass       : group
SID               : S-1-5-32-554
distinguishedName : CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=Fabrikam,DC=com

GroupScope        : DomainLocal
objectGUID        : c1e397c5-1e44-4270-94d1-88d6c4b78ee6
GroupCategory     : Security
SamAccountName    : Users
name              : Users
objectClass       : group
SID               : S-1-5-32-545
distinguishedName : CN=Users,CN=Builtin,DC=Fabrikam,DC=com
```

该命令会返回指定账户（其用户名为 `DavidCh`）的所有安全组信息。

### 示例 2：使用规范名称获取指定账户的所有安全组

```powershell
Get-ADAccountAuthorizationGroup -Identity "CN=DavidCh,DC=AppNC" -Server "<Server>:50000"
```

```output
distinguishedName : CN=AdminGroup,DC=AppNC
GroupCategory     : Security
GroupScope        : Global
name              : AdminGroup
objectClass       : group
objectGUID        : 4d72873f-fe09-4834-9ada-a905636d10df
SamAccountName    : AdminGroup
SID               : S-1-510474493-936115905-4021890855-1253703389-3958791574-3542197427
```

该命令会从 AD LDS 实例 `<Server>:50000` 中返回指定账户的所有安全组，这些安全组的 **DistinguishedName** 为 `CN=DavidCh,DC=AppNC`。

### 示例 3：获取过滤后的安全组列表

```powershell
Get-ADAccountAuthorizationGroup -Server "<Server>:50000" -Identity Administrator |
    Where-Object { $_.objectClass -ne $null } |
    Select-Object name, objectClass
```

```output
name                                                        objectClass
----                                                        -----------
Domain Users                                                group
Administrators                                              group
Users                                                       group
Pre-Windows 2000 Compatible Access                          group
Group Policy Creator Owners                                 group
Domain Admins                                               group
Enterprise Admins                                           group
Schema Admins                                               group
Denied RODC Password Replication Group                      group
```

该命令返回一个过滤后的内置安全组列表，这些安全组的 **objectClass** 设置不为空或为 null（例如 **Everyone** 或 **Authenticated Users**）。

> [!注意] > 当将此cmdlet的输出作为输入传递给其他Active Directory cmdlet时，这种对输出中的组进行过滤的方法会非常有用。

## 参数

### -AuthType

指定要使用的认证方法。该参数的可接受值包括：

- `Negotiate` or `0`
- `Basic` or `1`

默认的身份验证方法是`Negotiate`。

对于“基本”（Basic）认证方法而言，需要建立安全的套接字层（Secure Sockets Layer，简称SSL）连接。

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

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01\User01`），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

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

### -Identity

通过提供以下属性值之一来指定一个 Active Directory 账户对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (**objectGUID**)
- A Security Identifier (**objectSid**)
- A SAM Account Name (**SAMAccountName**)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止的错误（即程序会无限循环执行）。

这个参数也可以通过管道获取该对象，或者你可以将该参数设置为某个账户对象实例的值。

以下这类派生类型也是被接受的：

- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADUser**

```yaml
Type: Microsoft.ActiveDirectory.Management.ADAccount
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Partition

Specifies the distinguished name of an Active Directory partition. The distinguished name must be
one of the naming contexts on the current directory server. The cmdlet searches this partition to
find the object defined by the **Identity** parameter.

In many cases, a default value is used for the **Partition** parameter if no value is specified. The
rules for determining the default value are given below. Note that rules listed first are evaluated
first and once a default value can be determined, no further rules are evaluated.

In Active Directory Domain Services environments, a default value for **Partition** is set in the
following cases:

- If the **Identity** parameter is set to a distinguished name, the default value of **Partition**
  is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of **Partition** is
  automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of **Partition** is set to the default
  partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for
**Partition** is set in the following cases:

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
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server

Specifies the Active Directory Domain Services instance to connect to, by providing one of the
following values for a corresponding domain name or directory server. The service may be any of the
following: Active Directory Lightweight Domain Services, Active Directory Domain Services or Active
Directory snapshot instance.

Specify the Active Directory Domain Services instance in one of the following ways:

Domain name values:

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

The default value for this parameter is determined by one of the following methods in the order that
they are listed:

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

This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable,
-InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose,
-WarningAction, and -WarningVariable. For more information, see
[about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### Microsoft.ActiveDirectory.Management.ADAccount

An account object that represents the user, computer or service account is received by the
**Identity** parameter. Derived types, such as the following are also accepted:

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**

## 输出

### Microsoft.ActiveDirectory.Management.ADGroup

返回表示该账户所属安全组的信息对象。

## 备注

- This cmdlet doesn't work with an Active Directory snapshot.

## 相关链接

[Get-ADComputer](./Get-ADComputer.md)

[Get-ADServiceAccount](./Get-ADServiceAccount.md)

[Get-ADUser](./Get-ADUser.md)

[Search-ADAccount](./Search-ADAccount.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)
