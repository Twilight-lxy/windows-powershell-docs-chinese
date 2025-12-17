---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adresourceproperty?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADResourceProperty
---

# 新AD资源属性

## 摘要
在 Active Directory 中创建一个资源属性。

## 语法

```
New-ADResourceProperty [-WhatIf] [-Confirm] [-AppliesToResourceTypes <String[]>] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Description <String>] [-DisplayName] <String> [-Enabled <Boolean>]
 [-ID <String>] [-Instance <ADResourceProperty>] [-IsSecured <Boolean>] [-OtherAttributes <Hashtable>]
 [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>]
 -ResourcePropertyValueType <ADResourcePropertyValueType> [-Server <String>] [-SharesValuesWith <ADClaimType>]
 [-SuggestedValues <ADSuggestedValueEntry[]>] [<CommonParameters>]
```

## 描述
`New-ADResourceProperty` cmdlet 用于在指定目录中创建一个新的资源属性。

## 示例

### 示例 1：创建一个资源属性
```
PS C:\> New-ADResourceProperty -DisplayName "Authors" -ResourcePropertyValueType MS-DS-MultivaluedText
```

此命令创建了一个资源属性，其显示名称为“Authors”。该资源属性允许指定多位作者的姓名。

### 示例 2：创建一个资源属性以包含建议的值
```
PS C:\> $US = New-Object Microsoft.ActiveDirectory.Management.ADSuggestedValueEntry("US", "United States of America", "United States of America")
PS C:\> $JP = New-Object Microsoft.ActiveDirectory.Management.ADSuggestedValueEntry("JP", "Japan", "Japan")
PS C:\> New-ADResourceProperty -DisplayName "Country" -ResourcePropertyValueType MS-DS-MultivaluedChoice -SuggestedValues $US,$JP
```

此命令创建了一个新的资源属性，其显示名称为“Country”（国家）。建议使用的值分别为“US”（美国）和“JP”（日本）。使用该资源属性的应用程序将允许用户从中选择一个建议的值作为该资源属性的实际值。

### 示例 3：创建一个具有共享值的资源属性
```
PS C:\> New-ADResourceProperty -DisplayName "Country" -ResourcePropertyValueType MS-DS-MultivaluedChoice -SharesValuesWith Country
```

此命令创建了一个参考资源属性，其显示名称为“Country”（国家）。它使用了一个名为“Country”的现有声明类型作为该属性的建议值。这样一来，在中央访问规则中，该资源属性就可以始终与相应的声明类型进行有效比较了。

### 示例 4：创建一个多值文本资源属性
```
PS C:\> New-ADResourceProperty -DisplayName "Authors" -ResourcePropertyValueType MS-DS-MultivaluedText -ID "Authors_60DB20331638"
```

该命令创建了一个资源属性，其显示名称为“Authors”，并将其ID设置为“Authors_60DB20331638”。

在多森林环境中，只有当相同的资源属性需要在所有森林中都正常工作时，才应手动设置该资源的ID。默认情况下，`New-ADResourceProperty`会自动生成ID。为了让资源属性在所有森林中被视为相同，它们的ID必须是相同的。

## 参数

### -AppliesToResourceTypes
指定了该资源属性所适用的资源类型。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AuthType
指定要使用的认证方法。该参数的可接受值为：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Active Directory PowerShell 提供程序驱动器运行的。如果该 cmdlet 是从此类提供程序驱动器运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行该任务的代理账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
指定对象的描述信息。该参数用于设置对象의 **Description** 属性的值。此属性的 LDAP 显示名称（**ldapDisplayName**）即为 “description”。

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
指定资源属性的显示名称。资源属性的显示名称必须是唯一的。

资源属性的显示名称可以在其他 Active Directory cmdlet 中用作标识。例如，如果某个资源属性的显示名称是 “Country”，那么你可以输入 `Get-ADResourceProperty -Identity "Country"` 来获取该资源属性。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Enabled
表示资源属性是否已启用。

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

### -ID
指定资源属性的ID。这是一个可选参数。默认情况下，New-ADResourceProperty会自动生成该ID。

在多森林环境中，只有当需要让相同的资源属性在各个森林中都能正常使用时，才应手动设置资源的ID。为了使这些资源属性在各个森林中被视为相同，它们的ID必须是一致的。

要指定ID，该ID字符串必须符合以下格式：

