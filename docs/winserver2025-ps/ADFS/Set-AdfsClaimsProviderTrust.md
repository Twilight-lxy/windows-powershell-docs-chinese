---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsclaimsprovidertrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsClaimsProviderTrust
---

# 设置 AdfsClaimsProviderTrust

## 摘要
设置 claims provider 信任关系的相关属性。

## 语法

### 标识符Object
```
Set-AdfsClaimsProviderTrust [-Name <String>] [-Identifier <String>] [-SignatureAlgorithm <String>]
 [-TokenSigningCertificate <X509Certificate2[]>] [-MetadataUrl <Uri>] [-AcceptanceTransformRules <String>]
 [-AcceptanceTransformRulesFile <String>] [-AllowCreate <Boolean>] [-AutoUpdateEnabled <Boolean>]
 [-CustomMFAUri <Uri>] [-SupportsMFA <Boolean>] [-WSFedEndpoint <Uri>]
 [-EncryptionCertificate <X509Certificate2>] [-EncryptionCertificateRevocationCheck <String>]
 [-MonitoringEnabled <Boolean>] [-Notes <String>] [-OrganizationalAccountSuffix <String[]>]
 [-LookupForests <String[]>] [-AlternateLoginID <String>] [-Force] [-ClaimOffered <ClaimDescription[]>]
 [-SamlEndpoint <SamlEndpoint[]>] [-ProtocolProfile <String>] [-RequiredNameIdFormat <Uri>]
 [-EncryptedNameIdRequired <Boolean>] [-SignedSamlRequestsRequired <Boolean>]
 [-SamlAuthenticationRequestIndex <UInt16>] [-SamlAuthenticationRequestParameters <String>]
 [-SamlAuthenticationRequestProtocolBinding <String>] [-SigningCertificateRevocationCheck <String>]
 [-PromptLoginFederation <PromptLoginFederation>] [-PromptLoginFallbackAuthenticationType <String>]
 [-AnchorClaimType <String>] -TargetClaimsProviderTrust <ClaimsProviderTrust> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### TokenSigningCertificates
```
Set-AdfsClaimsProviderTrust [-Name <String>] [-Identifier <String>] [-SignatureAlgorithm <String>]
 [-TokenSigningCertificate <X509Certificate2[]>] [-MetadataUrl <Uri>] [-AcceptanceTransformRules <String>]
 [-AcceptanceTransformRulesFile <String>] [-AllowCreate <Boolean>] [-AutoUpdateEnabled <Boolean>]
 [-CustomMFAUri <Uri>] [-SupportsMFA <Boolean>] [-WSFedEndpoint <Uri>]
 [-EncryptionCertificate <X509Certificate2>] [-EncryptionCertificateRevocationCheck <String>]
 [-MonitoringEnabled <Boolean>] [-Notes <String>] [-OrganizationalAccountSuffix <String[]>]
 [-LookupForests <String[]>] [-AlternateLoginID <String>] [-Force] [-ClaimOffered <ClaimDescription[]>]
 [-SamlEndpoint <SamlEndpoint[]>] [-ProtocolProfile <String>] [-RequiredNameIdFormat <Uri>]
 [-EncryptedNameIdRequired <Boolean>] [-SignedSamlRequestsRequired <Boolean>]
 [-SamlAuthenticationRequestIndex <UInt16>] [-SamlAuthenticationRequestParameters <String>]
 [-SamlAuthenticationRequestProtocolBinding <String>] [-SigningCertificateRevocationCheck <String>]
 [-PromptLoginFederation <PromptLoginFederation>] [-PromptLoginFallbackAuthenticationType <String>]
 [-AnchorClaimType <String>] -TargetCertificate <X509Certificate2> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 标识符
