---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adreplicationattributemetadata?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADReplicationAttributeMetadata
---

# 获取 AD 复制属性元数据

## 摘要
获取一个或多个 Active Directory 复制伙伴的复制元数据。

## 语法

```
Get-ADReplicationAttributeMetadata [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Filter <String>]
 [-IncludeDeletedObjects] [-Object] <ADObject> [[-Properties] <String[]>] [-Server] <String>
 [-ShowAllLinkedValues] [<CommonParameters>]
```

## 描述
`Get-ADReplicationAttributeMetadata` cmdlet 可以获取指定对象上一个或多个属性的复制元数据。这些元数据存储在以下两个目录对象中：

- Single-value attribute: **msDS-ReplAttributeMetaData**
- Multi-value attribute: **msDS-ReplValueMetaData**

该cmdlet会解析字节数组，并以可读的格式返回数据。

## 示例

### 示例 1：获取一组属性的复制元数据
```
PS C:\> Get-ADReplicationAttributeMetadata -Object "CN=Domain Admins,CN=Users,DC=corp,DC=contoso,DC=com" -Server corp-DC01 -ShowAllLinkedValues
```

该命令从 CORP-DC01 域控制器中获取具有以下 distinguished name（可分辨名称）的组的属性的复制元数据：CN=Domain Admins,CN=Users,DC=corp,DC=contoso,DC=com。如果存在多值属性，并且指定了 *ShowAllLinkedValues* 参数，那么该属性的所有关联值也会被一并检索出来。

### 示例 2：获取对象属性的复制元数据
```
PS C:\> Get-ADReplicationAttributeMetadata -Object "1A7BFEC6-C92C-4804-94B0-D407E51F1B64" -Server corp-DC01 -IncludeDeletedObjects
```

此命令用于获取对象（其GUID为1A7BFEC6-C92C-4804-94B0-D407E51F1B64）的复制元数据，包括已删除的对象以及被停用的正向和反向链接信息。

### 示例 3：获取所有组的过滤后的复制元数据
```
PS C:\> Get-ADObject -Filter 'objectclass -eq "group"' | Get-ADReplicationAttributeMetadata -Server corp-DC01 | Where-Object {$_.lastoriginatingchangetime -like "*11/10/2011*"} | Format-Table object
```

这个命令会获取所有在2011年11月10日有任何属性被修改的组。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”（协商）。

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

请输入一个用户名，例如 User01 或 Domain01/User01；或者输入一个 **PSCredential** 对象（例如通过 **Get-Credential** cmdlet 生成的对象）。如果您输入了用户名，系统会要求您提供密码。

这个参数不被任何与 Windows PowerShell 一起安装的提供程序支持。

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

### -Filter
以提供者的格式或语言指定一个过滤器。此参数的值用于限定 *Path* 参数的含义。过滤器的语法（包括通配符的使用）取决于具体的提供者。与其它参数相比，过滤器更为高效：因为提供者在检索对象时会直接应用这些过滤器，而不是让 Windows PowerShell 在对象被检索后再进行筛选。

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

### -IncludeDeletedObjects
指定检索已删除的对象以及已被停用的“前进”和“后退”链接。当指定此参数时，cmdlet会使用以下轻量级目录访问协议（LDAP）控制机制：

- Show Deleted Objects (1.2.840.113556.1.4.417)
- Show Deactivated Links (1.2.840.113556.1.4.2065)

注意：如果未指定此参数，该cmdlet将不会返回任何信息，也不会对已删除的对象进行操作。

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

### -Object
通过提供以下属性值之一来指定一个 Active Directory 对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个无法终止的错误（即程序会持续运行而不会结束）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

派生类型也是被接受的，例如以下这些类型：

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy**
- **Microsoft.ActiveDirectory.Management.ADDomain**

```yaml
Type: ADObject
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Properties
指定一个由一个或多个属性名称组成的列表（用逗号分隔），用于返回复制伙伴的元数据。此参数还支持使用通配符*，表示要返回对象上设置的所有属性。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: Property, Attribute, Attributes

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务（AD DS）实例，方法是为相应的域名或目录服务器提供以下值之一。该服务可以是以下类型中的任何一种：Active Directory 轻量级目录服务（AD LDS）、AD DS 或 Active Directory 快照实例。

以下是指定 AD DS 实例的几种方法：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

- By using the *Server* value from objects passed through the pipeline
- By using the server information associated with the AD DS Windows PowerShell provider drive, when the cmdlet runs in that drive
- By using the domain of the computer running Windows PowerShell

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ShowAllLinkedValues
这表示：如果返回的属性是多值的（即可以包含多个值），那么该 cmdlet 会返回所有关联的值。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft ActiveDirectory.Management.AdObject
一种用于表示 Active Directory 对象的类结构。

## 输出

### Microsoft.ActiveDirectory.Management_ADReplicationAttributeMetadata
一种类结构，用于表示 Active Directory 复制属性元数据对象。

## 备注
* The default behavior for this cmdlet is to prompt for object identity. Other tools that have been provided to manage this feature in previous releases of Windows Server include the Repadmin.exe command-line tool.

## 相关链接

