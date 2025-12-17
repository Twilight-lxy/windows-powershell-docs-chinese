---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adaccountresultantpasswordreplicationpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADAccountResultantPasswordReplicationPolicy
---

# 获取 AD 账户的结果密码复制策略

## 摘要
获取Active Directory账户的密码复制策略结果。

## 语法

```
Get-ADAccountResultantPasswordReplicationPolicy [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-DomainController] <ADDomainController>
 [-Identity] <ADAccount> [-Partition <String>] [-Server <String>] [<CommonParameters>]
```

## 描述

`Get-ADAccountResultantPasswordReplicationPolicy` cmdlet 可以获取指定只读域控制器上用户、计算机或服务账户的密码复制策略信息。

该策略只能是以下值之一：

- `Allow` or `1`
- `DenyExplicit` or `0`
- `DenyImplicit` or `2`
- `Unknown` or `-1`

**Identity** 参数用于指定账户。您可以通过用户的唯一名称（Distinguished Name）、GUID、安全标识符（Security Identifier, SID）或安全账户管理器（Security Account Manager, SAM）账户名称来识别用户、计算机或服务账户对象。您还可以将 **Identity** 参数设置为某个账户对象变量（例如 `$<localAccountObject>`），或者通过管道将该账户对象传递给 **Identity** 参数。例如，可以使用 `Get-ADUser`、`Get-ADComputer`、`Get-ADServiceAccount` 或 `Search-ADAccount` 等 cmdlet 来检索账户对象，然后将该对象通过管道传递给 `Get-ADAccountResultantPasswordReplicationPolicy` cmdlet。

`DomainController` 参数用于指定只读的域控制器。您可以通过其 IPv4 地址、全局 IPv6 地址或 DNS 主机名来识别域控制器；也可以通过 NT 目录服务 (NTDS) 设置对象或服务器对象的唯一名称、该设置对象/服务器对象在配置分区下的 GUID，以及代表该域控制器的计算机对象的唯一名称、`SamAccountName`、GUID 和 SID 来进行识别。此外，您还可以将 `DomainController` 参数设置为某个域控制器对象变量（例如 `$<localDomainControllerObject>`）。

## 示例

### 示例 1：获取指定用户的密码复制策略

```powershell
 Get-ADAccountResultantPasswordReplicationPolicy -Identity DavidChe -DomainController DC1
```

此命令用于获取由 **DomainController** 参数指定的域上的密码复制策略，以及由 **Identity** 参数指定的用户账户的相关信息。

### 示例 2：使用规范名称获取指定用户的密码复制策略

```powershell
params = @{
    Identity = 'CN=Elisa Daugherty,OU=Europe,OU=Sales,OU=UserAccounts,DC=FABRIKAM,DC=COM'
    DomainController = 'DC1'
}
 Get-ADAccountResultantPasswordReplicationPolicy @params
```

该命令用于获取由 **DomainController** 参数指定的域控制器上的密码复制策略，以及由 **Identity** 参数指定的用户账户的标识名（distinguished name）。

## 参数

### -AuthType

指定要使用的身份验证方法。该参数的可接受值包括：

- `Negotiate` or `0`
- `Basic` or `1`

默认的认证方法是 `Negotiate`（协商）。

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

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果是从这样的驱动器中运行 cmdlet，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01\User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将该 **Credential** 对象设置为相应的参数值。

如果执行任务的代理程序没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

### -DomainController

用于指定一个只读域控制器（RODC）。该cmdlet会返回与该RODC关联的账户的密码复制策略。您可以通过提供以下值之一来识别相应的域控制器：

- GUID (**objectGUID**)
- IPV4Address
- Global IPV6Address
- DNS Host Name (**dNSHostName**)
- Name of the server object
- A distinguished name of the NTDS Settings object
- A distinguished name of the server object that represents the domain controller
- GUID of NTDS settings object under the configuration partition
- GUID of server object under the configuration partition
- A distinguished Name of the computer object that represents the domain controller

> [!NOTE]
> The identifier in parentheses is the Lightweight Directory Access Protocol (LDAP) display name for
> the attribute.

```yaml
Type: Microsoft.ActiveDirectory.Management.ADDomainController
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity

Specifies an Active Directory account object by providing one of the following property values. The
identifier in parentheses is the LDAP display name for the attribute. The acceptable values for this
parameter are:

- A distinguished name
- A GUID (**objectGUID**)
- A security identifier (**objectSid**)
- A SAM account name (**sAMAccountName**)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个非终止性的错误（即不会停止执行的错误）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个账户对象实例。

也接受以下这样的派生类型：

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**

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
  set the `msDS-defaultNamingContext` property of the Active Directory directory service agent
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

An account object is received by the **Identity** parameter.

Derived types, such as the following are also accepted:

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**

## 输出

### Microsoft.ActiveDirectory.Management.ADResultantPasswordReplicationPolicy

此cmdlet返回一个**ADResultantPasswordReplicationPolicy**枚举值，该值表示指定域控制器上某个账户的最终密码复制策略。

## 备注

- This cmdlet doesn't work with AD LDS.
- This cmdlet doesn't work with an Active Directory snapshot.

## 相关链接

[Get-ADComputer](./Get-ADComputer.md)

[Get-ADServiceAccount](./Get-ADServiceAccount.md)

[Get-ADUser](./Get-ADUser.md)

[Search-ADAccount](./Search-ADAccount.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)
