---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsglobalwebcontent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsGlobalWebContent
---

# 获取 AdfsGlobalWeb 内容

## 摘要
获取全局网页内容对象。

## 语法

```
Get-AdfsGlobalWebContent [-Locale <CultureInfo[]>] [<CommonParameters>]
```

## 描述
`Get-AdfsGlobalWebContent` cmdlet 可以获取所有的全局 Web 内容对象，或者获取与您指定的区域设置（locale）相对应的全局 Web 内容对象。如果您没有指定 `Locale` 参数，该 cmdlet 会获取所有区域设置下的全局 Web 内容对象。

## 示例

#### 示例 1：获取所有地区的全球网页内容
```
PS C:\> Get-AdfsGlobalWebContent


Locale                                            :
CompanyName                                       :
HelpDeskLink                                      :
HelpDeskLinkText                                  :
HomeLink                                          :
HomeLinkText                                      :
PrivacyLink                                       :
PrivacyLinkText                                   :
CertificatePageDescriptionText                    :
SignInPageDescriptionText                         :
SignOutPageDescriptionText                        :
ErrorPageDescriptionText                          :
ErrorPageGenericErrorMessage                      :
ErrorPageAuthorizationErrorMessage                : You have been denied access.
ErrorPageDeviceAuthenticationErrorMessage         :
ErrorPageSupportEmail                             :
UpdatePasswordPageDescriptionText                 :
SignInPageAdditionalAuthenticationDescriptionText :
```

这个命令可以获取所有地区（locales）的全局网页内容。

### 示例 2：获取特定地区的全局网页内容
```
PS C:\> Get-AdfsGlobalWebContent -Locale en-us
```

此命令会获取与英文（en-us）语言环境相关的全局网页内容。如果您在使用 **Set-AdfsGlobalWebContent** cmdlet 修改全局网页内容的属性时没有指定任何语言环境，那么该 cmdlet 将不会返回任何额外信息。

## 参数

### -Locale
指定一个本地化设置（locale）数组。该cmdlet会获取与您指定的这些本地化设置相关联的全球网页内容。

```yaml
Type: CultureInfo[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### MicrosoftIdentityServer.Management.Resources.AdfsGlobalWebContent; MicrosoftIdentityServer.ManagementResources.AdfsGlobalWebContent[]
这个 cmdlet 生成一个 **SystemIdentityServer.ManagementResources.AdfsGlobalWebContent** 对象，该对象表示全局网页内容。该对象包含以下属性：

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
- CertificatePageDescriptionText: **System.String**
- SignInPageAdditionalAuthenticationDescriptionText: **System.String**

## 备注

## 相关链接

[Set-AdfsGlobalWebContent](./Set-AdfsGlobalWebContent.md)

[Remove-AdfsGlobalWebContent](./Remove-AdfsGlobalWebContent.md)

