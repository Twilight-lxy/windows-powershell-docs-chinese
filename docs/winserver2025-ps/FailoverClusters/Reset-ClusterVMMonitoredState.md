---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/reset-clustervmmonitoredstate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Reset-ClusterVMMonitoredState
---

# 重置 ClusterVMM 的监控状态

## 摘要
将虚拟机的应用程序状态重置为“正常”状态，从而使该虚拟机在集群中不再被标记为处于临界状态。

## 语法

```
Reset-ClusterVMMonitoredState [-Wait <Int32>] [<CommonParameters>]
```

## 描述

`Reset-ClusterVMMonitoredState` cmdlet 用于将虚拟机的应用关键状态（Application Critical status）重置为正常状态，从而使该虚拟机不再在集群中被标记为处于关键状态。注意：此 cmdlet 只能在本机上直接运行，或者通过 Windows PowerShell 的远程连接来对虚拟机执行操作。

## 示例

### 示例 1

```powershell
Reset-ClusterVMMoniteredState
```

这个示例会重置虚拟机的状态，并清除所有关键错误信息（即“critical state”）。

## 参数

### -Wait

指定等待该 cmdlet 完成的时间（以秒为单位）。如果未指定 `Wait` 参数，那么 cmdlet 会一直等待直到完成；如果指定了 `-Wait 0`，则 cmdlet 会立即开始执行并立即返回结果，而不会进行等待。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Add-ClusterVMMonitoredItem](./Add-ClusterVMMonitoredItem.md)

[Get-ClusterVMMonitoredItem](./Get-ClusterVMMonitoredItem.md)

[Remove-ClusterVMMonitoredItem](./Remove-ClusterVMMonitoredItem.md)
