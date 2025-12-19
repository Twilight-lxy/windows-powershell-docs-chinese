---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.0.1
Locale: en-US
Module Guid: 53e1c251-4283-4b07-ab02-fc492c7ab8c5
Module Name: iSCSI
ms.date: 12/20/2016
title: iSCSI
---

# iSCSI模块
## 描述
此参考提供了所有针对 iSCSI 启动器（iSCSI Initiator）的 cmdlet 的描述和语法。这些 cmdlet 按照其开头命令动词的字母顺序进行排列。

## iSCSI cmdlet（命令行工具）
### [Connect-IscsiTarget](./Connect-IscsiTarget.md)
在本地 iSCSI 发起方和 iSCSI 目标设备之间建立连接。

### [ Disconnect-IscsiTarget](./Disconnect-IscsiTarget.md)
断开与指定iSCSI目标对象的会话连接。

### [Get-IscsiConnection](./Get-IscsiConnection.md)
获取有关已连接的 iSCSI 发起者连接的信息。

### [Get-IscsiSession](./Get-IscsiSession.md)
检索有关已建立的iSCSI会话的信息。

### [Get-IscsiTarget](./Get-IscsiTarget.md)
为每个向 iSCSI 启动器注册的 iSCSI 目标返回一个对应的 iSCSI 目标对象。

### [Get-IscsiTargetPortal](./Get-IscsiTargetPortal.md)
获取iSCSI目标端口（target portals）。

### [New-IscsiTargetPortal](./New-IscsiTargetPortal.md)
配置一个iSCSI目标端口（target portal）。

### [注册 IscsiSession](./Register-IscsiSession.md)
使用会话标识符作为输入，注册一个活跃的iSCSI会话以使其持久化（即不会在系统重启后丢失）。

### [Remove-IscsiTargetPortal](./Remove-IscsiTargetPortal.md)
删除指定的 iSCSI 目标端口。

### [Set-IscsiChapSecret](./Set-IscsiChapSecret.md)
设置一个用于 iSCSI 启动器连接的 CHAP 密钥。

### [Unregister-IscsiSession](./Unregister-IscsiSession.md)
使用会话标识符作为输入参数，删除一个处于活动状态的iSCSI会话，使其不再保持持久化状态（即不再被系统自动记录或保留）。

### [更新-IscsiTarget](./Update-IscsiTarget.md)
更新有关已连接的 iSCSI 目标对象的信息。

### [更新-IscsiTargetPortal](./Update-IscsiTargetPortal.md)
更新有关指定的iSCSI目标端口的信息。


