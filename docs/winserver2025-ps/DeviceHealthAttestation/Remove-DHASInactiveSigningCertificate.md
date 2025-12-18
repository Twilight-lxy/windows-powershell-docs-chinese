---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.DeviceHealthAttestation.PowerShell.dll-Help.xml
Module Name: DeviceHealthAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/devicehealthattestation/remove-dhasinactivesigningcertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DHASInactiveSigningCertificate
---

# 删除不再使用的DHAS签名证书

## 摘要
删除失效的签名证书。

## 语法

```
Remove-DHASInactiveSigningCertificate [[-Thumbprint] <String>] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-DHASIncompleteSigningCertificate` 这个 cmdlet 用于移除设备健康验证（Device Health Attestation）服务中不再使用的签名证书。

您必须具有管理员权限才能运行此cmdlet。

## 示例

### 示例 1：移除签名证书
```
PS C:\> Remove-DHASInactiveSigningCertificate -Thumbprint "0123456789ABCDEF0123456789ABCDEF01234567"
```

该命令会删除指定的无效签名证书。

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
强制命令运行，而不会要求用户确认。

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
指定签名证书的指纹（thumbprint）。该值必须仅包含十六进制数字（0-9、A-F），且长度为40个字符。此值不区分大小写。

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

[Get-DHASInactiveSigningCertificate](./Get-DHASInactiveSigningCertificate.md)

