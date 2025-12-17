---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-adobject?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADObject
---

# 删除 AD 对象

## 摘要
删除一个 Active Directory 对象。

## 语法

```
Remove-ADObject [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADObject> [-IncludeDeletedObjects] [-Partition <String>] [-Recursive] [-Server <String>]
 [<CommonParameters>]
```

## 描述
`Remove-ADObject` cmdlet 用于删除 Active Directory 对象。你可以使用这个 cmdlet 删除任何类型的 Active Directory 对象。

`Identity` 参数用于指定要删除的 Active Directory 对象。您可以通过该对象的唯一名称（Distinguished Name）或 GUID 来识别它。您也可以将 `Identity` 参数设置为一个 Active Directory 对象变量（例如 `$<localObject>`），或者通过管道将该对象传递给 `Identity` 参数。例如，您可以使用 **Get-ADObject** cmdlet 获取一个对象，然后通过管道将该对象传递给 **Remove-ADObject** cmdlet。

如果你指定要删除的对象有子对象，那么必须设置 `Recursive` 参数。

对于 Active Directory 轻量级目录服务（AD LDS）环境，必须指定 *Partition* 参数，除非以下情况：

- Using a distinguished name to identify objects.
The partition is auto-generated from the distinguished name.
- Running cmdlets from an Active Directory provider drive.
The current path is used to set the partition.
- A default naming context or partition is specified.

要为 AD LDS 环境指定一个默认的命名上下文，请设置 AD LDS 实例的 Active Directory 目录服务代理对象（**nTDSDSA**）的 **msDS-defaultNamingContext** 属性。

## 示例

### 示例 1：通过唯一名称删除对象
```
PS C:\> Remove-ADObject -Identity 'CN=AmyAl-LPTOP,CN=Computers,DC=FABRIKAM,DC=COM'
Confirm
Are you sure you want to perform this action?
Performing operation "Remove" on Target "CN=AmyAl-LPTOP,CN=Computers,DC=FABRIKAM,DC=COM".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): y
```

此命令会删除由唯一名称“CN=AmyAl-LPTOP,CN=Computers,DC=FABRIKAM,DC=COM”标识的对象。

### 示例 2：移除一个容器及其子节点
```
PS C:\> Remove-ADObject -Identity "OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM" -Recursive
Confirm
Are you sure you want to perform this action?
Performing operation "Remove" on Target "OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): y
```

此命令会删除名称为“OU=Finance,OU>UserAccounts,DC=FABRIKAM,DC=COM”的容器。该容器的所有子容器也会被删除，包括那些被设置为防止意外删除的子容器。

### 示例 3：通过 GUID 删除对象
```
PS C:\> Remove-ADObject -Identity "65511e76-ea80-45e1-bc93-08a78d8c4853" -Confirm:$False
```

此命令会删除GUID为65511e76-ea80-45e1-bc93-08a78d8c4853的对象，而不会提示用户进行确认。

### 示例 4：从 LDS 实例中删除一个对象
```
PS C:\> Remove-ADObject -Identity "CN=InternalApps,DC=AppNC" -Server "FABRIKAM-SRV1:60000"
Confirm
Are you sure you want to perform this action?
Performing operation "Remove" on Target "CN=InternalApps,DC=AppNC".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): y
```

该命令会从LDS实例中删除名称为CN=InternalApps,DC=AppNC的对象。

### 示例 5：在回收站中回收对象
```
PS C:\> Get-ADObject -Filter 'isDeleted -eq $True -and -not (isRecycled -eq $true) -and name -ne "Deleted Objects" -and lastKnownParent -eq "OU=Accounting,DC=Fabrikam,DC=com"' -IncludeDeletedObjects | Remove-ADObject
```

这个命令会回收回收站中的所有对象，这些对象原本属于容器“OU=Accounting,DC=Fabrikam,DC=com”。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认凭据将是与该驱动器关联的账户的凭据。

要指定这个参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行该任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
通过提供以下属性值之一来指定一个 Active Directory 对象。括号中的标识符是该属性的轻型目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)

该cmdlet会在默认的命名上下文或分区中搜索要找的对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止的错误（即程序会无限循环执行）。

这个参数也可以通过管道获取该对象，或者你可以将该参数设置为一个对象实例。

也接受派生类型，例如以下这些：

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy**
- **Microsoft.ActiveDirectory.Management.ADDomain**

```yaml
Type: ADObject
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -IncludeDeletedObjects
Specifies that the cmdlet retrieves deleted objects and the deactivated forward and backward links.
When this parameter is specified, the cmdlet uses the following LDAP controls:

- Show Deleted Objects (1.2.840.113556.1.4.417)
- Show Deactivated Links (1.2.840.113556.1.4.2065)

Note: If this parameter is not specified, the cmdlet does not return or operate on deleted objects.

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

In AD LDS environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
要为 AD LDS 环境指定一个默认的命名上下文，请设置 AD LDS 实例的 Active Directory 目录服务代理对象（**nTDSDSA**）的 **msDS-defaultNamingContext** 属性。
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

### -Recursive
Indicates that this cmdlet removes the object and any children it contains.

Note: Specifying this parameter removes all child objects even if there are objects marked with **ProtectedFromAccidentalDeletion**.

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

### 无 or Microsoft.ActiveDirectory.Management.ADObject
An Active Directory object is received by the *Identity* parameter.
也接受派生类型，例如以下这些：

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADOrganizationalUnit**
- **Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy**
- **Microsoft.ActiveDirectory.Management.ADDomain**

## 输出

### 无

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.
* This cmdlet does not work when connected to a global catalog port.
* By default, this cmdlet has the *Confirm* parameter set, which prompts you to confirm before a removal of the specified object type can occur. To bypass prompting for confirmation before removal, you can specify `-Confirm:$False` when using this cmdlet.

## 相关链接

[Get-ADObject](./Get-ADObject.md)

[Move-ADObject](./Move-ADObject.md)

[New-ADObject](./New-ADObject.md)

[ Rename-ADObject ](./Rename-ADObject.md)

[Set-ADObject](./Set-ADObject.md)

[Sync-ADObject](./Sync-ADObject.md)

