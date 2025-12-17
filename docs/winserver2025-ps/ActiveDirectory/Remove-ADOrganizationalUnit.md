---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-adorganizationalunit?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADOrganizationalUnit
---

# 删除 AD 组织单元

## 摘要
删除一个 Active Directory 组织单位。

## 语法

```
Remove-ADOrganizationalUnit [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADOrganizationalUnit> [-Partition <String>] [-Recursive] [-Server <String>] [<CommonParameters>]
```

## 描述
`Remove-ADOrganizationalUnit` cmdlet 用于删除 Active Directory 中的组织单元（Organizational Unit，简称 OU）。

`Identity` 参数用于指定要删除的组织单位。您可以通过该组织单位的唯一名称（Distinguished Name）或 GUID 来识别它。您也可以将该参数设置为一个组织单位对象变量（例如 `$<localOrganizationUnitObject>`），或者通过管道将某个对象传递给 `Identity` 参数。例如，可以使用 `Get-ADOrganizationalUnit` cmdlet 获取该组织单位对象，然后再通过管道将其传递给 `Remove-ADOrganizationalUnit` cmdlet。

如果你想要删除的对象有子对象，就必须指定*递归*参数。

如果组织单位对象（organization unit object）的 `ProtectedFromAccidentalDeletion` 属性被设置为 `true`，那么该 cmdlet 会返回一个终止错误（terminating error）。

对于 AD LDS 环境而言，必须指定 *Partition* 参数，以下两种情况除外：

- The cmdlet is run from an Active Directory provider drive.
- A default naming context or partition is defined for the AD LDS environment.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.

## 示例

### 示例 1：移除一个组织单元（OU）及其下属对象
```
PS C:\> Remove-ADOrganizationalUnit -Identity "OU=Accounting,DC=FABRIKAM,DC=COM" -Recursive
Are you sure you want to remove the item and all its children?
Performing recursive remove on Target: 'OU=Accounting,DC=Fabrikam,DC=com'.
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help
(default is "Y"):y
```

此命令会删除一个组织单元（OU）及其所有的子对象。如果该组织单元被设置为不可删除，则该组织单元及其子对象不会被删除；如果该组织单元本身没有被设置为不可删除，但其中的某个子对象被设置了不可删除属性，则该组织单元及其子对象会被删除。

### 示例 2：根据组织单元（OU）的 GUID 删除该组织单元
```
PS C:\> Remove-ADOrganizationalUnit -Identity "1b228aa5-2c14-48b8-ad8a-2685dc22e055" -Confirm:$False
```

这个命令会根据对象GUID来删除指定的组织单元（OU），并且会跳过确认提示。

### 示例 3：删除指定的组织单元（OU）
```
PS C:\> Remove-ADOrganizationalUnit -Identity "OU=Accounting,DC=FABRIKAM,DC=COM"
Confirm
Are you sure you want to perform this action?
Performing operation "Remove" on Target "OU=Accounting,DC=Fabrikam,DC=com".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help
(default is "Y"):y
```

这个命令会删除“会计”（Accounting）组织单元（OU）。

### 示例 4：从 AD LDS 实例中删除一个组织单元（OU）
```
PS C:\> Remove-ADOrganizationalUnit -Identity "OU=Managed,DC=AppNC" -Server "FABRIKAM-SRV1:60000" -Confirm:$False
```

此命令用于从 AD LDS 实例中删除一个组织单元（OU）。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Active Directory PowerShell提供程序驱动器运行的；如果是从此类驱动器运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该cmdlet会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行任务的代理凭据没有目录级别的权限，Active Directory PowerShell 将返回一个终止错误。

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
通过提供以下值之一来指定一个 Active Directory 组对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- 一个著名的名称  
- 一个 GUID（objectGUID）

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个表示搜索未完成的错误信息。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

```yaml
Type: ADOrganizationalUnit
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Partition
指定一个 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器上的命名上下文之一。此 cmdlet 会在此分区中搜索由 *Identity* 参数定义的对象。

在许多情况下，如果未指定任何值，则会为*Identity*参数使用一个默认值。确定默认值的规则如下所示。请注意，首先列出的规则会被优先评估；一旦确定了默认值，就不会再继续评估其他规则了。

在 Active Directory 域服务（AD DS）环境中，以下情况下会为“分区”（Partition）设置默认值：

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Partition* parameter does not take any default value.

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

### -Recursive
表示此cmdlet将删除该组织单元（OU）及其包含的所有子项。如果要删除一个非空的OU，则必须指定此参数。

注意：指定此参数会移除组织单元（OU）中所有被标记为 **ProtectedFromAccidentalDeletion** 的子对象。

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
指定要连接的 AD DS 实例，为此请提供相应的域名或目录服务器之一。该服务可以是以下类型中的任意一种：AD LDS、AD DS 或 Active Directory 快照实例。

以下是指定 AD DS 实例的几种方式：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

该参数的默认值是通过以下方法之一确定的，确定顺序按照列出的顺序进行：

- By using the *Server* value from objects passed through the pipeline
- By using the server information associated with the AD DS Windows PowerShell provider drive, when the cmdlet runs in that drive
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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

没有相关对象，或者使用了 `Microsoft.ActiveDirectory.Management.ADOrganizationalUnit` 类。
一个 `ADOrganizationalUnit` 对象通过 `Identity` 参数被接收。

## 输出

### 无

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.
* By default, this cmdlet has the *Confirm* parameter set, which prompts you to confirm before a removal of the specified object type can occur. To bypass prompting for confirmation before removal, you can specify `-Confirm:$False` when using this cmdlet.

## 相关链接

[Get-ADOrganizationalUnit](./Get-ADOrganizationalUnit.md)

[New-ADOrganizationalUnit](./New-ADOrganizationalUnit.md)

[Set-ADOrganizationalUnit](./Set-ADOrganizationalUnit.md)

