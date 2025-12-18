---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clustercheckpoint?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterCheckpoint
---

# 获取集群检查点（Get-ClusterCheckpoint）

## 摘要
检索资源的加密密钥检查点或注册表检查点。

## 语法

```
Get-ClusterCheckpoint [[-ResourceName] <StringCollection>] [-CheckpointName <String>]
 [-RegistryCheckpoint] [-CryptoCheckpoint] [-InputObject <PSObject>] [-Cluster <String>]
 [<CommonParameters>]
```

## 描述

`Get-ClusterCheckpoint` cmdlet 可以检索某个资源的加密密钥检查点或注册表检查点。

检查点（Checkpoints）有助于为那些将配置信息存储在本地（而非仅在集群配置数据库中存储或同时存储在两者中）的应用程序提供故障转移支持。应用程序可以通过两种方式在本地存储信息：一种是将配置信息存储在本地服务器的注册表中；另一种是使用本地服务器上的加密密钥来存储配置信息。

## 示例

### 示例 1

```powershell
Get-ClusterCheckpoint
```

这个示例会检索所有集群检查点（cluster checkpoints）。

### 示例 2

```powershell
Get-ClusterResource -ResourceName "Cluster Name" | Get-ClusterCheckpoint -CryptoCheckpoint
```

这个示例用于检索名为“Cluster Name”的资源的加密检查点信息。

## 参数

### -CheckpointName

指定要搜索的检查点的名称。支持使用通配符表达式。

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

### -CryptoCheckpoint

指定将检索加密检查点（cryptographic checkpoints）。

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

指定用于运行该 cmdlet 的集群，或用于检索检查点的集群资源。

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

### -RegistryCheckpoint

指定将检索注册表检查点信息。

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

### -ResourceName

指定要检索检查点的资源。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters.PowerShellCluster

### MicrosoftFailoverClusters.PowerShellClusterResource

## 输出

### System.Object

## 备注

## 相关链接

[添加集群检查点](./Add-ClusterCheckpoint.md)

[Remove-ClusterCheckpoint](./Remove-ClusterCheckpoint.md)
