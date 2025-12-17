---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/update-adfscertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-AdfsCertificate
---

# 更新 AdFS 证书

## 摘要
更新 AD FS 的证书。

## 语法

```
Update-AdfsCertificate [[-CertificateType] <String>] [-Urgent] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Update-AdfsCertificate` 这个 cmdlet 用于为 Active Directory Federation Services (AD FS) 创建新的证书。当自动证书更新功能被启用，并且 AD FS 负责管理用于签名操作的证书时，就可以使用这个更新 cmdlet 来启动证书的更新过程。

## 示例

### 示例 1：更新令牌签名证书
```
PS C:\> Update-AdfsCertificate -CertificateType "Token-Signing"
```

这个命令用于更新令牌签名证书。

## 参数

### -CertificateType
指定要滚动的证书类型。该参数的可接受值包括：

- Token-Decrypting
- Token-Signing

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Token-Decrypting, Token-Signing

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -Urgent
表示证书更新应立即进行。紧急更新会立即移除旧证书；由于系统需要更新信任关系以使用新证书，这可能会导致服务中断。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.IdentityServer.PowerShell.Resources.ServiceCertificate

当指定 *PassThru* 参数时，该命令会返回更新后的 ServiceCertificate 对象。默认情况下，此 cmdlet 不会产生任何输出。

## 备注
* The *Urgent* parameter option is useful for emergency rollover situations in which a key might be compromised.

## 相关链接

[Add-AdfsCertificate](./Add-AdfsCertificate.md)

[Get-AdfsCertificate](./Get-AdfsCertificate.md)

[Remove-AdfsCertificate](./Remove-AdfsCertificate.md)

[Set-AdfsCertificate](./Set-AdfsCertificate.md)

