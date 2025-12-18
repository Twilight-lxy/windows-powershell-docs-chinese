---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/block-clusteraccess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Block-ClusterAccess
---

# 块集群访问（Block-ClusterAccess）

## 摘要
阻止指定的用户访问故障转移集群。

## 语法

```
Block-ClusterAccess [-User] <StringCollection> [-InputObject <PSObject>] [-Cluster <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Block-ClusterAccess` cmdlet 可以阻止指定的用户访问故障转移集群。如果你不想完全禁止该用户访问，而是希望仅允许其使用 Windows PowerShell 查看集群配置（而不允许修改配置），则可以使用带有 `Readonly` 参数的 `Grant-ClusterAccess` cmdlet。

## 示例

### 示例 1

```powershell
Block-ClusterAccess -User contoso\johnj99
```

这个示例可以阻止名为 `johnj99` 的用户在 `contoso` 域名下访问本地集群。

## 参数

### -Cluster

指定要运行此 cmdlet 的集群名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 会在本地集群上运行。

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

### -InputObject

指定要阻止给定用户访问的集群。

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

指定要阻止其访问集群的用户。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果该cmdlet被运行会发生什么情况。但实际上这个cmdlet并没有被执行。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters PowerShellCluster

## 输出

## 备注

## 相关链接

[Get-ClusterAccess](./Get-ClusterAccess.md)

[Grant-ClusterAccess](./Grant-ClusterAccess.md)

[Remove-ClusterAccess](./Remove-ClusterAccess.md)
