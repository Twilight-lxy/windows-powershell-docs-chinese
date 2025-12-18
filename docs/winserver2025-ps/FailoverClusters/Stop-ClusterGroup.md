---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/23/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/stop-clustergroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-ClusterGroup
---

# 停止集群组（Stop-ClusterGroup）

## 摘要
在故障转移集群中，停止一个或多个群集角色（clustered roles）的运行。

## 语法

```
Stop-ClusterGroup [[-Name] <String>] [-IgnoreLocked] [-Wait <Int32>] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Stop-ClusterGroup` cmdlet 用于停止故障转移集群中的一个或多个群集角色（也称为资源组）。

如果需要对集群角色进行维护，可以使用此cmdlet以有序的方式停止该集群角色。

## 示例

#### 示例 1：在本地集群中停止一个集群角色（clustered role）

```powershell
Stop-ClusterGroup FileServer1
```

这个示例会停止名为 `FileServer1` 的集群角色或资源组在本地集群上的运行。

## 参数

### -Cluster

指定用于运行此 cmdlet 的集群名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 将在本地集群上运行。

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

指定在运行此cmdlet时忽略已锁定的组。

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

指定要停止运行的集群角色。

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

指定要停止运行的集群角色的名称。

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

指定等待该 cmdlet 完成的时间（以秒为单位）。如果未指定 **Wait** 参数，那么 cmdlet 会一直等待直到完成。如果指定了 `-Wait 0`，则调用会被立即启动，且 cmdlet 会在不等待的情况下立即返回结果。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell-clusterGroup

## 输出

### MicrosoftFailoverClusters.PowerShell-clusterGroup

## 备注

## 相关链接

[添加集群组](./Add-ClusterGroup.md)

[Get-ClusterGroup](./Get-ClusterGroup.md)

[Move-ClusterGroup](./Move-ClusterGroup.md)

[Remove-ClusterGroup](./Remove-ClusterGroup.md)

[开始创建集群组](./Start-ClusterGroup.md)
