---
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.0.1
Locale: en-US
Module Guid: 5c958595-c68c-4c00-a468-9763de83bbee
Module Name: ADFS
---

# ADFS 模块
## 描述
本参考文档为IT专业人员提供了Windows PowerShell命令行的使用说明。通过这些命令行工具，您可以部署和管理Windows Server中的Active Directory Federation Services（AD FS）。

## ADFSCmdlets
### [Add-AdfsAttributeStore](Add-AdfsAttributeStore.md)
向联邦服务（Federation Service）添加一个属性存储（attribute store）。

### [添加 AdFS 证书](Add-AdfsCertificate.md)
向 AD FS 添加新的证书，用于签名、解密或保护通信安全。

### [Add-AdfsClaimDescription](Add-AdfsClaimDescription.md)
向联邦服务添加一个声明描述（claim description）。

### [Add-AdfsClaimsProviderTrust](Add-AdfsClaimsProviderTrust.md)
向联邦服务（Federation Service）添加一个新的声明提供者信任关系（claims provider trust）。

### [Add-AdfsClaimsProviderTrustsGroup](Add-AdfsClaimsProviderTrustsGroup.md)
根据包含多个实体的元数据创建一个声明提供者信任组（claims provider trust group）。

### [Add-AdfsClient](Add-AdfsClient.md)
将一个 OAuth 2.0 客户端注册到 AD FS（Active Directory Federation Services）中。

### [Add-AdfsDeviceRegistrationUpnSuffix](Add-AdfsDeviceRegistrationUpnSuffix.md)
添加一个自定义的 UPN 后缀。

### [Add-AdfsFarmNode](Add-AdfsFarmNode.md)
将这台计算机添加到现有的联合服务器群中。

### [Add-AdfsLocalClaimsProviderTrust](Add-AdfsLocalClaimsProviderTrust.md)
创建一个本地的声明提供者信任（claims provider trust）。

### [Add-AdfsNativeClientApplication](Add-AdfsNativeClientApplication.md)
在 Active Directory Federation Services (AD FS) 中为某个应用程序添加一个本机客户端应用程序角色。

### [Add-AdfsNonClaimsAwareRelyingPartyTrust](Add-AdfsNonClaimsAwareRelyingPartyTrust.md)
向联邦服务添加一个依赖方信任（relaying party trust），该信任代表一个不支持处理身份验证请求（claims）的Web应用程序或服务。

### [Add-AdfsRelyingPartyTrust](Add-AdfsRelyingPartyTrust.md)
向联邦服务（Federation Service）添加一个新的依赖方信任（relying party trust）。

### [Add-AdfsRelyingPartyTrustsGroup](Add-AdfsRelyingPartyTrustsGroup.md)
创建一个依赖方信任组（relying party trusts group）。

### [Add-AdfsScopeDescription](Add-AdfsScopeDescription.md)
在 Active Directory Federation Services (AD FS) 中添加范围描述。

### [Add-AdfsServerApplication](Add-AdfsServerApplication.md)
将一个服务器应用程序角色添加到 AD FS 中的应用程序中。

### [Add-AdfsTrustedFederationPartner](Add-AdfsTrustedFederationPartner.md)
为 AD FS 中的可信联盟合作伙伴添加配置设置。

### [Add-AdfsWebApiApplication](Add-AdfsWebApiApplication.md)
将一个Web API应用程序角色添加到AD FS中的应用程序中。

### [Add-AdfsWebApplicationProxyRelyingPartyTrust](Add-AdfsWebApplicationProxyRelyingPartyTrust.md)
为Web应用程序代理添加一个依赖方信任（relying party trust）。

### [ Disable-AdfsApplicationGroup](Disable-AdfsApplicationGroup.md)
禁用一个应用程序组。

### [ Disable-AdfsCertificateAuthority](Disable-AdfsCertificateAuthority.md)
禁用一个证书颁发机构（CA）。

### [禁用 AdfsClaimsProviderTrust](Disable-AdfsClaimsProviderTrust.md)
禁用联邦服务中对某个声明提供者（claims provider）的信任。

