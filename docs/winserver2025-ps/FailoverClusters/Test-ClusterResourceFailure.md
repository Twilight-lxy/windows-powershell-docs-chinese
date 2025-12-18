---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/23/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/test-clusterresourcefailure?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-ClusterResourceFailure
---

# 测试集群资源故障

## 摘要
模拟集群资源发生故障的情况。

## 语法

```
Test-ClusterResourceFailure [[-Name] <String>] [-InputObject <PSObject>] [-Cluster <String>]
 [<CommonParameters>]
```

## 描述

`Test-ClusterResourceFailure` cmdlet 用于模拟集群资源的故障。

根据故障转移和故障恢复策略，当运行此cmdlet时，Cluster服务会移动集群角色或资源组，并尝试将集群资源重新上线。可以使用此cmdlet来模拟资源发生故障时Cluster服务将采取的操作。

## 示例

### 示例 1：模拟故障

```powershell
Test-ClusterResourceFailure -Name "Cluster Disk 4"
```

这个示例模拟了名为“Cluster Disk 4”的集群资源发生故障的情况。

## 参数

### -Cluster

指定要运行此 cmdlet 的集群的名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 将在本地集群上运行。

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

指定要模拟故障的集群资源。

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

指定要模拟故障的集群资源的名称。

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

### CommonParameters

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Move-ClusterGroup](./Move-ClusterGroup.md)

[开始创建集群资源](./Start-ClusterResource.md)
