---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adcentralaccesspolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADCentralAccessPolicy
---

# New-ADCentralAccessPolicy

## 摘要
在 Active Directory 中创建一个新的中央访问策略，其中包含一组中央访问规则。

## 语法

```
New-ADCentralAccessPolicy [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Description <String>] [-Instance <ADCentralAccessPolicy>] [-Name] <String> [-PassThru]
 [-ProtectedFromAccidentalDeletion <Boolean>] [-Server <String>] [<CommonParameters>]
```

## 描述
`New-ADCentralAccessPolicy` cmdlet 用于在 Active Directory 中创建一个新的中央访问策略。Active Directory 中的中央访问策略包含一组中央访问规则。

## 示例

### 示例 1：创建一个包含资源条件的中心访问策略
```
PS C:\> $DepartmentResourceProperty = Get-ADResourceProperty -Identity Department
PS C:\> $ResourceCondition = "(@RESOURCE." + $DepartmentResourceProperty.Name + " Contains {`"Finance`"})"
PS C:\> New-ADCentralAccessRule -Name "Finance Documents Rule" -ResourceCondition $ResourceCondition
```

这个命令创建了一条名为“Finance Documents Rule”的中央访问规则，并添加了一个新的资源条件。该资源条件的作用范围是那些在“Department”资源属性中包含“Finance”字样的资源。

### 示例 2：创建一个包含资源条件和新权限的中央访问策略
```
PS C:\> $CountryClaimType = Get-ADClaimType -Identity Country
PS C:\> $DepartmentClaimType = Get-ADClaimType -Identity Department
PS C:\> $CountryResourceProperty = Get-ADResourceProperty -Identity Country
PS C:\> $DepartmentResourceProperty = Get-ADResourceProperty -Identity Department
PS C:\> $FinanceException = Get-ADGroup -Identity FinanceException
PS C:\> $FinanceAdmin = Get-ADGroup -Identity FinanceAdmin
PS C:\> $ResourceCondition = "(@RESOURCE." + $DepartmentResourceProperty.Name + " Contains {`"Finance`"})"
PS C:\> $CurrentAcl = "O:SYG:SYD:AR(A;;FA;;;OW)(A;;FA;;;BA)(A;;0x1200a9;;;" + $FinanceException.SID.Value + ")(A;;0x1301bf;;;" + $FinanceAdmin.SID.Value + ")(A;;FA;;;SY)(XA;;0x1200a9;;;AU;((@USER." + $CountryClaimType.Name + " Any_of @RESOURCE." + $CountryResourceProperty.Name + ") && (@USER." + $DepartmentClaimType.Name + " Any_of @RESOURCE." + $DepartmentResourceProperty.Name + ")))"
PS C:\> Set-ADCentralAccessRule -Identity "Finance Documents Rule" -ResourceCondition $ResourceCondition -CurrentAcl $CurrentAcl
```

此命令创建了一条名为“Finance Documents Rule”的中央访问规则，该规则具有新的资源条件和新的权限设置。

新规则规定，文档只能由财务部门的成员阅读。财务部门的成员仅能访问自己所在国家/地区的文档。只有财务管理员才具有写入文档的权限。不过，对于属于“FinanceException”组的成员，该规则允许例外处理——这些成员拥有读取文档的权限。

目标定位：

- Resource.Department Contains Finance

访问规则：

- Allow Read User.Country=Resource.Country AND User.department = Resource.Department
- Allow Full control User.MemberOf(FinanceAdmin)
- Allow Read User.Country=Resource.Country AND User.department = Resource.DepartmentAllow Read User.MemberOf(FinanceException)

### 示例 3：使用现有 Active Directory 对象的属性来创建一个中央访问策略
```
PS C:\> Get-ADCentralAccessPolicy -Identity "Finance Policy" | New-ADCentralAccessPolicy -Name "Human Resources Policy" -Description "For the Human Resources Department."
```

此命令使用“财务政策”中的属性值创建一个名为“人力资源政策”的中央访问策略，并将描述设置为“用于人力资源部门”。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

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
在运行该 cmdlet 之前，会提示您进行确认。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果是从这样的驱动器中运行 cmdlet，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行该任务的代理（agent）没有目录级别的权限，Windows PowerShell的Active Directory模块会返回一个终止错误（terminating error）。

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
用于指定对象的描述信息。此参数用于设置对象对应的 `Description` 属性的值。在轻量级目录访问协议（LDAP）中，该属性的显示名称为 `ldapDisplayName`，其值为 “description”。

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
指定一个 Active Directory 对象的实例，用作新建 Active Directory 对象的模板。

你可以使用现有的 Active Directory 对象实例作为模板，或者通过使用 Windows PowerShell 命令行或脚本来创建一个新的 Active Directory 对象。

方法 1：使用现有的 Active Directory 对象作为新对象的模板。要检索现有 Active Directory 对象的实例，可以使用诸如 **Get-ADObject** 这样的 cmdlet。然后将该对象传递给 New-ADObject cmdlet 的 Instance 参数，以创建一个新的 Active Directory 对象。您可以通过设置适当的参数来覆盖新对象的属性值。

方法 2：创建一个新的 **ADObject**，并使用 Windows PowerShell 命令行界面设置其属性值。然后将该对象传递给 **New-ADObject** cmdlet 的 *Instance* 参数，以创建新的 Active Directory 对象。

注意：指定的属性不会被进行验证；因此，尝试设置不存在或无法设置的属性会引发错误。

```yaml
Type: ADCentralAccessPolicy
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
用于指定对象的名称。此参数会设置 Active Directory 对象的 **Name** 属性。该属性的轻量级目录访问协议（LDAP）显示名称（**ldapDisplayName**）即为该对象的实际名称。

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
指定是否阻止对象被删除。当此属性设置为 `true` 时，如果不更改该属性的值，则无法删除相应的对象。此参数的允许取值为：

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

以下是指定 Active Directory 域服务实例的几种方法：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

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

### 无值或 Microsoft.ActiveDirectory.Management.ADCentralAccessPolicy
通过*Instance*参数接收到一个Active Directory对象，该对象是新对象的模板。

## 输出

### 无值或 Microsoft.ActiveDirectory.Management.ADCentralAccessPolicy
当指定*PassThru*参数时，会返回新的中央访问策略对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADCentralAccessPolicy](./Get-ADCentralAccessPolicy.md)

[Remove-ADCentralAccessPolicy](./Remove-ADCentralAccessPolicy.md)

[Set-ADCentralAccessPolicy](./Set-ADCentralAccessPolicy.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)

