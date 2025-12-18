---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: microsoft.windows.appbackgroundtask.commands.dll-Help.xml
Module Name: AppBackgroundTask
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appbackgroundtask/enable-appbackgroundtaskdiagnosticlog?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-AppBackgroundTaskDiagnosticLog
---

# 启用应用程序后台任务诊断日志功能

## 摘要
在事件查看器中启用后台任务日志记录功能。

## 语法

```
Enable-AppBackgroundTaskDiagnosticLog [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-AppBackgroundTaskDiagnosticLog` 这个 cmdlet 可以在事件查看器（Event Viewer）中启用后台任务的日志记录功能。要启用这一功能，您必须具有管理员权限。

## 示例

#### 示例 1：启用后台任务日志记录
```
PS C:\> Enable-AppBackgroundTaskDiagnosticLog
```

这个命令会在事件查看器中启用后台任务的日志记录功能。

## 参数

### -Confirm
在运行cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上该cmdlet并未被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Disable-AppBackgroundTaskDiagnosticLog](./Disable-AppBackgroundTaskDiagnosticLog.md)

