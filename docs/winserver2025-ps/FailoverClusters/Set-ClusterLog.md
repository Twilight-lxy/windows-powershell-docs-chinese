---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/set-clusterlog?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ClusterLog
---

# 设置集群日志（Set-ClusterLog）

## 摘要
设置集群日志的大小和详细程度级别。

## 语法

```
Set-ClusterLog [-Size <Int32>] [-Level <Int32>] [-InputObject <PSObject>] [-Cluster <String>]
 [<CommonParameters>]
```

## 描述

`Set-ClusterLog` cmdlet 用于设置集群日志的大小和详细程度。默认的详细程度为 `3`，包括错误信息、警告信息以及其他相关数据。

## 示例

### 示例 1

```powershell
Set-ClusterLog -Level 1
```

这个示例将集群日志的详细程度设置为`1`。

### 示例 2

```powershell
Set-ClusterLog -Size 1024
```

这个示例将集群日志的大小设置为 1024 MB。

## 参数

### -Cluster

指定要运行此cmdlet的集群名称。如果该参数的值为`.`或被省略，则cmdlet将在本地集群上运行。

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

### -Level

指定要为集群设置的日志级别。该参数的可接受值为：`0` 到 `5`。

| Level  | Error  | Warning  | Info  | Verbose | Debug |
|:-----|:-----|:-----|:-----|:-----|:-----|
|0 (Disabled) ||||||
|1 |&#x2714;||||
|2 |&#x2714;|&#x2714;|||
|3 (Default) |&#x2714;|&#x2714;|&#x2714;||
|4 |&#x2714;|&#x2714;|&#x2714;|&#x2714;|
|5 |&#x2714;|&#x2714;|&#x2714;|&#x2714;|&#x2714;|

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

### -Size

指定要为集群设置的日志大小。在 Windows 2016 中，该参数的可接受值为：8 MB 到 1024 MB。在 Windows 2019 中，该参数的可接受值为：8 MB 到 2048 MB。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters PowerShellCluster

## 输出

### Microsoft FailoverClusters PowerShellCluster

## 备注

## 相关链接

[Get-ClusterLog](./Get-ClusterLog.md)
