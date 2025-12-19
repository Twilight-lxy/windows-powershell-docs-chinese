---
external help file: DDVCmdlets.dll-Help.xml
Module Name: Microsoft.DiagnosticDataViewer
online version: https://learn.microsoft.com/powershell/module/microsoft.diagnosticdataviewer/get-diagnosticdataviewingsetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DiagnosticDataViewingSetting
---

# 获取诊断数据查看设置

## 摘要
用于获取当前是否启用了诊断数据查看功能。

## 语法

```
Get-DiagnosticDataViewingSetting [<CommonParameters>]
```

## 描述
此cmdlet用于返回诊断数据查看的当前状态。该状态表明是否为该设备启用了诊断数据查看功能；如果未启用，则此工具会抛出错误。

## 示例

### 示例 1
```
Get-DiagnosticDataViewingSetting
```

检查是否启用了诊断数据查看功能。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

### System.String
## 备注
需要 Windows 10 版本 17134（1803）或更高版本。## 相关链接
