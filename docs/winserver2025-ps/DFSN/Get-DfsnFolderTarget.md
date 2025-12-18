---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsNamespaceFolderTarget.cdxml-help.xml
Module Name: DFSN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsn/get-dfsnfoldertarget?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsnFolderTarget
---

# Get-DfsnFolderTarget

## 摘要
获取DFS命名空间文件夹的目标设置信息。

## 语法

```
Get-DfsnFolderTarget [-Path] <String> [[-TargetPath] <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

`Get-DfsnFolderTarget` cmdlet 可用于获取分布式文件系统（DFS）命名空间文件夹的目标设置。您可以指定一个 DFS 命名空间文件夹路径来查看该路径下的所有目标；或者同时指定命名空间路径和目标路径，以查看特定目标的详细设置。

有关DFS命名空间的更多信息，请参阅[DFS命名空间概述](/windows-server/storage/dfs-namespaces/dfs-overview)。

## 示例

### 示例 1：获取目标的设置信息

```powershell
Get-DfsnFolderTarget -Path '\\Contoso\AccountingResources\LegacySoftware' -TargetPath '\\Contoso-FS\LegacySoftware'
```

```Output
NamespacePath         : \\Contoso\AccountingResources\LegacySoftware
ReferralPriorityClass : sitecost-normal
ReferralPriorityRank  : 0
State                 : Online
TargetPath            : \\Contoso-FS\LegacySoftware
PSComputerName        :
```

此命令用于获取“\\Contoso\AccountingResources\LegacySoftware”文件夹的设置信息，其中该文件夹的目标路径为“\\Contoso-FS\LegacySoftware”。

## 参数

### -AsJob

将该cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个代表该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: Microsoft.Management.Infrastructure.CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path

指定一个DFS命名空间的根文件夹的路径。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DfsPath, FolderPath, NamespacePath

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetPath

指定一个DFS命名空间文件夹的目标路径。此cmdlet会获取与该路径对应的目标的设置信息。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: Target, DfsTarget, FolderTarget

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时运行的命令行脚本（cmdlet）的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算一个最优的并发限制。这个并发限制仅适用于当前执行的命令行脚本，而不适用于整个会话或整个计算机。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### Microsoft.ManagementInfrastructure.CimInstance[]

## 备注

## 相关链接

[New-DfsnFolderTarget](./New-DfsnFolderTarget.md)

[Remove-DfsnFolderTarget](./Remove-DfsnFolderTarget.md)

[Set-DfsnFolderTarget](./Set-DfsnFolderTarget.md)
