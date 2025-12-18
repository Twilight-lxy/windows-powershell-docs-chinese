---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/23/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/update-clusternetworknameresource?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-ClusterNetworkNameResource
---

# 更新集群网络名称资源

## 摘要
将现有的网络名称资源注册到DNS服务器上，同时不会中断集群的正常运行（即保持集群的可用性）。

## 语法

```
Update-ClusterNetworkNameResource [[-Name] <StringCollection>] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Update-ClusterNetworkNameResource` cmdlet 可以将现有的网络名称资源注册到 DNS 服务器上，而不会中断集群的正常运行（即不会影响集群的可用性）。

## 示例

#### 示例 1：使用 DNS 服务器注册名称资源

```powershell
Get-ClusterResource -Name "Cluster Name" | Update-ClusterNetworkNameResource
```

这个示例将本地集群的网络名称资源注册到DNS服务器上。

## 参数

### -Cluster

指定要运行此cmdlet的集群名称。如果该参数的输入为`.`或被省略，则cmdlet将在本地集群上运行。

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

指定要注册到DNS服务器的网络名称资源。

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

指定要注册到 DNS 服务器上的网络名称。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell_clusterResource

## 输出

### MicrosoftFailoverClusters.PowerShell_clusterResource

## 备注

## 相关链接

[Get-ClusterResource](./Get-ClusterResource.md)

[更新 ClusterIP 资源](./Update-ClusterIPResource.md)
