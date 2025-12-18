---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusternetworkinterface?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterNetworkInterface
---

# Get-ClusterNetworkInterface

## 摘要
获取关于故障转移集群中一个或多个网络适配器的信息。

## 语法

```
Get-ClusterNetworkInterface [[-Name] <StringCollection>] [-Node <StringCollection>]
 [-Network <StringCollection>] [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Get-ClusterNetworkInterface` cmdlet 可以获取故障转移集群中一个或多个网络适配器的信息。故障转移集群要求节点之间以及客户端与节点之间能够保持网络连接。

## 示例

### 示例 1

```powershell
Get-ClusterNetworkInterface
```

这个示例显示了本地集群使用的物理网络适配器的相关信息。

### 示例 2

```powershell
Get-ClusterNode -Name node1 | Get-ClusterNetworkInterface
```

这个示例展示了本地集群中 `node1` 使用的物理网络适配器的相关信息。该 cmdlet 等同于 `Get-ClusterNetworkInterface -Node node1`。

## 参数

### -Cluster

指定用于运行此 cmdlet 的集群的名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 将在本地集群上运行。

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

指定用于遍历集群网络接口的集群。

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

指定要获取的集群网络接口的名称。

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

### -Network

指定要枚举网络接口的集群网络的名称。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Node

指定要遍历网络接口的集群节点的名称。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell_cluster

### MicrosoftFailoverClusters.PowerShell_clusterNetwork

## 输出

### Microsoft FailoverClusters PowerShellClusterNetworkInterface

## 备注

## 相关链接

[Get-ClusterNetwork](./Get-ClusterNetwork.md)
