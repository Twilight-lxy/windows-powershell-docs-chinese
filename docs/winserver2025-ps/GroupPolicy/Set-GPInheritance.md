---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/set-gpinheritance?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-GPInheritance
---

# Set-GPInheritance

## 摘要

允许或禁止指定域名或组织单元继承相关属性（如样式、设置等）。

## 语法

```
Set-GPInheritance [-Target] <String> -IsBlocked <BlockInheritance> [-Domain <String>]
 [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Set-GPInheritance` cmdlet 可以阻止或允许指定域或组织单位（OU）的继承设置。

组策略对象（GPOs）是根据组策略的层次结构按以下顺序应用的：本地GPO、与站点关联的GPO、与域关联的GPO、与组织单位（OU）关联的GPO。默认情况下，Active Directory容器会继承来自层次结构中更高层级上应用的GPO的设置。如果禁用了继承功能，那么与更高级别的站点、域或组织单位关联的GPO中的设置将不会自动应用到指定的域或组织单元中，除非明确强制执行了该GPO的链接。

您可以使用 **Target** 参数来指定域或组织单元（OU）的轻量级目录访问协议（LDAP）区分名称，并使用 **IsBlocked** 参数来指定是阻止还是允许继承功能的操作。

## 示例

### 示例 1：域中某个组织单元（OU）的块继承设置

```powershell
Set-GPInheritance -Target "ou=MyOU,dc=contoso,dc=com" -IsBlocked Yes
```

```Output
Name                  : MyOU
ContainerType         : OU
Path                  : ou=MyOU,dc=contoso,dc=com
GpoInheritanceBlocked : Yes
GpoLinks              : {TestGPO-1, TestGPO-2}
InheritedGpoLinks     : {TestGPO-1, TestGPO-2}
```

此命令会阻止名为“MyOU”的组织单位（OU）在`contoso.com`域中的继承功能。那些链接到更高级别站点或域的组策略对象（GPO），或者链接到“MyOU”这个OU的父级OU的GPO，在客户端处理该OU的组策略时将不会被应用，除非这些链接被强制执行。

由于继承功能被禁用了，因此只有那些直接链接到`MyOU`的GPO（组策略对象），以及那些在更高级别的容器中被强制应用的GPO，才会出现在`InheritedGpoLinks`列表中。

### 示例 2：为某个域名解除继承限制

```powershell
Set-GPInheritance -Target "dc=northwest,dc=contoso,dc=com" -IsBlocked No
```

此命令会解除 `northwest.contoso.com` 域名的继承限制。当在客户端上处理组策略（Group Policy）时，与上级站点或域名关联的组策略对象（GPOs）将会应用到该域名上。

### 示例 3：解除域中某个组织单元（OU）的继承限制

```powershell
Set-GPInheritance -Target "ou=MyOU,dc=contoso,dc=com" -IsBlocked No
```

```Output
Name                  : MyOU
ContainerType         : OU
Path                  : ou=MyOU,dc=contoso,dc=com
GpoInheritanceBlocked : No
GpoLinks              : {TestGPO-1, TestGPO-2}
InheritedGpoLinks     : {TestGPO-1, TestGPO-2, Default Domain Policy}
```

此命令会解除名为 `MyOU` 的组织单元（OU）在 `contoso.com` 域中的继承限制。当客户端处理该 OU 的组策略时，链接到更高级别站点或域的 GPO，以及链接到 `MyOU` 作为父级组织的 OU 的 GPO，都会被应用到该 OU 上。

由于继承功能没有被阻止，因此从上级容器继承而来的 GPO 会出现在“InheritedGpoLinks”列表中（与直接链接到该组织单元 (OU) 的 GPO 一起）。例如，“Default Domain Policy” GPO 是在域级别被链接的。

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

指定此 cmdlet 所使用的域名。您必须提供该域名的完全限定域名（FQDN）。

对于 `Set-GPInheritance` cmdlet 来说，通常需要指定的是你想要阻止或允许继承设置的 Active Directory 容器（域或组织单元，OU）。如果该 cmdlet 所使用的域与容器所在的域不同，则这两个域之间必须存在信任关系。

如果您不指定 **Domain** 参数，系统将使用当前会话所运行的用户的域信息。如果该 cmdlet 是从计算机启动或关闭脚本中执行的，则系统会使用计算机的域信息。有关更多详细信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域与当前会话所使用的用户的域不同（或者对于启动/关闭脚本来说，是与计算机所在的域不同），那么该域与用户或计算机所在域之间必须存在信任关系。

您也可以使用内置别名 **DomainName** 来引用 **Domain** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DomainName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IsBlocked

用于指示是否阻止该域或组织单元（OU）继承某些设置。必须指定“是”（Yes）或“否”（No）。

对于这种对象类型，允许使用以下值。

```yaml
Type: BlockInheritance
Parameter Sets: (All)
Aliases:
Accepted values: No, Yes

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server

指定此cmdlet用于联系以完成操作的域控制器的名称。您可以指定完全合格的域名（FQDN）或主机名。

如果您没有使用**Server**参数来指定名称，系统将会联系主域控制器（Primary Domain Controller，简称PDC）的仿真器。

您也可以使用其内置别名“DC”来引用**Server**参数。

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

通过LDAP区分名称指定要阻止或允许继承操作的域或组织单元（OU）。例如，`contoso.com` 域中的 `MyOU` 组织单元可以表示为 `ou=MyOU,dc=contoso,dc=com`。

您也可以使用 **Target** 参数的内置别名 **Path** 来引用它。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: Path

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.GroupPolicy.Som

这个cmdlet接受一个表示域或组织单元（OU）的对象作为输入。

## 输出

### Microsoft.GroupPolicy.Som

此cmdlet在操作应用后返回一个表示该域或组织单元（OU）的对象。该对象默认显示的属性用于描述该域或OU的组策略继承信息。**GpoInheritanceBlocked**属性指示继承是否被阻止。

## 备注

* GPO links that are enforced cannot be blocked. This cmdlet should be used sparingly. Casual use of
  this cmdlet can complicate troubleshooting.

你可以使用 **Domain** 参数来明确指定此 cmdlet 的域名。

如果您没有明确指定域名，该cmdlet会使用默认域名。默认域名是指当前会话运行的安全上下文用于访问网络资源时所使用的域名。这个域名通常就是启动该会话的用户所属的域名；例如，通过“Program Files”菜单打开Windows PowerShell来启动会话的用户对应的域名，或者在“runas”命令中指定的用户对应的域名。不过，计算机启动和关闭脚本是在“LocalSystem”账户的上下文中运行的。“LocalSystem”是一个内置的本地账户，它以计算机账户的身份访问网络资源。因此，当从启动或关闭脚本中运行该cmdlet时，默认域名就是计算机所属的域名。

## 相关链接

[Get-GPInheritance](./Get-GPInheritance.md)

