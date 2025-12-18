---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 09/17/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clustercredential?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterCredential
---

# 获取集群凭据

## 摘要
检索故障转移集群中指定节点的凭据。

## 语法

```
Get-ClusterCredential [[-NodeName] <String>] [<CommonParameters>]
```

## 描述

`Get-ClusterCredential` cmdlet 可以检索故障转移集群中指定节点的凭据信息。

## 示例

### 示例 1

```powershell
Get-ClusterCredential -NodeName "Node01"
```

这个示例用于获取故障转移集群中名为“Node01”的节点的凭据信息。

## 参数

### -NodeName

指定用于获取凭据的节点的名称。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.Management Automation.PSCredential

## 备注

## 相关链接
