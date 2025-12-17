---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adgroupmember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADGroupMember
---

# Get-ADGroupMember

## 摘要
获取Active Directory组的成员信息。

## 语法

```
Get-ADGroupMember [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Identity] <ADGroup>
 [-Partition <String>] [-Recursive] [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADGroupMember` cmdlet 可用于获取 Active Directory 组的成员信息。这些成员可以是用户、组或计算机。

`Identity` 参数用于指定要访问的 Active Directory 组。您可以通过组的 distinguished name（唯一名称）、GUID、安全标识符或 Security Account Manager (SAM) 账户名来识别该组。此外，您也可以通过将组对象传递到管道中来指定该组。例如，您可以使用 `Get-ADGroup` cmdlet 获取一个组对象，然后将该对象传递给 `Get-ADGroupMember` cmdlet。

如果指定了 `Recursive` 参数，该 cmdlet 会获取组层次结构中不包含子对象的所有成员。例如，如果组 SaraDavisReports 包含用户 KarenToh，而组 JohnSmithReports 包含用户 JoshPollock，那么该 cmdlet 将返回 KarenToh 和 JoshPollock。

对于 Active Directory 轻量级目录服务（AD LDS）环境，除非满足以下两种情况，否则必须指定 *Partition* 参数：

- The cmdlet is run from an Active Directory provider drive.
- A default naming context or partition is defined for the AD LDS environment.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.

## 示例

### 示例 1：获取某个小组的所有成员
```
PS C:\> Get-ADGroupMember
cmdlet Get-ADGroupMember at command pipeline position 1
Supply values for the following parameters: (Type !? for Help.)
Identity: Administrators

distinguishedName : CN=Domain Admins,CN=Users,DC=Fabrikam,DC=com
name              : Domain Admins
objectClass       : group
objectGUID        : 5ccc6037-c2c9-42be-8e92-c8f98afd0011
SamAccountName    : Domain Admins
SID               : S-1-5-21-41432690-3719764436-1984117282-512

distinguishedName : CN=Enterprise Admins,CN=Users,DC=Fabrikam,DC=com
name              : Enterprise Admins
objectClass       : group
objectGUID        : 0215b0a5-aea1-40da-b598-720efe930ddf
SamAccountName    : Enterprise Admins
SID               : S-1-5-21-41432690-3719764436-1984117282-519

distinguishedName : CN=LabAdmin,CN=Users,DC=Fabrikam,DC=com
name              : LabAdmin
objectClass       : user
objectGUID        : ab7c269d-aec5-4fcc-aebe-6cd1a2e6cd53
SamAccountName    : LabAdmin
SID               : S-1-5-21-41432690-3719764436-1984117282-1000

distinguishedName : CN=Administrator,CN=Users,DC=Fabrikam,DC=com
name              : Administrator
objectClass       : user
objectGUID        : 994f46e6-c62c-483f-a6cf-124197b6a959
SamAccountName    : Administrator
SID               : S-1-5-21-41432690-3719764436-1984117282-500
```

这个命令可以获取“Administrators”组中的所有成员。

### 示例 2：获取所有域本地组的所有组成员
```
PS C:\> Get-ADGroup -Server localhost:60000 -Filter "GroupScope -eq 'DomainLocal'" -SearchBase "DC=AppNC" | Get-ADGroupMember -Partition "DC=AppNC"
distinguishedName : CN=SanjayPatel,OU=AccountDeptOU,DC=AppNC
name              : SanjayPatel
objectClass       : user
objectGUID        : d671de28-6e40-42a7-b32c-63d336de296d
SamAccountName    :
SID               : S-1-510474493-936115905-2231798853-1260534229-4171027843-767619944
```

此命令会获取AD LDS实例中所有域本地组的组成员信息。

