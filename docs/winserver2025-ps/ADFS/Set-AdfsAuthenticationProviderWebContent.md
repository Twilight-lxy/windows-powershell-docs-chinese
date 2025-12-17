---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsauthenticationproviderwebcontent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsAuthenticationProviderWebContent
---

# 设置 AdfsAuthenticationProviderWebContent

## 摘要
修改显示名称和描述信息。

## 语法

### IdentifierName（默认值）
```
Set-AdfsAuthenticationProviderWebContent [-DisplayName <String>] [-Description <String>]
 [-UserNotProvisionedErrorMessage <String>] [-PassThru] [[-Locale] <CultureInfo>] -Name <String> [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### IdentifierObject
```
Set-AdfsAuthenticationProviderWebContent [-DisplayName <String>] [-Description <String>]
 [-UserNotProvisionedErrorMessage <String>] [-PassThru] [-TargetWebContent] <AdfsAuthProviderWebContent>
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsAuthenticationProviderWebContent` cmdlet 用于修改认证提供者的显示名称和描述。使用此 cmdlet 可以将认证提供者的名称自定义为更易于用户理解和使用的名称。您可以选择指定一个区域设置（locale），或者将 *Locale* 参数设置为空字符串，以确保名称在所有系统中都保持不变。

## 示例

### 示例 1：修改认证提供者的网页内容
```
PS C:\> Set-AdfsAuthenticationProviderWebContent -Name MultiFactorAuthentication -DisplayName "User Friendly Name for Multifactor Authentication" -Description "Description of your choice"
```

此命令会修改用户在使用 Active Directory Federation Services (AD FS) 登录页面时所看到的身份验证提供者的显示名称和描述信息。

## 参数

### -Description
指定一个描述性信息。该cmdlet会根据您提供的描述来修改提供者（provider）的网页内容。

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

### -DisplayName
指定一个显示名称。该cmdlet会根据您指定的显示名称来修改提供者（provider）的网页内容。

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

### -Locale
用于指定一个区域设置（locale）。该cmdlet会修改与你所指定的区域设置相关联的提供者网页内容。

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
指定正在修改其网页内容的身份验证提供者的名称。要查找可用的身份验证提供者列表，请运行 `Get-AdfsAuthenticationProvider` 命令。每个返回的提供者都有一个 **Name** 属性，可以使用该属性值作为此参数的值。

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

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不生成任何输出。

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

### -TargetWebContent
指定一个由流水线使用的 **AdfsAuthenticationProviderWebContent** 对象。

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

### -UserNotProvisionedErrorMessage
为未为用户分配资源的情况指定一条错误消息。

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

[Remove-AdfsAuthenticationProviderWebContent](./Remove-AdfsAuthenticationProviderWebContent.md)

