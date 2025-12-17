---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfsclaimsprovidertrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsClaimsProviderTrust
---

# 添加 AdfsClaimsProviderTrust

## 摘要
向联邦服务（Federation Service）添加一个新的声明提供者信任关系（claims provider trust）。

## 语法

### AllProperties
```
Add-AdfsClaimsProviderTrust -Name <String> -Identifier <String> -TokenSigningCertificate <X509Certificate2[]>
 [-AutoUpdateEnabled <Boolean>] [-AllowCreate <Boolean>] [-AnchorClaimType <String>] [-CustomMFAUri <Uri>]
 [-EncryptionCertificateRevocationCheck <String>] [-Enabled <Boolean>] [-Notes <String>]
 [-ProtocolProfile <String>] [-EncryptedNameIdRequired <Boolean>] [-SamlAuthenticationRequestIndex <UInt16>]
 [-SamlAuthenticationRequestParameters <String>] [-SamlAuthenticationRequestProtocolBinding <String>]
 [-SignatureAlgorithm <String>] [-SigningCertificateRevocationCheck <String>] [-SupportsMfa]
 [-PromptLoginFederation <PromptLoginFederation>] [-PromptLoginFallbackAuthenticationType <String>]
 [-RequiredNameIdFormat <Uri>] [-EncryptionCertificate <X509Certificate2>]
 [-OrganizationalAccountSuffix <String[]>] [-WSFedEndpoint <Uri>] [-ClaimOffered <ClaimDescription[]>]
 [-SamlEndpoint <SamlEndpoint[]>] [-SignedSamlRequestsRequired <Boolean>] [-PassThru]
 [-AcceptanceTransformRules <String>] [-AcceptanceTransformRulesFile <String>] [-MonitoringEnabled <Boolean>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### MetadataFile
```
Add-AdfsClaimsProviderTrust -Name <String> [-AutoUpdateEnabled <Boolean>] [-AllowCreate <Boolean>]
 [-AnchorClaimType <String>] [-EncryptionCertificateRevocationCheck <String>] [-Enabled <Boolean>]
 [-Notes <String>] [-ProtocolProfile <String>] [-EncryptedNameIdRequired <Boolean>]
 [-SamlAuthenticationRequestIndex <UInt16>] [-SamlAuthenticationRequestParameters <String>]
 [-SamlAuthenticationRequestProtocolBinding <String>] [-SignatureAlgorithm <String>]
 [-SigningCertificateRevocationCheck <String>] [-PromptLoginFederation <PromptLoginFederation>]
 [-PromptLoginFallbackAuthenticationType <String>] [-RequiredNameIdFormat <Uri>]
 [-OrganizationalAccountSuffix <String[]>] [-MetadataFile <String>] [-SignedSamlRequestsRequired <Boolean>]
 [-PassThru] [-AcceptanceTransformRules <String>] [-AcceptanceTransformRulesFile <String>]
 [-MonitoringEnabled <Boolean>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### MetadataUrl
```
Add-AdfsClaimsProviderTrust -Name <String> [-AutoUpdateEnabled <Boolean>] [-AllowCreate <Boolean>]
 [-AnchorClaimType <String>] [-EncryptionCertificateRevocationCheck <String>] [-Enabled <Boolean>]
 [-Notes <String>] [-ProtocolProfile <String>] [-EncryptedNameIdRequired <Boolean>]
 [-SamlAuthenticationRequestIndex <UInt16>] [-SamlAuthenticationRequestParameters <String>]
 [-SamlAuthenticationRequestProtocolBinding <String>] [-SignatureAlgorithm <String>]
 [-SigningCertificateRevocationCheck <String>] [-PromptLoginFederation <PromptLoginFederation>]
 [-PromptLoginFallbackAuthenticationType <String>] [-RequiredNameIdFormat <Uri>]
 [-OrganizationalAccountSuffix <String[]>] [-MetadataUrl <Uri>] [-SignedSamlRequestsRequired <Boolean>]
 [-PassThru] [-AcceptanceTransformRules <String>] [-AcceptanceTransformRulesFile <String>]
 [-MonitoringEnabled <Boolean>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-AdfsClaimsProviderTrust` cmdlet 用于向联邦服务（Federation Service）添加一个新的声明提供者信任关系。当来自合作伙伴组织的用户需要访问由 Active Directory Federation Services (AD FS) 保护的资源时，可以使用此 cmdlet。您可以手动指定声明提供者信任关系，或者提供一个联合元数据文档来启动初始配置过程。

在 Windows Server 2016 中，AD FS 支持 `prompt=login` 参数。当 AD FS 充当联合提供者（federation provider）时，这些与声明提供者信任（claims provider trust）相关的属性决定了 AD FS 如何处理该参数。

## 示例

### 示例 1：添加对声明提供者（claims provider）的信任
```
PS C:\> Add-AdfsClaimsProviderTrust -Name "Fabrikam" -MetadataURL "https://fabrikam.com/federationmetadata/2007-06/federationmetadata.xml"
```

此命令向联邦服务（Federation Service）添加了一个名为“Fabrikam”的声明提供者信任（claims provider trust），该信任包含了指定的元数据URL。

## 参数

### -AcceptanceTransformRules
指定用于接受来自该索赔提供者的索赔的规则。这些规则决定了从由索赔提供者信任关系所代表的合作伙伴那里可以接收到的信息内容。

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

### -AcceptanceTransformRulesFile
指定一个文件，该文件包含用于接受来自声明提供者的声明的声明接受转换规则。

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

### -AllowCreate
该参数用于指示在发送给声明提供者的 SAML 请求中是否包含“Security Assertion Markup Language (SAML)”中的 *AllowCreate* 参数。默认值为 $True。

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

### -AnchorClaimType
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

### -AutoUpdateEnabled
该参数用于指示：通过 *MetadataURL* 参数对联邦元数据进行的更改是否会自动应用到信任关系的配置中。如果该参数的值为 $True$，则合作伙伴的声明、证书和端点将会被自动更新。

注意：当自动更新功能启用时，那些可以被元数据覆盖的字段将变为只读状态。

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

### -ClaimOffered
指定由该声明提供者提供的声明数组。

```yaml
Type: ClaimDescription[]
Parameter Sets: AllProperties
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -CustomMFAUri
```yaml
Type: Uri
Parameter Sets: AllProperties
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Enabled
表示是否启用了对声明提供者的信任验证（即是否允许用户信任该声明提供者）。

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

### -EncryptedNameIdRequired
该设置用于指示依赖方是否要求对 **NameID** 主张进行加密。此配置适用于 SAML 注销请求。

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

### -EncryptionCertificate
指定用于在 SAML 登出请求中将该 **NameID** 加密并发送给此声明提供者的证书。对 **NameID** 进行加密是可选的。

```yaml
Type: X509Certificate2
Parameter Sets: AllProperties
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EncryptionCertificateRevocationCheck
指定加密证书在用于加密声明之前所进行的验证类型。该参数的允许取值为：

- None
- CheckEndCert
- CheckEndCertCacheOnly
- CheckChain
- CheckChainCacheOnly
- CheckChainExcludeRoot
- CheckChainExcludeRootCacheOnly

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: CheckChain, CheckChainCacheOnly, CheckChainExcludeRoot, CheckChainExcludeRootCacheOnly, CheckEndCert, CheckEndCertCacheOnly, None

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identifier
Specifies the unique identifier for this claims provider trust.
No other trust can use an identifier from this list.
Uniform Resource Identifiers (URIs) are often used as unique identifiers for a claims provider trust, but you can use any string of characters.

```yaml
Type: String
Parameter Sets: AllProperties
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MetadataFile
Specifies a file path, such as c:\metadata.xml, that contains the federation metadata to be used when this claims provider trust is created.

```yaml
Type: String
Parameter Sets: MetadataFile
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MetadataUrl
Specifies a URL at which the federation metadata for this claims provider trust is available.

```yaml
Type: Uri
Parameter Sets: MetadataUrl
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MonitoringEnabled
Indicates whether periodic monitoring of this claims provider's federation metadata is enabled.
The URL of the claims provider's federation metadata is specified by the *MetadataUrl* parameter.

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

### -Name
Specifies the friendly name of this claims provider trust.

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

### -Notes
Specifies notes for this claims provider trust.

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

### -OrganizationalAccountSuffix
Specifies an array of organizational account suffixes an administrator can configure for the claims provider trust for a Home Realm Discovery (HRD) scenario.

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

### -PassThru
Returns an object representing the item with which you are working.
By default, this cmdlet does not generate any output.

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

### -PromptLoginFallbackAuthenticationType
Specifies a fallback authentication type for a prompt login request.

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

### -PromptLoginFederation
The acceptable values for this parameter are:

- None.
Do not federate prompt=login request and error instead.
- FallbackToProtocolSpecificParameters.
Translate prompt=login to wfresh=0 and Wauth=forms during federation.
If wauth is present in the original request, it will be preserved.
- ForwardPromptAndHintsOverWsFederation.
Forward prompt, login_hint, and domain_hint parameters during federation.

```yaml
Type: PromptLoginFederation
Parameter Sets: (All)
Aliases:
Accepted values: None, FallbackToProtocolSpecificParameters, ForwardPromptAndHintsOverWsFederation, Disabled

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ProtocolProfile
Specifies which protocol profiles the claims provider supports.
The acceptable values for this parameter are:

- SAML
- WsFederation
- WsFed-SAML.

The default value is WsFed-SAML.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: WSFederation, WsFed-SAML, SAML

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RequiredNameIdFormat
Specifies the format that is required for **NameID** claims to be included in SAML requests to the claims provider.
By default, no format is required.

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

### -SamlAuthenticationRequestIndex
Specifies the value of **AssertionConsumerServiceIndex** that will be placed in SAML authentication requests that are sent to the claims provider.

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SamlAuthenticationRequestParameters
Specifies which of the following parameters to use in SAML authentication requests to the claims provider: **AssertionConsumerServiceIndex**, **AssertionConsumerServiceUrl**, and **ProtocolBinding**.The acceptable values for this parameter are:

- None
- Index
- Url
- ProtocolBinding
- UrlWithProtocolBinding

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Index, None, ProtocolBinding, Url, UrlWithProtocolBinding

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SamlAuthenticationRequestProtocolBinding
Specifies the value of **ProtocolBinding** to place in SAML authentication requests to the claims provider.
The acceptable values for this parameter are:

- Artifact
- Post
- Redirect

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Artifact, POST, Redirect

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SamlEndpoint
Specifies an array of SAML protocol endpoints for this claims provider.

```yaml
Type: SamlEndpoint[]
Parameter Sets: AllProperties
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -SignatureAlgorithm
Specifies the signature algorithm that the claims provider uses for signing and verification.
The acceptable values for this parameter are:

- https://www.w3.org/2000/09/xmldsig#rsa-sha1
- https://www.w3.org/2001/04/xmldsig-more#rsa-sha256

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: https://www.w3.org/2000/09/xmldsig#rsa-sha1, https://www.w3.org/2001/04/xmldsig-more#rsa-sha256

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignedSamlRequestsRequired
Indicates whether the Federation Service requires signed SAML protocol requests from the relying party.
If you specify a value of $True, the Federation Service rejects unsigned SAML protocol requests.

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

### -SigningCertificateRevocationCheck
Specifies the type of certificate validation that occurs when signatures are verified on responses or assertions from the claims provider.
The acceptable values for this parameter are:

- None
- CheckEndCert
- CheckEndCertCacheOnly
- CheckChain
- CheckChainCacheOnly
- CheckChainExcludeRoot
- CheckChainExcludeRootCacheOnly

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: CheckChain, CheckChainCacheOnly, CheckChainExcludeRoot, CheckChainExcludeRootCacheOnly, CheckEndCert, CheckEndCertCacheOnly, None

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SupportsMfa
```yaml
Type: SwitchParameter
Parameter Sets: AllProperties
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TokenSigningCertificate
Specifies an array of token-signing certificates that the claims provider uses.

```yaml
Type: X509Certificate2[]
Parameter Sets: AllProperties
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WSFedEndpoint
指定此声明提供者的 WS-Federation 被动 URL（Passive URL）。

```yaml
Type: Uri
Parameter Sets: AllProperties
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
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

字符串对象通过 *AcceptanceTransformRules* 参数被接收。

### MicrosoftIdentityServer.PowerShellResources.ClaimDescription

`ClaimDescription` 对象是通过 `SamlEndpoint` 参数接收到的。

### System SECURITY Cryptography.X509Certificates.X509Certificate.X509Certificate2

`X509Certificate2` 对象是通过 `TokenSigningCertificate` 参数接收到的。

## 输出

### Microsoft.IdentityServer.PowerShell.ResourcesClaimsProviderTrust

当指定 *PassThru* 参数时，该命令会返回一个新的 ClaimsProviderTrust 对象。默认情况下，此 cmdlet 不会产生任何输出。

## 备注
* The claims provider is responsible for collecting and authenticating a user's credentials, building up claims for that user, and packaging the claims into security tokens or Information Cards. In other words, a claims provider represents the organization for whose users the claims provider issues security tokens or Information Cards on their behalf. When you configure Active Directory Federation Services (AD FS) to use federation services, the role of the claims provider is to enable its users to access resources that a relying party organization hosts by establishing one side of a federation trust relationship. After the trust is established, tokens and Information Cards can be presented to the relying party across the federation trust.

## 相关链接

[禁用 AdfsClaimsProviderTrust](./ Disable-AdfsClaimsProviderTrust.md)

[Enable-AdfsClaimsProviderTrust](./Enable-AdfsClaimsProviderTrust.md)

[Get-AdfsClaimsProviderTrust](./Get-AdfsClaimsProviderTrust.md)

[ Remove-AdfsClaimsProviderTrust](./Remove-AdfsClaimsProviderTrust.md)

[Set-AdfsClaimsProviderTrust](./Set-AdfsClaimsProviderTrust.md)

[更新 AdfsClaimsProviderTrust](./Update-AdfsClaimsProviderTrust.md)

