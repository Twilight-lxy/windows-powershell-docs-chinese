---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/start-clustergroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-ClusterGroup
---

# 启动 ClusterGroup

## 摘要
在故障转移集群上启动一个或多个群集角色（也称为资源组）。

## 语法

```
Start-ClusterGroup [[-Name] <String>] [-IgnoreLocked] [-ChooseBestNode] [-Wait <Int32>]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Start-ClusterGroup` cmdlet 可以在故障转移集群上启动一个或多个集群角色（也称为资源组）。使用此 cmdlet，可以在因维护或诊断需要停止某个集群角色后重新启动它。

## 示例

### 示例 1

```powershell
Start-ClusterGroup FileServer1
```

这个示例启动了一个名为 `FileServer1` 的集群文件服务器或资源组。

### 示例 2

```powershell
Start-ClusterGroup FileServer1 -Wait 0
```

这个示例启动了一个名为“FileServer1”的集群文件服务器或资源组。一旦操作开始执行，Windows PowerShell提示符就会立即显示出来。

## 参数

### -ChooseBestNode

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

### -Cluster

指定要运行此cmdlet的集群名称。如果该参数的输入值为`.`或被省略，则cmdlet将在本地集群上运行。

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

### -IgnoreLocked

指定在运行此cmdlet时忽略已锁定的组。

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

### -InputObject

指定要启动的集群角色。

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

指定要启动的集群角色的名称。

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

### -Wait

指定等待该cmdlet完成所需的时间（以秒为单位）。如果未指定**Wait**参数，那么cmdlet会一直等待直到完成；如果指定了`-Wait 0`，则命令会被立即执行，而cmdlet会在不进行任何等待的情况下立即返回结果。

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

### MicrosoftFailoverClusters.PowerShell-clusterGroup

## 输出

### MicrosoftFailoverClusters.PowerShell-clusterGroup

## 备注

## 相关链接

[Add-ClusterGroup](./Add-ClusterGroup.md)

[Get-ClusterGroup](./Get-ClusterGroup.md)

[Move-ClusterGroup](./Move-ClusterGroup.md)

[Remove-ClusterGroup](./Remove-ClusterGroup.md)

[停止集群组](./Stop-ClusterGroup.md)
