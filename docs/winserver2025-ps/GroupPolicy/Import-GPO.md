---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.GroupPolicy.Commands.dll-Help.xml
Module Name: GroupPolicy
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/grouppolicy/import-gpo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-GPO
---

# 导入组策略对象（GPO）

## 摘要

将备份中的组策略设置（GPO）导入到指定的目标组策略对象中。

## 语法

### ImportGUID（默认值）

```
Import-GPO -BackupId <Guid> -Path <String> [-TargetGuid <Guid>] [-TargetName <String>]
 [-MigrationTable <String>] [-CreateIfNeeded] [-Domain <String>] [-Server <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### ImportName

```
Import-GPO -BackupGpoName <String> -Path <String> [-TargetGuid <Guid>] [-TargetName <String>]
 [-MigrationTable <String>] [-CreateIfNeeded] [-Domain <String>] [-Server <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Import-GPO` cmdlet 将来自组策略对象（GPO）备份的设置导入到指定的目标 GPO 中。目标 GPO 可以位于与备份所在的域或林不同的域或林中，并且在该操作之前不必已经存在。

使用 **Path** 参数来指定备份文件的位置，然后使用 **BackupGpoName** 参数来指定要使用的备份的 GPO 名称，或者使用 **BackupId** 参数来指定要使用的备份的 ID（GUID）。

如果您指定了一个 GPO 名称，该cmdlet会导入最新的备份文件。如果要导入某个较早版本的 GPO 备份文件，则必须使用 **BackupID** 参数来指定该版本的唯一备份标识符。这个标识符是一个 GUID（全局唯一标识符），用于在该备份目录中唯一地识别该备份文件。

使用 **TargetName** 参数或 **TargetGuid** 参数来指定目标 GPO（组策略对象），设置应导入到该目标 GPO 中。可以使用可选的 **MigrationTable** 参数来跨域映射安全主体和通用命名 convention (UNC) 路径。如果指定的目标 GPO 不存在，可以使用 **CreateIfNeeded** 参数创建一个新的 GPO。

## 示例

### 示例 1：将设置从最新的备份文件导入到同一域中的另一个目录

```powershell
Import-GPO -BackupGpoName 'TestGPO' -TargetName 'TestGPO' -path 'C:\backups'
```

```Output
DisplayName      : TestGPO
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : 87d38d82-cc2d-4bf7-ad9f-4083a60316eb
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 3/3/2009 1:03:28 PM
ModificationTime : 3/6/2009 5:03:29 PM
UserVersion      : AD Version: 9, SysVol Version: 9
ComputerVersion  : AD Version: 5, SysVol Version: 5
WmiFilter        :
```

该命令会将 `c:\backups` 目录中名为 `TestGPO` 的最新备份文件中的设置导入到当前域中同名의 GPO（组策略对象）中。如果当前域中不存在名为 `TestGPO` 的 GPO，那么该命令会失败，因为没有指定 `CreateIfNeeded` 参数。

### 示例 2：从同一域中的同一目录下的指定备份文件中导入设置

```powershell
$params = @{
    BackupId       = 'A491D730-F3ED-464C-B8C9-F50562C536AA'
    TargetName     = 'TestGPO'
    path           = 'C:\Backups'
    CreateIfNeeded = $true
}
Import-GPO @params
```

```Output
DisplayName      : TestGPO
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : 87d38d82-cc2d-4bf7-ad9f-4083a60316eb
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 3/3/2009 1:03:28 PM
ModificationTime : 3/6/2009 5:11:49 PM
UserVersion      : AD Version: 10, SysVol Version: 10
ComputerVersion  : AD Version: 6, SysVol Version: 6
WmiFilter        :
```

此命令将 `C:\Backups` 目录中指定的备份文件中的设置导入到当前域内名为 `TestGPO` 的组策略对象（GPO）中。**BackupId** 参数用于指定要使用的 GPO 备份的 GUID。由于指定了 **CreateIfNeeded** 参数，如果在当前域中不存在名为 `TestGPO` 的 GPO，则在导入设置之前会创建一个新的 GPO。

### 示例 3：将最新备份中的设置导入到当前域名的另一个目录中

```powershell
$params = @{
    BackupGpoName  = 'TestGPO'
    Path           = 'D:\Backups'
    TargetName     = 'NewTestGPO'
    MigrationTable = 'D:\Tables\Migtable1.migtable'
    CreateIfNeeded = $true
}
Import-GPO @params
```

```Output
DisplayName      : NewTestGPO
DomainName       : contoso.com
Owner            : CONTOSO\Domain Admins
Id               : 87d38d82-cc2d-4bf7-ad9f-4083a60316eb
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 3/3/2009 1:03:28 PM
ModificationTime : 3/6/2009 5:11:49 PM
UserVersion      : AD Version: 1, SysVol Version: 1
ComputerVersion  : AD Version: 1, SysVol Version: 1
WmiFilter        :
```

此命令从 `D:\Backups` 目录中名为 `TestGPO` 的最新备份文件中导入设置，并将这些设置应用到当前域中的名为 `NewTestGPO` 的 GPO 中。指定的迁移表用于将安全主体（security principals）和 UNC 路径迁移到新的 GPO 中。由于指定了 **CreateIfNeeded** 参数，因此如果新 GPO 不存在，系统会创建它。

## 参数

### -BackupGpoName

指定此cmdlet从中导入设置的备份GPO的显示名称。系统会使用该GPO的最新备份版本。如果备份目录中存在同一GPO的多个备份版本，您可以使用**BackupID**参数来指定要使用的特定版本。

您也可以使用 **BackupGpoName** 参数的内置别名 **DisplayName** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: System.String
Parameter Sets: ImportName
Aliases: DisplayName

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -BackupId

用于指定 GPO 备份的备份 ID。备份 ID 是一个全局唯一的标识符（GUID），可以唯一地识别该备份文件。您可以使用此参数来在备份目录中指定某个特定版本的 GPO 备份文件。

备份ID与被备份的GPO（组策略对象）的ID不同。

您也可以使用 **BackupID** 参数的内置别名 **Id** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

```yaml
Type: Guid
Parameter Sets: ImportGUID
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

### -CreateIfNeeded

表示如果指定的目标GPO不存在，该cmdlet会从备份中创建一个新的GPO。

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

### -Domain

指定此 cmdlet 所使用的域名。必须提供该域名的完全限定域名（FQDN）。

对于 `Import-GPO` cmdlet 来说，这里指的是你想要导入 GPO 的域。

如果您没有指定 `Domain` 参数，那么将使用当前会话所运行用户的域信息。如果该 cmdlet 是从计算机启动或关闭脚本中运行的，则会使用计算机的域信息。有关更多详细信息，请参阅完整帮助文档中的“备注”部分。

如果您指定的域与当前会话所使用的用户的域不同（或者对于启动/关闭脚本来说，是与计算机所在的域不同），那么该域与用户所在域或计算机所在域之间必须存在信任关系。

你也可以使用该参数的内置别名 **DomainName** 来引用它。有关更多信息，请参阅 [关于别名](/powershell/module/microsoft.powershell.core/about/aboutaliases)。

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

### -MigrationTable

指定迁移表文件的路径。您可以使用迁移表来在多个域之间映射安全主体（security principals）和统一命名目录（UNC）路径。

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

### -Path

指定备份目录的路径。

您也可以使用 **Path** 参数的内置别名来引用它：**BackupLocation** 或 **BackupDirectory**。

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

指定此cmdlet用于联系的域控制器的名称，以便完成操作。您可以指定完全限定的域名（FQDN）或主机名。

如果您不使用**Server**参数来指定名称，系统会联系主域控制器（PDC）仿真器。

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

### -TargetGuid

指定此 cmdlet 将设置导入到的 GPO 的 GUID。如果该 GPO 在域中尚不存在，可以使用 *CreateIfNeeded* 参数强制创建它。

你必须指定 **TargetGuid** 参数或 **TargetName** 参数中的一个。

```yaml
Type: Guid
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetName

指定要导入设置的组策略对象（GPO）的显示名称。如果该GPO在域中还不存在，可以使用**CreateIfNeeded**参数来强制创建它。

你必须指定 **TargetGuid** 参数或 **TargetName** 参数中的一个。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.GroupPolicy.GpoBackup

你可以将一个表示GPO备份的对象（该对象存在于文件系统中）作为参数传递给这个cmdlet。

## 输出

### Microsoft.GroupPolicy.Gpo

此cmdlet在设置被导入后返回一个表示GPO（组策略对象）的对象。

## 备注

* You can use the `Import-GPO` to copy settings from a GPO backup in one domain to the same domain
  or another domain in the same or different forest.

你可以使用 **Domain** 参数来明确指定此 cmdlet 的域名。

如果您没有明确指定域名，该cmdlet会使用默认域。默认域是指当前会话所运行的安全上下文用于访问网络资源的那个域。这个域通常就是运行该会话的用户的域；例如，通过打开Windows PowerShell启动会话的用户所在的域，或者在“runas”命令中指定的用户所属的域。然而，计算机启动和关闭脚本是在LocalSystem账户的上下文中运行的。LocalSystem账户是一个内置的本地账户，它以计算机账户的身份访问网络资源。因此，当从这个启动或关闭脚本中运行该cmdlet时，默认域就是计算机所连接的那个域。

## 相关链接

[备份GPO](./Backup-GPO.md)

[Restore-GPO](./Restore-GPO.md)

