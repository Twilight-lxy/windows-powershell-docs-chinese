---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 4.0.3.1
Locale: en-US
Module Guid: 2fbffabe-343d-4db8-ad9e-a8943f50d096
Module Name: MPIO
ms.date: 12/27/2016
title: MPIO
---

# MPIO模块
## 描述
本参考资料提供了所有与多路径I/O（MPIO）相关的cmdlet的描述和语法信息。这些cmdlet按照其开头动词的字母顺序进行排列。

## MPIO Cmdlets
### [Clear-MSDSMSSupportedHW](./Clear-MSDSMSSupportedHW.md)
从 MSDSM（Microsoft System Diagnosis and Management）支持的硬件列表中删除相应的硬件 ID。

### [禁用-MSDSMAutomaticClaim](./Disable-MSDSMAutomaticClaim.md)
防止MSDSM为某种总线类型自动将SAN磁盘分配给MPIO（多路径I/O）。

### [Enable-MSDSMAutomaticClaim](./Enable-MSDSMAutomaticClaim.md)
使 MSDSM 能够自动为 MPIO 功能申请使用 SAN 磁盘。

### [Get-MPIOAvailableHW](./Get-MPIOAvailableHW.md)
列出系统中可通过MSDSM进行管理的、适用于MPIO（多路径I/O）的设备。

### [Get-MPIOSetting](./Get-MPIOSetting.md)
获取 MPIO 设置信息。

### [Get-MSDSMAutomaticClaimSettings](./Get-MSDSMAutomaticClaimSettings.md)
获取用于自动将SAN磁盘标记为MPIO（多路径I/O）的MSDSM设置。

### [Get-MSDSMGlobalDefaultLoadBalancePolicy](./Get-MSDSMGlobalDefaultLoadBalancePolicy.md)
获取用于 MPIO 设备的默认负载均衡策略。

### [Get-MSDSMSSupportedHW](./Get-MSDSMSSupportedHW.md)
列出 MSDSM 支持的硬件列表中的硬件 ID。

### [New-MSDSMSSupportedHW](./New-MSDSMS SupportedHW.md)
在 MSDSM 支持的硬件列表中，创建一个包含厂商 ID 和产品 ID 组合的硬件 ID。

### [Remove-MSDSMSSupportedHW](./Remove-MSDSMSSupportedHW.md)
从 MSDSM 支持的硬件列表中删除具有特定供应商 ID 和产品 ID 组合的硬件设备。

### [Set-MPIOSetting](./Set-MPIOSetting.md)
更改MPIO设置。

### [Set-MSDSMGlobalDefaultLoadBalancePolicy](./Set-MSDSMGlobalDefaultLoadBalancePolicy.md)
为 MPIO 设备设置默认的负载均衡策略。

### [Update-MPIOClaimedHW](./Update-MPIOClaimedHW.md)
尝试获取当前位于 MSDSM 支持的硬件列表中的设备。


