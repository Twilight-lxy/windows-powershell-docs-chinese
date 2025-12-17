---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfswebapplicationproxyrelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsWebApplicationProxyRelyingPartyTrust
---

# 添加 AdfsWebApplicationProxyRelyingPartyTrust

## 摘要
为Web应用程序代理添加一个依赖方信任（relying party trust）。

## 语法

```
Add-AdfsWebApplicationProxyRelyingPartyTrust [-Name] <String> [-Identifier] <String[]>
 [-AlwaysRequireAuthentication] [-Enabled <Boolean>] [-AccessControlPolicyName <String>]
 [-AccessControlPolicyParameters <Object>] [-AdditionalAuthenticationRules <String>]
 [-AdditionalAuthenticationRulesFile <String>] [-NotBeforeSkew <Int32>] [-Notes <String>] [-PassThru]
 [-TokenLifetime <Int32>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-AdfsWebApplicationProxyRelyingPartyTrust` cmdlet 用于为 Web 应用程序代理（Web Application Proxy）添加依赖方信任关系。通过该代理访问内部 Web 应用程序时，需要依赖于这种信任关系来实施身份验证和授权策略。默认情况下，在部署 Web 应用程序代理时，系统会自动创建相应的依赖方信任关系。

Web应用程序代理（Web Application Proxy）所依赖的第三方信任机制对于管理来自企业网络外部的全球网络访问非常有用。通过设置身份验证和授权策略，管理员可以限制对通过Web应用程序代理发布的内部Web应用程序和服务的使用权限。

## 示例

#### 示例 1：添加依赖方信任（Relying Party Trust）
```
PS C:\> Add-AdfsWebApplicationProxyRelyingPartyTrust
```

此命令用于添加 Web 应用程序代理的依赖方信任关系。在首次部署 Web 应用程序代理角色服务时，该信任关系默认是存在的。仅当您删除了 Web 应用程序代理的依赖方信任关系时，才需要使用此示例。

## 参数

### -AccessControlPolicyName
指定访问控制策略的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AccessControlPolicyParameters
指定访问控制策略的参数。

```yaml
Type: Object
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AdditionalAuthenticationRules
用于指定代理服务器上额外的身份验证规则。有关这些规则所使用的声明语言的更多信息，请参阅TechNet上的[Understanding Claim Rule Language in AD FS 2.0 & Higher](https://social.technet.microsoft.com/wiki/contents/articles/4792.understanding-claim-rule-language-in-ad-fs-2-0-higher.aspx)。

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

### -AdditionalAuthenticationRulesFile
指定一个文件，该文件包含用于此依赖方进行额外身份验证的规则。

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

### -AlwaysRequireAuthentication
这表示即使代理之前已经验证过用户的身份信息，访问某些资源时仍然需要用户进行身份认证。设置此参数后，用户在使用敏感资源时必须始终提供有效的身份凭证。

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

### -Enabled
该参数用于指示是否启用对该依赖方的信任。如果设置为 `$True`，则允许对代理进行身份验证和授权操作。

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

### -Identifier
指定一个包含唯一标识符的数组。当代理发起登录请求以获取自己的令牌时，它会使用您指定的这些标识符来表明其所对应的依赖方信任关系。其他任何实体均不得使用该列表中的任何标识符。按照常规做法，您可以使用统一资源标识符（URI）作为依赖方信任关系的唯一标识符，或者使用任何字符串。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个名称。该cmdlet会添加一个Web应用程序代理（Web Application Proxy）的依赖方信任关系，并为其设置您指定的友好名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NotBeforeSkew
该参数用于指定时间戳的“偏斜量”（以整数形式表示），该时间戳标志着有效期开始的时刻。数值越大，有效期相对于为依赖方发放凭证的时间点而言就越早开始。默认情况下，此值为0。如果在Web应用程序代理（WAP）依赖方处验证失败（因为有效期尚未开始），请指定一个正数作为该偏斜量。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Notes
用于指定相关说明或备注。该cmdlet会存储您为Web应用程序代理（Web Application Proxy）的依赖方信任机制所指定的这些说明或备注内容。

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

### -TokenLifetime
指定了发放给依赖方的声明的有效期限（以分钟为单位）。

```yaml
Type: Int32
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
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

[禁用 AdfsWebApplicationProxy 依赖方信任功能](./Disable-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Enable-AdfsWebApplicationProxyRelyingPartyTrust](./Enable-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Get-AdfsWebApplicationProxyRelyingPartyTrust](./Get-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Remove-AdfsWebApplicationProxyRelyingPartyTrust](./Remove-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Set-AdfsWebApplicationProxyRelyingPartyTrust](./Set-AdfsWebApplicationProxyRelyingPartyTrust.md)

