---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adreplicationuptodatenessvectortable?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADReplicationUpToDatenessVectorTable
---

# 获取与数据准确性相关的复制向量表（Get-ADReplicationUpToDatenessVectorTable）

## 摘要
显示指定域控制器最高的更新序列号（USN）。

## 语法

### 目标（默认值）
```
Get-ADReplicationUpToDatenessVectorTable [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-EnumerationServer <String>] [-Filter <String>] [[-Partition] <String[]>] [-Target] <Object[]>
 [<CommonParameters>]
```

### 范围
```
Get-ADReplicationUpToDatenessVectorTable [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-EnumerationServer <String>] [-Filter <String>] [[-Partition] <String[]>] [-Scope] <ADScopeType>
 [[-Target] <Object[]>] [<CommonParameters>]
```

## 描述
`Get-ADReplicationUpToDatenessVectorTable` cmdlet 可以显示指定域控制器中的最高更新序列号（USN）。该信息表明副本与其复制伙伴之间的同步程度。在复制过程中，每个被复制的对象都有一个唯一的 USN；如果对象发生修改，其 USN 会随之递增。对于某个特定对象而言，其在各个域控制器上的 USN 值是不同的（即每个域控制器中的 USN 数值都不同）。

## 示例

### 示例 1：获取默认分区的最高 USN 值
```
PS C:\> Get-ADReplicationUpToDatenessVectorTable -Target corp-DC01
```

这个命令用于从 corp-DC01 获取默认分区的最高 USN（Unique Sequence Number）信息。

### 示例 2：获取默认分区的最高 USN 值
```
PS C:\> Get-ADReplicationUpToDatenessVectorTable -Target corp-DC01 -Scope Server
```

这个命令用于从 corp-DC01 获取默认分区的最高 USN（Unique Sequence Number）信息。

#### 示例 3：获取某个模式分区的最高 USN 值
```
PS C:\> Get-ADReplicationUpToDatenessVectorTable -Target corp-DC01,corp-DC02 -Partition Schema
```

这个命令从corp-DC01和corp-DC02中获取该模式分区的最高USN（通用序列号）信息。

### 示例 4：获取站点中所有域控制器所在的所有分区中的最高 USN（唯一系统编号）
```
PS C:\> Get-ADReplicationUpToDatenessVectorTable -Target NorthAmerica -Scope Site -Partition *
```

这个命令会从NorthAmerica站点中的所有域控制器中获取所有分区的最高USN（更新序列号）。

### 示例 5：从域中的所有域控制器中获取默认分区的最高 USN（统一序列号）
```
PS C:\> Get-ADReplicationUpToDatenessVectorTable -Target "corp.contoso.com" -Scope Domain -Partition Default
```

此命令从 domaincorp.contoso.com 域中的所有域控制器中获取默认分区的最高 USN（统一序列号）。

### 示例 6：从森林中的所有域控制器中获取配置分区的最高 USN 值
```
PS C:\> Get-ADReplicationUpToDatenessVectorTable -Target "corp.contoso.com" -Scope Forest -Partition Configuration
```

此命令从forestcorp.contoso.com中的所有域控制器中获取配置分区的最高USN（统一序列号）。

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

### -Credential
指定一个具有执行此操作权限的用户账户。默认值为当前用户。

输入一个用户名，例如 User01 或 Domain01/User01；或者输入一个 **PSCredential** 对象（例如通过 **Get-Credential** cmdlet 生成的凭据）。如果您输入了用户名，系统会要求您输入密码。

这个参数不被任何随 Windows PowerShell 安装的提供程序支持。

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
指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot instance）。

请使用以下方法之一来指定实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的列出顺序：

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
以提供者的格式或语言指定一个过滤器。此参数的值用于限定 *Path* 参数的范围。过滤器的语法（包括通配符的使用）取决于所使用的提供者。与其他参数相比，过滤器更为高效：因为提供者在检索对象时会直接应用这些过滤器，而不是让 Windows PowerShell 在对象被检索后再对其进行筛选。

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
指定 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器上支持的命名上下文之一。此 cmdlet 会在该分区中搜索由 *Identity* 参数所定义的对象。

在许多情况下，如果未指定“Partition”参数的值，则会使用默认值。确定默认值的规则如下所述。请注意，首先列出的规则会被优先评估；一旦确定了默认值，后续的规则将不再被评估。

在 Active Directory 域服务（AD DS）环境中，以下情况下会为“分区”（Partition）设置一个默认值：

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.
In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Partition* parameter does not take any default value.

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
It will return results for all the domain controllers that are specified or that are part of the specified container.

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ActiveDirectory.ManagementADDirectoryServer
一个类结构，其中包含一个或多个 Active Directory 服务器对象。

## 输出

### Microsoft.ActiveDirectory.Management.ADReplicationUpToDatenessVector
一个类结构，其中包含一个或多个用于维护 Active Directory 复制状态更新（UTD）的向量表。

## 备注

## 相关链接

