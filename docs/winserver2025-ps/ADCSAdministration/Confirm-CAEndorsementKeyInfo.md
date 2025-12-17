---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Administration.Commands.dll-Help.xml
Module Name: ADCSAdministration
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsadministration/confirm-caendorsementkeyinfo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Confirm-CAEndorsementKeyInfo
---

# 确认 CA 认证密钥信息

## 摘要
检查本地证书颁发机构（CA）是否信任用于密钥认证的安全硬件。

## 语法

### PublicKeyHash
```
Confirm-CAEndorsementKeyInfo [-PublicKeyHash] <String> [<CommonParameters>]
```

### 证书
```
Confirm-CAEndorsementKeyInfo [-Certificate] <X509Certificate2> [<CommonParameters>]
```

## 描述
`Confirm-CAEndorsementKeyInfo` 这个 cmdlet 用于检查本地证书颁发机构（CA）是否信任用于密钥认证的安全硬件（例如受信任的平台模块（TPM））。该 cmdlet 会验证相应的授权密钥或证书。授权密钥是永久嵌入到安全硬件中的；其公开部分有助于识别真正的安全硬件设备。

此cmdlet用于验证该背书公共证书是否通过证书链与CA（证书颁发机构）信任的锚点相连，从而实现密钥认证。请使用*Certificate*参数指定一个X509证书。

此cmdlet用于检查在本地CA配置的文件夹中，是否存在用于密钥认证的签名公钥文件。请使用 PublicKeyHash参数来指定该公钥。

## 示例

### 示例 1：检查背书证书
```
PS C:\> Confirm-CAEndorsementKeyInfo -Certificate Contoso87.cer

True
```

此命令用于检查签名证书 Contoso87.cer 是否能够通过证书链连接到某个受信任的根证书（即“可信锚点”）。在本示例中，返回的值为 $True。

### 示例 2：检查背书密钥
```
PS C:\> Confirm-CAEndorsementKeyInfo -PublicKeyHash "1dd117facfbdcbd8713b9c588eef305e61ce3d8e3c6e21e6323a877476ecd167"
False
```

该命令用于检查作为 SHA-256 哈希码指定的签名证书。在这个示例中，返回的值是 $False$，因此该证书颁发机构（CA）并不拥有这个公钥。

## 参数

### -Certificate
指定用于保护硬件的 X509 公钥证书。

```yaml
Type: X509Certificate2
Parameter Sets: Certificate
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PublicKeyHash
指定安全硬件的签名公钥，该公钥是通过SHA-256哈希算法计算得出的。这是一个由64个字符组成的十六进制字符串。

```yaml
Type: String
Parameter Sets: PublicKeyHash
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.Security.Cryptography.X509Certificates.X509Certificate2

## 输出

### System(Boolean)

## 备注

## 相关链接

