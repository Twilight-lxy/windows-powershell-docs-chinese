---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsproperties?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsProperties
---

# 获取 ADFS 属性

## 摘要
获取与 AD FS 服务相关的所有属性信息。

## 语法

```
Get-AdfsProperties [<CommonParameters>]
```

## 描述
`Get-AdfsProperties` cmdlet 可以获取与 Active Directory Federation Services (AD FS) 服务相关的所有属性信息。

## 示例

### 示例 1：获取关联的属性
```
PS C:\> Get-AdfsProperties


AcceptableIdentifiers                      : {}
AddProxyAuthorizationRules                 : exists([Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/groupsid", Value == "S-1-5-32-544", Issuer =~ "^AD AUTHORITY$"]) =>
issue(Type = "http://schemas.microsoft.com/authorization/claims/permit", Value = "true");
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/primarysid", Issuer =~ "^AD AUTHORITY$" ]
=>
issue(store="_ProxyCredentialStore",types=("http://schemas.microsoft.com/authorization/claims/permit"),query="isProxyTrustManagerSid({0})",
param=c.Value );
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/proxytrustid", Issuer =~ "^SELF AUTHORITY$" ]
=>
issue(store="_ProxyCredentialStore",types=("http://schemas.microsoft.com/authorization/claims/permit"),query="isProxyTrustProvisioned({0})",
param=c.Value );
ArtifactDbConnection                       : Data Source=np:\\.\pipe\microsoft##wid\tsql\query;Initial Catalog=AdfsArtifactStore;Integrated Security=True
AuthenticationContextOrder                 : {urn:oasis:names:tc:SAML:2.0:ac:classes:Password, urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport,
urn:oasis:names:tc:SAML:2.0:ac:classes:TLSClient, urn:oasis:names:tc:SAML:2.0:ac:classes:X509...}
AutoCertificateRollover                    : False
CertificateCriticalThreshold               : 2
CertificateDuration                        : 365
CertificateGenerationThreshold             : 20
CertificatePromotionThreshold              : 5
CertificateRolloverInterval                : 720
CertificateSharingContainer                : CN=e6ddcbbc-5dc9-4ef2-9354-5e9ba1cac82d,CN=ADFS,CN=Microsoft,CN=Program Data,DC=contoso,DC=com
CertificateThresholdMultiplier             : 1440
ClientCertRevocationCheck                  : None
ContactPerson                              : Microsoft.IdentityServer.Management.Resources.ContactPerson
DisplayName                                : Contoso Corp.
IntranetUseLocalClaimsProvider             : False
ExtendedProtectionTokenCheck               : Allow
FederationPassiveAddress                   : /adfs/ls/
HostName                                   : sts.contoso.com
HttpPort                                   : 80
HttpsPort                                  : 443
TlsClientPort                              : 49443
Identifier                                 : https://sts.contoso.com/adfs/services/trust
InstalledLanguage                          : en-US
LogLevel                                   : {Errors, Information, Verbose, Warnings}
MonitoringInterval                         : 1440
NetTcpPort                                 : 1501
NtlmOnlySupportedClientAtProxy             : True
OrganizationInfo                           :
PreventTokenReplays                        : False
ProxyTrustTokenLifetime                    : 21600
ReplayCacheExpirationInterval              : 60
SignedSamlRequestsRequired                 : False
SamlMessageDeliveryWindow                  : 5
SignSamlAuthnRequests                      : False
SsoLifetime                                : 480
PersistentSsoLifetimeMins                  : 10080
PersistentSsoEnabled                       : True
PersistentSsoCutoffTime                    : 1/1/0001 12:00:00 AM
KmsiEnabled                                : False
LoopDetectionEnabled                       : True
LoopDetectionTimeIntervalInSeconds         : 20
LoopDetectionMaximumTokensIssuedInInterval : 5
SendClientRequestIdAsQueryStringParameter  : True
WIASupportedUserAgents                     : {MSIE 6.0, MSIE 7.0, MSIE 8.0, MSIE 9.0...}
ExtranetLockoutThreshold                   : 2
ExtranetLockoutEnabled                     : True
ExtranetObservationWindow                  : 01:00:00
```

此命令从 Active Directory Federation Services (AD FS) 中检索相关的属性。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### MicrosoftIdentityServer.Management.Resources.ServiceProperties
以下是将给定的Markdown文档转换成中文的结果：

