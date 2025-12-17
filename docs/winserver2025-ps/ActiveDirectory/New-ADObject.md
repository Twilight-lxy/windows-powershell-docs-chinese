---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adobject?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADObject
---

# 新的 AD 对象

## 摘要
创建一个 Active Directory 对象。

## 语法

```
New-ADObject [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Description <String>]
 [-DisplayName <String>] [-Instance <ADObject>] [-Name] <String> [-OtherAttributes <Hashtable>] [-PassThru]
 [-Path <String>] [-ProtectedFromAccidentalDeletion <Boolean>] [-Server <String>] [-Type] <String>
 [<CommonParameters>]
```

## 描述
`New-ADObject` cmdlet 可以创建 Active Directory 对象，例如新的组织单位（OU）或新的用户账户。你可以使用此 cmdlet 创建任何类型的 Active Directory 对象。许多对象的属性是通过设置 cmdlet 参数来定义的；那些未通过 cmdlet 参数设置的属性，则可以通过使用 `OtherAttributes` 参数来进行配置。

您必须设置“名称”（Name）和“类型”（Type）参数才能创建一个新的 Active Directory 对象。“名称”用于指定新对象的名称；“类型”参数则用于指定表示要创建的对象类型的 Active Directory 架构类的轻量级目录访问协议（LDAP）显示名称。常见的“类型”值包括 computer（计算机）、group（组）、OU（组织单元）和 user（用户）。

`Path` 参数用于指定创建对象的容器。如果您不指定 `Path` 参数，该 cmdlet 会在域中 Active Directory 对象的默认命名上下文容器中创建对象。

以下方法解释了使用此cmdlet创建对象的不同方式。

方法 1：使用 **New-ADObject** cmdlet，指定所需的参数，并通过该 cmdlet 的参数设置任何额外的属性值。

方法 2：使用模板来创建新的对象。为此，可以创建一个新的 Active Directory 对象或获取现有 Active Directory 对象的副本，并将 *Instance* 参数设置为该对象。传递给 *Instance* 参数的对象将被用作新对象的模板。您可以通过设置 cmdlet 参数来覆盖模板中的属性值。有关更多信息，请参阅此 cmdlet 的 *Instance* 参数描述。

方法 3：使用 `Import-Csv` cmdlet 和 `New-ADObject` cmdlet 来创建多个 Active Directory 对象。具体操作如下：首先使用 `Import-CSV` cmdlet 从逗号分隔值（CSV）文件中导入对象属性信息，从而创建自定义对象；然后将这些对象传递给 `New-ADObject` cmdlet，以生成实际的 Active Directory 对象。

## 示例

### 示例 1：创建一个子网对象
```
PS C:\> New-ADObject -Name "192.168.1.0/26" -Type "subnet" -Description "192.168.1.0/255.255.255.192" -OtherAttributes @{location="Building A";siteObject="CN=HQ,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM"} -Path "CN=Subnets,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM"
```

该命令在总部站点创建一个具有所描述属性的子网对象。

### 示例 2：通过模板创建子网对象
```
PS C:\> $SubnetTemplate = Get-ADObject -Identity "CN=192.168.1.0/26,CN=Subnets,CN=Sites,CN=Configuration,DC=Fabrikam,DC=com" -Properties description,location
PS C:\> New-ADObject -Instance $SubnetTemplate -Name "192.168.1.0/28" -Type "subnet" -Path "CN=Subnets,CN=Sites,CN=Configuration,DC=FABRIKAM,DC=COM"
```

这个示例创建了一个新的子网对象，使用另一个子网对象作为模板。

### 示例 3：创建一个联系人对象
```
PS C:\> New-ADObject -Name "SaraDavisContact" -Type "contact" -ProtectedFromAccidentalDeletion $True -OtherAttributes @{'msDS-SourceObjectDN'="CN=FabrikamContacts,DC=CONTOSO,DC=COM"}
```

此命令创建一个新的联系人对象，设置 **msDS-SourceObjectDN** 属性，并防止该对象被意外删除。

### 示例 4：创建一个容器对象
```
PS C:\> New-ADObject -Name "Apps" -Type "container" -Path "DC=AppNC" -Server "FABRIKAM-SRV1:60000"
```

此命令在 AD LDS 实例中创建一个名为“Apps”的新容器对象。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值为：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从此类提供程序驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

您也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

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

### -Description
用于指定对象的描述信息。该参数会设置对象中 `Description` 属性的值。此属性的 LDAP 显示名称（`ldapDisplayName`）为 “description”。

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

### -Instance
指定一个 Active Directory 对象的实例，作为创建新 Active Directory 对象的模板使用。

你可以使用现有的 Active Directory 对象的实例作为模板，或者通过使用 Windows PowerShell 命令行或脚本来创建一个新的 Active Directory 对象。

