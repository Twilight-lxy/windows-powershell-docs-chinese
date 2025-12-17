---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADGroup
---

# 新AD组

## 摘要
创建一个 Active Directory 组。

## 语法

```
New-ADGroup [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Description <String>]
 [-DisplayName <String>] [-GroupCategory <ADGroupCategory>] [-GroupScope] <ADGroupScope> [-HomePage <String>]
 [-Instance <ADGroup>] [-ManagedBy <ADPrincipal>] [-Name] <String> [-OtherAttributes <Hashtable>] [-PassThru]
 [-Path <String>] [-SamAccountName <String>] [-Server <String>] [<CommonParameters>]
```

## 描述
`New-ADGroup` cmdlet 用于创建一个 Active Directory 组对象。许多对象的属性是通过设置 cmdlet 参数来定义的；那些无法通过 cmdlet 参数设置的属性，则可以使用 `OtherAttributes` 参数来进行配置。

`Name` 和 `GroupScope` 参数用于指定组的名称和范围，创建新组时这些参数是必需的。通过设置 `GroupType` 参数，您可以定义该新组是属于安全组还是分布组。`Path` 参数则指定了该组所属的容器或组织单元（OU）。

以下方法介绍了使用此cmdlet创建对象的不同方式。

方法 1：使用 `New-ADGroup` cmdlet，指定所需的参数，并通过该 cmdlet 的参数来设置任何额外的属性值。

方法 2：使用模板来创建新对象。为此，可以创建一个新的组对象或获取现有组对象的副本，并将 **Instance** 参数设置为该对象。传递给 **Instance** 参数的对象将作为新对象的模板。您可以通过设置 cmdlet 参数来覆盖模板中的属性值。有关更多信息，请参阅此 cmdlet 的 **Instance** 参数描述。

方法 3：使用 `Import-Csv` cmdlet 和 `New-ADGroup` cmdlet 来创建多个 Active Directory 组对象。具体操作如下：首先使用 `Import-CSV` cmdlet 从包含对象属性列表的逗号分隔值（CSV）文件中导入这些自定义对象；接着将这些对象传递给 `New-ADGroup` cmdlet，从而创建相应的组对象。

## 示例

### 示例 1：创建一个组并设置其属性
```
PS C:\> New-ADGroup -Name "RODC Admins" -SamAccountName RODCAdmins -GroupCategory Security -GroupScope Global -DisplayName "RODC Administrators" -Path "CN=Users,DC=Fabrikam,DC=Com" -Description "Members of this group are RODC Administrators"
```

此命令在容器 CN=Users,DC=Fabrikam,DC=Com 中创建一个名为 RODC Admins 的组，并为新对象设置 **GroupCategory**（组类别）、**DisplayName**（组显示名称）、**GroupScope**（组范围）和 **Description**（组描述）属性。

### 示例 2：使用现有的属性值创建一个组
```
PS C:\> Get-ADGroup FabrikamBranch1 -Properties Description | New-ADGroup -Name "Branch1Employees" -SamAccountName "Branch1Employees" -GroupCategory Distribution -PassThru
GroupScope        : Universal
Name              : Branch1Employees
GroupCategory     : Distribution
SamAccountName    : Branch1Employees
ObjectClass       : group
ObjectGUID        : 8eebce44-5df7-4bed-a98b-b987a702103e
SID               : S-1-5-21-41432690-3719764436-1984117282-1117
DistinguishedName : CN=Branch1Employees,CN=Users,DC=Fabrikam,DC=com
```

这个命令使用当前组的属性值来创建一个新的组。

### 示例 3：在 LDS 实例上创建一个组
```
PS C:\> New-ADGroup -Server localhost:60000 -Path "OU=AccountDeptOU,DC=AppNC" -Name "AccountLeads" -GroupScope DomainLocal -GroupCategory Distribution
```

此命令在 AD LDS 实例上创建一个名为 AccountLeads 的组。

## 参数

### -AuthType
指定要使用的身份验证方法。此参数的可接受值为：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的提供程序驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

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

### -Description
用于指定对象的描述信息。该参数用于设置对象의 **Description** 属性的值。轻量级目录访问协议（LDAP）中此属性的显示名称（**ldapDisplayName**）为 “description”。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DisplayName
指定对象的显示名称。此参数用于设置对象的 **DisplayName** 属性。该属性的 LDAP 显示名称（**ldapDisplayName**）为 “displayName”。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -GroupCategory
指定该组的类别。此参数的可接受值包括：

- Distribution or 0
- Security or 1

此参数用于设置组的 `GroupCategory` 属性。该参数值与其他组属性相结合，用于设置 LDAP 显示名称（`ldapDisplayName`）属性，该属性的名称为 `groupType`。

```yaml
Type: ADGroupCategory
Parameter Sets: (All)
Aliases:
Accepted values: Distribution, Security

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -GroupScope
指定组的范围（即组所属的“群组级别”）。该参数的可接受值为：

- DomainLocal or 0
- Global or 1
- Universal or 2

该参数将组对象的 **GroupScope** 属性设置为指定的值。此属性在 LDAP 中的显示名称为 groupType。

```yaml
Type: ADGroupScope
Parameter Sets: (All)
Aliases:
Accepted values: DomainLocal, Global, Universal

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -HomePage
指定对象主页的URL。此参数用于设置Active Directory对象的`homePage`属性。该属性的LDAP显示名称（`ldapDisplayName`）为“wwWWHomePage”。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Instance
指定一个组对象的实例，用作新组对象的模板。

