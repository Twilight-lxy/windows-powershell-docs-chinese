---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/import-adfsauthenticationproviderconfigurationdata?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-AdfsAuthenticationProviderConfigurationData
---

# 导入 AdfsAuthenticationProviderConfigurationData

## 摘要
导入用于身份验证提供者的自定义配置。

## 语法

```
Import-AdfsAuthenticationProviderConfigurationData -Name <String> -FilePath <String> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Import-AdfsAuthenticationProviderConfigurationData` cmdlet 用于从文件中导入身份验证提供者的自定义配置。在使用此 cmdlet 之前，请确保外部身份验证提供者支持自定义配置。

在您初次注册身份验证提供者之后，如果与该身份验证提供者相关的信息发生变化，请使用此 cmdlet。在某些情况下，用于访问身份验证服务的安全密钥可能会更改，因此必须更新 Active Directory Federation Services (AD FS) 配置存储中的相关信息，以确保身份验证提供者能够正常运行。

## 示例

### 示例 1：导入身份验证提供程序配置数据
```
PS C:\> Import-AdfsAuthenticationProviderConfigurationData -Name "ContosoExternalAuthProvider" -FilePath "C:\share\test.txt"
```

此命令用于导入认证提供者的配置数据。同时，该命令还会用文件中的数据覆盖指定认证提供者现有的配置数据。

## 参数

### -FilePath
指定一个文件路径。该 cmdlet 会从您指定的文件中导入配置数据。

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
指定要导入的身份验证提供者的名称。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[Export-AdfsAuthenticationProviderConfigurationData](./Export-AdfsAuthenticationProviderConfigurationData.md)

