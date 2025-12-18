---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsNamespaceFolder.cdxml-help.xml
Module Name: DFSN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsn/set-dfsnfolder?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DfsnFolder
---

# Set-DfsnFolder

## 摘要
更改DFS命名空间文件夹的设置。

## 语法

```
Set-DfsnFolder [-Path] <String> [[-EnableInsiteReferrals] <Boolean>]
 [[-EnableTargetFailback]<Boolean>] [[-State] <State>] [[-TimeToLiveSec] <UInt32>]
 [[-Description] <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Set-DfsnFolder` cmdlet 用于更改分布式文件系统（DFS）命名空间文件夹的设置。

DFS命名空间文件夹包含一个或多个作为共享文件夹的文件夹目标。当客户端尝试连接到某个文件夹时，DFS命名空间服务器会提供一份文件夹目标的列表（这些文件夹目标被称为“引用”）。服务器会确定这些引用的连接顺序，客户端会按照服务器提供的顺序尝试连接到相应的文件夹目标。

您可以使用此cmdlet来启用或禁用以下设置：

- **In-site referrals**
- **Target failback**

您还可以添加或修改描述性注释，更改 DFS 命名空间的状态，或者设置引用消息的生存时间（TTL）间隔。

有关DFS命名空间的更多信息，请参阅TechNet上的[DFS命名空间概述](https://technet.microsoft.com/library/cc730736)。

## 示例

### 示例 1：为 DFS 命名空间文件夹启用设置

```powershell
Set-DfsnFolder -Path '\\Contoso\AccountingResources\LegacySoftware' -EnableInsiteReferrals $true -EnableTargetFailback $true
```

此命令为DFS命名空间文件夹`\\Contoso\AccountingResources\LegacySoftware`启用了内部引用（in-site referrals）和目标故障切换（target failback）功能。

## 参数

### -AsJob

以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的任务。

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

在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -Description

为DFS命名空间文件夹指定一个描述信息。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: desc

Required: False
Position: 5
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableInsiteReferrals

该值用于指示DFS命名空间服务器是否仅向客户端提供与客户端位于同一站点内的引用（referrals）。如果值为 `$true`，则表示DFS命名空间服务器仅提供同一站点内的引用；如果值为 `$false`，则表示DFS命名空间服务器会先提供同一站点内的引用，然后再提供其他站点的引用。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: insite

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableTargetFailback

该值用于指示DFS命名空间是否使用目标服务器的故障切换机制。当客户端尝试访问某个服务器上的目标链接，但该服务器不可用时，客户端会自动切换到另一个备用服务器。如果该值为 `$true`，则当第一个服务器重新可用后，客户端会自动恢复与该服务器的连接；如果该值为 $false$，则表示DFS命名空间服务器不要求客户端必须使用首选服务器。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: failback, TargetFailback

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path

指定 DFS 命名空间文件夹的路径。此 cmdlet 会修改具有所指定路径的文件夹。

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

### -State

用于指定 DFS 命名空间文件夹的状态。该参数的可接受值为：

- `Online`
- `Offline`

Clients do not receive referrals for a DFS namespace folder that is offline.

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.DfsNamespaceRootTarget.State
Parameter Sets: (All)
Aliases:
Accepted values: Offline, Online

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit

指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

指定引用（referrals）的TTL间隔（以秒为单位）。客户端会将引用信息存储到目标对象中，存储时间为该TTL间隔所设定的时长。文件夹引用的默认TTL间隔为1800秒（30分钟）。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: ttl, TimeToLive

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf

展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

### SystemBoolean

### Microsoft.PowerShell Cmdletization GeneratedTypes.DfsNamespaceFolder.State

### System.UInt32

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接

[Get-DfsnFolder](./Get-DfsnFolder.md)

[Move-DfsnFolder](./Move-DfsnFolder.md)

[New-DfsnFolder](./New-DfsnFolder.md)

[Remove-DfsnFolder](./Remove-DfsnFolder.md)
