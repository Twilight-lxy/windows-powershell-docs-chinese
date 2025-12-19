---
description: 该原因会导致 Windows 本地管理员密码解决方案（LAPS）立即为当前管理的本地账户更新其密码。
external help file: lapspsh.dll-Help.xml
Module Name: LAPS
online version: https://learn.microsoft.com/powershell/module/laps/reset-lapspassword?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
Locale: en-US
ms.date: 04/10/2023
title: Reset-LapsPassword
---

# 重置Laps密码

## 摘要
该设置会导致 Windows 本地管理员密码解决方案（Local Administrator Password Solution，简称 LAPS）立即为当前管理的本地账户更改其密码。

## 语法

```
Reset-LapsPassword [<CommonParameters>]
```

## 描述

`Reset-LapsPassword` cmdlet 命令会指示 LAPS 立即更改当前管理的本地账户的密码。此操作无论当前密码的状态如何都会执行，也就是说，当前密码是否已经过期并不会影响该命令的执行。

> [!重要!] > 该cmdlet仅适用于需要立即更改密码的罕见情况，例如作为对机器安全漏洞响应的措施。 > 不建议频繁使用此cmdlet。

该cmdlet不会返回关于操作结果的详细信息。有关如何查询事件日志条目以获取操作具体结果的更多信息，请参阅[使用Windows LAPS事件日志](https://go.microsoft.com/fwlink/?linkid=2234103)。

## 示例

### 示例 1

```powershell
Reset-LapsPassword
```

这个示例会强制立即旋转（更新）被管理的本地账户。

## 参数

### CommonParameters

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Windows LAPS概述](https://go.microsoft.com/fwlink/?linkid=2233901)
