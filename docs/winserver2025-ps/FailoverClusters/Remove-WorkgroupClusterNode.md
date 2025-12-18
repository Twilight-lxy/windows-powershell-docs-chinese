---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.Adless.PowerShell.psm1-help.xml
Module Name: FailoverClusters
ms.date: 09/11/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusters/remove-workgroupclusternode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-WorkgroupClusterNode
---

# 删除工作组集群节点

## 摘要
从工作组集群中删除一个节点。

## 语法

```
Remove-WorkgroupClusterNode [-Node] <String[]> [-Credentials] <PSCredential[]> [-Name] <String>
 [[-Wait] <Int32>] [-IgnoreStorageConnectivityLoss] [-CleanupDisks] [-Force] [-Confirm] [-WhatIf]
 [<CommonParameters>]
```

## 描述

`Remove-WorkgroupCluster` 函数用于将某个节点从工作组集群（workgroup cluster）的成员列表中移除。其余参数将会被传递给 `Remove-ClusterNode` 函数。有关 [Remove-ClusterNode](/powershell/module/failoverclusters/remove-clusternode) cmdlet 的详细信息，请参阅相关文档。

## 示例

### 示例 1

```powershell
Remove-WorkgroupClusterNode -Node "Node1", "Node2" -Credentials $cred1, $cred2 -Name $Node2
```

这个示例将 `Node2` 从集群成员列表中删除。

### 示例 2

```powershell
Remove-WorkgroupClusterNode -Node "Node1", "Node2" -Credentials $cred1, $cred2 -Name $Node3
```

这个示例会将 `Node3` 从集群成员中移除。

可能需要手动进行清理操作，才能通过登录到 `Node3` 并运行 `Clear-ClusterNode` 命令来恢复节点的正常状态。

## 参数

### -Node

工作组集群中的一系列节点。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credentials

用于这些节点的一组凭据信息。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name

需要删除的节点的名称。如果该名称没有包含在 `Node` 参数中，那么将使用 `Node` 参数中的第一个节点来执行删除操作。此外，还需要进行额外的清理工作以清除该节点的状态信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Wait

指定等待该cmdlet完成所需的时间（以秒为单位）。如果未指定**Wait**参数，那么cmdlet会一直等待直到任务完成。如果指定值为`0`，则命令会被立即执行，cmdlet会在不等待的情况下立即返回结果。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: 0
Accept pipeline input: False
Accept wildcard characters: False
```

### -CleanupDisks

从指定的磁盘上删除所有残留的集群元数据。这些元数据包含集群服务用于管理磁盘的信息。通过清除元数据，磁盘就可以摆脱旧的集群配置，从而可以将其用于新的集群或其他用途。此cmdlet可以避免在重新使用磁盘时由于残留元数据而可能引发的潜在冲突。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

强制命令运行，而不会询问用户的确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -IgnoreStorageConnectivityLoss

该参数表示：即使启用了“Storage Spaces Direct”功能，此cmdlet也不会检查集群节点是否包含非共享存储资源。如果您未指定此参数，cmdlet会自动检查该节点是否存在“Storage Spaces Direct”存储资源。如果发现存在此类存储资源，在删除该节点之前，系统会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm

在运行cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

## 输出

## 备注

## 相关链接

[添加工作组集群节点](add-workgroupclusternode.md)

[清除集群节点](clear-clusternode.md)

[新工作组集群](new-workgroupcluster.md)

[Remove-WorkgroupCluster](remove-workgroupcluster.md)

[Set-WorkgroupClusterRemotingConfiguration](set-workgroupclusterremotingconfiguration.md)

[Test-WorkgroupCluster](test-workgroupcluster.md)

[Test-WorkgroupClusterRemoting](test-workgroupclusterremoting.md)
