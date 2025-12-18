---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.DeviceHealthAttestation.PowerShell.dll-Help.xml
Module Name: DeviceHealthAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/devicehealthattestation/get-dhasinactivesigningcertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DHASInactiveSigningCertificate
---

# 获取不活动的DHAS签名证书

## 摘要
获取未使用的签名证书。

## 语法

```
Get-DHASInactiveSigningCertificate [<CommonParameters>]
```

## 描述
`Get-DHASInactiveSigningCertificate` cmdlet 可用于获取设备健康验证（Device Health Attestation）服务中处于非活动状态的签名证书的指纹信息。

你必须具有管理员权限才能运行此cmdlet。

## 示例

### 示例 1：获取无效的签名证书
```
PS C:\> Get-DHASInactiveSigningCertificate
```

这个示例用于获取无效签名证书的指纹（即该证书的哈希值）。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Remove-DHASInactiveSigningCertificate](./Remove-DHASInactiveSigningCertificate.md)

