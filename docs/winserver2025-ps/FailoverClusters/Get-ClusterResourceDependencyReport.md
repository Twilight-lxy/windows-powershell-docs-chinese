---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusterresourcedependencyreport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterResourceDependencyReport
---

# 获取集群资源依赖关系报告

## 摘要
生成一份报告，列出故障转移集群中各资源之间的依赖关系。

## 语法

```
Get-ClusterResourceDependencyReport [-Resource <String>] [-Group <String>] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Get-ClusterResourceDependencyReport` cmdlet 生成一份报告，该报告列出了故障转移集群中各资源之间的依赖关系。

该报告的文件扩展名为 MHT。为了便于存储和查找，你可以将此 cmdlet 与 [复制项目](https://go.microsoft.com/fwlink/?LinkID=113292) cmdlet 结合使用，并指定一个目标文件夹来保存报告。

## 示例

### 示例 1

```powershell
Get-ClusterResourceDependencyReport -Group cluster1FS12
```

这个示例为本地集群中的集群文件服务器（或资源组）创建了一个依赖关系报告文件，该文件服务器的名称为`cluster1FS12`。

### 示例 2

```powershell
Get-ClusterResourceDependencyReport -Group cluster1FS12 | Copy-Item -Destination C:\users\user1
```

这个示例为本地集群上的集群文件服务器（或资源组）`cluster1FS12`生成了一个依赖关系报告文件。该报告文件被复制到了`C:\users\user1`目录中。

### 示例 3

```powershell
Get-ClusterGroup | Get-ClusterResourceDependencyReport | Copy-Item -Destination \\fileserver\share
```

这个示例会为本地集群中的每个集群角色或资源组生成一个依赖关系报告文件，并将所有报告复制到`\\fileserver\share`目录中。

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

### -Group

指定要为其生成依赖关系报告的集群组的名称。

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

指定要创建依赖关系报告的集群组或集群资源。

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

指定要生成依赖关系报告的集群资源的名称。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell-clusterGroup

### Microsoft FailoverClusters PowerShell ClusterResource

## 输出

### System.IO.FileInfo

## 备注

## 相关链接

[复制项目](https://go.microsoft.com/fwlink/?LinkID=113292)

[Add-ClusterResourceDependency](./Add-ClusterResourceDependency.md)

[Remove-ClusterResourceDependency](./Remove-ClusterResourceDependency.md)

[Set-ClusterResourceDependency](./Set-ClusterResourceDependency.md)
