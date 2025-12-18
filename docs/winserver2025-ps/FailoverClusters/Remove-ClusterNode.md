---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/remove-clusternode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ClusterNode
---

# 删除集群节点

## 摘要
从故障转移集群中删除一个节点。

## 语法

```
Remove-ClusterNode [[-Name] <StringCollection>] [-Force] [-Wait <Int32>]
 [-IgnoreStorageConnectivityLoss] [-CleanupDisks] [-InputObject <PSObject>] [-Cluster <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-ClusterNode` cmdlet 用于从故障转移集群中删除一个节点。删除该节点后，该节点将不再作为集群的一部分运行，除非将其重新添加回集群中。删除节点的过程也被称为“将节点逐出集群”。

注意：如果没有服务器计算机上的凭据安全服务提供程序（CredSSP）进行身份验证，此 cmdlet 无法远程运行。

## 示例

### 示例 1

```powershell
Remove-ClusterNode -Name node4
```

这个示例会从本地集群中删除名为 `node4` 的节点。

### 示例 2

```powershell
Remove-ClusterNode -Name node4 -Force
```

这个示例会从本地集群中删除名为 `node4` 的节点，而不会要求用户确认操作。

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

### -Force

该cmdlet会在不提示用户确认的情况下直接执行操作。默认情况下，该cmdlet在执行前会向用户请求确认。

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

### -IgnoreStorageConnectivityLoss

该参数表示：如果已启用“Storage Spaces Direct”功能，此cmdlet不会检查集群节点是否包含非共享存储资源。如果您未指定此参数，cmdlet会自动检查该节点是否存在“Storage Spaces Direct”存储资源。如果发现存在“Storage Spaces Direct”存储资源，cmdlet会在删除该节点之前提示您确认操作。

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

指定要删除的集群节点。

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

指定要删除的集群节点的名称。

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

指定等待该 cmdlet 完成的时间（以秒为单位）。如果未指定 `Wait` 参数，那么 cmdlet 会一直等待直到完成。如果指定了 `-Wait 0`，则命令会被立即执行，而 cmdlet 会在不等待的情况下返回结果。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell-clusterNode

## 输出

## 备注

## 相关链接

[添加集群节点](./Add-ClusterNode.md)

[Get-ClusterNode](./Get-ClusterNode.md)

[Resume-ClusterNode](./Resume-ClusterNode.md)

[启动集群节点](./Start-ClusterNode.md)

[停止集群节点](./Stop-ClusterNode.md)

[暂停集群节点](./Suspend-ClusterNode.md)
