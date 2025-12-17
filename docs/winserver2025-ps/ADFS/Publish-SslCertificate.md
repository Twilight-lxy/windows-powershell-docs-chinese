---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Deployment.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/publish-sslcertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Publish-SslCertificate
---

# 发布 SSL 证书

## 摘要
`Publish-SslCertificate` cmdlet 已被弃用。请使用 `Set-AdfsSslCertificate` cmdlet 代替它。

## 语法

### PublishByPfxPath（默认值）
```
Publish-SslCertificate -Path <String> -Password <SecureString> [<CommonParameters>]
```

### PublishByPfxData
```
Publish-SslCertificate -RawPfx <Byte[]> -Password <SecureString> [<CommonParameters>]
```

## 描述
`Publish-SslCertificate` cmdlet 在此版本中已被弃用。请改用 `Set-AdfsSslCertificate` cmdlet。

## 示例

## 参数

### -Password
```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
```yaml
Type: String
Parameter Sets: PublishByPfxPath
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RawPfx
```yaml
Type: Byte[]
Parameter Sets: PublishByPfxData
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[Set-AdfsSslCertificate](./Set-AdfsSslCertificate.md)

