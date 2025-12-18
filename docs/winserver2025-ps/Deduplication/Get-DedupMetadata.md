---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DedupMetadata.cdxml-help.xml
Module Name: Deduplication
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/deduplication/get-dedupmetadata?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DedupMetadata
---

# Get-DedupMetadata

## 摘要
返回具有数据去重元数据的卷的元数据。

## 语法

```
Get-DedupMetadata [[-Volume] <String[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

`Get-DedupMetadata` cmdlet 为每个具有优化元数据的卷返回一个 `DeduplicationMetadata` 对象。`DeduplicationMetadata` 对象包含只读属性，这些属性用于描述去重数据存储的特性，例如数据块的数量、容器的数量、平均数据块大小以及其他统计信息。

因为这个cmdlet必须扫描整个文件系统，所以运行它需要一些时间。

此cmdlet不能作为调度任务的一部分来运行，必须手动执行。如果在启动此cmdlet时指定的卷上正在运行其他优化任务，则该cmdlet会失败。此外，如果文件系统扫描和cmdlet处理所需的内存不足，也会导致命令执行失败。如果cmdlet执行失败，请查看事件日志和记录文件以获取更多详细信息。

要运行此 cmdlet，必须使用“以管理员身份运行”选项启动 Windows PowerShell®。

此 cmdlet 返回以下属性：

- `CorruptionCount`
  - Indicates the number of corruptions found on the volume.
- `DataChunkAverageSize`
  - Indicates the data store size, not including chunk metadata, divided by the total number of data
    chunks in the data store.
- `DataChunkCount`
  - Indicates the number of data chunks in a container.
- `DataContainerCount`
  - Indicates the number of containers in the data store.
- `HotspotContainerCount`
  - Indicates the number of hotspots in the stream map store.
- `HotspotCount`
  - Indicates the number of hotspots in a container.
- `StreamMapAverageChunkCount`
  - Indicates the stream map store size divided by the total number of streams in the store.
- `StreamMapContainerCount`
  - Indicates the number of containers in the stream map store.
- `StreamMapCount`
  - Indicates the number of data streams in a container.

## 示例

#### 示例 1：获取卷的元数据

```powershell
Get-DedupMetadata -Volume "D:"
```

这个命令可以获取 `D:` 卷的元数据信息。

## 参数

### -AsJob

将此cmdlet作为后台作业运行。使用该参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

在远程会话或远程计算机上运行该Cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) Cmdlet 所生成的会话对象）。默认情况下，该Cmdlet会在本地计算机的当前会话中运行。

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

该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

指定一个或多个文件系统卷，以返回相应的 **DeduplicationVolumeMetadata** 对象。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/Microsoft/Windows/Deduplication/MSFT_DedupVolumeMetadata

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Measure-DedupFileMetadata](./Measure-DedupFileMetadata.md)