### [ Disable-AdfsClient](Disable-AdfsClient.md)
禁用当前已注册到 AD FS 的 OAuth 2.0 客户端。

### [禁用 AdfsDeviceRegistration 功能](Disable-AdfsDeviceRegistration.md)
将设备注册服务标记为在 AD FS 服务器上处于禁用状态。

### [ Disable-AdfsEndpoint](Disable-AdfsEndpoint.md)
禁用 AD FS 的某个终端点（endpoint）。

### [禁用 AdfsLocalClaimsProviderTrust](Disable-AdfsLocalClaimsProviderTrust.md)
禁用本地声明提供者的信任机制。

### [禁用 AdfsNonClaims Aware Relying Party Trust]( Disable-AdfsNonClaimsAwareRelyingPartyTrust.md)
对于那些不支持“声明处理”（claim handling）功能的Web应用程序或服务，该功能会禁用联邦服务（Federation Service）所提供的依赖方信任（relying party trust）机制。

### [禁用 AdfsRelyingPartyTrust]( Disable-AdfsRelyingPartyTrust.md)
禁用联邦服务的依赖方信任（relying party trust）。

### [禁用 AdfsWebApplicationProxy 依赖方信任](Disable-AdfsWebApplicationProxyRelyingPartyTrust.md)
禁用对 Web 应用程序代理的依赖方信任（relaying party trust）。

### [Enable-AdfsApplicationGroup](Enable-AdfsApplicationGroup.md)
在 Active Directory Federation Services (AD FS) 中启用一个应用程序组。

### [Enable-AdfsClaimsProviderTrust](Enable-AdfsClaimsProviderTrust.md)
使声明提供者（claims provider）能够信任联邦服务（Federation Service）。

### [Enable-AdfsClient](Enable-AdfsClient.md)
允许通过 Active Directory Federation Services (AD FS) 使用 OAuth 2.0 客户端注册功能。

### [Enable-AdfsDeviceRegistration](Enable-AdfsDeviceRegistration.md)
此cmdlet已被弃用。

### [Enable-AdfsEndpoint](Enable-AdfsEndpoint.md)
启用 AD FS 中的一个端点。

### [Enable-AdfsLocalClaimsProviderTrust](Enable-AdfsLocalClaimsProviderTrust.md)
启用对本地索赔提供者的信任机制。

### [Enable-AdfsNonClaimsAwareRelyingPartyTrust](Enable-AdfsNonClaimsAwareRelyingPartyTrust.md)
该功能使依赖方能够信任来自联邦服务的、不支持索赔处理（即不识别或处理用户提出的索赔请求）的Web应用程序或服务。

### [Enable-AdfsRelyingPartyTrust](Enable-AdfsRelyingPartyTrust.md)
使依赖方能够信任联邦服务（Federation Service）。

### [Enable-AdfsWebApplicationProxyRelyingPartyTrust](Enable-AdfsWebApplicationProxyRelyingPartyTrust.md)
启用Web应用程序代理的可信赖方信任对象。

### [Export-AdfsAuthenticationProviderConfigurationData](Export-AdfsAuthenticationProviderConfigurationData.md)
返回一个文件，其中包含用于配置AD FS农场以支持Azure Multi-Factor Authentication（MFA）的租户ID，以及Azure MFA所使用的通用客户端ID。

### [Export-AdfsDeploymentSQLScript](Export-AdfsDeploymentSQLScript.md)
生成SQL脚本，用于创建AD FS数据库并授予相应的权限。

### [Export-AdfsWebContent](Export-AdfsWebContent.md)
将所有网页内容对象在特定区域设置（locale）下的属性导出到指定的文件中。

### [Export-AdfsWebTheme](Export-AdfsWebTheme.md)
将一个网页主题导出到一个文件夹中。

### [Get-AdfsAccessControlPolicy](Get-AdfsAccessControlPolicy.md)
获取一个 AD FS 访问控制策略。

### [Get-AdfsAdditionalAuthenticationRule](Get-AdfsAdditionalAuthenticationRule.md)
检索会触发其他身份验证提供者被调用的全局规则。

### [Get-AdfsApplicationGroup](Get-AdfsApplicationGroup.md)
获取一个应用程序组。

