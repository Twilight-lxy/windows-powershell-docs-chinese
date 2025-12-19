---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/get-iissharedconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IISSharedConfig
---

# 获取 IISSharedConfig 配置信息

## 摘要
获取IIS共享配置的状态信息。

## 语法

```
Get-IISSharedConfig [<CommonParameters>]
```

## 描述
`Get-IISSharedConfig` cmdlet 可以获取 IIS 共享配置功能的当前状态。

## 示例

### 示例 1：获取共享配置的状态
```
PS C:\> Get-IISSharedConfig
Enabled = True
Physical Path = C:\export
UserName = administrator
```

这个命令用于获取 IIS 共享配置的状态。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于(CommonParameters)（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[ Disable-IISSharedConfig](./Disable-IISSharedConfig.md)

[Enable-IISSharedConfig](./Enable-IISSharedConfig.md)

