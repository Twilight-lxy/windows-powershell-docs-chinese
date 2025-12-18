---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clustervmmonitoreditem?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterVMMonitoredItem
---

# 添加集群虚拟机监控项（Add-ClusterVMMonitoredItem）

## 摘要
配置对某个服务的监控机制，或者针对 Windows 事件跟踪（Event Tracing, ETW）事件的监控设置，以便在虚拟机上对这些服务或事件进行监控。

## 语法

### VirtualMachine（默认设置）

```
Add-ClusterVMMonitoredItem [-Service <StringCollection>] [-EventLog <String>]
 [-EventSource <String>] [-EventId <Int32>] [-OverrideServiceRecoveryActions]
 [[-VirtualMachine] <String>] [-Wait <Int32>] [-Cluster <String>] [<CommonParameters>]
```

### VMId

```
Add-ClusterVMMonitoredItem [-Service <StringCollection>] [-EventLog <String>]
 [-EventSource <String>] [-EventId <Int32>] [-OverrideServiceRecoveryActions] [-VMId <Guid>]
 [-Wait <Int32>] [-Cluster <String>] [<CommonParameters>]
```

### InputObject

```
Add-ClusterVMMonitoredItem [-Service <StringCollection>] [-EventLog <String>]
 [-EventSource <String>] [-EventId <Int32>] [-OverrideServiceRecoveryActions] [-Wait <Int32>]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Add-ClusterVMMonitoredItem` cmdlet 用于配置对某个服务或 Windows 事件跟踪 (ETW) 事件的监控，以便在虚拟机上对该服务或事件进行监视。当该服务出现故障或相应事件发生时，系统会根据虚拟机资源的故障转移配置采取相应的措施（例如重启虚拟机）。

## 示例

### 示例 1

```powershell
$parameters = @{
    VirtualMachine = 'test-VM11'
    EventLog = 'Microsoft-Windows-FailoverClustering-Manager/Admin'
    EventSource = 'Microsoft-Windows-FailoverClustering-Manager'
    EventId = '4708'
}
Add-ClusterVMMonitoredItem @parameters
```

这个示例为 ETW 事件 ID `4708` 添加了监控功能。该示例使用了“拼接”（splatting）技术，将 `$Parameters` 变量中的参数值传递给相应的命令。有关 [Splatting](/powershell/module/microsoft.powershell.core/about/about_splatting) 的更多信息，请参阅相关文档。

### 示例 2

```powershell
Add-ClusterVMMonitoredItem -VirtualMachine test-VM11 -Service spooler
```

这个示例配置了对打印队列服务（print spooler service）的监控功能。

## 参数

### -Cluster

指定用于运行此cmdlet的集群名称。如果该参数的输入值为`.`或被省略，则cmdlet将在本地集群上运行。

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

指定要监控的事件的标识符（ID）。

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

指定要监控的事件的事件日志。

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

指定要监控的事件的来源（即事件发生的源头）。

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

指定用于运行该 cmdlet 的集群、用于配置监控的集群虚拟机，以及需要被监控的集群虚拟机对象。

```yaml
Type: PSObject
Parameter Sets: InputObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -OverrideServiceRecoveryActions

该设置表明：如果集群服务未正确配置以进行监控，那么该服务将通过覆盖（override）现有的服务恢复机制来自动修复相关问题。要使集群服务能够被用于监控，需要满足以下条件：

- None of the service recovery actions are set to Restart the computer.

和（逻辑运算符）

- At least one of the service recovery actions are set to Take no action.

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

### -Service

指定要监控的服务的名称。这必须是服务的简称，而不是全称。例如，应指定“clussvc”，而不是“Failover Cluster Service”。

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

指定要对其进行监控的集群化虚拟机的名称。当指定了此参数时，必须在该主机集群节点之一上运行该cmdlet；否则还必须同时指定`Cluster`参数。

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

指定等待该cmdlet完成所需的时间（以秒为单位）。如果未指定**Wait**参数，则cmdlet会一直等待直到完成；如果指定了值`0`，则会立即启动调用，而cmdlet会在不等待的情况下返回结果。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FAILoverClusters.PowerShell Cluster

### Microsoft FailoverClusters.PowerShell ClusterGroup

### Microsoft FailoverClusters.PowerShell_clusterResource

### Microsoft FAILoverClusters.PowerShell_clusterVMMonitoredItem

## 输出

### 无

## 备注

## 相关链接

[Get-ClusterVMMonitoredItem](./Get-ClusterVMMonitoredItem.md)

[Remove-ClusterVMMonitoredItem](./Remove-ClusterVMMonitoredItem.md)

[Reset-ClusterVMMonitoredState](./Reset-ClusterVMMonitoredState.md)
