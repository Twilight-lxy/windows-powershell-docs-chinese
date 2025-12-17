---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-adresourcepropertylistmember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADResourcePropertyListMember
---

# 删除 AD 资源属性列表成员

## 摘要
从 Active Directory 中的资源属性列表中删除一个或多个资源属性。

## 语法

```
Remove-ADResourcePropertyListMember [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADResourcePropertyList> [-Members] <ADResourceProperty[]> [-PassThru] [-Server <String>]
 [<CommonParameters>]
```

## 描述
`Remove-ADResourcePropertyListMember` cmdlet 可用于从 Active Directory 中的资源属性列表中删除一个或多个资源属性。

## 示例

### 示例 1：删除指定的资源属性列表成员
```
PS C:\> Remove-ADResourcePropertyListMember -Identity "Global Resource Property List" -Members Country
```

此命令将从指定的资源属性列表（Global Resource Property List）中删除作为列表成员指定的资源属性“Country”。

### 示例 2：移除多个资源属性列表成员
```
PS C:\> Remove-ADResourcePropertyListMember -Identity "Corporate Resource Property List" -Members Department,Country
```

此命令会从资源属性列表（Corporate Resource Property List）中删除名为“Department”和“Country”的资源属性。

### 示例 3：从过滤后的资源属性列表中移除指定的成员
```
PS C:\> Get-ADResourcePropertyList -Filter "Name -like 'Corporate*'" | Remove-ADResourcePropertyListMember -Members Department,Country
```

这个命令会获取所有名称以“Corporate”开头的资源属性列表，然后将其传递给**Remove-ADResourcePropertyListMember**命令；该命令会从这些列表中删除名称为“Department”和“Country”的资源属性。

## 参数

### -AuthType
指定要使用的认证方法。此参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的认证方法是“Negotiate”。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的提供程序驱动器中运行的，则使用与该驱动器关联的账户作为默认凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行任务的代理进程没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

### -Identity
通过提供以下属性值之一来指定一个 Active Directory 对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

```yaml
Type: ADResourcePropertyList
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Members
指定一个由 **ADResourceProperty** 对象组成的数组（这些对象以逗号分隔），并将其添加到资源属性列表中。要标识每个对象，请使用以下属性值之一：

- Name
- Distinguished name
- GUID (objectGUID)

Note: The identifier in parentheses is the LDAP display name.

You can also provide objects to this parameter directly.

You cannot pass objects through the pipeline to this parameter.

```yaml
Type: ADResourceProperty[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
Returns an object representing the item with which you are working.
By default, this cmdlet does not generate any output.

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
指定要连接的 AD DS 实例，为此需要提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型中的任意一种：AD LDS、AD DS 或 Active Directory 快照实例。

以下是指定 AD DS 实例的几种方法：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，确定顺序按照列出的顺序进行：

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

### 无值或 `Microsoft ActiveDirectory.Management_ADResourcePropertyList`
*Identity* 参数接收到了一个 **ADResourcePropertyList** 对象。

## 输出

### 无值或 `Microsoft ActiveDirectory.Management_ADResourcePropertyList`
当指定了*PassThru*参数时，该cmdlet会返回修改后的**ADResourcePropertyList**对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* This cmdlet does not work with a read-only domain controller.
* This cmdlet does not work with an Active Directory snapshot.
* By default, this cmdlet has the *Confirm* parameter set, which prompts you to confirm before a removal of the specified object type can occur. To bypass prompting for confirmation before removal, you can specify `-Confirm:$False` when using this cmdlet.

## 相关链接

[Add-ADResourcePropertyListMember](./Add-ADResourcePropertyListMember.md)

