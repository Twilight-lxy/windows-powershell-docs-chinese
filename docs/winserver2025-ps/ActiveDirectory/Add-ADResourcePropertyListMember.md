---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/add-adresourcepropertylistmember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ADResourcePropertyListMember
---

# 添加 AD 资源属性列表成员

## 摘要
将一个或多个资源属性添加到 Active Directory 中的资源属性列表中。

## 语法

```
Add-ADResourcePropertyListMember [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Identity] <ADResourcePropertyList>
 [-Members] <ADResourceProperty[]> [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述

`Add-ADResourcePropertyListMember` cmdlet 可以将一个或多个资源属性添加到 Active Directory 中的资源属性列表中。

## 示例

### 示例 1：向资源属性列表中添加成员

```powershell
$params = @{
    Identity = 'Global Resource Property List'
    Members = 'Country', 'Authors'
}
Add-ADResourcePropertyListMember @params
```

该命令将名为“Country”和“Authors”的资源成员添加到名为“Global Resource Property List”的列表中。

### 示例 2：向过滤后的资源属性列表中添加成员

```powershell
Get-ADResourcePropertyList -Filter "Name -like 'Corporate*'" |
    Add-ADResourcePropertyListMember -Members Country, Authors
```

该命令会获取所有名称以“Corporate”开头的资源属性列表，然后将其传递给`Add-ADResourcePropertyListMember`函数。`Add-ADResourcePropertyListMember`函数会将`Country`和`Authors`这两个资源属性添加到该列表中。

## 参数

### -AuthType

指定要使用的身份验证方法。该参数的可接受值包括：

- `Negotiate` or `0`
- `Basic` or `1`

默认的认证方法是`Negotiate`。

对于“基本”（Basic）认证方法来说，需要使用安全套接字层（Secure Sockets Layer，简称 SSL）进行连接。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADAuthType
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
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从此类驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01/User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将这个 **Credential** 对象设置为相应的参数。

如果执行任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

```yaml
Type: System.Management.Automation.PSCredential
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
- A GUID (**objectGUID**)

这个参数也可以通过数据流（pipeline）来获取该对象，或者你可以将这个参数设置为某个对象实例的值。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADResourcePropertyList
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Members

指定一组以逗号分隔的 `ADResourceProperty` 对象，将其添加到资源属性列表中。要标识每个对象，请使用以下属性值之一：

- Name
- Distinguished name
- GUID (**objectGUID**)

You can also provide objects to this parameter directly.

You cannot pass objects through the pipeline to this parameter.

```yaml
Type: Microsoft.ActiveDirectory.Management.ADResourceProperty[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru

Returns an object representing the item with which you're working. By default, this cmdlet doesn't
generate any output.

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server

指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下是指定 Active Directory 域服务实例的几种方式：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

- By using the **Server** value from objects passed through the pipeline
- By using the server information associated with the Active Directory Domain Services Windows
  PowerShell provider drive, when the cmdlet runs in that drive
- By using the domain of the computer running Windows PowerShell

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: System.Management.Automation.SwitchParameter
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

### 无值或 Microsoft.ActiveDirectory.Management_ADClaimTypeList

`Identity` 参数接收一个 `ADClaimTypeList` 对象。

## 输出

### 无值或 Microsoft.ActiveDirectory.Management_ADClaimTypeList

当指定 `PassThru` 参数时，该命令会返回修改后的 `ADClaimTypeList` 对象。默认情况下，此cmdlet不会生成任何输出。

## 备注

- This cmdlet does not work with a read-only domain controller.
- This cmdlet does not work with an Active Directory snapshot.

## 相关链接

[Remove-ADResourcePropertyListMember](./Remove-ADResourcePropertyListMember.md)