- Start with a prefix string of one to 15 characters in length.
- The prefix string must be followed by an underscore.
- The prefix string and underscore must be followed by a suffix string of 1 to 16 characters in length.
- All characters contained in either prefix or suffix strings must contain only valid filename characters.

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
指定一个资源属性对象的实例，用作新资源属性对象的模板。

你可以使用现有资源属性对象的实例作为模板，或者通过使用 Windows PowerShell 命令行或脚本来创建一个新的资源属性对象。

方法 1：使用现有的资源属性对象作为新对象的模板。要获取现有资源属性对象的实例，可以使用诸如 **Get-ADResourceProperty** 这样的 cmdlet。然后将该对象传递给 **New-ADResourceProperty** cmdlet 的 *Instance* 参数，以创建一个新的资源属性对象。您可以通过设置相应的参数来覆盖新对象的属性值。

方法 2：创建一个新的 **ADResourceProperty**，并通过使用 Windows PowerShell 命令行界面来设置属性值。然后将这个对象传递给 **New-ADResourceProperty** cmdlet 的 *Instance* 参数，以创建新的资源属性对象。

注意：指定的属性不会被进行验证；因此，如果尝试设置不存在或无法设置的属性，将会引发错误。

```yaml
Type: ADResourceProperty
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsSecured
表示资源属性是否安全。只有安全的资源属性才能用于授权决策或中央访问规则中；不安全的资源属性不能用于这些目的。

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

### -OtherAttributes
用于为那些不是由cmdlet参数表示的属性指定对象属性值。你可以使用此参数同时设置一个或多个参数。如果某个属性支持多个值，你可以为其分配多个值。要识别某个属性，请指定在Active Directory架构中为其定义的LDAPDisplayName（**ldapDisplayName**）。

要为某个属性指定一个单一的值：

`-其他属性 @{'AttributeLDAPDisplayName'=值}'`

要为某个属性指定多个值

`-其他属性 @{'AttributeLDAPDisplayName'=value1, value2, ...}`

你可以使用分号（;）来分隔多个属性，从而为这些属性指定值。以下语法展示了如何为多个属性设置值：

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

### -ProtectedFromAccidentalDeletion
指定是否阻止对象被删除。当此属性设置为 `true` 时，如果不更改该属性的值，则无法删除相应的对象。此参数的可接受值为：

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

### -ResourcePropertyValueType
指定资源属性的值类型。当资源属性被传递给资源管理器（例如文件服务器）时，资源管理器会利用该资源属性的值类型来确定如何处理该属性。

你可以使用 `Get-ADResourceProperty ValueType` cmdlet 来获取资源属性值类型的列表。

以下是Active Directory中可用的内置资源属性值类型列表：

- MS-DS-SinglevaluedChoice
- MS-DS-YesNo
- MS-DS-Number
- MS-DS-DateTime
- MS-DS-OrderedList
- MS-DS-Text
- MS-DS-MultivaluedText
- MS-DS-MultivaluedChoice

```yaml
Type: ADResourcePropertyValueType
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Server
指定要连接的 AD DS 实例，为此需提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型中的任意一种：AD LDS、AD DS 或 Active Directory 快照实例。

请通过以下方式之一指定 AD DS 实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，确定顺序按照列出的顺序进行：

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

### -SharesValuesWith
用于指定引用资源属性。引用资源属性本身不提供推荐的默认值，而是使用该参数中指定的声明类型对象所提供的推荐值。这样一来，该资源属性在中央访问规则中与所引用的声明类型进行比较时，始终能够保持有效性。

```yaml
Type: ADClaimType
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SuggestedValues
为资源属性指定一个或多个建议值。应用程序可以选择向用户展示这份建议值列表供其选择。当 **RestrictValues** 被设置为 `$True` 时，应用程序应限制用户只能从该列表中选取值。

```yaml
Type: ADSuggestedValueEntry[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft.ActiveDirectory.Management.ADResourceProperty

## 输出

### 无或 Microsoft.ActiveDirectory.Management.ADResourceProperty

## 备注
* This cmdlet does not work with an Active Directory Snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADResourceProperty](./Get-ADResourceProperty.md)

[Remove-ADResourceProperty](./Remove-ADResourceProperty.md)

[Set-ADResourceProperty](./Set-ADResourceProperty.md)

