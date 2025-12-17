---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adreplicationsitelink?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADReplicationSiteLink
---

# 新的AD复制站点链接

## 摘要
创建一个新的 Active Directory 站点链接，以便管理复制过程。

## 语法

```
New-ADReplicationSiteLink [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Cost <Int32>]
 [-Credential <PSCredential>] [-Description <String>] [-Instance <ADReplicationSiteLink>]
 [-InterSiteTransportProtocol <ADInterSiteTransportProtocolType>] [-Name] <String>
 [-OtherAttributes <Hashtable>] [-PassThru] [-ReplicationFrequencyInMinutes <Int32>]
 [-ReplicationSchedule <ActiveDirectorySchedule>] [-Server <String>] [[-SitesIncluded] <ADReplicationSite[]>]
 [<CommonParameters>]
```

## 描述
`New-ADReplicationSiteLink` cmdlet 可用于创建一个新的 Active Directory 站点链接。站点链接用于连接两个或多个站点。这些链接体现了关于站点之间如何相互连接的行政策略，以及用于传输复制数据的方法。必须通过站点链接将各个站点连接起来，以便每个站点的域控制器能够同步 Active Directory 的更改内容。

## 示例

### 示例 1：创建一个复制站点链接
```
PS C:\> New-ADReplicationSiteLink -Name "NorthAmerica-Europe" -SitesIncluded NorthAmerica,Europe
```

这条命令创建了一个新的站点链接，名为“NorthAmerica-Europe”，用于连接两个站点“NorthAmerica”和“Europe”。

### 示例 2：创建一个复制站点链接并为其设置属性
```
PS C:\> New-ADReplicationSiteLink -Name "Europe-Asia" -SitesIncluded Europe,Asia -Cost 100 -ReplicationFrequencyInMinutes 15 -InterSiteTransportProtocol IP
```

此命令创建了一个名为“Europe-Asia”的新站点链接，用于连接两个站点“Europe”和“Asia”，并设置了该新对象的*Cost*（成本）、*ReplicationFrequencyInMinutes*（复制频率，单位为分钟）以及*InterSiteTransportProtocol*（站点间传输协议）。

### 示例 3：创建一个复制站点链接并设置其复制计划
```
PS C:\> $Schedule = New-Object -TypeName System.DirectoryServices.ActiveDirectory.ActiveDirectorySchedule
PS C:\> $Schedule.ResetSchedule()
PS C:\> $Schedule.SetDailySchedule("Twenty","Zero","TwentyTwo","Thirty")
PS C:\> New-ADReplicationSiteLink -Name "NorthAmerica-SouthAmerica" -SitesIncluded NorthAmerica,SouthAmerica -ReplicationSchedule $Schedule
```

这个示例创建了一个名为“NorthAmerica-SouthAmerica”的新站点链接，用于连接两个网站“NorthAmerica”和“SouthAmerica”，并将每日复制计划（ReplicationSchedule）设置为从20:00到22:30。

### 示例 4：创建一个复制站点链接，并为其启用变更通知功能
```
PS C:\> New-ADReplicationSiteLink -Name "Europe-Asia" -SitesIncluded Europe,Asia -OtherAttributes @{'options'=1}
```

此命令创建了一个名为“Europe-Asia”的新站点链接，用于连接两个站点：Europe和Asia。同时，该命令还启用了对新对象的变更通知功能。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的认证方法是“Negotiate”（协商）。

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

