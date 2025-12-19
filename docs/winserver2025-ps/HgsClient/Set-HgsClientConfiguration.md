---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsClient-help.xml
Module Name: HgsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsclient/set-hgsclientconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-HgsClientConfiguration
---

# Set-HgsClientConfiguration

## 摘要
修改Host Guardian Service客户端的相关配置。

## 语法

### ChangeToLocalMode
```
Set-HgsClientConfiguration [-EnableLocalMode] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### FullSecureHostingServiceMode
```
Set-HgsClientConfiguration -KeyProtectionServerUrl <String> -AttestationServerUrl <String>
 -FallbackKeyProtectionServerUrl <String> -FallbackAttestationServerUrl <String> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### SecureHostingServiceMode
```
Set-HgsClientConfiguration -KeyProtectionServerUrl <String> -AttestationServerUrl <String> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-HgsClientConfiguration` cmdlet 用于修改主机防护服务（Host Guardian Service）客户端的相关配置。您可以在本地模式或主机防护服务模式下对客户端进行配置。在本地模式下，不涉及任何身份验证过程，且客户端会自行保管密钥材料。

## 示例

### 示例 1：设置认证服务器和密钥保护服务器
```
PS C:\> Set-HgsClientConfiguration -AttestationServerUrl "https://DemoHgs.Contoso.com/Attestation" -KeyProtectionServerUrl "https://DemoHgs.Contoso.com/KeyProtection"
```

此命令用于配置认证客户端（attestation client）和密钥保护客户端（key protection client）所使用的URL。使用该命令可以将本地主机设置为在Host Guardian Service模式下运行。

### 示例 2：将模式更改为“本地”（Local）
```
PS C:\> Set-HgsClientConfiguration -EnableLocalMode
```

此命令将Host Guardian Service客户端从“Host Guardian Service模式”切换为“本地模式”。同时，该命令还会重置证书颁发服务器（attestation server）的URL和密钥保护服务器（key protection server）的URL。

## 参数

### -AttestationServerUrl
指定证书颁发服务器的 URL。处于“安全托管服务”（Secure Hosting Service）模式的 Host Guardian Service 客户端会使用此参数所指定的服务器。

```yaml
Type: String
Parameter Sets: FullSecureHostingServiceMode, SecureHostingServiceMode
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableLocalMode
该命令行工具用于将客户端的工作模式从“Host Guardian Service”更改为“Local”模式。当模式切换到“Local”时，会重置认证服务器（attestation server）和密钥保护服务器（key protection server）的URL地址。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: ChangeToLocalMode
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FallbackAttestationServerUrl
指定在无法访问主要认证服务器时使用的认证服务器的URL。

```yaml
Type: String
Parameter Sets: FullSecureHostingServiceMode
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -FallbackKeyProtectionServerUrl
指定在无法访问主认证服务器时使用的密钥保护服务器的URL。

```yaml
Type: String
Parameter Sets: FullSecureHostingServiceMode
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -KeyProtectionServerUrl
指定密钥保护服务器的 URL。处于“安全托管服务”（Secure Hosting Service）模式的 Host Guardian Service 客户端会使用该参数所指定的服务器。

```yaml
Type: String
Parameter Sets: FullSecureHostingServiceMode, SecureHostingServiceMode
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前会提示您进行确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于通用参数（about_CommonParameters）的文档：http://go.microsoft.com/fwlink/?LinkID=113216。

## 输入

## 输出

### CimInstance#MSFT_HgsClientConfiguration
一个HGS客户端配置对象，其中包含有关操作模式、已配置的URL以及最近一次认证尝试的结果（如适用）。

## 备注

## 相关链接

[Get-HgsClientConfiguration](./Get-HgsClientConfiguration.md)

