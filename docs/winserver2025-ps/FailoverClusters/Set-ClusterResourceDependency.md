---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/set-clusterresourcedependency?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ClusterResourceDependency
---

# 设置集群资源依赖关系

## 摘要
指定某个资源在故障转移集群中依赖于哪些其他资源。

## 语法

```
Set-ClusterResourceDependency [[-Resource] <String>] [[-Dependency] <String>]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Set-ClusterResourceDependency` cmdlet 用于指定某个资源在故障转移集群中依赖的其他资源。您指定的依赖关系会覆盖现有的依赖关系。

该术语可以用于描述依赖关系的表达式中。例如，可以设置一种“或”（or）依赖关系，使得某个“网络名称资源”依赖于两个IP地址资源中的任意一个，而不是同时依赖于这两个资源。这种使用“或”依赖关系的做法在多站点集群部署中非常常见。

## 示例

### 示例 1

```powershell
Set-ClusterResourceDependency -Resource cluster1FS12 -Dependency "[IP Address 151.56.48.0]"
```

这个示例使得名为 `cluster1FS12` 的资源依赖于 `[IP 地址 151.56.48.0]`。

### 示例 2

```powershell
$parameters = @{
    Resource = 'cluster1FS12'
    Dependency = '[IP Address 151.56.48.0] or [New IP Address]'
}
Set-ClusterResourceDependency @parameters
```

这个示例使得名为 `cluster1FS12` 的资源依赖于 `[IP 地址 151.56.48.0]` 或 `[新 IP 地址]` 中的任何一个。

这个示例使用“拆分”（splatting）机制，将 `$Parameters` 变量中的参数值传递给命令。欲了解更多关于“拆分”的信息，请参阅 [Splatting](/powershell/module/microsoft.powershell.core/about/about_splatting)。

### 示例 3

```powershell
Set-ClusterResourceDependency -Resource cluster1FS12 -Dependency ""
```

这个示例清除了名为 `cluster1FS12` 的资源的依赖关系列表，使其不再依赖于任何其他资源。

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

### -Dependency

用于指定要为此资源设置的依赖关系表达式。其格式如下（以字符串形式表示）：`"[资源名称1] [和/或 [资源名称2] [...]]"`，其中 `资源名称1` 和 `资源名称2` 是需要配置的资源的名称。

资源名称应使用方括号括起来，例如 `[Cluster Disk 2]Cluster Disk 2`。要重置资源依赖关系，请在此参数中使用空字符串 `""`。

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

指定要设置依赖表达式的集群资源。

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

指定要设置依赖表达式的集群资源的名称。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters PowerShell ClusterResource

## 输出

### 无

## 备注

## 相关链接

[添加集群资源依赖关系](./Add-ClusterResourceDependency.md)

[Get-ClusterResourceDependency](./Get-ClusterResourceDependency.md)

[Get-ClusterResourceDependencyReport](./Get-ClusterResourceDependencyReport.md)

[Remove-ClusterResourceDependency](./Remove-ClusterResourceDependency.md)
