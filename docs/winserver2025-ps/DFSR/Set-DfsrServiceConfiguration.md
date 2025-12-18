---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/set-dfsrserviceconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DfsrServiceConfiguration
---

# Set-DfsrServiceConfiguration

## 摘要
修改DFS复制服务的设置。

## 语法

```
Set-DfsrServiceConfiguration [[-ComputerName] <String[]>] [[-RPCPort] <UInt32>] [[-DisableDebugLog] <Boolean>]
 [[-MaximumDebugLogFiles] <UInt32>] [[-DebugLogPath] <String>] [[-DebugLogSeverity] <UInt32>]
 [[-MaximumDebugLogMessages] <UInt32>] [[-UnexpectedAutoRecovery] <Boolean>]
 [[-CleanupStagingFolderAtPercent] <UInt32>] [[-CleanupStagingFolderUntilPercent] <UInt32>]
 [[-CleanupConflictFolderAtPercent] <UInt32>] [[-CleanupConflictFolderUntilPercent] <UInt32>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DfsrServiceConfiguration` cmdlet 用于修改分布式文件系统（DFS）复制服务在复制组成员上的设置。复制组的成员会托管被复制的文件夹。可以使用此 cmdlet 来配置清理设置、调试日志记录设置，以及实现意外关机时的自动恢复功能。

DFS复制（DFS Replication）会将文件存储在一个名为“ConflictsAndDeleted”的文件夹中，直到因空间不足而删除这些文件。此外，DFS复制还可以将这些文件临时存放在另一个过渡性文件夹（staging folder）中。在这两种情况下，您都可以使用`Set-DfsrMembership` cmdlet来设置该文件夹的最大容量（即配额）。通过调整该cmdlet中的参数，您可以控制用于启动或停止删除旧文件的配额占用百分比。

默认情况下，DFS复制功能会启用调试日志记录。您可以禁用日志记录功能。此外，您还可以更改写入每个日志文件的行数、日志文件中消息的严重程度、需要保留的日志文件数量以及存储日志文件的位置。

## 示例

### 示例 1：配置一台计算机以使用动态 RPC 端口
```
PS C:\> Set-DfsrServiceConfiguration -RPCPort 0
ComputerName                      : SRV01
RPCPort                           :
DynamicRPCPort                    : True
DisableDebugLog                   : False
MaximumDebugLogFiles              : 1000
DebugLogPath                      : C:\Windows\debug
DebugLogSeverity                  : 4
MaximumDebugLogMessages           : 200000
UnexpectedAutoRecovery            : False
CleanupStagingFolderAtPercent     : 90
CleanupStagingFolderUntilPercent  : 60
CleanupConflictFolderAtPercent    : 90
CleanupConflictFolderUntilPercent : 60
```

此命令配置本地计算机使用动态 RPC 端口进行 DFS 复制。将 *RPCPort* 参数设置为 0 或 $Null 可使计算机使用动态端口。

### 示例 2：配置所有成员以特定严重级别记录日志信息
```
PS C:\> Get-DfsrMember | Set-DfsrServiceConfiguration -DebugLogSeverity 5
ComputerName                      : SRV01
RPCPort                           :
DynamicRPCPort                    : True
DisableDebugLog                   : False
MaximumDebugLogFiles              : 1000
DebugLogPath                      : C:\Windows\debug
DebugLogSeverity                  : 5
MaximumDebugLogMessages           : 200000
UnexpectedAutoRecovery            : False
CleanupStagingFolderAtPercent     : 90
CleanupStagingFolderUntilPercent  : 60
CleanupConflictFolderAtPercent    : 90
CleanupConflictFolderUntilPercent : 60

ComputerName                      : SRV02
RPCPort                           :
DynamicRPCPort                    : True
DisableDebugLog                   : True
MaximumDebugLogFiles              : 1000
DebugLogPath                      : C:\Windows\debug
DebugLogSeverity                  : 5
MaximumDebugLogMessages           : 200000
UnexpectedAutoRecovery            : False
CleanupStagingFolderAtPercent     : 90
CleanupStagingFolderUntilPercent  : 60
CleanupConflictFolderAtPercent    : 90
CleanupConflictFolderUntilPercent : 60
```

此命令将所有复制组中的所有成员的日志记录严重级别设置为 5。该命令通过使用 **Get-DfsrMember** cmdlet 来获取所有复制组的所有成员信息，然后通过管道运算符将这些成员传递给 **Set-DfsrServiceConfiguration** cmdlet。该 cmdlet 将调试日志记录的严重级别设置为 5。此命令会修改两台成员计算机的相关设置。控制台会显示这两台成员的计算机的详细信息，包括它们新的严重级别设置。

