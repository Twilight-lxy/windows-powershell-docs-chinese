---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/restore-dfsrpreservedfiles?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Restore-DfsrPreservedFiles
---

# 恢复 DFSR 保留的文件

## 摘要
恢复之前由DFS复制功能保存的文件和文件夹。

## 语法

### RestorePath（默认值）
```
Restore-DfsrPreservedFiles [-Path] <String> [-RestoreToPath] <String> [-RestoreAllVersions] [-CopyFiles]
 [-AllowClobber] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### RestoreOrigin
```
Restore-DfsrPreservedFiles [-Path] <String> [-RestoreToOrigin] [-RestoreAllVersions] [-CopyFiles]
 [-AllowClobber] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Restore-DfsrPreservedFiles` cmdlet 用于恢复被保留的文件和文件夹。分布式文件系统（DFS）复制服务会保留以下类型的文件和文件夹：

- Conflicted.
If users make changes to the same file on multiple servers before replication converges, a file might conflict with the current version.
DFS Replication preserves previous conflicting versions of the file.
- Deleted.
When a member computer deletes a replicated file, other members also remove that file.
Depending on membership settings, computers can preserve deleted files.
To modify whether a member computer preserves deleted files, use the **Set-DfsrMembership** cmdlet.
- Preexisting.
If DFS Replication overwrites files during its initial synchronization, DFS Replication preserves those files.

对于这三种类型，DFS复制（DFS Replication）都会将文件移动到 `<replicated folder>\DfsrPrivate\ConflictAndDeleted` 或 `<replicated folder>\DfsrPrivate\Preexisting` 目录中。DFS复制会根据实际情况将这些文件记录在相应的清单文件中（`ConflictAndDeletedManifest.xml` 或 `PreExistingManifest.xml`）。要恢复发生冲突或被删除的文件及文件夹，请指定 `ConflictAndDeletedManifest.xml` 清单文件；要恢复原有的文件及文件夹，则请指定 `PreExistingManifest.xml` 清单文件。您可以使用 `Get-DfsrPreservedFiles` cmdlet 来查看那些被保留下来的文件及文件夹。

**注意：** 默认情况下，此cmdlet会移动所有文件并删除任何已存在的保留文件（包括文件的旧版本）。在使用此cmdlet之前，请考虑备份`ConflictsAndDeleted`和`Preexisting`文件夹。

## 示例

### 示例 1：将已存在的文件恢复到它们的原始位置
```
PS C:\> Restore-DfsrPreservedFiles -Path "C:\RF01\DfsrPrivate\PreExistingManifest.xml" -RestoreToOrigin
```

该命令会将复制文件夹C:\RF01中已存在的文件和文件夹恢复到它们的原始位置。该命令没有指定*CopyFiles*参数，因此它只是移动文件，而不会修改原有的文件夹（即原来的文件夹仍然保持为空状态）。

### 示例 2：将现有文件的副本恢复到不同的位置
```
PS C:\> Restore-DfsrPreservedFiles -Path "C:\RF01\DfsrPrivate\PreExistingManifest.xml" -RestoreToPath "C:\DFSRTest" -CopyFiles -AllowClobber -Verbose
VERBOSE: Loading Preserved file Manifest C:\rf01\DfsrPrivate\PreExistingManifest.xml
VERBOSE: Restoring Preserved Files from manifest C:\rf01\DfsrPrivate\PreExistingManifest.xml
```

此命令将复制文件夹 C:\RF01 中的原有文件和文件夹的副本恢复到位置 C:\DFSRTest。该命令通过使用 *RestoreToPath* 参数来指定目标位置，并使用了 *AllowClobber* 参数，因此它会覆盖目标位置中已存在的同名文件。此外，该命令还使用了 *Verbose* 参数以便在控制台中显示相关信息。

### 示例 3：将发生冲突的文件以及被删除的文件恢复到另一个位置
```
PS C:\> Restore-DfsrPreservedFiles -Path "C:\RF01\DfsrPrivate\ConflictAndDeletedManifest.xml" -RestoreToPath "C:\DFSRRestore" -RestoreAllVersions -Force
PS C:\> Get-ChildItem -Path "C:\DFSRRestore"
    Directory: C:\dfsrrestore

