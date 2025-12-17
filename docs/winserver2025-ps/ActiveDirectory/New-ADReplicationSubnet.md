---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adreplicationsubnet?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADReplicationSubnet
---

# New-ADReplicationSubnet

## 摘要
创建一个 Active Directory 复制子网对象。

## 语法

```
New-ADReplicationSubnet [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Description <String>] [-Instance <ADReplicationSubnet>] [-Location <String>] [-Name] <String>
 [-OtherAttributes <Hashtable>] [-PassThru] [-Server <String>] [[-Site] <ADReplicationSite>]
 [<CommonParameters>]
```

## 描述
`New-ADReplicationSubnet` cmdlet 用于创建一个新的 Active Directory 子网对象。子网对象（属于 subnet 类）用于在 Active Directory 中定义网络子网。网络子网是指 TCP/IP 网络中的一个部分，该部分被分配了一组逻辑 IP 地址。子网通过某种方式对计算机进行分组，从而标识它们在网络中的物理位置。Active Directory 中的子网对象用于将计算机映射到相应的站点。

## 示例

#### 示例 1：创建一个子网
```
PS C:\> New-ADReplicationSubnet -Name "10.0.0.0/25"
```

这个命令创建了一个名为 10.0.0.0/25 的子网。

### 示例 2：为指定位置创建一个子网
```
PS C:\> New-ADReplicationSubnet -Name "10.10.0.0/22" -Site Asia -Location "Tokyo,Japan"
```

该命令创建了一个名为 10.10.0.0/22 的新子网，将其关联站点设置为“亚洲”，并将 **位置（Location）** 属性设置为日本东京。

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
指定一个具有执行此操作权限的用户账户。默认值为当前用户。

请输入一个用户名，例如 User01 或 Domain01\User01；或者输入一个 **PSCredential** 对象（例如通过 **Get-Credential** cmdlet 生成的对象）。如果您输入了用户名，系统会要求您输入密码。

此参数不适用于任何与 Windows PowerShell 一起安装的提供程序。

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
用于指定对象的描述信息。该参数会设置对象对应 `Description` 属性的值。此属性的 LDAP 显示名称（`ldapDisplayName`）即为该描述内容。

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
指定一个子网对象的实例，用作创建新的子网对象的模板。

你可以使用现有的子网对象的实例作为模板，或者通过使用 Windows PowerShell 命令行或脚本来创建一个新的子网对象。

方法 1：使用现有的子网对象作为新子网对象的模板。要获取现有子网对象的实例，请使用 Get-ADReplicationSubnet cmdlet。然后将该对象传递给 **New-ADReplicationSubnet** cmdlet 的 *Instance* 参数以创建新的子网对象。您可以通过设置相应的参数来覆盖新对象的属性值。

方法 2：使用 Windows PowerShell 命令行界面创建一个新的 **ADReplicationSubnet**，并设置相应的属性值。然后将该对象传递给 **New-ADReplicationSubnet** cmdlet 的 *Instance* 参数，以创建新的子网对象。

注意：指定的属性不会被进行验证；因此，尝试设置不存在或无法设置的属性会引发错误。

```yaml
Type: ADReplicationSubnet
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Location
用于描述该子网的物理位置信息。

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

### -Name
指定子网的名称。此参数设置了 Active Directory 对象的 **Name** 属性。该属性的 LDAP 显示名称（**ldapDisplayName**）即为 “name”。

在 Active Directory 中，子网的名称采用“网络地址/掩码位”的形式。例如，子网对象 172.16.72.0/22 表示该子网的 IP 地址为 172.16.72.0，且使用的是 22 位的子网掩码。

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
用于指定那些无法通过cmdlet参数表示的对象属性的值。你可以使用此参数同时设置一个或多个参数。如果某个属性支持多个值，你可以为其分配多个数值。要识别某个属性，请使用在Active Directory架构中定义的该属性的LDAP显示名称（**ldapDisplayName**）。

要为某个属性指定一个单一的值：

`-其他属性 @{'AttributeLDAPDisplayName'=值}`

要为某个属性指定多个值：

`-其他属性 @{'AttributeLDAPDisplayName'=值1,值2,...}`

你可以使用分号（;）来分隔多个属性，从而为这些属性指定相应的值。以下语法展示了如何为多个属性设置值：

`-其他属性 @{'Attribute1LDAPDisplayName'=值; 'Attribute2LDAPDisplayName'=值1,值2;...}`

以下示例展示了如何使用这个参数。

要设置一个名为 `favColors` 的自定义属性的值，该属性接受一组 Unicode 字符串，请使用以下语法：

`-其他属性 @{'favColors'="粉色","紫色"}`

要同时为 `favColors` 和 `dateOfBirth` 设置值，请使用以下语法：

`-其他属性 @{'favColors'="粉色", "紫色"; 'dateOfBirth'="1960年1月1日"}`

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
指定要连接的 Active Directory 域服务（AD DS）实例，为此需要提供一个相应的域名或目录服务器的名称。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（AD LDS）、AD DS 或 Active Directory 快照实例。

以下是指定 Active Directory 域服务实例的几种方式之一：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

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

### -Site
指定与此子网关联的站点。

```yaml
Type: ADReplicationSite
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。不过实际上并没有运行这个cmdlet。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft.ActiveDirectory.Management.ADReplicationSubnet
通过 `Instance` 参数接收到一个子网对象，该对象是新子网对象的模板。

## 输出

### 无或 Microsoft.ActiveDirectory.Management.ADReplicationSubnet

## 备注

## 相关链接

[Get-ADReplicationSubnet](./Get-ADReplicationSubnet.md)

[Remove-ADReplicationSubnet](./Remove-ADReplicationSubnet.md)

[Set-ADReplicationSubnet](./Set-ADReplicationSubnet.md)

