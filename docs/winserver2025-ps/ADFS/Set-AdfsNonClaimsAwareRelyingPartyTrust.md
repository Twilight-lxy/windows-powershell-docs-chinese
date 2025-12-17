---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsnonclaimsawarerelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsNonClaimsAwareRelyingPartyTrust
---

# 设置 AdfsNonClaimsAwareRelyingPartyTrust

## 摘要
为不支持 claims（声明）处理的 Web 应用程序或服务设置依赖方信任（relying party trust）的属性。

## 语法

### 标识符Name（默认值）
```
Set-AdfsNonClaimsAwareRelyingPartyTrust [-AlwaysRequireAuthentication] [-Identifier <String[]>]
 [-IssuanceAuthorizationRules <String>] [-IssuanceAuthorizationRulesFile <String>] [-Name <String>]
 [-Notes <String>] [-PassThru] [-AdditionalAuthenticationRules <String>]
 [-AdditionalAuthenticationRulesFile <String>] [-AccessControlPolicyName <String>]
 [-AccessControlPolicyParameters <Object>] [-ClaimsProviderName <String[]>] [-TargetName] <String> [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 标识符
```
Set-AdfsNonClaimsAwareRelyingPartyTrust [-AlwaysRequireAuthentication] [-Identifier <String[]>]
 [-IssuanceAuthorizationRules <String>] [-IssuanceAuthorizationRulesFile <String>] [-Name <String>]
 [-Notes <String>] [-PassThru] [-AdditionalAuthenticationRules <String>]
 [-AdditionalAuthenticationRulesFile <String>] [-AccessControlPolicyName <String>]
 [-AccessControlPolicyParameters <Object>] [-ClaimsProviderName <String[]>] -TargetIdentifier <String>
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 标识符Object
```
Set-AdfsNonClaimsAwareRelyingPartyTrust [-AlwaysRequireAuthentication] [-Identifier <String[]>]
 [-IssuanceAuthorizationRules <String>] [-IssuanceAuthorizationRulesFile <String>] [-Name <String>]
 [-Notes <String>] [-PassThru] [-AdditionalAuthenticationRules <String>]
 [-AdditionalAuthenticationRulesFile <String>] [-AccessControlPolicyName <String>]
 [-AccessControlPolicyParameters <Object>] [-ClaimsProviderName <String[]>]
 -TargetNonClaimsAwareRelyingPartyTrust <NonClaimsAwareRelyingPartyTrust> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-AdfsNonClaimsAwareRelyingPartyTrust` 这个 cmdlet 用于为不支持声明处理（non-claims-aware）的 Web 应用程序或服务配置相关属性。

一种“不关注声明（non-claims-aware）的依赖方信任”是指适用于那些不直接依赖 Active Directory Federation Services (AD FS) 来生成令牌的 Web 应用程序或服务的依赖方信任模型。这类信任模型会依赖于第三方来处理这些令牌，并将其转换成应用程序能够识别的格式。对于那些不使用 AD FS 生成的令牌的 Web 应用程序和服务来说，这种信任模型非常有助于定义相应的身份验证和授权策略。Web Application Proxy 会为来自网络外部的请求，在通过代理进行预身份验证时请求这些令牌。

## 示例

#### 示例 1：将不支持“非声明性认证”（non-claims-aware）的依赖方信任设置为始终强制进行身份验证
```
PS C:\> Set-AdfsNonClaimsAwareRelyingPartyTrust -TargetName "ExpenseReport" -AlwaysRequireAuthentication $True
```

此命令为名为“ExpenseReport”的应用程序设置了“不支持声明验证（non-claims-aware）”的依赖方信任模式，该模式会始终强制要求用户进行身份认证。

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
为依赖方指定额外的身份验证规则。有关这些规则的声明语言的更多信息，请参阅TechNet上的[Understanding Claim Rule Language in AD FS 2.0 & Higher](https://social.technet.microsoft.com/wiki/contents/articles/4792.understanding-claim-rule-language-in-ad-fs-2-0-higher.aspx)。

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
指定包含依赖方所有额外身份验证规则的文件。

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
表示即使该依赖方之前已经使用过认证凭据进行过访问，仍然需要再次进行身份验证。指定此参数可强制用户始终提供凭据才能访问敏感资源。

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

### -ClaimsProviderName
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

### -Identifier
指定一个用于表示“非声明感知型”（non-claims-aware）依赖方信任的唯一标识符数组。其他任何信任关系都不得使用该列表中的标识符。按照常规做法，您可以使用统一资源标识符（URIs）作为依赖方信任的唯一标识符，或者使用任意字符串作为标识符。

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
指定了向依赖方颁发声明（claims）时的授权规则。

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

### -IssuanceAuthorizationRulesFile
指定包含授权规则的文件，这些规则用于向依赖方发放声明（claims）。

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
指定一个名称。该cmdlet会添加具有您所指定的显示名称的Web应用程序代理（Web Application Proxy）依赖方信任关系（dependency trust）。

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

### -Notes
指定一个名称。该cmdlet会添加具有您所指定的显示名称的Web应用程序代理（Web Application Proxy）依赖方信任关系（dependency trust）。

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
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -TargetIdentifier
指定需要修改的、不支持“声明处理”（claims-aware）功能的依赖方信任（relying party trust）的标识符。

```yaml
Type: String
Parameter Sets: Identifier
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetName
指定需要修改的、不支持处理声明（claims）的依赖方信任（relying party trust）的名称。

```yaml
Type: String
Parameter Sets: IdentifierName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetNonClaimsAwareRelyingPartyTrust
指定一个 **NonClaimsAwareRelyingPartyTrust** 对象。该 cmdlet 会删除您所指定的、不支持处理身份声明（claims）的依赖方信任关系。若要获取一个 **NonClaimsAwareRelyingPartyTrust** 对象，可以使用 **Get-AdfsNonClaimsAwareRelyingPartyTrust** cmdlet。

```yaml
Type: NonClaimsAwareRelyingPartyTrust
Parameter Sets: IdentifierObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[添加 AdfsNonClaimsAwareRelyingPartyTrust](./Add-AdfsNonClaimsAwareRelyingPartyTrust.md)

[禁用 AdfsNonClaimsAwareRelyingPartyTrust](./Disable-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Enable-AdfsNonClaimsAwareRelyingPartyTrust](./Enable-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Get-AdfsNonClaimsAwareRelyingPartyTrust](./Get-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Remove-AdfsNonClaimsAwareRelyingPartyTrust](./Remove-AdfsNonClaimsAwareRelyingPartyTrust.md)

