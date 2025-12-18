---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: microsoft.windows.appbackgroundtask.commands.dll-Help.xml
Module Name: AppBackgroundTask
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appbackgroundtask/disable-appbackgroundtaskdiagnosticlog?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-AppBackgroundTaskDiagnosticLog
---

# 禁用应用后台任务诊断日志功能

## 摘要
禁用事件查看器中后台任务的日志记录功能。

## 语法

```
Disable-AppBackgroundTaskDiagnosticLog [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
` Disable-AppBackgroundTaskDiagnosticLog ` 这个 cmdlet 会禁用事件查看器（Event Viewer）中的后台任务日志记录功能。要禁用该功能，您必须具有管理员权限。

## 示例

#### 示例 1：禁用后台任务的日志记录
```
PS C:\> Disable-AppBackgroundTaskDiagnosticLog
```

这个命令会关闭事件查看器（Event Viewer）中的后台任务日志记录功能。

## 参数

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Enable-AppBackgroundTaskDiagnosticLog](./Enable-AppBackgroundTaskDiagnosticLog.md)

