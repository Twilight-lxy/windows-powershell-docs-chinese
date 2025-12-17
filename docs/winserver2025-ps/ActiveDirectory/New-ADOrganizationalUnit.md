---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADOrganizationalUnit
---

# 新的 Active Directory 组织单元

## 摘要

创建一个 Active Directory 组织单位。

## 语法

```
New-ADOrganizationalUnit [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-City <String>] [-Country <String>]
 [-Credential <PSCredential>] [-Description <String>] [-DisplayName <String>]
 [-Instance <ADOrganizationalUnit>] [-ManagedBy <ADPrincipal>] [-Name] <String> [-OtherAttributes <Hashtable>]
 [-PassThru] [-Path <String>] [-PostalCode <String>] [-ProtectedFromAccidentalDeletion <Boolean>]
 [-Server <String>] [-State <String>] [-StreetAddress <String>] [<CommonParameters>]
```

## 描述

`New-ADOrganizationalUnit` cmdlet 用于创建 Active Directory 组织单位（OU）。您可以使用 cmdlet 参数来设置常用的 OU 属性值。那些未与 cmdlet 参数关联的属性值，则可以通过 `OtherAttributes` 参数来进行设置。

您必须设置 *Name* 参数才能创建一个新的组织单元（OU）。如果您不指定 *Path* 参数，该cmdlet将在域的默认命名上下文（NC）下创建一个OU。

以下方法描述了如何使用此cmdlet来创建一个对象。

方法 1：使用 `New-ADOrganizationalUnit` cmdlet，指定所需的参数，并通过该 cmdlet 的参数设置任何额外的属性值。

方法 2：使用模板来创建新对象。为此，可以创建一个新的组织单元（OU）对象，或者获取一个现有 OU 对象的副本，并将 *Instance* 参数设置为该对象。传递给 *Instance* 参数的对象将作为新对象的模板。您可以通过设置 cmdlet 参数来覆盖模板中的属性值。有关更多信息，请参阅该 cmdlet 的 *Instance* 参数说明。

方法 3：使用 `Import-Csv` cmdlet 和 `New-ADOrganizationalUnit` cmdlet 来创建多个 Active Directory 组织单位（OU）对象。具体操作如下：首先使用 `[Import-Csv](/powershell/module/microsoft.powershellutility/import-csv)` cmdlet 从包含对象属性列表的逗号分隔值（CSV）文件中导入这些自定义对象；然后将这些对象传递给 `New-ADOrganizationalUnit` cmdlet，从而创建相应的 OU 对象。

## 示例

### 示例 1：创建一个组织单位（OU）

```
PS C:\> New-ADOrganizationalUnit -Name "UserAccounts" -Path "DC=FABRIKAM,DC=COM"
```

此命令创建了一个名为 UserAccounts 的组织单元（OU），该组织单元受到保护，以防止被意外删除。请注意，这种“意外删除的保护”是默认启用的（即它是隐式的）。

### 示例 2：创建一个不会被意外删除的保护组（OU）

```
PS C:\> New-ADOrganizationalUnit -Name "UserAccounts" -Path "DC=FABRIKAM,DC=COM" -ProtectedFromAccidentalDeletion $False
```

这个命令创建了一个名为“UserAccounts”的组织单元（Organizational Unit，简称OU），该OU没有采取任何保护措施来防止被意外删除。

### 示例 3：创建一个受保护的组织单位（OU），以防止其被意外删除

```
PS C:\> New-ADOrganizationalUnit -Name "UserAccounts" -Path "DC=FABRIKAM,DC=COM" -OtherAttributes @{seeAlso="CN=HumanResourceManagers,OU=Groups,OU=Managed,DC=Fabrikam,DC=com";managedBy="CN=TomC,DC=FABRIKAM,DC=COM"}
```

此命令创建了一个名为 UserAccounts 的组织单元（OU），该组织单元受到保护，以防被意外删除。**seeAlso** 和 **managedBy** 属性被设置为指定的值。

