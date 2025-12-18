---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/23/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/stop-clusterresource?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-ClusterResource
---

# 停止集群资源

## 摘要
在故障转移集群中，将某个资源设置为离线状态。

## 语法

```
Stop-ClusterResource [[-Name] <String>] [-IgnoreLocked] [-Wait <Int32>] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Stop-ClusterResource` cmdlet 用于将故障转移集群中的某个资源置于离线状态。在将该资源置为离线状态之前，所有依赖于该资源的资源也会被同时置于离线状态。

## 示例

### 示例 1：将资源置于离线状态

```powershell
Stop-ClusterResource "IP Address 10.24.11.0"
```

这个示例会将名为“IP Address 10.24.11.0”的资源从本地集群中下线。在将该资源下线之前，系统会先将其所有依赖的资源也一并下线。

## 参数

### -Cluster

指定用于运行此cmdlet的集群名称。如果该参数的输入值为`.`或被省略，则cmdlet将在本地集群上运行。

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

### -IgnoreLocked

指定在运行该cmdlet时忽略被锁定的组。

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

指定要离线的集群资源。

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

指定要下线的集群资源的名称。这也可以是一个集群共享卷（Cluster Shared Volume）的名称。

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

### -Wait

指定命令块需要等待的时间（以秒为单位）。如果未指定 `Wait` 参数，那么命令块会一直等待直到操作完成。如果指定了 `-Wait 0`，则命令会立即被执行，而不会等待任何结果，之后命令块会立即返回。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell-clusterResource

### MicrosoftFailoverClusters.PowerShellClusterSharedVolume

## 输出

### MicrosoftFailoverClusters.PowerShell-clusterResource

### MicrosoftFailoverClusters.PowerShellClusterSharedVolume

## 备注

## 相关链接

[添加集群资源](./Add-ClusterResource.md)

[Get-ClusterResource](./Get-ClusterResource.md)

[Move-ClusterResource](./Move-ClusterResource.md)

[Remove-ClusterResource](./Remove-ClusterResource.md)

[ Resume-ClusterResource ](./Resume-ClusterResource.md)

[开始创建集群资源](./Start-ClusterResource.md)

[暂停集群资源](./Suspend-ClusterResource.md)
