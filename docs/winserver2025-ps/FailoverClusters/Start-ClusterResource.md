---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/23/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/start-clusterresource?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-ClusterResource
---

# 启动集群资源

## 摘要
在故障转移集群中，将某个资源在线化（即使其能够正常运行）。

## 语法

```
Start-ClusterResource [[-Name] <String>] [-IgnoreLocked] [-ChooseBestNode] [-Wait <Int32>]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Start-ClusterResource` cmdlet 用于在故障转移集群中启动某个资源。在该资源被启用之前，它所依赖的所有其他资源也会被依次启用。

## 示例

### 示例 1

```powershell
Start-ClusterResource -Name "IP Address 172.24.11.0"
```

这个示例用于将名为“IP Address 172.24.11.0”的资源在线启用到本地集群中。在将该资源上线之前，此cmdlet会先启动所有依赖于该资源的其它资源。

### 示例 2

```powershell
Start-ClusterResource -Name "IP Address 172.24.11.0" -Wait 0
```

这个示例用于将名为“IP地址 172.24.11.0”的资源在本地集群上启用（即使其能够被访问）。在启用该资源之前，此 cmdlet 会先启动所有依赖于该资源的其余资源。一旦操作开始，Windows PowerShell 提示符就会立即返回正常显示状态。

## 参数

### -ChooseBestNode

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

指定在运行该 cmdlet 时忽略已锁定的组。

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

指定要在线化的集群资源。

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

指定要在线启用的集群资源的名称。这也可以是一个集群共享卷（Cluster Shared Volume，简称 CSV）的名称。

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

指定等待该cmdlet完成所需的时间（以秒为单位）。如果未指定**Wait**参数，那么cmdlet会一直等待直到操作完成；如果指定了 `-Wait 0`，则命令会被立即执行，而cmdlet会在不等待的情况下立即返回结果。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FAILoverClusters.PowerShell_clusterResource

### MicrosoftFailoverClusters.PowerShellClusterSharedVolume

## 输出

### Microsoft FAILoverClusters.PowerShell_clusterResource

### MicrosoftFailoverClusters.PowerShellClusterSharedVolume

## 备注

## 相关链接

[Add-ClusterResource](./Add-ClusterResource.md)

[Get-ClusterResource](./Get-ClusterResource.md)

[Move-ClusterResource](./Move-ClusterResource.md)

[Remove-ClusterResource](./Remove-ClusterResource.md)

[ Resume-ClusterResource](./Resume-ClusterResource.md)

[Stop-ClusterResource](./Stop-ClusterResource.md)

[暂停集群资源](./Suspend-ClusterResource.md)
