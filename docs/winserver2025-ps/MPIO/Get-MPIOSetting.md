---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Mpio-help.xml
Module Name: MPIO
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/mpio/get-mpiosetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-MPIOSetting
---

# 获取 MPIO 设置

## 摘要
获取 MPIO 设置信息。

## 语法

```
Get-MPIOSetting [<CommonParameters>]
```

## 描述
`Get-MPIOSetting` cmdlet 用于获取 Microsoft 多路径输入/输出（MPIO）的设置。这些设置包括以下内容：

- PathVerificationState
- PathVerificationPeriod
- PDORemovePeriod
- RetryCount
- RetryInterval
- UseCustomPathRecoveryTime
- CustomPathRecoveryTime
- DiskTimeoutValue

You can use the **Set-MPIOSetting** cmdlet to change these values.

## 示例

### Example 1: Get MPIO settings
```
PS C:\> Get-MPIOSetting
PathVerificationState     : Disabled
PathVerificationPeriod    : 30
PDORemovePeriod           : 20
RetryCount                : 3
RetryInterval             : 1
UseCustomPathRecoveryTime : Disabled
CustomPathRecoveryTime    : 40
DiskTimeoutValue          : 120
```

这个命令用于获取MPIO（多路径I/O）的相关设置信息。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Set-MPIOSetting](./Set-MPIOSetting.md)

