---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-adresourcepropertylist?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADResourcePropertyList
---

# 新的广告资源属性列表

## 摘要
在 Active Directory 中创建一个资源属性列表。

## 语法

```
New-ADResourcePropertyList [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Description <String>] [-Instance <ADResourcePropertyList>] [-Name] <String> [-PassThru]
 [-ProtectedFromAccidentalDeletion <Boolean>] [-Server <String>] [<CommonParameters>]
```

## 描述
`New-ADResourcePropertyList` cmdlet 可以在 Active Directory 中创建一个资源属性列表。

## 示例

### 示例 1：创建资源属性列表
```
PS C:\> New-ADResourcePropertyList -Name "Corporate Resource Property List"
```

该命令创建了一个名为“Corporate Resource Property List”的新资源属性列表。

### 示例 2：创建资源属性列表并指定描述
```
PS C:\> New-ADResourcePropertyList -Name "Corporate Resource Property List" -Description "For corporate documents."
```

此命令创建了一个新的资源属性列表，名为“Corporate Resource Property List”，其描述为“用于企业文档”。

### 示例 3：使用现有资源属性列表中的值来创建一个新的资源属性列表
```
PS C:\> Get-ADResourcePropertyList -Identity "Corporate Resource Property List" | New-ADResourcePropertyList -Name "Finance Resource Property List"
```

此命令使用“企业资源属性列表”中的属性值来创建一个新的资源属性列表。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Active Directory PowerShell 提供程序驱动器运行的。如果该 cmdlet 是从这样的提供程序驱动器运行的，则默认凭据将是与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将该对象设置为 `Credential` 参数的值。

如果该执行任务的账号没有目录级别的权限，Active Directory PowerShell 将返回一个终止错误。

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
指定对象的描述信息。该参数用于设置对象中 **Description** 属性的值。此属性的 LDAP 显示名称（**ldapDisplayName**）即为 “description”。

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
指定一个资源属性列表对象的实例，用作创建新的资源属性列表对象的模板。

你可以使用现有的资源属性列表对象的实例作为模板，或者可以通过使用 Windows PowerShell 命令行或脚本来创建一个新的资源属性列表对象。

方法 1：使用现有的资源属性列表对象作为新对象的模板。要获取现有资源属性列表对象的实例，可以使用诸如 **Get-ADResourcePropertyList** 这样的 cmdlet。然后将该对象传递给 **New-ADResourcePropertyList** cmdlet 的 `Instance` 参数，以创建一个新的资源属性列表对象。你可以通过设置相应的参数来覆盖新对象的属性值。

方法 2：创建一个新的 **ADResourcePropertyList**，并通过使用 Windows PowerShell 命令行界面来设置属性值。然后将这个对象传递给 **New-ADResourcePropertyList** cmdlet 的 Instance 参数，以创建新的资源属性列表对象。

注意：指定的属性不会经过验证；因此，尝试设置不存在或无法设置的属性将会引发错误。

```yaml
Type: ADResourcePropertyList
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定对象的名称。此参数用于设置 Active Directory 对象的 **Name** 属性。该属性的 LDAP 显示名称（**ldapDisplayName**）即为对象的名称。

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
指定是否阻止对象被删除。当此属性设置为 $True 时，如果不更改该属性的值，则无法删除相应的对象。此参数的可接受值为：

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
指定要连接的 AD DS 实例，请为相应的域名或目录服务器提供以下值之一。该服务可以是以下类型中的任意一种：AD LDS、AD DS 或 Active Directory 快照实例。

以下列方式之一指定 AD DS 实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

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
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft.ActiveDirectory.Management.ADResourcePropertyList

## 输出

### 无或 Microsoft.ActiveDirectory.Management.ADResourcePropertyList

## 备注
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADResourcePropertyList](./Get-ADResourcePropertyList.md)

[Remove-ADResourcePropertyList](./Remove-ADResourcePropertyList.md)

[Set-ADResourcePropertyList](./Set-ADResourcePropertyList.md)

