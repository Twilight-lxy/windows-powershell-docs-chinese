---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clusterresource?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterResource
---

# 添加集群资源

## 摘要
将资源添加到故障转移集群中的集群角色或资源组中。

## 语法

```
Add-ClusterResource [-Name] <String> [[-Group] <String>] [-ResourceType] <String>
 [-SeparateMonitor] [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Add-ClusterResource` cmdlet 可将资源添加到故障转移集群中的群集角色或资源组中。在添加资源之前，需要先获取资源的类型以及要将其添加到的组的名称。

## 示例

### 示例 1

```powershell
Add-ClusterResource -Name resource1 -ResourceType "IP Address" -Group ClusterSrv1
```

这个示例在本地集群上创建了一个名为 `resource1` 的新 IP 地址资源。该 cmdlet 将此资源配置为名为 `ClusterSrv1` 的集群角色或资源组的一部分。

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

### -Group

指定新资源将被添加到的集群角色的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定新资源将被添加到的集群角色。

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

指定要创建的集群资源的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourceType

为新集群资源指定集群资源类型的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ResType, Type

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SeparateMonitor

指定新的资源应在单独的资源监控器中运行。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell ClusterGroup

## 输出

### MicrosoftFailoverClusters.PowerShell-clusterResource

## 备注

## 相关链接

[Get-ClusterResource](./Get-ClusterResource.md)

[Move-ClusterResource](./Move-ClusterResource.md)

[Remove-ClusterResource](./Remove-ClusterResource.md)

[Resume-ClusterResource](./Resume-ClusterResource.md)

[开始集群资源设置](./Start-ClusterResource.md)

[Stop-ClusterResource](./Stop-ClusterResource.md)

[暂停集群资源](./Suspend-ClusterResource.md)