### [Get-AdfsApplicationPermission](Get-AdfsApplicationPermission.md)
获取应用程序使用的权限。

### [Get-AdfsAttributeStore](Get-AdfsAttributeStore.md)
获取联邦服务的属性存储信息。

### [Get-AdfsAuthenticationProvider](Get-AdfsAuthenticationProvider.md)
获取 AD FS 中所有身份验证提供程序的列表。

### [Get-AdfsAuthenticationProviderWebContent](Get-AdfsAuthenticationProviderWebContent.md)
为身份验证提供者检索网页内容对象。

### [Get-AdfsAzureMfaConfigured](Get-AdfsAzureMfaConfigured.md)
用于获取是否启用了Azure多因素身份验证（MFA）。

### [Get-AdfsCertificate](Get-AdfsCertificate.md)
从 AD FS 中检索证书。

### [Get-AdfsCertificateAuthority](Get-AdfsCertificateAuthority.md)
获取一个证书颁发机构（Certificate Authority）。

### [Get-AdfsClaimDescription](Get-AdfsClaimDescription.md)
从联邦服务（Federation Service）获取索赔描述。

### [Get-AdfsClaimsProviderTrust](Get-AdfsClaimsProviderTrust.md)
获取联邦服务中使用的声明提供者信任关系（claims provider trusts）。

### [Get-AdfsClaimsProviderTrustsGroup](Get-AdfsClaimsProviderTrustsGroup.md)
获取一个 AD FS 主张提供者信任组。

### [Get-AdfsClient](Get-AdfsClient.md)
检索 OAuth 2.0 客户端的注册信息。

### [Get-AdfsDeviceRegistration](Get-AdfsDeviceRegistration.md)
获取设备注册服务的管理策略信息。

### [Get-AdfsDeviceRegistrationUpnSuffix](Get-AdfsDeviceRegistrationUpnSuffix.md)
获取可用于设备注册的 UPN 后缀。

### [Get-AdfsEndpoint](Get-AdfsEndpoint.md)
从 AD FS 中检索一个端点。

### [Get-AdfsFarmInformation](Get-AdfsFarmInformation.md)
获取 AD FS 行为级别和农场节点信息。

### [Get-AdfsGlobalAuthenticationPolicy](Get-AdfsGlobalAuthenticationPolicy.md)
显示 AD FS 全局策略。

### [Get-AdfsGlobalWebContent](Get-AdfsGlobalWebContent.md)
获取全局网页内容对象。

### [Get-AdfsLocalClaimsProviderTrust](Get-AdfsLocalClaimsProviderTrust.md)
获取本地的声明提供者信任关系（即本地声明提供者被信任的程度）。

### [Get-AdfsNativeClientApplication](Get-AdfsNativeClientApplication.md)
从 AD FS 中的应用程序获取本机客户端应用程序的角色信息。

### [Get-AdfsNonClaimsAwareRelyingPartyTrust](Get-AdfsNonClaimsAwareRelyingPartyTrust.md)
为不支持声明处理（claims-aware）的Web应用程序或服务获取依赖方信任（relying party trust）的相关属性。

### [Get-AdfsProperties](Get-AdfsProperties.md)
获取与 AD FS 服务相关的所有属性。

### [Get-AdfsRegistrationHosts](Get-AdfsRegistrationHosts.md)
`Get-AdfsRegistrationHosts` cmdlet 已被弃用。请使用 `Get-AdfsDeviceRegistrationUpnSuffix` cmdlet 代替它。

### [Get-AdfsRelyingPartyTrust](Get-AdfsRelyingPartyTrust.md)
获取联邦服务的依赖方信任信息。

### [Get-AdfsRelyingPartyTrustsGroup](Get-AdfsRelyingPartyTrustsGroup.md)
获取一个依赖方信任组。

### [Get-AdfsRelyingPartyWebContent](Get-AdfsRelyingPartyWebContent.md)
为依赖方获取网页内容对象。

### [Get-AdfsRelyingPartyWebTheme](Get-AdfsRelyingPartyWebTheme.md)
获取应用于依赖方信任（relying party trusts）的网页主题的相关属性。

