---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adprincipalgroupmembership?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADPrincipalGroupMembership
---

# 获取 AD 主体组成员身份信息

## 摘要
获取包含指定用户、计算机、组或服务帐户的 Active Directory 组。

## 语法

```
Get-ADPrincipalGroupMembership [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADPrincipal>
 [-Partition <String>] [-ResourceContextPartition <String>] [-ResourceContextServer <String>]
 [-Server <String>] [<CommonParameters>]
```

## 描述
**Get-ADPrincipalGroupMembership** cmdlet 可用于获取那些包含指定用户、计算机、组或服务账户作为成员的 Active Directory 组。该 cmdlet 需要使用全局目录来执行组搜索。如果包含该用户、计算机或组的域没有全局目录，该 cmdlet 会返回一个无法终止的错误。如果你想在另一个域中搜索本地组，请使用 *ResourceContextServer* 参数来指定该另一个域中的备用服务器。

`Identity` 参数用于指定您想要确定其组成员身份的用户、计算机或组对象。您可以通过该对象的唯一名称（Distinguished Name）、GUID、安全标识符（Security Identifier）或 SAM 账户名称来识别该用户、计算机或组对象。此外，您还可以指定一个用户、组或计算机的变量（例如 `$<localGroupObject>`），或者将某个对象通过管道传递给 `Identity` 参数。例如，您可以使用 `Get-ADGroup` cmdlet 获取一个组对象，然后将该对象通过管道传递给 `Get-ADPrincipalGroupMembership` cmdlet；同样地，您也可以使用 `Get-ADUser` 或 `Get-ADComputer` 来获取用户或计算机对象，并将其通过管道进行后续处理。

对于 Active Directory 轻量级目录服务（AD LDS）环境，除非满足以下两种情况，否则必须指定 *Partition* 参数：

- The cmdlet is run from an Active Directory provider drive.
- A default naming context or partition is defined for the AD LDS environment.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent  object (**nTDSDSA**) for the AD LDS instance.

## 示例

### 示例 1：获取 AD LDS 实例中用户的组成员身份
```
PS C:\> Get-ADPrincipalGroupMembership -Server localhost:60000 -Identity "CN=DavidChew,DC=AppNC" -Partition "DC=AppNC"
```

这个命令可以获取AD LDS实例中用户CN=DavidChew,DC=AppNC的所有组成员身份信息。

### 示例 2：获取管理员的组成员身份信息
```
PS C:\> Get-ADPrincipalGroupMembership -Identity Administrator


distinguishedName : CN=Domain Users,CN=Users,DC=Fabrikam,DC=com
GroupCategory     : Security
GroupScope        : Global
name              : Domain Users
objectClass       : group
objectGUID        : 86c0f0d5-8b4d-4f35-a867-85a006b92902
SamAccountName    : Domain Users
SID               : S-1-5-21-41432690-3719764436-1984117282-513

distinguishedName : CN=Administrators,CN=Builtin,DC=Fabrikam,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
name              : Administrators
objectClass       : group
objectGUID        : 02ce3874-dd86-41ba-bddc-013f34019978
SamAccountName    : Administrators
SID               : S-1-5-32-544

distinguishedName : CN=Schema Admins,CN=Users,DC=Fabrikam,DC=com
GroupCategory     : Security
GroupScope        : Universal
name              : Schema Admins
objectClass       : group
objectGUID        : 8d62890f-385e-4cfa-9b2a-c72576097583
SamAccountName    : Schema Admins
SID               : S-1-5-21-41432690-3719764436-1984117282-518

distinguishedName : CN=Enterprise Admins,CN=Users,DC=Fabrikam,DC=com
GroupCategory     : Security
GroupScope        : Universal
name              : Enterprise Admins
objectClass       : group
objectGUID        : 0215b0a5-aea1-40da-b598-720efe930ddf
SamAccountName    : Enterprise Admins
SID               : S-1-5-21-41432690-3719764436-1984117282-519

distinguishedName : CN=Domain Admins,CN=Users,DC=Fabrikam,DC=com
GroupCategory     : Security
GroupScope        : Global
name              : Domain Admins
objectClass       : group
objectGUID        : 5ccc6037-c2c9-42be-8e92-c8f98afd0011
SamAccountName    : Domain Admins
SID               : S-1-5-21-41432690-3719764436-1984117282-512

distinguishedName : CN=Group Policy Creator Owners,CN=Users,DC=Fabrikam,DC=com
GroupCategory     : Security
GroupScope        : Global
name              : Group Policy Creator Owners
objectClass       : group
objectGUID        : a58f7bf2-fd20-4bbd-96f0-ee10fa1613c7
SamAccountName    : Group Policy Creator Owners
SID               : S-1-5-21-41432690-3719764436-1984117282-520
```

这个命令可以获取管理员的所有组成员身份信息。

