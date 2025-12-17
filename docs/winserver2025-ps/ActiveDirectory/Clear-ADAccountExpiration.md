---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/clear-adaccountexpiration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-ADAccountExpiration
---

# 清除 AD 账户过期状态

## 摘要
清除 Active Directory 账户的过期日期。

## 语法

```
Clear-ADAccountExpiration [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Identity] <ADAccount> [-Partition <String>] [-PassThru]
 [-Server <String>] [<CommonParameters>]
```

## 描述

`Clear-ADAccountExpiration` cmdlet 可以清除 Active Directory 用户或计算机账户的过期日期。当您清除某个账户的过期日期后，该账户将不会失效（即不会被自动删除）。

`Identity` 参数用于指定要修改的用户或计算机账户。您可以通过用户的唯一名称（Distinguished Name）、GUID、安全标识符（Security Identifier，SID）或安全帐户管理器（Security Accounts Manager，SAM）账户名来识别该用户或组。您还可以将 `Identity` 参数设置为某个用户或计算机对象变量（例如 `$<localUserObject>`），或者通过管道将该用户或计算机对象传递给 `Identity` 参数。例如，您可以使用 `Get-ADUser`、`Get-ADComputer` 或 `Search-ADAccount` cmdlet 来检索一个对象，然后再将该对象通过管道传递给 `Clear-ADAccountExpiration` cmdlet。

对于 Active Directory 轻量级目录服务（AD LDS）环境，除非满足以下两种情况，否则必须指定 **Partition** 参数：

- The cmdlet is run from an Active Directory provider drive.
- A default naming context or partition is defined for the AD LDS environment.

要为 AD LDS 环境指定一个默认的命名上下文，请设置该 AD LDS 实例对应的 Active Directory 目录服务代理对象（**nTDSDSA**）的 **msDS-defaultNamingContext** 属性。

## 示例

### 示例 1：为指定的用户清除账户过期日期

```powershell
Clear-ADAccountExpiration -Identity PattiFuller
```

该命令会清除用户名为`PattiFuller`的用户账户的过期日期设置。

### 示例 2：使用特殊名称清除账户的有效期

```powershell
Clear-ADAccountExpiration -Identity 'CN=PattiFuller,DC=AppNC' -Server 'PATTIFU-SVR1:60000'
```

此命令会清除AD LDS实例`PATTIFU-SVR1:60000`上名为`CN=PattiFuller,DC=AppNC`的用户账户的过期日期。

## 参数

### -AuthType

指定要使用的认证方法。该参数的可接受值为：

- `Negotiate` or `0`
- `Basic` or `1`

默认的身份验证方法是“Negotiate”。

对于“基本”认证方法来说，需要使用安全套接字层（SSL）连接。

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

### -Confirm

在运行cmdlet之前，会提示您进行确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认使用与该驱动器关联的帐户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01/User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 **Credential** 参数设置为这个 **PSCredential** 对象。

如果该执行任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
- A security identifier (**objectSid**)
- A SAM account name (**sAMAccountName**)

该cmdlet会在默认的命名上下文或分区中搜索以找到相应的对象。如果找到了两个或多个对象，该cmdlet会返回一个“非终止性错误”（即无法继续执行的错误）。

这个参数也可以通过数据管道（pipeline）来获取相关对象，或者你可以将这个参数设置为一个账户对象（account object）的实例。

也接受以下这样的派生类型：

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

### -PassThru

Returns an object representing the item with which you're working. By default, this cmdlet doesn't
generate any output.

```yaml
Type: System.Management.Automation.SwitchParameter
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

### -WhatIf

Shows what would happen if the cmdlet runs. The cmdlet isn't run.

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
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

An account object (**Microsoft.ActiveDirectory.Management.ADAccount**) is received by the
**Identity** parameter.

Derived types, such as the following are also accepted:

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**

## 输出

### 无

## 备注

- This cmdlet does not work with an Active Directory snapshot.
- This cmdlet does not work with a read-only domain controller.

## 相关链接

[Search-ADAccount](./Search-ADAccount.md)

[Set-ADAccountExpiration](./Set-ADAccountExpiration.md)

[Get-ADUser](./Get-ADUser.md)

[Get-ADComputer](./Get-ADComputer.md)

[Windows PowerShell中的AD DS管理命令集](./activedirectory.md)
