---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adauthenticationpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADAuthenticationPolicy
---

# 新的 ADAuthenticationPolicy

## 摘要
创建一个 Active Directory 域服务身份验证策略对象。

## 语法

```
New-ADAuthenticationPolicy [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-ComputerAllowedToAuthenticateTo <String>] [-ComputerTGTLifetimeMins <Int32>]
 [-Credential <PSCredential>] [-Description <String>] [-Enforce]
 [-Instance <ADAuthenticationPolicy>] [-Name] <String> [-OtherAttributes <Hashtable>] [-PassThru]
 [-ProtectedFromAccidentalDeletion <Boolean>] [-RollingNTLMSecret <ADStrongNTLMPolicyType>]
 [-Server <String>] [-ServiceAllowedToAuthenticateFrom <String>]
 [-ServiceAllowedToAuthenticateTo <String>] [-ServiceAllowedNTLMNetworkAuthentication]
 [-ServiceTGTLifetimeMins <Int32>] [-UserAllowedToAuthenticateFrom <String>]
 [-UserAllowedToAuthenticateTo <String>] [-UserAllowedNTLMNetworkAuthentication]
 [-UserTGTLifetimeMins <Int32>] [<CommonParameters>]
```

## 描述

`New-ADAuthenticationPolicy` 用于在 Active Directory® 域服务中创建一个身份验证策略对象。

此cmdlet的参数可用于指定对象常用的属性。如果要为对象设置未在此cmdlet参数中列出的属性，请指定*OtherAttributes*参数。

你可以使用管道运算符（pipeline operator）和 `Import-Csv` cmdlet 来传递一个列表，以便在目录中批量创建对象。此外，你还可以通过使用 `*Instance` 参数来指定一个模板对象，从而根据该模板创建新的对象。

## 示例

### 示例 1：创建一个认证策略，并设置用户的 TGT（Ticket-to-Identity）有效期

```
PS C:\> New-ADAuthenticationPolicy -Name "AuthenticationPolicy01" -UserTGTLifetimeMins 60
```

此命令创建了一个名为AuthenticationPolicy01的认证策略对象，并将用户账户的TGT（Temporary Grant）有效期设置为60分钟。由于未指定*Enforce*参数，因此创建的认证策略处于审计模式。

### 示例 2：创建强制性的身份验证策略

```
PS C:\> New-ADAuthenticationPolicy -Name "AuthenticationPolicy02" -Enforce
```

该命令创建一个名为“AuthenticationPolicy02”的身份验证策略，并通过指定“Enforce”参数来强制执行该策略。

### 示例 3：创建身份验证策略

```
PS C:\> New-ADAuthenticationPolicy -Name "TestAuthenticationPolicy" -UserAllowedToAuthenticateFrom (Get-Acl .\someFile.txt).sddl
```

该命令创建了一个名为 TestAuthenticationPolicy 的身份验证策略。*UserAllowedToAuthenticationFrom* 参数通过一个名为 someFile.txt 的文件中的 SDDL 字符串来指定允许用户进行身份验证的设备。

## 参数

### -AuthType

指定要使用的身份验证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”。对于基本身份验证方法（Basic authentication），需要建立安全套接字层（SSL）连接。

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

### -ComputerAllowedToAuthenticateTo

指定了用于确定计算机是否可以身份验证到该账户的安全描述符所使用的安全描述符定义语言（SDDL）字符串。

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

### -ComputerTGTLifetimeMins

指定非可续订的计算机账户票证（TGT）的有效时长（以分钟为单位）。