你可以使用现有的组对象实例作为模板，或者通过使用 Windows PowerShell 命令行或脚本来创建一个新的组对象。

方法 1：使用现有的组对象作为新对象的模板。首先使用 **Get-ADGroup** cmdlet 获取一个组对象，然后将该对象传递给 **New-ADGroup** cmdlet 的 *Instance* 参数以创建一个新的组对象。你可以通过设置相应的参数来覆盖新对象的属性值。

方法 2：创建一个新的 **ADGroup** 对象，并使用 Windows PowerShell 命令行界面设置相应的属性值。然后将这个对象传递给 **New-ADGroup** cmdlet 的 *Instance* 参数，以创建新的组对象。

注意：指定的属性不会被验证；因此，尝试设置不存在或无法设置的属性会引发错误。

```yaml
Type: ADGroup
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagedBy
通过提供以下属性值之一来指定管理该对象的用户或组。注意：括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- SAM account name (sAMAccountName)

```yaml
Type: ADPrincipal
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定对象的名称。此参数用于设置 Active Directory 对象的 **Name** 属性。该属性的 LDAP 显示名称（**ldapDisplayName**）即为“name”。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -OtherAttributes
用于指定那些未通过 cmdlet 参数表示的对象属性的值。您可以使用此参数同时设置一个或多个属性值。如果某个属性支持多个值，您可以为其分配多个值。要识别某个属性，请使用在 Active Directory 架构中为该属性定义的 LDAP 显示名称（**ldapDisplayName**）来进行标识。

要为某个属性指定一个单独的值：

`-其他属性 @{'AttributeLDAPDisplayName'=值}`

要为某个属性指定多个值

`-其他属性 @{'AttributeLDAPDisplayName'=value1, value2,...}`

您可以使用分号（;）来分隔多个属性，从而为这些属性指定相应的值。以下语法展示了如何为多个属性设置值：

`-其他属性 @{'Attribute1LDAPDisplayName'=值; 'Attribute2LDAPDisplayName'=值1,值2;...}`

```yaml
Type: Hashtable
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的该项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -Path
指定用于创建新对象的组织单元（Organizational Unit，简称OU）或容器的X.500路径。

在许多情况下，如果未指定任何值，则会为 *Path* 参数使用一个默认值。确定默认值的规则如下所示。请注意，首先列出的规则会被优先评估；一旦确定了默认值，后续的规则将不再被执行。

在 Active Directory 域服务（AD DS）环境中，以下情况下会为“Path”属性设置默认值：

- If the cmdlet is run from an Active Directory module for Windows PowerShell provider drive, the parameter is set to the current path of the provider drive.
- If the cmdlet has a default path, this is used.
For example: in New-ADUser, the *Path* parameter defaults to the Users container.
- If none of the previous cases apply, the default value of *Path* is set to the default partition or naming context of the target domain.

在 Active Directory 轻量级目录服务（AD LDS）环境中，以下情况下会为 *Path* 设置默认值：

- If the cmdlet is run from an Active Directory PowerShell provider drive, the parameter is set to the current path of the provider drive.
- If the cmdlet has a default path, this is used.
For example: in New-ADUser, the *Path* parameter defaults to the Users container.
- If the target AD LDS instance has a default naming context, the default value of *Path* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent (DSA) object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Path* parameter does not take a default value.

注意：Active Directory 提供程序的 cmdlet（如 **New-Item**、**Remove-Item**、**Remove-ItemProperty**、**Rename-Item** 和 **Set-ItemProperty**）也包含一个 **Path** 属性。但是，对于这些提供程序 cmdlet 来说，*Path* 参数标识的是实际对象的路径，而不是容器（与 Active Directory cmdlet 的情况不同）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SamAccountName
指定用户、组、计算机或服务账户的安全账户管理器（Security Account Manager，简称SAM）账户名称。描述字段的最大长度为256个字符。为了与旧版本的操作系统兼容，请创建一个长度不超过20个字符的SAM账户名称。此参数用于设置账户对象的**SAMAccountName**属性。该属性对应的LDAP显示名称（**ldapDisplayName**）即为`sAMAccountName`。

注意：如果提供的字符串值没有以美元符号（$）结尾，系统会在必要时自动添加一个美元符号。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务实例，为此请提供相应的域名或目录服务器之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot instance）。

以下是几种指定 Active Directory 域服务实例的方法：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们在列表中的排列顺序：

- By using the *Server* value from objects passed through the pipeline
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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft ActiveDirectory.Management.AdGroup
通过 **Instance** 参数接收到一个组对象，该对象是新组对象的模板。

## 输出

### 无或 Microsoft ActiveDirectory.Management.AdGroup
当指定*PassThru*参数时，该cmdlet会返回一个新的组对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* This cmdlet does not work with an Active Directory Snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADGroup](./Get-ADGroup.md)

[Remove-ADGroup](./Remove-ADGroup.md)

[Set-ADGroup](./Set-ADGroup.md)

