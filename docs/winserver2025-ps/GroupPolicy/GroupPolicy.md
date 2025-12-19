---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.0.1
Locale: en-US
Module Guid: 03e49e3a-be77-4422-9d97-8fe355c2284c
Module Name: GroupPolicy
ms.date: 12/20/2016
title: GroupPolicy
---

# GroupPolicy模块

## 描述

这个主题简要介绍了用于在安装了远程服务器管理工具（RSAT）的Windows Server和Windows客户端中管理组策略的Windows PowerShell cmdlets。（RSAT包含了GPMC以及各种组策略相关的cmdlets。）

表格中的每个 cmdlet 都链接到了有关该 cmdlet 的更多信息。


## GroupPolicyCmdlets

### [备份GPO](./Backup-GPO.md)

备份一个GPO或域中的所有GPO。

### [复制GPO](./Copy-GPO.md)

复制一个组策略对象（GPO）。

### [Get-GPInheritance](./Get-GPInheritance.md)

获取指定域或组织单位（OU）的组策略继承信息。

### [Get-GPO](./Get-GPO.md)

可以获取一个GPO或域中的所有GPO。

### [Get-GPOReport](./Get-GPOReport.md)

为指定的组策略对象（GPO）或域中的所有组策略对象生成报告，报告可以以XML或HTML格式呈现。

### [Get-GPPermission](./Get-GPPermission.md)

获取指定GPO上一个或多个安全主体（security principal）的权限级别。

### [Get-GPPrefRegistryValue](./Get-GPPrefRegistryValue.md)

从一个GPO中的“计算机配置”或“用户配置”部分获取一个或多个注册表偏好设置项。

### [Get-GPRegistryValue](./Get-GPRegistryValue.md)

在组策略对象（GPO）中，“计算机配置”或“用户配置”下可以找到一个或多个基于注册表的策略设置。

### [Get-GPResultantSetOfPolicy](./Get-GPResultantSetOfPolicy.md)

将用户、计算机或两者的RSoP（运行状态概述）信息读写到文件中。

### [Get-GPStarterGPO](./Get-GPStarterGPO.md)

获取一个启动组策略对象（Starter GPO），或者获取域中的所有启动组策略对象。

### [Import-GPO](./Import-GPO.md)

将备份的组策略设置（GPO）导入到指定的目标组策略对象（GPO）中。

### [Invoke-GPUpdate](./Invoke-GPUpdate.md)

在指定的计算机上安排远程Group Policy刷新任务。

### [New-GPLink](./New-GPLink.md)

将组策略对象（GPO）链接到站点、域或组织单元（OU）。

### [New-GPO](./New-GPO.md)

创建一个组策略对象（Group Policy Object，简称GPO）。

### [New-GPStarterGPO](./New-GPStarterGPO.md)

创建一个起始组策略对象（Starter GPO）。

### [Remove-GPLink](./Remove-GPLink.md)

从站点、域或组织单元（OU）中删除GPO链接。

### [Remove-GPO](./Remove-GPO.md)

删除一个组策略对象（GPO）。

### [Remove-GPPrefRegistryValue](./Remove-GPPrefRegistryValue.md)

从一个GPO中的“计算机配置”或“用户配置”中删除一个或多个注册表偏好设置项。

### [Remove-GPRegistryValue](./Remove-GPRegistryValue.md)

从组策略对象（GPO）中的“计算机配置”或“用户配置”中删除一个或多个基于注册表的策略设置。

### [Rename-GPO](./Rename-GPO.md)

为组策略对象（GPO）分配一个新的显示名称。

### [ Restore-GPO](./Restore-GPO.md)

从一个或多个GPO备份文件中恢复一个GPO或域中的所有GPO。

### [Set-GPInheritance](./Set-GPInheritance.md)

允许或禁止指定域或组织单元继承相关设置。

### [Set-GPLink](./Set-GPLink.md)

设置指定的GPO链接的属性。

### [Set-GPPermission](./Set-GPPermission.md)

为某个安全主体授予针对一个GPO或域中所有GPO的相应权限级别。

### [Set-GPPrefRegistryValue](./Set-GPPrefRegistryValue.md)

在组策略对象（GPO）中，将某个注册表偏好设置项配置到“计算机配置”或“用户配置”下。

### [Set-GPRegistryValue](./Set-GPRegistryValue.md)

在组策略对象（GPO）中，通过“计算机配置”或“用户配置”选项来设置一个或多个基于注册表的策略项。


