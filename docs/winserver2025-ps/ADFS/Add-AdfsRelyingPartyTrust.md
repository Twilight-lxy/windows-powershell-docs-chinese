---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfsrelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsRelyingPartyTrust
---

# 添加 AdfsRelyingPartyTrust

## 摘要
向联邦服务（Federation Service）添加一个新的依赖方信任（relying party trust）。

## 语法

### AllProperties
```
Add-AdfsRelyingPartyTrust -Name <String> -Identifier <String[]> [-EncryptClaims <Boolean>] [-Enabled <Boolean>]
 [-EncryptionCertificate <X509Certificate2>] [-AutoUpdateEnabled <Boolean>] [-WSFedEndpoint <Uri>]
 [-AdditionalWSFedEndpoint <String[]>] [-ClaimAccepted <ClaimDescription[]>] [-SamlEndpoint <SamlEndpoint[]>]
 [-RequestSigningCertificate <X509Certificate2[]>] [-EncryptedNameIdRequired <Boolean>]
 [-SignedSamlRequestsRequired <Boolean>] [-Notes <String>] [-SignatureAlgorithm <String>]
 [-SigningCertificateRevocationCheck <String>] [-TokenLifetime <Int32>] [-AlwaysRequireAuthentication]
 [-RequestMFAFromClaimsProviders] [-AllowedAuthenticationClassReferences <String[]>]
 [-EncryptionCertificateRevocationCheck <String>] [-NotBeforeSkew <Int32>] [-ProtocolProfile <String>]
 [-ClaimsProviderName <String[]>] [-EnableJWT <Boolean>] [-SamlResponseSignature <String>]
 [-AllowedClientTypes <AllowedClientTypes>] [-IssueOAuthRefreshTokensTo <RefreshTokenIssuanceDeviceTypes>]
 [-RefreshTokenProtectionEnabled <Boolean>] [-PassThru] [-MonitoringEnabled <Boolean>]
 [-ImpersonationAuthorizationRules <String>] [-ImpersonationAuthorizationRulesFile <String>]
 [-IssuanceTransformRules <String>] [-IssuanceTransformRulesFile <String>]
 [-IssuanceAuthorizationRules <String>] [-IssuanceAuthorizationRulesFile <String>]
 [-DelegationAuthorizationRules <String>] [-DelegationAuthorizationRulesFile <String>]
 [-AdditionalAuthenticationRules <String>] [-AdditionalAuthenticationRulesFile <String>]
 [-AccessControlPolicyName <String>] [-AccessControlPolicyParameters <Object>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### MetadataFile
```
Add-AdfsRelyingPartyTrust -Name <String> -MetadataFile <String> [-EncryptClaims <Boolean>]
 [-Enabled <Boolean>] [-AutoUpdateEnabled <Boolean>] [-EncryptedNameIdRequired <Boolean>]
 [-SignedSamlRequestsRequired <Boolean>] [-Notes <String>] [-SignatureAlgorithm <String>]
 [-SigningCertificateRevocationCheck <String>] [-TokenLifetime <Int32>] [-AlwaysRequireAuthentication]
 [-RequestMFAFromClaimsProviders] [-AllowedAuthenticationClassReferences <String[]>]
 [-EncryptionCertificateRevocationCheck <String>] [-NotBeforeSkew <Int32>] [-ProtocolProfile <String>]
 [-ClaimsProviderName <String[]>] [-EnableJWT <Boolean>] [-SamlResponseSignature <String>]
 [-AllowedClientTypes <AllowedClientTypes>] [-IssueOAuthRefreshTokensTo <RefreshTokenIssuanceDeviceTypes>]
 [-RefreshTokenProtectionEnabled <Boolean>] [-PassThru] [-MonitoringEnabled <Boolean>]
 [-ImpersonationAuthorizationRules <String>] [-ImpersonationAuthorizationRulesFile <String>]
 [-IssuanceTransformRules <String>] [-IssuanceTransformRulesFile <String>]
 [-IssuanceAuthorizationRules <String>] [-IssuanceAuthorizationRulesFile <String>]
 [-DelegationAuthorizationRules <String>] [-DelegationAuthorizationRulesFile <String>]
 [-AdditionalAuthenticationRules <String>] [-AdditionalAuthenticationRulesFile <String>]
 [-AccessControlPolicyName <String>] [-AccessControlPolicyParameters <Object>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### MetadataUrl
```
Add-AdfsRelyingPartyTrust -Name <String> -MetadataUrl <Uri> [-EncryptClaims <Boolean>] [-Enabled <Boolean>]
 [-AutoUpdateEnabled <Boolean>] [-EncryptedNameIdRequired <Boolean>] [-SignedSamlRequestsRequired <Boolean>]
 [-Notes <String>] [-SignatureAlgorithm <String>] [-SigningCertificateRevocationCheck <String>]
 [-TokenLifetime <Int32>] [-AlwaysRequireAuthentication] [-RequestMFAFromClaimsProviders]
 [-AllowedAuthenticationClassReferences <String[]>] [-EncryptionCertificateRevocationCheck <String>]
 [-NotBeforeSkew <Int32>] [-ProtocolProfile <String>] [-ClaimsProviderName <String[]>] [-EnableJWT <Boolean>]
 [-SamlResponseSignature <String>] [-AllowedClientTypes <AllowedClientTypes>]
 [-IssueOAuthRefreshTokensTo <RefreshTokenIssuanceDeviceTypes>] [-RefreshTokenProtectionEnabled <Boolean>]
 [-PassThru] [-MonitoringEnabled <Boolean>] [-ImpersonationAuthorizationRules <String>]
 [-ImpersonationAuthorizationRulesFile <String>] [-IssuanceTransformRules <String>]
 [-IssuanceTransformRulesFile <String>] [-IssuanceAuthorizationRules <String>]
 [-IssuanceAuthorizationRulesFile <String>] [-DelegationAuthorizationRules <String>]
 [-DelegationAuthorizationRulesFile <String>] [-AdditionalAuthenticationRules <String>]
 [-AdditionalAuthenticationRulesFile <String>] [-AccessControlPolicyName <String>]
 [-AccessControlPolicyParameters <Object>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-AdfsRelyingPartyTrust` cmdlet 用于向联邦服务（Federation Service）中添加一个新的依赖方信任关系（relying party trust）。您可以手动指定这个依赖方信任关系，或者提供一份联邦元数据文档来初始化配置。

## 示例

### 示例 1：添加依赖方信任（Relaying Party Trust）
```
PS C:\> Add-ADFSRelyingPartyTrust -Name "Fabrikam" -MetadataURL "https://fabrikam.com/federationmetadata/2007-06/federationmetadata.xml"
```

此命令为联合身份验证（federation）添加了一个名为“Fabrikam”的依赖方信任（relying party trust）。

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
指定额外的授权规则，以便在完成身份验证的第一步后，根据用户、设备和位置属性要求进行进一步的身份验证。注意：这些规则只有在至少启用了一个用于额外身份验证的身份提供者之后才能进行配置。

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
指定一个文件，该文件包含额外的身份验证规则。当用户尝试访问此依赖方时，这些规则将要求进行额外的身份验证。

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

### -AdditionalWSFedEndpoint
指定一个用于应用程序的备用返回地址数组。当应用程序需要告知 AD FS 在成功生成令牌时应使用的返回 URL 时，通常会使用这种方法。AD FS 要求管理员将所有可接受的 URL 都作为受信任的信息进行配置。

```yaml
Type: String[]
Parameter Sets: AllProperties
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowedAuthenticationClassReferences
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
指定允许的客户端类型。该参数的可接受值为：

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
表示始终要求进行身份验证。

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

### -AutoUpdateEnabled
该参数用于指示：通过 `MetadataURL` 对联邦元数据进行更改后，这些更改是否会自动应用到信任关系的配置中。如果该参数的值为 `$True`，则合作伙伴的信息、证书以及相关端点将会被自动更新。

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

### -ClaimAccepted
指定了该依赖方所接受的声明（claims）数组。

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

### -ClaimsProviderName
指定一个包含声明提供者名称的数组。

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
指定了向该依赖方颁发声明（claims）时的授权规则。

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
指定一个文件，该文件包含用于向此依赖方颁发声明（claims）的委托授权规则。

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

### -Enabled
表示是否启用了依赖方的信任机制。

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

### -EnableJWT
该参数用于指示是否应使用 JSON Web Token (JWT) 格式来在 WS-Federation 请求中颁发令牌。默认情况下，SAML 令牌是通过 WS-Federation 发行的。

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

### -EncryptClaims
表示发送给依赖方的声明是否已加密。

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
表示依赖方是否要求对 **NameID** 主张进行加密。

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
指定用于加密发给该依赖方的声明（claims）的证书。对声明进行加密是可选的操作。

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
指定用于加密发送给依赖方的声明（claims）的加密证书应进行的验证类型。该参数的可接受值为：

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
Specifies the unique identifiers for this relying party trust.
No other trust can use an identifier from this list.
Uniform Resource Identifiers (URIs) are often used as unique identifiers for a relying party trust, but you can use any string of characters.

```yaml
Type: String[]
Parameter Sets: AllProperties
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ImpersonationAuthorizationRules
Specifies the impersonation authorization rules for issuing claims to this relying party.

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
Specifies the file that contains the impersonation authorization rules for issuing claims to this relying party.

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
Specifies the issuance authorization rules for issuing claims to this relying party.

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
Specifies the file that contains the issuance authorization rules for issuing claims to this relying party.

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
Specifies the issuance transform rules for issuing claims to this relying party.

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
Specifies the file that contains the issuance transform rules for issuing claims to this relying party.

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
Specifies the refresh token issuance device types.
The acceptable values for this parameter are:

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

### -MetadataFile
Specifies a file path, such as c:\metadata.xml, that contains the federation metadata for this relying party trust.

```yaml
Type: String
Parameter Sets: MetadataFile
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MetadataUrl
Specifies a URL at which the federation metadata for this relying party trust is available.

```yaml
Type: Uri
Parameter Sets: MetadataUrl
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MonitoringEnabled
Indicates whether periodic monitoring of this relying party federation metadata is enabled.
The *MetadataUrl* parameter specifies the URL of the relying party federation metadata.

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
Specifies the friendly name of this relying party trust.

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
Specifies the skew, as in integer, for the time stamp that marks the beginning of the validity period.
The higher this number is, the further back in time the validity period begins with respect to the time that the claims are issued for the relying party.
By default, this value is 0.
Specify a positive value if validation fails on the relying party because the validity period has not yet begun.

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

### -Notes
Specifies notes for this relying party trust.

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

### -ProtocolProfile
Specifies which protocol profiles the relying party supports.
The acceptable values for this parameter are:

- SAML
- WsFederation
- WsFed-SAML

The default value is WsFed-SAML.

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

### -RefreshTokenProtectionEnabled
Indicates that refresh token protection is enabled.

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
Indicates whether to use the request MFA from claims providers option.

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

### -RequestSigningCertificate
Specifies an array of certificates to be used to verify the signature on a request from the relying party.

```yaml
Type: X509Certificate2[]
Parameter Sets: AllProperties
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -SamlEndpoint
Specifies an array of Security Assertion Markup Language (SAML) protocol endpoints for this relying party.

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

### -SamlResponseSignature
Specifies the response signature or signatures that the relying party expects.
The acceptable values for this parameter are:

- AssertionOnly
- MessageAndAssertion
- MessageOnly

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: AssertionOnly, MessageAndAssertion, MessageOnly

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignatureAlgorithm
Specifies the signature algorithm that the relying party uses for signing and verification.
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
Specifies the type of certificate validation that occur when signatures on requests from the relying party are verified.
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

### -TokenLifetime
Specifies the duration, in minutes, for which the claims that are issued to the relying party are valid.

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

### -WSFedEndpoint
Specifies the WS-Federation Passive URL for this relying party.

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
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被运行。

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

### System.String

字符串对象会被用于 *AccessControlPolicyName*、*AdditionalAuthenticationRules*、*DelegationAuthorizationRules*、*ImpersonationAuthorizationRules*、*IssuanceAuthorizationRules* 和 *IssuanceTransformRules* 这些参数中。

### System.Object

对象是通过 *AccessControlPolicyParameters* 参数接收的。

### System.ManagementAutomation.SwitchParameter

`SwitchParameter` 对象会被 `AlwaysRequireAuthentication` 和 `RequestMFAFromClaimsProviders` 参数接收。

### MicrosoftIdentityServer.PowerShellResources.ClaimDescription

`ClaimDescription` 对象是通过 `ClaimAccepted` 参数接收到的。

### System.Security Cryptography.X509Certificates.X509Certificate2

`X509Certificate2` 对象是通过 `RequestSigningCertificate` 参数接收到的。

### MicrosoftIdentityServer.PowerShell.Resources.SamlEndpoint

`SamlEndpoint` 对象是通过 `SamlEndpoint` 参数接收到的。

## 输出

### MicrosoftIdentityServer.PowShell.Resources.RelyingPartyTrust

当指定*PassThru*参数时，会返回一个新的RelyingPartyTrust对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* A relying party in Active Directory Federation Services (AD FS) is an organization in which Web servers that host one or more Web-based applications reside. Tokens and Information Cards that originate from a claims provider can then be presented and ultimately accessed by the Web-based resources that are located in the relying party organization. When AD FS is configured in the role of the relying party, it acts as a partner that trusts a claims provider to authenticate users. Therefore, the relying party accesses the claims that are packaged in security tokens that come from users in the claims provider. In other words, a relying party is the organization whose Web servers are protected by the resource-side federation server. The federation server in the relying party uses the security tokens that the claims provider produces to issue tokens to the Web servers that are located in the relying party.

## 相关链接

[ Disable-AdfsRelyingPartyTrust](./Disable-AdfsRelyingPartyTrust.md)

[Enable-AdfsRelyingPartyTrust](./Enable-AdfsRelyingPartyTrust.md)

[Get-AdfsRelyingPartyTrust](./Get-AdfsRelyingPartyTrust.md)

[Remove-AdfsRelyingPartyTrust](./Remove-AdfsRelyingPartyTrust.md)

[Set-AdfsRelyingPartyTrust](./Set-AdfsRelyingPartyTrust.md)

[更新：依赖于 ADFS 的方的信任设置](./Update-AdfsRelyingPartyTrust.md)

