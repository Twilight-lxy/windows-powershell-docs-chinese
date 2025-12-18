---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clustercheckpoint?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterCheckpoint
---

# 添加集群检查点

## 摘要
为某个资源添加一个加密密钥检查点或注册表检查点。

## 语法

```
Add-ClusterCheckpoint [[-ResourceName] <String>] [-CryptoCheckpointName <String>]
 [-CryptoCheckpointType <String>] [-CryptoCheckpointKey <String>] [-RegistryCheckpoint <String>]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Add-ClusterCheckpoint` cmdlet 用于为某个资源添加加密密钥检查点或注册表检查点。

检查点（Checkpoints）有助于为那些将配置信息存储在本地（而非或除了存储在集群配置数据库中之外）的应用程序提供故障转移支持。应用程序可以通过两种方式在本地存储信息：一种是将配置信息存储在本地服务器的注册表中；另一种是使用本地服务器上的加密密钥来存储配置信息。

## 示例

### 示例 1：添加注册表检查点

```powershell
Add-ClusterCheckpoint -ResourceName "Cluster Name" -RegistryCheckpoint "software\clusname"
```

这个示例为名为 “cluster name” 的资源添加了一个注册表检查点（registry checkpoint），该检查点的名称为 “software\clusname”。

### 示例 2：添加加密检查点

```powershell
$parameters = @{
    CryptoCheckpointName = 'Microsoft Base Cryptographic Provider v1.0'
    CryptoCheckpointType = '1'
    CryptoCheckpointKey = 'Crypto'
}
Get-ClusterResource -Name "Cluster Name" | Add-ClusterCheckpoint @parameters
```

这个示例为名为“Cluster Name”的资源添加了一个加密检查点。该示例使用了“Splatting”技术，将参数值从 `$Parameters` 变量传递给命令。有关 [Splatting] 的更多信息，请参阅 [ /powershell/module/microsoft.powershell.core/about/about_splatting ]。

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

### -CryptoCheckpointKey

指定要添加的加密密钥检查点的键值对。

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

### -CryptoCheckpointName

指定要添加的加密密钥检查点的名称。

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

### -CryptoCheckpointType

指定要添加的加密密钥检查点的类型。可选选项取决于所使用的加密提供者。

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

指定用于运行该cmdlet的集群，或者应为此添加检查点的集群资源。

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

指定要添加的注册表检查点的名称。

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

### -ResourceName

指定应为其添加检查点的资源。

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

### MicrosoftFailoverClusters.PowerShell-cluster

### MicrosoftFailoverClusters.PowerShellClusterResource

## 输出

### System.Object

## 备注

## 相关链接

[Get-ClusterCheckpoint](./Get-ClusterCheckpoint.md)

[Get-ClusterResource](./Get-ClusterResource.md)

[Remove-ClusterCheckpoint](./Remove-ClusterCheckpoint.md)
