---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/start-sbecinstance?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-SbecInstance
---

# 启动 SbecInstance

## 摘要
启动“设置与启动事件收集器”服务。

## 语法

```
Start-SbecInstance [-Service] [-PassThru] [<CommonParameters>]
```

## 描述
`Start-SbecInstance` cmdlet 用于启动 Setup and Boot Event Collector 服务。

您必须具有内置管理员权限才能运行此命令。

## 示例

### 示例 1：启动启动事件收集器
```
PS C:\> Start-SbecInstance -Service
```

这个命令用于启动“Boot Event Collector”服务。

## 参数

### -PassThru
返回一个表示已启动服务的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Service
在当前计算机上启动设置程序和BEC服务。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的内容）。

## 输出

### System.ServiceProcess.ServiceController

## 备注

## 相关链接

[Get-SbecActiveConfig](./Get-SbecActiveConfig.md)

[Set-SbecActiveConfig](./Set-SbecActiveConfig.md)

[Stop-SbecInstance](./Stop-SbecInstance.md)

[Test-SbecActiveConfig](./Test-SbecActiveConfig.md)

