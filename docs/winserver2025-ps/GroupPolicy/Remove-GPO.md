---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/remove-gpo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-GPO
---

# 删除GPO

## 摘要

删除一个组策略对象（GPO）。

## 语法

### 使用 ByGUID（默认值）

```
Remove-GPO -Guid <Guid> [-Domain <String>] [-Server <String>] [-KeepLinks] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 按名称查找

```
Remove-GPO [-Name] <String> [-Domain <String>] [-Server <String>] [-KeepLinks] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Remove-GPO` cmdlet 会从目录服务和系统卷文件夹（SysVol）中删除组策略对象（GPO）及其相关数据。

## 示例

### 示例 1：通过 GUID 删除 GPO

```powershell
Remove-GPO -Guid 50cc3e45-0b14-46dd-8b4d-afa012bc331c -Domain "contoso.com" -KeepLinks
```

此命令会从 `contoso.com` 域中删除 GUID 为 `50cc3e45-0b14-46dd-8b4d-afa012bc331c` 的 GPO。由于指定了 **KeepLinks** 参数，因此该 GPO 与所有站点之间的链接以及该 GPO 与域中所有容器之间的链接都将被保留。

### 示例 2：按名称删除 GPO

```powershell
Remove-GPO -Name "TestGPO"
```

该命令会从正在运行会话的用户所在的域中删除名为 `TestGPO` 的组策略对象（GPO）。由于未指定 `KeepLinks` 参数，因此 GPO 与域内所有站点之间的链接以及 GPO 与域内所有容器之间的链接都会被删除。

## 参数

### -Confirm

在运行cmdlet之前，会提示您进行确认。

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

指定您希望从中删除 GPO 的域。必须提供该域的完全限定域名（FQDN）。

如果您没有指定**Domain**参数，那么将使用您登录所使用的计算机的域名。

如果您指定的域名与用户对象的所属域名不同，则您想要从中删除 GPO 的域与用户对象的所属域之间必须存在信任关系。

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

### -Guid

通过全局唯一标识符（GUID）指定要删除的组策略对象（GPO）。该 GUID 可唯一地识别该 GPO。

你也可以使用该参数的内置别名 **Id** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: Guid
Parameter Sets: ByGUID
Aliases: ID, GPOID

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -KeepLinks

这表示当GPO被删除时，该cmdlet会保留对该GPO的链接，包括其在指定域中的组织单元（OU）以及所有站点的相关信息。

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

### -Name

指定此cmdlet要根据其显示名称删除的GPO（组策略对象）。

显示名称在域内并不保证是唯一的。如果该域中存在另一个具有相同显示名称的 GPO，将会出现错误。你可以使用 **Guid** 参数来唯一地标识一个 GPO。

您也可以使用其内置别名 **DisplayName** 来引用 **Name** 参数。有关更多信息，请参阅 [关于别名](/powershell.module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: ByName
Aliases: DisplayName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Server

指定此 cmdlet 用于联系的域控制器的名称，以便完成操作。您可以指定完全合格的域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统会联系主域控制器（PDC）模拟器。

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

### -WhatIf

展示了如果该cmdlet被运行会发生什么情况。但实际上该cmdlet并未被运行。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.GroupPolicy.Gpo

这个cmdlet用于将需要删除的GPO传输出去（即将其从当前环境移除）。不支持包含来自不同域的GPO的集合。

## 输出

### 无

此cmdlet不会生成任何输出。

## 备注

* When you remove a GPO, by default, all links to that GPO in the domain of the GPO are deleted. To
  remove a link to a GPO, you must have permission to link Group Policy Objects for the
  organizational unit or domain. If you do not have rights to delete a link, the GPO is deleted, but
  the link remains. Links from other domains and sites are not removed. The link to a deleted GPO
  appears in the GPMC as Not Found. To remove Not Found links, you must either have permission on
  the site, domain, or organizational unit containing the link, or ask someone with sufficient
  rights to delete it.

## 相关链接

[Get-GPO](./Get-GPO.md)

[New-GPO](./New-GPO.md)

