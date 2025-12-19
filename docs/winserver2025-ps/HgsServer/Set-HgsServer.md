---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsServer-help.xml
Module Name: HgsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsserver/set-hgsserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-HgsServer
---

# Set-HgsServer

## 摘要
用于设置Host Guardian Service服务器的配置参数。

## 语法

### http 和 httpsThumbprint
```
Set-HgsServer [-Http] [-Https] [-HttpPort <UInt16>] [-HttpsPort <UInt16>]
 [-HttpsCertificateThumbprint <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### http 和 https
```
Set-HgsServer [-Http] [-Https] [-HttpPort <UInt16>] [-HttpsPort <UInt16>] [-HttpsCertificatePath <String>]
 [-HttpsCertificatePassword <SecureString>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### http
```
Set-HgsServer [-Http] [-HttpPort <UInt16>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### httpsThumbprint
```
Set-HgsServer [-Https] [-HttpPort <UInt16>] [-HttpsPort <UInt16>] [-HttpsCertificateThumbprint <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### https
```
Set-HgsServer [-Https] [-HttpsPort <UInt16>] [-HttpsCertificatePath <String>]
 [-HttpsCertificatePassword <SecureString>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### TrustActiveDirectory
```
Set-HgsServer [-TrustActiveDirectory] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### TrustTpm
```
Set-HgsServer [-TrustTpm] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### UpdateMemoryLimit
```
Set-HgsServer [-UpdateMemoryLimit] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-HgsServer` cmdlet 用于设置 Host Guardian Service (HGS) 服务器的配置。变更的配置属性包括通信协议、网络端口以及用于身份验证和密钥保护服务的 HTTPS 证书。

## 示例

### 示例 1：配置 HGS 服务器以使其可以通过 HTTP 访问
```
PS C:\> Set-HgsServer -Http -HttpPort 81
```

此命令配置HGS服务器通过HTTP协议在81端口上对外提供服务。

### 示例 2：配置 HGS 服务器以便通过 HTTP 和 HTTPS 访问
```
PS C:\> Set-HgsServer -Http -Https -HttpsCertificatePath $PathToPfx -HttpsCertificatePassword $PfxSecureString
```

此命令配置HGS服务器在默认端口上同时通过HTTP和HTTPS进行访问。HTTPS通信使用由$PathToPfx指定的证书进行加密保护。

## 参数

### -Http
表示可以通过 HTTP 访问 HGS 服务器。

```yaml
Type: SwitchParameter
Parameter Sets: httpAndHttpsThumbprint, httpAndHttps, http
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HttpPort
指定HTTP端口。

```yaml
Type: UInt16
Parameter Sets: httpAndHttpsThumbprint, httpAndHttps, http, httpsThumbprint
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Https
表示可以通过 HTTPS 访问 HGS 服务器。

```yaml
Type: SwitchParameter
Parameter Sets: httpAndHttpsThumbprint, httpAndHttps, httpsThumbprint, https
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HttpsCertificatePassword
指定用于加密 **HttpsCertificatePath** 中指定的证书文件的密码。

```yaml
Type: SecureString
Parameter Sets: httpAndHttps, https
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HttpsCertificatePath
指定HTTPS证书文件（.pfx）的路径。

```yaml
Type: String
Parameter Sets: httpAndHttps, https
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HttpsCertificateThumbprint
表示HTTPS证书的“指纹”（即用于唯一标识该证书的特征信息）。

```yaml
Type: String
Parameter Sets: httpAndHttpsThumbprint, httpsThumbprint
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HttpsPort
指定 HGS 服务器的 HTTPS 端口。

```yaml
Type: UInt16
Parameter Sets: httpAndHttpsThumbprint, httpAndHttps, httpsThumbprint, https
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TrustActiveDirectory
表示该cmdlet将认证服务（Attestation service）的操作模式设置为“Active Directory”。

```yaml
Type: SwitchParameter
Parameter Sets: TrustActiveDirectory
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TrustTpm
表示此 cmdlet 将认证服务（Attestation service）的操作模式设置为“受信任平台模块”（Trusted Platform Module，简称 TPM）。

```yaml
Type: SwitchParameter
Parameter Sets: TrustTpm
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UpdateMemoryLimit
表示应该更新身份验证服务的应用程序池内存限制，以反映系统中当前的实际物理内存用量。

```yaml
Type: SwitchParameter
Parameter Sets: UpdateMemoryLimit
Aliases:

Required: True
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

## 备注

## 相关链接

[HGS 服务器Cmdlets](./hgsserver.md)

