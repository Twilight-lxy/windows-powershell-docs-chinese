---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clustergroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterGroup
---

# Get-ClusterGroup

## 摘要
获取有关故障转移集群中一个或多个聚类角色（资源组）的信息。

## 语法

```
Get-ClusterGroup [[-Name] <StringCollection>] [-VMId <Guid>] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Get-ClusterGroup` cmdlet 可以获取有关故障转移集群中的一个或多个集群角色（资源组）的信息。

资源组是故障转移的基本单位。在发生故障转移时，资源组中的所有资源会一起被迁移（或重新分配）到其他位置。

## 示例

### 示例 1

```powershell
Get-ClusterGroup
```

这个示例列出了本地集群中每个集群化角色（或资源组）的状态和所属节点信息。

### 示例 2

```powershell
Get-ClusterGroup -Name "Cluster Group" | Get-ClusterResource
```

这个示例列出了本地集群中“Cluster Group”中的资源。

### 示例 3

```powershell
Get-ClusterNode -Name node1 | Get-ClusterGroup
```

这个示例列出了当前由 `node1` 拥有的、位于本地集群中的服务、应用程序或资源组。

### 示例 4

```powershell
Get-ClusterGroup -Name FileServer1 | Format-List -Property *
```

这个示例以列表的形式展示了名为`FileServer1`的集群文件服务器或资源组的属性。

## 参数

### -Cluster

指定用于运行此cmdlet的集群名称。如果该参数的值为`.`或被省略，则cmdlet将在本地集群上运行。

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

指定用于遍历集群角色的集群或集群节点。

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

指定要获取的集群角色的名称。

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

### -VMId

指定虚拟机标识符（ID）。

```yaml
Type: Guid
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters PowerShellCluster

### Microsoft FailoverClusters.PowerShell ClusterNode

## 输出

### MicrosoftFailoverClusters.PowerShell_CLUSTERGroup

## 备注

## 相关链接

[格式化列表](https://go.microsoft.com/fwlink/?LinkID=113302)

[Add-ClusterGroup](./Add-ClusterGroup.md)

[Move-ClusterGroup](./Move-ClusterGroup.md)

[Remove-ClusterGroup](./Remove-ClusterGroup.md)

[开始使用 ClusterGroup](./Start-ClusterGroup.md)

[Stop-ClusterGroup](./Stop-ClusterGroup.md)
