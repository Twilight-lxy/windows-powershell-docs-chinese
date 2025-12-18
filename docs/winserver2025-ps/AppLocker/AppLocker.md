---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.0.1
Locale: en-US
Module Guid: 9dafd409-67de-4108-8ee9-73cd61f5b7bf
Module Name: AppLocker
ms.date: 09/28/2020
title: AppLocker
---

# AppLocker 模块
## 说明
用于 AppLocker 的 Windows PowerShell cmdlet 旨在简化应用程序控制策略的管理。这些 cmdlet 可以帮助创建、测试、维护和排查应用程序控制策略的问题，并且可以与 AppLocker 用户界面配合使用。该用户界面可通过 Microsoft Management Console (MMC) 中的“本地安全策略”管理单元和“组策略管理控制台”来访问。

请注意，AppLocker cmdlets 仅与组策略交互，并不了解 AppLocker CSP 的任何信息。

## AppLockerCmdlets
### [Get-AppLockerFileInformation](./Get-AppLockerFileInformation.md)
从文件列表或事件日志中获取创建 AppLocker 规则所需的文件信息。

### [Get-AppLockerPolicy](./Get-AppLockerPolicy.md)
获取本地、生效的或域级别的 AppLocker 策略。

### [新应用锁策略](./New-AppLockerPolicy.md)
根据文件信息列表及其他规则创建选项，生成一个新的AppLocker策略。

### [Set-AppLockerPolicy](./Set-AppLockerPolicy.md)
为指定的组策略对象（GPO）设置 AppLocker 策略。

### [Test-AppLockerPolicy](./Test-AppLockerPolicy.md)
指定 AppLocker 策略，以确定给定用户是否被允许运行输入文件。

