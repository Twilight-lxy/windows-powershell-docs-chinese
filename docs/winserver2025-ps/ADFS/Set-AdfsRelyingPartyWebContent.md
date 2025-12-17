---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsrelyingpartywebcontent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsRelyingPartyWebContent
---

# 设置 AdfsRelyingPartyWebContent

## 摘要
为依赖方（relying party）的网页内容对象设置属性。

## 语法

### IdentifierName（默认值）
```
Set-AdfsRelyingPartyWebContent [-CertificatePageDescriptionText <String>] [-CompanyName <String>]
 [-ErrorPageDescriptionText <String>] [-ErrorPageGenericErrorMessage <String>]
 [-ErrorPageAuthorizationErrorMessage <String>] [-ErrorPageDeviceAuthenticationErrorMessage <String>]
 [-ErrorPageSupportEmail <String>] [-HelpDeskLink <Uri>] [-HelpDeskLinkText <String>] [-HomeLink <Uri>]
 [-HomeLinkText <String>] [-HomeRealmDiscoveryOtherOrganizationDescriptionText <String>]
 [-HomeRealmDiscoveryPageDescriptionText <String>] [-OrganizationalNameDescriptionText <String>]
 [-PrivacyLink <Uri>] [-PrivacyLinkText <String>] [-SignInPageDescriptionText <String>]
 [-SignInPageAdditionalAuthenticationDescriptionText <String>] [-PassThru] [[-Locale] <CultureInfo>]
 -TargetRelyingPartyName <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### IdentifierObject
```
Set-AdfsRelyingPartyWebContent [-CertificatePageDescriptionText <String>] [-CompanyName <String>]
 [-ErrorPageDescriptionText <String>] [-ErrorPageGenericErrorMessage <String>]
 [-ErrorPageAuthorizationErrorMessage <String>] [-ErrorPageDeviceAuthenticationErrorMessage <String>]
 [-ErrorPageSupportEmail <String>] [-HelpDeskLink <Uri>] [-HelpDeskLinkText <String>] [-HomeLink <Uri>]
 [-HomeLinkText <String>] [-HomeRealmDiscoveryOtherOrganizationDescriptionText <String>]
 [-HomeRealmDiscoveryPageDescriptionText <String>] [-OrganizationalNameDescriptionText <String>]
 [-PrivacyLink <Uri>] [-PrivacyLinkText <String>] [-SignInPageDescriptionText <String>]
 [-SignInPageAdditionalAuthenticationDescriptionText <String>] [-PassThru]
 [-TargetRelyingPartyWebContent] <AdfsRelyingPartyWebContent> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsRelyingPartyWebContent` cmdlet 用于设置依赖方网页内容对象的属性。这些属性会覆盖通过 `Set-AdfsGlobalWebContent` cmdlet 获取网页内容对象时所设置的相应属性值。您可以使用名称和区域设置（locale）来指定一个依赖方网页内容对象，或者使用 `Get-AdfsRelyingPartyWebContent` cmdlet 来获取该对象。如果您不指定区域设置，此 cmdlet 会使用默认的不变区域设置（invariant locale）。

## 示例

#### 示例 1：指定一个通用的错误消息
```
PS C:\> Set-AdfsRelyingPartyWebContent -Name "RelyingParty01" -ErrorPageGenericErrorMessage "There is an error."
```

此命令指定了一条通用的错误消息，用于向名为“RelyingParty01”的依赖方用户显示。

### 示例 2：指定多条错误信息
```
PS C:\> Set-AdfsRelyingPartyWebContent -Locale en-us -Name "RelyingParty02" -ErrorPageAuthorizationErrorMessage "There is an authorization error." -ErrorPageDeviceAuthenticationErrorMessage "There is a device authentication error." -ErrorPageGenericErrorMessage "There is an error."
```

此命令为名为 RelyingParty01 的依赖方分配了多条错误信息，以便在指定的区域设置（locale）下显示给用户。

### 示例 2：在登录页面上创建自定义消息
```
PS C:\> Set-AdfsRelyingPartyWebContent -SignInPageDescription "If you have forgotten your password, visit <A href='https://passwordreset.microsoftonline.com/'>Microsoft Entra self-service password reset</A>." -TargetRelyingPartyName "Microsoft Office 365 Identity Platform"
```

该命令会在 Office 365 依赖方的登录页面上创建一条自定义消息。

## 参数

### -CertificatePageDescriptionText
用于指定在证书选择页面上，“CompanyName”参数对应的文本下方显示的文字。

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

### -CompanyName
指定“登录”页面上的标题文本。

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

### -ErrorPageAuthorizationErrorMessage
当用户在进行令牌请求时遇到任何授权错误时，该字段用于指定要显示的错误消息。这个字符串可以是一段HTML代码。

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

### -ErrorPageDescriptionText
用于指定“登录错误页面”上“Company Name”参数下显示的文本。

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

### -ErrorPageDeviceAuthenticationErrorMessage
指定一个错误消息，用于在令牌请求过程中出现设备认证错误时显示给用户。设备认证错误发生在用户向 Active Directory Federation Services (AD FS) 提供过期的 user@device 证书、Active Directory® Domain Services 中不存在的证书，或者在 Active Directory Domain Services 中已被禁用的证书时。该字符串可以是一个 HTML 片段。

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

### -ErrorPageGenericErrorMessage
指定一个错误消息，用于显示在令牌请求过程中出现的任何通用错误时。该字符串可以是一个HTML片段。

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

### -ErrorPageSupportEmail
指定在登录错误页面上显示的电子邮件地址。

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

### -HelpDeskLink
指定登录页面底部“帮助台”链接的目标页面。

```yaml
Type: Uri
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HelpDeskLinkText
指定登录页面底部“帮助台”链接的文本内容。

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