#### 示例 4：根据模板组织单元（OU）创建一个新的组织单元

```
PS C:\> $OuTemplate = Get-ADOrganizationalUnit -Identity "OU=UserAccounts,DC=Fabrikam,DC=com" -Properties seeAlso,managedBy
PS C:\> New-ADOrganizationalUnit -Name "TomCReports" -Instance $OuTemplate
```

这个命令使用来自OU“UserAccounts,DC=Fabrikam,DC=com”的数据作为另一个OU的模板。

### 示例 5：在 AD LDS 实例中创建一个组织单元（OU）

```
PS C:\> New-ADOrganizationalUnit -Name "Managed" -Path "DC=AppNC" -Server "FABRIKAM-SRV1:60000"
```

此命令在 AD LDS 实例中创建一个名为“Managed”的组织单位（OU）。

## 参数

### -AuthType

指定要使用的身份验证方法。该参数的可接受值包括：

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

### -City

用于指定城镇或城市的名称。此参数用于设置组织单元（OU）对象的 **City** 属性。该属性在轻量级目录访问协议（LDAP）中的显示名称（**ldapDisplayName**）为 `l`。

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

### -Country

指定国家或地区代码。此参数用于设置组织单元（OU）对象的“Country”属性。该属性的LDAP显示名称（**ldapDisplayName**）为“c”。Windows 2000系统不使用这个值。

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

### -Credential

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Active Directory PowerShell 提供程序驱动器运行的。如果该 cmdlet 是从这样的提供程序驱动器运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01/User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

您还可以通过脚本或使用 [Get-Credential](/powershell/module/microsoft.powershell.security/get-credential?view=powershell-7.3) 命令来创建一个 **PSCredential** 对象。之后，可以将 *Credential* 参数设置为该 **PSCredential** 对象。

如果执行任务的账户没有目录级别的权限，Active Directory PowerShell 会返回一个终止错误。

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

用于指定对象的描述信息。此参数会设置组织单元（OU）对象中 **Description** 属性的值。该属性的 LDAP 显示名称（**ldapDisplayName**）为 `description`。

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

指定对象的显示名称。此参数用于设置OU对象的**DisplayName**属性。该属性的LDAP显示名称（**ldapDisplayName**）为`displayName`。

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

指定一个OU（组织单元）对象的实例，用作新OU对象的模板。

你可以使用现有的组织单位（OU）对象的实例作为模板，或者通过使用 Windows PowerShell 命令行或脚本来创建一个新的 OU 对象。

方法 1：使用现有的组织单元（OU）对象作为新对象的模板。要获取现有 OU 对象的实例，可以使用 `Get-ADOrganizationalUnit` 命令。然后将此对象传递给 `New-ADOrganizationalUnit` cmdlet 的 `Instance` 参数，以创建一个新的 OU 对象。您可以通过设置适当的参数来覆盖新对象的属性值。

方法 2：使用 Windows PowerShell 命令行界面创建一个新的 **ADOrganizationalUnit** 对象，并设置相应的属性值。然后将该对象传递给 **New-ADOrganizationalUnit** cmdlet 的 *Instance* 参数，以创建新的 Active Directory 组织单元（OU）对象。

> [注意] > 指定的属性不会经过验证；因此，尝试设置不存在或无法设置的属性会引发错误。

