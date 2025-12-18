---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/remove-clustersharedvolume?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ClusterSharedVolume
---

# 删除集群共享卷

## 摘要
从故障转移集群中的“集群共享卷”中删除某个卷，并将其放入该集群的“可用存储”资源中。

## 语法

```
Remove-ClusterSharedVolume [[-Name] <StringCollection>] [-InputObject <PSObject>]
 [-Cluster <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-ClusterSharedVolume` cmdlet 用于从故障转移集群中的 Cluster Shared Volumes 中删除某个卷，并将其放入该集群的 “可用存储”（Available Storage）中。将卷放入可用存储后，您可以在配置新的集群角色时使用该卷。

## 示例

### 示例 1

```powershell
Remove-ClusterSharedVolume -Name "Cluster Disk 3"
```

这个示例会将名为“Cluster Disk 3”的CSV文件从本地集群的“Cluster Shared Volumes”中删除，并将其放入“Available Storage”（可用存储）中。

### 示例 2

```powershell
Get-ClusterSharedVolume -Name "Cluster Disk 4" | Remove-ClusterSharedVolume
```

这个示例会将名为“Cluster Disk 4”的CSV文件从本地集群的“Cluster Shared Volumes”中删除，并将其放入“Available Storage”（可用存储）中。

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

指定要删除的集群共享卷（Cluster Shared Volume）。

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

指定要删除的集群共享卷（Cluster Shared Volume）的名称。

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

### -WhatIf

展示了如果该cmdlet运行会发生的结果。但实际上该cmdlet并没有被运行。

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

### MicrosoftFailoverClusters.PowerShell ClusterSharedVolume

## 输出

### MicrosoftFailoverClusters.PowerShellClusterResource

## 备注

## 相关链接

[添加集群共享卷](./Add-ClusterSharedVolume.md)

[Get-ClusterSharedVolume](./Get-ClusterSharedVolume.md)

[Move-ClusterSharedVolume](./Move-ClusterSharedVolume.md)
