---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/start-cluster?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-Cluster
---

# 启动集群

## 摘要
在集群中所有尚未启动Cluster服务的节点上，启动该服务。

## 语法

```
Start-Cluster [[-Name] <String>] [-IgnorePersistentState] [-Wait <Int32>] [<CommonParameters>]
```

## 描述

`Start-Cluster` cmdlet 会在集群中所有尚未启动 Cluster 服务的节点上启动该服务。只有当某个节点上运行着 Cluster 服务时，该节点才能作为集群的一部分正常工作。

注意：如果服务器计算机上没有启用凭据安全服务提供程序（CredSSP）进行身份验证，那么该cmdlet无法远程运行。

## 示例

### 示例 1

```powershell
Start-Cluster
```

这个示例会在本地集群中启动所有集群节点。

### 示例 2

```powershell
Start-Cluster -Name node2
```

这个示例会启动该集群中所有节点，而节点`node2`属于该集群。如果需要停止所有集群节点，则必须提供相应的节点名称；如果集群已经在运行中，且集群名称资源处于可用状态，那么可以直接使用集群名称来代替节点名称。

## 参数

### -IgnorePersistentState

启动集群中的节点，但不会将这些节点上的资源设置为在线状态。请注意，这种行为会一直持续到集群重新启动为止，或者直到将集群属性 **IgnorePersistentStateOnStartup** 设置为 0 为止。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: ips

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name

指定要启动的集群的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Cluster

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Wait

指定等待该cmdlet完成所需的时间（以秒为单位）。如果未指定此参数，那么该cmdlet将一直等待直到达到法定人数（quorum）才会返回结果。如果指定值为`0`，则该cmdlet会尝试在所有节点上启动Cluster服务，然后立即返回而无需等待。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### MicrosoftFailoverClusters.PowerShell Cluster

## 备注

## 相关链接

[Get-Cluster](./Get-Cluster.md)

[Get-ClusterNode](./Get-ClusterNode.md)

[新集群](./New-Cluster.md)

[Remove-Cluster](./Remove-Cluster.md)

[停止集群操作](./Stop-Cluster.md)

[测试集群](./Test-Cluster.md)
