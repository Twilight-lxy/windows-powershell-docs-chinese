---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clustervmmonitoreditem?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterVMMonitoredItem
---

# 获取集群虚拟机监控项

## 摘要
获取虚拟机中当前正在被监控的服务和事件的列表。

## 语法

### VirtualMachine（默认设置）

```
Get-ClusterVMMonitoredItem [[-VirtualMachine] <String>] [-Wait <Int32>] [-Cluster <String>]
 [<CommonParameters>]
```

### VMId

```
Get-ClusterVMMonitoredItem [-VMId <Guid>] [-Wait <Int32>] [-Cluster <String>] [<CommonParameters>]
```

### InputObject

```
Get-ClusterVMMonitoredItem [-Wait <Int32>] [-InputObject <PSObject>] [-Cluster <String>]
 [<CommonParameters>]
```

## 描述

`Get-ClusterVMMonitoredItem` cmdlet 可以获取当前在虚拟机中正在被监控的服务和事件的列表。如果其中某个服务发生故障，或者某个事件被触发，系统会根据该虚拟机资源的故障转移配置采取相应的措施进行响应。例如，配置可能规定需要重新启动该虚拟机。

## 示例

### 示例 1

```powershell
Get-Cluster -Name Cluster1 | Get-ClusterVMMonitoredItem -VirtualMachine vm1
```

这个示例会返回在名为 `Cluster1` 的集群中、名为 `vm1` 的虚拟机上被监控的服务和事件信息。

## 参数

### -Cluster

指定用于运行此 cmdlet 的集群名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 将在本地集群上运行。

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

指定要运行该cmdlet的集群，或者是要从中检索被监控的集群虚拟机对象的集群化虚拟机。

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

### -VMId

指定虚拟机标识符（ID）。

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

指定要对其进行监控的集群化虚拟机的名称。当指定了此参数时，必须在主机集群节点之一上运行该 cmdlet；否则还必须指定 **Cluster** 参数。

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

指定等待该cmdlet完成所需的时间（以秒为单位）。如果未指定**Wait**参数，那么cmdlet会一直等待直到任务完成。如果指定了`-Wait 0`，则命令会立即被执行，而cmdlet会在不进行等待的情况下直接返回结果。

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

### MicrosoftFailoverClusters.PowerShell Cluster

### Microsoft FailoverClusters.PowerShell ClusterGroup

### MicrosoftFailoverClusters.PowerShell ClusterResource

## 输出

### MicrosoftFailoverClusters.PowerShell.ClusterVMMonitoredItem

## 备注

## 相关链接

[Add-ClusterVMMonitoredItem](./Add-ClusterVMMonitoredItem.md)

[Remove-ClusterVMMonitoredItem](./Remove-ClusterVMMonitoredItem.md)

[Reset-ClusterVMMonitoredState](./Reset-ClusterVMMonitoredState.md)
