---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-adprincipalgroupmembership?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADPrincipalGroupMembership
---

# 移除 AD 主组成员身份

## 摘要
将某个成员从一个或多个 Active Directory 组中移除。

## 语法

```
Remove-ADPrincipalGroupMembership [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADPrincipal> [-MemberOf] <ADGroup[]> [-Partition <String>] [-PassThru] [-Server <String>]
 [<CommonParameters>]
```

## 描述
`Remove-ADPrincipalGroupMembership` cmdlet 可以将用户、组、计算机、服务账户或任何其他账户对象从一个或多个 Active Directory 组中删除。

`Identity` 参数用于指定要删除的用户、组或计算机。您可以通过其唯一名称（Distinguished Name）、全局唯一标识符（GUID）、安全标识符（Security Identifier，SID）或安全账户管理器（Security Account Manager，SAM）帐户名称来识别该用户、组或计算机。此外，您还可以指定一个用户/组/计算机对象变量（例如 `$<localGroupObject>`），或将某个对象通过管道传递给 `Identity` 参数。例如，您可以使用 `Get-ADUser` cmdlet 获取用户对象，然后将该对象通过管道传递给 `Remove-ADPrincipalGroupMembership` cmdlet；同样地，您也可以使用 `Get-ADGroup` 或 `Get-ADComputer` 来获取组、服务帐户或计算机对象，并将它们通过管道传递。

此cmdlet会从管道中收集所有的用户、计算机、服务账户和组对象，然后通过一次Active Directory操作将这些对象从指定的组中删除。

`memberOf` 参数用于指定您希望从中移除成员的组。您可以通过组的唯一名称、GUID、安全标识符或 SAM 账户名称来识别该组。您也可以指定组对象变量（例如 `$<localGroupObject>`）。如果要指定多个组，请使用逗号分隔的列表。需要注意的是，无法将组对象直接通过管道传递给 `memberOf` 参数。要从通过管道传递过来的组中移除成员，请使用 `Remove-ADGroupMember` cmdlet。

## 示例

### 示例 1：将用户从组中移除
```
PS C:\> Remove-ADPrincipalGroupMembership -Identity "David Chew" -MemberOf "Administrators"
Remove members from group
Do you want to remove all the specified member(s) from the specified group(s)?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```

此命令会将用户David Chew从“Administrators”组中删除。

### 示例 2：将用户从特定名称组中移除
```
PS C:\> Get-ADUser -Server localhost:60000 -Identity "CN=GlenJohns,DC=AppNC" | Remove-ADPrincipalGroupMembership -MemberOf "CN=AccessControl,DC=AppNC"
```

该命令使用管道运算符（pipeline operator）来查找具有唯一名称 CN=DavidChew,DC=AppNC 的用户，并将其从名为 CN=AccessControl,DC=AppNC 的组中移除。

## 参数

### -AuthType
指定要使用的认证方法。此参数的可接受值为：

- Negotiate or 0
- Basic or 1

默认的认证方法是“Negotiate”。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Active Directory PowerShell 提供程序驱动器运行的；在这种情况下，默认凭据将是与该驱动器关联的用户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

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
通过提供以下属性值之一来指定一个 Active Directory 主体对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

The cmdlet searches the default naming context or partition to find the object.
If two or more objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

Derived types, such as the following are also accepted:

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**

```yaml
Type: ADPrincipal
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -MemberOf
Specifies the Active Directory groups to remove a user, computer, or group to as a member.
You can identify a group by providing one of the following values.
Note: The identifier in parentheses is the LDAP display name for the attribute.
The acceptable values for this parameter are:

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

If you are specifying more than one group, use commas to separate the groups in the list.

```yaml
Type: ADGroup[]
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

In many cases, a default value will be used for the *Partition* parameter if no value is specified.
The rules for determining the default value are given below.
Note that rules listed first are evaluated first and once a default value can be determined, no further rules will be evaluated.

In Active Directory Domain Services (AD DS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent (DSA) object (**nTDSDSA**) for the AD LDS instance.
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

### 无值或 Microsoft.ActiveDirectory.Management_ADPrincipal
A principal object that represents user, computer, or group is received by the *Identity* parameter.
Derived types, such as the following are also received by this parameter.

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADGroup**

## 输出

### 无值或 Microsoft.ActiveDirectory.Management_ADPrincipal
当指定 *PassThru* 参数时，该 cmdlet 会返回一个表示已修改的用户、计算机或组对象的主对象。默认情况下，此 cmdlet 不会产生任何输出。

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.
* By default, this cmdlet has the *Confirm* parameter set, which prompts you to confirm before a removal of the specified object type can occur. To bypass prompting for confirmation before removal, you can specify `-Confirm:$False` when using this cmdlet.

## 相关链接

[Add-ADGroupMember](./Add-ADGroupMember.md)

[Add-ADPrincipalGroup Membership](./Add-ADPrincipalGroupMembership.md)

[Get-ADComputer](./Get-ADComputer.md)

[Get-ADGroup](./Get-ADGroup.md)

[Get-ADGroupMember](./Get-ADGroupMember.md)

[Get-ADPrincipalGroupMembership](./Get-ADPrincipalGroupMembership.md)

[Get-ADServiceAccount](./Get-ADServiceAccount.md)

[Get-ADUser](./Get-ADUser.md)

[Remove-ADGroupMember](./Remove-ADGroupMember.md)