### -HomeLink
指定登录页面底部“首页”链接的目标页面。

```yaml
Type: Uri
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HomeLinkText
指定登录页面底部“首页”链接的文本内容。

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

### -HomeRealmDiscoveryOtherOrganizationDescriptionText
用于指定显示在用户名输入提示框上方的描述文字。如果您将 UPN 后缀映射配置到一个或多个声明提供者信任源，那么“主域发现”页面会提供一个名为“其他组织”的选项。当用户选择该选项时，系统会要求他们输入用户名。

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

### -HomeRealmDiscoveryPageDescriptionText
指定在主域发现页面上，用于显示与“CompanyName”参数相关内容的文本下方的文字。

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
用于指定一个区域设置（locale）。该cmdlet会为您指定的区域设置设置相应的“依赖方网页内容”（relying party web content）。

```yaml
Type: CultureInfo
Parameter Sets: IdentifierName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -OrganizationalNameDescriptionText
用于指定“登录”页面上“Company Name”参数下显示的文本。

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

### -PrivacyLink
指定登录页面底部“隐私”链接的目标（即该链接所指向的具体内容或页面）。

```yaml
Type: Uri
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PrivacyLinkText
指定登录页面底部“隐私政策”链接所显示的文本内容。

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

### -SignInPageAdditionalAuthenticationDescriptionText
在额外的身份验证选择页面上，用于指定“CompanyName”参数下显示的文本内容。

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

### -SignInPageDescriptionText
指定登录页面上“登录”选项下方显示的文本。

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

### -TargetRelyingPartyName
指定要修改的依赖方信任（relying party trust）的名称。

```yaml
Type: String
Parameter Sets: IdentifierName
Aliases: Name

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetRelyingPartyWebContent
指定需要修改的依赖方（relying party）网页内容的名称。

```yaml
Type: AdfsRelyingPartyWebContent
Parameter Sets: IdentifierObject
Aliases: TargetWebContent

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
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
展示了如果运行该cmdlet会发生什么情况。不过实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### SystemIdentityServer.ManagementResources.AdfsRelyingPartyWebContent
此cmdlet生成一个`SystemIdentityServer.ManagementResources.AdfsRelyingPartyWebContent`对象，该对象表示依赖方的网页内容；或者生成此类对象的数组。该对象包含以下属性：

- Locale: **System.Globalization.CultureInfo**
- Name: **System.String**
- ErrorPageGenericErrorMessage: **System.String**
- ErrorPageAuthorizationErrorMessage: **System.String**
- ErrorPageDeviceAuthenticationErrorMessage: **System.String**

## 备注

## 相关链接

[Get-AdfsRelyingPartyWebContent](./Get-AdfsRelyingPartyWebContent.md)

[Remove-AdfsRelyingPartyWebContent](./Remove-AdfsRelyingPartyWebContent.md)

