---
external help file: DDVCmdlets.dll-Help.xml
Module Name: Microsoft.DiagnosticDataViewer
online version: https://learn.microsoft.com/powershell/module/microsoft.diagnosticdataviewer/get-diagnosticdatatypes?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DiagnosticDataTypes
---

# Get-DiagnosticDataTypes

## 摘要
获取诊断数据类型标识符与其相应描述的映射关系。

## 语法

```
Get-DiagnosticDataTypes [<CommonParameters>]
```

## 描述
此cmdlet显示了诊断数据类型标识符与其官方描述之间的对应关系。每个诊断数据事件都会根据微软对数据的处理方式被归类到相应的数据类型中。描述信息的加载可能需要一些时间。

## 示例

### 示例 1
```
Get-DiagnosticDataTypes
```

获取Windows诊断数据的相关类型信息。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### DDVCmdlets.Containers.DiagnosticDataType
诊断数据类型信息。

## 备注
需要 Windows 10 的 17134（1803）版本或更高版本

## 相关链接

[关于Windows诊断数据](/windows/privacy/windows-diagnostic-data)
