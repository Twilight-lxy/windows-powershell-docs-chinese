---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusterresourcetype?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterResourceType
---

# Get-ClusterResourceType

## 摘要
获取关于故障转移集群中一种或多种资源类型的信息。

## 语法

```
Get-ClusterResourceType [[-Name] <StringCollection>] [-InputObject <PSObject>] [-Cluster <String>]
 [<CommonParameters>]
```

## 描述

`Get-ClusterResourceType` cmdlet 可以获取关于故障转移集群中一种或多种资源类型的信息。例如，它可以提供动态链接库（DLL）的名称，该 DLL 用于让 Cluster 服务与特定资源类型进行通信。

## 示例

### 示例 1

```powershell
Get-ClusterResourceType
```

这个示例列出了可以在本地集群的配置中使用的所有资源类型。

### 示例 2

```powershell
Get-ClusterResourceType -Name "File Server" | Format-List -Property *
```

这个示例获取有关本地集群中“文件服务器”资源类型的信息，并以列表的形式显示这些信息。

## 参数

### -Cluster

指定用于运行此cmdlet的集群名称。如果该参数的输入为`.`或被省略，则cmdlet将在本地集群上运行。

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

指定用于枚举集群资源类型的集群。

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

指定要获取的集群资源类型的名称。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FAILoverClusters.PowerShell.Cluster

## 输出

### MicrosoftFailoverClusters.PowerShell_clusterResourceType

## 备注

## 相关链接

[Add-ClusterResourceType](./Add-ClusterResourceType.md)

[Remove-ClusterResourceType](./Remove-ClusterResourceType.md)
