---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsglobalwebcontent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsGlobalWebContent
---

# Set-AdfsGlobalWebContent

## 摘要
为全局网页内容对象设置属性。

## 语法

### IdentifierName（默认值）
```
Set-AdfsGlobalWebContent [-CompanyName <String>] [-HelpDeskLink <Uri>] [-HelpDeskLinkText <String>]
 [-HomeLink <Uri>] [-HomeLinkText <String>] [-HomeRealmDiscoveryOtherOrganizationDescriptionText <String>]
 [-HomeRealmDiscoveryPageDescriptionText <String>] [-OrganizationalNameDescriptionText <String>]
 [-PrivacyLink <Uri>] [-PrivacyLinkText <String>] [-CertificatePageDescriptionText <String>]
 [-SignInPageDescriptionText <String>] [-SignOutPageDescriptionText <String>]
 [-ErrorPageDescriptionText <String>] [-ErrorPageGenericErrorMessage <String>]
 [-ErrorPageAuthorizationErrorMessage <String>] [-ErrorPageDeviceAuthenticationErrorMessage <String>]
 [-ErrorPageSupportEmail <String>] [-UpdatePasswordPageDescriptionText <String>]
 [-SignInPageAdditionalAuthenticationDescriptionText <String>] [-PassThru] [[-Locale] <CultureInfo>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### IdentifierObject
```
Set-AdfsGlobalWebContent [-CompanyName <String>] [-HelpDeskLink <Uri>] [-HelpDeskLinkText <String>]
 [-HomeLink <Uri>] [-HomeLinkText <String>] [-HomeRealmDiscoveryOtherOrganizationDescriptionText <String>]
 [-HomeRealmDiscoveryPageDescriptionText <String>] [-OrganizationalNameDescriptionText <String>]
 [-PrivacyLink <Uri>] [-PrivacyLinkText <String>] [-CertificatePageDescriptionText <String>]
 [-SignInPageDescriptionText <String>] [-SignOutPageDescriptionText <String>]
 [-ErrorPageDescriptionText <String>] [-ErrorPageGenericErrorMessage <String>]
 [-ErrorPageAuthorizationErrorMessage <String>] [-ErrorPageDeviceAuthenticationErrorMessage <String>]
 [-ErrorPageSupportEmail <String>] [-UpdatePasswordPageDescriptionText <String>]
 [-SignInPageAdditionalAuthenticationDescriptionText <String>] [-PassThru]
 [-TargetWebContent] <AdfsGlobalWebContent> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsGlobalWebContent` cmdlet 用于设置全局 Web 内容对象的属性。您可以使用区域设置（locale）来指定全局 Web 对象，或者使用 `Get-AdfsGlobalWebContent` cmdlet 来获取该 Web 对象。

## 示例

### 示例 1：为全球网页内容设置公司名称
```
PS C:\> Set-AdfsGlobalWebContent -Locale "" -CompanyName "Contoso"
```

此命令用于设置全球网页内容中的公司名称（适用于不变的本地化设置）。如果没有公司的Logo，登录页面会显示“Contoso”作为公司名称。

### 示例 2：设置登录页面的文本和链接
```
PS C:\> Set-AdfsWebContent -Locale "en-us" -CompanyName "Contoso" -HelpDeskLink "https://helpdesklink" -HelpDeskLinkText "Help desk" -HomeLink "https://homelink" -HomeLinkText "Home" -PrivacyLink "https://privacylink" -PrivacyLinkText "Privacy statement" -SignInPageDescriptionText "Sign in here" -SignOutPageDescriptionText "Sign out here" -ErrorPageGenericErrorMessage "An error occurred." -ErrorPageSupportEmail "support@contoso.com" -UpdatePasswordPageDescriptionText "Update password here"
```

此命令指定了在 AD FS 的登录页面上显示的文本（适用于 en-us 地区设置）。

### 示例 3：为证书页面设置文本和链接
```
PS C:\> Set-AdfsGlobalWebContent -Locale "en-us" -CompanyName "Contoso" -HomeLink "https://homelink" -HomeLinkText "Home" -PrivacyLink "https://privaylink" -PrivacyLinkText "Privacy statement" -SignInPageDescriptionText "<p>Sign-in to Contoso requires device registration. Click <A href='https://fs1.contoso.com/deviceregistration/'>here</A> for more information.</p>" -SignOutPageDescriptionText "Sign out here" -ErrorPageGenericErrorMessage "An error occurred." -ErrorPageSupportEmail "support@contoso.com" -UpdatePasswordPageDescriptionText "Update password here" -CertificatePageDescriptionText "Sign in with your Smartcard"
```

此命令指定了当应用程序要求用户提供证书时显示的文本和链接内容。

## 参数

### -CertificatePageDescriptionText
用于指定证书页面上显示的文本。Active Directory Federation Services（AD FS）在向用户请求证书时会显示您指定的文本。在AD FS的早期版本中，当AD FS要求用户提供证书时，用户会看到一个空白页面。

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
用于指定公司名称。当您未在当前网页主题中设置徽标时，AD FS 会在登录页面上显示该公司名称。

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
当用户在执行令牌请求时遇到任何授权错误时，该属性用于指定要显示的错误消息。此字符串可以是一个 HTML 片段。您可以使用 `Set-AdfsRelyingPartyWebContent` cmdlet 为应用程序覆盖此默认消息。

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
指定当用户在使用令牌请求时遇到任何通用错误时显示的错误消息。该字符串可以是一个HTML片段。您可以使用`Set-AdfsRelyingPartyWebContent` cmdlet为应用程序覆盖此消息。

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
用于指定在令牌请求过程中发生设备身份验证错误时显示的错误消息。当用户向 AD FS 提供过期的 user@device 证书、AD DS 中找不到相应的证书，或者该证书在 AD DS 被禁用时，就会发生设备身份验证错误。此字符串可以是一个 HTML 片段。您可以使用 **Set-AdfsRelyingPartyWebContent** cmdlet 为特定应用程序覆盖此默认消息。

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
指定一个错误消息，用于显示在令牌请求过程中出现的任何通用错误时。该字符串可以是一个 HTML 片段。您可以使用 **Set-AdfsRelyingPartyWebContent** cmdlet 为特定应用程序覆盖此消息。

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
指定错误页面上的支持邮箱地址。

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
指定在 AD FS 的登录页面上显示的帮助台链接。

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
指定在 AD FS 的登录页面上显示的帮助台链接文本。

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
指定在 AD FS 的登录页面上显示的主页链接。

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
指定在 AD FS 的登录页面上显示的“主页”链接文本。

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
指定用于向其他组织展示本地域（home realm）发现信息的描述文本。

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
用于指定主领域发现页面描述文本的内容。

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
用于指定一个区域设置（locale）。该cmdlet会为你指定的区域设置设置全局网页内容。

```yaml
Type: CultureInfo
Parameter Sets: IdentifierName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -OrganizationalNameDescriptionText
用于指定组织名称描述的文本。

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