## 参数

### -CleanupConflictFolderAtPercent
指定一个介于80到100之间的百分比值。默认值为90。

当 `ConflictsAndDeleted` 文件夹的大小达到该文件夹配额的指定百分比时，DFS 复制服务会删除最旧的文件，直到文件夹大小降至配额的某个设定百分比以下。您可以通过使用 `CleanupConflictFolderUntilPercent` 参数来指定这个百分比值。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 10
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CleanupConflictFolderUntilPercent
指定一个介于 10 到 100 之间的百分比值。默认值为 60。

在DFS复制服务开始清理“ConflictsAndDeleted”文件夹后，它会继续删除最旧的文件，直到该文件夹的大小达到“ConflictsAndDeleted”配额的指定百分比。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 11
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CleanupStagingFolderAtPercent
指定一个介于80到100之间的百分比值。默认值为90。

当 staging 文件夹的大小达到该文件夹配额的指定百分比时，DFS 复制服务会删除最旧的文件，直到文件夹大小降至配额的某个设定百分比以下。您可以通过使用 *CleanupStagingFolderUntilPercent* 参数来指定这个百分比值。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 8
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CleanupStagingFolderUntilPercent
指定一个介于 10 到 80 之间的百分比值。默认值为 60。

在DFS复制服务开始清理临时文件夹后，它会继续删除最旧的文件，直到文件夹的大小达到临时文件夹配额的指定百分比为止。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 9
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一组复制成员计算机的名称。该 cmdlet 会修改这些成员计算机的成员资格设置。您可以使用逗号分隔的列表以及通配符（*）。如果您不指定此参数，cmdlet 将修改当前计算机的设置。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: MemberList, MemList

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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

### -DebugLogPath
指定用于DFS复制调试日志的文件夹路径。日志的默认存储位置是%SystemRoot%\Debug。如果您通过此参数指定了自定义的日志存储位置，请选择DFS复制不用于复制的驱动器。选择DFS复制不使用的驱动器可以最大限度地减少日志记录对复制性能的影响。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DebugLogSeverity
用于指定调试日志条目的严重级别。此参数的可接受值为：

- 1 - Write log header information only.
- 2 - Write errors and header information.
- 3 - Write warning, error, and header information.
- 4 - Write informational, warning, error, and header information.
- 5 - Write trace, informational, warning, error, and header information.

在DFS复制计算机上，默认的严重性级别为4。如果将严重性级别提高，性能可能会受到影响；因此请仅在排查故障时使用更高级别的严重性设置。如果降低严重性级别，虽然性能会有所提升，但可能会导致丢失用于故障排查所需的信息以及问题的根本原因数据。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableDebugLog
用于指示是否禁用调试日志记录功能。如果禁用了调试日志记录，性能会有所提升，但可能会丢失用于排查问题所需的信息以及问题的根本原因相关信息。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumDebugLogFiles
指定要保留的调试日志文件的数量。该参数的可接受值为：从零（0）到100,000之间的整数。默认情况下，DFS复制会存储1000个日志文件。如果设置的值过大，可能会影响性能。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumDebugLogMessages
指定每个调试日志文件中应写入的消息数量。该参数的可接受值为：从 1000 到 4294967295 之间的整数。默认值为 200,000。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 6
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RPCPort
为DFS复制服务指定一个静态TCP端口，以便该服务通过远程过程调用（RPC）协议进行监听。此参数的可接受值为：1024到65535之间的整数。默认情况下，DFS复制会使用动态端口进行监听。如果要使DFS复制使用动态端口，请指定值0或$Null。

微软推荐使用动态端口。不过，为了满足防火墙的要求，您可能需要指定一个静态端口。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UnexpectedAutoRecovery
该参数用于指定是否将名为 **StopReplicationAutoRecovery** 的注册表键的值设置为 0（关闭自动恢复功能）或 1（启用自动恢复功能）。当值为 0 时，服务器在非正常关机或硬件故障后可以自动恢复。如果需要将该注册表键的值设置为 1，请指定 $False。默认值为 0。

当服务器错误地关闭后又自动恢复时，必须对数据库进行验证。将相关参数的值设置为“1”后，你可以在恢复复制之前执行其他恢复操作、备份或故障排查步骤。

该参数的推荐值为 $True。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 7
Default value: None
Accept pipeline input: False
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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 字符串（String）

## 输出

### DfsrServiceConfiguration

## 备注

## 相关链接

[Get-DfsrServiceConfiguration](./Get-DfsrServiceConfiguration.md)

[Get-DfsrMember](./Get-DfsrMember.md)

[Set-DfsrMembership](./Set-DfsrMembership.md)

