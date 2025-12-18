---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.DeviceHealthAttestation.PowerShell.dll-Help.xml
Module Name: DeviceHealthAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/devicehealthattestation/get-dhasactivesigningcertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DHASActiveSigningCertificate
---

# 获取 DHAS 活动签名证书

## 摘要
获取当前活动的签名证书。

## 语法

```
Get-DHASActiveSigningCertificate [<CommonParameters>]
```

## 描述
`Get-DHASActiveSigningCertificate` cmdlet 可以获取设备健康认证（Device Health Attestation）服务中当前使用的签名证书的指纹信息。

您必须具有管理员权限才能运行此cmdlet。

## 示例

### 示例 1：获取当前使用的签名证书
```
PS C:\> Get-DHASActiveSigningCertificate
```

此命令用于获取设备健康验证（Device Health Attestation）服务所使用的当前签名证书的摘要信息（即“指纹”）。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 字符串（String）
此cmdlet返回活动的签名证书的指纹（thumbprint）。

## 备注

## 相关链接

[Set-DHASActiveSigningCertificate](./Set-DHASActiveSigningCertificate.md)

