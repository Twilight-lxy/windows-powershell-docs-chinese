---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfswebapplicationproxyrelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsWebApplicationProxyRelyingPartyTrust
---

# 获取 AdfsWebApplicationProxy 依赖方的信任信息

## 摘要
获取用于 Web 应用程序代理的依赖方信任对象。

## 语法

```
Get-AdfsWebApplicationProxyRelyingPartyTrust [<CommonParameters>]
```

## 描述
`Get-AdfsWebApplicationProxyRelyingPartyTrust` cmdlet 用于获取与代理相关的 Web 应用程序代理依赖方信任对象。

Web应用程序代理（WAP）所依赖的信任机制有助于管理来自企业网络外部的全局网络访问。通过设置身份验证和授权策略，管理员可以限制对通过Web应用程序代理发布的内部Web应用程序和服务的访问权限。

## 示例

### 示例 1：获取依赖方的信任对象
```
PS C:\> Get-AdfsWebApplicationProxyRelyingPartyTrust

AlwaysRequireAuthentication   : False
Enabled                       : True
Identifier                    : {urn:AppProxy:com}
IssuanceAuthorizationRules    : @RuleTemplate="AllowAllAuthzRule" => issue(Type = "http://schemas.contoso.com/authorization/claims/permit", Value="true");
IssuanceTransformRules        : @RuleTemplate="PassThroughClaims"
@RuleName="Pass Through Application Identifier"
c:[Type == "http://schemas.contoso.com/2012/01/requestcontext/claims/relyingpartytrustid"] => issue(claim = c);
@RuleTemplate="PassThroughClaims"
@RuleName="Pass Through Device Registration Identifier"
c:[Type == "http://schemas.contoso.com/2012/01/devicecontext/claims/registrationid"] => issue(claim = c);
@RuleTemplate="PassThroughClaims"
@RuleName="Pass Through UPN"
c:[Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn"] => issue(claim = c);
@RuleTemplate="PassThroughClaims"
@RuleName="Pass Through Activity ID"
c:[Type == "http://schemas.contoso.com/2012/01/requestcontext/claims/client-request-id"] => issue(claim = c);

AdditionalAuthenticationRules :
Name                          : urn:AppProxy:com
NotBeforeSkew                 : 0
Notes                         :
RelyingPartyType              : WebApplicationProxy
TokenLifetime                 : 0
```

此命令用于获取 Web 应用程序代理的依赖方信任对象，并显示之前添加的身份验证和授权规则。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-AdfsWebApplicationProxyRelyingPartyTrust](./Add-AdfsWebApplicationProxyRelyingPartyTrust.md)

[禁用 AdfsWebApplicationProxy 依赖方信任](./Disable-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Enable-AdfsWebApplicationProxyRelyingPartyTrust](./Enable-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Remove-AdfsWebApplicationProxyRelyingPartyTrust](./Remove-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Set-AdfsWebApplicationProxyRelyingPartyTrust](./Set-AdfsWebApplicationProxyRelyingPartyTrust.md)

