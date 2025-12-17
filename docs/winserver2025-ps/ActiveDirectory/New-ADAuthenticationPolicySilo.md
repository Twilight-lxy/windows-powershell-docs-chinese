---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adauthenticationpolicysilo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADAuthenticationPolicySilo
---

# New-ADAuthenticationPolicySilo

## 摘要
创建一个 Active Directory 域服务身份验证策略对象（silo object）。

## 语法

```
New-ADAuthenticationPolicySilo [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-ComputerAuthenticationPolicy <ADAuthenticationPolicy>] [-Credential <PSCredential>] [-Description <String>]
 [-Enforce] [-Instance <ADAuthenticationPolicySilo>] [-Name] <String> [-OtherAttributes <Hashtable>]
 [-PassThru] [-ProtectedFromAccidentalDeletion <Boolean>] [-Server <String>]
 [-ServiceAuthenticationPolicy <ADAuthenticationPolicy>] [-UserAuthenticationPolicy <ADAuthenticationPolicy>]
 [<CommonParameters>]
```

## 描述
`New-ADAuthenticationPolicySilo` cmdlet 在 Active Directory® 域服务中创建一个身份验证策略隔离对象（即身份验证策略的独立存储和管理单元）。

## 示例

#### 示例 1：创建一个身份验证策略库并强制执行它
```
PS C:\> New-ADAuthenticationPolicySilo -Name AuthenticationPolicySilo01 -Enforce
```

该命令创建一个认证策略对象，并将其应用到系统中（即执行相应的强制措施）。

### 示例 2：创建一个不带有强制执行的身份验证策略孤岛
```
PS C:\> New-ADAuthenticationPolicySilo -Name AuthenticationPolicySilo02
```

这个命令创建了一个身份验证策略对象（即用于存储策略信息的对象），但并不会强制执行该策略。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的认证方法是“Negotiate”。对于基本认证（Basic authentication）方法来说，需要建立安全套接字层（SSL）连接。

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

### -ComputerAuthenticationPolicy
指定适用于计算机账户的身份验证策略。

```yaml
Type: ADAuthenticationPolicy
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

### -Credential
指定一个具有执行该任务权限的用户账户。默认值为当前用户。可以输入一个用户名（例如 User01 或 Domain01/User01），或者输入一个 **PSCredential** 对象（例如由 **Get-Credential** cmdlet 生成的对象）。

默认情况下，该 cmdlet 使用当前登录用户的凭据，除非该 cmdlet 是从 Active Directory 域服务 Windows PowerShell 提供程序驱动器中运行的。如果在提供程序驱动器中运行该 cmdlet，则使用与该驱动器关联的账户作为默认凭据。

如果你指定的凭据没有执行该任务的权限，那么这个 cmdlet 会返回一个错误。

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
为对象指定一个描述性文本。该参数用于设置对象的 `description` 属性的值。在轻量级目录访问协议（LDAP）中，这个属性的显示名称（**ldapDisplayName**）就是 “description”。

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

### -Enforce
表示强制实施了身份验证策略（即各个身份验证模块之间是相互独立的、无法协同工作的）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Instance
指定一个 **ADAuthenticationPolicySilo** 对象的实例，用作新创建的 **ADAuthenticationPolicySilo** 对象的模板。要获取用于作为模板的 **ADAuthenticationPolicySilo** 对象，请使用 Get-ADAuthenticationPolicySilo cmdlet 命令。

```yaml
Type: ADAuthenticationPolicySilo
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定对象的名称。此参数用于设置 Active Directory 域服务对象的 **Name** 属性。该属性的 LDAP 显示名称（**ldapDisplayName**）即为“name”。

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
用于指定那些无法通过其他参数表示的属性的对象属性值列表。您可以使用该参数同时设置一个或多个属性；如果某个属性支持多个值，您可以为其分配多个值。要标识某个属性，请使用在 Active Directory 域服务架构中为其定义的 LDAP 显示名称（**ldapDisplayName**）来进行识别。

请按照以下格式指定属性及其值：`@{'AttributeLDAPDisplayName'=value'}`.

要为某个属性指定多个值，请使用逗号分隔这些值。如果您需要为多个属性指定值，可以使用分号来分隔各个属性及其对应的值。

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
该属性用于指示是否阻止对象被删除。当此属性设置为 `true` 时，必须先修改该属性的值，才能删除相应的对象。该参数的可接受值包括：

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
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下是指定 Active Directory 域服务实例的几种方式：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们的列出顺序：

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

### -ServiceAuthenticationPolicy
指定适用于托管服务账户的身份验证策略。

```yaml
Type: ADAuthenticationPolicy
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -UserAuthenticationPolicy
指定适用于用户账户的身份验证策略。

```yaml
Type: ADAuthenticationPolicy
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

### Microsoft ActiveDirectory.Management ADAuthenticationPolicy

### System.String

### System.Management.Automation.SwitchParameter

## 输出

### System.Object

## 备注

## 相关链接

[Get-ADAuthenticationPolicySilo](./Get-ADAuthenticationPolicySilo.md)

[Remove-ADAuthenticationPolicySilo](./Remove-ADAuthenticationPolicySilo.md)

[Set-ADAuthenticationPolicySilo](./Set-ADAuthenticationPolicySilo.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)
