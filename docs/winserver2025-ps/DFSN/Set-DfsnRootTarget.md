---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsNamespaceRootTarget.cdxml-help.xml
Module Name: DFSN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsn/set-dfsnroottarget?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DfsnRootTarget
---

# Set-DfsnRootTarget

## 摘要
更改分布式文件系统（DFS）命名空间中根目标的设置。

## 语法

```
Set-DfsnRootTarget [-Path] <String> [-TargetPath] <String> [[-State] <State>]
 [[-ReferralPriorityClass] <ReferralPriorityClass>] [[-ReferralPriorityRank] <UInt32>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Set-DfsnRootTarget` cmdlet 用于更改分布式文件系统（DFS）命名空间根目标的设置。您可以修改 DFS 命名空间目标的状态，并配置引用操作的优先级类别和优先级等级。

DFS命名空间文件夹包含一个或多个文件夹目标，这些文件夹目标是计算机上的共享文件夹。当客户端尝试连接到某个文件夹时，DFS命名空间服务器会提供一份文件夹目标的列表（称为引用信息）。服务器会确定这些引用信息的显示顺序，客户端会按照服务器提供的顺序尝试连接到相应的文件夹目标。

有关DFS命名空间的更多信息，请参阅TechNet上的[DFS命名空间概述](https://technet.microsoft.com/library/cc730736)。

## 示例

### 示例 1：设置推荐优先级值

```powershell
Set-DfsnRootTarget -Path '\\contoso.com\dfsroot' -TargetPath '\\Contoso-fs\dfsroot' -ReferralPriorityClass 'GlobalLow'
```

此命令将引用优先级类别设置为“GlobalLow”，适用于路径为 `\\Contoso\AccountingSoftware` 以及目标路径为 `\\Contoso-FS\AccountingSoftware` 的 DFS 命名空间根目标。

## 参数

### -AsJob

以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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

在运行cmdlet之前，会提示您进行确认。

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

指定一个用于DFS命名空间根目录的路径。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: DfsPath, NamespaceRoot

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReferralPriorityClass

用于指定DFS命名空间根目标的优先级类别。目标优先级使您能够对站点内的目标进行分类和排序：您可以指定某些目标获得最高的优先级，或者最低的优先级；同时，您还可以根据这些目标对DFS客户端连接的成本来对剩余的目标进行划分。该参数的可接受取值为：

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

指定DFS命名空间中根目标的优先级等级（以整数表示）。数值越小，优先级越高；数值为零（0）表示最高优先级。

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

指定DFS命名空间根目标的状态。该参数的可接受值包括：

- `Online`
- `Offline`

Clients do not receive referrals for a DFS namespace target that is offline.

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

指定DFS命名空间中某个根目标的路径。此cmdlet会更改该路径所指向的根目标的设置。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: Target, DfsTarget, RootTargetPath

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit

指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

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

此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### Microsoft.PowerShell Cmdletization GeneratedTypes.DfsNamespaceRootTarget.State

### Microsoft.PowerShell Cmdletization GeneratedTypes.DfsNamespaceRootTarget_ReferralPriorityClass

### System.UInt32

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接

[Get-DfsnRootTarget](./Get-DfsnRootTarget.md)

[New-DfsnRootTarget](./New-DfsnRootTarget.md)

[Remove-DfsnRootTarget](./Remove-DfsnRootTarget.md)
