---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsNamespaceFolderTarget.cdxml-help.xml
Module Name: DFSN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsn/new-dfsnfoldertarget?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-DfsnFolderTarget
---

# New-DfsnFolderTarget

## 摘要
向DFS命名空间文件夹中添加一个目标（target）。

## 语法

```
New-DfsnFolderTarget [-Path] <String> [-TargetPath] <String> [[-State] <State>]
 [[-ReferralPriorityClass] <ReferralPriorityClass>] [[-ReferralPriorityRank] <UInt32>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`New-DfsnFolderTarget` cmdlet 用于向分布式文件系统（DFS）的命名空间文件夹中添加一个目标。需要指定 DFS 命名空间文件夹以及该文件夹的目标位置。您可以设置 DFS 命名空间目标的状态，并配置引用相关的优先级类别和优先级等级。

一个DFS命名空间文件夹包含一个或多个目标文件夹，这些目标文件夹是位于不同计算机上的共享文件夹。当客户端尝试连接到某个文件夹时，DFS命名空间服务器会提供一份目标文件夹的列表（称为“引用”）。服务器会确定这些引用文件的目标连接顺序，客户端会按照服务器提供的顺序依次尝试连接到相应的目标文件夹。

有关DFS命名空间的更多信息，请参阅TechNet上的[DFS命名空间概述](https://technet.microsoft.com/library/cc730736)。

## 示例

### 示例 1：添加一个目标

```powershell
New-DfsnFolderTarget -Path '\\Contoso\AccountingResources\LegacySoftware' -TargetPath '\\Contoso-FS\Software' -ReferralPriorityClass 'GlobalLow'
```

此命令将 `\\Contoso-FS\Software` 添加为 DFS 命名空间文件夹 `\\Contoso\AccountingResources\LegacySoftware` 的目标，其引用优先级设置为“全局低”。

## 参数

### -AsJob

以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

在远程会话或远程计算机上运行该cmdlet。输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -Confirm

在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path

指定DFS命名空间文件夹的路径。此cmdlet会为具有所指定路径的文件夹添加一个目标（即对该文件夹进行操作）。

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

### -ReferralPriorityClass

用于指定 DFS 命名空间文件夹目标的优先级类别。目标优先级允许您对站点内的目标进行分类和排序：您可以指定某些目标获得最高或最低的优先级，并根据这些目标对 DFS 客户端来说的连接成本来划分其余的目标。该参数的可接受取值如下：

- `GlobalHigh` - The highest priority class for a DFS target. Targets assigned this class receive
  global preference.
- `SiteCostHigh` - The highest site cost priority class for a DFS target. Targets assigned this
  class receive the most preference among targets of the same site cost for a given DFS client.
- `SiteCostNormal` - The middle or normal site cost priority class for a DFS target.
- `SiteCostLow` - The lowest site cost priority class for a DFS target. Targets assigned this class
  receive the least preference among targets of the same site cost for a given DFS client.
- `GlobalLow` - The lowest level of priority class for a DFS target. Targets assigned this class
  receive the least preference globally.

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.DfsNamespaceRootTarget.ReferralPriorityClass
Parameter Sets: (All)
Aliases: PriorityClass, Class
Accepted values: SiteCostNormal, GlobalHigh, SiteCostHigh, SiteCostLow, GlobalLow

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReferralPriorityRank

用于指定 DFS 命名空间文件夹目标的优先级等级（以整数形式表示）。数值越低，优先级越高；数值为零（0）表示最高优先级。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: PriorityRank, Rank

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -State

指定DFS命名空间根目标的状态。此参数的可接受值为：

- `Online`
- `Offline`

Clients do not receive referrals for a DFS namespace folder target that is offline.

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.DfsNamespaceRootTarget.State
Parameter Sets: (All)
Aliases:
Accepted values: Offline, Online

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetPath

指定一个DFS命名空间文件夹目标的路径。此cmdlet会将指定的路径添加为该文件夹的目标。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: Target, DfsTarget, FolderTarget

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时运行的最大操作数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -WhatIf

展示了如果该cmdlet被运行时会发生什么情况。不过实际上这个cmdlet并没有被运行。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### Microsoft.PowerShell Cmdletization GeneratedTypes.DfsNamespaceFolderTarget.State

### Microsoft.PowerShell Cmdletization GeneratedTypes.DfsNamespaceFolderTarget.ReferralPriorityClass

### System.UInt32

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接

[Get-DfsnFolderTarget](./Get-DfsnFolderTarget.md)

[Remove-DfsnFolderTarget](./Remove-DfsnFolderTarget.md)

[Set-DfsnFolderTarget](./Set-DfsnFolderTarget.md)
