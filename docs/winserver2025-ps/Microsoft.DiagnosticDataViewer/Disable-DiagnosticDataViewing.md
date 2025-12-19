---
external help file: DDVCmdlets.dll-Help.xml
Module Name: Microsoft.DiagnosticDataViewer
online version: https://learn.microsoft.com/powershell/module/microsoft.diagnosticdataviewer/disable-diagnosticdataviewing?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-DiagnosticDataViewing
---

# 禁用诊断数据查看功能

## 摘要
禁用诊断数据查看功能。

## 语法

```
Disable-DiagnosticDataViewing [<CommonParameters>]
```

## 描述
此 cmdlet 禁用了诊断数据的查看功能。一旦禁用了诊断数据的查看功能，该工具将抛出错误。请注意，禁用诊断数据的查看功能还会删除设备上现有的诊断数据记录。

## 示例

### 示例 1
```
Disable-DiagnosticDataViewing
```

禁用诊断数据查看功能。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

### System.String

## 备注
需要Windows 10版本17134（1803）或更高版本

## 相关链接

