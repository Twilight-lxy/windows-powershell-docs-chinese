---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsalternatetlsclientbinding?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsAlternateTlsClientBinding
---

# 设置 AdfsAlternateTlsClientBinding

## 摘要
配置现有的 AD FS 部署，使其在设备证书认证和客户端证书认证过程中使用相同的端口。

## 语法

```
Set-AdfsAlternateTlsClientBinding [-Thumbprint <String>] [-Member <String[]>] [-Force <Boolean>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsAlternateTlsClientBinding` cmdlet 用于配置现有的 AD FS（Active Directory Federation Services）部署，使其在设备证书认证和客户端证书认证（即客户端 TLS 连接）过程中使用相同的端口（443）。该 cmdlet 会在 `certauth.\<federation service name\>`（例如 `certauth.contoso.com`）上创建一个用于用户证书认证的端点。

要将部署方式改回使用非标准端口的用户证书认证的方式，请使用 `Set-AdfsSslCertificate` cmdlet，并使用一个新的证书。该新证书不应包含用于 `<federation service name>`. 的“Subject Alternative Name (SAN)”字段。

如果 SSL 证书中没有包含用于 `<federation service name>`（例如 `certauth.contoso.com`）的 “Subject Alternative Name”（SAN），则 **Install-AdfsFarm** cmdlet 会配置客户端在端口 49443 上使用 TLS 协议进行通信。

使用 `Set-AdfsAlternateTlsClientBinding` 命令，并搭配一个包含 SAN（Subject Alternative Name）字段的新证书。该命令会配置 Active Directory Federation Services (AD FS) 使用端口 443 进行客户端与服务器之间的 TLS 通信。

## 示例

#### 示例 1：配置一个部署
```
PS C:\> Set-AdfsAlternateTlsClientBinding -Member "ADFSServer1.contoso.com" -Thumbprint "c67e1ffba186d70c7e00c89596e0cb5645f9874a"
```

此命令配置了一个部署方案，使得设备证书认证和用户证书认证使用相同的端口。在这个例子中，具有指定指纹的证书包含一个用于 certauth.contoso.com 的 SAN（Subject Alternative Name）。

## 参数

### -Force
强制命令运行，而不会询问用户的确认。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Member
```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Thumbprint
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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

## 输出

## 备注

## 相关链接

[Set-AdfsSslCertificate](./Set-AdfsSslCertificate.md)