```
Set-AdfsClaimsProviderTrust [-Name <String>] [-Identifier <String>] [-SignatureAlgorithm <String>]
 [-TokenSigningCertificate <X509Certificate2[]>] [-MetadataUrl <Uri>] [-AcceptanceTransformRules <String>]
 [-AcceptanceTransformRulesFile <String>] [-AllowCreate <Boolean>] [-AutoUpdateEnabled <Boolean>]
 [-CustomMFAUri <Uri>] [-SupportsMFA <Boolean>] [-WSFedEndpoint <Uri>]
 [-EncryptionCertificate <X509Certificate2>] [-EncryptionCertificateRevocationCheck <String>]
 [-MonitoringEnabled <Boolean>] [-Notes <String>] [-OrganizationalAccountSuffix <String[]>]
 [-LookupForests <String[]>] [-AlternateLoginID <String>] [-Force] [-ClaimOffered <ClaimDescription[]>]
 [-SamlEndpoint <SamlEndpoint[]>] [-ProtocolProfile <String>] [-RequiredNameIdFormat <Uri>]
 [-EncryptedNameIdRequired <Boolean>] [-SignedSamlRequestsRequired <Boolean>]
 [-SamlAuthenticationRequestIndex <UInt16>] [-SamlAuthenticationRequestParameters <String>]
 [-SamlAuthenticationRequestProtocolBinding <String>] [-SigningCertificateRevocationCheck <String>]
 [-PromptLoginFederation <PromptLoginFederation>] [-PromptLoginFallbackAuthenticationType <String>]
 [-AnchorClaimType <String>] -TargetIdentifier <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 标识符Name
```
Set-AdfsClaimsProviderTrust [-Name <String>] [-Identifier <String>] [-SignatureAlgorithm <String>]
 [-TokenSigningCertificate <X509Certificate2[]>] [-MetadataUrl <Uri>] [-AcceptanceTransformRules <String>]
 [-AcceptanceTransformRulesFile <String>] [-AllowCreate <Boolean>] [-AutoUpdateEnabled <Boolean>]
 [-CustomMFAUri <Uri>] [-SupportsMFA <Boolean>] [-WSFedEndpoint <Uri>]
 [-EncryptionCertificate <X509Certificate2>] [-EncryptionCertificateRevocationCheck <String>]
 [-MonitoringEnabled <Boolean>] [-Notes <String>] [-OrganizationalAccountSuffix <String[]>]
 [-LookupForests <String[]>] [-AlternateLoginID <String>] [-Force] [-ClaimOffered <ClaimDescription[]>]
 [-SamlEndpoint <SamlEndpoint[]>] [-ProtocolProfile <String>] [-RequiredNameIdFormat <Uri>]
 [-EncryptedNameIdRequired <Boolean>] [-SignedSamlRequestsRequired <Boolean>]
 [-SamlAuthenticationRequestIndex <UInt16>] [-SamlAuthenticationRequestParameters <String>]
 [-SamlAuthenticationRequestProtocolBinding <String>] [-SigningCertificateRevocationCheck <String>]
 [-PromptLoginFederation <PromptLoginFederation>] [-PromptLoginFallbackAuthenticationType <String>]
 [-AnchorClaimType <String>] -TargetName <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsClaimsProviderTrust` cmdlet 用于配置与声明提供者（claims provider）之间的信任关系。

## 示例

#### 示例 1：为某个声明提供者（claims provider）的信任关系启用自动更新功能
```
PS C:\> Set-ADFSClaimsProviderTrust -TargetName "Fabrikam claims provider" -AutoUpdateEnabled $False
```

此命令可为名为“Fabrikam Claims Provider”的声明提供者信任配置自动更新功能。

## 参数

### -AcceptanceTransformRules
指定了用于接受来自该索赔提供者的索赔的规则集。这些规则决定了从由该索赔提供者所代表的合作伙伴那里可以接收哪些信息。

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
指定一个文件，该文件包含用于接受来自此索赔提供者的索赔的规则（即索赔处理流程）。

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
该参数用于指示在发送给声明提供者的 SAML 请求中是否包含“Security Assertion Markup Language (SAML)”中的 *AllowCreate* 参数。默认值为 True。

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

### -AlternateLoginID
指定用于登录的属性的 LDAP 名称。

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
该参数用于指示：通过 *MetadataURL* 对联邦元数据进行更改后，这些更改是否会自动应用到信任关系的配置中。如果该参数的值为 $True，则合作伙伴的信息、证书和终端将会被自动更新。

注意：当自动更新功能启用时，那些可能被元数据覆盖的字段将变为只读状态。

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
指定此声明提供者所提供的声明数组（claims）。

```yaml
Type: ClaimDescription[]
Parameter Sets: (All)
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
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EncryptedNameIdRequired
该设置用于指示依赖方是否要求对 **NameID** 主张进行加密。此配置适用于 SAML 登出请求。

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
指定用于在 SAML 注销请求中将 **NameID** 加密并发送给此声明提供者的证书。对 **NameID** 进行加密是可选的。

