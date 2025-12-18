---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell-help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/get-clusterdiagnosticinfo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ClusterDiagnosticInfo
---

# 获取集群诊断信息

## 摘要
为包含虚拟机的集群获取诊断信息，并生成一个包含这些数据的ZIP文件。

## 语法

### 编写

```
Get-ClusterDiagnosticInfo [[-WriteToPath] <String>] [[-Cluster] <String>] [[-ZipPrefix] <String>]
 [-HoursOfEvents <Int32>] [-IncludeEvents] [<CommonParameters>]
```

### 阅读

```
Get-ClusterDiagnosticInfo -ReadFromPath <String> [<CommonParameters>]
```

## 描述

`Get-ClusterDiagnosticInfo` cmdlet 可以获取包含虚拟机的集群的诊断信息，并生成一个包含这些数据的 ZIP 文件。

## 示例

### 示例 1：将诊断信息写入指定的路径

```powershell
Get-ClusterDiagnosticInfo -WriteToPath "C:\Users\MyUser\HealthTest\"
```

这个命令将集群诊断信息读取并写入到 `C:\Users\MyUser\HealthTest\` 文件夹中。

## 参数

### -Cluster

指定该 cmdlet 所获取的集群的名称。

```yaml
Type: String
Parameter Sets: Write
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HoursOfEvents

指定此cmdlet收集系统事件日志的时间范围（以小时为单位）。

```yaml
Type: Int32
Parameter Sets: Write
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeEvents

表示此 cmdlet 用于收集系统事件日志。

```yaml
Type: SwitchParameter
Parameter Sets: Write
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReadFromPath

指定在检查之前收集的日志文件时用于读取数据的路径。

```yaml
Type: String
Parameter Sets: Read
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WriteToPath

指定用于创建包含所有日志的ZIP文件的路径。

```yaml
Type: String
Parameter Sets: Write
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ZipPrefix

指定要添加到生成的ZIP文件前面的名称。

```yaml
Type: String
Parameter Sets: Write
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[故障转移集群](./failoverclusters.md)
