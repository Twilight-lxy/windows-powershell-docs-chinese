---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/enable-appv?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-Appv
---

# 启用 AppV 功能

## 摘要
启用App-V服务。

## 语法

```
Enable-Appv [<CommonParameters>]
```

## 描述
`Enable-Appv` cmdlet 可以在运行至少 Windows 10 Anniversary Edition（版本 1607）的计算机上启用 Microsoft 应用虚拟化（App-V）服务。如果此 cmdlet 成功执行，它会返回一条消息。

在启用 App-V 服务之前，请使用 Windows PowerShell 或组策略来配置 App-V 服务的设置。

## 示例

#### 示例 1：启用该服务
```
PS C:\> Enable-Appv
```

此命令用于启用App-V服务。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[disable-Appv](./Disable-Appv.md)

[Get-AppvStatus](./Get-AppvStatus.md)

