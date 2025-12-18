---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.DeviceHealthAttestation.PowerShell.dll-Help.xml
Module Name: DeviceHealthAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/devicehealthattestation/get-dhasinactiveencryptioncertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DHASInactiveEncryptionCertificate
---

# 获取未使用的加密证书（使用 Get-DHASInactiveEncryptionCertificate 命令）

## 摘要
获取无效的加密证书。

## 语法

```
Get-DHASInactiveEncryptionCertificate [<CommonParameters>]
```

## 描述
`Get-DHASInactiveEncryptionCertificate` cmdlet 用于获取设备健康认证（Device Health Attestation）服务中无效的加密证书的指纹信息。

你必须具有管理员权限才能运行此cmdlet。

## 示例

### 示例 1：获取无效的加密证书
```
PS C:\> Get-DHASInactiveEncryptionCertificate
```

这个命令用于获取失效的加密证书的指纹（thumbprint）。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 字符串
此cmdlet以**字符串**的形式返回无效的加密证书。

## 备注

## 相关链接

[Remove-DHASInactiveEncryptionCertificate](./Remove-DHASInactiveEncryptionCertificate.md)

