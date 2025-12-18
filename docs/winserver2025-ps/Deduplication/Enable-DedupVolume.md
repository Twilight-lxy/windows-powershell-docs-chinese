---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DedupVolume.cdxml-help.xml
Module Name: Deduplication
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/deduplication/enable-dedupvolume?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-DedupVolume
---

# Enable-DedupVolume

## 摘要
支持在一个或多个卷上实现数据去重功能。

## 语法

```
Enable-DedupVolume [-Volume] <String[]> [-DataAccess] [-UsageType <UsageType>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

`Enable-DedupVolume` cmdlet 可以在一个或多个卷上启用数据去重功能。你可以使用 `Set-DedupVolume` cmdlet 来自定义数据去重的设置。默认情况下，数据去重是处于禁用状态的。某些卷不支持数据去重功能，例如那些不是 NTFS 文件系统的卷，或者体积小于 2 GB 的卷。

## 示例

### 示例 1：在卷上启用数据去重功能

```powershell
Enable-DedupVolume -Volume "D:","E:","F:"
```

此命令可对`D:`、`E:`和`F:`这些卷启用数据去重功能。该命令未为**UsageType**参数指定具体值，因此该cmdlet会使用适用于通用文件服务器操作的默认设置。

### 示例 2：为 Hyper-V 存储在卷上启用数据去重功能

```powershell
Enable-DedupVolume -Volume "D:" -UsageType HyperV
```

此命令允许在D:卷上进行数据复制。该命令指定了使用Hyper-V存储作为该卷的存储类型。

### 示例 3：使用 GUID 启用卷上的数据去重功能

```powershell
Enable-DedupVolume -Volume "\\?\Volume{26a21bda-a627-11d7-9931-806e6f6e6963}\"
```

此命令可为GUID为`26a21bda-a627-11d7-9931-806e6f6e6963`的卷启用数据去重功能。

### 示例 4：恢复对指定卷的 I/O 活动

```powershell
Enable-DedupVolume -Volume "X:" -DataAccess
```

此命令会恢复指定卷上的数据去重I/O操作。实际上，该命令会使数据去重文件系统迷你过滤器连接到指定的卷上。

## 参数

### -AsJob

将该cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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

### -DataAccess

表示已启用对卷上已去重文件的数据访问功能。

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

### -ThrottleLimit

该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM コマンド的数量来计算该コマンド的最佳限制值。此限制仅适用于当前执行的コマンド，而不影响整个会话或计算机本身。

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

### -UsageType

指定卷的工作负载类型。此cmdlet会将若干低级设置设置为适合您所指定使用类型的默认值。如果您为已启用数据去重的卷指定该参数，cmdlet会将其设置修改为相应的默认值；如果您在已启用数据去重的卷上运行此cmdlet但不指定该参数，则cmdlet不会更改该卷的使用类型。该参数的可接受值为：

- `HyperV` A volume for Hyper-V storage.
- `Backup` A volume that is optimized for virtualized backup servers.
- `Default` A general purpose volume. If you do not specify a value for this parameter, the cmdlet
  uses a value of Default.

如果您指定了一个 HyperV 的值，那么启用数据去重的计算机不能与运行 HyperV 的同一台计算机相同。这两台计算机必须通过远程方式进行通信。

```yaml
Type: UsageType
Parameter Sets: (All)
Aliases:
Accepted values: Default, HyperV, Backup

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Volume

指定一组系统卷。可以提供一个或多个卷ID、驱动器字母或卷GUID路径。对于驱动器字母，请使用格式“D:”。对于卷GUID路径，请使用格式“\\?\Volume{{GUID}}”。多个卷之间用逗号分隔。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases: DeviceId, Path, Name

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[ Disable-DedupVolume](./Disable-DedupVolume.md)

[Get-DedupVolume](./Get-DedupVolume.md)

[Set-DedupVolume](./Set-DedupVolume.md)
