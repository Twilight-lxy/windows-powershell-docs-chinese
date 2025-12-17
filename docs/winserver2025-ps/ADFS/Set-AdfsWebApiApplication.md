---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfswebapiapplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsWebApiApplication
---

# 设置 AdfsWebApi 应用程序

## 摘要
修改 AD FS 中 Web API 应用程序的配置设置。

## 语法

### 标识符（默认值）
```
Set-AdfsWebApiApplication [-TargetIdentifier] <String> [-AllowedAuthenticationClassReferences <String[]>]
 [-AlwaysRequireAuthentication <Boolean>] [-ClaimsProviderName <String[]>] [-Name <String>]
 [-NotBeforeSkew <Int32>] [-Identifier <String[]>] [-IssuanceAuthorizationRules <String>]
 [-IssuanceAuthorizationRulesFile <String>] [-DelegationAuthorizationRules <String>]
 [-DelegationAuthorizationRulesFile <String>] [-ImpersonationAuthorizationRules <String>]
 [-ImpersonationAuthorizationRulesFile <String>] [-IssuanceTransformRules <String>]
 [-IssuanceTransformRulesFile <String>] [-AdditionalAuthenticationRules <String>]
 [-AdditionalAuthenticationRulesFile <String>] [-AccessControlPolicyName <String>]
 [-AccessControlPolicyParameters <Object>] [-Description <String>] [-TokenLifetime <Int32>]
 [-AllowedClientTypes <AllowedClientTypes>] [-IssueOAuthRefreshTokensTo <RefreshTokenIssuanceDeviceTypes>]
 [-RefreshTokenProtectionEnabled <Boolean>] [-RequestMFAFromClaimsProviders <Boolean>] [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 名称
```
Set-AdfsWebApiApplication [-TargetName] <String> [-AllowedAuthenticationClassReferences <String[]>]
 [-AlwaysRequireAuthentication <Boolean>] [-ClaimsProviderName <String[]>] [-Name <String>]
 [-NotBeforeSkew <Int32>] [-Identifier <String[]>] [-IssuanceAuthorizationRules <String>]
 [-IssuanceAuthorizationRulesFile <String>] [-DelegationAuthorizationRules <String>]
 [-DelegationAuthorizationRulesFile <String>] [-ImpersonationAuthorizationRules <String>]
 [-ImpersonationAuthorizationRulesFile <String>] [-IssuanceTransformRules <String>]
 [-IssuanceTransformRulesFile <String>] [-AdditionalAuthenticationRules <String>]
 [-AdditionalAuthenticationRulesFile <String>] [-AccessControlPolicyName <String>]
 [-AccessControlPolicyParameters <Object>] [-Description <String>] [-TokenLifetime <Int32>]
 [-AllowedClientTypes <AllowedClientTypes>] [-IssueOAuthRefreshTokensTo <RefreshTokenIssuanceDeviceTypes>]
 [-RefreshTokenProtectionEnabled <Boolean>] [-RequestMFAFromClaimsProviders <Boolean>] [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### ApplicationObject
```
Set-AdfsWebApiApplication [-TargetApplication] <WebApiApplication>
 [-AllowedAuthenticationClassReferences <String[]>] [-AlwaysRequireAuthentication <Boolean>]
 [-ClaimsProviderName <String[]>] [-Name <String>] [-NotBeforeSkew <Int32>] [-Identifier <String[]>]
 [-IssuanceAuthorizationRules <String>] [-IssuanceAuthorizationRulesFile <String>]
 [-DelegationAuthorizationRules <String>] [-DelegationAuthorizationRulesFile <String>]
 [-ImpersonationAuthorizationRules <String>] [-ImpersonationAuthorizationRulesFile <String>]
 [-IssuanceTransformRules <String>] [-IssuanceTransformRulesFile <String>]
 [-AdditionalAuthenticationRules <String>] [-AdditionalAuthenticationRulesFile <String>]
 [-AccessControlPolicyName <String>] [-AccessControlPolicyParameters <Object>] [-Description <String>]
 [-TokenLifetime <Int32>] [-AllowedClientTypes <AllowedClientTypes>]
 [-IssueOAuthRefreshTokensTo <RefreshTokenIssuanceDeviceTypes>] [-RefreshTokenProtectionEnabled <Boolean>]
 [-RequestMFAFromClaimsProviders <Boolean>] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsWebApiApplication` cmdlet 用于修改 Active Directory Federation Services (AD FS) 中现有应用程序的 Web API 应用程序角色的配置设置。

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
指定一个文件，该文件包含了用于此依赖方（relying party）的所有额外身份验证规则。

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
指定允许的客户端类型。此参数的可接受值包括：

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
这表示该 Web API 应用程序角色始终需要身份验证，即使之前已经通过身份验证获得了访问权限。指定此参数可强制用户每次访问敏感资源时都必须提供有效的凭据。

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

### -ClaimsProviderName
指定一个声明提供者名称数组，您可以为依赖于该提供者的信任关系（用于家庭领域发现（Home Realm Discovery，HRD）场景）进行配置。

如果为依赖方指定了声明提供者名称，那么家园领域发现页面只会显示该依赖方的那些声明提供者。如果只指定了一个声明提供者的名称，则不会显示家园领域发现页面。用户将被重定向到该声明提供者进行身份验证。

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
指定一个文件，其中包含了该依赖方进行委托身份验证所需的所有规则。

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
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Identifier
指定一个标识符数组。

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

### -ImpersonationAuthorizationRules
指定模拟（impersonation）授权规则。

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
指定一个文件，其中包含该依赖方进行身份冒用认证所需的所有规则。

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
指定一个文件，其中包含了该依赖方进行发行认证所需的所有规则。

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
指定一个文件，其中包含了该依赖方进行发行转换（issuance transform）所需的所有规则。

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
指定用于发放刷新令牌的设备类型。该参数的可接受值为：

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

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NotBeforeSkew
指定“not before skew”值的范围。

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

### -RefreshTokenProtectionEnabled
表示是否启用了刷新令牌的保护功能。

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
表示使用了“来自声明提供者的多因素认证（MFA）请求”这一选项。

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

### -TargetApplication
指定要修改设置的网络应用程序。

```yaml
Type: WebApiApplication
Parameter Sets: ApplicationObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetIdentifier
指定要修改设置的网络应用程序的ID。

```yaml
Type: String
Parameter Sets: Identifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -TargetName
指定要修改设置的网络应用程序的名称。

```yaml
Type: String
Parameter Sets: Name
Aliases:

Required: True
Position: 0
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
在运行 cmdlet 之前会提示您确认是否要执行该操作。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

字符串对象会被用于以下参数：`AccessControlPolicyName`、`AdditionalAuthenticationRules`、`DelegationAuthorizationRules`、`Description`、`ImpersonationAuthorizationRules`、`IssuanceAuthorizationRules`、`IssuanceTransformRules`、`TargetIdentifier` 和 `TargetName`。

### System.Object

对象是通过 *AccessControlPolicyParameters* 参数接收的。

### Microsoft IdentityServer.Management.Resources.WebApiApplication

`WebApiApplication` 对象是通过 `*TargetApplication*` 参数接收到的。

## 输出

### Microsoft IdentityServer.Management.Resources.WebApiApplication

当指定 `PassThru` 参数时，该命令会返回更新后的 `WebApiApplication` 对象。默认情况下，此命令不会生成任何输出。

## 备注

## 相关链接

[添加 AdfsWebApi 应用程序](./Add-AdfsWebApiApplication.md)

[Get-AdfsWebApiApplication](./Get-AdfsWebApiApplication.md)

[Remove-AdfsWebApiApplication](./Remove-AdfsWebApiApplication.md)

