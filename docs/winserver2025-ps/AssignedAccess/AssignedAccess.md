---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.0.1
Locale: en-US
Module Guid: 9e72217e-9e27-45f7-81fc-048763587e0a
Module Name: AssignedAccess
ms.date: 12/20/2016
title: AssignedAccess
---

# AssignedAccess 模块
## 描述
用于管理“指定访问权限”（Assigned Access）的 Windows PowerShell cmdlets 的设计目的是为了实现对特定用户账户应用访问权限的控制。当某个用户账户被配置为使用“指定访问权限”时，该用户只能使用一个来自 Windows Store 的应用程序。此时，用户无法退出该应用程序、登出系统，也无法访问任何系统设置。

“Assigned Access” cmdlet 仅支持 Windows 10 和 Windows 11 客户端操作系统。

## AssignedAccessCmdlets
### [Clear-AssignedAccess](./Clear-AssignedAccess.md)
将用户账户从已分配的访问权限中移除。

### [获取分配的访问权限](./Get-AssignedAccess.md)
获取当前分配的访问权限的配置信息。

### [Set-AssignedAccess](./Set-AssignedAccess.md)
配置用户仅能启动一个应用程序。


