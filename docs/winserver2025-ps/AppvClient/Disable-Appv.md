---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/disable-appv?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-Appv
---

# 禁用AppV功能

## 摘要
禁用App-V服务。

## 语法

```
Disable-Appv [<CommonParameters>]
```

## 描述
**Disable-Appv** cmdlet 可以在 Windows 10 周年纪念版计算机上禁用 Microsoft 应用虚拟化（App-V）服务。该 cmdlet 会阻止所有 App-V 应用程序从 App-V 服务器或 Configuration Manager 下载。如果操作成功，它会返回一条消息。为了使更改生效，您必须重新启动计算机。

## 示例

#### 示例 1：禁用 App-V 服务
```
PS C:\> Disable-Appv
```

这个命令会禁用App-V服务。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Enable-Appv](./Enable-Appv.md)

[Get-AppvStatus](./Get-AppvStatus.md)

