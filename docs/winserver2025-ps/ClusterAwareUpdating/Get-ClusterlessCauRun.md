---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 07/01/2024
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/get-clusterlesscaurun?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterlessCauRun
---

# 获取-ClusterlessCauRun

## 摘要
检索与任何集群无关的“Cluster-Aware Updating（CAU）”运行相关的信息。

## 语法

### DefaultParamSet（默认值）

```
Get-ClusterlessCauRun [-Credential <PSCredential>] [<CommonParameters>]
```

### ShowClusterNodeState

```
Get-ClusterlessCauRun [-Credential <PSCredential>] [-ShowClusterNodeState] [<CommonParameters>]
```

## 描述

`Get-ClusterlessCauRun` cmdlet 用于检索与集群无关的 Cluster-Aware Updating (CAU) 运行相关的信息。

## 示例

### 示例 1

```powershell
Get-ClusterlessCauRun
```

这个示例显示了有关当前CAU运行过程的信息，包括每个正在被更新的节点的状态。

## 参数

### -Credential

指定目标集群的管理凭据。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ShowClusterNodeState

显示关于CAU运行过程中每个节点状态的详细信息。

```yaml
Type: SwitchParameter
Parameter Sets: ShowClusterNodeState
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### Microsoft-clusterawareupdating.cauwmiobject

### Microsoft ClusterAware UpdatingClusterlessCauRun

### Microsoft ClusterAwareUpdating.RunState

## 备注

## 相关链接

[Invoke-ClusterlessCauRun](invoke-clusterlesscaurun.md)
