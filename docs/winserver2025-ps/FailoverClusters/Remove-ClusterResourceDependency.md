---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/remove-clusterresourcedependency?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ClusterResourceDependency
---

# 移除集群资源依赖关系

## 摘要
在故障转移集群中，删除集群角色内两个资源之间的依赖关系。

## 语法

```
Remove-ClusterResourceDependency [[-Resource] <String>] [[-Provider] <String>]
 [-InputObject <PSObject>] [-Cluster <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-ClusterResourceDependency` cmdlet 用于删除故障转移集群中某个集群角色内两个资源之间的依赖关系。

一个依赖资源会在其所依赖的资源上线之后再上线；同样，一个依赖资源也会在其所依赖的资源下线之前先下线。如果集群资源之间没有配置任何依赖关系，那么它们上线或下线的顺序可能会有所不同。

## 示例

### 示例 1

```powershell
$parameters = @{
    Resource = 'cluster1FS'
    Provider = 'IP Address 2001:4898:9:2:: (3)'
}
Remove-ClusterResourceDependency @parameters
```

这个示例消除了集群资源 `cluster1FS` 与名为 `IP Address 2001:4898:9:2:: (3)` 的资源之间的依赖关系。

### 示例 2

```powershell
$parameters = @{
    Provider = 'IP Address 2001:4898:9:2:: (3)'
}
Get-ClusterResource -Name cluster1FS | Remove-ClusterResourceDependency @parameters
```

这个示例消除了名为 `cluster1FS` 的集群资源与名为 `IP Address 2001:4898:9:2:: (3)` 的资源之间的依赖关系。该示例使用了“Splatting”技术，将 `$Parameters` 变量中的参数值传递给相应的命令。有关 [Splatting](/powershell/module/microsoft.powershell.core/about/about_splatting) 的更多信息，请参阅相关文档。

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

### -Confirm

在运行cmdlet之前，会提示您进行确认。

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

### -InputObject

指定要从中移除依赖关系的集群资源。

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

指定要从中删除依赖关系的集群资源。

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

指定要从中移除依赖关系的集群资源的名称。

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

展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被运行。

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

此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters PowerShell ClusterResource

## 输出

### Microsoft FailoverClusters PowerShell ClusterResource

## 备注

## 相关链接

[Add-ClusterResourceDependency](./Add-ClusterResourceDependency.md)

[Get-ClusterResourceDependency](./Get-ClusterResourceDependency.md)

[Set-ClusterResourceDependency](./Set-ClusterResourceDependency.md)
