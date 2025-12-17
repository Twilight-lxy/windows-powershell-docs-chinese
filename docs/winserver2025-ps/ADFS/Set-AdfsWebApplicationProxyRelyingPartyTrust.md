---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfswebapplicationproxyrelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsWebApplicationProxyRelyingPartyTrust
---

# 设置 AdfsWebApplicationProxy 依赖的第三方信任关系（Set-AdfsWebApplicationProxyRelyingPartyTrust）

## 摘要
修改用于 Web 应用程序代理的依赖方信任对象的属性。

## 语法

```
Set-AdfsWebApplicationProxyRelyingPartyTrust [-AlwaysRequireAuthentication <Boolean>] [-Identifier <String[]>]
 [-AccessControlPolicyName <String>] [-AccessControlPolicyParameters <Object>]
 [-IssuanceAuthorizationRules <String>] [-IssuanceAuthorizationRulesFile <String>]
 [-IssuanceTransformRules <String>] [-IssuanceTransformRulesFile <String>]
 [-AdditionalAuthenticationRules <String>] [-AdditionalAuthenticationRulesFile <String>] [-Name <String>]
 [-NotBeforeSkew <Int32>] [-Notes <String>] [-PassThru] [-TokenLifetime <Int32>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-AdfsWebApplicationProxyRelyingPartyTrust` cmdlet 用于修改与 Web 应用程序代理相关的依赖方信任对象（relying party trust object）的属性。你可以通过该 cmdlet 修改身份验证和授权策略，从而控制所有通过该代理进行的外部访问。

## 示例

### 示例 1：通过使用文件来指定授权规则
```
PS C:\> Set-AdfsWebApplicationProxyRelyingPartyTrust -IssuanceAuthorizationRulesFile "C:\Rules\RulesFile07"
```

该命令为 Web 应用程序代理（Web Application Proxy）的依赖方信任机制指定了授权规则，这些规则来自于一个包含具体规则的文件。

## 参数

### -AccessControlPolicyName
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
指定访问控制策略参数。

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
用于指定代理服务器上额外身份验证的规则。有关这些规则的声明语言的更多信息，请参阅 TechNet 上的 [Understanding Claim Rule Language in AD FS 2.0 & Higher](https://social.technet.microsoft.com/wiki/contents/articles/4792.understanding-claim-rule-language-in-ad-fs-2-0-higher.aspx)。

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
指定一个文件，该文件包含用于此依赖方额外身份验证的规则。

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
该属性用于指示访问是否需要身份验证，即使依赖方之前已经使用有效的凭据进行过身份验证。如果设置为 `$True`，则用户必须始终提供凭据才能访问敏感资源。

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
指定一个包含唯一标识符的数组。当代理发起登录请求以获取自己的令牌时，它会使用您指定的这些标识符来表明其对应的依赖方信任关系。其他任何信任关系都不能使用该列表中的标识符。按照常规做法，您可以使用统一资源标识符（URIs）作为依赖方信任关系的唯一标识符，或者使用任何字符串。

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

### -IssuanceAuthorizationRules
指定向该依赖方发放声明（claims）的授权规则。这些授权规则用于控制对通过 Active Directory Federation Services (AD FS) 实现预身份验证的应用程序的访问权限，随后用户可通过代理来访问这些应用程序。默认情况下，所有已认证的用户都可以访问这些应用程序。

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

### -IssuanceAuthorizationRulesFile
指定一个文件，该文件包含向该依赖方发放声明（claims）所需的授权规则。

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

### -IssuanceTransformRules
指定用于向该依赖方发放声明的发行转换规则。通常情况下，您不应修改此设置的值。

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

### -IssuanceTransformRulesFile
指定一个文件，该文件包含用于向此依赖方发放声明（claims）的转换规则（transformation rules）。

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
指定一个名称。该cmdlet会修改Web应用程序代理（Web Application Proxy）中的依赖方信任设置，使其使用您指定的友好名称进行显示。

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

### -NotBeforeSkew
该参数用于指定时间戳的偏移量（以整数形式表示），该时间戳标志着有效期的开始。数值越大，表示有效期相对于为依赖方颁发声明的时间来说起始得更早。默认值为 0。如果在 Web 应用程序代理依赖方的验证过程中失败（因为有效期尚未开始），请指定一个正数。

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
用于指定相关说明或备注。该cmdlet会存储您为Web应用程序代理（Web Application Proxy）的“依赖方信任”（dependant party trust）机制所指定的这些说明或备注信息。

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
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

## 备注

## 相关链接

[Add-AdfsWebApplicationProxyRelyingPartyTrust](./Add-AdfsWebApplicationProxyRelyingPartyTrust.md)

[禁用 AdfsWebApplicationProxy 依赖的第三方信任设置](./Disable-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Enable-AdfsWebApplicationProxyRelyingPartyTrust](./Enable-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Get-AdfsWebApplicationProxyRelyingPartyTrust](./Get-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Remove-AdfsWebApplicationProxyRelyingPartyTrust](./Remove-AdfsWebApplicationProxyRelyingPartyTrust.md)

