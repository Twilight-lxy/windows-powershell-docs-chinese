---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsNamespaceFolder.cdxml-help.xml
Module Name: DFSN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsn/new-dfsnfolder?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-DfsnFolder
---

# 新Dfsn文件夹

## 摘要
在分布式文件系统（DFS）命名空间中创建一个文件夹。

## 语法

```
New-DfsnFolder [-Path] <String> [-TargetPath] <String> [[-EnableInsiteReferrals] <Boolean>]
 [[-EnableTargetFailback] <Boolean>] [[-State] <State>] [[-TimeToLiveSec] <UInt32>]
 [[-Description] <String>] [[-TargetState] <State>]
 [[-ReferralPriorityClass] <ReferralPriorityClass>] [[-ReferralPriorityRank] <UInt32>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`New-DfsnFolder` cmdlet 用于在分布式文件系统（DFS）命名空间中创建一个文件夹。请指定新文件夹的路径以及目标文件夹的位置。

DFS命名空间文件夹包含一个或多个目标文件夹，这些目标文件夹是位于不同计算机上的共享文件夹。当客户端尝试连接到某个文件夹时，DFS命名空间服务器会提供一份目标文件夹的列表（称为“引用”）。服务器会确定这些引用文件的连接顺序，客户端会按照服务器提供的顺序依次尝试连接到相应的目标文件夹。

你可以为新文件夹指定设置。你可以使用这个 cmdlet 来启用或禁用以下设置：

- **In-site referrals**
- **Target failback**

您还可以添加描述性注释，选择文件夹的状态及目标文件夹，并设置引用内容的“生存时间”（Time to Live，简称TTL）间隔。

最后，您可以指定推荐任务的优先级类别和优先级等级。

有关DFS命名空间的更多信息，请参阅TechNet上的[DFS命名空间概述](https://technet.microsoft.com/library/cc730736)。

## 示例

#### 示例 1：创建一个DFS命名空间文件夹

```powershell
PS C:\> New-DfsnFolder -Path '\\Contoso\AccountingResources\LegacySoftware' -TargetPath '\\Contoso-FS\AccountingLegacy' -EnableTargetFailback $true -Description 'Folder for legacy software.'
```

此命令在 `\\Contoso\AccountingResources` 命名空间中创建一个名为 `LegacySoftware` 的文件夹。该文件夹的目标路径是 `\\Contoso-FS\AccountingLegacy`，并且该命令为该文件夹启用了目标故障恢复（failback）功能。此外，该命令还为新文件夹提供了描述信息。

## 参数

### -AsJob

以后台作业的方式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

在运行cmdlet之前会提示您进行确认。

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

### -Description

为DFS命名空间文件夹指定一个描述信息。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: desc

Required: False
Position: 6
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableInsiteReferrals

该值用于指示DFS命名空间服务器是否仅向客户端提供位于同一站点内的引用（referrals）。如果值为`$true`，则DFS命名空间服务器仅提供在同一站点内的引用；如果值为`$false`，则DFS命名空间服务器会先提供同一站点内的引用，然后再提供其他站点的引用。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: insite

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableTargetFailback

该值用于指示DFS命名空间是否使用目标服务器的故障恢复机制。当客户端尝试访问某台服务器上的目标资源时，如果该服务器不可用，客户端会自动切换到其他可用的服务器。如果该值为 `$true`，则一旦第一台服务器恢复正常运行，客户端会重新连接到该服务器；如果该值为 `$false$`，则表示DFS命名空间服务器不要求客户端必须切换回首选的服务器。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: failback, TargetFailback

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path

指定文件夹的路径。该路径必须是唯一的，并且不能是现有DFS命名空间文件夹的名称。

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

用于指定DFS命名空间文件夹的目标优先级类别。目标优先级功能允许您对站点内的目标进行分类和排序：您可以指定某些目标应获得最高或最低的优先级，同时还可以根据这些目标的连接成本来划分其余目标，以便DFS客户端能够选择合适的连接对象。该参数的可接受取值包括：

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
Position: 8
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReferralPriorityRank

指定深度优先搜索（DFS）命名空间中目标的优先级等级（以整数表示）。数值越低，优先级越高；数值为零（0）表示最高优先级。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: PriorityRank, Rank

Required: False
Position: 9
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -State

用于指定DFS命名空间文件夹的状态。该参数的可接受值包括：

- `Online`
- `Offline`

Clients do not receive referrals for a DFS namespace folder that is offline.

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.DfsNamespaceRootTarget.State
Parameter Sets: (All)
Aliases:
Accepted values: Offline, Online

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetPath

Specifies a path for a target for the DFS namespace folder.

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

### -TargetState

Specifies the state of the DFS namespace folder target. The acceptable values for this parameter
are:

- `Online`
- `Offline`

Clients do not receive referrals for a DFS namespace folder target that is offline.

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.DfsNamespaceRootTarget.State
Parameter Sets: (All)
Aliases:
Accepted values: Offline, Online

Required: False
Position: 7
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit

指定可以同时运行的最大操作数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -TimeToLiveSec

指定引用的TTL间隔（以秒为单位）。客户端会将引用信息存储到目标地址对应的位置，存储时间为该TTL间隔所设定的时长。文件夹引用的默认TTL间隔为1800秒（30分钟）。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: ttl, TimeToLive

Required: False
Position: 5
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。不过实际上这个cmdlet并没有被执行。

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

此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System(Boolean)

### Microsoft.PowerShell Cmdletization GeneratedTypes.DfsNamespaceFolder.State

### System.UInt32

### Microsoft.PowerShellCmdletizationGeneratedTypes.DfsNamespaceFolderTarget.State

### Microsoft.PowerShell CmdletIZATION GeneratedTypes.DfsNamespaceFolderTarget.ReferralPriorityClass

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接

[Get-DfsnFolder](./Get-DfsnFolder.md)

[Move-DfsnFolder](./Move-DfsnFolder.md)

[Remove-DfsnFolder](./Remove-DfsnFolder.md)

[Set-DfsnFolder](./Set-DfsnFolder.md)