### 示例 3：获取资源域中某个账户的组成员身份信息
```
PS C:\> Get-ADPrincipalGroupMembership -Identity Administrator -ResourceContextServer ChildDomain.Fabrikam.Com -ResourceContextPartition "DC=Fabrikam,DC=com"


distinguishedName : CN=Domain Users,CN=Users,DC=Fabrikam,DC=com
GroupCategory     : Security
GroupScope        : Global
name              : Domain Users
objectClass       : group
objectGUID        : 86c0f0d5-8b4d-4f35-a867-85a006b92902
SamAccountName    : Domain Users
SID               : S-1-5-21-41432690-3719764436-1984117282-513

distinguishedName : CN=Group Policy Creator Owners,CN=Users,DC=Fabrikam,DC=com
GroupCategory     : Security
GroupScope        : Global
name              : Group Policy Creator Owners
objectClass       : group
objectGUID        : a58f7bf2-fd20-4bbd-96f0-ee10fa1613c7
SamAccountName    : Group Policy Creator Owners
SID               : S-1-5-21-41432690-3719764436-1984117282-520

distinguishedName : CN=Enterprise Admins,CN=Users,DC=Fabrikam,DC=com
GroupCategory     : Security
GroupScope        : Universal
name              : Enterprise Admins
objectClass       : group
objectGUID        : 0215b0a5-aea1-40da-b598-720efe930ddf
SamAccountName    : Enterprise Admins
SID               : S-1-5-21-41432690-3719764436-1984117282-519

distinguishedName : CN=Schema Admins,CN=Users,DC=Fabrikam,DC=com
GroupCategory     : Security
GroupScope        : Universal
name              : Schema Admins
objectClass       : group
objectGUID        : 8d62890f-385e-4cfa-9b2a-c72576097583
SamAccountName    : Schema Admins
SID               : S-1-5-21-41432690-3719764436-1984117282-518

distinguishedName : CN=Domain Admins,CN=Users,DC=Fabrikam,DC=com
GroupCategory     : Security
GroupScope        : Global
name              : Domain Admins
objectClass       : group
objectGUID        : 5ccc6037-c2c9-42be-8e92-c8f98afd0011
SamAccountName    : Domain Admins
SID               : S-1-5-21-41432690-3719764436-1984117282-512

distinguishedName : CN=Administrators,CN=Builtin,DC=Fabrikam,DC=com
GroupCategory     : Security
GroupScope        : DomainLocal
name              : Administrators
objectClass       : group
objectGUID        : 02ce3874-dd86-41ba-bddc-013f34019978
SamAccountName    : Administrators
SID               : S-1-5-32-544
```

此命令会获取管理员账户在资源域ChildDomain.Fabrikam.Com中所属的所有组成员信息。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值为：

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

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Active Directory PowerShell提供程序驱动器运行的；如果是从此类驱动器运行，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果该执行任务的账户没有目录级别的权限，Active Directory PowerShell 会返回一个终止错误（即无法继续执行任务）。

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
通过提供以下属性值之一来指定一个 Active Directory 主体对象。括号中的标识符是该属性在轻型目录访问协议（LDAP）中的显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索目标对象。如果找到两个或多个对象，该cmdlet会返回一个无法终止的错误信息。

这个参数也可以通过管道来获取该对象，或者你可以将该参数设置为一个对象实例。

派生类型也是被接受的，例如以下这些类型：

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

### -Partition
Specifies the distinguished name of an Active Directory partition.
The distinguished name must be one of the naming contexts on the current directory server.
The cmdlet searches this partition to find the object defined by the **Identity** parameter.

In many cases, a default value is used for the **Partition** parameter if no value is specified.
The rules for determining the default value are given below.
Note that rules listed first are evaluated first and once a default value can be determined, no further rules are evaluated.

In Active Directory Domain Services (AD DS) environments, a default value for **Partition** is set in the following cases:

- If the **Identity** parameter is set to a distinguished name, the default value of **Partition** is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of **Partition** is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of **Partition** is set to the default partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for **Partition** is set in the following cases:

- If the **Identity** parameter is set to a distinguished name, the default value of **Partition** is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of **Partition** is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of **Partition** is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the **Partition** parameter does not take any default value.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: DefaultNC; Provider: The default is to use the Partition that you are currently in. Otherwise, use DefaultNC (that is, if you are in the RootDSE)
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourceContextPartition
Specifies the distinguished name of the partition of an AD or AD LDS instance to search.
Use this parameter with the *ResourceContextServer* parameter to specify a partition hosted by the specified server.
If the *ResourceContextPartition* parameter is not specified, the default partition of the *ResourceContextServer* is searched.

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

### -ResourceContextServer
Specifies that the cmdlet return a list of groups that the user is a member of and that reside in the specified domain.
Use this parameter to search for groups in a domain that is not the domain where the user's account resides.
To search a partition other than the default partition in this domain, also specify the *ResourceContextPartition* parameter.

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
默认的认证方法是“Negotiate”。

基本身份验证方法需要使用安全套接字层（SSL）连接。

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

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### Microsoft.ActiveDirectory.Management.ADPrincipal
A principal object that represents a user, computer or group is received by the *Identity* parameter.
Derived types, such as the following are also received by this parameter:

- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADGroup**

## 输出

### Microsoft.ActiveDirectory.Management.ADGroup
返回那些包含指定用户、计算机、组或服务账户作为成员的群组对象。

`Get-ADPrincipalGroupMembership` cmdlet 返回一组默认的 `ADGroup` 属性值。若要获取更多的 `ADGroup` 属性信息，需将该 cmdlet 生成的 `ADGroups` 对象通过管道传递给 `Get-ADGroup` 命令。可以通过向 `Get-ADGroup` 命令传递 `-Properties` 参数来指定所需从组对象中获取的额外属性。

## 备注
* This cmdlet does not work with an Active Directory snapshot.

## 相关链接

[Add-ADGroupMember](./Add-ADGroupMember.md)

[Add-ADPrincipalGroupMembership](./Add-ADPrincipalGroupMembership.md)

[Get-ADComputer](./Get-ADComputer.md)

[Get-ADGroup](./Get-ADGroup.md)

[Get-ADGroupMember](./Get-ADGroupMember.md)

[Get-ADUser](./Get-ADUser.md)

[Remove-ADGroupMember](./Remove-ADGroupMember.md)

[Remove-ADPrincipalGroupMembership](./Remove-ADPrincipalGroupMembership.md)

