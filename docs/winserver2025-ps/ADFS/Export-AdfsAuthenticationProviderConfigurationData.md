---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/export-adfsauthenticationproviderconfigurationdata?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-AdfsAuthenticationProviderConfigurationData
---

# 导出 AdfsAuthenticationProviderConfigurationData 数据

## 摘要
返回一个文件，其中包含用于配置AD FS农场以支持Azure MFA的租户ID，以及知名的Azure MFA客户端ID。

## 语法

```
Export-AdfsAuthenticationProviderConfigurationData -Name <String> -FilePath <String> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Export-AdfsAuthenticationProviderConfigurationData` cmdlet 会返回一个文件，其中包含用于配置 Active Directory Federation Services (AD FS) 农场以支持 Azure MFA 的租户 ID，以及 Azure MFA 所使用的客户端 ID。

在使用此cmdlet之前，请确认外部身份验证提供程序支持自定义配置。

## 示例

### 示例 1：导出配置数据
```
PS C:\> Export-AdfsAuthenticationProviderConfigurationData -Name "ContosoExternalAuthProvider" -FilePath "C:\share\test.txt"
```

该命令将名为 ContosoExternalAuthProvider 的身份验证提供者的配置数据导出到文件 C:\share\test.txt 中。

### 示例 2：确定 Azure MFA 使用的是哪种证书
```
PS C:\> New-AdfsAzureMfaTenantCertificate -TenantID <your tenant ID> - FilePath amfacert.cer
```

在为 Azure MFA 配置了 AD FS 之后，此命令用于确定 Azure MFA 使用的是哪张证书。

## 参数

### -FilePath
指定用于输出配置信息的文本文件的路径和文件名。

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

### -Name
指定要导出的身份验证提供者的名称，例如 AzureMfaAuthentication。

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

## 输出

### System.Object

## 备注

## 相关链接

[Import-AdfsAuthenticationProviderConfigurationData](./Import-AdfsAuthenticationProviderConfigurationData.md)

