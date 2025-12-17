---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adcentralaccessrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADCentralAccessRule
---

# 新的 ADCentral 访问规则

## 摘要
在 Active Directory 中创建一条中央访问规则。

## 语法

```
New-ADCentralAccessRule [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-CurrentAcl <String>] [-Description <String>] [-Instance <ADCentralAccessRule>] [-Name] <String> [-PassThru]
 [-ProposedAcl <String>] [-ProtectedFromAccidentalDeletion <Boolean>] [-ResourceCondition <String>]
 [-Server <String>] [<CommonParameters>]
```

## 描述
`New-ADCentralAccessRule` cmdlet 用于在 Active Directory 中创建中央访问规则。

## 示例

### 示例 1：创建一个新的命名中央访问规则
```
PS C:\> New-ADCentralAccessRule -Name "Finance Documents Rule"
```

此命令创建了一条新的中央访问规则，名为“Finance Documents Rule”。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值为：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果是从这样的驱动器中运行该 cmdlet，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该cmdlet会要求您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

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

### -CurrentAcl
指定该规则当前生效的访问控制列表。

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

### -Description
用于指定对象的描述信息。该参数会设置对象中 **Description** 属性的值。在轻量级目录访问协议（LDAP）中，此属性的显示名称（**ldapDisplayName**）为 “description”。

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
指定一个 Active Directory 对象的实例，作为创建新的 Active Directory 对象的模板使用。

你可以使用现有的 Active Directory 对象作为一个模板，或者通过使用 Windows PowerShell 命令行或脚本来创建一个新的 Active Directory 对象。

方法1：使用现有的Active Directory对象作为新对象的模板。要获取现有Active Directory对象的实例，可以使用诸如**Get-ADObject**之类的cmdlet。然后将该对象提供给New-ADObject cmdlet的*Instance*参数，以创建一个新的Active Directory对象。你可以通过设置相应的参数来覆盖新对象的属性值。

方法 2：创建一个新的 **ADObject**，并使用 Windows PowerShell 命令行界面设置属性值。然后将这个对象传递给 New-ADObject cmdlet 的 *Instance* 参数，以创建新的 Active Directory 对象。

注意：指定的属性不会被进行验证；因此，尝试设置不存在或无法设置的属性将会引发错误。

```yaml
Type: ADCentralAccessRule
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定对象的名称。此参数用于设置 Active Directory 对象的 **Name** 属性。该属性的 LDAP 显示名称（**ldapDisplayName**）即为对象的实际名称。

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

### -PassThru
返回一个表示您当前正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -ProposedAcl
此参数指定了规则中建议使用的访问控制列表。

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
指定是否阻止对象的删除。当此属性设置为 `true` 时，不更改该属性的值就无法删除相应的对象。此参数的允许取值为：

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

### -ResourceCondition
此参数指定了规则所关联的资源状态（即资源所处的条件）。

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
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下是指定 Active Directory 域服务实例的几种方式：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

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
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft.ActiveDirectory.Management.ADCentralAccessRule
通过 `Instance` 参数接收到一个 Active Directory 对象，该对象是新对象的模板。

## 输出

### 无值或 Microsoft.ActiveDirectory.Management.ADCentralAccessRule
当指定*PassThru*参数时，会返回一个新的中央访问规则对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADCentralAccessRule](./Get-ADCentralAccessRule.md)

[Remove-ADCentralAccessRule](./Remove-ADCentralAccessRule.md)

[Set-ADCentralAccessRule](./Set-ADCentralAccessRule.md)

[Windows PowerShell中的AD DS管理命令集](./activedirectory.md)

