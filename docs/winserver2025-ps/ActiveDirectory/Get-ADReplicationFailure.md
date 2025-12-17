---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adreplicationfailure?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADReplicationFailure
---

# Get-ADReplicationFailure

## 摘要
返回一个数据集合，用于描述 Active Directory 复制失败的情况。

## 语法

### 目标（默认值）
```
Get-ADReplicationFailure [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-EnumeratingServer <String>]
 [-Filter <String>] [-Target] <Object[]> [<CommonParameters>]
```

### 范围
```
Get-ADReplicationFailure [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-EnumeratingServer <String>]
 [-Filter <String>] [-Scope] <ADScopeType> [[-Target] <Object[]>] [<CommonParameters>]
```

## 描述
`Get-ADReplicationFailure` cmdlet 可以返回与指定的域控制器或 Active Directory Lightweight Directory Services (AD LDS) 实例当前关联的所有复制故障信息。返回的对象类型为 `ADReplicationFailure`。该 cmdlet 会将故障列表存储在特定服务器的 `ADReplicationSummary` 对象中。

## 示例

#### 示例 1：获取某个域控制器的复制失败数据
```
PS C:\> Get-ADReplicationFailure -Target corp-DC01
```

这个命令获取了一组数据，这些数据描述了corp-DC01上的Active Directory复制失败情况。

### 示例 2：获取服务器的复制故障数据
```
PS C:\> Get-ADReplicationFailure -Target corp-DC01 -Scope Server
```

这条命令从 corp-DC01 获取了一组描述 Active Directory 复制失败的数据。

### 示例 3：获取多个域控制器的复制故障数据
```
PS C:\> Get-ADReplicationFailure -Target corp-DC01,corp-DC02
```

这个命令从corp-DC01和corp-DC02获取了一组描述Active Directory复制故障的数据。

### 示例 4：获取某个站点的复制失败数据
```
PS C:\> Get-ADReplicationFailure -Target NorthAmerica -Scope Site
```

该命令从NorthAmerica站点中的所有域控制器获取一组描述Active Directory复制故障的数据。

### 示例 5：获取域中所有域控制器复制失败的数据
```
PS C:\> Get-ADReplicationFailure -Target "corp.contoso.com" -Scope Domain
```

这个命令从域 corp.contoso.com 中的所有域控制器那里获取一组描述 Active Directory 复制故障的数据。

### 示例 6：获取林中所有域控制器中的复制故障数据
```
PS C:\> Get-ADReplicationFailure -Target "corp.contoso.com" -Scope Forest
```

这个命令从corp.contoso.com森林中的所有域控制器中获取一组描述Active Directory复制失败的数据。

## 参数

### -AuthType
指定要使用的身份验证方法。此参数的可接受值为：

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
指定一个具有执行此操作权限的用户账户。默认值为当前用户。

请输入一个用户名，例如 User01 或 Domain01\User01；或者输入一个 **PSCredential** 对象（例如通过 **Get-Credential** cmdlet 生成的对象）。如果您输入了用户名，系统会提示您输入密码。

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

### -EnumeratingServer
指定要连接的 Active Directory 域服务（AD DS）实例，为此请提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型之一：Active Directory 轻量级域服务（AD LDS）、AD DS 或 Active Directory 快照实例。

请以下列方式之一指定实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法中列出的顺序来确定的：

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

### -Filter
该参数用于指定符合提供者格式或语言规范的过滤器。其值会对 *Path* 参数的使用进行限制。过滤器的具体语法（包括通配符的用法）取决于所使用的提供者。与其它参数相比，过滤器更加高效：因为提供者在检索对象时会直接应用这些过滤器，而无需让 Windows PowerShell 在对象被检索后再对其进行筛选处理。

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

### -Scope
指定作为*Target*参数输入的对象类型。该参数的可接受值包括：

- Server
- Site
- Domain
- Forest

```yaml
Type: ADScopeType
Parameter Sets: Scope
Aliases: ReplicationSite
Accepted values: Server, Domain, Forest, Site

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Target
Specifies either one or more (using a comma separated list) of Active Directory domain controllers, sites, domains, or forests.
It returns results for all the domain controllers that are specified or that are part of the specified container.

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
一个类结构，其中包含一个或多个 Active Directory 服务器对象。

## 输出

### Microsoft Active Directory Management ADReplicationFailure
一种用于表示 Active Directory 复制失败对象的类结构。

## 备注

## 相关链接

