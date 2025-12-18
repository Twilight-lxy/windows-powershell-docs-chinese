---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DedupStatus.cdxml-help.xml
Module Name: Deduplication
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/deduplication/update-dedupstatus?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-DedupStatus
---

# Update-DedupStatus

## 摘要
扫描各个卷以查找新的数据，从而实现重复数据删除带来的节省效果。

## 语法

```
Update-DedupStatus [[-Volume] <String[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

`Update-DedupStatus` cmdlet 会扫描一个或多个指定的卷，以计算新的数据去重节省信息。该 cmdlet 会返回一个 **DeduplicationStatus** 对象。若需快速访问缓存的元数据，请使用 `Get-DedupStatus`。当此 cmdlet 通过一次调用同时处理多个卷时，每个卷的分析会依次进行（即按顺序执行）。

> [!注意] > 在处理大量数据时，此cmdlet的运行时间可能会超过几分钟，并且在初始扫描之后总会执行一次重新扫描。默认行为是等待操作完成，无论扫描和重新扫描所需的时间长短如何。

要运行此cmdlet，您必须使用“以管理员身份运行”选项启动Windows PowerShell®。

此cmdlet返回以下元数据：

- `DedupSavedSpace`
  - Saved space is the difference between the logical size of the optimized files
  and the logical size of the store. This is the deduplicated user data plus data deduplication
  metadata. This number changes continually.
- `DedupRate`
  - Data deduplication rate is the ratio of data deduplication saved space to the logical
  size of all of the files on the volume and is expressed in percentage. This number will change
  continually.
- `OptimizedFilesCount`
  - Optimized files count is the number of optimized files on the specified volume. This number
    remains steady, instead of decreasing, as users delete files from, or add files to, the volume,
    until a garbage collection job is run. This count is most accurate after a garbage collection
    job runs.
- `OptimizedFilesSize`
  - Optimized files size is the aggregate size of all optimized files on the specified volume. This
    number remains steady, instead of decreasing, as users delete files from, or add new files to,
    the volume, until a garbage collection job is run. This number is most accurate after a garbage
    collection job runs.
- `InPolicyFilesCount`
  - In policy files count is the number of files that currently qualify for optimization. This
    number stays relatively constant between optimization jobs.
- `InPolicyFilesSize`
  - In policy files size is the aggregate size of all files that currently qualify for optimization.
    This number stays relatively constant between optimization jobs.
- `LastOptimizationTime`
  - Last optimization time specifies the data and time when an optimization job was run last on the
    specified volume. This date and time stays constant between optimization jobs.
- `LastGarbageCollectionTime`
  - Last garbage collection time specifies the data and time when a garbage collection job was run
    last on the specified volume. This date and time stays constant between optimization jobs.
- `LastScrubbingTime`
  - Last scrubbing time specifies the data and time when a scrubbing job was run last on the
    specified volume. This date and time stays constant between optimization jobs.

## 示例

### 示例 1：扫描某个文件以获取储蓄信息

```powershell
Update-DedupStatus -Volume "D:"
```

该命令会扫描`D:`磁盘以计算数据去重所带来的节省效果。

## 参数

### -AsJob

将 cmdlet 作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 `[New-CimSession](/powershell/module/cimcmdlets/new-cimsession)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，使用的是本地计算机上的当前会话。

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

### -ThrottleLimit

该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值为`0`，那么Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算一个最优的操作限制值。此操作限制仅适用于当前执行的cmdlet，而不影响整个会话或计算机本身的运行状态。

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

### -Volume

指定一个或多个需要扫描并计算新的数据去重节省信息的文件系统卷。请输入一个或多个卷ID、驱动器字母或卷GUID路径。对于驱动器字母，请使用格式`D:`；对于卷GUID路径，请使用格式`\\?\Volume{{GUID}}`。多个卷之间用逗号分隔。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases: Path, Name, DeviceId

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DedupStatus](./Get-DedupStatus.md)
