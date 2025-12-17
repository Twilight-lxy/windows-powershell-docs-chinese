---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adreplicationsitelinkbridge?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADReplicationSiteLinkBridge
---

# 新的 AD 复制站点链接桥接器

## 摘要
在 Active Directory 中创建一个站点链接桥以用于数据复制。

## 语法

```
New-ADReplicationSiteLinkBridge [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Description <String>] [-Instance <ADReplicationSiteLinkBridge>]
 [-InterSiteTransportProtocol <ADInterSiteTransportProtocolType>] [-Name] <String>
 [-OtherAttributes <Hashtable>] [-PassThru] [-Server <String>] [[-SiteLinksIncluded] <ADReplicationSiteLink[]>]
 [<CommonParameters>]
```

## 描述
`New-ADReplicationSiteLinkBridge` cmdlet 在 Active Directory 中创建一个站点链接桥（site link bridge），用于复制操作。站点链接桥用于连接两个或多个站点链接，并实现这些站点链接之间的“传递性”（即数据可以在站点链接之间顺畅传输）。桥梁中的每个站点链接都必须与另一个站点链接所属的站点相同。

## 示例

### 示例 1：创建一个站点链接桥（Site Link Bridge）
```
PS C:\> New-ADReplicationSiteLinkBridge -Name "NorthAmerica-Asia" -SiteLinksIncluded "NorthAmerica-Europe","Europe-Asia"
```

此命令创建了一个名为“NorthAmerica-Asia”的站点链接桥接器，该桥接器用于连接“NorthAmerica-Europe”和“Europe-Asia”这两个站点链接。

### 示例 2：创建站点链接桥并设置站点间传输协议
```
PS C:\> New-ADReplicationSiteLinkBridge -Name "NorthAmerica-Asia" -SiteLinksIncluded "NorthAmerica-Europe","Europe-Asia" -InterSiteTransportProtocol IP
```

此命令创建了一个名为“NorthAmerica-Asia”的站点链接桥接器，该桥接器用于连接“NorthAmerica-Europe”和“Europe-Asia”这两个站点链接，并为新创建的对象设置了*InterSiteTransportProtocol*属性的值。

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
在运行 cmdlet 之前会提示您确认是否要执行该操作。

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

你也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

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
用于指定对象的描述信息。该参数会设置对象中 **Description** 属性的值。在轻量级目录访问协议（LDAP）中，此属性的显示名称为 **ldapDisplayName**，其值为 “description”。

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
指定一个站点链接桥接对象的实例，作为新建站点链接桥接对象的模板使用。

你可以使用现有的站点链接桥接对象的实例作为模板，或者通过使用 Windows PowerShell 命令行或脚本来创建一个新的站点链接桥接对象。

方法 1：使用现有的站点链接桥接对象作为新对象的模板。要获取一个现有 Active Directory 对象的实例，可以使用 `Get-ADReplicationSiteLinkBridge` cmdlet。然后将该对象传递给 `New-ADReplicationSiteLinkBridge` cmdlet 的 `Instance` 参数，以创建一个新的站点链接桥接对象。你可以通过设置适当的参数来覆盖新对象的属性值。

方法 2：使用 Windows PowerShell 命令行界面创建一个新的 **ADReplicationSiteLinkBridge**，并设置相应的属性值。然后将这个对象传递给 **New-ADReplicationSiteLinkBridge** cmdlet 的 *Instance* 参数，以创建新的站点链接桥接对象。

注意：指定的属性不会被验证；因此，尝试设置不存在或无法设置的属性会引发错误。

```yaml
Type: ADReplicationSiteLinkBridge
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InterSiteTransportProtocol
指定此站点链接桥的站点间传输协议。该参数的可接受值包括：

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
指定复制站点链接桥对象的名称。

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
用于指定那些不由 cmdlet 参数表示的属性的对象属性值。您可以使用此参数同时设置一个或多个参数。如果某个属性需要多个值，您可以为其分配多个值。要识别某个属性，请使用在 Active Directory 架构中为此属性定义的 LDAP 显示名称（**ldapDisplayName**）来进行标识。

要为某个属性指定一个单一的值：

`-其他属性 @{'AttributeLDAPDisplayName'=值}`

要为某个属性指定多个值：

`-其他属性 @{'AttributeLDAPDisplayName'=值1,值2,...}`

你可以使用分号（;）来分隔多个属性，从而为这些属性指定值。以下语法展示了如何为多个属性设置值：

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

### -Server
指定要连接的 Active Directory 域服务（AD DS）实例，为此提供相应的域名或目录服务器之一的值。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（AD LDS）、AD DS 或 Active Directory 快照实例。

以下是指定 Active Directory 域服务实例的几种方式：

域名值：

- FQDN
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

### -SiteLinksIncluded
指定一个包含在该站点链接桥中的站点链接数组。该参数允许的取值为：区分名称（distinguished name）、GUID 或站点链接的名称。在创建时，此参数必须包含两个站点；否则必须同时使用 *Instance* 参数。

```yaml
Type: ADReplicationSiteLink[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上，这个cmdlet并没有被执行。

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

### 无或 Microsoft.ActiveDirectory.Management.ADReplicationSiteLinkBridge
通过 *Instance* 参数接收到一个站点链接桥接对象（该对象是新站点链接桥接对象的模板）。

## 输出

### 无或 Microsoft.ActiveDirectory.Management.ADReplicationSiteLinkBridge

## 备注
* By default, all site links are bridged (transitive), and creating a site link design is not required. We recommend that you keep transitivity enabled by not changing this default. However, you must disable bridging for all site links and complete a site link bridge design if either of the following is true:

- Your IP network is not fully routed.
- You need to control the replication flow of the changes made in Active Directory Domain Services (AD DS).

## 相关链接

[Get-ADReplicationSiteLinkBridge](./Get-ADReplicationSiteLinkBridge.md)

[Remove-ADReplicationSiteLinkBridge](./Remove-ADReplicationSiteLinkBridge.md)

[Set-ADReplicationSiteLinkBridge](./Set-ADReplicationSiteLinkBridge.md)

