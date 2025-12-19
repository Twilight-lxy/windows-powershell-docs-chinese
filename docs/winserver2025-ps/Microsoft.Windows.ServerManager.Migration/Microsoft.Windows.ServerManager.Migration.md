---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link:
Help Version:
Locale: en-US
Module Name: Microsoft.Windows.ServerManager.Migration
Module Guid: 00000000-0000-0000-0000-000000000000
ms.date: 01/03/2017
schema: 2.0.0
title: Microsoft.Windows.ServerManager.Migration
---
# Microsoft.Windows.ServerManager.Migration 模块

## 描述

此参考资料提供了所有服务器迁移 cmdlet 的描述和语法信息。这些 cmdlet 按其名称开头所使用的动词（即命令行为语）的字母顺序进行排列。

管理员可以使用 Windows PowerShell 中的 Windows Server 迁移工具（Windows Server Migration Tools）cmdlet，将服务器角色、功能、操作系统设置以及其他数据和共享资源迁移到运行最新版本 Windows Server 的计算机上。

## Microsoft.Windows.ServerManager.MigrationCmdlets

### [禁用 ServerManagerStandardUserRemoting 功能](Disable-ServerManagerStandardUserRemoting.md)

禁止指定的标准用户访问由服务器管理器为某台服务器收集的事件数据、服务信息、性能计数器数据以及角色和功能清单数据。

### [Enable-ServerManagerStandardUserRemoting](Enable-ServerManagerStandardUserRemoting.md)

通过使用 Server Manager，可以为一个服务器的一个或多个标准非管理员用户提供访问事件数据、服务数据、性能计数器数据以及角色和功能清单数据的权限。

### [Export-SmigServerSetting](Export-SmigServerSetting.md)

将本地计算机上选定的 Windows 功能和操作系统设置导出，并存储在迁移存储库中。

### [Get-SmigServerFeature](Get-SmigServerFeature.md)

获取可以从本地服务器或迁移存储中迁移的所有Windows功能的集合。

### [Get-WindowsFeature](Get-WindowsFeature.md)

获取有关指定服务器上可安装和已安装的 Windows Server 角色、角色服务以及功能的信息。

### [Import-SmigServerSetting](Import-SmigServerSetting.md)

从迁移存储库中导入选定的 Windows 功能和操作系统设置，并将它们应用到本地计算机上。

### [Install-WindowsFeature](Install-WindowsFeature.md)

在运行 Windows Server 2012 R2 的本地服务器或指定的远程服务器上，安装一个或多个角色、角色服务或功能。

### [Receive-SmigServerData](Receive-SmigServerData.md)

允许目标服务器接收从源服务器迁移过来的共享资源（包括文件夹、文件及其相关权限和共享属性）。在目标服务器上运行 `Receive-SmigServerData` 命令的同时，必须在源服务器上同时运行 `Send-SmigServerData` 命令。

### [Send-SmigServerData](Send-SmigServerData.md)

该命令可以将文件夹、文件及其关联的权限和共享属性从源服务器通过端口7000迁移到目标服务器。在源服务器上运行`Send-SmigServerData`命令的同时，必须在目标服务器上也运行`Receive-SmigServerData`命令。

### [Uninstall-WindowsFeature](Uninstall-WindowsFeature.md)

从运行 Windows Server 2012 R2 的计算机上卸载指定的 Windows Server 角色、角色服务及功能。