```yaml
Type: Int32
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

指定一个具有执行该任务权限的用户账户。默认值为当前用户。可以输入用户名（例如 User01 或 Domain01\User01），或者输入一个 **PSCredential** 对象（例如通过 **Get-Credential** cmdlet 生成的对象）。

默认情况下，该cmdlet使用当前登录用户的凭据，除非它是从Active Directory域服务Windows PowerShell提供程序驱动器中运行的。如果在提供程序驱动器中运行该cmdlet，则会使用与该驱动器关联的账户作为默认凭据。

如果您指定的凭据没有执行该任务的权限，那么此cmdlet会返回一个错误。

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

为对象指定一个描述性信息。此参数用于设置该对象的 `description` 属性的值。在轻量级目录访问协议（LDAP）中，该属性的显示名称（**ldapDisplayName**）就是 “description”。

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

表示身份验证策略正在被执行（即用户必须按照该策略进行认证）。

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

指定一个 **ADAuthenticationPolicy** 对象的实例，用作新 **ADAuthenticationPolicy** 对象的模板。要获取用作模板的 **ADAuthenticationPolicy** 对象，请使用 **Get-ADAuthenticationPolicy** cmdlet。

```yaml
Type: ADAuthenticationPolicy
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name

指定对象的名称。此参数用于设置 Active Directory 域服务对象的 **Name**（名称）属性。该属性的 LDAP 显示名称（**ldapDisplayName**）即为 “name”。

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

该参数用于指定那些未被其他参数表示的对象属性的值列表。您可以使用此参数同时设置一个或多个属性；如果某个属性具有多个值，您可以为其分配多个值。要识别某个属性，请使用在 Active Directory 域服务架构中为此属性定义的 LDAPDisplayName（**ldapDisplayName**）进行标识。

请按照以下格式指定属性及其值：@{'AttributeLDAPDisplayName'=value}。

要为某个属性指定多个值，请使用逗号分隔这些值。如果需要为多个属性指定值，可以使用分号来分隔各个属性值对。

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

### -ProtectedFromAccidentalDeletion

该属性用于指示是否阻止对象的删除。当此属性设置为 `true` 时，如果不更改该属性的值，则无法删除相应的对象。该参数的可接受值为：

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

### -RollingNTLMSecret

从 Windows 10 的 1703 版本开始，该功能已被弃用，因此不应在 Active Directory 中进行配置。

```yaml
Type: ADStrongNTLMPolicyType
Parameter Sets: (All)
Aliases:
Accepted values: Disabled, Optional, Required

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Server

指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

请以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

- By using the *Server* value from objects passed through the pipeline
- By using the server information associated with the Active Directory Domain Services Windows
  PowerShell provider drive, when the cmdlet runs in that drive
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

### -ServiceAllowedNTLMNetworkAuthentication

该规定表明：如果服务账户具有由 *ServiceAllowedToAuthenticateFrom* 参数指定的访问控制表达式，则策略允许使用 NTLM 网络身份验证机制。

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

### -ServiceAllowedToAuthenticateFrom

指定一个访问控制表达式，用于确定该服务可以从哪些设备进行身份验证。

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

### -ServiceAllowedToAuthenticateTo

指定用于判断该服务是否可以以此账户进行身份验证的安全描述符的 SDDL（Security Descriptors Language）字符串。

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

### -ServiceTGTLifetimeMins

指定服务账户中不可续期的TGT（临时令牌）的有效时长（以分钟为单位）。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -UserAllowedNTLMNetworkAuthentication

表示如果用户账户具有由*User AllowedToAuthenticateFrom*参数指定的访问控制表达式，则该策略允许使用NTLM网络身份验证。

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

### -UserAllowedToAuthenticateFrom

指定一个访问控制表达式，用于确定用户可以从哪些设备进行身份验证。

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

### -UserAllowedToAuthenticateTo

指定用于确定用户是否可以登录到该账户的安全描述符的 SDDL（Security Description Language）字符串。

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

### -UserTGTLifetimeMins

指定用户账户中不可续期的TGT（临时全局令牌）的有效时长（以分钟为单位）。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该 cmdlet 会发生什么情况。但实际上并没有运行该 cmdlet。

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

### ADStrongNTLMPolicyType

### System Boolean

### System.Int32

### System.ManagementAutomation.SwitchParameter

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Get-ADAuthenticationPolicy](./Get-ADAuthenticationPolicy.md)

[Remove-ADAuthenticationPolicy](./Remove-ADAuthenticationPolicy.md)

[Set-ADAuthenticationPolicy](./Set-ADAuthenticationPolicy.md)

[Windows PowerShell中的AD DS管理Cmdlet](./activedirectory.md)
