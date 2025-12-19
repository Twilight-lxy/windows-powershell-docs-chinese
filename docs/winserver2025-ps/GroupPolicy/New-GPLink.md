---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/new-gplink?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-GPLink
---

# New-GPLink

## 摘要

将GPO（组策略对象）链接到站点、域或组织单元（OU）。

## 语法

### LinkbyGUID（默认值）

```
New-GPLink -Guid <Guid> -Target <String> [-LinkEnabled <EnableLink>] [-Order <Int32>]
 [-Domain <String>] [-Server <String>] [-Enforced <EnforceLink>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### LinkbyName

```
New-GPLink [-Name] <String> -Target <String> [-LinkEnabled <EnableLink>] [-Order <Int32>]
 [-Domain <String>] [-Server <String>] [-Enforced <EnforceLink>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`New-GPLink` cmdlet 将一个 GPO（组策略对象）链接到一个站点、域或组织单元（OU）。默认情况下，该链接是处于启用状态的，这意味着在处理组策略时，GPO 的设置会根据继承规则和优先级被应用到目标 Active Directory 容器的相应级别。

您可以通过 GPO 的显示名称或其 GUID 来指定该 GPO；也可以将该 GPO 通过管道（pip）传递给相应的 cmdlet。要指定要链接到的站点、域或组织单元（OU），可以使用其轻量级目录访问协议（LDAP）标识名。此外，还可以使用其他参数来指定是否启用该链接、是否强制应用该链接，以及在站点、域或组织单元中应用的顺序。

## 示例

### 示例 1：创建一个组策略对象（GPO）并将其链接到域

```powershell
New-GPO -Name "MyGPO" | New-GPLink -Target "ou=MyOU,dc=contoso,dc=com" -LinkEnabled Yes
```

```Output
GpoId       : c25daa3e-5d05-43b3-87ca-0a237882fd63
DisplayName : MyGPO
Enabled     : True
Enforced    : False
Target      : OU=MyOU,DC=contoso,DC=com
Order       : 1
```

此命令会在用户的域名（或者对于启动/关闭脚本来说，是在计算机的域名）中创建一个名为“MyGPO”的组策略对象（GPO），并将其链接到“contoso.com”域中的“MyOU”组织单位。如果用户或计算机的域名与“contoso.com”不同，则这两个域名之间必须存在信任关系。

因为这个命令可以接受一个GPO作为输入，所以你可以在`New-GPO`和`New-GPLink`之间插入任何能够生成GPO的命令来配置该GPO。例如，你可以使用`Set-GPPermissions`命令来设置GPO的权限；使用`Set-GPRegistryValue` cmdlet来为GPO配置一个或多个基于注册表的策略设置；或者使用`Set-GPPrefRegistryValue` cmdlet来为GPO配置一个或多个注册表偏好设置项。

### 示例 2：将 GPO 链接到用户的域中

```powershell
New-GPLink -Name "TestGPO" -Target "dc=contoso,dc=com"
```

```Output
GpoId       : d5a3b4e7-e37a-4070-846c-568689eaa838
DisplayName : TestGPO
Enabled     : True
Enforced    : False
Target      : DC=contoso,DC=com
Order       : 2
```

此命令将用户所在域中的 `TestGPO` 组策略对象（对于启动或关闭脚本来说，也可以是计算机对应的组策略对象）与 `contoso.com` 域关联起来。如果用户的域或计算机的域与 `contoso.com` 不同，则这两个域之间必须存在信任关系。

### 示例 3：将组策略对象（GPO）链接到某个站点，并强制应用该链接

```powershell
New-GPLink -name "TestGPO" -Target "Test-Site" -Enforced Yes
```

```Output
GpoId       : d5a3b4e7-e37a-4070-846c-568689eaa838
DisplayName : TestGPO
Enabled     : True
Enforced    : True
Target      : CN=test-site,cn=Sites,CN=Configuration,DC=contoso,DC=com
Order       : 1
```

此命令将 `TestGPO` 这个组策略对象（GPO）链接到名为 `Test-Site` 的站点，并将该链接设置为“强制执行”模式。

## 参数

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

### -Domain

指定此cmdlet所属的域名。您必须提供该域名的完全限定域名（FQDN）。

关于 `New-GPLink` cmdlet：

- The GPO to link from must exist in this domain.

- The Active Directory container to link to must exist in a domain that has a trust relationship
  with this domain.

要指定要链接到的域名，请使用*Target*参数。

如果您没有指定**Domain**参数，那么将使用当前会话所运行的用户的域名。如果该cmdlet是从计算机启动或关闭脚本中运行的，那么将使用计算机的域名。有关更多信息，请参阅完整帮助文档中的“备注”部分。

如果您指定了一个与当前会话所使用的用户所在域（或者对于启动/关闭脚本来说，是与计算机所在的域）不同的域，那么该域与用户所在域或计算机所在域之间必须存在信任关系。

您也可以使用其内置别名 **DomainName** 来引用 **Domain**。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DomainName

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Enforced

指定是否强制应用组策略对象（GPO）链接。您可以选择“是”或“否”。默认情况下，GPO 链接不会被强制应用。

通过将 GPO 链接设置为“强制执行”（enforced），您可以确保以下几点：

- That the settings of the GPO cannot be blocked (by blocking inheritance) at a lower-level Active
  Directory container.
- That the settings of the GPO always take precedence over conflicting settings in GPOs that are
  linked to lower-level containers.

这个选项应该谨慎使用。随意使用这个选项会使得故障排查变得复杂。

```yaml
Type: EnforceLink
Parameter Sets: (All)
Aliases:
Accepted values: Unspecified, No, Yes

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Guid

通过其全局唯一标识符（GUID）来指定要链接的组策略对象（GPO）。该 GUID 可在域中唯一地识别该 GPO。

您也可以使用该参数的内置别名 **Id** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: Guid
Parameter Sets: LinkbyGUID
Aliases: ID

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LinkEnabled

指定是否启用了GPO链接。

这个参数的可接受值为：Yes（是）或No（否）。

默认情况下，所有组策略对象（GPO）链接都启用了组策略处理功能。你可以通过禁用特定站点、域或组织单元（OU）的相应GPO链接来完全阻止该GPO在该站点、域或OU中的应用。不过，禁用某个GPO链接并不会直接导致该GPO本身被禁用。如果该GPO还与其他站点、域或OU关联，那么组策略仍会继续针对所有已启用的链接处理该GPO。

```yaml
Type: EnableLink
Parameter Sets: (All)
Aliases:
Accepted values: Unspecified, No, Yes

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name

通过显示名称来指定要链接的GPO（组策略对象）。

显示名称在该域内并不保证是唯一的。如果该域中存在另一个具有相同显示名称的组策略对象（GPO），则会发生错误。你可以使用 **Guid** 参数来唯一地标识一个 GPO。

您也可以通过其内置别名**DisplayName**来引用**Name**参数。有关更多信息，请参阅[关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: LinkbyName
Aliases: DisplayName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Order

指定 GPO 链接的顺序。您可以指定一个介于 1 到当前目标站点、域或组织单位（OU）所连接的 GPO 链接数量加 1 之间的数字。

链接顺序决定了与同一 Active Directory 容器关联的 GPO（组策略对象）的应用优先级。在处理组策略时，链接顺序编号较高的 GPO 会先于链接顺序编号较低的 GPO 被应用。因此，当两个 GPO 包含相互冲突的设置时，链接顺序编号较低的 GPO 中的设置会覆盖链接顺序编号较高的 GPO 中的设置（因为后者被应用的顺序较晚）。较低的数字表示更高的优先级。

默认情况下，GPO 链接会被添加到优先级最低的位置，其链接顺序等于该容器中 GPO 链接的数量加一。链接顺序是一个动态值，因为随着 GPO 链接的添加或删除，这个顺序可能会发生变化。你可以使用 `Set-GPLink` cmdlet 来更改某个 GPO 链接的顺序。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server

指定此cmdlet用于联系以完成操作的域控制器的名称。您可以指定FQDN或主机名。

如果您不使用 **Server** 参数来指定名称，系统将会联系主域控制器（PDC）模拟器。

您也可以通过其内置别名“DC”来引用**Server**参数。有关更多信息，请参阅[关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DC

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Target

指定用于链接 GPO 的站点、域或组织单元（OU）的 LDAP 区分名称。例如，对于 `contoso.com` 域中的 `MyOU` 组织单元，其 LDAP 区分名称为 `ou=MyOU,dc=contoso,dc=com`。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftGROUPPolicy.Gpo

你可以将一个 GPO 对象通过管道（pipe）连接到 Active Directory 容器中。但是不支持包含来自不同域的 GPO 的集合（collections）。

## 输出

### MicrosoftGROUPPolicy.GpoLink

此 cmdlet 返回一个对象，该对象表示 GPO 与站点、域或组织单元（OU）之间的关联关系。

## 备注

* To link a GPO to a site, domain, or OU, you must have Link GPOs permission on that site, domain,
  or OU. By default, only domain administrators and enterprise administrators have this privilege
  for domains and OUs. Enterprise administrators and domain administrators of the forest root domain
  have this privilege for sites.

你可以使用 **Domain** 参数来明确指定此 cmdlet 的域名。

如果您没有明确指定域名，该cmdlet会使用默认域名。默认域名是指当前会话运行的安全上下文用于访问网络资源的那个域名。这个域名通常就是启动该会话的用户所属的域名；例如，通过“程序文件”菜单打开Windows PowerShell来启动会话的用户所在的域，或者在`runas`命令中指定的用户所属的域。然而，计算机启动和关闭脚本是在`LocalSystem`账户的上下文中运行的。`LocalSystem`是一个内置的本地账户，它以计算机账户的身份访问网络资源。因此，当从这个启动或关闭脚本中运行该cmdlet时，默认域名就是计算机所加入的域。

## 相关链接

[Remove-GPLink](./Remove-GPLink.md)

[Set-GPLink](./Set-GPLink.md)

[Set-GPPrefRegistryValue](./Set-GPPrefRegistryValue.md)

[Set-GPRegistryValue](./Set-GPRegistryValue.md)