Mode                LastWriteTime     Length Name
----                -------------     ------ ----
-a---          4/5/2013   9:58 AM     848294 canary.bmp
-a---          4/5/2013   9:58 AM     848294 canary2013_04_05_17_00_00Z.bmp
-a---          4/5/2013   9:58 AM     848294 canary2013_04_05_17_17_37Z.bmp
-a---          4/5/2013   9:58 AM     848294 canary2013_04_05_17_17_47Z.bmp
```

这个示例将多个版本的有冲突或已被删除的文件恢复到指定的位置。

第一个命令用于将复制文件夹 C:\FR01 中的冲突文件和被删除的文件及文件夹恢复到 C:\DFSRRestore 目录中。该命令会恢复所有保存过的文件版本。由于使用了 *Force* 参数，因此系统不会提示用户确认操作，而是会直接覆盖目标目录中的现有文件。

第二个命令使用了 **Get-ChildItem** cmdlet 来显示关于已恢复文件的信息。如需更多信息，请输入 `Get-Help Get-ChildItem`。在这个例子中，第一个命令恢复了同一个文件的多个版本。

## 参数

### -AllowClobber
表示该cmdlet会覆盖目标位置中已存在的同名文件。如果您未指定此参数，cmdlet在覆盖现有文件之前会先提示您。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您确认是否继续。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -CopyFiles
表示该 cmdlet 是复制文件而不是移动文件。

如果您不指定此参数，该 cmdlet 会移动被保留的文件，但仅恢复文件的最新版本。这样会导致冲突文件或已删除文件的先前版本丢失。现有的文件从不会有多个版本。为了避免丢失先前版本，请考虑备份 “ConflictsAndDeleted” 文件夹。或者，您可以指定 *RestoreAllVersions* 参数来恢复所有版本的文件。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而不需要用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定清单文件的路径。默认情况下，清单文件位于 `<复制文件夹>\DfsrPrivate` 文件夹中。若要恢复存在冲突或已被删除的文件，请指定 `ConflictAndDeletedManifest.xml`；若要恢复已存在的文件（即这些文件在之前的版本中也存在），请指定 `PreExistingManifest.xml`。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -RestoreAllVersions
表示该cmdlet会恢复文件的所有版本。同时，该cmdlet会在文件名中添加时间戳。此参数仅影响存在冲突的文件或已被删除的文件；原有的文件永远不会有多个版本。

如果您不指定此参数，该cmdlet将仅恢复文件的最新版本。如果您既不指定此参数也不指定*CopyFiles*参数，该cmdlet会恢复最新版本并从ConflictsAndDeleted文件夹中删除所有其他版本。在使用此cmdlet之前，请考虑先备份ConflictsAndDeleted文件夹。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RestoreToOrigin
该cmdlet用于将所有记录在ConflictAndDeletedManifest.xml或PreExistingManifest.xml清单文件中的文件和文件夹恢复到它们的原始位置。如果需要恢复到其他位置，请使用*RestoreToPath*参数指定路径。

```yaml
Type: SwitchParameter
Parameter Sets: RestoreOrigin
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RestoreToPath
用于指定记录在 `ConflictAndDeletedManifest.xml` 或 `PreExistingManifest.xml` 文档中的文件和文件夹的位置。如果希望将文件恢复到原始位置，请使用 `*RestoreToOrigin*` 参数。

```yaml
Type: String
Parameter Sets: RestorePath
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被执行。

```yaml
Type: SwitchParameter
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

### 字符串

## 输出

### 无

## 备注

## 相关链接

[Get-DfsrPreservedFiles](./Get-DfsrPreservedFiles.md)

[Set-DfsrMembership](./Set-Dfsr Membership.md)

