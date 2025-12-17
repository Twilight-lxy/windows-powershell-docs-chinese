---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfswebapiapplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsWebApiApplication
---

# 添加 AdfsWebApi 应用程序

## 摘要
将一个Web API应用程序角色添加到AD FS中的应用程序中。

## 语法

### ApplicationGroupIdentifier（默认值）
```
Add-AdfsWebApiApplication [-ApplicationGroupIdentifier] <String> -Name <String> -Identifier <String[]>
 [-AllowedAuthenticationClassReferences <String[]>] [-ClaimsProviderName <String[]>]
 [-IssuanceAuthorizationRules <String>] [-IssuanceAuthorizationRulesFile <String>]
 [-DelegationAuthorizationRules <String>] [-DelegationAuthorizationRulesFile <String>]
 [-ImpersonationAuthorizationRules <String>] [-ImpersonationAuthorizationRulesFile <String>]
 [-IssuanceTransformRules <String>] [-IssuanceTransformRulesFile <String>]
 [-AdditionalAuthenticationRules <String>] [-AdditionalAuthenticationRulesFile <String>]
 [-AccessControlPolicyName <String>] [-AccessControlPolicyParameters <Object>] [-NotBeforeSkew <Int32>]
 [-Description <String>] [-TokenLifetime <Int32>] [-AlwaysRequireAuthentication]
 [-AllowedClientTypes <AllowedClientTypes>] [-IssueOAuthRefreshTokensTo <RefreshTokenIssuanceDeviceTypes>]
 [-RefreshTokenProtectionEnabled <Boolean>] [-RequestMFAFromClaimsProviders] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ApplicationGroupObject
```
Add-AdfsWebApiApplication [-ApplicationGroup] <ApplicationGroup> -Name <String> -Identifier <String[]>
 [-AllowedAuthenticationClassReferences <String[]>] [-ClaimsProviderName <String[]>]
 [-IssuanceAuthorizationRules <String>] [-IssuanceAuthorizationRulesFile <String>]
 [-DelegationAuthorizationRules <String>] [-DelegationAuthorizationRulesFile <String>]
 [-ImpersonationAuthorizationRules <String>] [-ImpersonationAuthorizationRulesFile <String>]
 [-IssuanceTransformRules <String>] [-IssuanceTransformRulesFile <String>]
 [-AdditionalAuthenticationRules <String>] [-AdditionalAuthenticationRulesFile <String>]
 [-AccessControlPolicyName <String>] [-AccessControlPolicyParameters <Object>] [-NotBeforeSkew <Int32>]
 [-Description <String>] [-TokenLifetime <Int32>] [-AlwaysRequireAuthentication]
 [-AllowedClientTypes <AllowedClientTypes>] [-IssueOAuthRefreshTokensTo <RefreshTokenIssuanceDeviceTypes>]
 [-RefreshTokenProtectionEnabled <Boolean>] [-RequestMFAFromClaimsProviders] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-AdfsWebApiApplication` cmdlet 用于在 Active Directory Federation Services (AD FS) 中为某个应用程序添加一个 Web API 应用程序角色。

## 示例

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
指定额外的身份验证规则。

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

### -AdditionalAuthenticationRulesFile
指定一个文件，该文件包含了用于此依赖方（relying party）的附加身份验证（additional authentication）的所有规则。

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

### -AllowedAuthenticationClassReferences
指定一个允许身份验证的类引用数组。

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

### -AllowedClientTypes
指定允许的客户端类型。此参数的可接受值为：

- None
- Public
- Confidential

```yaml
Type: AllowedClientTypes
Parameter Sets: (All)
Aliases:
Accepted values: None, Public, Confidential

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AlwaysRequireAuthentication
这表示该 Web API 应用程序角色始终需要身份验证，即使之前已经通过身份验证获得了访问权限。指定此参数可以强制用户在使用敏感资源时始终提供有效的身份凭证。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ApplicationGroup
指定一个应用程序组。

```yaml
Type: ApplicationGroup
Parameter Sets: ApplicationGroupObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ApplicationGroupIdentifier
指定一个应用程序组的ID。

```yaml
Type: String
Parameter Sets: ApplicationGroupIdentifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -ClaimsProviderName
指定一个声明提供者名称数组，您可以为依赖方信任（Relying Party Trust）在家庭领域发现（Home Realm Discovery, HRD）场景中配置这些提供者。

如果为依赖方指定了声明提供者的名称，那么“归属域发现”页面将仅显示该依赖方的那些声明提供者。如果只指定了一个声明提供者的名称，则不会显示“归属域发现”页面。用户会被重定向到该声明提供者进行身份验证。

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

### -DelegationAuthorizationRules
指定委托授权规则。

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

### -DelegationAuthorizationRulesFile
指定一个文件，该文件包含了该依赖方进行委托认证所需的所有规则。

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

### -Description
指定一个描述信息。

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

### -Identifier
指定一个标识符数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ImpersonationAuthorizationRules
指定身份冒用授权规则。

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

### -ImpersonationAuthorizationRulesFile
指定一个文件，该文件包含了用于此依赖方进行身份冒用认证的所有规则。

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

### -IssuanceAuthorizationRules
指定发行授权规则。

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
指定一个文件，其中包含该依赖方进行身份验证（即授权过程）所需的所有规则。

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
指定发行转换规则。

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
指定一个文件，该文件包含了用于此依赖方（relying party）的所有规则。这些规则用于实现发行转换（issuance transformation）过程。

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

### -IssueOAuthRefreshTokensTo
指定用于生成刷新令牌的设备类型。该参数的可接受值包括：

- NoDevice
- WorkplaceJoinedDevices
- AllDevices

```yaml
Type: RefreshTokenIssuanceDeviceTypes
Parameter Sets: (All)
Aliases:
Accepted values: NoDevice, WorkplaceJoinedDevices, AllDevices

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个名称。

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

### -NotBeforeSkew
指定“not before skew”值。

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

### -PassThru
返回一个表示您正在操作的该项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -RefreshTokenProtectionEnabled
表示是否启用了刷新令牌保护功能。

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

### -RequestMFAFromClaimsProviders
表示使用了“来自声明提供者的多因素身份验证（MFA）请求”这一选项。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TokenLifetime
指定令牌的有效期（即令牌的使用时间）。

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
在运行该cmdlet之前，会提示您确认是否要执行该操作。

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

`String` 对象会被传递给 `AccessControlPolicyName`, `AdditionalAuthenticationRules`, `ApplicationGroupIdentifier`, `DelegationAuthorizationRules`, `ImpersonationAuthorizationRules`, `IssuanceAuthorizationRules`, 和 `IssuanceTransformRules` 这些参数。

### System.Object

对象是通过 *AccessControlPolicyParameters* 参数接收的。

### System.Management.Automation.SwitchParameter

`SwitchParameter` 对象会被 `AlwaysRequireAuthentication` 和 `RequestMFAFromClaimsProviders` 参数接收。

### MicrosoftIdentityServer.ManagementResources.ApplicationGroup

`ApplicationGroup` 对象是通过 `ApplicationGroup` 参数接收到的。

## 输出

### Microsoft.IdentityServer.ManagementResources.WebApiApplication

当指定了 `PassThru` 参数时，会返回一个新的 `WebApiApplication` 对象。默认情况下，此 cmdlet 不会产生任何输出。

## 备注

## 相关链接

[Get-AdfsWebApiApplication](./Get-AdfsWebApiApplication.md)

[Remove-AdfsWebApiApplication](./Remove-AdfsWebApiApplication.md)

[Set-AdfsWebApiApplication](./Set-AdfsWebApiApplication.md)
