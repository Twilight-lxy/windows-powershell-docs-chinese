---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: microsoft.windows.appbackgroundtask.commands.dll-Help.xml
Module Name: AppBackgroundTask
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appbackgroundtask/set-appbackgroundtaskresourcepolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AppBackgroundTaskResourcePolicy
---

# 设置应用背景任务资源策略

## 摘要
配置后台任务对全局资源池的使用方式。

## 语法

```
Set-AppBackgroundTaskResourcePolicy -Mode <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AppBackgroundTaskResourcePolicy` cmdlet 用于配置后台任务对全局资源池的使用。全局资源池是一种共享资源，在应用程序需要额外资源来完成任务时，可以提供 CPU 或网络资源。要设置后台任务的资源策略，必须具有管理员权限。

## 示例

#### 示例 1：将全局资源策略设置为“保守”模式
```
PS C:\> Set-AppBackgroundTaskResourcePolicy -Mode Conservative
```

此命令将后台任务的全局资源策略设置为“Conservative”（保守模式），从而确保后台任务使用最少的CPU资源。

### 示例 2：将全局资源策略设置为“正常”模式
```
PS C:\> Set-AppBackgroundTaskResourcePolicy -Mode Normal
```

此命令将后台任务的全局资源策略设置为“Normal”（正常）。如果之前的设置是“Conservative”（保守的），则需要重新启动系统。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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

### -Mode
指定系统中后台任务的全局池设置。有效值为 Normal 和 Conservative。使用 Normal 可为所有应用程序启用全局池；使用 Conservative 可禁用所有应用程序的全局池。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Normal, Conservative

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

