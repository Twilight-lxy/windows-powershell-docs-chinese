---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsrelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsRelyingPartyTrust
---

# 设置 AdfsRelyingPartyTrust

## 摘要
设置依赖方信任（relying party trust）的属性。

## 语法

### 标识符
```
Set-AdfsRelyingPartyTrust [-AllowedAuthenticationClassReferences <String[]>] [-Name <String>]
 [-NotBeforeSkew <Int32>] [-EnableJWT <Boolean>] [-Identifier <String[]>]
 [-EncryptionCertificate <X509Certificate2>] [-EncryptionCertificateRevocationCheck <String>]
 [-EncryptClaims <Boolean>] [-MetadataUrl <Uri>] [-IssuanceAuthorizationRules <String>]
 [-IssuanceAuthorizationRulesFile <String>] [-DelegationAuthorizationRules <String>]
 [-DelegationAuthorizationRulesFile <String>] [-ImpersonationAuthorizationRules <String>]
 [-ImpersonationAuthorizationRulesFile <String>] [-IssuanceTransformRules <String>]
 [-IssuanceTransformRulesFile <String>] [-AdditionalAuthenticationRules <String>]
 [-AdditionalAuthenticationRulesFile <String>] [-AccessControlPolicyName <String>]
 [-AccessControlPolicyParameters <Object>] [-AutoUpdateEnabled <Boolean>] [-WSFedEndpoint <Uri>]
 [-AdditionalWSFedEndpoint <String[]>] [-ClaimsProviderName <String[]>] [-MonitoringEnabled <Boolean>]
 [-Notes <String>] [-ClaimAccepted <ClaimDescription[]>] [-SamlEndpoint <SamlEndpoint[]>]
 [-ProtocolProfile <String>] [-RequestSigningCertificate <X509Certificate2[]>]
 [-EncryptedNameIdRequired <Boolean>] [-SignedSamlRequestsRequired <Boolean>] [-SamlResponseSignature <String>]
 [-SignatureAlgorithm <String>] [-SigningCertificateRevocationCheck <String>] [-TokenLifetime <Int32>]
 [-AlwaysRequireAuthentication <Boolean>] [-AllowedClientTypes <AllowedClientTypes>]
 [-IssueOAuthRefreshTokensTo <RefreshTokenIssuanceDeviceTypes>] [-RefreshTokenProtectionEnabled <Boolean>]
 [-RequestMFAFromClaimsProviders <Boolean>] -TargetIdentifier <String> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 标识符Object
```
Set-AdfsRelyingPartyTrust [-AllowedAuthenticationClassReferences <String[]>] [-Name <String>]
 [-NotBeforeSkew <Int32>] [-EnableJWT <Boolean>] [-Identifier <String[]>]
 [-EncryptionCertificate <X509Certificate2>] [-EncryptionCertificateRevocationCheck <String>]
 [-EncryptClaims <Boolean>] [-MetadataUrl <Uri>] [-IssuanceAuthorizationRules <String>]
 [-IssuanceAuthorizationRulesFile <String>] [-DelegationAuthorizationRules <String>]
 [-DelegationAuthorizationRulesFile <String>] [-ImpersonationAuthorizationRules <String>]
 [-ImpersonationAuthorizationRulesFile <String>] [-IssuanceTransformRules <String>]
 [-IssuanceTransformRulesFile <String>] [-AdditionalAuthenticationRules <String>]
 [-AdditionalAuthenticationRulesFile <String>] [-AccessControlPolicyName <String>]
 [-AccessControlPolicyParameters <Object>] [-AutoUpdateEnabled <Boolean>] [-WSFedEndpoint <Uri>]
 [-AdditionalWSFedEndpoint <String[]>] [-ClaimsProviderName <String[]>] [-MonitoringEnabled <Boolean>]
 [-Notes <String>] [-ClaimAccepted <ClaimDescription[]>] [-SamlEndpoint <SamlEndpoint[]>]
 [-ProtocolProfile <String>] [-RequestSigningCertificate <X509Certificate2[]>]
 [-EncryptedNameIdRequired <Boolean>] [-SignedSamlRequestsRequired <Boolean>] [-SamlResponseSignature <String>]
 [-SignatureAlgorithm <String>] [-SigningCertificateRevocationCheck <String>] [-TokenLifetime <Int32>]
 [-AlwaysRequireAuthentication <Boolean>] [-AllowedClientTypes <AllowedClientTypes>]
 [-IssueOAuthRefreshTokensTo <RefreshTokenIssuanceDeviceTypes>] [-RefreshTokenProtectionEnabled <Boolean>]
 [-RequestMFAFromClaimsProviders <Boolean>] -TargetRelyingParty <RelyingPartyTrust> [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 标识符Name
```
Set-AdfsRelyingPartyTrust [-AllowedAuthenticationClassReferences <String[]>] [-Name <String>]
 [-NotBeforeSkew <Int32>] [-EnableJWT <Boolean>] [-Identifier <String[]>]
 [-EncryptionCertificate <X509Certificate2>] [-EncryptionCertificateRevocationCheck <String>]
 [-EncryptClaims <Boolean>] [-MetadataUrl <Uri>] [-IssuanceAuthorizationRules <String>]
 [-IssuanceAuthorizationRulesFile <String>] [-DelegationAuthorizationRules <String>]
 [-DelegationAuthorizationRulesFile <String>] [-ImpersonationAuthorizationRules <String>]
 [-ImpersonationAuthorizationRulesFile <String>] [-IssuanceTransformRules <String>]
 [-IssuanceTransformRulesFile <String>] [-AdditionalAuthenticationRules <String>]
 [-AdditionalAuthenticationRulesFile <String>] [-AccessControlPolicyName <String>]
 [-AccessControlPolicyParameters <Object>] [-AutoUpdateEnabled <Boolean>] [-WSFedEndpoint <Uri>]
 [-AdditionalWSFedEndpoint <String[]>] [-ClaimsProviderName <String[]>] [-MonitoringEnabled <Boolean>]
 [-Notes <String>] [-ClaimAccepted <ClaimDescription[]>] [-SamlEndpoint <SamlEndpoint[]>]
 [-ProtocolProfile <String>] [-RequestSigningCertificate <X509Certificate2[]>]
 [-EncryptedNameIdRequired <Boolean>] [-SignedSamlRequestsRequired <Boolean>] [-SamlResponseSignature <String>]
 [-SignatureAlgorithm <String>] [-SigningCertificateRevocationCheck <String>] [-TokenLifetime <Int32>]
 [-AlwaysRequireAuthentication <Boolean>] [-AllowedClientTypes <AllowedClientTypes>]
 [-IssueOAuthRefreshTokensTo <RefreshTokenIssuanceDeviceTypes>] [-RefreshTokenProtectionEnabled <Boolean>]
 [-RequestMFAFromClaimsProviders <Boolean>] -TargetName <String> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-AdfsRelyingPartyTrust` cmdlet 用于配置与指定的依赖方对象之间的信任关系。

## 示例

### 示例 1：为依赖方信任（relying party trust）设置名称和标识符
```
PS C:\> Set-AdfsRelyingPartyTrust -TargetName "FabrikamApp" -Identifier "https://FabrikamApp.CentralServerNew.org"
```

此命令为指定的依赖方信任（relying party trust）设置名称和标识符。

### 示例 2：为依赖方信任设置目标标识符
```
PS C:\> Set-AdfsRelyingPartyTrust -TargetIdentifier "https://FabrikamApp.CentralServer.org" -Identifier "https://FabrikamApp.CentralServerNew.org"
```

此命令为指定的依赖方信任关系设置目标标识符。

### 示例 3：分配一个使用参数的策略
```
PS C:\> Set-AdfsRelyingPartyTrust -TargetName "DemoRP1" -AccessControlPolicyParameters ("Administrators","Users") -AccessControlPolicyName "DemoOne"
```

此命令分配了一个使用参数的策略。

有关访问控制策略参数的更多信息，请参阅 TechNet 上的 [Active Directory Federation Services](https://technet.microsoft.com/windows-server-docs/identity/active-directory-federation-services)。

### 示例 4：取消分配策略模板
```
PS C:\> Set-AdfsRelyingPartyTrust -TargetName "DemoRP1" -AccessControlPolicyName $null
```

此命令用于取消对某个策略模板的关联（即不再将该模板应用于任何对象）。

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
指定额外的授权规则，以便在完成第一步身份验证后，根据用户、设备和位置属性要求进行进一步的身份验证。注意：这些规则必须仅在至少启用了一个用于额外身份验证的身份提供者之后才能进行配置。

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
指定一组用于应用程序的备用返回地址。这通常在应用程序需要告知 AD FS 成功生成令牌后应使用的返回 URL 时使用。AD FS 要求管理员将所有可接受的 URL 都作为受信任的信息输入。

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
表示始终需要身份验证。

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

### -AutoUpdateEnabled
该参数用于指示：通过 `MetadataURL` 对联盟元数据进行修改后，这些更改是否会自动应用于信任关系的配置。如果该参数的值为 `$True`，则合作伙伴的主张、证书和终端会自动更新。

注意：当启用自动更新功能时，那些可能被元数据覆盖的字段将变为只读状态。

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
指定一个该依赖方所接受的声明（claims）数组。

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
规定了向该依赖方发放声明（claims）时的授权规则。

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
指定一个文件，其中包含用于向该依赖方颁发声明的授权规则。

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

### -EnableJWT
该属性用于指示是否应使用 JSON Web Token（JWT）格式来在 WS-Federation 请求中生成令牌。默认情况下，SAML 令牌是通过 WS-Federation 发行的。

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
用于指示发送给依赖方的声明是否应该被加密。

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
指定用于加密发送给该依赖方的声明的证书。对声明进行加密是可选的。

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
指定在加密证书用于向依赖方发送声明之前对其进行验证的类型。此参数的可接受值包括：

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
Specifies an array of unique identifiers for this relying party trust.
No other trust can use an identifier from this list.
Uniform Resource Identifiers (URIs) are often used as unique identifiers for a relying party trust, but you can use any string of characters.

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
Specifies a file that contains the impersonation authorization rules for issuing claims to this relying party.

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
Specifies a file that contains the issuance authorization rules for issuing claims to this relying party.

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
Specifies a file that contains the issuance transform rules for issuing claims to this relying party.

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

### -MetadataUrl
Specifies a URL at which the federation metadata for this relying party trust is available.

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
Indicates whether periodic monitoring of this relying party federation metadata is enabled.
The *MetadataUrl* parameter specifies the URL of the relying party's federation metadata.

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

Note: You can use the *Name* parameter as an identifier for the object.

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
The acceptable values for this parameter are: SAML and WsFederation.
By default, this parameter is blank, which indicates that both protocols are supported.

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
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RequestSigningCertificate
Specifies an array of certificate that is used to verify the signature on a request from the relying party.

```yaml
Type: X509Certificate2[]
Parameter Sets: (All)
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
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -SamlResponseSignature
Specifies the response signatures that the relying party expects.
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
Specifies the type of certificate validation that should occur when signatures on requests from the relying party are verified.
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

### -TargetIdentifier
Specifies the identifier of the relying party trust that is modified by the cmdlet.

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
Specifies the friendly name of the relying party trust that is modified by the cmdlet.

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

### -TargetRelyingParty
Specifies a **RelyingPartyTrust** object.
The cmdlet modifies the relying party trust that you specify.
To obtain a **RelyingPartyTrust** object, use the **Get-AdfsRelyingPartyTrust** cmdlet.

```yaml
Type: RelyingPartyTrust
Parameter Sets: IdentifierObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TokenLifetime
Specifies the duration, in minutes, for which the claims that are issued to the relying party are valid. The default TokenLifetime is 60 minutes.

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

字符串对象会被传递给 *AccessControlPolicyName*、*AdditionalAuthenticationRules*、*DelegationAuthorizationRules*、*ImpersonationAuthorizationRules*、*IssuanceAuthorizationRules*、*IssuanceTransformRules*、*TargetIdentifier* 和 *TargetName* 这些参数。

### System.Object

对象是通过 *AccessControlPolicyParameters* 参数接收的。

### System.ManagementAutomation.SwitchParameter

`SwitchParameter` 对象会被 `AlwaysRequireAuthentication` 和 `RequestMFAFromClaimsProviders` 参数接收。

### Microsoft.IdentityServer.PowerShell.Resources.ClaimDescription

`ClaimDescription` 对象是通过 `ClaimAccepted` 参数接收到的。

### System.Security Cryptography.X509Certificates.X509Certificate2

`X509Certificate2` 对象是通过 `RequestSigningCertificate` 参数接收到的。

### Microsoft IdentityServer.PowerShell.Resources.SamlEndpoint

`SamlEndpoint` 对象是通过 `SamlEndpoint` 参数接收到的。

### Microsoft.IdentityServer.PowerShellResources.RelyingPartyTrust

`RelyingPartyTrust` 对象是通过 `TargetRelyingParty` 参数接收的。

## 输出

### Microsoft.IdentityServer.PowerShellResources.RelyingPartyTrust

当指定*PassThru*参数时，该命令会返回更新后的RelyingPartyTrust对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* A relying party in Active Directory Federation Services (AD FS) is an organization in which Web servers that host one or more Web-based applications reside. Tokens and Information Cards that originate from a claims provider can then be presented and ultimately accessed by the Web-based resources that are located in the relying party organization. When AD FS is configured in the role of the relying party, it acts as a partner that trusts a claims provider to authenticate users. Therefore, the relying party accesses the claims that are packaged in security tokens that come from users in the claims provider. In other words, a relying party is the organization whose Web servers are protected by the resource-side federation server. The federation server in the relying party uses the security tokens that the claims provider produces to issue tokens to the Web servers that are located in the relying party.

## 相关链接

[Add-AdfsRelyingPartyTrust](./Add-AdfsRelyingPartyTrust.md)

[禁用依赖 ADFS 的信任关系](./ Disable-AdfsRelyingPartyTrust.md)

[Enable-AdfsRelyingPartyTrust](./Enable-AdfsRelyingPartyTrust.md)

[Get-AdfsRelyingPartyTrust](./Get-AdfsRelyingPartyTrust.md)

[Remove-AdfsRelyingPartyTrust](./Remove-AdfsRelyingPartyTrust.md)

[更新-AdfsRelyingPartyTrust](./Update-AdfsRelyingPartyTrust.md)

