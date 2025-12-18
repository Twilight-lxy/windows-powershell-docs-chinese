---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.DeviceHealthAttestation.PowerShell.dll-Help.xml
Module Name: DeviceHealthAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/devicehealthattestation/get-dhasactiveencryptioncertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DHASActiveEncryptionCertificate
---

# 获取 DHA 活动加密证书

## 摘要
获取活动的加密证书指纹。

## 语法

```
Get-DHASActiveEncryptionCertificate [<CommonParameters>]
```

## 描述
`Get-DHASActiveEncryptionCertificate` cmdlet 可以获取设备健康认证（Device Health Attestation）服务当前使用的加密证书的摘要（thumbprint）。

您必须具有管理员权限才能运行此cmdlet。

## 示例

#### 示例 1：获取当前的加密证书
```
PS C:\> Get-DHASActiveEncryptionCertificate
```

此命令用于获取设备健康验证（Device Health Attestation）服务所使用的当前加密证书的“指纹”信息。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 字符串
此cmdlet返回当前的加密证书指纹。

## 备注

## 相关链接

[Set-DHASActiveEncryptionCertificate](./Set-DHASActiveEncryptionCertificate.md)

