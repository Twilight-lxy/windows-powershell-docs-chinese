---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/23/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/suspend-clusterresource?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Suspend-ClusterResource
---

# 暂停集群资源

## 摘要
为某个磁盘资源或CSV文件启用维护模式，这样你就可以运行磁盘维护工具而不会触发故障转移（failover）。

## 语法

```
Suspend-ClusterResource [[-Name] <String>] [-VolumeName <String>] [-RedirectedAccess] [-Force]
 [-InputObject <PSObject>] [-Cluster <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Suspend-ClusterResource` cmdlet 用于将磁盘资源或集群共享卷（Cluster Shared Volume，简称 CSV）设置为维护模式，这样就可以运行磁盘维护工具而不会触发故障转移。

此cmdlet仅适用于磁盘和CSV文件。对于集群共享卷（Cluster Shared Volumes），启用维护模式会使得相关资源处于离线状态，从而中断客户端对这些资源的访问；而对于其他类型的磁盘（例如逻辑单元号LUNs）在集群存储环境中的情况，启用维护模式后相关资源仍保持在线状态。

## 示例

#### 示例 1：为 CSV 文件启用维护模式

```powershell
Suspend-ClusterResource -Name "Cluster Disk 2"
```

这个示例会启用名为“Cluster Disk 2”的CSV文件的维护功能，这样你就可以运行磁盘维护工具而不会触发故障转移。

### 示例 2：为多个卷启用维护模式

```powershell
Get-ClusterSharedVolume -Name "Cluster Disk 5" | Suspend-ClusterResource
```

这个示例会为名为“Cluster Disk 5”的CSV文件中的所有卷启用维护功能。

## 参数

### -Cluster

指定用于运行此 cmdlet 的集群的名称。如果该参数的输入值为`.` 或省略，则 cmdlet 将在本地集群上运行。

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

### -Force

强制命令运行，而无需请求用户确认。

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

指定要挂起的集群资源（磁盘或 CSV 文件）。

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

指定要挂起的集群资源（磁盘或CSV文件）的名称。

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

### -RedirectedAccess

这会导致对存储设备的CSV访问通过网络重定向到另一个集群节点上。此参数仅适用于CSV文件。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: FileSystemRedirectedAccess

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VolumeName

指定要挂起的卷的名称。此参数仅适用于CSV（Cloud Storage Volume）对象。如果未指定该参数，操作将针对CSV中的所有卷执行。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters PowerShell ClusterResource

### MicrosoftFailoverClusters.PowerShell-clusterSharedVolume

## 输出

### Microsoft FailoverClusters PowerShell ClusterResource

### MicrosoftFailoverClusters.PowerShell-clusterSharedVolume

## 备注

## 相关链接

[添加集群资源](./Add-ClusterResource.md)

[Get-ClusterResource](./Get-ClusterResource.md)

[Move-ClusterResource](./Move-ClusterResource.md)

[Remove-ClusterResource](./Remove-ClusterResource.md)

[Resume-ClusterResource](./Resume-ClusterResource.md)

[开始创建集群资源](./Start-ClusterResource.md)

[Stop-ClusterResource](./Stop-ClusterResource.md)
