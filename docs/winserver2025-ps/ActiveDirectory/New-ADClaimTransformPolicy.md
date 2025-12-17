---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adclaimtransformpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADClaimTransformPolicy
---

# New-ADClaimTransformPolicy

## 摘要
在 Active Directory 中创建一个新的声明转换策略对象。

## 语法

### AllowAll
```
New-ADClaimTransformPolicy [-WhatIf] [-Confirm] [-AllowAll] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Description <String>] [-Name] <String> [-PassThru]
 [-ProtectedFromAccidentalDeletion <Boolean>] [-Server <String>] [<CommonParameters>]
```

### AllowAllExcept
```
New-ADClaimTransformPolicy [-WhatIf] [-Confirm] -AllowAllExcept <ADClaimType[]> [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Description <String>] [-Name] <String> [-PassThru]
 [-ProtectedFromAccidentalDeletion <Boolean>] [-Server <String>] [<CommonParameters>]
```

### DenyAll
```
New-ADClaimTransformPolicy [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-DenyAll] [-Description <String>] [-Name] <String> [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>]
 [-Server <String>] [<CommonParameters>]
```

### DenyAllExcept
```
New-ADClaimTransformPolicy [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 -DenyAllExcept <ADClaimType[]> [-Description <String>] [-Name] <String> [-PassThru]
 [-ProtectedFromAccidentalDeletion <Boolean>] [-Server <String>] [<CommonParameters>]
```

### 身份证明
```
New-ADClaimTransformPolicy [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Description <String>] [-Instance <ADClaimTransformPolicy>] [-Name] <String> [-PassThru]
 [-ProtectedFromAccidentalDeletion <Boolean>] -Rule <String> [-Server <String>] [<CommonParameters>]
```

## 描述
`New-ADClaimTransformPolicy` cmdlet 用于在 Active Directory 中创建一个新的声明转换策略对象。该声明转换策略对象包含一组用转换规则语言编写的规则。创建策略对象后，您可以将它与森林信任（forest trust）关联起来，以便将该声明转换应用于相应的信任关系中。

## 示例

### 示例 1：按名称创建一个新的声明转换策略，该策略会拒绝所有请求（即拒绝所有的索赔处理）。
```
PS C:\> New-ADClaimTransformPolicy -Name "DenyAllPolicy" -DenyAll
```

此命令创建了一个名为“DenyAllPolicy”的新声明转换策略，该策略会拒绝所有声明，无论是发送的还是接收到的。

### 示例 2：按名称创建一个新的理赔处理策略，并指定排除项
```
PS C:\> New-ADClaimTransformPolicy -Name "AllowAllExceptCompanyAndDepartmentPolicy" -AllowAllExcept Company,Department
```

这个命令创建了一个新的声明转换策略（claims transformation policy），名为 AllowAllExceptCompanyAndDepartmentPolicy。该策略允许发送或接收所有类型的声明，除了 “Company” 和 “Department” 这两个类型的声明之外。

### 示例 3：创建一个新的声明转换策略，用于将现有的名称更改为新的名称
```
PS C:\> New-ADClaimTransformPolicy -Name "HumanResourcesToHrPolicy" -Rule 'C1:[Type=="ad://ext/Department:88ceb0fe88a125db", Value=="Human Resources", ValueType=="string"] => issue(Type=C1.Type, Value="HR", ValueType=C1.ValueType);'
```

此命令创建了一个名为“HumanResourcesToHrPolicy”的新声明转换策略，该策略会将声明中的“Human Resources”字段的值转换为“HR”。

### 示例 4：通过文件中指定的规则，按名称创建一个新的理赔处理策略
```
PS C:\> $Rule = Get-Content C:\rule.txt
PS C:\> New-ADClaimTransformPolicy -Name "MyRule" -Rule $Rule
```

这个示例创建了一个名为“MyRule”的声明转换策略，其规则内容存储在文件C:\rule.txt中。

## 参数

### -AllowAll
这表示该政策设置了一条索赔转换规则，允许所有类型的索赔被发送或接收。

