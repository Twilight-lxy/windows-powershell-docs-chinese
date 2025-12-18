---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/23/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/stop-clusternode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-ClusterNode
---

# 停止集群节点

## 摘要
在故障转移集群中，停止某个节点上的Cluster服务。

## 语法

```
Stop-ClusterNode [[-Name] <StringCollection>] [-Wait <Int32>] [-InputObject <PSObject>]
 [-Cluster <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Stop-ClusterNode` cmdlet 用于停止故障转移集群中某个节点上的 Cluster 服务。如果停止该节点会导致集群的成员数量低于法定人数（quorum），则不允许执行此操作。如果要停止整个集群，请使用 `Stop-Cluster` cmdlet。

注意：如果服务器计算机上没有启用凭据安全服务提供程序（CredSSP）进行身份验证，则无法远程运行此cmdlet。

## 示例

### 示例 1：在本地集群节点上停止 Cluster 服务

```powershell
Stop-ClusterNode -Name "node3"
```

这个示例会停止本地集群中名为 `node3` 的节点上的 Cluster 服务。

### 示例 2：在集群节点上停止 Cluster 服务

```powershell
Stop-ClusterNode -Name "node1" -Cluster "cluster2"
```

这个示例会停止名为 `cluster2` 的集群中名为 `node1` 的节点上的 Cluster 服务。

## 参数

### -Cluster

指定要运行此cmdlet的集群名称。如果该参数的输入值为`.`或被省略，则cmdlet将在本地集群上运行。

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

### -Confirm

在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定要停止运行的集群节点。

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

指定要停止运行的集群节点的名称。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Wait

指定等待该 cmdlet 完成的时间（以秒为单位）。如果未指定 **Wait** 参数，那么 cmdlet 会一直等待其完成；如果指定了 `-Wait 0`，则命令会被立即执行，cmdlet 会在不等待的情况下返回结果。

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

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters.PowerShell ClusterNode

## 输出

## 备注

## 相关链接

[Add-ClusterNode](./Add-ClusterNode.md)

[Get-ClusterNode](./Get-ClusterNode.md)

[Remove-ClusterNode](./Remove-ClusterNode.md)

[Resume-ClusterNode](./Resume-ClusterNode.md)

[开始创建集群节点](./Start-ClusterNode.md)

[停止集群操作](./Stop-Cluster.md)

[暂停集群节点](./Suspend-ClusterNode.md)
