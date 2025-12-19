---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/get-gpinheritance?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-GPInheritance
---

# Get-GPInheritance

## 摘要

获取指定域或组织单位（OU）的组策略继承信息。

## 语法

```
Get-GPInheritance [-Target] <String> [-Domain <String>] [-Server <String>] [<CommonParameters>]
```

## 描述

`Get-GPInheritance` cmdlet 可以获取指定域或组织单元（OU）的组策略继承相关信息。

这些信息包括以下内容：

- A list of GPOs that are linked directly to the location (the **GpoLinks** property).
- A list of GPOs that are applied to the location when Group Policy is processed on a client (the
  **InheritedGpoLinks** property).
- Whether inheritance is blocked for the location (the **GpoInheritanceBlocked** property).

`InheritedGpoLinks` 属性包含一个列表，该列表列出了在客户端上处理组策略时应用于该组织单元（OU）或域的组策略对象（GPO）。这些 GPO 是按照它们被应用的优先级顺序排列的。这个列表包括以下内容：

- Inherited GPOs that are linked, enabled, and enforced at higher levels of the Group Policy
  hierarchy (for example, a site).
- GPOs that are linked and enabled directly at the specified location.
- If inheritance is not blocked for the specified location, inherited GPOs that are linked and
  enabled -- but not enforced -- at higher levels of the Group Policy hierarchy.

## 示例

### 示例 1：获取特定组织单元（OU）的组策略继承信息

```powershell
Get-GPInheritance -Target 'ou=MyOU,dc=contoso,dc=com'
```

```Output
ContainerName         : myou
ContainerType         : OU
Path                  : ou=myou,dc=contoso,dc=com
GpoInheritanceBlocked : No
GpoLinks              : {TestGPO-0, TestGPO-1, TestGPO-2, TestGPO-3...}
InheritedGpoLinks     : {TestGPO-2, TestGPO-3, Default Domain Policy}
```

这个命令用于获取`contoso.com`域中名为`MyOU`的组织单元（Organizational Unit, OU）的组策略继承信息。

**GpoLinks** 属性包含一个列表，其中列出了所有直接与该 GPO 相关联的 GPO（组策略对象），无论这些链接是否处于启用状态。

**InheritedGpoLinks** 属性包含一个列表，其中列出了在客户端上处理组策略时应用的所有 GPO（组策略对象）。`TestGPO-2` 和 `TestGPO-3` 出现在这个列表中，因为它们的链接已被启用。

默认的域策略组策略（GPO）是从 `contoso.com` 域继承而来的。如果继承被禁止，那么该组策略将不会显示在 **InheritedGpoLinks** 属性中；只有当其在某个域中被强制应用时，才会出现在该属性中。如果其链接在该域中被强制应用，它将会在列表中排在最前面。

### 示例 2：获取特定域的组策略继承设置

```powershell
Get-GPInheritance -Target "dc=contoso,dc=com" -Domain "contoso.com" -Server "DomainController1"
```

```Output
Name                  : contoso.com
ContainerType         : Domain
Path                  : dc=contoso,dc=com
GpoInheritanceBlocked : No
GpoLinks              : {Default Domain Policy}
InheritedGpoLinks     : {Default Domain Policy}
```

此命令用于获取 `contoso.com` 域的组策略继承信息。操作完成后会联系主机名为 `DomainController1` 的域控制器来完成相关任务。

在这个例子中，不需要使用 `Domain` 参数来显式指定域名。如果运行会话的用户所在的域（或者对于启动和关闭脚本来说，是指计算机所在的域）与目标域相同，或者它们之间存在信任关系，那么就不必指定 `Domain` 参数了。

### 示例 3：通过评估 SOM 对象来获取与特定组织单位关联的 GPO（组策略对象）

```powershell
(Get-GPInheritance -Target "ou=myou,dc=contoso,dc=com").GpoLinks |
    Foreach-Object { Get-GPO -Name ($_.DisplayName) }
```

