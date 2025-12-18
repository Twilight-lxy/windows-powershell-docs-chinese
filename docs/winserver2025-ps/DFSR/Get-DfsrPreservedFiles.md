---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/get-dfsrpreservedfiles?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsrPreservedFiles
---

# Get-DfsrPreservedFiles

## 摘要
获取DFS复制之前已保存的文件和文件夹列表。

## 语法

```
Get-DfsrPreservedFiles [-Path] <String> [<CommonParameters>]
```

## 描述
`Get-DfsrPreservedFiles` cmdlet 可用于获取被保留的文件和文件夹列表。分布式文件系统（DFS）复制服务会保留以下类型的文件和文件夹：

- Conflicted.
If users make changes to the same file on multiple servers before replication converges, a file might conflict with the current version.
DFS Replication preserves previous conflicting versions of the file.
- Deleted.
When a member computer deletes a replicated file, other members also remove that file.
Depending on membership settings, computers can preserve deleted files.
To modify whether a member computer preserves deleted files, use the **Set-DfsrMembership** cmdlet.
- Preexisting.
If DFS Replication overwrites files during its initial synchronization, DFS Replication preserves those files.

对于这三种类型，DFS复制都会将文件和文件夹移动到 `<replicated folder>\DfsrPrivate\ConflictsAndDeleted` 或 `<replicated folder>\DfsrPrivate\Preexisting` 中。DFS复制会将这些文件记录在相应的清单文件中（分别为 `ConflictAndDeletedManifest.xml` 或 `PreexistingManifest.xml`）。要查看发生冲突或被删除的文件和文件夹，请指定 `ConflictAndDeletedManifest.xml`；要查看原本就存在的文件和文件夹，请指定 `PreexistingManifest.xml`。您可以使用 `Restore-DfsrPreservedFiles` cmdlet 来恢复这些文件和文件夹。

## 示例

### 示例 1：获取某个复制文件夹中发生冲突并被删除的文件和文件夹
```
PS C:\> Get-DfsrPreservedFiles -Path "C:\RF01\DfsrPrivate\ConflictAndDeletedManifest.xml"
Path            : \\.\C:\ RF01\Sales 2013.pptx
Uid             : {9F159608-2199-4D8B-B9F5-51D83A778089}-v22
Gvsn            : {9F159608-2199-4D8B-B9F5-51D83A778089}-v27
MemberGuid      : e4b69303-5f51-4aec-80b1-89f21323e2b7
Attributes      : System, Directory
PreservedName   : Sales 2013-{9F159608-2199-4D8B-B9F5-51D83A778089}-v27.pptx
PreservedTime   : 4/5/2013 4:03:57 PM
PreservedReason : ConflictAndDelete
FileCount       : 1
FileSize        : 7435676

Path            : \\.\C:\RF01\Sales 2012.pptx
Uid             : {9F159608-2199-4D8B-B9F5-51D83A778089}-v24
Gvsn            : {9F159608-2199-4D8B-B9F5-51D83A778089}-v26
MemberGuid      : e4b69303-5f51-4aec-80b1-89f21323e2b7
Attributes      : System, Directory
PreservedName   : Sales 2012-{9F159608-2199-4D8B-B9F5-51D83A778089}-v26.pptx
PreservedTime   : 4/5/2013 4:03:57 PM
PreservedReason : ConflictAndDelete
FileCount       : 1
FileSize        : 7727683
```

该命令会获取复制文件夹 C:\RF01 中存在冲突或已被删除的文件和文件夹的列表。命令指定了该复制文件夹的相关信息（即清单文件）。控制台会显示文件的名称以及其他相关数据。

### 示例 2：获取复制文件夹中已存在的文件
```
PS C:\> Get-DfsrPreservedFiles -Path "C:\RF01\DfsrPrivate\PreExistingManifest.xml"
Path            : \\.\C:\RF01\Marketing
Uid             : {9F159608-2199-4D8B-B9F5-51D83A778089}-v30
Gvsn            : {9F159608-2199-4D8B-B9F5-51D83A778089}-v30
MemberGuid      : 00000000-0000-0000-0000-000000000000
Attributes      : 10
PreservedName   : Marketing-{9F159608-2199-4D8B-B9F5-51D83A778089}-v30
PreservedTime   : 4/5/2013 4:21:16 PM
PreservedReason : Preexisting
FileCount       : 4
FileSize        : 2548978

Path            : \\.\C:\RF01\Sales
Uid             : {9F159608-2199-4D8B-B9F5-51D83A778089}-v32
Gvsn            : {9F159608-2199-4D8B-B9F5-51D83A778089}-v32
MemberGuid      : 00000000-0000-0000-0000-000000000000
Attributes      : 10
PreservedName   : Sales-{9F159608-2199-4D8B-B9F5-51D83A778089}-v32
PreservedTime   : 4/5/2013 4:21:16 PM
PreservedReason : Preexisting
FileCount       : 4
FileSize        : 4096
```

这个命令会获取复制文件夹 C:\RF01 中已存在的文件和文件夹的列表。控制台会显示文件名称以及其他相关信息。

### 示例 3：通过文件名查找存在冲突或已被删除的文件
```
PS C:\> Get-DfsrPreservedFiles -Path "C:\RF01\DfsrPrivate\ConflictAndDeletedManifest.xml" | Where-Object Path -like "*canary*"
Path            : \\.\C:\RF01\canary.bmp
Uid             : {031C15B7-397D-4F99-A340-B1C7931EEE01}-v3451
Gvsn            : {9F159608-2199-4D8B-B9F5-51D83A778089}-v54
MemberGuid      : 11d2449a-d25f-4272-bac8-fe10f2299cdd
Attributes      : System, Directory
PreservedName   : canary-{9F159608-2199-4D8B-B9F5-51D83A778089}-v54.bmp
PreservedTime   : 4/5/2013 5:00:00 PM
PreservedReason : ConflictAndDelete
FileCount       : 1
FileSize        : 848294
```

这个命令用于查找那些名称中包含字符串“canary”的、存在冲突或已被删除的文件。该命令会将被保留下来的文件记录在指定的清单（manifest）中，然后通过管道运算符将这些文件传递给**Where-Object** cmdlet。该cmdlet会将与指定条件匹配的文件显示回控制台。如需更多信息，请输入`Get-Help Where-Object`。

在这个例子中，该命令会找到一个名为 `canary.bmp` 的文件。你可以使用 `Restore-DfsrPreservedFiles` 命令来恢复这个文件。

## 参数

### -Path
指定清单文件的路径。默认情况下，清单文件位于 `<Replicated Folder>\DfsrPrivate` 文件夹中。如果想查看存在冲突或已被删除的文件，请指定 `ConflictAndDeletedManifest.xml`；如果想查看预先存在的文件，请指定 `PreexistingManifest.xml`。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 字符串

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrPreservedEntry

## 备注

## 相关链接

[Restore-DfsrPreservedFiles](./Restore-DfsrPreservedFiles.md)

