---
description: 使用这个主题来借助 Windows PowerShell 帮助管理 Windows 和 Windows Server 技术。
external help file: Get-ProviderAddress.psm1-help.xml
Module Name: HNVDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hnvdiagnostics/get-provideraddress?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ProviderAddress
---

# Get-ProviderAddress

## 摘要
获取服务器的提供者地址。

## 语法

```
Get-ProviderAddress [<CommonParameters>]
```

## 描述
`Get-ProviderAddress` cmdlet 可以获取物理服务器的提供程序地址（Provider Address，简称 PA）。该 cmdlet 会收集以下信息：

- Provider Address (PA).
The IP address assigned to a hidden network adapter in a non-default network compartment.
- Subnet mask.
The IP prefix length, or mask, of the PA IP address.
- MAC Address.
The media access control address.
- Default gateway.
The default gateway (next-hop) for the specified PA IP address.
This typically corresponds to the IP address assigned to the top-of-rack (ToR) switch.

## 示例

### 示例 1：获取提供者的地址
```
PS C:\> Get-ProviderAddress
ProviderAddress : 10.10.182.68
MAC Address     : 00-1D-D8-EE-1C-07
Subnet Mask     : 255.255.255.128
Default Gateway : 10.10.182.1
VLAN            : VLAN11
ProviderAddress : 10.10.182.69
MAC Address     : 00-1D-D8-EE-1C-09
Subnet Mask     : 255.255.255.128
Default Gateway : 10.10.182.1
VLAN            : VLAN11
```

这个命令用于获取提供者的地址。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

