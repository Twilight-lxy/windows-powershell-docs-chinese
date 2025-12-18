---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusterresourcedependency?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterResourceDependency
---

# Get-ClusterResourceDependency

## 摘要
获取有关故障转移集群中已配置的、用于连接集群资源之间依赖关系的信息。

## 语法

```
Get-ClusterResourceDependency [[-Resource] <StringCollection>] [-Guid] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Get-ClusterResourceDependency` cmdlet 可以获取关于故障转移集群中配置的资源依赖关系的信息。这些资源依赖关系决定了集群中资源上线或下线的顺序。

## 示例

#### 示例 1

```powershell
Get-ClusterResourceDependency -Resource cluster1FS12
```

这个示例展示了名为 `cluster1FS12` 的资源所依赖的其他组件（即其依赖关系）。

### 示例 2

```powershell
Get-ClusterGroup -Name cluster1FS12 | Get-ClusterResource | Get-ClusterResourceDependency
```

这个示例展示了名为`cluster1FS12`的集群文件服务器资源组中每个资源的依赖关系。有些资源没有依赖关系。

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

### -Guid

这会导致生成的依赖关系表达式中包含资源GUID而不是资源名称。

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

指定要获取依赖关系表达式的集群资源。

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

### -Resource

指定要获取依赖关系表达式的集群资源的名称。

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

### Microsoft_failoverClusters.PowerShellClusterResource

## 输出

### Microsoft FailoverClusters PowerShellClusterResourceDependency

## 备注

## 相关链接

[添加集群资源依赖关系](./Add-ClusterResourceDependency.md)

[Get-ClusterGroup](./Get-ClusterGroup.md)

[Get-ClusterResource](./Get-ClusterResource.md)

[Remove-ClusterResourceDependency](./Remove-ClusterResourceDependency.md)

[Set-ClusterResourceDependency](./Set-ClusterResourceDependency.md)
