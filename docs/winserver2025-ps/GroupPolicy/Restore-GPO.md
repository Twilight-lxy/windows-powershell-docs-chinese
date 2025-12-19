---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/restore-gpo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Restore-GPO
---

# 恢复组策略对象（GPO）

## 摘要

从一个或多个GPO备份文件中恢复一个GPO或域中的所有GPO。

## 语法

### RestoreFromBackupId（默认值）

```
Restore-GPO -BackupId <Guid> -Path <String> [-Domain <String>] [-Server <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

###RestoreFromGpo(GUID)

```
Restore-GPO -Guid <Guid> -Path <String> [-Domain <String>] [-Server <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### RestoreFromGpo(Name)

```
Restore-GPO [-Name] <String> -Path <String> [-Domain <String>] [-Server <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### RestoreAll

```
Restore-GPO -Path <String> [-Domain <String>] [-Server <String>] [-All] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Restore-GPO` cmdlet 将组策略对象（GPO）的备份恢复到其最初保存的域中。如果原始域不可用，或者该 GPO 在该域中已不存在，则此 cmdlet 会失败。

你可以：

- Use the **Guid** parameter or the *Name* parameter to restore a GPO from its most recent backup.

- Use the **All** parameter to restore all GPOs in the domain from their most recent backups.

- Use the **BackupID** parameter to restore a GPO from a specific backup.
This parameter enables you to restore a GPO from a backup prior to the most recent one.

## 示例

#### 示例 1：从目录中恢复组策略对象（GPO）

```powershell
Restore-GPO -Name "TestGPO" -Path "\\Server1\Backups"
```

该命令从 `\\Server1\Backups` 目录中恢复名为 `TestGPO` 的组策略对象（Group Policy Object，简称 GPO）。系统会恢复最新的备份版本。

### 示例 2：使用 GPO 的 GUID 从目录中恢复 GPO

```powershell
Restore-GPO -GUID fa4a9473-6e2a-4b87-ab78-175e68d97bde -Path "\\Server1\Backups"
```

此命令会从 `\\Server1\Backups` 目录中恢复具有 GUID `fa4a9473-6e2a-4b87-ab78-175e68d97bde` 的 GPO。系统将恢复最新的备份版本。

### 示例 3：恢复域中所有之前已备份到某个目录中的 GPO（组策略对象）

```powershell
Restore-GPO -All -Domain "contoso.com" -Path "\\Server1\Backups"
```

此命令会恢复之前备份到 `\\Server1\Backup` 的 `contoso.com` 域中的所有 GPO（组策略对象）。每个 GPO 都会使用其最新的备份数据进行恢复。

如果运行会话的用户所在的域（或者对于启动/关闭脚本来说，是指计算机所在的域）与 `contoso.com` 域不同，那么这两个域之间必须存在信任关系，否则命令将无法执行。

### 示例 4：使用备份ID恢复GPO

```powershell
Restore-GPO -BackupId 0fc29b3c-fb83-4076-babb-6194c1b4fc26 -Path "\\Server1\Backups"
```

此命令会根据 **BackupID** 参数指定的备份文件来恢复一个组策略对象（GPO）。**BackupID** 参数可用于从最近一次备份之前的任何备份文件中恢复 GPO。

## 参数

### -All

这表示该cmdlet会恢复域中所有在备份目录中拥有备份的GPO（组策略对象）。每个GPO都会从其在该目录中的最新备份中恢复过来。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: RestoreAll
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -BackupId

用于指定 GPO 备份的备份 ID。该备份 ID 是一个全局唯一的标识符（GUID），可以唯一地识别该备份文件。您可以使用此参数在备份目录中指定某个特定版本的 GPO 备份文件。

备份ID与被备份的GPO的ID不同（该ID由**Guid**参数指定），你可以在备份目录中找到备份ID。

```yaml
Type: Guid
Parameter Sets: RestoreFromBackupId
Aliases: Id

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

### -Domain

指定此 cmdlet 的域名。必须提供该域名的完全限定域名（FQDN）。

对于 `Restore-GPO` cmdlet 来说，这里指的是您希望恢复组策略对象（GPO）的域。该域必须是与备份 GPO 相同的域。

如果您不指定 **Domain** 参数，将使用运行当前会话的用户的域信息。如果该 cmdlet 是通过计算机启动或关闭脚本来执行的，则会使用计算机的域信息。有关更多详细信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域名与当前会话所使用的用户的域名不同（或者对于启动或关闭脚本来说，是与计算机相关的域名不同），那么该域名与用户或计算机的域名之间必须存在信任关系。

您也可以使用其内置别名 **DomainName** 来引用 **Domain** 参数。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

通过其全局唯一标识符（GUID）指定要恢复的组策略对象（GPO）。该GUID能够唯一地识别该GPO。

GPO是从备份目录中最近的备份版本恢复过来的。如果要指定非最近版本的备份，请使用**BackupID**参数。

您也可以使用其内置别名 **Id** 来引用 **Guid** 参数。

```yaml
Type: Guid
Parameter Sets: RestoreFromGpo(GUID)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name

根据显示名称指定要恢复的组策略对象（GPO）。该GPO将从备份目录中最近的备份文件中恢复。如果需要恢复的不是最近的备份文件，请使用BackupId参数。

显示名称在域内并不保证是唯一的。如果该域中存在另一个具有相同显示名称的组策略对象（GPO），则会发生错误。您可以使用 **Guid** 参数来唯一标识一个 GPO。

您也可以通过其内置别名 **DisplayName** 来引用 Name 参数。

```yaml
Type: System.String
Parameter Sets: RestoreFromGpo(Name)
Aliases: DisplayName

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path

指定备份目录的路径。

您也可以通过其内置别名**BackupLocation**来引用**Path**参数。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: BackupLocation, BackupDirectory

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Server

指定此cmdlet用于联系的域控制器的名称，以便完成操作。您可以指定完全合格的域名（FQDN）或主机名。

如果您没有使用 **Server** 参数来指定名称，系统将会联系主域控制器（PDC）仿真器。

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

### -WhatIf

展示了如果运行该 cmdlet 会发生什么情况。但实际上该 cmdlet 并没有被运行。

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

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft(GroupPolicy.BackupGpo)

你可以将 GPO 备份文件（即包含 GPO 设置的单独文件，该文件可以导入到其他位置以重新创建相应的 GPO）传递给这个 cmdlet。

## 输出

### Microsoft(GroupPolicy.Gpo)

此cmdlet返回已恢复的GPO（组策略对象）。

## 备注

* You can use the **Domain** parameter to explicitly specify the domain for this cmdlet.

如果您没有明确指定域名，该cmdlet会使用默认域名。默认域名是指当前会话运行的安全上下文用于访问网络资源的那个域名。这个域名通常就是运行该会话的用户的所在域；例如，通过“程序文件”菜单启动Windows PowerShell的用户所在的域，或者在`runas`命令中指定的用户所在的域。不过，计算机启动和关闭脚本是在`LocalSystem`账户的上下文中运行的。`LocalSystem`是一个内置的本地账户，它以计算机的身份访问网络资源。因此，当从这个启动或关闭脚本中运行该cmdlet时，默认域名就是计算机所属的域名。

## 相关链接

[备份GPO](./Backup-GPO.md)

[复制GPO](./Copy-GPO.md)

[Get-GPO](./Get-GPO.md)

[Import-GPO](./Import-GPO.md)

[New-GPO](./New-GPO.md)

[Remove-GPO](./Remove-GPO.md)

[重命名GPO](./Rename-GPO.md)

