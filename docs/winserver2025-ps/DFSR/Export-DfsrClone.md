---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/export-dfsrclone?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-DfsrClone
---

# Export-DfsrClone

## 摘要
导出克隆的DFS复制数据库及卷配置设置。

## 语法

```
Export-DfsrClone [-Volume] <String> [[-Path] <String>] [[-Validation] <ValidationLevel>] [-AllowClobber]
 [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Export-DfrsClone` cmdlet 用于从本地计算机导出指定卷的分布式文件系统（DFS）复制数据库及卷配置相关的 XML 文件设置，以便将这些数据克隆到另一台计算机上。所有包含已复制文件夹内容的卷上都存在 DFS 复制数据库，且每个数据库中都保存着该卷上所有已复制文件夹的引用信息。运行此 cmdlet 会触发 DFS 复制服务中的导出操作，并等待服务完成这一过程。您可以使用 `Get-DfsrCloneState` 命令来监控导出操作的进度。

DFSR在Windows Server 2012 R2中不支持克隆SYSVOL文件夹或只读副本。这些被复制的文件夹会在导出过程中被自动忽略。对于一台计算机来说，一次只能导出一个或导入一个数据库。

请按照推荐和支持的步骤来执行DFS复制数据库的克隆操作，具体方法请参考TechNet库中的[导出DFS复制数据库的副本](https://go.microsoft.com/fwlink/?LinkId=302005)文档。其中，“上游”指的是作为复制文件数据及DFS复制数据库权威来源的服务器；“下游”则指的是非权威性的服务器，它是该权威服务器的副本。

## 示例

### 示例 1：将数据库导出到一个文件夹中
```
PS C:\> Export-DfsrClone -Volume "C:" -Path "C:\DfsRClone" | Format-List
This operation will export the database and create a clone. It can take a long time to complete and any replication
will stop on the volume. Use Get-DfsrCloneState or DFSR event 2402 to determine when the export has succeeded. Volume:
C:\ Path: "C:\Dfsrclone"
Are you sure you want to continue to export the database clone?
[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):y

CloneFolderPath : C:\Dfsrclone
CopyHint : Robocopy.exe "c:\dfsrclone" "<DestinationPath>" /B

RootFolderPath : c:\Rf01
PreseedingHint : Robocopy.exe "c:\Rf01" "<DestinationPath>" /E /B /COPYALL /R:6 /W:5 /MT:64 /XD DfsrPrivate /TEE /LOG+:preseed.log

RootFolderPath : c:\RF02
PreseedingHint Robocopy.exe "c:\RF02" "<DestinationPath>" /E /B /COPYALL /R:6 /W:5 /MT:64 /XD DfsrPrivate /TEE /LOG+:preseed.log
```

该命令将C:卷的DFS复制数据库克隆版本导出到C:\DfsRClone目标文件夹中，并显示相关的已复制文件夹。推荐的Robocopy语法会出现在输出结果中。

### 示例 2：导出数据库并监控进度
```
PS C:\> Export-DfsrClone -Volume "C:" -Path "C:\DfsRClone" -Force
PS C:\> Get-DfsrCloneState
PS C:\> Get-DfsrCloneState
```

这个示例演示了如何导出DFS复制数据库的克隆副本，然后使用`Get-DfsrCloneState`命令定期检查复制状态，直到复制完成。

第一个命令使用了 **Export-DfsrClone** cmdlet 来启动导出过程。您需要打开另一个 Windows PowerShell 控制台，或者按下 CTRL+C 来终止 **Export-DfsrClone** cmdlet 的执行。即使该 cmdlet 停止运行，克隆过程仍会在服务器上继续进行。

第二个命令使用了 **Get-DfsrCloneState** cmdlet 来检查导出进程的状态。命令执行后即可看到相应的输出结果。

第三个命令使用了 **Get-DfsrCloneState** cmdlet 来检查导出进程的状态。输出结果表明导出操作已经成功完成。

### 示例 3：导出和导入数据库
```
PS C:\> New-DfsReplicationGroup "RG05" | New-DfsReplicatedFolder -FolderName "RF 5" | Add-DfsrMember -ComputerName "SRV01"
PS C:\> Set-DfsrMembership -ComputerName "SRV01" -ContentPath C:\Rf05 -PrimaryMember $True -FolderName "RF05"
PS C:\> Update-DfsrConfigurationFromAD
PS C:\> New-Item -Path "C:\DfsRClone" -Type Directory
PS C:\> Export-DfsrClone -Volume C: -Path "C:\DfsRClone"
PS C:\> Robocopy.exe C:\Rf05 \\srv02\c$\Rf05 /E /B /COPYALL /R:6 /W:5 /MT:64 /XD DfsrPrivate /TEE /LOG+:preseed.log
PS C:\> Robocopy.exe C:\DfsRClone \\srv02\c$\DfsRClone /B
PS C:\> RD "C:\system volume information\dfsr" -Force -Recurse
PS C:\> Import-DfsrClone -Volume C: -Path "C:\DfsRClone"
PS C:\> Get-DfsrCloneState
PS C:\> Add-DfsrMember -GroupName "RG05" -ComputerName "SRV02" | Set-DfsrMembership -FolderName "RF05" -ContentPath "C:\Rf05"
PS C:\> Add-DfsrConnection -GroupName "RG05" -SourceComputerName "SRV01" -DestinationComputerName "SRV02"
PS C:\> Update-DfsrConfigurationFromAD
```

这个示例演示了从源服务器SRV01克隆其RF05复制文件夹到目标服务器SRV02的整个过程。前七个命令在上游服务器上执行，其余命令则在下游服务器上执行。

第一个命令是在上游服务器上执行的，它使用 **New-DfsReplicationGroup** cmdlet 创建一个名为 RG05 的复制组。该命令的输出结果被传递给 **New-DfsReplicatedFolder** cmdlet 以创建一个名为 RF05 的文件夹；随后，这个输出结果又被传递给 **Add-DfsrMember** cmdlet，用于将 SRV01 这台计算机添加为该复制组的成员。

第二个命令是在上游服务器上执行的，它使用 **Set-DfsrMembership** cmdlet 来修改名为 SRV01 的计算机的成员身份。

第三个命令是在上游服务器上执行的，它使用 **Update-DfsrConfigurationFromAD** cmdlet 来更新源服务器上的 DFS 复制配置。

第四条命令是在上游服务器上执行的，它使用 **New-Item** cmdlet 在路径 C:\DfsRClone 中创建一个新的目录。

第五条命令是在上游服务器上执行的，它使用 **Export-DfsrClone** cmdlet 来导出一个卷。

第六条命令是在上游服务器上执行的，它使用 Robocopy 将复制过来的文件夹目录结构拷贝到目标服务器上。

第七条命令是在上游服务器上执行的，它使用 Robocopy 工具将 C:\DfsRClone 目录复制到目标服务器。

第八条命令在下游服务器上执行，使用RD（可能是某个特定的工具或程序）来删除复制目录（如果该目录存在的话）。

第九条指令是在下游服务器上执行的，它使用 **Import-DfsrClone** cmdlet 将数据库和卷配置导入到目标服务器中。

在下游服务器上执行的第十条命令使用了 **Get-DfsrCloneState** cmdlet 来验证导入过程的完成情况。

第十一条命令是在下游服务器上执行的，它使用 `Add-DfsrMember` cmdlet 在目标服务器上创建一个新的组。该命令会将 `Add-DfsrMember` cmdlet 的输出结果传递给 `Set-DfsrMembership` cmdlet，以便为这个复制的文件夹组添加成员资格（即将该组中的文件夹添加到相应的分布式文件系统（DFS）资源中）。

第十二条命令是在下游服务器上执行的，它使用 **Add-DfsrConnection** cmdlet 来为目标服务器添加一个连接。

最后一个命令是在下游服务器上执行的，它使用 **Update-DfsrConfigurationFromAD** cmdlet 来更新目标服务器上的 DFS 复制配置。

## 参数

### -AllowClobber
这表示该 cmdlet 会覆盖现有的导出的数据库和 XML 配置文件。默认情况下，如果指定路径中已存在该文件，则操作将停止执行。在导出 DFS 复制数据库之后、但在执行导入/克隆操作之前，必须将复制文件夹的内容填充到下游服务器中。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: Overwrite

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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

### -Force
强制命令运行，而无需询问用户确认。在脚本化的克隆操作中使用此参数。

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
指定一个文件夹路径，用于保存导出的DFS复制文件（dfsr.db.clone和config.xml）。该文件夹路径必须存在，并且必须是本地卷，而不能是映射的驱动器或UNC路径。如果您不指定此参数，cmdlet将使用当前的工作目录。在导出DFS复制文件后、但在执行导入操作之前，您需要将复制到的文件夹内容填充到下游服务器中。

```yaml
Type: String
Parameter Sets: (All)
Aliases: DestinationFolderPath

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Validation
用于指定DFS复制服务在导入过程中对复制的文件和文件夹进行检查时的详细程度（即报告信息的量）。该参数的可接受值包括：

- None (0) No validation is performed on the files, all files and folders are assumed to exist, and the administrator must have populated the files and folders without errors, or allowing any changes to the file structures on upstream and downstream servers. This is the fastest but most optimistic mode.
- Basic (1) Simple comparisons are performed for every file and folder using the size, modified time-date stamp, and hash of the ACL. Any added, missing or differing files or folders are replicated inbound and any inconsistent local copies on the downstream are moved to the \<replicated-folder\>\Dfsrprivate\ConflictAndDeleted folder or to the \<replicated-folder\>\DfsrPrivate\PreExisting folder. This mode is a good balance of performance and optimism.
- Full (2) DFS Replication hash computation is performed for every file and folder. Any missing or differing files or folders are replicated inbound and any inconsistent local copies on the downstream are moved to the \<replicated-folder\>\Dfsrprivate\ConflictAndDeleted folder or to the \<replicated-folder\>\DfsrPrivate\PreExisting folder. This is the slowest but most accurate mode.

```yaml
Type: ValidationLevel
Parameter Sets: (All)
Aliases:
Accepted values: None, Basic, Full

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Volume
请指定一个驱动器字母或挂载点路径，该路径指向要导出的数据库文件所在的文件夹（这些文件夹属于某个卷的复制内容）。这样就可以进行克隆操作了。如果该卷上托管了多个复制文件夹，那么它们都会使用同一个 DFS 复制数据库，并且都会被克隆。在导出 DFS 复制数据库之后、但在执行导入克隆操作之前，必须将复制文件夹中的内容填充到下游服务器中。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 字符串

## 输出

### DfsrFolderToSync

## 备注

## 相关链接

[Get-DfsrCloneState](./Get-DfsrCloneState.md)

[Import-DfsrClone](./Import-DfsrClone.md)

[Reset-DfsrCloneState](./Reset-DfsrCloneState.md)

