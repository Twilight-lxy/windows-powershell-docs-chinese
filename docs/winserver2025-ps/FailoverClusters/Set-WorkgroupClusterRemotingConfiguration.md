---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.Adless.PowerShell.psm1-help.xml
Module Name: FailoverClusters
ms.date: 09/11/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusters/set-workgroupclusterremotingconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WorkgroupClusterRemotingConfiguration
---

# 设置工作组集群远程访问配置

## 摘要
配置作为工作组的一部分的故障转移集群的远程管理设置。

## 语法

```
Set-WorkgroupClusterRemotingConfiguration [<CommonParameters>]
```

## 描述

`Set-WorkgroupClusterRemotingConfiguration` cmdlet 用于配置属于工作组的故障转移集群的远程管理设置。

## 示例

### 示例 1

```powershell
Set-WorkgroupClusterRemotingConfiguration -Verbose
```

这个示例展示了关于当前工作组集群远程配置的详细信息。

## 参数

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[添加工作组集群节点](add-workgroupclusternode.md)

[New-WorkgroupCluster](new-workgroupcluster.md)

[Remove-WorkgroupCluster](remove-workgroupcluster.md)

[Remove-WorkgroupClusterNode](remove-workgroupclusternode.md)

[Test-WorkgroupCluster](test-workgroupcluster.md)

[测试-工作组集群远程访问](test-workgroupclusterremoting.md)
