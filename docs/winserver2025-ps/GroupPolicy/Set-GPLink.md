---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/set-gplink?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-GPLink
---

# Set-GPLink

## 摘要

设置指定 GPO 链接的属性。

## 语法

### LinkGUID（默认值）

```
Set-GPLink -Guid <Guid> -Target <String> [-LinkEnabled <EnableLink>] [-Order <Int32>]
 [-Domain <String>] [-Server <String>] [-Enforced <EnforceLink>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### LinkName

```
Set-GPLink [-Name] <String> -Target <String> [-LinkEnabled <EnableLink>] [-Order <Int32>]
 [-Domain <String>] [-Server <String>] [-Enforced <EnforceLink>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Set-GPLink` cmdlet 用于设置组策略对象（Group Policy Object，简称 GPO）链接的属性。

你可以设置以下属性：

- Enabled. If the GPO link is enabled, the settings of the GPO are applied when Group Policy is
  processed for the site, domain or OU.

- Enforced.
  If the GPO link is enforced, it cannot be blocked at a lower-level (in the Group Policy
  processing hierarchy) container.

- Order.
  The order specifies the precedence that the settings of the GPO take over conflicting
  settings in other GPOs that are linked, and enabled, to the same site, domain, or OU.

## 示例

### 示例 1：启用 GPO 与 OU 之间的关联

```powershell
Set-GPLink -Name TestGPO -Target "ou=MyOU,dc=contoso,dc=com" -LinkEnabled Yes
```

```Output
GpoId       : c25daa3e-5d05-43b3-87ca-0a237882fd63
DisplayName : Test2GPO
Enabled     : True
Enforced    : False
Target      : OU=MyOU,DC=contoso,DC=com
Order       : 1
```

此命令用于在 `contoso.com` 域中，将名为 `TestGPO` 的组策略对象（Group Policy Object, GPO）与名为 `MyOU` 的组织单元（Organizational Unit, OU）关联起来。`Enforced` 和 `Order` 属性保持不变。

### 示例 2：启用 GPO 与两个域之间的关联

```powershell
$params = @{
    Name        = 'TestGPO'
    Domain      = "north.contoso.com"
    Target      = "dc=south,dc=contoso,dc=com"
    LinkEnabled = $true
    Enforced    = $true
    Order       = 1
}
Set-GPLink @params
```

此命令用于在 `north.contoso.com` 域中的名为 `TestGPO` 的组策略对象（GPO）与 `south.contoso.com` 域之间建立链接。该链接被设置为“强制执行”模式，因此无法在较低级别的容器（例如 `south_contoso.com` 域中的组织单位（OU））中被阻止。由于链接的优先级被设置为 “1”，因此在处理 `south.contoso.com` 域容器的组策略时，`TestGPO` 的设置将具有最高的优先级（强制执行的链接除外）。

### 示例 3：设置 GPO 与测试站点之间链接的强制属性

```powershell
Set-GPLink -Guid 77c5285d-952e-4559-94ef-a02f5c107799 -Target "Test-Site" -Enforced Yes
```

```Output
GpoId       : 77c5285d-952e-4559-94ef-a02f5c107799
DisplayName : TestGPO
Enabled     : True
Enforced    : True
Target      : CN=test-site,cn=Sites,CN=Configuration,DC=contoso,DC=com
Order       : 1
```

此命令用于设置 ID 为 `77c5285d-952e-4559-94ef-a02f5c107799` 的 GPO 与 `Test-Site` 之间的链接的“强制属性”（enforced property）。对于位于 Group Policy 层次结构较低级别的容器而言，无法阻止该链接继承相关设置。

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

指定此 cmdlet 所使用的域。您必须提供该域的完全限定域名（FQDN）。

关于 `Set-GPLink` cmdlet：

- The GPO that is linked from must exist in this domain.

- The Active Directory container that is linked to must exist in a domain that has a trust
  relationship with this domain.

要指定要链接到的域名，请使用**Target**参数。

如果您没有指定 **Domain** 参数，将使用当前会话所运行用户的域名。如果该 cmdlet 是从计算机启动或关闭脚本中运行的，则将使用计算机的域名。有关更多信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域名与当前会话所使用的用户的域名不同（或者对于启动/关闭脚本来说，是与计算机相关的域名不同），那么该域名与用户或计算机的域名之间必须存在信任关系。

您也可以使用该参数的内置别名 **DomainName** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

指定是否强制执行GPO链接。您可以选择“是”或“否”。默认情况下，GPO链接不会被强制执行。

通过将 GPO 链接设置为“强制执行”（enforced），您可以确保以下几点：

- That the settings of the GPO cannot be blocked (by blocking inheritance) at a lower-level Active
  Directory container.

- That the settings of the GPO always take precedence over conflicting settings in GPOs that are
  linked to lower-level containers.

这个选项应该谨慎使用。随意使用该选项会使故障排查变得更加复杂。

对于这种对象类型，允许使用以下值。

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

通过该链接的全局唯一标识符（GUID）来指定相应的组策略对象（GPO）。GUID能够唯一地识别这个GPO。

您也可以使用其内置别名 **Id** 来引用 **Guid** 参数。

```yaml
Type: Guid
Parameter Sets: LinkGUID
Aliases: ID, GPOID

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LinkEnabled

指定是否启用GPO链接。可以选择“是”或“否”。

默认情况下，所有组策略对象（GPO）链接都启用了组策略处理功能。你可以通过禁用某个站点、域或组织单元（OU）对应的GPO链接来完全阻止该GPO在该站点、域或OU中的应用。不过，禁用GPO链接并不会导致该GPO本身被禁用。如果该GPO还与其他站点、域或OU关联，那么组策略仍会继续针对所有已启用的链接对该GPO进行处理。

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

通过链接的显示名称来指定该链接对应的GPO（组策略对象）。

显示名称在域内不保证是唯一的。如果域中存在另一个具有相同显示名称的 GPO，将会发生错误。您可以使用 **Guid** 参数来唯一地标识一个 GPO。

您也可以通过其内置别名 **DisplayName** 来引用 **Name** 参数。

```yaml
Type: System.String
Parameter Sets: LinkName
Aliases: DisplayName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Order

指定GPO链接的顺序。您可以指定一个介于1和当前目标站点、域或组织单元（OU）所关联的GPO链接数量之间的数值（该数值需加上1）。

链接顺序决定了链接到同一 Active Directory 容器的 GPO（组策略对象）的优先应用顺序。在处理组策略时，链接顺序号较高的 GPO 会先于链接顺序号较低的 GPO 被执行。因此，当两个 GPO 包含相互冲突的设置时，链接顺序号较低的 GPO 中的设置会覆盖链接顺序号较高的 GPO 中的设置（因为后者被执行的顺序较晚）。较低的链接顺序号表示更高的优先级。

默认情况下，GPO链接会被添加到优先级最低的位置（其链接顺序等于该容器中所有GPO链接的数量加一）。链接顺序是一个动态值，因为随着GPO链接的添加或删除，这个顺序可能会发生变化。

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

指定此 cmdlet 用于联系以完成操作的域控制器的名称。您可以指定完全合格的域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统将会联系主域控制器（PDC）的仿真器。

您也可以通过其内置别名“DC”来引用**Server**参数。

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

指定链接所对应的站点、域或组织单元（OU）的轻量级目录访问协议（LDAP）规范名称。例如，对于位于 `contoso.com` 域中的 `MyOU` 组织单元，其 LDAP 规范名称为 `ou=MyOU,dc=contoso,dc=com`。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被执行。

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

### Microsoft.GroupPolicy.GpoLink

GPO与站点、域或组织单元（OU）之间的链接。

## 输出

### Microsoft.GroupPolicy.GpoLink

此cmdlet在更改应用后会返回GPO链接。

## 备注

* You can use the **Domain** parameter to explicitly specify the domain for this cmdlet.

如果您没有明确指定域名，该 cmdlet 会使用默认域名。默认域名是指当前会话所运行的安全上下文用于访问网络资源时使用的域名。这个域名通常就是运行该会话的用户的域名。例如，通过“程序文件”菜单启动 Windows PowerShell 的用户的域名，或者在 `runas` 命令中指定的用户的域名。然而，计算机启动和关闭脚本是在 `LocalSystem` 账户的上下文中运行的。`LocalSystem` 账户是一个内置的本地账户，它以计算机的身份访问网络资源。因此，当从这个启动或关闭脚本中运行该 cmdlet 时，默认域名就是计算机所属的域名。

## 相关链接

[New-GPLink](./New-GPLink.md)

[Remove-GPLink](./Remove-GPLink.md)