### -PrivacyLink
指定在 AD FS 的登录页面上显示的隐私政策链接。

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
指定在 AD FS 的登录页面上显示的隐私政策链接文本。

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
当应用程序要求用户进行额外的身份验证时，该属性用于指定显示的描述信息。登录页面也可能显示由额外身份验证提供者提供的描述内容。

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
指定当用户使用 AD FS 登录到应用程序时显示的描述信息。当在内部网络中使用集成 Windows 身份验证时，用户将看不到此页面。

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

### -SignOutPageDescriptionText
指定用户在退出应用程序时显示的描述信息。

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

### -TargetWebContent
指定一个 **AdfsGlobalWebContent** 对象。该 cmdlet 会修改你所指定的对象的内容。若要获取一个 **AdfsGlobalWebContent** 对象，可以使用 **Get-AdfsGlobalWebContent** cmdlet。

```yaml
Type: AdfsGlobalWebContent
Parameter Sets: IdentifierObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -UpdatePasswordPageDescriptionText
指定在用户更改密码时，在“修改密码”页面上显示的描述信息。

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
展示了如果运行该 cmdlet 会发生什么情况。但实际上并没有运行该 cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System IdentityServer.Management.Resources.AdfsGlobalWebContent
此cmdlet生成一个**SystemIdentityServer.Management.Resources.AdfsGlobalWebContent**对象，该对象表示全局网页内容。该对象包含以下属性：

- Locale: **System.Globalization.CultureInfo**
- CompanyName: **System.String**
- HelpDeskLink: **System.Uri**
- HelpDeskLinkText: **System.String**
- HomeLink: **System.Uri**
- HomeLinkText: **System.String**
- PrivacyLink: **System.Uri**
- PrivacyLinkText: **System.String**
- SignInPageDescriptionText: **System.String**
- SignOutPageDescriptionText: **System.String**
- ErrorPageDescriptionText: **System.String**
- ErrorPageGenericErrorMessage: **System.String**
- ErrorPageAuthorizationErrorMessage: **System.String**
- ErrorPageDeviceAuthenticationErrorMessage: **System.String**
- ErrorPageSupportEmail: **System.String**
- UpdatePasswordPageDescriptionText: **System.String**
- SignInPageAdditionalAuthenticationDescriptionText: **System.String**

## 备注

## 相关链接

[Get-AdfsGlobalWebContent](./Get-AdfsGlobalWebContent.md)

[Remove-AdfsGlobalWebContent](./Remove-AdfsGlobalWebContent.md)

[Set-AdfsRelyingPartyWebContent](./Set-AdfsRelyingPartyWebContent.md)

