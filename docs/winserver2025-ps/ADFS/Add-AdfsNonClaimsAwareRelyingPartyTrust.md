---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfsnonclaimsawarerelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsNonClaimsAwareRelyingPartyTrust
---

# 添加 AdFS 非声明感知型依赖方信任（Add-AdfsNonClaimsAwareRelyingPartyTrust）

## 摘要
向联邦服务添加一个依赖方信任（relaying party trust），该信任代表一个不支持处理身份验证请求（claims）的Web应用程序或服务。

## 语法

```
Add-AdfsNonClaimsAwareRelyingPartyTrust [-Name] <String> [-Identifier] <String[]>
 [-AlwaysRequireAuthentication] [-Enabled <Boolean>] [-IssuanceAuthorizationRules <String>]
 [-IssuanceAuthorizationRulesFile <String>] [-Notes <String>] [-PassThru]
 [-AdditionalAuthenticationRules <String>] [-AdditionalAuthenticationRulesFile <String>]
 [-AccessControlPolicyName <String>] [-AccessControlPolicyParameters <Object>] [-ClaimsProviderName <String[]>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Add-AdfsNonClaimsAwareRelyingPartyTrust** cmdlet 用于为那些不直接依赖 Active Directory Federation Services (AD FS) 来发放令牌的 Web 应用程序或服务创建依赖方信任关系。这些应用程序或服务实际上依赖于第三方来获取令牌，并将令牌转换成它们能够理解的形式。对于不使用 AD FS 令牌的 Web 应用程序和服务来说，这种“非声明感知型”（non-claims-aware）的依赖方信任关系非常有用，因为它可以帮助定义相应的身份验证和授权策略。Web Application Proxy 会为来自网络外部的请求请求这些令牌，以便对这些请求进行预身份验证（pre-authentication）。

## 示例

#### 示例 1：为某个应用程序添加一个不支持声明验证（non-claims-aware）的依赖方信任机制
```
PS C:\> Add-AdfsNonClaimsAwareRelyingPartyTrust -Name "ExpenseReport" -Identifier "https://contosoexpense/" -IssuanceAuthorizationRules "=>issue(Type = "http://schemas.microsoft.com/authorization/claims/permit", Value = "true");"
```

此命令为名为“ExpenseReport”的应用程序添加了一个不支持“claims”（声明）功能的依赖方信任关系，并允许所有经过身份验证的用户通过Web应用代理访问该应用程序。

### 示例 2：添加一个不支持 Claim 处理的依赖方信任机制（relying party trust），以限制对应用程序的访问
```
PS C:\> Add-AdfsNonClaimsAwareRelyingPartyTrust -Name "ExpenseReport" -Identifier "https://contosoexpense/" -IssuanceAuthorizationRules "c:[type=="http://schemas.microsoft.com/2012/01/devicecontext/claims/isregistereduser"]=>issue(Type = "http://schemas.microsoft.com/authorization/claims/permit", Value = "true");"
```

该命令为名为“ExpenseReport”的应用程序添加了一个不支持身份验证（即“非claims-aware”）的依赖方信任设置，并通过Web应用代理限制对该应用程序的访问权限，仅允许来自用户工作场所连接设备的用户才能访问该应用程序。

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
该文档规定了依赖方（relying party）上需要执行的额外身份验证规则。有关这些规则的声明语言（claims language）的更多信息，请参阅TechNet上的[Understanding Claim Rule Language in AD FS 2.0 & Higher](https://social.technet.microsoft.com/wiki/contents/articles/4792.understanding-claim-rule-language-in-ad-fs-2-0-higher.aspx)。

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
表示即使依赖方之前已经使用过认证凭据进行过访问，此次访问仍然需要进行身份验证。指定此参数可确保用户在使用敏感资源时始终需要提供有效的认证凭据。

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

### -Enabled
该参数用于指示是否启用对依赖方的信任机制。若要允许对该依赖方进行身份验证和授权操作，请将此参数的值设置为 `$True`。

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
为不支持“claim-aware”（声明感知）功能的依赖方信任机制指定一个由唯一标识符组成的数组。其他任何信任机制都不能使用该列表中的标识符。按照常规做法，您可以使用统一资源标识符（URIs）作为依赖方信任机制的唯一标识符，或者使用任何字符串来实现这一目的。

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

### -IssuanceAuthorizationRules
规定了向依赖方颁发声明（claims）时的授权规则。

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
指定包含授权规则的文件，这些规则用于向依赖方颁发声明（claims）。

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
指定一个名称。该 cmdlet 会添加具有您所指定的显示名称的 Web 应用程序代理依赖方信任关系。

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

### -Notes
用于为依赖方信任关系指定相关说明或备注。在管理大量应用程序时，可以使用此参数来存储所有者、联系人等信息。

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

### -Confirm
在运行cmdlet之前会提示您进行确认。

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
展示了如果该cmdlet运行会发生的结果。但实际上并没有运行这个cmdlet。

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

[禁用 AdfsNonClaimsAwareRelyingPartyTrust 功能](./ Disable-AdfsNonClaimsAwareRelyingPartyTrust.md)

[ Enable-AdfsNonClaimsAwareRelyingPartyTrust](./Enable-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Get-AdfsNonClaimsAwareRelyingPartyTrust](./Get-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Remove-AdfsNonClaimsAwareRelyingPartyTrust](./Remove-AdfsNonClaimsAwareRelyingPartyTrust.md)

[Set-AdfsNonClaimsAwareRelyingPartyTrust](./Set-AdfsNonClaimsAwareRelyingPartyTrust.md)

