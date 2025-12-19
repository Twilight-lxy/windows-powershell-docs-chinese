---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/new-gpstartergpo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-GPStarterGPO
---

# New-GPStarterGPO

## 摘要

创建一个初始组策略对象（Starter GPO）。

## 语法

```
New-GPStarterGPO [-Name] <String> [-Comment <String>] [-Domain <String>] [-Server <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`New-GPStarterGPO` cmdlet 用于创建一个具有指定名称的起始组策略对象（Starter GPO）。如果在调用 `New-GPStarterGPO` cmdlet 时 `SYSVOL` 目录中还不存在 “Starter GPOs” 文件夹，那么该文件夹将会被创建，并且会填充随 Group Policy 一起提供的八个默认的起始组策略对象。

## 示例

### 示例 1：创建一个起始组策略对象（GPO）

```powershell
New-GPStarterGPO -Name StarterSecurity -Comment "Security Template"
```

此命令创建了一个名为“StarterSecurity”的启动组策略对象（Starter GPO）。该启动组策略对象上附有指定的注释。

## 参数

### -Comment

为新创建的“Starter GPO”指定一条注释。注释字符串必须使用双引号或单引号括起来，且长度最多为2,047个字符。

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

指定此cmdlet所使用的域。必须提供该域的完全限定域名（FQDN）。

不支持跨域创建起始GPO（Starter GPO）。如果您指定的域名与当前会话运行用户的所在域名不同，将会出现错误。

如果您没有指定 **Domain** 参数，系统将使用当前会话所运行的用户的域信息。

您也可以使用内置别名 **DomainName** 来引用 **Domain** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

### -Name

指定新的“Starter GPO”（启动组策略对象）的显示名称。

如果域中存在另一个具有相同显示名称的“Starter GPO”（启动组策略对象），则会发生错误。

您也可以通过其内置别名 **DisplayName** 来引用 **Name** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DisplayName

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server

指定此 cmdlet 用于联系以完成操作的域控制器的名称。您可以指定完全限定的域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统将会联系主域控制器（Primary Domain Controller，简称 PDC）的仿真器。

您也可以使用服务器参数的内置别名“DC”来引用它。有关更多信息，请参阅[关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

展示了如果该cmdlet被运行会发生的结果。但实际上该cmdlet并没有被运行。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

这个cmdlet不接受任何输入。

## 输出

### Microsoft(GroupPolicy.StarterGpo)

此cmdlet会返回创建的初始GPO（Starter GPO）。

## 备注

## 相关链接

[Get-GPStarterGPO](./Get-GPStarterGPO.md)

[New-GPO](./New-GPO.md)

