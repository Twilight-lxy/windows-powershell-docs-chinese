---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/stop-vmtrace?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-VMTrace
---

# 停止虚拟机跟踪（Stop-VMTrace）

## 摘要
停止对文件的追踪（或：停止对该文件的进一步分析/处理）。

## 语法

```
Stop-VMTrace [<CommonParameters>]
```

## 描述
**Stop-VMTrace** cmdlet 停止将追踪数据写入文件的过程。

## 示例

### 示例 1：停止跟踪
```
PS C:\> Stop-VMTrace
```

这个命令会停止跟踪操作。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[开始虚拟机追踪](./Start-VMTrace.md)