```yaml
Type: SwitchParameter
Parameter Sets: AllowAll
Aliases:
Accepted values: true

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AllowAllExcept
指定一个索赔类型数组。当指定此参数时，策略会设置一条索赔转换规则，允许发送或接收所有类型的索赔，除了那些在数组中指定的索赔类型之外。

```yaml
Type: ADClaimType[]
Parameter Sets: AllowAllExcept
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AuthType
指定要使用的身份验证方法。该参数的可接受值如下：

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
在运行cmdlet之前会提示您进行确认。

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
指定一个具有执行此操作权限的用户账户。默认值为当前用户。

请输入一个用户名，例如 User01 或 Domain01/User01；或者输入一个 **PSCredential** 对象（例如通过 **Get-Credential** cmdlet 生成的对象）。如果输入了用户名，系统会提示您输入密码。

此参数不受任何与 Windows PowerShell 一起安装的提供程序的支持。

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

### -DenyAll
这表示该策略设置了一条索赔转换规则，该规则会拒绝所有发送或接收的索赔请求。

```yaml
Type: SwitchParameter
Parameter Sets: DenyAll
Aliases:
Accepted values: true

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DenyAllExcept
指定一个声明类型数组。当该参数被指定时，策略会设置一条声明转换规则，该规则会拒绝所有发送或接收的声明，除非这些声明属于指定的类型。

```yaml
Type: ADClaimType[]
Parameter Sets: DenyAllExcept
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Description
指定对象的描述信息。此参数用于设置对象의 **Description** 属性的值。在轻量级目录访问协议（LDAP）中，该属性的显示名称（**ldapDisplayName**）为 “description”。

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

### -Instance
指定一个 Active Directory 对象的实例，用作新声明转换策略对象的模板。

你可以使用现有的索赔转换策略对象的实例作为模板，或者通过使用 Windows PowerShell 命令行或脚本来创建一个新的索赔转换策略对象。

方法1：使用现有的声明转换策略对象作为新对象的模板。要获取现有声明转换策略对象的实例，可以使用`Get-ADClaimTransformPolicy`cmdlet。然后将该对象提供给`New-ADClaimTransformPolicy` cmdlet的`Instance`参数，以创建一个新的声明转换策略对象。您可以通过设置相应的参数来覆盖新对象的属性值。

方法 2：创建一个新的 **ADClaimsTransformationPolicy** 对象，并使用 Windows PowerShell 命令行界面设置该对象的属性值。然后将该对象传递给 **New-ADClaimTransformPolicy** cmdlet 的 Instance 参数，以创建新的 Active Directory 对象。

注意：指定的属性不会被进行验证；因此，尝试设置不存在或无法设置的属性将会引发错误。

```yaml
Type: ADClaimTransformPolicy
Parameter Sets: Identity
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定对象的名称。此参数用于设置 Active Directory 对象的 **Name** 属性。该属性的 LDAP 显示名称（**ldapDisplayName**）即为“name”。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
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
指定是否防止对象被删除。当此属性设置为 `$True` 时，除非更改该属性的值，否则无法删除相应的对象。该参数的可接受值包括：

- $False or 0
- $True or 1

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Rule
用于指定声明转换规则。要指定该规则，您可以：（1）将规则输入到一个文本文件中，然后将该文件传递给相应的 cmdlet（推荐这种方式）；或者（2）直接在命令行中输入规则内容。

例如，以下命令演示了如何创建一个新的声明转换策略对象，并使用位于临时文件夹C:\temp中的文本文件Rule.txt中指定的规则。

`$Rule = Get-Content C:\temp\rule.txt`

`New-ADClaimTransformPolicy MyRule -Rule $Rule`

```yaml
Type: String
Parameter Sets: Identity
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

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
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 `Microsoft.ActiveDirectory.Management_ADClaimTransformPolicy`
指定一个声明转换策略对象（claims transformation policy object），该对象是一个模板，用于新声明转换策略对象的创建。这个新策略对象将通过*Instance*参数接收。

## 输出

### 无值或 `Microsoft.ActiveDirectory.Management_ADClaimTransformPolicy`

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADClaimTransformPolicy](./Get-ADClaimTransformPolicy.md)

[Remove-ADClaimTransformPolicy](./Remove-ADClaimTransformPolicy.md)

[Set-ADClaimTransformPolicy](./Set-ADClaimTransformPolicy.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