### [Get-AdfsScopeDescription](Get-AdfsScopeDescription.md)
获取 AD FS 中某个作用域（scope）的描述信息。

### [Get-AdfsServerApplication](Get-AdfsServerApplication.md)
获取用于 AD FS 中某个应用程序的服务器应用角色的配置设置。

### [Get-AdfsSslCertificate](Get-AdfsSslCertificate.md)
获取为 AD FS 和设备注册服务配置的 SSL 绑定的主机名、端口以及证书哈希值。

### [Get-AdfsSyncProperties](Get-AdfsSyncProperties.md)
从 AD FS 的配置数据库中获取同步属性。

### [Get-AdfsTrustedFederationPartner](Get-AdfsTrustedFederationPartner.md)
在 Active Directory Federation Services (AD FS) 中找到一个可信赖的联盟合作伙伴。

### [Get-AdfsWebApiApplication](Get-AdfsWebApiApplication.md)
在 AD FS 中获取 Web API 应用程序角色。

### [Get-AdfsWebApplicationProxyRelyingPartyTrust](Get-AdfsWebApplicationProxyRelyingPartyTrust.md)
获取用于 Web 应用程序代理的依赖方信任对象。

### [Get-AdfsWebConfig](Get-AdfsWebConfig.md)
获取 AD FS Web 定制配置设置。

### [Get-AdfsWebTheme](Get-AdfsWebTheme.md)
可以获取网页主题（web themes）。

### [Grant-AdfsApplicationPermission](Grant-AdfsApplicationPermission.md)
允许申请补助金（或拨款等）。

### [Import-AdfsAuthenticationProviderConfigurationData](Import-AdfsAuthenticationProviderConfigurationData.md)
导入用于身份验证提供者的自定义配置。

### [Import-AdfsWebContent](Import-AdfsWebContent.md)
从资源文件中导入属性，并将其添加到全局对象以及依赖方的网页内容对象中。

### [Initialize-ADDeviceRegistration]( Initialize-ADDeviceRegistration.md)
在 Active Directory 林中初始化设备注册服务（Device Registration Service）的配置。

### [安装 AdfsFarm](Install-AdfsFarm.md)
创建一个新的联邦服务器群组中的第一个节点。

### [Invoke-AdfsFarmBehaviorLevelRaise](Invoke-AdfsFarmBehaviorLevelRaise.md)
提升农场的整体管理水平和运营效率。

### [新 AdfsAccessControlPolicy](New-AdfsAccessControlPolicy.md)
创建一个 AD FS 访问控制策略。

### [New-AdfsApplicationGroup](New-AdfsApplicationGroup.md)
创建一个应用程序组。

### [New-AdfsAzureMfaTenantCertificate](New-AdfsAzureMfaTenantCertificate.md)
为 AD FS 农场创建一个证书，以便用于连接到 Azure MFA；或者返回当前配置的证书。

### [New-AdfsClaimRuleSet](New-AdfsClaimRuleSet.md)
创建一组声明规则。

### [New-AdfsContactPerson](New-AdfsContactPerson.md)
创建一个联系人对象。

### [New-AdfsLdapAttributeToClaimMapping](New-AdfsLdapAttributeToClaimMapping.md)
创建一个映射关系，将LDAP文件夹中的属性与AD FS声明类型关联起来。

### [New-AdfsLdapServerConnection](New-AdfsLdapServerConnection.md)
创建一个连接对象。

### [New-AdfsOrganization](New-AdfsOrganization.md)
创建一个新的组织信息对象。

### [New-AdfsSamlEndpoint](New-AdfsSamlEndpoint.md)
创建一个SAML协议端点对象。

### [New-AdfsWebTheme](New-AdfsWebTheme.md)
创建一个 AD FS 网页主题。

### [Publish-SslCertificate](Publish-SslCertificate.md)
`Publish-SslCertificate` cmdlet 已被弃用。请使用 `Set-AdfsSslCertificate` cmdlet 代替它。

### [注册 AdfsAuthenticationProvider](Register-AdfsAuthenticationProvider.md)
在 AD FS 中注册一个外部身份验证提供程序。

