---
description: 这会导致 Windows 本地管理员密码解决方案（LAPS）处理当前配置的政策。
external help file: lapspsh.dll-Help.xml
Module Name: LAPS
online version: https://learn.microsoft.com/powershell/module/laps/invoke-lapspolicyprocessing?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
Locale: en-US
ms.date: 04/10/2023
title: Invoke-LapsPolicyProcessing
---

# 调用LapsPolicyProcessing函数

## 摘要
这会导致 Windows 本地管理员密码解决方案（LAPS）处理当前配置的策略。

## 语法

```
Invoke-LapsPolicyProcessing [<CommonParameters>]
```

## 描述

`Invoke-LapsPolicyProcessing` cmdlet 告诉 LAPS 处理当前配置的策略。

该cmdlet不会返回有关操作结果的详细信息。有关如何查询事件日志条目以获取操作结果的具体信息的更多内容，请参阅[使用Windows LAPS事件日志](https://go.microsoft.com/fwlink/?linkid=2234103)。

## 示例

### 示例 1

```powershell
Invoke-LapsPolicyProcessing
```

这个示例启动了对已配置的LAPS策略的处理流程。

## 参数

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Windows LAPS概述](https://go.microsoft.com/fwlink/?linkid=2233901)
