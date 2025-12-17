---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-adreplicationsitelink?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADReplicationSiteLink
---

# 删除 AD 复制站点链接

## 摘要
删除用于管理复制的 Active Directory 站点链接。

## 语法

```
Remove-ADReplicationSiteLink [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADReplicationSiteLink> [-Server <String>] [<CommonParameters>]
```

## 描述
**Remove-ADReplicationSiteLink** cmdlet 用于删除用于管理 Active Directory 安装中两个站点之间复制流量的站点链接对象。有关站点链接的更多信息，请参阅 TechNet 文库中的 [创建站点链接设计](https://go.microsoft.com/fwlink/?LinkId=221870)：http://go.microsoft.com/fwlink/?LinkId=221870。

## 示例

### 示例 1：删除复制站点链接
```
PS C:\> Remove-ADReplicationSiteLink -Identity "Europe-Asia"
```

这个命令会删除名称为“Europe-Asia”的站点链接。

### 示例 2：获取经过过滤的复制站点链接列表并删除这些链接
```
PS C:\> Get-ADReplicationSiteLink -Filter "SitesIncluded -eq 'NorthAmerica'" | Remove-ADReplicationSiteLink
```

这个命令会获取包含“NorthAmerica”这个词的网站链接，并将它们删除。

## 参数

### -AuthType
指定要使用的身份验证方法。此参数的可接受值为：

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
在运行 cmdlet 之前会提示您进行确认。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从此类驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

如果执行任务的账号没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误（即程序异常退出）。

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
通过提供以下属性值之一来指定一个 Active Directory 对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，cmdlet会返回一个无法终止的错误信息。

这个参数也可以通过管道（pipeline）来获取相应的对象，或者你可以将该参数设置为一个对象的实例。

```yaml
Type: ADReplicationSiteLink
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
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

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft ActiveDirectory.Management.AdReplicationSiteLink
站点链接对象是通过“Identity”参数接收到的。

## 输出

### 无

## 备注
* By default, this cmdlet has the *Confirm* parameter set, which prompts you to confirm before a removal of the specified object type can occur. To bypass prompting for confirmation before removal, you can specify `-Confirm:$False` when using this cmdlet.

## 相关链接

[Get-ADReplicationSiteLink](./Get-ADReplicationSiteLink.md)

[New-ADReplicationSiteLink](./New-ADReplicationSiteLink.md)

[Set-ADReplicationSiteLink](./Set-ADReplicationSiteLink.md)

