---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/clear-clusternode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-ClusterNode
---

# 清除集群节点

## 摘要
从被从故障转移集群中移除的节点清除集群配置信息。

## 语法

```
Clear-ClusterNode [[-Name] <StringCollection>] [-Force] [-Wait <Int32>] [-CleanupDisks]
 [-InputObject <PSObject>] [-Cluster <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Clear-ClusterNode` cmdlet 用于清除从故障转移集群中被移除的节点上的集群配置信息。该 cmdlet 可确保被移除的节点上的所有故障转移集群配置都已完全删除。

> [注意] > 该cmdlet无法在没有服务器计算机上的凭据安全服务提供者（CredSSP）身份验证的情况下远程运行。

## 示例

### 示例 1

```powershell
Clear-ClusterNode -Name node4 -Force
```

这个示例会从名为 `node4` 的节点中删除集群配置信息，而无需请求用户确认。

### 示例 2

```powershell
Clear-ClusterNode
```

这个示例在提示用户确认后，会从本地节点中删除集群配置信息。

## 参数

### -CleanupDisks

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

### -Confirm

在运行该cmdlet之前，会提示您进行确认。

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

### -Force

该cmdlet会在不提示用户确认的情况下直接执行操作。默认情况下，该cmdlet在执行前会要求用户进行确认。

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

指定用于清除集群配置信息的集群节点。

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

指定要清除集群配置的集群节点的名称。

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

### -Wait

指定等待该cmdlet完成所需的时间（以秒为单位）。如果未指定**Wait**参数，那么cmdlet会一直等待直到完成；如果指定值为`0`，则命令会被立即执行，且cmdlet会在不等待的情况下返回结果。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。不过实际上这个cmdlet并没有被执行。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters.PowerShell-clusterNode

## 输出

## 备注

## 相关链接

[添加集群节点](./Add-ClusterNode.md)

[Get-ClusterNode](./Get-ClusterNode.md)

[Remove-ClusterNode](./Remove-ClusterNode.md)
