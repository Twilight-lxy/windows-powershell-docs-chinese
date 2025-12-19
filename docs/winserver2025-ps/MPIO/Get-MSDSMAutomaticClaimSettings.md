---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Mpio-help.xml
Module Name: MPIO
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/mpio/get-msdsmautomaticclaimsettings?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-MSDSMAutomaticClaimSettings
---

# 获取 MSDSMAutomaticClaimSettings 设置

## 摘要
获取用于自动将SAN磁盘标记为MPIO（多路径I/O）的MSDSM设置。

## 语法

```
Get-MSDSMAutomaticClaimSettings [<CommonParameters>]
```

## 描述
`Get-MSDSMAutomaticClaimSettings` cmdlet 可用于获取 Microsoft 设备特定模块（MSDSM）的设置，这些设置用于自动申请存储区域网络（SAN）磁盘以支持 Microsoft 多路径输入/输出（MPIO）功能。

MSDSM可以自动选择是否支持串行连接存储（SAS）或互联网小型计算机系统接口（iSCSI），或者同时支持两者，或者两者都不支持。您可以使用 **Enable-MSDSMAutomaticClaim** 或 **Disable-MSDSMAutomaticClaim** cmdlet 来更改这些设置。

## 示例

#### 示例 1：获取自动理赔设置
```
PS C:\> Get-MSDSMAutomaticClaimSettings
Name                            Value

----                            -----

iSCSI                           False

SAS                             True
```

此命令用于获取MSDSM的自动资源 claiming（即自动分配存储资源的）设置。在这种情况下，MSDSM会自动为SAS磁盘分配存储空间，但不会为iSCSI磁盘进行自动资源分配。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Cim.Instance

## 备注

## 相关链接

[Get-MSDSMSSupportedHW](./Get-MSDSMS SupportedHW.md)

[禁用 MSDSMAutomaticClaim 功能](./ Disable-MSDSMAutomaticClaim.md)

[Enable-MSDSMAutomaticClaim](./Enable-MSDSMAutomaticClaim.md)

