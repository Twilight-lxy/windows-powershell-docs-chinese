---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-adserviceaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADServiceAccount
---

# 删除 AD 服务账户

## 摘要
删除一个由 Active Directory 管理的服务账户对象或由组管理的服务账户对象。

## 语法

```
Remove-ADServiceAccount [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADServiceAccount> [-Partition <String>] [-Server <String>] [<CommonParameters>]
```

## 描述
`Remove-ADServiceAccount` cmdlet 用于删除一个由 Active Directory 管理的服务账户。此 cmdlet 不会对使用该服务账户的任何计算机进行任何更改。操作完成后，该服务账户将不再存在于目录中，但相关计算机的配置仍会显示该账户被使用。

`Identity` 参数用于指定要删除的 Active Directory 管理服务账户。您可以通过该账户的唯一名称（DN）、GUID、安全标识符（SID）或安全账户管理器（SAM）账户名称来识别该管理服务账户。您还可以将 `Identity` 参数设置为一个管理服务账户对象变量（例如 `$<localServiceAccountObject>`），或者通过管道将该管理服务账户对象传递给 `Identity` 参数。例如，您可以使用 **Get-ADServiceAccount** cmdlet 来检索一个管理服务账户对象，然后通过管道将该对象传递给 **Remove-ADServiceAccount** cmdlet。

注意：删除服务账户与在本地卸载该服务账户是不同的操作。

## 示例

### 示例 1：删除指定的托管服务账户
```
PS C:\> Remove-ADServiceAccount -Identity SQL-SRV1
```

此命令将删除名为 SQL-SRV1 的托管服务账户。

### 示例 2：删除经过过滤的管理服务账户列表
```
PS C:\> Get-ADServiceAccount -Filter "Name -like 'SQL*'" | Remove-ADServiceAccount
```

此命令会删除所有名称以“SQL”开头的受管理服务账户。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值包括：

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
在运行cmdlet之前，会提示您进行确认。

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

要指定这个参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

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

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个表示搜索未完成的错误信息。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为某个对象的实例。

```yaml
Type: ADServiceAccount
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Partition
指定一个 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器上所支持的命名上下文之一。此 cmdlet 会在此分区中搜索由 *Identity* 参数定义的对象。

在许多情况下，如果未指定 `Partition` 参数的值，系统会使用默认值。确定默认值的规则如下所示。请注意，列出的规则会按顺序依次被评估；一旦确定了默认值，后续的规则将不再被执行。

在 Active Directory Domain Services (AD DS) 环境中，*Partition* 的默认值将在以下情况下被设置：

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* will be set to the default partition or naming context of the target domain.

In AD LDS environments, a default value for *Partition* will be set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* will be set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent (DSA) object (**nTDSDSA**) for the AD LDS instance.
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

### -Server
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的相关值。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot instance）。

域名值：

- Fully qualified domain name (FQDN)
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

*Server* 参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

- By using *Server* value from objects passed through the pipeline.
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

### -WhatIf
展示了如果该cmdlet运行会发生的结果。但实际上该cmdlet并未被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft.ActiveDirectory.Management.ADServiceAccount
由*Identity*参数接收一个托管服务账户对象。

## 输出

### 无

## 备注
* This cmdlet does not work with Active Directory Lightweight Directory Services (AD LDS).
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.
* By default, this cmdlet has the *Confirm* parameter set, which prompts you to confirm before a removal of the specified object type can occur. To bypass prompting for confirmation before removal, you can specify `-Confirm:$False` when using this cmdlet.

## 相关链接

[Get-ADServiceAccount](./Get-ADServiceAccount.md)

[安装 AD 服务账户](./Install-ADServiceAccount.md)

[New-ADServiceAccount](./New-ADServiceAccount.md)

[Set-ADServiceAccount](./Set-ADServiceAccount.md)

[卸载AD服务账户](./Uninstall-ADServiceAccount.md)

