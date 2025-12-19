---
external help file: DDVCmdlets.dll-Help.xml
Module Name: Microsoft.DiagnosticDataViewer
online version: https://learn.microsoft.com/powershell/module/microsoft.diagnosticdataviewer/set-diagnosticstorecapacity?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DiagnosticStoreCapacity
---

# 设置诊断存储容量

## 摘要
设置诊断数据的存储时间和存储容量。

## 语法

```
Set-DiagnosticStoreCapacity [[-Size] <UInt32>] [[-Time] <UInt32>] [<CommonParameters>]
```

## 描述
此 cmdlet 设置了通过该工具可以显示的诊断数据历史记录的最大数量（按时间和大小划分）。大小限制以兆字节为单位，时间限制以天为单位。一旦达到任一限制（以先到达者为准），诊断数据历史记录将按照“先进先出”的顺序被删除。

## 示例

### 示例 1
```
Set-DiagnosticStoreCapacity -Size 1024
```

设置诊断存储器的容量（以兆字节为单位）。

### 示例 2
```
Set-DiagnosticStoreCapacity -Time 24
```

设置诊断存储的时间容量（以小时为单位）。

### 示例 3
```
Set-DiagnosticStoreCapacity -Size 1024 -Time 24
```

同时设置诊断存储器的容量（以兆字节为单位）和存储时间（以小时为单位）。

## 参数

### -Size
设置诊断存储的容量大小。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: s

Required: False
Position: 0
Default value: 0
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Time
设置诊断存储的时间容量。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: t

Required: False
Position: 1
Default value: 0
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于公有参数（about_CommonParameters）的文档（链接：http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### System.UInt32
设置诊断存储的容量大小。

### System.UInt32
设置诊断存储的时间容量。

## 输出

### System.String
## 备注
需要使用 Windows 10 的 17134（1803）版本或更高版本。

## 相关链接
