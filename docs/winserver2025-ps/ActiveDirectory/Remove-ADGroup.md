---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-adgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADGroup
---

# 删除广告组（Remove-ADGroup）

## 摘要
删除一个Active Directory组。

## 语法

```
Remove-ADGroup [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADGroup>
 [-Partition <String>] [-Server <String>] [<CommonParameters>]
```

## 描述
**Remove-ADGroup** cmdlet 用于删除 Active Directory 组对象。您可以使用此 cmdlet 删除安全组（security groups）和分布组（distribution groups）。

`Identity` 参数用于指定要删除的 Active Directory 组。您可以通过该组的 distinguished name（唯一名称）、GUID、安全标识符、Security Account Manager (SAM) 账户名或规范名称来识别它。您也可以将 `Identity` 参数设置为某个对象变量（例如 `$<localADGroupObject>`），或者通过管道将该对象传递给 `Identity` 参数。例如，您可以使用 `Get-ADGroup` cmdlet 获取一个组对象，然后通过管道将该对象传递给 `Remove-ADGroup` cmdlet。

如果**ADGroup**是通过其唯一名称来识别的，那么*Partition*参数会自动被确定。

对于 Active Directory 轻量目录服务（AD LDS）环境，除非满足以下两个条件，否则必须指定 *Partition* 参数：

- The cmdlet is run from an Active Directory provider drive.
- A default naming context or partition is defined for the AD LDS environment.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.

## 示例

### 示例 1：按名称删除一个组
```
PS C:\> Remove-ADGroup -Identity SanjaysReports
Confirm
Are you sure you want to perform this action?
Performing operation "Remove" on Target "CN=SanjayReports,DC=Fabrikam,DC=com".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```

此命令会删除拥有SAM账户名称“SanjaysReports”的组。

### 示例 2：获取经过过滤的组并删除它们
```
PS C:\> Get-ADGroup -Filter 'Name -like "Sanjay*"' | Remove-ADGroup
Confirm
Are you sure you want to perform this action?
Performing operation "Remove" on Target "CN=SanjaysReports,DC=Fabrikam,DC=com".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```

这个命令会获取所有名称以“Sanjay”开头的组，然后删除这些组。

## 参数

### -AuthType
指定要使用的认证方法。此参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的认证方法是“Negotiate”（协商）。

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
在运行该cmdlet之前，会提示您确认是否要继续执行。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Windows PowerShell提供程序的Active Directory模块驱动器中运行的。如果该cmdlet是从此类驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将该 `PSCredential` 对象设置为 `Credential` 参数的值。

如果执行任务的代理组件没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
通过提供以下值之一来指定一个 Active Directory 组对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A Security Account Manager account name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，cmdlet会返回一个非终止性错误（即无法继续执行的错误）。此参数也可以通过管道来获取所需对象；另外，你还可以将此参数设置为一个具体的对象实例。

```yaml
Type: ADGroup
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Partition
指定一个 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器上所支持的命名上下文之一。此 cmdlet 会在该分区中搜索由 *Identity* 参数定义的对象。

在许多情况下，如果未指定`Partition`参数的值，系统会使用一个默认值。确定默认值的规则如下所示。请注意，列出的规则会按顺序依次被评估；一旦确定了默认值，后续的规则将不再被评估。

在 Active Directory Domain Services (AD DS) 环境中，以下情况下会为“Partition”（分区）设置默认值：

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
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器对应的值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot）。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的列出的顺序：

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft ActiveDirectory.Management.AdGroup
一个组对象通过*Identity*参数被接收。

## 输出

### 无

## 备注
* This cmdlet does not work with an Active Directory Snapshot.
* This cmdlet does not work with a read-only domain controller.
* By default, this cmdlet has the *Confirm* parameter set, which prompts you to confirm before a removal of the specified object type can occur. To bypass prompting for confirmation before removal, you can specify `-Confirm:$False` when using this cmdlet.

## 相关链接

[Add-ADGroupMember](./Add-ADGroupMember.md)

[Get-ADGroup](./Get-ADGroup.md)

[Get-ADGroupMember](./Get-ADGroupMember.md)

[New-ADGroup](./New-ADGroup.md)

[Remove-ADGroupMember](./Remove-ADGroupMember.md)

[Set-ADGroup](./Set-ADGroup.md)

