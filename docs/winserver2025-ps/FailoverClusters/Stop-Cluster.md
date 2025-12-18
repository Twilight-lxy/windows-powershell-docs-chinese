---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/23/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/stop-cluster?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-Cluster
---

# 停止集群（Stop-Cluster）

## 摘要
在故障转移集群中的所有节点上停止Cluster服务，这将导致集群中配置的所有服务和应用程序也随之停止运行。

## 语法

### 集群名称（默认值）

```
Stop-Cluster [[-Cluster] <String>] [-Force] [-Wait <Int32>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### InputObject

```
Stop-Cluster [-Force] [-Wait <Int32>] [-InputObject <PSObject>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Stop-Cluster` cmdlet 会停止故障转移集群中所有节点上的 Cluster 服务，这会导致集群中配置的所有服务和应用程序也停止运行。只有当某个节点上正在运行 Cluster 服务时，该节点才能作为集群的一部分正常工作。

## 示例

### 示例 1：停止本地集群中所有节点上的集群服务

```powershell
Stop-Cluster
```

这个示例会停止本地集群中所有节点上的Cluster服务，从而导致集群中配置的所有服务和应用程序也随之停止运行。

### 示例 2：停止集群中所有节点上的集群服务

```powershell
Stop-Cluster -Name cluster1
```

这个示例会停止名为 `cluster1` 的集群中所有节点上的 Cluster 服务，从而终止该集群中配置的所有服务和应用程序。

## 参数

### -Cluster

指定用于运行此cmdlet的集群名称。如果该参数的输入值为`.`或被省略，则cmdlet将在本地集群上运行。

```yaml
Type: String
Parameter Sets: Cluster name
Aliases: Name

Required: False
Position: 0
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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

直接运行该 cmdlet，而不会提示用户进行确认。默认情况下，该 cmdlet 会在执行前询问用户的确认。

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

指定要停止运行的集群。

```yaml
Type: PSObject
Parameter Sets: InputObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Wait

指定等待该 cmdlet 完成的时间（以秒为单位）。如果未指定 **Wait** 参数，那么 cmdlet 会一直等待直到完成。如果指定了 `-Wait 0`，则命令会被立即执行，且 cmdlet 会在不等待的情况下立即返回结果。

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

展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShellCluster

## 输出

### 无

## 备注

## 相关链接

[Get-Cluster](./Get-Cluster.md)

[新集群](./New-Cluster.md)

[Remove-Cluster](./Remove-Cluster.md)

[启动集群](./Start-Cluster.md)

[测试集群](./Test-Cluster.md)
