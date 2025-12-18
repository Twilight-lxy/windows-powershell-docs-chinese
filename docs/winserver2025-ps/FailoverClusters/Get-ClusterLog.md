---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusterlog?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterLog
---

# 获取集群日志

## 摘要
在故障转移集群中，为所有节点或某个特定节点创建一个日志文件。

## 语法

```
Get-ClusterLog [[-Node] <StringCollection>] [-Destination <String>] [-TimeSpan <UInt32>]
 [-UseLocalTime] [-SkipClusterState] [-Health] [-InputObject <PSObject>] [-Cluster <String>]
 [<CommonParameters>]
```

## 描述

`Get-ClusterLog` cmdlet 为故障转移集群中的所有节点或某个特定节点创建一个日志文件。

在为集群创建日志文件时，除了指定日志文件的目标存储位置外，您还可以指定希望记录信息的时间范围。

注意：如果没有服务器计算机上的凭据安全服务提供程序（CredSSP）身份验证功能，此cmdlet无法远程运行。

## 示例

### 示例 1：为本地集群创建一个日志文件

```powershell
Get-ClusterLog
```

此命令会在集群的每个节点上的 `C:\Windows\Cluster\Reports` 文件夹中为本地集群创建一个日志文件。

### 示例 2：为每个节点创建日志文件，并将其保存在本地

```powershell
Get-ClusterLog -Destination .
```

该命令会为本地集群中的每个节点创建一个日志文件，并将所有日志复制到指定的本地文件夹中。

### 示例 3：为本地集群创建一个日志文件，记录过去五分钟内的数据

```powershell
Get-ClusterLog -TimeSpan 5
```

该命令会在集群的每个节点上的 `C:\Windows\Cluster\Reports` 文件夹中为本地集群创建一个日志文件。该日志记录了过去 5 分钟内的所有事件。

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

### -Destination

指定要将一个或多个集群日志复制到的位置。如果想将日志复制到当前文件夹中，可以使用`.`作为该参数的输入值。默认位置是 `C:\Windows\Cluster\Reports`。

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

### -Health

表示该cmdlet还会记录集群的健康状况信息。

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

指定用于生成集群日志的集群。

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

### -Node

指定要生成集群日志的集群节点名称。

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

### -SkipClusterState

表示该 cmdlet 不会向集群日志中添加额外的集群状态信息。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: scs

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TimeSpan

指定用于生成集群日志的时间跨度（以分钟为单位）。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: Span

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseLocalTime

指定每个集群日志条目的时间戳使用本地时间。默认情况下，时间戳使用格林尼治标准时间（GMT）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: lt

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters PowerShell Cluster

## 输出

### System.IO.FileInfo

## 备注

## 相关链接

[Set-ClusterLog](./Set-ClusterLog.md)