方法 1：使用现有的 Active Directory 对象作为新对象的模板。要获取现有 Active Directory 对象的实例，可以使用诸如 **Get-ADObject** 这样的 cmdlet。然后将该对象传递给 **New-ADObject** cmdlet 的 *Instance* 参数，以创建一个新的 Active Directory 对象。您可以通过设置适当的参数来覆盖新对象的属性值。

方法 2：创建一个新的 **ADObject**，并通过使用 Windows PowerShell 命令行界面来设置属性值。然后将这个对象传递给 **New-ADObject** cmdlet 的 *Instance* 参数，以创建新的 Active Directory 对象。

注意：指定的属性不会被验证；因此，尝试设置不存在或无法设置的属性会引发错误。

```yaml
Type: ADObject
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定对象的名称。此参数用于设置 Active Directory 对象的 **Name** 属性。该属性的 LDAP 显示名称（**ldapDisplayName**）即为指定的名称。

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
用于指定那些无法通过 cmdlet 参数表示的对象属性的值。您可以使用此参数同时设置一个或多个属性值。如果某个属性支持多个值，您可以为其分配多个值。要识别某个属性，请使用在 Active Directory 架构中为其定义的 LDAP 显示名称（**ldapDisplayName**）来进行标识。

要为某个属性指定一个单一的值：

`-其他属性 @{'AttributeLDAPDisplayName'=值}`

要为某个属性指定多个值：

`-其他属性 @{'AttributeLDAPDisplayName'=值1, 值2, ...}`

要为多个属性指定值：

`-其他属性 @{'Attribute1LDAPDisplayName'=值; 'Attribute2LDAPDisplayName'=值1,值2;...}'`

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
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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
指定用于创建新对象的OU（组织单位）或容器的X.500路径。

在许多情况下，如果未指定值，则会为 *Path* 参数使用默认值。确定默认值的规则如下所示。请注意，首先列出的规则会被优先评估；一旦确定了默认值，后续的规则将不再被评估。

在 Active Directory Domain Services (AD DS) 环境中，以下情况下会为 “Path”（路径）字段设置一个默认值：

- If the cmdlet is run from an Active Directory PowerShell provider drive, the parameter is set to the current path of the provider drive.
- If the cmdlet has a default path, this is used.
For example: in New-ADUser, the *Path* parameter defaults to the Users container.
- If none of the previous cases apply, the default value of *Path* is set to the default partition or naming context of the target domain.

在 AD LDS 环境中，在以下情况下会为 *Path* 设置一个默认值：

- If the cmdlet is run from an Active Directory module for PowerShell provider drive, the parameter is set to the current path of the provider drive.
- If the cmdlet has a default path, this is used.
For example: in New-ADUser, the *Path* parameter defaults to the Users container.
- If the target AD LDS instance has a default naming context, the default value of *Path* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Path* parameter does not take any default value.

注意：Active Directory Provider 的 cmdlet（如 **New-Item**、**Remove-Item**、**Remove-ItemProperty**、**Rename-Item** 和 **Set-ItemProperty**）也包含一个 *Path* 属性。但对于这些 cmdlet 来说，*Path* 参数标识的是实际对象的路径，而不是容器的路径。

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

### -ProtectedFromAccidentalDeletion
指定是否阻止对象被删除。当该属性设置为 `true` 时，不更改该属性的值就无法删除相应的对象。此参数的可接受值为：

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务（AD DS）实例，为此需提供一个对应的域名或目录服务器的值。该服务可以是以下类型中的任意一种：Active Directory 轻量级目录服务（AD LDS）、AD DS 或 Active Directory 快照实例。

以下是指定 AD DS 实例的几种方式：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的列出顺序：

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

### -Type
指定要创建的对象类型。将 *Type* 参数设置为表示所需创建对象类型的 Active Directory 架构类的 LDAP 显示名称。类型值的示例包括 user（用户）、computer（计算机）和 group（组）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft.ActiveDirectory.Management.ADObject
`Instance` 参数接收一个 Active Directory 对象，该对象是新对象的模板。

派生类型也是被接受的，例如以下这些：

- **Microsoft.ActiveDirectory.Management.ADPartition**
- **Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy**
- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**

## 输出

### 无值或 Microsoft.ActiveDirectory.Management.ADObject
当指定 *PassThru* 参数时，该命令会返回一个新的 Active Directory 对象。默认情况下，此 cmdlet 不会生成任何输出。

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADObject](./Get-ADObject.md)

[Move-ADObject](./Move-ADObject.md)

[Remove-ADObject](./Remove-ADObject.md)

[重命名 AD 对象](./Rename-ADObject.md)

[Restore-ADObject](./Restore-ADObject.md)

[Set-ADObject](./Set-ADObject.md)

[Sync-ADObject](./Sync-ADObject.md)

