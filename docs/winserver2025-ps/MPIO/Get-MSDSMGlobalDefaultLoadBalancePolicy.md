---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Mpio-help.xml
Module Name: MPIO
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/mpio/get-msdsmglobaldefaultloadbalancepolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-MSDSMGlobalDefaultLoadBalancePolicy
---

# Get-MSDSMGlobalDefaultLoadBalancePolicy

## 摘要
获取用于 MPIO 设备的默认负载均衡策略。

## 语法

```
Get-MSDSMGlobalDefaultLoadBalancePolicy [<CommonParameters>]
```

## 描述
`Get-MSDSMGlobalDefaultLoadBalancePolicy` cmdlet 用于获取 Microsoft Multipath I/O (MPIO) 设备的默认负载均衡策略。您可以使用 `Set-MSDSMGlobalDefaultLoadBalancePolicy` cmdlet 来更改该策略。Microsoft Device Specific Module (MSDSM) 仅在您设置策略后，针对其管理的设备应用该策略。

该cmdlet返回一个字符串，其中包含以下值之一：

- None.
No currently configured default load balance policy.
- FOO.
Fail Over Only.
- RR.
Round Robin.
- LQD.
Least Queue Depth.
- LB.
Least Blocks.

## 示例

### 示例 1：获取负载均衡策略
```
PS C:\> Get-MSDSMGlobalDefaultLoadBalancePolicy
RR
```

这个命令用于获取全局默认的负载均衡策略，在这种情况下，该策略是采用轮询（RR）方式的负载均衡策略。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.String

## 备注

## 相关链接

[Set-MSDSMGlobalDefaultLoadBalancePolicy](./Set-MSDSMGlobalDefaultLoadBalancePolicy.md)

