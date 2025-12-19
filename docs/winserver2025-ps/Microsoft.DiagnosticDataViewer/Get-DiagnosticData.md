---
external help file: DDVCmdlets.dll-Help.xml
Module Name: Microsoft.DiagnosticDataViewer
online version: https://learn.microsoft.com/powershell/module/microsoft.diagnosticdataviewer/get-diagnosticdata?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DiagnosticData
---

# 获取诊断数据

## 摘要
获取该机器上传的历史Windows诊断数据。

## 语法

```
Get-DiagnosticData [[-StartTime] <DateTime>] [[-EndTime] <DateTime>] [[-RecordCount] <Int32>]
 [-DiagnosticDataType <Int32>] [-BasicTelemetryOnly] [<CommonParameters>]
```

## 描述
此cmdlet用于获取该机器上传的历史Windows诊断数据。可用的历史数据总量受到诊断数据存储配置的限制。如需更改相关设置，请参阅“Set-DiagnosticStoreCapacity”。

## 示例

### 示例 1
```
Get-DiagnosticData -StartTime (Get-Date).AddDays(-1) -RecordCount 1
```

返回自昨天以来最早的（最旧的）诊断事件。以下是示例输出。

名称：Microsoft.Windows.Kernel.PnP DeviceConfig

时间戳：2018年11月8日下午4:52:53

有效载荷（Payload）：JSON 格式的有效载荷数据

IsBasic: False

DiagnosticDataTypes: {11}

### 示例 2
```
Get-DiagnosticData -StartTime (Get-Date).AddHours(-12) -EndTime (Get-Date).AddHours(-6) -BasicTelemetryOnly
```

返回所有在12小时到6小时前之间发送的基本诊断事件。

### 示例 3
```
Get-DiagnosticData -DiagnosticDataType 11
```

返回标记有诊断数据类型ID 11的诊断事件。有关诊断数据类型的列表，请参阅Get-DiagnosticDataTypes。

## 参数

### -StartTime
查询过滤参数：用于指定获取的数据集中最旧事件的窗口起始时间。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases: st, start

Required: False
Position: 0
Default value: 1/1/0001 12:00:00 AM
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -EndTime
查询过滤参数：用于指定获取的数据集中最新事件的窗口结束时间。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases: et, end

Required: False
Position: 1
Default value: 12/31/9999 11:59:59 PM
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -RecordCount
指定要获取的最大事件数量。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases: rc, recCount, c, count

Required: False
Position: 2
Default value: 0
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -DiagnosticDataType
查询过滤器参数：用于指定结果集是否仅应包含具有该诊断数据类型的事件。有关数据类型ID的信息，请参阅Get-DiagnosticDataTypes。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases: ddt, dt

Required: False
Position: Named
Default value: -2147483648
Accept pipeline input: False
Accept wildcard characters: False
```

### -BasicTelemetryOnly
查询过滤器参数：用于指定结果集是否仅应包含基本诊断数据事件。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: basic, basicOnly

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONPARAMETERS（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### System DateTime
查询过滤参数：用于指定获取的数据集中最旧事件的窗口起始时间。

### System DateTime
查询过滤参数：用于指定获取的数据集中最新事件的窗口结束时间。

### System.Int32
指定要获取的最大事件数量。

## 输出

### DDVCmdlets.Containers.EventRecord
已保存的事件记录。

## 备注
需要Windows 10版本17134（1803）或更高版本

## 相关链接
[关于Windows诊断数据](/windows/privacy/windows-diagnostic-data)
