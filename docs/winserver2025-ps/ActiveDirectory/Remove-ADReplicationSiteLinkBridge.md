---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-adreplicationsitelinkbridge?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADReplicationSiteLinkBridge
---

# 删除 ADReplicationSiteLinkBridge

## 摘要
从 Active Directory 中删除复制站点链接桥接（replication site link bridge）。

## 语法

```
Remove-ADReplicationSiteLinkBridge [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADReplicationSiteLinkBridge> [-Server <String>] [<CommonParameters>]
```

## 描述
`Remove-ADReplicationSiteLinkBridge` cmdlet 用于从 Active Directory 中删除复制站点链接桥（replication site link bridge）。站点链接桥用于连接两个或多个站点链接，并实现这些站点链接之间的数据传输功能。桥中的每个站点链接都必须与桥内的另一个站点链接共享相同的站点信息。

## 示例

### 示例 1：删除站点链接桥接（Site Link Bridge）
```
PS C:\> Remove-ADReplicationSiteLinkBridge -Identity "NorthAmerica-Asia"
```

这个命令会删除名为“NorthAmerica-Asia”的站点链接桥接器。

### 示例 2：删除经过筛选的站点链接桥接列表
```
PS C:\> Get-ADReplicationSiteLinkBridge -Filter "SiteLinksIncluded -eq 'Europe-Asia'" | Remove-ADReplicationSiteLinkBridge
```

这个命令会获取包含欧亚地区在内的站点链接桥接（site link bridges），并将其删除。

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
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行该任务的代理组件没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个无法终止的错误信息。

这个参数也可以通过数据流（pipeline）来获取相应的对象；或者你可以将这个参数设置为一个对象的实例。

```yaml
Type: ADReplicationSiteLinkBridge
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Server
默认的身份验证方法是“Negotiate”。

基本身份验证方法需要使用安全套接字层（SSL）连接。

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
展示了如果该 cmdlet 运行会发生的结果。不过实际上这个 cmdlet 并没有被运行。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction和-WarningVariable。有关更多信息，请参阅[关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft.ActiveDirectory.Management.ADReplicationSiteLinkBridge
一个站点链接桥接对象是通过*Identity*参数接收到的。

## 输出

### 无

## 备注
* By default, this cmdlet has the *Confirm* parameter set, which prompts you to confirm before a removal of the specified object type can occur. To bypass prompting for confirmation before removal, you can specify `-Confirm:$False` when using this cmdlet.

## 相关链接

[Get-ADReplicationSiteLinkBridge](./Get-ADReplicationSiteLinkBridge.md)

[New-ADReplicationSiteLinkBridge](./New-ADReplicationSiteLinkBridge.md)

[Set-ADReplicationSiteLinkBridge](./Set-ADReplicationSiteLinkBridge.md)

