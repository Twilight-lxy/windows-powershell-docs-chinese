---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/start-iiscommitdelay?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-IISCommitDelay
---

# 启动 IIS 提交延迟（Start-IISCommitDelay）

## 摘要
指示 IIS 配置系统延迟对更改的确认（即推迟将这些更改应用到实际运行环境中）。

## 语法

```
Start-IISCommitDelay [<CommonParameters>]
```

## 描述
`Start-IISCommitDelay` cmdlet 命令用于指示 Internet Information Services (IIS) 配置系统延迟对更改的确认（即延迟将这些更改应用到实际运行环境中）。这些更改的确认过程会一直持续到 `Stop-IISCommitDelay` cmdlet 被执行为止。

## 示例

#### 示例 1：延迟提交更改
```
PS C:\> Start-IISCommitDelay
```

此命令会延迟对 IIS 配置设置的修改，直到执行 `Stop-IISCommitDelay` cmdlet 为止。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about	CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Stop-IISCommitDelay](./Stop-IISCommitDelay.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

