---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DedupVolume.cdxml-help.xml
Module Name: Deduplication
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/deduplication/get-dedupvolume?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DedupVolume
---

# Get-DedupVolume

## 摘要
返回具有数据去重元数据的去重卷。

## 语法

### 按体积计算Id（默认值）

```
Get-DedupVolume [-VolumeId <String[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 按体积计算

```
Get-DedupVolume [[-Volume] <String[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

`Get-DedupVolume` cmdlet 会为每个具有数据去重元数据的卷返回一个 `DeduplicationVolume` 对象，无论这些卷的去重功能是处于启用状态还是禁用状态。在集群环境中，该 cmdlet 仅会返回当前由管理节点挂载的卷的 `DeduplicationVolume` 对象，而这些卷可以是本地卷，也可以是集群中的卷。

要运行此cmdlet，您必须使用“以管理员身份运行”选项来启动Windows PowerShell®。

## 示例

#### 示例 1：获取由字母标识的卷的设置信息

```powershell
Get-DedupVolume -Volume "E:"
```

此命令返回卷`E:`的数据去重设置信息。

### 示例 2：获取由 ID 指定的卷的设置信息

```powershell
Get-DedupVolume -Volume "\\?\Volume{26a21bda-a627-11d7-9931-806e6f6e6963}\"
```

此命令会返回具有指定GUID的卷的数据去重设置信息。

## 参数

### -AsJob

将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者提供一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

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

该参数用于指定可以同时执行的操作的最大数量。如果省略了此参数或输入的值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlets 的数量来计算该 cmdlet 的最佳限制值（即并发操作的最多数量）。这个限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Volume

指定一个或多个文件系统卷，以获取数据去重元数据；在集群环境中，则是指由被管理节点当前挂载的、包含数据去重元数据的卷。请输入一个或多个卷ID、驱动器字母或卷 GUID 路径。使用驱动器字母时，请采用 `D:` 的格式；使用卷 GUID 路径时，请采用 `\\?\Volume{{GUID}}\` 的格式。多个卷之间请用逗号分隔。

```yaml
Type: System.String[]
Parameter Sets: ByVolume
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VolumeId

指定一个字符串，用于唯一标识要从中获取数据去重元数据的卷。

```yaml
Type: System.String[]
Parameter Sets: ByVolumeId
Aliases: DeviceId, Path, Id

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/Microsoft/Windows/Deduplication/MSFT_DedupVolume

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Disable-DedupVolume](./Disable-DedupVolume.md)

[Enable-DedupVolume](./Enable-DedupVolume.md)

[Set-DedupVolume](./Set-DedupVolume.md)
