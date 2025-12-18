---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/remove-clustervmmonitoreditem?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ClusterVMMonitoredItem
---

# 删除 ClusterVMM 监控项

## 摘要
## 语法

### VirtualMachine（默认值）

```
Remove-ClusterVMMonitoredItem [-InputObject <PSObject>] [-Service <StringCollection>]
 [-EventLog <String>] [-EventSource <String>] [-EventId <Int32>] [[-VirtualMachine] <String>]
 [-Wait <Int32>] [-Cluster <String>] [<CommonParameters>]
```

### VMId

```
Remove-ClusterVMMonitoredItem [-InputObject <PSObject>] [-Service <StringCollection>]
 [-EventLog <String>] [-EventSource <String>] [-EventId <Int32>] [-VMId <Guid>] [-Wait <Int32>]
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Remove-ClusterVMMonitoredItem` cmdlet 用于停止对某个当前正在被监控的服务或事件的监控。在取消监控后，如果该服务出现故障或相关事件发生，系统将不再采取任何操作（例如重启虚拟机）。

## 示例

### 示例 1

```powershell
Get-ClusterVMMonitoredItem -VirtualMachine VM1 | Remove-ClusterVMMonitoredItem -VirtualMachine VM1
```

这个示例会移除在名为`VM1`的虚拟机上被监控的所有项目。

### 示例 2

```powershell
Remove-ClusterVMMonitoredItem -VirtualMachine VM1 -Service spooler
```

这个示例会取消对名为`VM1`的虚拟机上的打印后台进程（print spooler service）的监控功能。

## 参数

### -Cluster

指定要运行此 cmdlet 的集群的名称。如果该参数的输入为`.` 或被省略，则 cmdlet 将在本地集群上运行。

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

### -EventId

指定要从监控中移除的 Windows 事件跟踪（ETW）事件的标识符（ID）。

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

### -EventLog

指定要从监控中移除的事件对应的事件日志。

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

### -EventSource

指定要从监控中移除的事件的来源。

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

指定用于运行该cmdlet的集群、要从其中移除监控功能的集群化虚拟机，或是需要停止对其实施监控的集群化虚拟机中的被监控对象。

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

### -Service

指定要从监控中移除的服务名称。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMId

指定虚拟机的标识符（ID）。

```yaml
Type: Guid
Parameter Sets: VMId
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -VirtualMachine

指定要从中移除监控功能的集群虚拟机的名称。当指定了此参数时，必须在该主机集群节点之一上运行此 cmdlet；否则还必须指定 **Cluster** 参数。

```yaml
Type: String
Parameter Sets: VirtualMachine
Aliases: VM

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Wait

指定用于等待该 cmdlet 的时间（以秒为单位）。如果未指定 **Wait** 参数，那么 cmdlet 将一直等待直到完成。如果指定了 `-Wait 0`，则 cmdlet 会立即开始执行并立即返回结果，而不会进行任何等待。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell.Cluster

### Microsoft FailoverClusters.PowerShell ClusterGroup

### MicrosoftFailoverClusters.PowerShellClusterResource

### Microsoft_failoverClusters.PowerShell ClusterVMMonitoredItem

## 输出

### 无

## 备注

## 相关链接

[Add-ClusterVMMonitoredItem](./Add-ClusterVMMonitoredItem.md)

[Get-ClusterVMMonitoredItem](./Get-ClusterVMMonitoredItem.md)

[Reset-ClusterVMMonitoredState](./Reset-ClusterVMMonitoredState.md)
