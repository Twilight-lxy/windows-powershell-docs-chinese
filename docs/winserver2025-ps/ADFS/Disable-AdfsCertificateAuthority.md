---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/disable-adfscertificateauthority?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-AdfsCertificateAuthority
---

# 禁用 AdfsCertificateAuthority

## 摘要
禁用一个证书颁发机构（CA）。

## 语法

```
Disable-AdfsCertificateAuthority [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
` Disable-AdfsCertificateAuthority` 这个 cmdlet 用于禁用 Active Directory Federation Services (AD FS) 中的证书颁发机构。

## 示例

## 参数

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -WhatIf
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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

## 输出

### Microsoft IdentityServer.Management.Resources.AdfsCertificateAuthority

当指定*PassThru*参数时，该命令会返回一个被禁用的AdfsCertificatAuthority对象。默认情况下，此cmdlet不会生成任何输出。

## 备注

## 相关链接

[Get-AdfsCertificateAuthority](./Get-AdfsCertificateAuthority.md)

[Set-AdfsCertificateAuthority](./Set-AdfsCertificateAuthority.md)

