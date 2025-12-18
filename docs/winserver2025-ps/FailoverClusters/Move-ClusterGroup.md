---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/move-clustergroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Move-ClusterGroup
---

# 移动集群组（Move-ClusterGroup）

## 摘要
将一个集群角色（即资源组）从一个节点迁移到故障转移集群中的另一个节点。

## 语法

```
Move-ClusterGroup [[-Name] <String>] [[-Node] <String>] [-IgnoreLocked] [-Wait <Int32>]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Move-ClusterGroup` cmdlet 可以将一个集群角色（即资源组）从一个节点移动到故障转移集群中的另一个节点。

移动资源组是一种模拟故障转移的方法。运行此cmdlet也是在为节点进行常规维护做准备时应该采取的适当步骤。

## 示例

### 示例 1

```powershell
Move-ClusterGroup -Name MyFileServer
```

这个示例将名为 `MyFileServer` 的集群服务从当前的所有者节点迁移到其他任意节点上。

### 示例 2

```powershell
Move-ClusterGroup -Name MyFileServer -Node node2
```

这个示例将名为 `MyFileServer` 的资源组从当前的所有者节点移动到名为 `node2` 的节点上。

### 示例 3

```powershell
Get-ClusterNode node3 | Get-ClusterGroup | Move-ClusterGroup
```

这个示例会将当前由名为 `node3` 的节点拥有的所有资源组转移到其他节点上。在对指定节点进行维护操作之前，请使用此cmdlet。

### 示例 4

```powershell
Move-ClusterGroup -Name MyFileServer -Node node2 -Wait 0
```

这个示例将名为 `MyFileServer` 的资源组从当前的所有者节点移动到名为 `node2` 的节点。在移动过程中，关于 `MyFileServer` 的信息会立即显示出来。

## 参数

### -Cluster

指定用于运行此cmdlet的集群名称。如果该参数的输入值为`.`或被省略，则cmdlet将在本地集群上运行。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IgnoreLocked

指定在运行该cmdlet时忽略已被锁定的组。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定要移动的资源组。

```yaml
Type: PSObject
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name

指定要移动的资源组的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Node

指定要将资源组移动到的集群节点的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Wait

指定用于等待该cmdlet完成的时间（以秒为单位）。如果未指定**Wait**参数，则cmdlet会一直等待直到完成；如果指定了`-Wait 0`，则命令会被立即执行，且cmdlet会在不等待的情况下返回结果。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell-clusterGroup

## 输出

### MicrosoftFailoverClusters.PowerShell-clusterGroup

## 备注

## 相关链接

[添加集群组](./Add-ClusterGroup.md)

[Get-ClusterGroup](./Get-ClusterGroup.md)

[Remove-ClusterGroup](./Remove-ClusterGroup.md)

[Start-ClusterGroup](./Start-ClusterGroup.md)

[Stop-ClusterGroup](./Stop-ClusterGroup.md)