### [Remove-AdfsAccessControlPolicy](Remove-AdfsAccessControlPolicy.md)
删除一个 AD FS 访问控制策略。

### [Remove-AdfsApplicationGroup](Remove-AdfsApplicationGroup.md)
删除一个应用程序组。

### [Remove-AdfsAttributeStore](Remove-AdfsAttributeStore.md)
从联邦服务中删除一个属性存储（attribute store）。

### [Remove-AdfsAuthenticationProviderWebContent](Remove-AdfsAuthenticationProviderWebContent.md)
从 Active Directory Federation Services (AD FS) 的用户登录网页中移除了身份验证提供者的 Web 内容自定义功能。

### [Remove-AdfsCertificate](Remove-AdfsCertificate.md)
从 AD FS 中删除证书。

### [Remove-AdfsClaimDescription](Remove-AdfsClaimDescription.md)
从联邦服务中删除一个索赔描述。

### [Remove-AdfsClaimsProviderTrust](Remove-AdfsClaimsProviderTrust.md)
从联合服务（Federation Service）中移除某个声明提供者（claims provider）的信任关系。

### [Remove-AdfsClaimsProviderTrustsGroup](Remove-AdfsClaimsProviderTrustsGroup.md)
删除一个 AD FS 主张提供者信任组。

### [Remove-AdfsClient](Remove-AdfsClient.md)
删除当前在 AD FS 中注册的 OAuth 2.0 客户端的注册信息。

### [Remove-AdfsDeviceRegistrationUpnSuffix](Remove-AdfsDeviceRegistrationUpnSuffix.md)
删除自定义的UPN后缀。

### [Remove-AdfsFarmNode](Remove-AdfsFarmNode.md)
`Remove-AdfsFarmNode` cmdlet 已被弃用。请改用 `Uninstall-WindowsFeature` cmdlet。

### [Remove-AdfsGlobalWebContent](Remove-AdfsGlobalWebContent.md)
删除一个全局性的网页内容对象。

### [Remove-AdfsLocalClaimsProviderTrust](Remove-AdfsLocalClaimsProviderTrust.md)
移除对某个本地声明提供者的信任。

### [Remove-AdfsNativeClientApplication](Remove-AdfsNativeClientApplication.md)
从 AD FS 中的应用程序中移除一个本机客户端应用程序角色。

### [Remove-AdfsNonClaimsAwareRelyingPartyTrust](Remove-AdfsNonClaimsAwareRelyingPartyTrust.md)
将一个不支持声明处理的Web应用程序或服务的依赖方信任信息从联邦服务（Federation Service）中删除。

### [Remove-AdfsRelyingPartyTrust](Remove-AdfsRelyingPartyTrust.md)
从联合服务（Federation Service）中移除某个依赖方信任关系（relying party trust）。

### [Remove-AdfsRelyingPartyTrustsGroup](Remove-AdfsRelyingPartyTrustsGroup.md)
删除一个依赖方信任组（relying party trusts group）。

### [Remove-AdfsRelyingPartyWebContent](Remove-AdfsRelyingPartyWebContent.md)
删除一个依赖方（relying party）的网页内容对象。

### [Remove-AdfsRelyingPartyWebTheme](Remove-AdfsRelyingPartyWebTheme.md)
将一个网络主题从依赖该主题的第三方系统中移除。

### [Remove-AdfsScopeDescription](Remove-AdfsScopeDescription.md)
删除 Active Directory Federation Services (AD FS) 中的范围描述（scope description）。

### [Remove-AdfsServerApplication](Remove-AdfsServerApplication.md)
从 Active Directory Federation Services (AD FS) 中的应用程序中移除一个服务器应用程序角色。

### [Remove-AdfsTrustedFederationPartner](Remove-AdfsTrustedFederationPartner.md)
从 Active Directory Federation Services (AD FS) 中移除一个受信任的联盟合作伙伴。

### [Remove-AdfsWebApiApplication](Remove-AdfsWebApiApplication.md)
从 AD FS 中的应用程序中移除一个 Web API 应用程序角色。

