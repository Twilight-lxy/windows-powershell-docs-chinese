---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/unlock-adaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Unlock-ADAccount
---

# 解锁 AD 账户

## 摘要
解锁一个 Active Directory 账户。

## 语法

```
Unlock-ADAccount [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADAccount> [-Partition <String>] [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述
`Unlock-ADAccount` cmdlet 可以恢复被锁定的账户对 Active Directory 域服务（AD DS）的访问权限。当账户输入错误密码的次数超过密码策略允许的最大次数时，该账户的对 AD DS 的访问权限会被暂停或锁定。

`Identity` 参数用于指定要解锁的 Active Directory 账户。您可以通过该账户的唯一名称（Distinguished Name）、 GUID、安全标识符（Security Identifier，SID）或安全帐户管理器（Security Accounts Manager，SAM）账户名称来识别该账户。您还可以将 `Identity` 参数设置为某个账户对象变量（例如 `$<localADAccountObject>`），或者通过管道将某个对象传递给 `Identity` 参数。例如，可以使用 **Search-ADAccount** cmdlet 获取一个账户对象，然后通过管道将该对象传递给 `Unlock-ADAccount` cmdlet 以解锁该账户；同样地，您也可以使用 **Get-ADUser** 和 **Get-ADComputer** 来获取所需对象并通过管道进行后续操作。

对于 Active Directory 轻量级目录服务（AD LDS）环境而言，必须指定 *Partition* 参数，除非满足以下情况：

- Using a distinguished name to identify objects: the partition is auto-generated from the distinguished name.
- Running cmdlets from an Active Directory provider drive: the current path is used to set the partition.
- A default naming context or partition is specified.

要为 AD LDS 环境指定一个默认的命名上下文，请设置 AD LDS 实例的 Active Directory 目录服务代理对象（**nTDSDSA**）的 **msDS-defaultNamingContext** 属性。

## 示例

#### 示例 1：解锁一个 Active Directory 账户
```
PS C:\> Unlock-ADAccount -Identity PattiFu
```

此命令会使用名为 PattiFu 的 SAM 账户名来解锁该账户。

### 示例 2：使用istinguished名称解锁Active Directory账户
```
PS C:\> Unlock-ADAccount -Identity "CN=Patti Fuller,OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM"
```

该命令用于解锁名为“CN=Patti Fuller, OU=Finance, OU/UserAccounts, DC=FABRIKAM, DC=COM”的账户。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

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

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Windows PowerShell提供程序的Active Directory模块驱动器中运行的。如果该cmdlet是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 [Get-Credential](https://go.microsoft.com/fwlink/?LinkID=293936) cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将该 **Credential** 对象设置为相应的参数。

如果执行该任务的代理组件没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

### -Identity
通过提供以下属性值之一来指定一个 Active Directory 账户对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

该 cmdlet 会在默认的命名上下文或分区中搜索以找到相应的对象。如果找到两个或多个对象，该 cmdlet 会返回一个无法终止的错误信息。

这个参数也可以通过管道获取该对象，或者你可以将该参数设置为一个账户对象实例。

也接受以下这样的派生类型：

- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADUser**

```yaml
Type: ADAccount
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Partition
Specifies the distinguished name of an Active Directory partition.
The distinguished name must be one of the naming contexts on the current directory server.
The cmdlet searches this partition to find the object defined by the *Identity* parameter.

In many cases, a default value is used for the *Partition* parameter if no value is specified.
The rules for determining the default value are given below.
Note that rules listed first are evaluated first and once a default value can be determined, no further rules are evaluated.

In AD DS environments, a default value for **Partition** is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of **Partition** is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of **Partition** is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of **Partition** is set to the default partition or naming context of the target domain.

In AD LDS environments, a default value for **Partition** is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of **Partition** is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of **Partition** is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of **Partition** is set to the default naming context.
要为 AD LDS 环境指定一个默认的命名上下文，请设置 AD LDS 实例的 Active Directory 目录服务代理对象（**nTDSDSA**）的 **msDS-defaultNamingContext** 属性。
- If none of the previous cases apply, the *Partition* parameter will not take any default value.

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

### -PassThru
Returns an object representing the item with which you are working.
By default, this cmdlet does not generate any output.

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

### -Server
Specifies the Active Directory Domain Services instance to connect to, by providing one of the following values for a corresponding domain name or directory server.
The service may be any of the following: Active Directory Lightweight Domain Services, Active Directory Domain Services or Active Directory snapshot instance.

Specify the Active Directory Domain Services instance in one of the following ways:

Domain name values:

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

The default value for this parameter is determined by one of the following methods in the order that they are listed:

- By using the **Server** value from objects passed through the pipeline
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

### -WhatIf
Shows what would happen if the cmdlet runs.
The cmdlet is not run.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### 无 or Microsoft.ActiveDirectory.Management.ADAccount
An account object is received by the *Identity* parameter.

Derived types, such as the following, are also accepted:

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**

## 输出

### 无

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Clear-ADAccountExpiration](./Clear-ADAccountExpiration.md)

[禁用 AD 账户](./Disable-ADAccount.md)

[Enable-ADAccount](./Enable-ADAccount.md)

[Get-ADAccountAuthorizationGroup](./Get-ADAccountAuthorizationGroup.md)

[Search-ADAccount](./Search-ADAccount.md)

[Set-ADAccountControl](./Set-ADAccountControl.md)

[Set-ADAccountExpiration](./Set-ADAccountExpiration.md)

[Set-ADAccountPassword](./Set-ADAccountPassword.md)

[Windows PowerShell中的AD DS管理cmdlet](./activedirectory.md)

