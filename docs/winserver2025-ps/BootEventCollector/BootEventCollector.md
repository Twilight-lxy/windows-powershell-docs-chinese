---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.0.2
Locale: en-US
Module Guid: 7e4c6113-1789-4c2d-abaa-bea1ef5c62e8
Module Name: BootEventCollector
ms.date: 12/20/2016
title: BootEventCollector
---

# BootEventCollector 模块
## 描述
“Boot Event Collector”模块包含了一些cmdlet（命令脚本），可帮助您在Windows Server 2016技术预览版中管理与该模块相关的任务。

## BootEventCollectorCmdlets
### [Checkpoint-SbecActiveConfig](./Checkpoint-SbecActiveConfig.md)
创建一个配置检查点。

### [Clear-SbecProviderCache](./Clear-SbecProviderCache.md)
清除提供商的缓存。

### [ Disable-SbecAutologger](./Disable-SbecAutologger.md)
在 AutoLogger 设置中，禁用将事件转发到“设置和启动事件收集器”（Setup and Boot Event Collector）的功能。

### [ Disable-SbecBcd](./Disable-SbecBcd.md)
在BCD设置中禁用事件转发模式。

### [Enable-SbecAutologger](./Enable-SbecAutologger.md)
在 AutoLogger 设置中，启用将事件转发到 Setup 和 Boot 事件收集器的功能。

### [Enable-SbecBcd](./Enable-SbecBcd.md)
在BCD设置中启用并配置事件转发模式。

### [Enable-SbecBootImage](./Enable-SbecBootImage.md)
在离线的WinPE安装镜像中启用AutoLogger设置。

### [Enable-SbecWdsBcd](./Enable-SbecWdsBcd.md)
允许在导入到 WDS 服务器中的离线启动镜像中配置 BCD（二进制编码十进制）设置。

### [Get-SbecActiveConfig](./Get-SbecActiveConfig.md)
从正在运行的设置和启动事件收集器中获取当前活动的配置信息。

### [Get-SbecBackupConfig](./Get-SbecBackupConfig.md)
获取可用于恢复的备份配置文件。

### [Get-SbecDestination](./Get-SbecDestination.md)
获取目的地的数据文件。

### [Get-SbecForwarding](./Get-SbecForwarding.md)
获取当前的连接信息以及数据转发的方式。

### [Get-SbecHistory](./Get-SbecHistory.md)
获取连接状态变化的最新历史记录。

### [Get-SbecLocalization](./Get-Sbec.Localization.md)
获取一个本地化的消息字符串。

### [Get-SbecLogSession](./Get-SbecLogSession.md)
获取运行日志会话记录。

### [Get-SbecTraceProviders](./Get-SbecTraceProviders.md)
获取 ETW（事件跟踪）提供程序。

### [New-SbecUnattendFragment](./New-SbecUnattendFragment.md)
为 Unattend.xml 创建一个片段，其中包含安装后的命令。

### [Redo-SbecActiveConfig](./Redo-SbecActiveConfig.md)
重做对当前活动配置所做的更改。

### [ Restore-SbecBackupConfig](./Restore-SbecBackupConfig.md)
从备份文件中恢复配置。

### [Save-SbecInstance](./Save-SbecInstance.md)
将内存缓冲区中的数据写入磁盘。

### [Save-SbecLogSession](./Save-SbecLogSession.md)
将日志会话中的缓冲区数据刷新到磁盘上。

### [Set-SbecActiveConfig](./Set-SbecActiveConfig.md)
为正在运行的设置和启动事件收集器（Setup and Boot Event Collector）设置新的活动配置（active configuration）。

### [Set-SbecLogSession](./Set-SbecLogSession.md)
更新日志会话的设置。

### [启动Sbec实例](./Start-SbecInstance.md)
启动“设置与引导事件收集器”服务。

### [Start-SbecLogSession](./Start-SbecLogSession.md)
开始一个ETW日志会话。

### [Start-SbecNtKernelLogSession](./Start-SbecNtKernelLogSession.md)
启动一个 NT 内核日志记录会话，并将事件转发到收集器（Collector）。

### [Start-SbecSimpleLogSession](./Start-SbecSimpleLogSession.md)
开始一个日志会话，并将事件转发给收集器（Collector）。

### [Stop-SbecInstance](./Stop-SbecInstance.md)
停止设置过程及启动事件收集器的运行。

### [停止 SbecLogSession 会话](./Stop-SbecLogSession.md)
停止一个日志会话。

### [Test-SbecActiveConfig](./Test-SbecActiveConfig.md)
测试当前的启动事件收集器（Boot Event Collector）配置。

### [Test-SbecConfig](./Test-SbecConfig.md)
验证配置的正确性。

### [Undo-SbecActiveConfig](./Undo-SbecActiveConfig.md)
将更改恢复到当前使用的配置状态。



