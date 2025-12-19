---
description: 此参考资料提供了 Windows 本地管理员密码解决方案（LAPS）模块对应的cmdlet描述和语法信息。
Module Name: LAPS
Module Guid: 8eb7ddf9-7890-49ae-9af1-3b41d7e63c41
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 1.0.0.0
Locale: en-US
ms.date: 04/10/2023
title: LAPS
---

# LAPS模块

## 描述

该参考资料提供了用于 Windows 本地管理员密码解决方案（LAPS）模块的 cmdlet 描述和语法信息，并将这些 cmdlet 按字母顺序进行了排列。

## LAPSCmdlets

### [Find-LapsADExtendedRights](Find-LapsADExtendedRights.md)

查询 Active Directory（AD），以找到被授予读取 Windows 本地管理员密码解决方案（LAPS）密码属性权限的主体。

### [Get-LapsAADPassword](Get-LapsAADPassword.md)

在指定的 Microsoft Entra 设备上，查询用于获取 Windows 本地管理员密码解决方案（LAPS）凭据的 Microsoft Entra ID。

### [Get-LapsADPassword](Get-LapsADPassword.md)

从指定的 Active Directory（AD）计算机或域控制器对象中查询 Windows 本地管理员密码解决方案（LAPS）的凭据。

### [Get-LapsDiagnostics](Get-LapsDiagnostics.md)

从本地机器收集 Windows 本地管理员密码解决方案（LAPS）的相关日志和跟踪数据。

### [Invoke-LapsPolicyProcessing](Invoke-LapsPolicyProcessing.md)

这会导致 Windows 本地管理员密码解决方案（LAPS）处理当前配置的策略。

### [Reset-LapsPassword](Reset-LapsPassword.md)

该原因会导致 Windows 本地管理员密码解决方案（LAPS）立即为当前管理的本地账户更改其密码。

### [Set-LapsADAuditing](Set-LapsADAuditing.md)

配置 Active Directory（AD）中的组织单位（Organizational Unit，简称 OU），以启用对 Windows 本地管理员密码解决方案（Windows Local Administrator Password Solution，简称 LAPS）中密码模式属性的审计功能。

### [Set-LapsADComputer_permissions](Set-LapsADComputer上面这段话翻译为中文如下：  
### [Set-LapsADComputerSelfPermission](Set-LapsADComputer.Permission.md)

配置 Active Directory（AD）组织单元（Organizational Unit，简称 OU）的权限，以使该 OU 中的计算机能够更新其 Windows 本地管理员密码解决方案（Windows Local Administrator Password Solution，简称 LAPS）的密码。

### [Set-LapsADPasswordExpirationTime](Set-LapsADPasswordExpirationTime.md)

用于在 Active Directory（AD）计算机或域控制器对象上设置 Windows 本地管理员密码解决方案（LAPS）的密码过期时间戳。

### [Set-LapsADReadPasswordPermission](Set-LapsADReadPasswordPermission.md)

配置 Active Directory（AD）组织单位（OU）的安全设置，以允许特定的用户或组查询 Windows 本地管理员密码解决方案（LAPS）中的密码。

### [Set-LapsADResetPasswordPermission](Set-LapsADResetPasswordPermission.md)

配置 Active Directory（AD）组织单元（OU）的安全设置，以允许特定用户或组更改 Windows 本地管理员密码解决方案（LAPS）的密码过期时间。

### [更新LapsADSchema](Update-LapsADSchema.md)

通过添加 Windows 本地管理员密码解决方案（LAPS）的架构属性来扩展 Active Directory（AD）的架构。