### 示例 3：获取所有管理员组成员
```
PS C:\> Get-ADGroupMember -Identity Administrators
distinguishedName : CN=Domain Admins,CN=Users,DC=Fabrikam,DC=com
name              : Domain Admins
objectClass       : group
objectGUID        : 5ccc6037-c2c9-42be-8e92-c8f98afd0011
SamAccountName    : Domain Admins
SID               : S-1-5-21-41432690-3719764436-1984117282-512

distinguishedName : CN=Enterprise Admins,CN=Users,DC=Fabrikam,DC=com
name              : Enterprise Admins
objectClass       : group
objectGUID        : 0215b0a5-aea1-40da-b598-720efe930ddf
SamAccountName    : Enterprise Admins
SID               : S-1-5-21-41432690-3719764436-1984117282-519

distinguishedName : CN=LabAdmin,CN=Users,DC=Fabrikam,DC=com
name              : LabAdmin
objectClass       : user
objectGUID        : ab7c269d-aec5-4fcc-aebe-6cd1a2e6cd53
SamAccountName    : LabAdmin
SID               : S-1-5-21-41432690-3719764436-1984117282-1000

distinguishedName : CN=Administrator,CN=Users,DC=Fabrikam,DC=com
name              : Administrator
objectClass       : user
objectGUID        : 994f46e6-c62c-483f-a6cf-124197b6a959
SamAccountName    : Administrator
SID               : S-1-5-21-41432690-3719764436-1984117282-500
```

这个命令可以获取“Administrators”组中的所有成员信息。

### 示例 4：获取某个组的成员信息，包括该组下属子组的成员信息
```
PS C:\> Get-ADGroupMember -Identity "Enterprise Admins" -Recursive
distinguishedName : CN=Administrator,CN=Users,DC=Fabrikam,DC=com
name              : Administrator
objectClass       : user
objectGUID        : 994f46e6-c62c-483f-a6cf-124197b6a959
SamAccountName    : Administrator
SID               : S-1-5-21-41432690-3719764436-1984117282-500

distinguishedName : CN=Sagiv Hadaya,CN=Users,DC=Fabrikam,DC=com
name              : Sagiv Hadaya
objectClass       : user
objectGUID        : 64706230-f179-4fe4-b8c9-f0d334e66ab1
SamAccountName    : SHadaya
SID               : S-1-5-21-41432690-3719764436-1984117282-1158
```

这个命令可以获取“Enterprise Admins”组中的所有成员，包括该组下的所有子组中的成员。

## 参数

### -AuthType
指定要使用的认证方法。此参数的可接受值包括：

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

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Windows PowerShell提供程序的Active Directory模块驱动器中运行的。如果该cmdlet是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定这个参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

如果执行该任务的账号没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A Security Account Manager account name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该cmdlet会返回一个“非终止性错误”（即无法继续执行的错误）。

这个参数也可以通过管道来获取该对象，或者你可以将这个参数设置为一个对象实例。

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
用于指定 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器上支持的命名上下文之一。此 cmdlet 会在该分区中搜索由 *Identity* 参数所定义的对象。

在许多情况下，如果未指定 `Partition` 参数的值，系统会使用一个默认值。确定默认值的规则如下所示。请注意，列出的规则会按顺序依次进行评估；一旦确定了默认值，就不会再继续评估其他规则了。

在 Active Directory 域服务（AD DS）环境中，在以下情况下会为“分区”（Partition）设置一个默认值：

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

### -Recursive
该命令指定了 `get` cmdlet 应获取组层次结构中所有不包含子对象的成员。

如果指定的组没有任何成员，那么将不会返回任何内容。

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
用于指定要连接的 AD DS 实例，方法是为相应的域名或目录服务器提供一个以下值之一。该服务可以是以下类型中的任意一种：AD LDS、AD DS 或 Active Directory 快照实例。

以下是指定 AD DS 实例的几种方式：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft.ActiveDirectory.Management.ADGroup
一个组对象通过 *Identity* 参数被接收。

## 输出

### Microsoft ActiveDirectory.Management.AdPrincipal
返回一个或多个主要对象，这些对象代表属于指定组的用户、计算机或组。

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work when a group has members located in a different forest, and the forest does not have Active Directory Web Service running.

## 相关链接

[Add-ADGroupMember](./Add-ADGroupMember.md)

[Add-ADPrincipalGroupMembership](./Add-ADPrincipalGroupMembership.md)

[Get-ADGroup](./Get-ADGroup.md)

[Get-ADPrincipalGroupMembership](./Get-ADPrincipalGroupMembership.md)

[Remove-ADGroupMember](./Remove-ADGroupMember.md)

[Remove-ADPrincipalGroupMembership](./Remove-ADPrincipalGroup Membership.md)

