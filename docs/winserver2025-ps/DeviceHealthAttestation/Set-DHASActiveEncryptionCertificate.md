---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.DeviceHealthAttestation.PowerShell.dll-Help.xml
Module Name: DeviceHealthAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/devicehealthattestation/set-dhasactiveencryptioncertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DHASActiveEncryptionCertificate
---

# Set-DHASActiveEncryptionCertificate

## 摘要
设置活动的加密证书。

## 语法

```
Set-DHASActiveEncryptionCertificate [-Thumbprint] <String> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DHASActiveEncryptionCertificate` cmdlet 用于设置设备健康验证（Device Health Attestation）服务的活动加密证书。

您必须具有管理员权限才能运行此cmdlet。

## 示例

### 示例 1：设置加密证书
```
PS C:\> Set-DHASActiveEncryptionCertificate -Thumbprint "0123456789ABCDEF0123456789ABCDEF01234567"
```

此命令用于设置设备健康认证（Device Health Attestation）服务所使用的有效加密证书。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需请求用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Thumbprint
指定加密证书的指纹（thumbprint）。该值必须仅包含十六进制数字（0-9、A-F），且长度为40个字符。此值不区分大小写。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 字符串（String）
输入类型为字符串（String），用于表示当前使用的加密证书的指纹（thumbprint）。

## 输出

## 备注

## 相关链接

[Get-DHASActiveEncryptionCertificate](./Get-DHASActiveEncryptionCertificate.md)

