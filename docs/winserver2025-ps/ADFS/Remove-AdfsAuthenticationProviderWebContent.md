---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsauthenticationproviderwebcontent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsAuthenticationProviderWebContent
---

# 删除 AdfsAuthenticationProviderWebContent

## 摘要
从 AD FS 的用户登录网页中移除了身份验证提供者的 Web 内容自定义功能。

## 语法

### IdentifierName（默认值）
```
Remove-AdfsAuthenticationProviderWebContent [[-Locale] <CultureInfo>] -Name <String> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### IdentifierObject
```
Remove-AdfsAuthenticationProviderWebContent [-TargetWebContent] <AdfsAuthProviderWebContent> [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-AdfsAuthenticationProviderWebContent` cmdlet 用于删除 Active Directory Federation Services (AD FS) 服务中用户登录网页上与身份验证提供程序相关的自定义网页内容。

## 示例

### 示例 1：移除认证提供者的网页内容
```
PS C:\> Remove-AdfsAuthenticationProviderWebContent -Name "ContosoAuthenticationProvider"
```

此命令会删除名为 ContosoAuthenticationProvider 的身份验证提供程序的相关网页内容（即其 Web 内容）。

## 参数

### -Locale
用于指定一个区域设置（locale）。该cmdlet会删除与您指定的区域设置相关联的提供程序网页内容。

```yaml
Type: CultureInfo
Parameter Sets: IdentifierName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
用于指定一个名称。该cmdlet会获取与您指定的名称关联的提供程序网页内容。

```yaml
Type: String
Parameter Sets: IdentifierName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetWebContent
指定一个由管道使用的 **AdfsAuthenticationProviderWebContent** 对象。

```yaml
Type: AdfsAuthProviderWebContent
Parameter Sets: IdentifierObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-AdfsAuthenticationProviderWebContent](./Get-AdfsAuthenticationProviderWebContent.md)

[Set-AdfsAuthenticationProviderWebContent](./Set-AdfsAuthenticationProviderWebContent.md)

