---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusterresource?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterResource
---

# Get-ClusterResource

## 摘要
获取关于故障转移集群中一个或多个资源的信息。

## 语法

```
Get-ClusterResource [[-Name] <StringCollection>] [-VMId <Guid>] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Get-ClusterResource` cmdlet 可以获取关于故障转移集群中一个或多个资源的信息。

要为集群资源设置一个通用属性，可以使用此cmdlet获取该集群资源的对象，然后直接在该对象上设置相应的属性。若要获取或设置关于集群资源的更具体信息，请将该cmdlet与`Get-ClusterParameter`和`Set-ClusterParameter`结合使用。

## 示例

### 示例 1

```powershell
Get-ClusterResource
```

这个例子列出了本地集群上的所有集群资源。

### 示例 2

```powershell
Get-ClusterResource -Name "Cluster Disk 2" | Format-List -Property *
```

这个示例以列表的形式显示了本地集群中“Cluster Disk 2”的相关信息。

### 示例 3

```powershell
Get-ClusterResource -Name "Cluster Disk 2" | Get-ClusterParameter
```

这个示例展示了本地集群中“Cluster Disk 2”的详细参数信息。

### 示例 4

```powershell
Get-ClusterGroup -Name FileServer1 | Get-ClusterResource
```

这个示例列出了名为`FileServer1`的集群组中的集群资源，该集群组是一个位于本地集群上的集群化文件服务器。

### 示例 5

```powershell
Get-ClusterResource -Name "Cluster Disk 2" | ForEach-Object -Process {
    $_.RestartDelay = 600
}
```

这个示例将本地集群中“Cluster Disk 2”资源的公共属性“RestartDelay”设置为“600”。

### 示例 6

```powershell
Get-ClusterResource -Name "cluster pool 1" | Format-List -Property OwnerNode
```

这个示例展示了如何显示集群中共享磁盘的所有者信息。

### 示例 7

```powershell
Get-ClusterResource -Name *print-VM1 | Get-VM | Stop-VM -Verbose -Confirm:$false
```

这个示例列出了包含通配符 `*print-VM1` 的集群资源，并在无需用户确认的情况下停止了相应的虚拟机。为了详细了解操作过程，已启用了详细日志记录（verbose mode）。

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

### -InputObject

指定用于枚举集群资源的集群节点或集群组。

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

指定要获取的集群资源的名称。

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

### Microsoft FailoverClusters.PowerShellClusterResource

### Microsoft FailoverClusters.PowerShell ClusterNode

## 输出

### Microsoft FailoverClusters.PowerShellClusterResource

## 备注

## 相关链接

[ForEach-Object](https://go.microsoft.com/fwlink/?LinkID=113300)

[格式化列表](https://go.microsoft.com/fwlink/?LinkID=113302)

[Add-ClusterResource](./Add-ClusterResource.md)

[Move-ClusterResource](./Move-ClusterResource.md)

[Remove-ClusterResource](./Remove-ClusterResource.md)

[Resume-ClusterResource](./Resume-ClusterResource.md)

[开始创建集群资源](./Start-ClusterResource.md)

[Stop-ClusterResource](./Stop-ClusterResource.md)

[暂停集群资源](./Suspend-ClusterResource.md)
