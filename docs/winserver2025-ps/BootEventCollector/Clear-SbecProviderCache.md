---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/clear-sbecprovidercache?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-SbecProviderCache
---

# 清除 Clear-SbecProviderCache 的缓存

## 摘要
清除供应商缓存。

## 语法

```
Clear-SbecProviderCache [<CommonParameters>]
```

## 描述
`Clear-SbecProviderCache` cmdlet 用于清除提供程序缓存。

下次您运行 `Get-SbecTraceProviders` cmdlet 时，该 cmdlet 会从操作系统重新读取这些提供者（providers），并更新缓存中的信息。

## 示例


## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的内容）。

## 输出

### 没有（需要处理的内容）。

## 备注

## 相关链接

[Get-SbecTraceProviders](./Get-SbecTraceProviders.md)

