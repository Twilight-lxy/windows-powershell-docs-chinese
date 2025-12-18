---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clustergroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterGroup
---

# 添加 ClusterGroup

## 摘要
向故障转移集群配置中添加一个空的资源组，为后续向该组中添加集群化资源做准备。

## 语法

```
Add-ClusterGroup [-Name] <StringCollection> [[-GroupType] <GroupType>] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Add-ClusterGroup` cmdlet 用于向故障转移集群配置中添加一个空的资源组，为后续向该组中添加集群化资源做准备。资源组（或称为“集群角色”）是故障转移的基本单位；在发生故障转移时，资源组中的所有资源都会一同被迁移。

## 示例

### 示例 1：添加资源组

```powershell
Add-ClusterGroup -Name "Group1"
```

这个示例向故障转移集群中添加了一个名为“Group1”的空资源组。

## 参数

### -Cluster

指定要运行此 cmdlet 的集群的名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 会在本地集群上运行。

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

### -GroupType

指定要添加到故障转移集群配置中的组类型。

```yaml
Type: GroupType
Parameter Sets: (All)
Aliases:
Accepted values: Cluster, AvailableStorage, Temporary, ClusterSharedVolume, ClusterStoragePool, FileServer, DhcpServer, Dtc, Msmq, Wins, StandAloneDfs, GenericApplication, GenericService, GenericScript, IScsiNameService, VirtualMachine, TsSessionBroker, IScsiTarget, ScaleoutFileServer, VMReplicaBroker, TaskScheduler, Unknown

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定用于创建资源组的集群。

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

指定要添加的资源组的名称。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShellCluster

## 输出

### MicrosoftFailoverClusters.PowShell ClusterGroup

## 备注

## 相关链接

[Get-ClusterGroup](./Get-ClusterGroup.md)

[Move-ClusterGroup](./Move-ClusterGroup.md)

[ Remove-ClusterGroup](./Remove-ClusterGroup.md)

[开始创建集群组](./Start-ClusterGroup.md)

[停止集群组](./Stop-ClusterGroup.md)
