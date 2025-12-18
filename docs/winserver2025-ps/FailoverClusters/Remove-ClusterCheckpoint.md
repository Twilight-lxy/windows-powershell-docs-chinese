---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 01/09/2023
online version: https://learn.microsoft.com/powershell/module/failoverclusters/remove-clustercheckpoint?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ClusterCheckpoint
---

# 删除集群检查点

## 摘要
删除某个资源的加密密钥检查点或注册表检查点。

## 语法

```
Remove-ClusterCheckpoint [[-ResourceName] <String>] [-Force] [-CheckpointName <String>]
 [-RegistryCheckpoint] [-CryptoCheckpoint] [-InputObject <PSObject>] [-Cluster <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-ClusterCheckpoint` cmdlet 用于删除资源的加密密钥检查点或注册表检查点。

检查点（Checkpoints）有助于为那些将配置信息存储在本地（而不是或除了存储在集群配置数据库中之外）的应用程序提供故障转移支持。应用程序可以通过两种方式在本地存储信息：一种是将配置信息存储在本地服务器的注册表中；另一种是使用本地服务器上的加密密钥来存储配置信息。

## 示例

### 示例 1

```powershell
$checkpoint = Get-ClusterCheckpoint -ResourceName "Cluster Name" -RegistryCheckpoint
$checkpoint | Remove-ClusterCheckpoint -Confirm:$false
```

这个示例会返回名为“Cluster Name”的资源的所有注册表检查点（即该资源在注册表中的状态变化记录），然后在没有用户确认的情况下删除这些检查点。

## 参数

### -CheckpointName

指定要删除的检查点的名称。

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

指定用于运行此 cmdlet 的集群名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 会在本地集群上运行。

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

### -CryptoCheckpoint

指定将删除加密密钥的检查点（即用于验证密钥完整性的数据）。

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

### -Force

该cmdlet在运行时不会提示用户进行确认。默认情况下，该cmdlet会在执行前询问用户的确认意见。

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

指定用于运行该 cmdlet 的集群，或用于删除检查点的集群资源。

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

指定将删除注册表检查点。

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

指定应从中删除检查点的资源。

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

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft_failoverClusters.PowerShell-cluster

### MicrosoftFailoverClusters.PowerShell-clusterResource

## 输出

### System.Object

## 备注

## 相关链接

[添加集群检查点](./Add-ClusterCheckpoint.md)

[Get-ClusterCheckpoint](./Get-ClusterCheckpoint.md)
