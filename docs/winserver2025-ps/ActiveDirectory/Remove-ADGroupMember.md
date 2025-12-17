---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 06/11/2021
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADGroupMember
---

# 移除AD组成员

## 摘要
从一个Active Directory组中移除一个或多个成员。

## 语法

```
Remove-ADGroupMember [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADGroup> [-Members] <ADPrincipal[]> [-Partition <String>] [-PassThru] [-Server <String>]
 [-DisablePermissiveModify] [<CommonParameters>]
```

## 描述
`Remove-ADGroupMember` cmdlet 可以将一个或多个用户、组、服务账户或计算机从 Active Directory 组中移除。

`Identity` 参数用于指定包含需要删除的成员的 Active Directory 组。您可以通过该组的唯一名称（Distinguished Name）、GUID、安全标识符或安全账户管理器（Security Account Manager, SAM）帐户名称来识别该组。此外，您还可以指定一个组对象变量（例如 `$<localGroupObject>`），或者通过管道将某个组对象传递给 `Identity` 参数。例如，您可以使用 **Get-ADGroup** cmdlet 来获取一个组对象，然后将该对象通过管道传递给 `Remove-ADGroupMember` cmdlet。

`Members` 参数用于指定要从由 `Identity` 参数指定的组中删除的用户、计算机和组。您可以通过它们的唯一名称（Distinguished Name）、GUID、安全标识符（Security Identifier）或 SAM 账户名来识别用户、计算机或组。您还可以指定用户、计算机和组对象变量，例如 `$<localUserObject>`。如果您要指定多个新成员，请使用逗号分隔的列表。无法通过管道将用户、计算机或组对象传递给此 cmdlet。要通过管道从组中删除用户、计算机或组对象，请使用 `Remove-ADPrincipalGroupMembership` cmdlet。

对于 Active Directory 轻量级目录服务（AD LDS）环境，必须指定 *Partition* 参数，以下两种情况除外：

- The cmdlet is run from an Active Directory provider drive.
- A default naming context or partition is defined for the AD LDS environment.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.

## 示例

### 示例 1：从组中移除成员
```
PS C:\> Remove-ADGroupMember -Identity DocumentReaders -Members DavidChew
Confirm
Are you sure you want to perform this action?
Performing operation "Set" on Target "CN=DocumentReaders,CN=Users,DC=Fabrikam,DC=com".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```

此命令会将使用SAM账户名称“DavidChew”的用户从“DocumentReaders”组中移除。

### 示例 2：从组中删除多个成员
```
PS C:\> Remove-ADGroupMember -Identity "DocumentReaders" -Members administrator,DavidChew
```

这个命令会将用户名为“administrator”和“DavidChew”的用户从“DocumentReaders”组中移除。

### 示例 3：将一位具有特殊权限的用户从组中移除
```
PS C:\> Get-ADGroup -Server localhost:60000 -Identity CN=AccessControl,DC=AppNC | Remove-ADGroupMember -Members CN=GlenJohn,DC=AppNC
Confirm
Are you sure you want to perform this action?
Performing operation "Set" on Target "CN=AccessControl,DC=AppNC".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```

此命令使用管道将具有独特名称“CN=GlenJohn,DC=AppNC”的用户从AD LDS实例中的AccessControl组中删除。

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
在运行cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: True
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

如果该执行任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

### -DisablePermissiveModify
组成员信息的更新默认采用“允许修改”（permissive modify）的权限设置。这种设置可以避免在尝试删除实际上并不属于该组的成员时出现错误。当使用这个参数时，系统会返回一个错误信息：“指定的账户名称不属于该组”。

此参数在安装了2020年9月更新的Windows Server 2019系统中可用。


```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity
通过提供以下值之一来指定一个 Active Directory 组对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A Security Account Manager account name (sAMAccountName)

此cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止的错误（即程序会持续运行而不会停止）。

这个参数也可以通过管道获取该对象，或者你可以将该参数设置为一个对象实例。

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

### -Members
指定一个由用户、组和计算机对象组成的数组（这些对象以逗号分隔的列表形式提供），以便从某个组中移除这些对象。要识别每个对象，请使用以下属性值之一。注意：括号中的标识符是LDAP显示名称。此参数的可接受值为：

- Distinguished name
- GUID (objectGUID)
- Security identifier (objectSid)
- SAM account name (sAMAccountName)

您也可以直接将对象传递给这个参数。

以下示例展示了如何指定这个参数。

这个示例通过指定用户的唯一名称（Distinguished Name）和SAM账户名称属性来指定要删除的用户和组。

```
-Members "CN=SaraDavis,CN=employees,CN=Users,DC=contoso,DC=com", "saradavisreports"
```

这个示例指定了一个用户和一个组对象，这两个对象是在当前的 Windows PowerShell 会话中定义的，并作为参数的输入值。

`-成员：$userObject、$GroupObject`

此参数指定的对象会被处理为 **Microsoft ActiveDirectory.Management.ADPrincipal** 对象。此外，该参数还会接收各种派生类型（例如以下所示的类型）。

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADGroup**

You cannot pass objects through the pipeline to this parameter.

```yaml
Type: ADPrincipal[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Partition
Specifies the distinguished name of an Active Directory partition.
The distinguished name must be one of the naming contexts on the current directory server.
The cmdlet searches this partition to find the object defined by the *Identity* parameter.

In many cases, a default value is used for the *Partition* parameter if no value is specified.
The rules for determining the default value are given below.
Note that rules listed first are evaluated first and once a default value can be determined, no further rules are evaluated.

In Active Directory Domain Services (AD DS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Partition* parameter does not take a default value.

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
Specifies the AD DS instance to connect to, by providing one of the following values for a corresponding domain name or directory server.
The service may be any of the following: AD LDS, AD DS, or Active Directory snapshot instance.

Specify the AD DS instance in one of the following ways:

Domain name values:

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

The default value for this parameter is determined by one of the following methods in the order that they are listed:

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

### -DisablePermissiveModify
组成员信息的更新默认采用“允许修改”（permissive modify）的权限设置。这种设置可以避免在尝试删除实际上并不属于该组的成员时出现错误。当使用这个参数时，系统会返回一个错误信息：“指定的账户名称不属于该组”。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:
Required: False
Position: Named
Default value: False
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

### 无或 Microsoft.ActiveDirectory.Management_ADGroup
A group object is received by the *Identity* parameter.

## 输出

### 无或 Microsoft.ActiveDirectory.Management_ADGroup
当指定 *PassThru* 参数时，会返回修改后的组对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.
* By default, this cmdlet has the *Confirm* parameter set, which prompts you to confirm before a removal of the specified object type can occur. To bypass prompting for confirmation before removal, you can specify `-Confirm:$False` when using this cmdlet.

## 相关链接

[Add-ADGroupMember](./Add-ADGroupMember.md)

[Add-ADPrincipalGroupMembership](./Add-ADPrincipalGroupMembership.md)

[Get-ADGroup](./Get-ADGroup.md)

[Get-ADGroupMember](./Get-ADGroupMember.md)

[Get-ADPrincipalGroupMembership](./Get-ADPrincipalGroupMembership.md)

[Remove-ADPrincipalGroupMembership](./Remove-ADPrincipalGroupMembership.md)

