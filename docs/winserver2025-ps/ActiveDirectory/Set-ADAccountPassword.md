---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ADAccountPassword
---

# 设置 AD 账户密码

## 摘要
修改 Active Directory 账户的密码。

## 语法

```
Set-ADAccountPassword [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADAccount> [-NewPassword <SecureString>] [-OldPassword <SecureString>] [-Partition <String>]
 [-PassThru] [-Reset] [-Server <String>] [<CommonParameters>]
```

## 描述
`Set-ADAccountPassword` cmdlet 用于设置用户、计算机或服务账户的密码。

*Identity* 参数指定了要修改的 Active Directory 账户。

您可以通过账户的独特名称、GUID（全局唯一标识符）、安全标识符（SID）或安全帐户管理器（SAM）账户名称来识别该账户。您还可以将 *Identity* 参数设置为某个对象变量（例如 `$<localADAccountObject>`），或者通过管道将该对象传递给 *Identity* 参数。例如，您可以使用 **Search-ADAccount** cmdlet 获取一个账户对象，然后通过管道将该对象传递给 **Set-ADAccountPassword** cmdlet。同样地，您也可以使用 **Get-ADUser**、**Get-ADComputer** 或 **Get-ADServiceAccount**（用于独立的 MSAs）等 cmdlet 来获取账户对象，并将这些对象通过管道传递给相应的 cmdlet。

注意：群组管理的 Microsoft Account（MSA）无法设置密码，因为其密码会按照预定的时间间隔自动更改。

对于 Active Directory 轻量级目录服务（AD LDS）环境，除非满足以下两种情况，否则必须指定 “Partition” 参数：

- The cmdlet is run from an Active Directory provider drive.
- A default naming context or partition is defined for the AD LDS environment.

要为 AD LDS 环境指定一个默认的命名上下文，请设置 Active Directory 目录服务代理（DSA）对象（**nTDSDSA**）的 **msDS-defaultNamingContext** 属性，该对象属于相应的 AD LDS 实例。

## 示例

### 示例 1：使用可区分名称（distinguished name）为用户账户设置密码
```
PS C:\> Set-ADAccountPassword -Identity 'CN=Elisa Daugherty,OU=Accounts,DC=Fabrikam,DC=com' -Reset -NewPassword (ConvertTo-SecureString -AsPlainText "p@ssw0rd" -Force)
```

此命令将用户名为“DistinguishedName CN=Elisa Daugherty, OU=Accounts, DC=Fabrikam, DC=com”的用户的密码设置为“p@ssw0rd”。

### 示例 2：更改指定用户的密码
```
PS C:\> Set-ADAccountPassword -Identity elisada -OldPassword (ConvertTo-SecureString -AsPlainText "p@ssw0rd" -Force) -NewPassword (ConvertTo-SecureString -AsPlainText "qwert@12345" -Force)
```

此命令将用户账户“SamAccountName=elisada”的密码设置为“qwert@12345”。如果使用参数 `-NewPassword` 并指定新密码，而不提供参数 `-OldPassword` 的值，那么该用户的密码也会被重置。

### 示例 3：提示指定的用户更改他们的密码
```
PS C:\> Set-ADAccountPassword -Identity EvanNa


Please enter the current password for 'CN=Evan Narvaez,CN=Users,DC=Fabrikam,DC=com'
Password:**********
Please enter the desired password for 'CN=Evan Narvaez,CN=Users,DC=Fabrikam,DC=com'
Password:***********
Repeat Password:***********
```

此命令用于设置用户账户的密码，该用户的 distinguishedName 为 CN=Evan Narvaez,CN=Users,DC=Fabrikam,DC=com。该 cmdlet 会提示您输入旧密码和新密码。

### 示例 4：提示用户输入新密码，并将新密码存储在一个临时变量中
```
PS C:\> $NewPassword = (Read-Host -Prompt "Provide New Password" -AsSecureString)
PS C:\> Set-ADAccountPassword -Identity DavidChe -NewPassword $NewPassword -Reset
Provide New Password: **********
```

这个命令会提示用户输入一个新的密码，该密码会被存储在一个名为 $NewPassword 的临时变量中，随后使用这个新密码来重置用户名为 DavidChe 的用户账户的密码。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

如果该执行任务的账号没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
通过提供以下属性值之一来指定一个 Active Directory 用户对象。括号中的标识符是该属性的轻型目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个表示无法继续执行的错误（即非终止性错误）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象的实例。

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

### -NewPassword
指定一个新的密码值。该值会以加密字符串的形式存储。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OldPassword
指定最新的密码值。该值以加密字符串的形式进行处理。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Partition
指定一个 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器所支持的命名上下文之一。此 cmdlet 会在此分区中搜索由 *Identity* 参数定义的对象。

在许多情况下，如果未指定“Partition”参数的值，则会使用默认值。确定默认值的规则如下所示。请注意，首先列出的规则会被优先评估；一旦确定了默认值，就不会再继续评估其他规则了。

在 Active Directory 域服务环境中，以下情况下会为 **分区（Partition）** 设置默认值：

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In AD LDS environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of  is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.
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
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -Reset
用于指定重置账户的密码。使用此参数时，必须设置 *NewPassword* 参数；无需设置 *OldPassword* 参数。

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
指定要连接的 Active Directory 域服务实例，为此提供相应的域名或目录服务器之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

域名值：

- Fully qualified domain name (FQDN)
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

*Server* 参数的默认值是根据以下方法之一确定的，确定顺序如下所示：

- By using *Server* value from objects passed through the pipeline.
- By using the server information associated with the Active Directory provider drive, when running under that drive.
- By using the domain of the computer running Windows PowerShell.

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft ActiveDirectory.Management.ADAccount
一个账户对象通过*Identity*参数被接收。

派生类型也是被接受的，例如以下这些类型：

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**

## 输出

### 无

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller. This cmdlet does not work when connected to global catalog port.

## 相关链接

[Get-ADComputer](./Get-ADComputer.md)

[Get-ADServiceAccount](./Get-ADServiceAccount.md)

[Get-ADUser](./Get-ADUser.md)

[Search-ADAccount](./Search-ADAccount.md)

[Windows PowerShell 中的 AD DS 管理命令集](./activedirectory.md)

