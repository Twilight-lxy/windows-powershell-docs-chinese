---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/move-clusterresource?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Move-ClusterResource
---

# 移动集群资源

## 摘要
将一个集群资源从一个集群角色移动到另一个集群角色，该操作发生在故障转移集群内部。

## 语法

```
Move-ClusterResource [[-Name] <String>] [[-Group] <String>] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Move-ClusterResource` cmdlet 可以将集群资源从一个集群角色移动到另一个集群角色，这一操作是在故障转移集群中进行的。当集群资源被移动到一个不同的集群角色后，该资源将会与该新的集群角色一起执行故障转移（即在该新角色下继续运行）。

## 示例

### 示例 1

```powershell
Move-ClusterResource -Name resource1 -Group group2
```

此命令将名为 `resource1` 的集群资源移动到本地集群中名为 `group2` 的资源组中。

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

指定要将资源移动到的集群组的名称。

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

指定要移动的集群资源。

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

指定要移动的集群资源的名称。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell ClusterResource

## 输出

### MicrosoftFailoverClusters.PowerShell ClusterResource

## 备注

## 相关链接

[Add-ClusterResource](./Add-ClusterResource.md)

[Get-ClusterResource](./Get-ClusterResource.md)

[Remove-ClusterResource](./Remove-ClusterResource.md)

[Resume-ClusterResource](./Resume-ClusterResource.md)

[启动集群资源](./Start-ClusterResource.md)

[Stop-ClusterResource](./Stop-ClusterResource.md)

[暂停集群资源](./Suspend-ClusterResource.md)
