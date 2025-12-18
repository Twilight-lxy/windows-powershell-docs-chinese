---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusternetwork?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterNetwork
---

# Get-ClusterNetwork

## 摘要
获取有关故障转移集群中一个或多个网络的信息。

## 语法

```
Get-ClusterNetwork [[-Name] <StringCollection>] [-InputObject <PSObject>] [-Cluster <String>]
 [<CommonParameters>]
```

## 描述

`Get-ClusterNetwork` cmdlet 可以获取关于故障转移集群中一个或多个网络的信息。故障转移集群要求节点之间以及客户端与节点之间存在网络连接。

## 示例

### 示例 1

```powershell
Get-ClusterNetwork
```

这个示例用于获取有关本地集群所使用的网络的信息。

### 示例 2

```powershell
(Get-ClusterNetwork -Name "Cluster Network 1").Name = "Cluster Network 3"
```

这个例子将“Cluster Network 1”重命名为“Cluster Network 3”。

## 参数

### -Cluster

指定要运行此cmdlet的集群名称。如果该参数的输入为`.`或被省略，则cmdlet将在本地集群上运行。

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

指定用于遍历集群网络的集群。

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

指定要获取的集群网络的名称。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters PowerShell Cluster

## 输出

### MicrosoftFailoverClusters.PowerShell-clusterNetwork

## 备注

## 相关链接

[Get-ClusterNetworkInterface](./Get-ClusterNetworkInterface.md)
