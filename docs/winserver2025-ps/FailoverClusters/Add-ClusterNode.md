---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clusternode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterNode
---

# 添加集群节点

## 摘要
向故障转移集群中添加一个节点（服务器）。

## 语法

```
Add-ClusterNode [[-Name] <StringCollection>] [-NoStorage] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Add-ClusterNode` cmdlet 可用于将一个节点（或服务器）添加到故障转移集群中。在添加新节点之前，应先对现有节点以及拟添加的新节点一起进行验证测试。

在添加新节点之前，你应该对现有的节点以及提议添加的新节点一起运行验证测试。通过这些验证测试，你可以确认要添加的服务器已正确连接到网络和存储系统，并且其安装了相同的软件更新。

> [注意] > 如果服务器计算机上没有启用凭据安全服务提供程序（CredSSP）的认证功能，此cmdlet无法远程运行。

## 示例

### 示例 1

```powershell
Add-ClusterNode -Name node4
```

这个示例向本地集群添加了一个名为 `node4` 的节点。

### 示例 2

```powershell
Get-Cluster -Name cluster1 | Add-ClusterNode -Name node3
```

这个示例将名为 `node3` 的节点添加到名为 `cluster1` 的集群中。

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

### -InputObject

指定要向其中添加新集群节点的集群。

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

指定要添加的集群节点的名称。

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

### -NoStorage

确保在将节点加入集群的过程中，该节点上的共享存储不会被添加到集群中。可以通过将 `Get-ClusterAvailableDisk` cmdlet 返回的 `ClusterDiskInfo` 对象传递给 `Add-ClusterDisk` cmdlet 来添加共享存储。

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

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell Cluster

## 输出

### MicrosoftFailoverClusters.PowerShellClusterNode

## 备注

## 相关链接

[添加集群磁盘](./Add-ClusterDisk.md)

[Get-ClusterAvailableDisk](./Get-ClusterAvailableDisk.md)

[Get-ClusterNode](./Get-ClusterNode.md)

[新集群](./New-Cluster.md)

[Remove-ClusterNode](./Remove-ClusterNode.md)

[Resume-ClusterNode](./Resume-ClusterNode.md)

[启动集群节点](./Start-ClusterNode.md)

[Stop-ClusterNode](./Stop-ClusterNode.md)

[暂停集群节点](./Suspend-ClusterNode.md)

[测试集群](./Test-Cluster.md)
