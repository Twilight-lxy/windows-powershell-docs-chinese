---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusteraccess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterAccess
---

# 获取集群访问权限

## 摘要
获取有关控制对故障转移集群访问权限的信息。

## 语法

```
Get-ClusterAccess [[-User] <StringCollection>] [-InputObject <PSObject>] [-Cluster <String>]
 [<CommonParameters>]
```

## 描述

`Get-ClusterAccess` cmdlet 可以获取有关控制对故障转移集群访问权限的信息。

一个集群可以允许用户进行完全访问或仅限读取访问。仅限读取访问权限的用户只能使用 Windows PowerShell 中的那些能够提供关于集群信息的 cmdlet（命令行工具）。

## 示例

### 示例 1

```powershell
Get-ClusterAccess
```

这个示例列出了分配给该集群用户的权限级别，其中包括那些被阻止访问的用户。

## 参数

### -Cluster

指定用于运行此cmdlet的集群名称。如果该参数的值为`.`或被省略，则cmdlet将在本地集群上运行。

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

指定用于枚举集群访问详细信息的集群。

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

### -User

指定要获取集群访问权限的用户。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowShell-cluster

## 输出

### MicrosoftFailoverClusters.PowerShell_clusterAccessRule

## 备注

## 相关链接

[Block-ClusterAccess](./Block-ClusterAccess.md)

[Grant-ClusterAccess](./Grant-ClusterAccess.md)

[Remove-ClusterAccess](./Remove-ClusterAccess.md)
