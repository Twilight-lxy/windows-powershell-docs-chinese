---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.0.1
Locale: en-US
Module Guid: 80cb11cf-96b5-4d48-84bd-f85f65de78ae
Module Name: EventTracingManagement
ms.date: 01/05/2017
title: EventTracingManagement
---

# 事件追踪管理模块
## 描述
本参考资料提供了针对事件跟踪管理（Event Tracing Management）特定命令集的cmdlet描述及其语法信息。这些cmdlet按照它们开头所使用的动词字母顺序进行排列。

## EventTracingManagementCmdlets
### [Add-EtwTraceProvider](./Add-EtwTraceProvider.md)
将一个 ETW（事件跟踪）跟踪提供程序添加到 ETW 跟踪会话或 AutoLogger 会话配置中。

### [Get-AutologgerConfig](./Get-AutologgerConfig.md)
列出现有的AutoLogger会话配置。

### [Get-EtwTraceProvider](./Get-EtwTraceProvider.md)
列出现有的AutoLogger会话配置。

### [Get-EtwTraceSession](./Get-EtwTraceSession.md)
枚举系统上的 ETW（Event Tracking Wizard）会话。

### [New-AutologgerConfig](./New-AutologgerConfig.md)
在注册表中创建一个自动记录器会话配置。

### [New-EtwTraceSession](./New-EtwTraceSession.md)
创建一个 ETW 跟踪会话（ETW trace session）。

### [Remove-AutologgerConfig](./Remove-AutologgerConfig.md)
从注册表中删除指定的AutoLogger会话配置信息。

### [Remove-EtwTraceProvider](./Remove-EtwTraceProvider.md)
从 ETW（Event Tracing for Windows）或 AutoLogger 会话中移除一个 ETW 提供者。

### [Save-EtwTraceSession](./Save-EtwTraceSession.md)
将ETW会话收集到的事件保存到.etl文件中。

### [Send-EtwTraceSession](./Send-EtwTraceSession.md)
将指定ETW会话的日志文件发送到目标位置。

### [Set-EtwTraceProvider](./Set-EtwTraceProvider.md)
在 ETW 或 AutoLogger 会话中修改提供者的启用设置。

### [开始 ETWTraceSession 会话](./Start-EtwTraceSession.md)
使用指定的名称和设置启动一个ETW会话。

### [Stop-EtwTraceSession](./Stop-EtwTraceSession.md)
停止指定的 ETW（Events Tracking Writer）会话。

### [更新自动记录器配置](Update-AutologgerConfig.md)
修改现有的AutoLogger会话配置。

### [Update-EtwTraceSession](Update-EtwTraceSession.md)
修改现有的 ETW 会话。


