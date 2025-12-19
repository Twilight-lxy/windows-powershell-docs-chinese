---
external help file: DDVCmdlets.dll-Help.xml
Module Name: Microsoft.DiagnosticDataViewer
online version: https://learn.microsoft.com/powershell/module/microsoft.diagnosticdataviewer/get-diagnosticstorecapacity?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DiagnosticStoreCapacity
---

# 获取诊断存储容量信息

## 摘要
获取当前的诊断数据存储容量。参数 \[-Size\] 以兆字节（MB）为单位返回诊断数据存储的容量；参数 \[-Time\] 以天为单位返回诊断数据存储的容量。默认的诊断数据存储容量为 1024 MB，默认的时间期限为 30 天。

## 语法

```
Get-DiagnosticStoreCapacity [-Size] [-Time] [<CommonParameters>]
```

## 描述
通过该工具可以显示的诊断数据历史记录的数量受到时间（以天为单位）和数据大小（以兆字节为单位）的限制。一旦达到任一限制条件（以先到达的条件为准），诊断数据将按照“先进先出”的原则被删除。例如，如果数据大小的限制是 1GB，而时间的限制是 30 天，那么当诊断数据存储量达到 1GB 时，或者最旧的记录已经存在了 30 天（以先发生的情况为准），系统就会删除该最旧的事件记录。

## 示例

### 示例 1
```
Get-DiagnosticStoreCapacity -Size
```

获取诊断存储的配置大小（以兆字节为单位）。

### 示例 2
```
Get-DiagnosticStoreCapacity -Time
```

获取诊断存储的配置时间容量（以小时为单位）。

## 参数

### -Size
获取诊断存储的配置大小（以兆字节为单位）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: s

Required: False
Position: Named
Default value: False
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Time
获取诊断存储的配置时间容量（以小时为单位）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: t

Required: False
Position: Named
Default value: False
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于通用参数（about_CommonParameters）的文档（链接：http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### System.Management.Automation.SwitchParameter
获取诊断存储的配置大小（以兆字节为单位）。

### System.Management.Automation.SwitchParameter
获取诊断存储的配置时间容量（以小时为单位）。

## 输出

### System.String
## 备注
需要 Windows 10 版本 17134（1803）或更高版本

## 相关链接
