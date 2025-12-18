---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.0.1
Locale: en-US
Module Guid: c3f81f5f-6555-43cb-802a-aef7aa5a11cb
Module Name: DFSR
ms.date: 12/20/2016
title: DFSR
---

# DFSR模块
## 描述
此参考资料提供了所有分布式文件系统（DFS）复制相关cmdlet的描述和语法信息。这些cmdlet按照它们开头所使用的动词（即命令操作）的字母顺序进行排列。

## DFSRCmdlets
### [Add-DfsrConnection](./Add-DfsrConnection.md)
在复制组的成员之间建立连接。

### [Add-DfsrMember](./Add-DfsrMember.md)
将计算机添加到复制组中。

### [ConvertFrom-DfsrGuid](./ConvertFrom-DfsrGuid.md)
将给定复制组中的GUID转换为友好的名称（即易于理解的字符串）。

### [Export-DfsrClone](./Export-DfsrClone.md)
导出克隆后的DFS复制数据库和卷配置设置。

### [Get-DfsrBacklog](./Get-DfsrBacklog.md)
检索两个DFS复制伙伴之间待处理的文件更新列表。

### [Get-DfsrCloneState](./Get-DfsrCloneState.md)
获取数据库克隆操作的状态。

### [Get-DfsrConnection](./Get-DfsrConnection.md)
在DFS复制合作伙伴之间建立连接。

### [Get-DfsrConnectionSchedule](./Get-DfsrConnectionSchedule.md)
获取复制组成员之间的连接调度信息。

### [Get-DfsrDelegation](./Get-DfsrDelegation.md)
获取具有复制组权限的主体（principals）。

### [Get-DfsReplicatedFolder](./Get-DfsReplicatedFolder.md)
从一个复制组中获取一个已复制的文件夹。

### [Get-DfsReplicationGroup](./Get-DfsReplicationGroup.md)
检索一个复制组。

### [Get-DfsrFileHash](./Get-DfsrFileHash.md)
获取一个文件哈希值。

### [Get-DfsrGroupSchedule](./Get-DfsrGroupSchedule.md)
检索复制组的调度信息。

### [Get-DfsrIdRecord](./Get-DfsrIdRecord.md)
从DFS复制数据库中获取已复制文件或文件夹的ID记录。

### [Get-DfsrMember](./Get-DfsrMember.md)
获取复制组中的成员计算机。

### [Get-DfsrMembership](./Get-Dfsr Membership.md)
获取复制组中成员的会员设置信息。

### [Get-DfsrPreservedFiles](./Get-DfsrPreservedFiles.md)
获取DFS复制之前保存的文件和文件夹列表。

### [Get-DfsrServiceConfiguration](./Get-DfsrServiceConfiguration.md)
获取组成员上DFS复制服务的设置信息。

### [Get-DfsrState](./Get-DfsrState.md)
获取成员的DFS复制状态。

### [Grant-DfsrDelegation](./Grant-DfsrDelegation.md)
为复制组的安全主体授予相应的权限。

### [Import-DfsrClone](./Import-DfsrClone.md)
导入克隆的DFS复制数据库和卷配置设置。

### [New-DfsReplicatedFolder](./New-DfsReplicatedFolder.md)
在复制组中创建一个被复制的文件夹。

### [New-DfsReplicationGroup](./New-DfsReplicationGroup.md)
创建一个复制组。

### [Remove-DfsrConnection](./Remove-DfsrConnection.md)
删除复制组中成员之间的连接。

### [Remove-DfsReplicatedFolder](./Remove-DfsReplicatedFolder.md)
从一个复制组中删除一个已复制的文件夹。

### [Remove-DfsReplicationGroup](./Remove-DfsReplicationGroup.md)
删除一个复制组。

### [Remove-DfsrMember](./Remove-DfsrMember.md)
将计算机从复制组中移除。

### [Remove-DfsrPropagationTestFile](./Remove-DfsrPropagationTestFile.md)
删除DFS复制传播测试文件。

### [Reset-DfsrCloneState](./Reset-DfsrCloneState.md)
取消克隆操作。

### [Restore-DfsrPreservedFiles](./Restore-DfsrPreservedFiles.md)
恢复之前由DFS复制功能保存的文件和文件夹。

### [Revoke-DfsrDelegation](./Revoke-DfsrDelegation.md)
撤销复制组中安全主体（security principals）的权限。

### [Set-DfsrConnection](./Set-DfsrConnection.md)
更改复制组中成员之间连接的设置。

### [Set-DfsrConnectionSchedule](./Set-DfsrConnectionSchedule.md)
用于更改复制组中成员之间连接调度的相关设置。

### [Set-DfsReplicatedFolder](./Set-DfsReplicatedFolder.md)
更改已复制文件夹的设置。

### [Set-DfsReplicationGroup](./Set-DfsReplicationGroup.md)
修改一个复制组。

### [Set-DfsrGroupSchedule](./Set-DfsrGroupSchedule.md)
修改复制组的计划（即复制组的工作时间安排）。

### [Set-DfsrMember](./Set-DfsrMember.md)
修改复制组中成员计算机的信息。

### [Set-DfsrMembership](./Set-DfsrMembership.md)
配置复制组成员的成员资格设置。

### [Set-DfsrServiceConfiguration](./Set-DfsrServiceConfiguration.md)
修改DFS复制服务的设置。

### [Start-DfsrPropagationTest](./Start-DfsrPropagationTest.md)
在复制的文件夹中创建一个用于测试传播效果的文件。

### [Suspend-DfsReplicationGroup](./Suspend-DfsReplicationGroup.md)
无论原定计划如何，都会暂停计算机之间的数据复制（即阻止数据在两台计算机之间传输）。

### [Sync-DfsReplicationGroup](./Sync-DfsReplicationGroup.md)
无论计划如何，都能在计算机之间同步复制过程。

### [Update-DfsrConfigurationFromAD](./Update-DfsrConfigurationFromAD.md)
启动DFS复制服务的更新过程。

### [Write-DfsrHealthReport](./Write-DfsrHealthReport.md)
生成深度优先搜索（DFS）复制健康状况报告。

### [Write-DfsrPropagationReport](./Write-DfsrPropagationReport.md)
为复制组中的传播测试文件生成报告。


