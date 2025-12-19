---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/backup-gpo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Backup-GPO
---

# 备份组策略对象（Backup-GPO）

## 摘要

备份一个GPO或域中的所有GPO。

## 语法

### BackupOne（GUID）（默认设置）

```
Backup-GPO -Guid <Guid> -Path <String> [-Comment <String>] [-Domain <String>] [-Server <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### BackupOne（名称）

```
Backup-GPO [-Name] <String> -Path <String> [-Comment <String>] [-Domain <String>]
 [-Server <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### BackupAll

```
Backup-GPO -Path <String> [-Comment <String>] [-Domain <String>] [-Server <String>] [-All]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Backup-GPO` cmdlet 可将指定的组策略对象（GPO）或域中的所有 GPO 备份到备份目录中。备份目录和 GPO 必须已经存在。

## 示例

### 示例 1：将 GPO 备份到特定目录

```powershell
Backup-Gpo -Name TestGPO -Path C:\GpoBackups -Comment "Weekly Backup"
```

```output
DisplayName     : TestGPO
GpoId           : 35c12ab3-956c-45d5-973b-46b17d225f47
Id              : 2b509d4e-40f5-4337-82f7-458584555d0c
BackupDirectory : C:\GpoBackups
CreationTime    : 2/25/2009 8:48:19 PM
DomainName      : contoso.com
Comment         : Weekly Backup
```

该命令将 `TestGPO` GPO 备份到 `C:\GpoBackups` 目录中。指定的注释也会被包含在 GPO 备份文件中。

### 示例 2：将具有指定 GUID 的 GPO 备份到指定的目录中

```powershell
$params = @{
    GUID   = 'fa4a9473-6e2a-4b87-ab78-175e68d97bde'
    Domain = 'contoso.com'
    Server   = 'DC1'
    Path = '\\Server1\GpoBackups'
}
Backup-Gpo @params
```

此命令会将具有指定 **GUID** 的 GPO 备份到 `contoso.com` 域中的 `\\Server1\GpoBackups` 目录中。操作过程中会联系位于 `DC1` 的域控制器以完成备份任务。

如果运行会话的用户所在域（或者对于启动和关闭脚本来说，是计算机所在的域）与 `contoso.com` 域不同，则这两个域之间必须存在信任关系，否则命令将无法执行。

### 示例 3：为正在运行会话的用户备份该域中的所有组策略对象（GPO）

```powershell
Backup-Gpo -All -Path "\\Server1\GpoBackups"
```

此命令会将运行该会话的用户所在域中的所有 GPO（对于启动和关闭脚本而言，则是相应的计算机上的 GPO）备份到 `\\Server1\GpoBackups` 目录中。

## 参数

### -All

指定对域中的所有组策略对象（GPO）进行备份。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: BackupAll
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Comment

为备份的GPO指定一条注释。注释字符串必须用双引号或单引号括起来，且可以包含最多2,047个字符。

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

在运行cmdlet之前会提示您进行确认。

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

指定此 cmdlet 所使用的域。您必须提供该域的完全限定域名（FQDN），例如：sales.contoso.com。

对于 `Backup-GPO` cmdlet 来说，要备份的 GPO 必须存在于当前域中。

如果您没有指定 **Domain** 参数，那么将使用当前会话所运行的用户的域信息。（如果该 cmdlet 是通过计算机启动或关闭脚本来执行的，那么将使用计算机的域信息。）有关更多详细信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域名与当前会话的用户所使用的域名不同（或者对于启动/关闭脚本来说，是与计算机所属的域名不同），那么该域名与用户所在的域名（或计算机所属的域名）之间必须存在信任关系。

您也可以使用该域名的内置别名“domain name”来引用它。有关更多信息，请参阅[关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

通过其全局唯一标识符（GUID）指定要备份的组策略对象（GPO）。该 GUID 能唯一地识别该 GPO。

您也可以使用其内置别名 **Id** 来引用 **Guid** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: Guid
Parameter Sets: BackupOne(GUID)
Aliases: Id

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name

根据显示名称指定要备份的GPO（组策略对象）。

显示名称在该域中不保证是唯一的。如果该域中存在另一个具有相同显示名称的组策略对象（GPO），则会发生错误。你可以使用 **Guid** 参数来唯一标识一个 GPO。

您也可以通过其内置别名 **DisplayName** 来引用 Name 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: BackupOne(Name)
Aliases: DisplayName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Path

指定备份目录的路径；例如，`C:\Backups` 或 `\\MyServer\Backups`。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: BackupLocation

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server

指定此cmdlet用于联系以完成操作的域控制器的名称。您可以指定完全限定域名（FQDN）或主机名。

如果您不使用 **Server** 参数来指定名称，系统将会联系 PDC 模拟器。

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

展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft(GroupPolicy.Gpo)

需要备份的一个组策略对象（GPO）。不支持包含来自不同域的GPO的集合。

## 输出

### Microsoft(GroupPolicy.Gpo)Backup

这个cmdlet返回一个对象，该对象表示存储备份GPO设置文件的文件。

## 备注

* You can use the **Domain** parameter to explicitly specify the domain for this cmdlet.

如果您没有明确指定域名，该cmdlet会使用默认域名。默认域名是指当前会话所运行的安全上下文用于访问网络资源时所使用的域名。这个域名通常是与运行该会话的用户相关的域名；例如，通过“程序文件”菜单打开Windows PowerShell来启动会话的用户的域名，或者在“runas”命令中指定的用户的域名。然而，计算机启动和关闭脚本是在LocalSystem账户的上下文中运行的。LocalSystem账户是一个内置的本地账户，它以计算机的身份访问网络资源。因此，当从这个启动或关闭脚本中运行该cmdlet时，默认域名就是计算机所属的域名。

## 相关链接

[导入GPO](./Import-GPO.md)

[恢复GPO](./Restore-GPO.md)

