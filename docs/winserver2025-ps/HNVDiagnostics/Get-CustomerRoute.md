---
description: 使用这个主题来借助 Windows PowerShell 帮助管理 Windows 和 Windows Server 技术。
external help file: Get-CustomerRoute.psm1-help.xml
Module Name: HNVDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hnvdiagnostics/get-customerroute?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-CustomerRoute
---

# Get-CustomerRoute

## 摘要
获取CA路由信息。

## 语法

```
Get-CustomerRoute [<CommonParameters>]
```

## 描述
`Get-CustomerRoute` cmdlet 可以获取按路由域 ID（RDID）分类的客户地址（CA）路由信息。这些信息包括：

- Virtual Subnet ID (VSID).
This value is unique per virtual subnet, and corresponds to the VxLAN Network Identifier (VNI) or the NVGRE Tenant Network Identifier (TNI) in the VxLAN and NVGRE headers, respectively.
- CA IP Prefix.
IP prefix for the virtual subnet.
- CA IP Prefix Length.
Length (or subnet mask) of the CA IP Prefix.
- CA IP Next Hop.
The next hop required to reach the specified CA IP Prefix, usually the default gateway assigned to the HNV distributed router.
- Routing Domain ID.

## 示例


## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