```yaml
Type: X509Certificate2
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EncryptionCertificateRevocationCheck
指定在加密证书用于加密声明之前所进行的验证类型。该参数的可接受值如下：

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

### -Force
Forces the command to run without asking for user confirmation.

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

### -Identifier
Specifies the unique identifier for this claims provider trust.
No other trust can use an identifier from this list.
Uniform Resource Identifiers (URIs) are often used as unique identifiers for a claims provider trust, but you can use any string of characters.

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

### -LookupForests
Specifies the forest DNS names that can be used to look up the **AlternateLoginID**.

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

### -MetadataUrl
Specifies the URL at which the federation metadata for this claims provider trust is available.

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

Required: False
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
Specifies a list of organizational account suffixes that an administrator can configure for the claims provider trust for Home Realm Discovery (HRD) scenarios.

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
- WsFed-SAML

By default, both SAML and WS-Federation protocols are supported.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: WsFed-SAML, WSFederation, SAML

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
Specifies the value of **AssertionConsumerServiceIndex** that is placed in SAML authentication requests that are sent to the claims provider.

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
Specifies which of the following parameters to use in SAML authentication requests to the claims provider: **AssertionConsumerServiceIndex**, **AssertionConsumerServiceUrl**, and **ProtocolBinding**.
The acceptable values for this parameter are:

- None
- Index
- Url
- ProtocolBinding
- UrlWithProtocolBinding

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Index, None, , ProtocolBinding, Url, UrlWithProtocolBinding

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
- POST
- Redirect

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Artifact, , POST, Redirect

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
Parameter Sets: (All)
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

### -SupportsMFA
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

### -TargetCertificate
Specifies the certificate of the claims provider trust that is modified by the cmdlet.

```yaml
Type: X509Certificate2
Parameter Sets: TokenSigningCertificates
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetClaimsProviderTrust
Specifies a **ClaimsProviderTrust** object.
The cmdlet modifies the claims provider trust that you specify.
To obtain a **ClaimsProviderTrust** object, use the **Get-AdfsClaimsProviderTrust** cmdlet.

```yaml
Type: ClaimsProviderTrust
Parameter Sets: IdentifierObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetIdentifier
Specifies the identifier of the claims provider trust that is modified by the cmdlet.

```yaml
Type: String
Parameter Sets: Identifier
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetName
Specifies the friendly name of the claims provider trust that is modified by the cmdlet.

```yaml
Type: String
Parameter Sets: IdentifierName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TokenSigningCertificate
Specifies an array of token-signing certificates that the claims provider use.

```yaml
Type: X509Certificate2[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WSFedEndpoint
Specifies the WS-Federation Passive URL for this claims provider.

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft IdentityServer.PowerShell.Resources.ClaimDescription

`ClaimDescription` 对象是通过 `ClaimOffered` 参数接收到的。

### System.Security cryptography.X509Certificates.X509Certificate.X509Certificate2

`X509Certificate2` 对象是通过 `TargetCertificate` 参数接收到的。

### Microsoft IdentityServer.PowShellResourcesClaimsProviderTrust

`ClaimsProviderTrust` 对象是通过 `*TargetClaimsProviderTrust*` 参数接收到的。

### System.String

`String` 对象被传递给 `AcceptanceTransformRules`、`SamlEndpoint`、`TargetIdentifier` 和 `TargetName` 这些参数。

## 输出

### Microsoft IdentityServer.PowShellResourcesClaimsProviderTrust

当指定 *PassThru* 参数时，该命令会返回一个经过修改的 ClaimsProviderTrust 对象。默认情况下，此 cmdlet 不会生成任何输出。

## 备注
* The claims provider collects and authenticates a user's credentials, builds up claims for that user, and packages the claims into security tokens or Information Cards. In other words, a claims provider represents the organization for whose users the claims provider issues security tokens or Information Cards on their behalf. When you configure Active Directory Federation Services (AD FS), the role of the claims provider is to enable its users to access resources that are hosted in a relying party organization by establishing one side of a federation trust relationship. After the trust is established, tokens and Information Cards can be presented to a relying party across the federation trust.

## 相关链接

[Add-AdfsClaimsProviderTrust](./Add-AdfsClaimsProviderTrust.md)

[禁用 AdfsClaimsProviderTrust](./ Disable-AdfsClaimsProviderTrust.md)

[Enable-AdfsClaimsProviderTrust](./Enable-AdfsClaimsProviderTrust.md)

[Get-AdfsClaimsProviderTrust](./Get-AdfsClaimsProviderTrust.md)

[Remove-AdfsClaimsProviderTrust](./Remove-AdfsClaimsProviderTrust.md)

[更新 AdfsClaimsProviderTrust](./Update-AdfsClaimsProviderTrust.md)

