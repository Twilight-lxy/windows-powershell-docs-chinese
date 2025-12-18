---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.0.1
Locale: en-US
Module Guid: 4e804861-1dce-46c1-868d-c8f2ab9d220a
Module Name: ClusterAwareUpdating
ms.date: 09/27/2022
title: ClusterAwareUpdating
---

# ClusterAwareUpdating 模块

## 描述

这个参考资料提供了所有与“Cluster-Aware Updating”功能相关的cmdlet的描述和语法信息。这些cmdlet按照它们开头所使用的动词（即命令的操作部分）按字母顺序排列。

## ClusterAwareUpdatingCmdlets

### [Add-CauClusterRole](Add-CauClusterRole.md)

为指定的集群添加CAU（Clustered Authentication Unit）集群角色，该角色提供了自更新功能。

### [Disable-CauClusterRole]( Disable-CauClusterRole.md)

暂停指定集群上的自动更新功能。

### [Enable-CauClusterRole](Enable-CauClusterRole.md)

重新启用指定集群上的自动更新功能。

### [Export-CauReport](Export-CauReport.md)

将一份或多份“更新运行”报告导出为HTML或CSV格式的文档。

### [Get-CauClusterRole](Get-CauClusterRole.md)

获取指定集群上CAU集群角色的配置属性。

### [Get-CauDeviceInfoForFeatureUpdates](Get-CauDeviceInfoForFeatureUpdates.md)

从指定的目录中检索设备信息，以便进行功能更新。

### [Get-CauPlugin](Get-CauPlugin.md)

获取有关在本地计算机上注册的一个或多个软件更新插件的信息。

### [Get-CauReport](Get-CauReport.md)

获取所有已知更新运行的报告，或者获取符合指定日期或其他指定参数的所有更新运行的报告。

### [Get-CauRun](Get-CauRun.md)

获取关于当前正在进行的更新运行的状态信息。

### [Get-ClusterlessCauRun](Get-ClusterlessCauRun.md)

检索与某个集群无关的“Cluster-Aware Updating”（CAU）运行相关的信息。

### [Invoke-CauRun](Invoke-CauRun.md)

对集群节点进行扫描，查找可应用的更新，并通过在该指定集群上执行的“更新运行”（Updating Run）来安装这些更新。

### [Invoke-CauScan](Invoke-CauScan.md)

扫描集群节点以查找可应用的更新，并获取将应用于指定集群中每个节点的初始更新列表。

### [Invoke-ClusterlessCauRun](Invoke-ClusterlessCauRun.md)

在一组未与任何集群关联的节点上执行集群感知更新（Cluster-Aware Updating, CAU）操作。

### [Register-CauPlugin](Register-CauPlugin.md)

在本地计算机上注册一个用于更新CAU软件的插件。

### [Remove-CauClusterRole](Remove-CauClusterRole.md)

从指定的故障转移集群中移除CAU集群角色。

### [Save-CauDebugTrace](Save-CauDebugTrace.md)

将中国农业大学（CAU）的调试追踪信息保存到本地ZIP文件中。

### [Set-CauClusterRole](Set-CauClusterRole.md)

为指定集群上的CAU（Clustered Application Utility）集群角色设置配置属性。

### [Stop-CauRun](Stop-CauRun.md)

停止集群上正在进行的更新操作。

### [Test-CauSetup](Test-CauSetup.md)

用于测试集群是否已正确配置，以便使用CAU（Cluster Application Update）应用软件更新。

### [Unregister-CauPlugin](Unregister-CauPlugin.md)

从CAU使用的插件列表中移除一个用于软件更新的插件。
