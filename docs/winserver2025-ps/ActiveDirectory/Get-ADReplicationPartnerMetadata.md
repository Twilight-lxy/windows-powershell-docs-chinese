---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adreplicationpartnermetadata?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADReplicationPartnerMetadata
---

# Get-ADReplicationPartnerMetadata

## 摘要
返回一组一个或多个复制伙伴的复制元数据。

## 语法

### 目标（默认值）
```
Get-ADReplicationPartnerMetadata [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-EnumerationServer <String>] [-Filter <String>] [[-Partition] <String[]>] [[-PartnerType] <ADPartnerType>]
 [-Target] <Object[]> [<CommonParameters>]
```

### 范围
```
Get-ADReplicationPartnerMetadata [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-EnumerationServer <String>] [-Filter <String>] [[-Partition] <String[]>] [[-PartnerType] <ADPartnerType>]
 [-Scope] <ADScopeType> [[-Target] <Object[]>] [<CommonParameters>]
```

## 描述
`Get-ADReplicationPartnerMetadata` cmdlet 会为每个 Active Directory 复制伙伴返回一个相应的元数据对象，其中包含这些复制伙伴所需的所有相关复制信息。这些信息包括 `LastReplicationSuccess`、`LastReplicationAttempt` 等属性，以及每对复制伙伴特有的其他数据。如果返回的结果过于冗长，可以使用 `Partition` 参数来指定一个分区以缩小结果范围；或者也可以使用 `Filter` 参数来实现同样的目的。如果没有为查询结果指定分区或过滤条件，则会使用默认的命名上下文，从而返回所有复制伙伴的元数据。

## 示例

### 示例 1：获取域控制器的复制伙伴元数据
```
PS C:\> Get-ADReplicationPartnerMetadata -Target corp-DC01
```

该命令仅获取corp-DC01与其入站合作伙伴之间针对默认分区的复制元数据。

### 示例 2：获取域控制器及其入站伙伴的复制伙伴元数据
```
PS C:\> Get-ADReplicationPartnerMetadata -Target corp-DC01 -PartnerType Inbound
```

此命令仅获取corp-DC01与其入站合作伙伴之间针对默认分区的复制元数据（与上述内容相同）。

### 示例 3：获取某个模式分区的复制伙伴元数据
```
PS C:\> Get-ADReplicationPartnerMetadata -Target corp-DC01,corp-DC02 -PartnerType Both -Partition Schema
```

此命令仅获取corp-DC01、corp-DC02及其各自合作伙伴之间的复制元数据（包括入站和出站的元数据），针对的是该模式分区。

### 示例 4：获取站点中所有域控制器复制伙伴的元数据
```
PS C:\> Get-ADReplicationPartnerMetadata -Target NorthAmerica -Scope Site -Partition *
```

此命令用于获取NorthAmerica站点内所有域名控制器的所有入站合作伙伴的所有托管分区的复制元数据。

### 示例 5：获取默认分区中入站伙伴的复制伙伴元数据
```
PS C:\> Get-ADReplicationPartnerMetadata -Target "corp.contoso.com" -Scope Domain
```

此命令用于获取域 corp.contoso.com 中默认分区所有入站伙伴（即作为该分区数据复制目标的域控制器）的复制元数据。

### 示例 6：获取森林中入站合作伙伴的复制伙伴元数据
```
PS C:\> Get-ADReplicationPartnerMetadata -Target "corp.contoso.com" -Scope Forest -Partition Configuration
```

此命令会获取forest.corp.contoso.com中配置分区所有入站域控制器（即作为该配置分区伙伴的域控制器）的复制元数据。

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

### -Credential
指定一个具有执行此操作权限的用户账户。默认值是当前用户。

请输入一个用户名，例如 User01 或 Domain01/User01；或者输入一个 **PSCredential** 对象（例如由 **Get-Credential** cmdlet 生成的对象）。如果您输入了用户名，系统会提示您输入密码。

此参数不被任何随 Windows PowerShell 安装的提供程序支持。

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

### -EnumerationServer
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下是指定实例的几种方式之一：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们在列表中的排列顺序：

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

### -Filter
该参数用于指定以提供者所支持的格式或语言表示的过滤器。其值用于限定 *Path* 参数的有效范围。过滤器的语法（包括通配符的使用方式）取决于具体的提供者。与其它参数相比，过滤器更加高效：因为提供者在检索对象时直接应用这些过滤器，而非等到对象被检索后再由 Windows PowerShell 来进行过滤操作。

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

### -Partition
默认的身份验证方法是“Negotiate”。

基本身份验证方法需要使用安全套接字层（SSL）连接。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: NC, NamingContext

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PartnerType
指定此cmdlet返回的复制类型的枚举值。该参数的可接受值为：

- Inbound
- Outbound
- Both

```yaml
Type: ADPartnerType
Parameter Sets: (All)
Aliases:
Accepted values: Inbound, Outbound, Both

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Scope
当“Target”参数被用作输入时，该属性用于指定其作用范围（scope type）。此参数的可接受取值为：

- Server
- Site
- Domain
- Forest

Server

Site

Domain

Forest

```yaml
Type: ADScopeType
Parameter Sets: Scope
Aliases:
Accepted values: Server, Domain, Forest, Site

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Target
Specifies the target for returning replication partner metadata as either one or more domain controllers, sites, domains, or forests.
If multiple values for the target are to be specified, they need to be separated by commas.
This parameter will return results for all the domain controllers specified or for part of the specified container.

```yaml
Type: Object[]
Parameter Sets: Target
Aliases: Name, HostName, Site, Domain, Forest

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

```yaml
Type: Object[]
Parameter Sets: Scope
Aliases: Name, HostName, Site, Domain, Forest

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ActiveDirectory.Management ADDDirectoryServer
一种用于表示 Active Directory 服务器对象的类结构。

## 输出

### Microsoft.ActiveDirectory.Management.ADReplicationPartnerMetadata
一种类结构，用于表示 Active Directory 复制伙伴元数据对象。

## 备注
* The default behavior for this cmdlet is to prompt for server identity. Other tools that have been made available in prior releases of Windows Server to manage replication partnerships include Active Directory Sites and Services and the Repadmin.exe tool. If this cmdlet is aliased, it should use ReplSummary as the alias name value.

## 相关链接