### [Remove-AdfsWebApplicationProxyRelyingPartyTrust](Remove-AdfsWebApplicationProxyRelyingPartyTrust.md)
移除了用于 Web 应用程序代理的依赖方信任对象（relying party trust object）。

### [Remove-AdfsWebTheme](Remove-AdfsWebTheme.md)
删除一个网页主题。

### [Restore-AdfsFarmBehaviorLevel](Restore-AdfsFarmBehaviorLevel.md)
将农场恢复到之前的运行状态（即之前的行为模式）。

### [Revoke-AdfsApplicationPermission](Revoke-AdfsApplicationPermission.md)
撤销对某个应用程序的访问权限。

### [撤销 AdfsProxyTrust 的信任关系](Revoke-AdfsProxyTrust.md)
撤销对所有为联邦服务（Federation Service）配置的联邦服务器代理（federation server proxies）的信任。

### [Set-AdfsAccessControlPolicy](Set-AdfsAccessControlPolicy.md)
修改 AD FS 访问控制策略。

### [Set-AdfsAdditionalAuthenticationRule](Set-AdfsAdditionalAuthenticationRule.md)
设置了全局规则，这些规则用于触发其他身份验证提供者的调用。

### [Set-AdfsAlternateTlsClientBinding](Set-AdfsAlternateTlsClientBinding.md)
配置现有的 AD FS 部署，使其在设备证书认证和客户端证书认证过程中使用相同的端口。

### [Set-AdfsApplicationGroup](Set-AdfsApplicationGroup.md)
修改应用程序组。

### [Set-AdfsApplicationPermission](Set-AdfsApplicationPermission.md)
修改应用程序的权限设置。

### [Set-AdfsAttributeStore](Set-AdfsAttributeStore.md)
修改属性存储（attribute store）的属性。

### [Set-AdfsAuthenticationProviderWebContent](Set-AdfsAuthenticationProviderWebContent.md)
修改显示名称和描述内容。

### [Set-AdfsAzureMfaTenant](Set-AdfsAzureMfaTenant.md)
使 AD FS 站点群能够使用多因素身份验证（MFA）。

### [Set-AdfsCertificate](Set-AdfsCertificate.md)
用于设置现有证书的属性，这些属性被 Active Directory Federation Services (AD FS) 用来签名、解密或保护通信安全。

### [Set-AdfsCertificateAuthority](Set-AdfsCertificate Authority.md)
修改证书颁发机构（CA）。

### [Set-AdfsCertSharingContainer](Set-AdfsCertSharingContainer.md)
设置用于在联邦服务器群中共享托管证书的账户。

### [Set-AdfsClaimDescription](Set-AdfsClaimDescription.md)
修改索赔描述的属性。

### [Set-AdfsClaimsProviderTrust](Set-AdfsClaimsProviderTrust.md)
设置声明提供者信任（claims provider trust）的属性。

### [Set-AdfsClient](Set-AdfsClient.md)
修改在 AD FS 中注册的 OAuth 2.0 客户端的注册设置。

### [Set-AdfsDeviceRegistration](Set-AdfsDeviceRegistration.md)
配置设备注册服务的管理策略。

### [Set-AdfsDeviceRegistrationUpnSuffix](Set-AdfsDeviceRegistrationUpnSuffix.md)
设置 UPN 后缀的列表。

### [Set-AdfsEndpoint](Set-AdfsEndpoint.md)
将端点设置在一个Web应用程序代理上。

### [Set-AdfsFarmInformation](Set-AdfsFarmInformation.md)
从农场信息表中移除不再可用或已离线的农场节点。

### [Set-AdfsGlobalAuthenticationPolicy](Set-AdfsGlobalAuthenticationPolicy.md)
修改 AD FS 全局策略。

### [Set-AdfsGlobalWebContent](Set-AdfsGlobalWebContent.md)
为全局网页内容对象设置属性。

### [Set-AdfsLocalClaimsProviderTrust](Set-AdfsLocalClaimsProviderTrust.md)
修改本地声明提供者（claims provider）的信任设置。