```Output
DisplayName      : TestGPO-3
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : d02126d4-82e8-4e87-b4a0-2d44b6891411
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 2/27/2009 2:59:51 PM
ModificationTime : 2/27/2009 4:00:44 PM
UserVersion      : AD Version: 13, SysVol Version: 13
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :

DisplayName      : TestGPO-2
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : 375865b2-3b5f-480f-8f56-2a994ea6e725
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 2/26/2009 11:28:08 PM
ModificationTime : 3/1/2009 11:07:30 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 1, SysVol Version: 1
WmiFilter        :
```

这个命令会评估由 `Get-GPInheritance` 返回的 `Microsoft.GroupPolicy.SOM` 对象，并找出与 `MyOU` 组织单元关联的所有组策略对象（GPO）。你可以将这个命令的输出通过管道传递给其他 cmdlet 来设置这些 GPO 的属性。例如，你可以将输出结果传递给 `Set-GPPermissions` cmdlet，从而为与该组织单元关联的每个 GPO 授权管理员相应的管理权限。

SOM对象的`GpoLinks`属性包含该组织单位（OU）所有组策略对象链接（GPO links）的列表。列表中的每个对象都属于`Microsoft.GroupPolicy.GpoLink`类型。

该集合通过管道传递给 `Foreach-Object` 命令，该命令利用 `GpoLink` 对象的 **DisplayName** 属性来检索每个组策略对象（GPO）。

## 参数

### -Domain

指定此cmdlet对应的域名称。您必须提供该域的完全限定域名（FQDN）。

对于 `Get-GPInheritance` cmdlet 来说，这通常是指您想要检索继承信息的容器的域（即该容器所属的域或组织单元，OU）。如果指定的域与容器的域不同，则这两个域之间必须存在信任关系。

如果您不指定 **Domain** 参数，将使用当前会话的运行用户的域信息。如果该 cmdlet 是从计算机启动或关闭脚本中运行的，则会使用计算机的域信息。有关更多详细信息，请参阅完整帮助文档中的“注释”部分。

如果您指定的域名与当前会话的用户所使用的域名不同（或者对于启动/关闭脚本来说，是与计算机所在的域名不同），那么该域名与用户或计算机的域名之间必须存在信任关系。

您也可以使用**Domain**参数的内置别名**DomainName**来引用它。有关更多信息，请参阅[关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

### -Server

指定此 cmdlet 用于联系的域控制器的名称，以完成操作。您可以指定完整的域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统将会联系主域控制器（PDC）模拟器。

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

指定要通过其轻量级目录访问协议（LDAP）唯一名称来检索组策略继承信息的域或组织单元（Organizational Unit，简称OU）。例如，`contoso.com` 域中的 `MyOU` 组织单元可以表示为 `ou=MyOU,dc=contoso,dc=com`。

您也可以使用其内置别名**Path**来引用**Target**参数。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.GroupPolicy.Som

一个用于表示域（domain）或组织单位（organizational unit, OU）的对象。

## 输出

### Microsoft.GroupPolicy.Som

此cmdlet返回一个表示域或组织单元（OU）的对象。**GpoInheritanceBlocked**属性用于指示继承是否被阻止。您可以使用`Set-GPInheritance` cmdlet来修改该域或OU的继承设置。

## 备注

* You can use the **Domain** parameter to explicitly specify the domain for this cmdlet.

如果您没有明确指定域名，那么此cmdlet会使用默认域名。默认域名是指当前会话所运行的安全上下文用于访问网络资源时所使用的域名。这个域名通常就是运行该会话的用户的域名。例如，通过“程序文件”菜单打开Windows PowerShell来启动会话的用户所属的域，或者在`runas`命令中指定的用户所属的域。然而，计算机启动和关闭脚本是在`LocalSystem`账户的上下文中运行的。`LocalSystem`是一个内置的本地账户，它以计算机账户的身份访问网络资源。因此，当从这个启动或关闭脚本中运行此cmdlet时，默认域名就是计算机所连接的那个域名。

## 相关链接

[Set-GPInheritance](./Set-GPInheritance.md)

