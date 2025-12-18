---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.DeviceHealthAttestation.PowerShell.dll-Help.xml
Module Name: DeviceHealthAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/devicehealthattestation/get-dhascertificatechainpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DHASCertificateChainPolicy
---

# 获取DHASCertificateChainPolicy

## 摘要
获取证书链策略。

## 语法

```
Get-DHASCertificateChainPolicy [<CommonParameters>]
```

## 描述
`Get-DHASCertificateChainPolicy` cmdlet 可以获取设备健康验证（Device Health Attestation）服务所实施的证书链策略。该证书链策略规定了用于证书链验证和撤销行为的相关参数。

你必须具有管理员权限才能运行此cmdlet。

## 示例

### 示例 1：获取证书链策略
```
PS C:\> Get-DHASCertificateChainPolicy
```

此命令用于获取设备健康证明（Device Health Attestation）服务当前的证书链策略。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### CertificateChainPolicy
此cmdlet返回的**CertificateChainPolicy**对象具有以下成员：

- RevocationFlag.
A .NET [X509RevocationFlag enumeration](https://go.microsoft.com/fwlink/?LinkId=821152).
- RevocationMode.
A .NET [X509RevocationMode enumeration](https://go.microsoft.com/fwlink/?LinkId=821153).
- VerificationFlags.
A .NET [X509VerificationFlags enumeration](https://go.microsoft.com/fwlink/?LinkId=821154).
- UrlRetrievalTimeout.
A .NET [TimeSpan structure](https://go.microsoft.com/fwlink/?LinkId=821155).

## 备注

## 相关链接

[Set-DHASCertificateChainPolicy](./Set-DHASCertificateChainPolicy.md)

