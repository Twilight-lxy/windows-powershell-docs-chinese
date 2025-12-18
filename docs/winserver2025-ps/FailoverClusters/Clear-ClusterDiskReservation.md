---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/clear-clusterdiskreservation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-ClusterDiskReservation
---

# 清除集群磁盘预留（Clear-ClusterDiskReservation）

## 摘要
清除故障转移集群中磁盘上的永久性保留信息（即那些不会被自动删除的数据）。

## 语法

```
Clear-ClusterDiskReservation [[-Node] <StringCollection>] -Disk <UInt32[]> [-Force] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Clear-ClusterDiskReservation` cmdlet 用于清除故障转移集群中磁盘上的永久性预留信息。除非指定了 `Force` 参数，否则该 cmdlet 会提示用户进行确认操作。

> [!注意] > 如果服务器计算机上没有启用凭据安全服务提供程序（CredSSP）的身份验证机制，此cmdlet无法远程运行。

## 示例

### 示例 1

```powershell
Clear-ClusterDiskReservation -Disk 5
```

此示例在获取用户确认后，会清除本地节点上“磁盘5”上的持久性预订（即已预留的资源）。

### 示例 2

```powershell
Clear-ClusterDiskReservation -Disk 6 -Node node2 -Force
```

这个示例会清除名为 `node2` 的节点上位于 `Disk 6` 上的持久性预留资源，而无需请求用户的确认。

## 参数

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

### -Disk

指定用于清除持久性预留资源的磁盘编号。该编号是指在节点的“磁盘管理”工具中显示的磁盘编号。

```yaml
Type: UInt32[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

直接运行该cmdlet，而不会提示用户进行确认。默认情况下，该cmdlet在执行前会先询问用户的确认意见。

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

### -Node

指定要清除磁盘预留的集群节点的名称。

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

展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

### 无

## 输出

### 无

## 备注

## 相关链接

[Clear-ClusterNode](./Clear-ClusterNode.md)

[Remove-Cluster](./Remove-Cluster.md)
