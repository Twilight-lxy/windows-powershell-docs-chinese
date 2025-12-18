---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/get-appxlasterror?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppxLastError
---

# Get-AppxLastError

## 摘要
获取应用程序包安装日志中报告的最后一个错误信息。

## 语法

```
Get-AppxLastError [<CommonParameters>]
```

## 描述

`Get-AppxLastError` cmdlet 可以获取当前 Windows PowerShell 会话中应用程序包安装日志中报告的最后一个错误。应用程序包的文件扩展名为 `.msix` 或 `.appx`。

## 示例

#### 示例 1：获取最后一个错误

```powershell
Get-AppxLastError
```

这个命令用于获取应用程序安装日志中报告的最后一条错误信息。

## 参数

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Diagnostics.Eventing.Reader.EventLogRecord

## 备注

## 相关链接

[包管理器 API](https://go.microsoft.com/fwlink/?LinkId=245447)

[如何部署应用程序包](https://go.microsoft.com/fwlink/?LinkID=231020)

[Get-AppxPackage](./Get-AppxPackage.md)

[Get-AppxPackageManifest](./Get-AppxPackageManifest.md)

[Get-AppxLog](./Get-AppxLog.md)