### -Cost
用于指定要添加到站点链接上的成本。有关确定成本的更多信息，请参阅 TechNet 文库中的 [Determining the Cost](https://go.microsoft.com/fwlink/?LinkId=221871)：http://go.microsoft.com/fwlink/?LinkId=221871。

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

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从此类驱动器中运行的，则默认使用与该驱动器关联的帐户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过使用脚本或 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行任务的代理账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
用于指定对象的描述信息。此参数用于设置对象의 **Description** 属性的值。轻量级目录访问协议（LDAP）中该属性的显示名称（**ldapDisplayName**）为 “description”。

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
指定一个站点链接对象的实例，用作新建站点链接对象的模板。

你可以使用现有的站点链接对象的实例作为模板，也可以通过使用 Windows PowerShell 命令行或脚本来创建一个新的站点链接对象。

方法 1：使用现有的站点链接对象作为新对象的模板。要获取一个现有站点链接对象的实例，可以使用诸如 **Get-ADReplicationSiteLink** 这样的 cmdlet。然后将该对象传递给 **New-ADReplicationSiteLink** cmdlet 的 *Instance* 参数，以创建一个新的 Active Directory 对象。你可以通过设置相应的参数来覆盖新对象的属性值。

方法 2：创建一个新的 **ADReplicationSiteLink**，并通过使用 Windows PowerShell 命令行界面来设置相应的属性值。然后将这个对象传递给 **New-ADReplicationSiteLink** cmdlet 的 Instance 参数，以创建新的站点链接对象。

注意：指定的属性不会经过验证；因此，尝试设置不存在或无法设置的属性会引发错误。

```yaml
Type: ADReplicationSiteLink
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InterSiteTransportProtocol
指定一个有效的站点间传输协议选项。该参数的可接受值包括：

- IP
- SMTP

```yaml
Type: ADInterSiteTransportProtocolType
Parameter Sets: (All)
Aliases:
Accepted values: IP, SMTP

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定站点链接的名称。此参数用于设置 Active Directory 对象的 **Name** 属性。该属性的 LDAP 显示名称（**ldapDisplayName**）即为“name”。

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

### -OtherAttributes
用于指定那些未被 cmdlet 参数表示的对象属性的值。您可以使用此参数同时设置一个或多个属性值。如果某个属性支持多个值，您可以为其分配多个值。要识别某个属性，请使用在 Active Directory 架构中为该属性定义的 LDAPDisplayName（**ldapDisplayName**）进行标识。

语法：

要为某个属性指定单个值：

`-其他属性 @{'AttributeLDAPDisplayName'=值}'`

要为某个属性指定多个值

`-其他属性 @{'AttributeLDAPDisplayName'=值1, 值2, ...}`

您可以使用分号（;）来分隔多个属性，从而为这些属性指定相应的值。以下语法展示了如何为多个属性设置值：

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

### -ReplicationFrequencyInMinutes
请告诉我，在使用该站点链接进行站点间数据复制时，复制操作的频率（以分钟为单位）。Active Directory 通过减少复制操作的频率以及允许用户安排站点链接的可用时间来节省站点间的带宽。默认情况下，每个站点链接之间的数据复制操作每 180 分钟（3 小时）执行一次。您可以根据具体需求调整这一频率。需要注意的是，提高复制频率会增加复制过程所消耗的带宽量。

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

### -ReplicationSchedule
指定此站点链接内所有连接（站内复制）的默认复制计划。这使您可以安排站点链接的使用时间，以便进行数据复制。默认情况下，站点链接全天24小时、每周7天都可用于数据复制。您可以将复制计划限制在特定的工作日或时间段内；例如，可以设置站点间复制仅在正常工作时间之外进行。

```yaml
Type: ActiveDirectorySchedule
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务（AD DS）实例，为此需提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型之一：Active Directory 轻量级域服务（AD LDS）、AD DS 或 Active Directory 快照实例。

以下是指定 AD DS 实例的几种方式：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

该参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

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

### -SitesIncluded
指定包含在站点链接中的站点列表。

```yaml
Type: ADReplicationSite[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

没有相关设置，或者使用了 `Microsoft.ActiveDirectory.Management.ADReplicationSiteLink`。
通过*Instance*参数接收到一个站点链接对象，该对象是新站点链接对象的模板。

## 输出

没有相关设置，或者使用了 `Microsoft.ActiveDirectory.Management.ADReplicationSiteLink`。

## 备注

## 相关链接

[Get-ADReplicationSiteLink](./Get-ADReplicationSiteLink.md)

[Remove-ADReplicationSiteLink](./Remove-ADReplicationSiteLink.md)

[Set-ADReplicationSiteLink](./Set-ADReplicationSiteLink.md)