### [Set-AdfsNativeClientApplication](Set-AdfsNativeClientApplication.md)
修改应用程序在 AD FS 中作为服务器原生客户端应用程序角色时的配置设置。

### [Set-AdfsNonClaimsAwareRelyingPartyTrust](Set-AdfsNonClaimsAwareRelyingPartyTrust.md)
为不支持声明处理（claims-aware）的Web应用程序或服务设置依赖方信任（relying party trust）的相关属性。

### [Set-AdfsProperties](Set-AdfsProperties.md)
设置用于控制 Active Directory Federation Services (AD FS) 中全局行为的属性。

### [Set-AdfsRegistrationHosts](Set-AdfsRegistrationHosts.md)
`Set-AdfsRegistrationHosts` cmdlet 已经被弃用。请使用 `Set-AdfsDeviceRegistrationUpnSuffix` cmdlet 代替它。

### [Set-AdfsRelyingPartyTrust](Set-AdfsRelyingPartyTrust.md)
设置依赖方信任（relying party trust）的属性。

### [Set-AdfsRelyingPartyWebContent](Set-AdfsRelyingPartyWebContent.md)
为依赖方（relying party）的网页内容对象设置相关属性。

### [Set-AdfsRelyingPartyWebTheme](Set-AdfsRelyingPartyWebTheme.md)
将一个网页主题应用于依赖方（即使用该主题的网站或应用程序）。

### [Set-AdfsScopeDescription](Set-AdfsScopeDescription.md)
修改 Active Directory Federation Services (AD FS) 中的作用域描述（scope description）。

### [Set-AdfsServerApplication](Set-AdfsServerApplication.md)
修改应用程序在 Active Directory Federation Services (AD FS) 中的服务器应用角色的配置设置。

### [Set-AdfsSslCertificate](Set-AdfsSslCertificate.md)
为 AD FS 的 HTTPS 绑定设置 SSL 证书。

### [Set-AdfsSyncProperties](Set-AdfsSyncProperties.md)
修改 AD FS 配置数据库的同步频率，以及确定服务器群中的主服务器。

### [Set-AdfsTrustedFederationPartner](Set-AdfsTrustedFederationPartner.md)
修改 Active Directory Federation Services (AD FS) 中受信任的联合合作伙伴的配置设置。

### [Set-AdfsWebApiApplication](Set-AdfsWebApiApplication.md)
修改 AD FS 中 Web API 应用程序的配置设置。

### [Set-AdfsWebApplicationProxyRelyingPartyTrust](Set-AdfsWebApplicationProxyRelyingPartyTrust.md)
修改用于 Web 应用程序代理的依赖方信任对象的属性。

### [Set-AdfsWebConfig](Set-AdfsWebConfig.md)
修改网页自定义配置设置。

### [Set-AdfsWebTheme](Set-AdfsWebTheme.md)
修改网页主题的属性。

### [Test-AdfsFarmBehaviorLevelRaise](Test-AdfsFarmBehaviorLevelRaise.md)
测试你是否能够提升农场的运营效率（即提高农场的“行为水平”）。

### [Test-AdfsFarmBehaviorLevelRestore](Test-AdfsFarmBehaviorLevelRestore.md)
测试是否可以将 Active Directory Federation Services（AD FS）集群恢复到之前的运行状态。

### [Test-AdfsFarmInstallation](Test-AdfsFarmInstallation.md)
运行安装新的联合服务器群所需的先决条件检查。

### [Test-AdfsFarmJoin](Test-AdfsFarmJoin.md)
在将服务器计算机添加到联合服务器群之前，会运行必要的检查。

### [Unregister-AdfsAuthenticationProvider](Unregister-AdfsAuthenticationProvider.md)
从 AD FS 中删除外部身份验证提供程序。

### [更新 AdfsCertificate](Update-AdfsCertificate.md)
更新 AD FS 的证书。

### [更新 AdfsClaimsProviderTrust](Update-AdfsClaimsProviderTrust.md)
根据联盟元数据更新对声明提供者的信任关系。

### [Update-AdfsRelyingPartyTrust](Update-AdfsRelyingPartyTrust.md)
根据联盟元数据更新依赖方的信任关系。

