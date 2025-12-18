---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DedupVolume.cdxml-help.xml
Module Name: Deduplication
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/deduplication/disable-dedupvolume?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-DedupVolume
---

# 禁用去重卷（Disable-DedupVolume）

## 摘要
禁用一个或多个卷上的数据去重操作。

## 语法

```
Disable-DedupVolume [-Volume] <String[]> [-DataAccess] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述

`Disable-DedupVolume` cmdlet 用于禁用一个或多个卷上的数据去重操作。在禁用数据去重后，该卷仍会保持去重状态，并且现有的已去重数据仍然可以访问。服务器将停止为该卷执行数据去重任务，新添加的数据也不会被进行去重处理。如果要重新启用某个卷的数据去重功能，可以使用 `Start-DedupJob` cmdlet，并在 **Type** 参数中指定 `Unoptimization`。

在禁用卷上的数据去重功能后，你可以对该卷执行所有只读类型的去重相关命令操作。例如，可以使用 `Get-DedupStatus` 命令来获取具有数据去重元数据的卷的去重状态信息。然而，在禁用了数据去重功能之后，你就不能再使用与数据去重相关的命令以及 `Update-DedupStatus` 命令来对该卷进行任何操作了。例如，如果你已经禁用了某个卷的数据去重功能，那么就无法再使用 `Start-DedupJob` 命令来启动该卷上的数据去重任务了。

## 示例

### 示例 1：禁用卷上的数据去重功能

```powershell
Disable-DedupVolume -Volume "D:","E:","F:","G:"
```

此命令将禁用驱动器`D:`、`E:`、`F:`和`G:`的数据去重功能。

### 示例 2：通过使用 GUID 来禁用卷上的数据去重功能

```powershell
Disable-DedupVolume -Volume "\\?\Volume{26a21bda-a627-11d7-9931-806e6f6e6963}\"
```

此命令将禁用GUID为`26a21bda-a627-11d7-9931-806e6f6e6963`的卷的数据去重功能。

### 示例 3：暂停指定卷的 I/O 操作

```powershell
Disable-DedupVolume -Volume "X:" -DataAccess
```

此命令会暂停指定卷上的数据去重操作（即I/O活动）。实际上，该命令会导致用于数据去重的文件系统迷你过滤器从该卷上断开连接。在该命令执行完成后，对数据去重文件的任何读写操作都会失败，并提示`ERROR_INVALID_FUNCTION`错误；这种情况将持续到运行`Enable-DedupVolume -DataAccess`命令或服务器重启为止。

## 参数

### -AsJob

以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的任务。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在会话中操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

表示已禁用对卷上已去重文件的数据访问功能。

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

该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在运行的 cmdlet，而不适用于整个会话或计算机本身。

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

指定一个系统卷数组，以禁用这些卷的数据去重功能。可以提供一个或多个卷ID、驱动器字母或卷GUID路径。对于驱动器字母，请使用格式 `D:`；对于卷GUID路径，请使用格式 `\\?\Volume{{GUID}}`。多个卷之间用逗号分隔。

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

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Enable-DedupVolume](./Enable-DedupVolume.md)

[Get-DedupVolume](./Get-DedupVolume.md)

[Set-DedupVolume](./Set-DedupVolume.md)

[Update-DedupStatus](./Update-DedupStatus.md)
