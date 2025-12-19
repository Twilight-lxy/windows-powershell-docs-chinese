---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.RemoteAttestation.Server.PowerShell.dll-Help.xml
Module Name: HgsAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsattestation/get-hgsattestationsignercertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-HgsAttestationSignerCertificate
---

# 获取 HGS 证书签名者的证书

## 摘要
获取用于签署认证证书的密钥对的公共证书。

## 语法

```
Get-HgsAttestationSignerCertificate [<CommonParameters>]
```

## 描述
`Get-HgsAttestationSignerCertificate` cmdlet 用于获取 Host Guardian Service (HGS) 认证所需的签名证书。认证服务使用密钥对来签署认证证书，该 cmdlet 则用于获取与该密钥对对应的公钥证书。

## 示例

#### 示例 1：获取签名者证书
```
PS C:\> Get-HgsAttestationSignerCertificate
```

此命令用于获取认证服务（Attestation Service）签名者的证书。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONPARAMETERS（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

### System SECURITY Cryptography.X509Certificates.X509Certificate2
这个cmdlet返回一个X.509证书。

## 备注

## 相关链接