```yaml
Type: ADOrganizationalUnit
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagedBy

通过提供以下属性值之一来指定管理该对象的用户或组。注意：括号中的标识符是该属性的LDAP显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

此参数设置了 Active Directory 属性，并为其指定一个 LDAP 显示名称为 `managedBy`。

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

指定对象的名称。此参数用于设置组织单元（OU）对象的**Name**属性。该属性的LDAP显示名称（**ldapDisplayName**）为`name`。

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

用于指定那些未通过cmdlet参数表示的对象属性的值。您可以使用此参数同时设置一个或多个属性值。如果某个属性支持多个值，您可以为其分配多个数值。要识别某个属性，请使用该属性在Active Directory架构中定义的LDAP显示名称（**ldapDisplayName**）进行标识。

要为某个属性指定一个单一的值：

`-其他属性 @{'AttributeLDAPDisplayName'=值}`

要为某个属性指定多个值，请用逗号将这些值分隔开来：

`-其他属性 @{'AttributeLDAPDisplayName'=value1, value2, ...}`

要为多个属性指定值，请用分号（;）将它们分隔开：

`-其他属性 @{'Attribute1LDAPDisplayName'=值; 'Attribute2LDAPDisplayName'=值1,值2;...'}`

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

返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

指定用于创建新对象的OU（组织单元）或容器的X.500路径。

在许多情况下，如果未指定`Path`参数的值，则会使用默认值。确定默认值的规则如下所述。请注意，列出的规则会按顺序依次被评估；一旦确定了默认值，就不会再继续评估其他规则了。

在 Active Directory 域服务（AD DS）环境中，以下情况下会为“路径”（Path）字段设置默认值：

- If the cmdlet is run from an Active Directory PowerShell provider drive, the parameter is set to the current path of the provider drive.
- If the cmdlet has a default path, this is used. For example: in **New-ADUser**, the *Path* parameter defaults to the Users container.
- If none of the previous cases apply, the default value of *Path* is set to the default partition or naming context of the target domain.

In AD LDS environments, a default value for *Path* is set in the following cases:

- If the cmdlet is run from an Active Directory module for PowerShell provider drive, the parameter is set to the current path of the provider drive.
- If the cmdlet has a default path, this is used. For example: in **New-ADUser**, the *Path* parameter defaults to the Users container.
- If the target AD LDS instance has a default naming context, the default value of *Path* is set to the default naming context.
  To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Path* parameter does not take any default value.

> [!注意] > Active Directory 提供程序的 cmdlet（如 **New-Item**、**Remove-Item**、**Remove-ItemProperty**、**Rename-Item** 和 **Set-ItemProperty**）也包含一个 **Path** 属性。  
> > 但是，对于这些 Active Directory 提供程序的 cmdlet 来说，*Path* 参数指的是实际对象的路径，而不是容器本身的路径。

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

### -PostalCode

用于指定邮政编码或zip代码。该参数用于设置OU对象（Organizational Unit）的`PostalCode`属性。此属性的LDAP显示名称（`ldapDisplayName`）为`postalCode`。

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

表示是否阻止对象被删除。当此属性设置为 `$True` 时，如果不更改该属性的值，则无法删除相应的对象。该参数的可接受值为：

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

指定要连接的 AD DS 实例，为此提供一个相应的域名或目录服务器的值。该服务可以是以下类型中的任意一种：AD LDS、AD DS 或 Active Directory 快照实例。

以下列方式之一指定 AD DS 实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

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

### -State

用于指定一个州或省份。此参数用于设置组织单位（OU）对象的 `State` 属性。该属性的 LDAP 显示名称（`ldapDisplayName`）为 `st`。

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

### -StreetAddress

用于指定街道地址。此参数用于设置组织单元（OU）对象的 **StreetAddress** 属性。该属性的 LDAP 显示名称（**ldapDisplayName**）为 `street`。

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

没有相关对象，或者使用了 `Microsoft.ActiveDirectory.Management.ADOrganizationalUnit` 类。

作为新OU对象模板的OU对象是通过*Instance*参数接收到的。

## 输出

没有相关对象，或者使用了 `Microsoft.ActiveDirectory.Management.ADOrganizationalUnit` 类。

当指定 *PassThru* 参数时，会返回新的组织单位（OU）对象。默认情况下，此 cmdlet 不会生成任何输出。

## 备注

* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADOrganizationalUnit](./Get-ADOrganizationalUnit.md)

[Remove-ADOrganizationalUnit](./Remove-ADOrganizationalUnit.md)

[Set-ADOrganizationalUnit](./Set-ADOrganizationalUnit.md)
