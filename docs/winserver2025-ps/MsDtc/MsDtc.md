---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.0.1
Locale: en-US
Module Guid: 52923875-f2e3-4ad2-8e0c-96c7b10e2e3d
Module Name: MsDtc
ms.date: 12/20/2016
title: MsDtc
---

# MsDtc 模块
## 描述
本参考资料提供了关于 Microsoft 分布式事务协调器（MSDTC）所提供的 Windows PowerShell cmdlet 的相关信息。本节中的 cmdlet 帮助主题按字母顺序排列。

## MsDtcCmdlets
### [Add-DtcClusterTMMapping](./Add-DtcClusterTMMapping.md)
添加一个集群DTC（诊断跟踪代码）映射关系。

### [Complete-DtcDiagnosticTransaction](./Complete-DtcDiagnosticTransaction.md)
如果指定的事务是根事务，则会调用提交（Commit）过程；否则，会在事务对象上调用完成（Complete）方法。

### [Get-Dtc](./Get-Dtc.md)
获取 DTC 实例。

### [Get-DtcAdvancedHostSetting](./Get-DtcAdvancedHostSetting.md)
查询注册表中DTC主机级别的属性。

### [Get-DtcAdvancedSetting](./Get-DtcAdvancedSetting.md)
查询注册表中关于 MSDTC（Microsoft Distributed Transaction Coordinator）的高级设置。

### [Get-DtcClusterDefault](./Get-DtcClusterDefault.md)
检索默认的集群服务器。

### [Get-DtcClusterTMMapping](./Get-DtcClusterTMMapping.md)
获取集群DTC映射数据。

### [Get-DtcDefault](./Get-DtcDefault.md)
获取默认的 DTC 实例。

### [Get-DtcLog](./Get-DtcLog.md)
获取DTC日志文件设置信息。

### [Get-DtcNetworkSetting](./Get-DtcNetworkSetting.md)
获取 DTC 的网络和安全配置设置。

### [Get-DtcTransaction](./Get-DtcTransaction.md)
获取有关由DTC实例处理的交易的信息。

### [Get-DtcTransactionsStatistics](./Get-DtcTransactionsStatistics.md)
获取交易摘要。

### [Get-DtcTransactionsTraceSession](./Get-DtcTransactionsTraceSession.md)
获取主机特定的 DTC 事务跟踪会话设置。

### [Get-DtcTransactionsTraceSetting](./Get-DtcTransactionsTraceSetting.md)
获取主机的 DTC 事务跟踪设置。

### [Install-Dtc](./Install-Dtc.md)
安装本地事务协调器。

### [Join-DtcDiagnostic ResourceManager](./Join-DtcDiagnosticResourceManager.md)
为某个事务对象（transaction object）分配一个用于诊断目的的资源管理器（Diagnostic Resource Manager）。

### [New-DtcDiagnosticTransaction](./New-DtcDiagnosticTransaction.md)
在本地计算机上的事务管理器中创建一个新的交易。

### [接收 DTC 诊断交易](./Receive-DtcDiagnosticTransaction.md)
从给定的诊断资源管理器（Diagnostic Resource Manager）传播一笔交易。

### [Remove-DtcClusterTMMapping](./Remove-DtcClusterTMMapping.md)
删除一个集群的DTC（诊断 trouble code）映射关系。

### [Reset-DtcLog](./Reset-DtcLog.md)
重置 DTC 实例的日志文件。

### [Send-DtcDiagnosticTransaction](./Send-DtcDiagnosticTransaction.md)
将一笔交易传播到指定的诊断资源管理器（Diagnostic Resource Manager）。

### [Set-DtcAdvancedHostSetting](./Set-DtcAdvancedHostSetting.md)
在注册表中设置DTC（诊断 trouble code）主机级别的属性。

### [Set-DtcAdvancedSetting](./Set-DtcAdvancedSetting.md)
在注册表中设置与DTC实例相关的特定属性。

### [Set-DtcClusterDefault](./Set-DtcClusterDefault.md)
设置集群的默认事务协调器。

### [Set-DtcClusterTMMapping](./Set-DtcClusterTMMapping.md)
修改现有的集群DTC映射（Cluster DTC Mapping）。

### [Set-DtcDefault](./Set-DtcDefault.md)
设置默认的交易协调器。

### [Set-DtcLog](./Set-DtcLog.md)
修改DTC实例的日志文件设置。

### [Set-DtcNetworkSetting](./Set-DtcNetworkSetting.md)
修改 DTC 实例的网络和安全配置。

### [Set-DtcTransaction](./Set-DtcTransaction.md)
修改事务的状态。

### [Set-DtcTransactionsTraceSession](./Set-DtcTransactionsTraceSession.md)
修改主机的DTC事务跟踪设置。

### [Set-DtcTransactionsTraceSetting](./Set-DtcTransactionsTraceSetting.md)
修改主机的DTC事务跟踪设置。

### [Start-Dtc](./Start-Dtc.md)
启动 DTC 实例。

### [Start-DtcDiagnostic ResourceManager](./Start-DtcDiagnostic ResourceManager.md)
启动一个用于诊断的资源管理器（Resource Manager）。

### [Start-DtcTransactionsTraceSession](./Start-DtcTransactionsTraceSession.md)
为主机启动一个新的DTC事务跟踪会话。

### [Stop-Dtc](./Stop-Dtc.md)
停止一个DTC实例。

### [Stop-DtcDiagnostic ResourceManager](./Stop-DtcDiagnosticResourceManager.md)
停止并移除一个诊断性的资源管理器（Resource Manager）作业。

### [Stop-DtcTransactionsTraceSession](./Stop-DtcTransactionsTraceSession.md)
停止主机上正在进行的DTC（Diagnostic Trouble Code）事务跟踪会话。

### [Test-Dtc](./Test-Dtc.md)
用于测试两台计算机是否能够参与联网交易。

### [Undo-DtcDiagnosticTransaction](./Undo-DtcDiagnosticTransaction.md)
对指定的事务调用“Abort”流程（即终止该事务的执行）。

### [Uninstall-Dtc](./Uninstall-Dtc.md)
卸载本地的交易协调器程序。

### [Write-DtcTransactionsTraceSession](./Write-DtcTransactionsTraceSession.md)
将来自活动中的DTC事务跟踪会话的数据写入日志文件。


