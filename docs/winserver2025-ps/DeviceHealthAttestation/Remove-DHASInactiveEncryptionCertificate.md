---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.DeviceHealthAttestation.PowerShell.dll-Help.xml
Module Name: DeviceHealthAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/devicehealthattestation/remove-dhasinactiveencryptioncertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DHASInactiveEncryptionCertificate
---

# 删除不再使用的 DHAS 加密证书

## 摘要
删除无效的加密证书。

## 语法

```
Remove-DHASInactiveEncryptionCertificate [[-Thumbprint] <String>] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-DHASInactiveEncryptionCertificate` cmdlet 用于移除设备健康认证（Device Health Attestation）服务中处于非活动状态的加密证书。

你必须具有管理员权限才能运行此 cmdlet。

## 示例

### 示例 1：移除无效的加密证书
```
PS C:\> Remove-DHASInactiveEncryptionCertificate -Thumbprint "0123456789ABCDEF0123456789ABCDEF01234567"
```

## 参数

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-DHASinactiveEncryptionCertificate](./Get-DHASInactiveEncryptionCertificate.md)

