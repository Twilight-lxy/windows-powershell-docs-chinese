---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.KpsServer.Administration.dll-Help.xml
Module Name: HgsKeyProtection
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgskeyprotection/set-hgskeyprotectionattestationsignercertificatepolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-HgsKeyProtectionAttestationSignerCertificatePolicy
---

# 设置 HGS 密钥保护认证签名者证书策略

## 摘要
修改用于证明签名者证书的策略。

## 语法

```
Set-HgsKeyProtectionAttestationSignerCertificatePolicy -DenyHealthCertificatesIssuedBefore <DateTime>
 [-Thumbprint <String>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-HgsKeyProtectionAttestationSignerCertificatePolicy` 这个 cmdlet 用于修改与认证签名者证书相关的策略。你可以更改该策略中的日期设置。Key Protection Service 会拒绝那些由指定的认证签名者证书签署、但发行时间早于所设定日期的健康证书（即不符合策略要求的证书）。

## 示例

### 示例 1：修改所有证明签名者证书上的日期
```
PS C:\> $DenyTime = Get-Date
PS C:\> Set-HgsKeyProtectionAttestationSignerCertificatePolicy -DenyHealthCertificatesIssuedBefore $DenyTime
```

第一个命令使用 `Get-Date` cmdlet 创建一个 `DateTime` 对象，并将其存储在 `$DenyTime` 变量中。

第二个命令将所有受信任的认证签名者证书中的日期修改为存储在 `$DenyTime` 变量中的值。

### 示例 2：修改认证签名者证书上的日期
```
PS C:\> $DenyTime = Get-Date
PS C:\> Set-HgsKeyProtectionAttestationSignerCertificatePolicy -DenyHealthCertificatesIssuedBefore $DenyTime -Thumbprint "8bdc4fb5034c4adb86cb57a4465dc161"
```

第一个命令创建了一个 `DateTime` 对象，然后将其存储在 `$DenyTime` 变量中。

第二个命令将某个特定的受信任的证明签名者证书的日期修改为存储在 `$DenyTime` 变量中的值。

## 参数

### -DenyHealthCertificatesIssuedBefore
指定一个日期作为 **DateTime** 对象。密钥保护服务会拒绝任何由指定的认证签名者证书签署且在该时间之前颁发的健康证书。要获取一个 **DateTime** 对象，请使用 [Get-Date](https://go.microsoft.com/fwlink/?LinkID=293966) cmdlet。有关更多信息，输入 `Get-Help Get-Date`。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
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
指定要应用策略的认证签名者证书的“指纹”（即该证书的唯一标识符）。如果您未为此参数指定值，此cmdlet将把策略应用于所有签名者证书。

```yaml
Type: String
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
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于常用参数（about_CommonParameters）的文档（网址：http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无
您无法将输入内容通过管道（pipe）传递给此cmdlet。

## 输出

### 无
此cmdlet不会生成任何输出。

## 备注

## 相关链接

[Get-HgsKeyProtectionAttestationSignerCertificate](./Get-HgsKeyProtectionAttestationSignerCertificate.md)

