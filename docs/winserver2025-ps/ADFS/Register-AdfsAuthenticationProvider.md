---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/register-adfsauthenticationprovider?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Register-AdfsAuthenticationProvider
---

# 注册 AdfsAuthenticationProvider

## 摘要
在 AD FS 中注册一个外部身份验证提供程序。

## 语法

```
Register-AdfsAuthenticationProvider -TypeName <String> -Name <String> [-ConfigurationFilePath <String>]
 [<CommonParameters>]
```

## 描述
`Register-AdfsAuthenticationProvider` cmdlet 将外部身份验证提供程序注册为 Active Directory Federation Services (AD FS) 中的提供程序。可以使用 `Get-AdfsAuthenticationProvider` cmdlet 来获取已注册的身份验证提供程序列表。

## 示例

### 示例 1：注册一个身份验证提供者
```
PS C:\> $TypeName = "ExternalAuthMethod.ExternalAuthProvider, ExternalAuthProvider, Version=1.0.0.0, Culture=neutral, PublicKeyToken=365143bb27e7ac8b, processorArchitecture=MSIL"
PS C:\> Register-AdfsAuthenticationProvider -TypeName $TypeName -Name "MyExternalAuthProvider" -ConfigurationFilePath ".\configdata.txt"
```

第一个命令创建了一个名为 `$TypeName` 的变量，该变量包含了外部提供者的配置数据。

第二个命令使用存储在 `$TypeName` 变量中的数据来注册身份验证提供者。

## 参数

### -ConfigurationFilePath
指定包含身份验证提供程序配置数据的文件的完整路径。

您还可以将文件上传到 Active Directory Federation Services (AD FS) 的配置存储中，以便身份验证提供商可以使用该文件。如果您在初始化身份验证提供商时需要提供与特定客户相关的额外信息，请使用此方法。任何对该方法的使用都取决于提供该身份验证提供商的供应商。

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

### -Name
指定要在 AD FS 中注册的身份验证提供程序的名称。

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

### -TypeName
指定联合服务器上身份验证提供程序程序集的完全限定类型。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[Get-AdfsAuthenticationProvider](./Get-AdfsAuthenticationProvider.md)

[Unregister-AdfsAuthenticationProvider](./Unregister-AdfsAuthenticationProvider.md)

