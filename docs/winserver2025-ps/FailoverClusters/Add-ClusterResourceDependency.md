---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clusterresourcedependency?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterResourceDependency
---

# 添加集群资源依赖关系

## 摘要
在故障转移集群中，将一个资源添加到另一个特定资源所依赖的资源列表中，使用“AND”作为连接符。

## 语法

```
Add-ClusterResourceDependency [[-Resource] <String>] [[-Provider] <String>]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Add-ClusterResourceDependency` cmdlet 用于将某个资源添加到故障转移集群中其他资源的依赖关系列表中，连接符使用的是 `AND`。现有的依赖关系仍会保留在列表中。如果您指定了 `InputObject` 参数，则 `Resource` 参数将被忽略。

依赖资源会在其所依赖的资源上线之后才上线；而在其依赖的资源下线之前，该依赖资源会首先被下线。

## 示例

### 示例 1

```powershell
Add-ClusterResourceDependency -Resource "FileServer-(cluster1FS12)" -Provider "Cluster Disk 4"
```

这个示例将名为“Cluster Disk 4”的资源添加到依赖名为“FileServer-(cluster1FS12)”的资源的资源列表中。

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

### -InputObject

指定要为其添加依赖关系的集群资源。

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

### -Provider

指定要作为依赖项添加的集群资源。

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

### -Resource

指定要为其添加依赖关系的集群资源的名称。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

```powershell
### MicrosoftFailoverClusters.PowerShell_clusterResource
```

## 输出

```powershell
### MicrosoftFailoverClusters.PowerShell_clusterResource
```

## 备注

## 相关链接

[Get-ClusterResourceDependency](./Get-ClusterResourceDependency.md)

[Get-ClusterResourceDependencyReport](./Get-ClusterResourceDependencyReport.md)

[Remove-ClusterResourceDependency](./Remove-ClusterResourceDependency.md)

[Set-ClusterResourceDependency](./Set-ClusterResourceDependency.md)
