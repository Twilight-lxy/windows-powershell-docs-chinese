---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.KpsServer.Administration.dll-Help.xml
Module Name: HgsKeyProtection
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgskeyprotection/remove-hgskeyprotectionattestationsignercertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-HgsKeyProtectionAttestationSignerCertificate
---

# 移除HGS密钥保护认证签名证书

## 摘要
从密钥保护服务（Key Protection Service）中的受信任证书列表中移除某个认证签名者的证书。

## 语法

```
Remove-HgsKeyProtectionAttestationSignerCertificate -Thumbprint <String> [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-HgsKeyProtectionAttestationSignerCertificate` cmdlet 会从 Key Protection Service 所信任的认证签名证书列表中移除某个认证服务器的签名证书。

## 示例

### 示例 1：删除认证证书
```
PS C:\> Remove-HgsKeyProtectionAttestationSignerCertificate -Thumbprint "d39203a3b3544743ad552afe0615dc1f"
```

此命令用于移除一个受信任的证书签名者。该命令通过使用“指纹”（即证书的独特标识信息）来查找需要移除的证书签名者。

## 参数

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
指定要删除的认证签名者证书的“指纹”（即该证书的唯一标识信息）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您确认是否要继续执行该操作。

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无
您不能将输入数据通过管道传递给此 cmdlet。

## 输出

### 无
此cmdlet不会生成任何输出。

## 备注

## 相关链接

[Add-HgsKeyProtectionAttestationSignerCertificate](./Add-HgsKeyProtectionAttestationSignerCertificate.md)

[Get-HgsKeyProtectionAttestationSignerCertificate](./Get-HgsKeyProtectionAttestationSignerCertificate.md)