```json
{
  "AcceptableIdentifiers": ["uri"],
  "AddProxyAuthorizationRules": ["string"],
  "AllowLocalAdminsServiceAdministration": ["bool"],
  "AllowSystemServiceAdministration": ["bool"],
  "ArtifactDbConnection": ["string"],
  "AuditLevel": ["string"],
  "AuthenticationContextOrder": ["uri"],
  "AutoCertificateRollover": ["bool"],
  "BrowserSsoEnabled": ["bool"],
  "BrowserSsoSupportedUserAgents": ["string"],
  "CertificateCriticalThreshold": [["int"]],
  "CertificateDuration": [["int"]],
  "CertificateGenerationThreshold": [["int"]],
  "CertificatePromotionThreshold": [["int"]],
  "CertificateRolloverInterval": [["int"]],
  "CertificateSharingContainer": ["string"],
  "CertificateThresholdMultiplier": [["int"]],
  "ClientCertRevocationCheck": ["MicrosoftIdentityServer.PolicyModel.Configuration.RevocationSetting"],
  "ContactPerson": ["Microsoft.IdentityServer.Management.Resources.ContactPerson"],
  "CurrentFarmBehavior": [["int"]],
  "DelegateServiceAdministration": ["string"],
  "DeviceUsageWindowInDays": [["int"]],
  "DisplayName": ["string"],
  "EnableIdpInitiatedSignonPage": ["bool"],
  "EnableOauthDeviceFlow": ["bool"],
  "EnableOauthLogout": ["bool"],
  "ExtendedProtectionTokenCheck": ["Microsoft.IdentityServer.PolicyModel.Configuration.ProtectionPolicySetting"],
  "ExtranetLockoutEnabled": ["bool"],
  "ExtranetLockoutRequirePDC": [["bool"]],
  "ExtranetLockoutThreshold": [["int"]],
  "ExtranetObservationWindow": [["timespan"]],
  "FederationPassiveAddress": ["string"],
  "GlobalRelyingPartyClaimsIssuancePolicy": ["string"],
  "HostName": ["string"],
  "HttpPort": [["int"]],
  "HttpsPort": [["int"]],
  "Identifier": ["uri"],
  "IdTokenIssuer": ["uri"],
  "IgnoreTokenBinding": ["bool"],
  "InstalledLanguage": ["string"],
  "IntranetUseLocalClaimsProvider": ["bool"],
  "KmsiEnabled": ["bool"],
  "KmsiLifetimeMins": [["int"]],
  "LocalAuthenticationTypesEnabled": ["bool"],
  "LogLevel": [["string"]],
  "LoopDetectionEnabled": ["bool"],
  "LoopDetectionMaximumTokensIssuedInInterval": [["int"]],
  "LoopDetectionTimeIntervalInSeconds": [["int"]],
  "MonitoringInterval": [["int"]],
  "NetTcpPort": [["int"]],
  "NtlmOnlySupportedClientAtProxy": [["bool"]],
  "OrganizationInfo": ["Microsoft.IdentityServer.Management.Resources.Organization"],
  "PasswordValidationDelayInMinutes": [["int"]],
  "PersistentSsoCutoffTime": [["datetime"]],
  "PersistentSsoEnabled": ["bool"],
  "PersistentSsoLifetimeMins": [["int"]],
  "PreventTokenReplays": ["bool"],
  "ProxyTrustTokenLifetime": [["int"]],
  "RelayStateForIdpInitiatedSignOnEnabled": ["bool"],
  "ReplayCacheExpirationInterval": [["int"]],
  "SamlMessageDeliveryWindow": [["int"]],
  "SendClientRequestIdAsQueryStringParameter": ["bool"],
  "SignedSamlRequestsRequired": ["bool"],
  "SignSamlAuthnRequests": ["bool"],
  "SsoLifetime": [["int"]],
  "TlsClientPort": [["int"]],
  "WiaEvaluationMethod": ["MicrosoftIdentityServer.WiaEvaluationMethodState"],
  "WIASupportedUserAgents": ["string"]
}
```

请注意，由于原始Markdown文档中包含了一些复杂的配置选项和数组元素，因此将其转换成JSON时需要将这些信息组织成键值对的形式。此外，某些字段的值是嵌套的列表或结构体，但在JSON中表示时通常使用简单的数组或对象结构。

### MicrosoftIdentityServer.PolicyModel.Configuration.RevocationSetting

RevocationSetting {  
   None = 0,  
   CheckEndCert = 1,  
   CheckEndCertCacheOnly = 2,  
   CheckChain = 3,  
   CheckChainCacheOnly = 4,  
   CheckChainExcludeRoot = 5,  
   CheckChain ExcludeRootCacheOnly = 6,  
}

### Microsoft_identityServer.Management.Resources.ContactPerson
ContactType      string  
EmailAddresses   string[]  
GivenName        string  
PhoneNumbers     string[]  
Surname          string

### Microsoft.IdentityServer.PolicyModel.Configuration.ProtectionPolicySetting
- `Allow`: 字符串  
- `Require`: 字符串  
- `None`: 字符串

### Microsoft.IdentityServer.Management.Resources.Organization
DisplayName      字符串  
Name             字符串  
OrganizationUrl    字符串

### Microsoft.IdentityServer.WiaEvaluationMethodState

WiaEvaluationMethodState {  
    WiaCapabilityDetection,  
    WiaUserAgentDetection  
}

## 备注

## 相关链接

[Set-AdfsProperties](./Set-AdfsProperties.md)
