---
external help file: DDVCmdlets.dll-Help.xml
Module Name: Microsoft.DiagnosticDataViewer
online version: https://learn.microsoft.com/powershell/module/microsoft.diagnosticdataviewer/enable-diagnosticdataviewing?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-DiagnosticDataViewing
---

# 启用诊断数据查看功能

## 摘要
启用诊断数据查看功能。

## 语法

```
Enable-DiagnosticDataViewing [<CommonParameters>]
```

## 描述
此cmdlet允许查看诊断数据。一旦启用，设备将开始记录所有上传到Microsoft的诊断数据事件；这些数据的总存储量受到诊断数据存储容量的限制。因此，可能需要一些时间才能看到所有的事件记录。

## 示例

### 示例 1
```
Enable-DiagnosticDataViewing
```

启用诊断数据查看功能。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONPARAMETERS（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

### System.String
## 备注
需要 Windows 10 的 17134（1803）版本或更高版本

## 相关链接
