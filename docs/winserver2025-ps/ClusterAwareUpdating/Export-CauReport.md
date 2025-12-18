---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 09/27/2022
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/export-caureport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-CauReport
---

# 导出Cau报告

## 摘要
将一份或多份“更新运行”报告导出为HTML或CSV格式的文档。

## 语法

```
Export-CauReport [-InputReport] <CauReport[]> [-Format] <OutputType> [-Path] <String> [-PassThru]
 [-Force] [-TimeZone <TimeZoneInfo>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Export-CauReport` cmdlet 将一个或多个 “Updating Run” 报告导出为 HTML 或 CSV 格式的文档。每个 “Run” 报告都会汇总该 “Updating Run” 在节点级别和集群级别的运行状态。

使用 `Get-CauReport` cmdlet 并指定 **Detailed** 参数来获取一份或多份报告，并通过为该 cmdlet 指定适当的参数来控制报告中的内容。例如，**Last** 参数用于指定最近的一次更新操作（Updating Run）。

## 示例

#### 示例 1：获取指定集群的最新 CAU 报告的详细版本

```powershell
$CauReport = Get-CauReport -ClusterName "Contoso-FC1" -Last -Detailed
$CauReport | Export-CauReport -Format HTML -Path "C:\temp\contoso-fc1_last.html" -TimeZone ([system.timezoneinfo]::Utc)
```

此命令会获取名为“Contoso-FC1”的集群的最近一次CAU报告的详细内容，然后将该报告以HTML格式导出到路径`C:\temp\contoso-fc1_last.html`。报告中的时间戳采用协调世界时（UTC）进行显示。

## 参数

### -Confirm

在运行cmdlet之前会提示您确认是否要执行该操作。

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

### -Force

强制命令运行，而不需要用户确认。

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

### -Format

指定输出报告的格式。此参数可接受的值为：CSV 或 HTML。

```yaml
Type: OutputType
Parameter Sets: (All)
Aliases:
Accepted values: Csv, Html

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputReport

指定一个CAU报告对象的数组，这些对象可能是通过调用带有`Detailed`参数的`Get-CauReport`命令生成的。

```yaml
Type: CauReport[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PassThru

返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -Path

指定用于保存导出报告的文件的本地路径或完整路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TimeZone

指定报告时间戳的格式，以使其与指定的时区相匹配。

```yaml
Type: TimeZoneInfo
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft_clusterAwareUpdating.CauReport

## 输出

### Microsoft_clusterAwareUpdating.CauReport

## 备注

## 相关链接

[Get-CauReport](./Get-CauReport.md)

[Invoke-CauRun](./Invoke-CauRun.md)

