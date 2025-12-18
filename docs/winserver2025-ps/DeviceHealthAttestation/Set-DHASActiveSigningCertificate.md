---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.DeviceHealthAttestation.PowerShell.dll-Help.xml
Module Name: DeviceHealthAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/devicehealthattestation/set-dhasactivesigningcertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DHASActiveSigningCertificate
---

# Set-DHASActiveSigningCertificate

## 摘要
设置当前使用的签名证书。

## 语法

```
Set-DHASActiveSigningCertificate [-Thumbprint] <String> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DHASActiveSigningCertificate` cmdlet 用于设置设备健康认证（Device Health Attestation）服务的当前签名证书。

您必须具有管理员权限才能运行此cmdlet。

## 示例

### 示例 1：设置激活的签名证书
```
PS C:\> Set-DHASActiveSigningCertificate -Thumbprint "0123456789ABCDEF0123456789ABCDEF01234567"
```

这个命令用于设置当前的签名证书。

## 参数

### -Confirm
在运行cmdlet之前会提示您进行确认。

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
强制命令执行，而无需请求用户确认。

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
指定签名证书的指纹（thumbprint）。该值必须仅包含十六进制数字（0-9、A-F），且长度为40个字符。此值的大小写不敏感。

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
展示了如果该cmdlet被运行时会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 字符串（String）
输入类型是一个字符串，用于表示当前使用的签名证书的指纹（thumbprint）。

## 输出

## 备注

## 相关链接

[Get-DHASActiveSigningCertificate](./Get-DHASActiveSigningCertificate.md)

