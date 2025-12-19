---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/remove-gplink?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-GPLink
---

# 移除 GPL 链接

## 摘要

从站点、域或组织单位（OU）中删除GPO链接。

## 语法

### LinkbyGUID（默认值）

```
Remove-GPLink -Guid <Guid> -Target <String> [-Domain <String>] [-Server <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### LinkbyName

```
Remove-GPLink [-Name] <String> -Target <String> [-Domain <String>] [-Server <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-GPLink` cmdlet 用于移除组策略对象（GPO）与指定站点、域或组织单元（OU）之间的关联。该 cmdlet 不会删除实际的 GPO，也不会删除 GPO 与其他站点、域或 OU 之间的其他关联。

## 示例

### 示例 1：删除指定的 GPO 链接

```powershell
Remove-GPLink -Name "MyGPO" -Target "OU=MyOU,dc=contoso,dc=com"
```

```Output
DisplayName      : MyGPO
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : 375865b2-3b5f-480f-8f56-2a994ea6e725
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 2/26/2009 11:28:08 PM
ModificationTime : 3/5/2009 3:36:34 PM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 1, SysVol Version: 1
WmiFilter        :
```

此命令会删除名为 `MyGPO` 的组策略对象（GPO）与 `contoso.com` 域中的 `MyOU` 组织单元之间的关联。

### 示例 2：移除指定的 GPO 与默认站点之间的链接

```powershell
Remove-GPLink -Name "MyGPO" -Target "Default-First-Site-Name"
```

这个命令会删除名为“MyGPO”的组策略对象（GPO）与默认站点之间的关联。

### 示例 3：删除所有与指定组织单元关联的 GPO 的链接

```powershell
(Get-GPInheritance -Target "ou=MyOU,dc=contoso,dc=com").GpoLinks | Remove-GPLink
```

```Output
DisplayName      : TestGPO-3
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : d02126d4-82e8-4e87-b4a0-2d44b6891411
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 2/27/2009 2:59:51 PM
ModificationTime : 3/5/2009 3:36:37 PM
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
ModificationTime : 3/5/2009 3:36:34 PM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 1, SysVol Version: 1
WmiFilter        :
```

此命令会删除所有与 `contoso.com` 域中的 `MyOU` 组织单位关联的 GPO（组策略对象）所对应的链接。

这个 cmdlet 用于获取与某个组织单元（OU）相关联的 **Microsoft.GroupPolicy.Som** 对象。该 SOM 对象的 GpoLinks 属性中包含了所有与该 OU 相关联的组策略对象（GPO）的链接信息；不过，从更高级别的容器继承而来的链接不会被包含在内。这些链接信息会被传递给 `Remove-GPLink` 命令进行处理。最终，那些链接已被移除的 GPO 对象会返回结果。

## 参数

### -Domain

指定此cmdlet的域名。必须提供该域名的完全限定域名（FQDN）。

关于 `Remove-GPLink` cmdlet：

- The GPO that is linked must exist in this domain.

- The Active Directory container (site, domain, or OU) that is linked must exist in a domain that
  has a trust relationship with this domain.

注意：要指定要链接到的域名，请使用 **Target** 参数。

如果您没有指定 **Domain** 参数，那么将使用运行当前会话的用户所在的域。如果该cmdlet是从计算机启动或关闭脚本中执行的，那么将使用计算机所属的域。有关更多信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域名与当前会话的用户所使用的域名不同（或者对于启动/关闭脚本来说，是与计算机相关的域名不同），那么该域名与用户所在的域名或计算机所在的域名之间必须存在信任关系。

您也可以使用其内置别名**DomainName**来引用**Domain**参数。有关更多信息，请参阅[关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

### -Guid

通过其全局唯一标识符（GUID）指定要删除链接的组策略对象（GPO）。该 GUID 可唯一地标识该 GPO。

您也可以通过其内置的别名 `id` 和 `gpoid` 来引用 `Guid` 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: Guid
Parameter Sets: LinkbyGUID
Aliases: ID, GPOID

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name

根据显示名称指定要删除链接的GPO（组策略对象）。

显示名称在该域中并不保证是唯一的。如果该域中存在另一个具有相同显示名称的组策略对象（GPO），将会发生错误。您可以使用 **Guid** 参数来唯一标识一个 GPO。

您也可以通过其内置别名 **DisplayName** 来引用 **Name** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

### -Server

指定此 cmdlet 用于联系以完成操作的域控制器的名称。您可以指定完全限定的域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统会联系主域控制器（PDC）模拟器。

你也可以使用 **Server** 参数的内置别名 **DC** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

指定用于删除链接的站点、域或组织单元（OU）的轻量级目录访问协议（LDAP）区分名称。例如，对于 `contoso.com` 域中的 `MyOU` 组织单元，其 LDAP 区分名称为 `ou=MyOU,dc=contoso,dc=com`。

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

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction和-WarningVariable。有关更多信息，请参阅[about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.GroupPolicy.GpoLink

此 cmdlet 接受一个对象，该对象表示 GPO 与站点、域或组织单元（OU）之间的关联。

## 输出

### Microsoft.GroupPolicy.Gpo

此cmdlet返回了链接已被删除的GPO（组策略对象）。

## 备注

## 相关链接

[New-GPLink](./New-GPLink.md)

[Set-GPLink](./Set-GPLink.md)
