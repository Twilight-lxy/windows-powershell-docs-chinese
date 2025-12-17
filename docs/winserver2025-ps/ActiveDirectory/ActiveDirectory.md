---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 4.0.6.1
Locale: en-US
Module Guid: 43c15630-959c-49e4-a977-758c5cc93408
Module Name: ActiveDirectory
ms.date: 12/27/2016
title: ActiveDirectory
---

# ActiveDirectory Module
## 描述
Windows PowerShell 的 Active Directory 模块是一个 PowerShell 模块，它将一组 cmdlet 集合在一起。你可以使用这些 cmdlet 在一个独立的包中管理你的 Active Directory 域、Active Directory 轻量级目录服务（AD LDS）配置集以及 Active Directory 数据库挂载工具实例。

如果你的机器上没有安装Active Directory模块，你需要下载适用于你所使用操作系统的远程服务器管理工具（Remote Server Administration Tools，简称RSAT）软件包。如果你使用的是Windows 7系统，还需要在具有管理员权限的PowerShell提示符下执行`import-module ActiveDirectory`命令。详情请参阅[适用于Windows操作系统的RSAT](https://support.microsoft.com/help/2693643/remote-server-administration-tools-rsat-for-windows-operating-systems)文档。从Windows 10 2018年10月更新版本开始，RSAT作为“按需功能”（Features on Demand）的一部分直接内置在Windows 10系统中了。因此，你现在无需再下载RSAT软件包，只需进入“设置”（Settings），选择“管理可选功能”（Manage optional features），然后点击“添加功能”（Add a feature）即可查看可用的RSAT工具列表。选中所需的具体RSAT工具后进行安装；若想查看安装进度，可以点击“返回”（Back）按钮，在“管理可选功能”页面上查看安装状态。

如果你想在 PowerShell 7 中使用这个模块，请参阅 [PowerShell 7 模块兼容性](/powershell/scripting/whats-new.module-compatibility)。

## ActiveDirectory Cmdlets
### [Add-ADCentralAccessPolicyMember](./Add-ADCentralAccessPolicyMember.md)
将中央访问规则添加到 Active Directory 中的中央访问策略中。

### [Add-ADComputerServiceAccount](./Add-ADComputerServiceAccount.md)
将一个或多个服务帐户添加到 Active Directory 计算机上。

### [Add-ADDomainControllerPasswordReplicationPolicy](./Add-ADDomainControllerPasswordReplicationPolicy.md)
将用户、计算机和组添加到只读域控制器密码复制策略的允许列表或拒绝列表中。

### [Add-ADFineGrainedPasswordPolicySubject](./Add-ADFineGrainedPasswordPolicySubject.md)
将细粒度的密码策略应用于一个或多个用户和组。

### [Add-ADGroupMember](./Add-ADGroupMember.md)
向一个 Active Directory 组中添加一个或多个成员。

### [Add-ADPrincipalGroupMembership](./Add-ADPrincipalGroupMembership.md)
将一个成员添加到一个或多个 Active Directory 组中。

### [Add-ADResourcePropertyListMember](./Add-ADResourcePropertyListMember.md)
将一个或多个资源属性添加到 Active Directory 中的资源属性列表中。

### [Clear-ADAccountExpiration](./Clear-ADAccountExpiration.md)
清除 Active Directory 账户的过期日期。

### [Clear-ADClaimTransformLink](./Clear-ADClaimTransformLink.md)
移除对 Active Directory 中一个或多个跨林信任关系应用的声明转换（claims transformation）。

### [Complete-ADServiceAccountMigration](./Complete-ADServiceAccountMigration.md)
完成将服务账户迁移到委托管理的服务账户的过程。

### [Disable-ADAccount](./Disable-ADAccount.md)
禁用一个 Active Directory 账户。

### [Disable-ADOptionalFeature](./Disable-ADOptionalFeature.md)
禁用 Active Directory 的一个可选功能。

### [Enable-ADAccount](./Enable-ADAccount.md)
启用一个 Active Directory 账户。

### [Enable-ADOptionalFeature](./Enable-ADOptionalFeature.md)
启用 Active Directory 的一个可选功能。

### [Get-ADAccountAuthorizationGroup](./Get-ADAccountAuthorizationGroup.md)
获取账户令牌组信息。

### [Get-ADAccountResultantPasswordReplicationPolicy](./Get-ADAccountResultantPasswordReplicationPolicy.md)
获取与Active Directory账户相关的密码复制策略信息。

### [Get-ADAuthenticationPolicy](./Get-ADAuthenticationPolicy.md)
获取一个或多个 Active Directory 域服务身份验证策略。

### [Get-ADAuthenticationPolicySilo](./Get-ADAuthenticationPolicySilo.md)
获取一个或多个 Active Directory 域服务（AD DS）身份验证策略孤岛（即各自独立、互不关联的身份验证策略集合）。

### [Get-ADCentralAccessPolicy](./Get-ADCentralAccessPolicy.md)
从 Active Directory 中检索中央访问策略。

### [Get-ADCentralAccessRule](./Get-ADCentralAccessRule.md)
从 Active Directory 中检索中央访问规则。

### [Get-ADClaimTransformPolicy](./Get-ADClaimTransformPolicy.md)
根据指定的筛选条件返回一个或多个 Active Directory 主张转换对象（Claim Transform Object）。

### [Get-ADClaimType](./Get-ADClaimType.md)
从 Active Directory 返回一个声明类型（claim type）。

### [Get-ADComputer](./Get-ADComputer.md)
获取一台或多台 Active Directory 服务器。

### [Get-ADComputerServiceAccount](./Get-ADComputerServiceAccount.md)
获取由某台计算机托管的服务账户信息。

### [Get-ADDCCloningExcludedApplicationList](./Get-ADDCCloningExcludedApplicationList.md)
获取该域控制器上已安装的程序和服务的列表，这些程序和服务不在默认的或用户自定义的包含列表中。

### [Get-ADDefaultDomainPasswordPolicy](./Get-ADDefaultDomainPasswordPolicy.md)
获取 Active Directory 域的默认密码策略。

### [Get-ADDomain](./Get-ADDomain.md)
获取一个 Active Directory 域名。

### [Get-ADDomainController](./Get-ADDomainController.md)
根据可发现的服务标准、搜索参数，或通过提供域控制器标识符（如NetBIOS名称），获取一个或多个Active Directory域控制器。

### [Get-ADDomainControllerPasswordReplicationPolicy](./Get-ADDomainControllerPasswordReplicationPolicy.md)
获取只读域控制器密码复制策略中允许列表（allowed list）或拒绝列表（denied list）的成员信息。

### [Get-ADDomainControllerPasswordReplicationPolicyUsage](./Get-ADDomainControllerPasswordReplicationPolicyUsage.md)
获取那些由只读域控制器进行身份验证的 Active Directory 账户，或者那些在域控制器的公开列表中的账户。

### [Get-ADFineGrainedPasswordPolicy](./Get-ADFineGrainedPasswordPolicy.md)
获取一个或多个 Active Directory 细粒化的密码策略。

### [Get-ADFineGrainedPasswordPolicySubject](./Get-ADFineGrainedPasswordPolicySubject.md)
获取适用细粒度密码策略的用户和组。

### [Get-ADForest](./Get-ADForest.md)
获取一个 Active Directory 林（Active Directory forest）。

### [Get-ADGroup](./Get-ADGroup.md)
获取一个或多个 Active Directory 组。

### [Get-ADGroupMember](./Get-ADGroupMember.md)
获取Active Directory组的成员信息。

### [Get-ADObject](./Get-ADObject.md)
获取一个或多个 Active Directory 对象。

### [Get-ADOptionalFeature](./Get-ADOptionalFeature.md)
获取一个或多个 Active Directory 可选功能。

### [Get-ADOrganizationalUnit](./Get-ADOrganizationalUnit.md)
获取一个或多个 Active Directory 组织单元。

### [Get-ADPrincipalGroupMembership](./Get-ADPrincipalGroupMembership.md)
获取包含指定用户、计算机、组或服务账户的 Active Directory 组。

### [Get-ADReplicationAttributeMetadata](./Get-ADReplicationAttributeMetadata.md)
获取一个或多个 Active Directory 复制伙伴的复制元数据。

### [Get-ADReplicationConnection](./Get-ADReplicationConnection.md)
根据指定的过滤器返回一个特定的 Active Directory 复制连接对象，或者一组 Active Directory 复制连接对象。

### [Get-ADReplicationFailure](./Get-ADReplicationFailure.md)
返回一个数据集合，用于描述 Active Directory 复制失败的情况。

### [Get-ADReplicationPartnerMetadata](./Get-ADReplicationPartnerMetadata.md)
返回一组一个或多个复制伙伴的复制元数据。

### [Get-ADReplicationQueueOperation](./Get-ADReplicationQueueOperation.md)
返回指定服务器的复制队列中的内容。

### [Get-ADReplicationSite](./Get-ADReplicationSite.md)
根据指定的过滤器返回一个特定的 Active Directory 复制站点或一组复制站点对象。

### [Get-ADReplicationSiteLink](./Get-ADReplicationSiteLink.md)
根据指定的过滤器返回一个特定的 Active Directory 站点链接或一组站点链接。

### [Get-ADReplicationSiteLinkBridge](./Get-ADReplicationSiteLinkBridge.md)
根据指定的筛选条件获取特定的 Active Directory 站点链接桥（site link bridge）或一组站点链接桥对象。

### [Get-ADReplicationSubnet](./Get-ADReplicationSubnet.md)
获取一个或多个 Active Directory 子网。

### [Get-ADReplicationUpToDatenessVectorTable](./Get-ADReplicationUpToDatenessVectorTable.md)
显示指定域控制器的最高更新序列号（Update Sequence Number，简称 USN）。

### [Get-ADResourceProperty](./Get-ADResourceProperty.md)
获取一个或多个资源属性。

### [Get-ADResourcePropertyList](./Get-ADResourcePropertyList.md)
从 Active Directory 中获取资源属性列表。

### [Get-ADResourcePropertyValueType](./Get-ADResourcePropertyValueType.md)
从 Active Directory 中获取资源属性的值类型。

### [Get-ADRootDSE](./Get-ADRootDSE.md)
获取目录服务器信息树的根节点。

### [Get-ADServiceAccount](./Get-ADServiceAccount.md)
获取一个或多个由 Active Directory 管理的服务账户或由组管理的服务账户。

### [Get-ADTrust](./Get-ADTrust.md)
获取目录中所有受信任的域对象。

### [Get-ADUser](./Get-ADUser.md)
获取一个或多个 Active Directory 用户。

### [Get-ADUserResultantPasswordPolicy](./Get-ADUserResultantPasswordPolicy.md)
获取用户的最终密码策略。

### [Grant-ADAuthenticationPolicySiloAccess](./Grant-ADAuthenticationPolicySiloAccess.md)
允许加入某个身份验证策略组（即“认证策略孤岛”）。

### [Install-ADServiceAccount](./Install-ADServiceAccount.md)
在计算机上安装一个由 Active Directory 管理的服务账户，或在计算机上缓存一个组管理服务账户。

### [Move-ADDirectoryServer](./Move-ADDirectoryServer.md)
将 Active Directory 中的目录服务器移动到新的站点。

### [Move-ADDirectoryServerOperationMasterRole](./Move-ADDirectoryServerOperationMasterRole.md)
将操作主节点的角色迁移到Active Directory目录服务器上。

### [Move-ADObject](./Move-ADObject.md)
将一个 Active Directory 对象或对象容器移动到另一个容器或域中。

### [New-ADAuthenticationPolicy](./New-ADAuthenticationPolicy.md)
创建一个 Active Directory 域服务身份验证策略对象。

### [New-ADAuthenticationPolicySilo](./New-ADAuthenticationPolicySilo.md)
创建一个 Active Directory 域服务（AD DS）身份验证策略对象。

### [New-ADCentralAccessPolicy](./New-ADCentralAccessPolicy.md)
在 Active Directory 中创建一个新的中央访问策略，其中包含一组中央访问规则。

### [New-ADCentralAccessRule](./New-ADCentralAccessRule.md)
在 Active Directory 中创建一条中央访问规则。

### [New-ADClaimTransformPolicy](./New-ADClaimTransformPolicy.md)
在 Active Directory 中创建一个新的声明转换策略对象。

### [New-ADClaimType](./New-ADClaimType.md)
在 Active Directory 中创建一个新的声明类型（claim type）。

### [New-ADComputer](./New-ADComputer.md)
创建一个新的 Active Directory 计算机对象。

### [New-ADDCCloneConfigFile](./New-ADDCCloneConfigFile.md)
执行克隆域控制器所需的预检查；如果所有检查都通过，则生成克隆配置文件。

### [New-ADFineGrainedPasswordPolicy](./New-ADFineGrainedPasswordPolicy.md)
创建一个新的 Active Directory 细粒度密码策略。

### [New-ADGroup](./New-ADGroup.md)
创建一个 Active Directory 组。

### [New-ADObject](./New-ADObject.md)
创建一个 Active Directory 对象。

### [New-ADOrganizationalUnit](./New-ADOrganizationalUnit.md)
创建一个 Active Directory 组织单位。

### [New-ADReplicationSite](./New-ADReplicationSite.md)
在目录中创建一个 Active Directory 复制站点。

### [New-ADReplicationSiteLink](./New-ADReplicationSiteLink.md)
创建一个新的 Active Directory 站点链接，以便管理复制过程。

### [New-ADReplicationSiteLinkBridge](./New-ADReplicationSiteLinkBridge.md)
在 Active Directory 中创建一个站点链接桥以用于复制。

### [New-ADReplicationSubnet](./New-ADReplicationSubnet.md)
创建一个 Active Directory 复制子网对象。

### [New-ADResourceProperty](./New-ADResourceProperty.md)
在 Active Directory 中创建一个资源属性。

### [New-ADResourcePropertyList](./New-ADResourcePropertyList.md)
在 Active Directory 中创建一个资源属性列表。

### [New-ADServiceAccount](./New-ADServiceAccount.md)
创建一个新的 Active Directory 管理服务账户或组管理服务账户对象。

### [New-ADUser](./New-ADUser.md)
创建一个 Active Directory 用户。

### [Remove-ADAuthenticationPolicy](./Remove-ADAuthenticationPolicy.md)
删除一个 Active Directory 域服务（Domain Services）的身份验证策略对象。

### [Remove-ADAuthenticationPolicySilo](./Remove-ADAuthenticationPolicySilo.md)
删除一个 Active Directory 域服务（AD DS）身份验证策略对象。

### [Remove-ADCentralAccessPolicy](./Remove-ADCentralAccessPolicy.md)
从 Active Directory 中删除一条中央访问策略。

### [Remove-ADCentralAccessPolicyMember](./Remove-ADCentralAccessPolicyMember.md)
从 Active Directory 中的中央访问策略中删除中央访问规则。

### [Remove-ADCentralAccessRule](./Remove-ADCentralAccessRule.md)
从 Active Directory 中删除一条中央访问规则。

### [Remove-ADClaimTransformPolicy](./Remove-ADClaimTransformPolicy.md)
从 Active Directory 中删除一个声明转换策略对象。

### [Remove-ADClaimType](./Remove-ADClaimType.md)
从 Active Directory 中删除某种索赔类型。

### [Remove-ADComputer](./Remove-ADComputer.md)
删除一台 Active Directory 电脑。

### [Remove-ADComputerServiceAccount](./Remove-ADComputerServiceAccount.md)
从计算机中删除一个或多个服务账户。

### [Remove-ADDomainControllerPasswordReplicationPolicy](./Remove-ADDomainControllerPasswordReplicationPolicy.md)
从只读域控制器的密码复制策略的允许列表或拒绝列表中移除用户、计算机和组。

### [Remove-ADFineGrainedPasswordPolicy](./Remove-ADFineGrainedPasswordPolicy.md)
删除一个 Active Directory 的细粒度密码策略。

### [Remove-ADFineGrainedPasswordPolicySubject](./Remove-ADFineGrainedPasswordPolicySubject.md)
从一个细粒度的密码策略中移除一个或多个用户。

### [Remove-ADGroup](./Remove-ADGroup.md)
删除一个Active Directory组。

### [Remove-ADGroupMember](./Remove-ADGroupMember.md)
从 Active Directory 组中删除一个或多个成员。

### [Remove-ADObject](./Remove-ADObject.md)
删除一个Active Directory对象。

### [Remove-ADOrganizationalUnit](./Remove-ADOrganizationalUnit.md)
删除一个 Active Directory 组织单位。

### [Remove-ADPrincipalGroupMembership](./Remove-ADPrincipalGroupMembership.md)
将某个成员从一个或多个Active Directory组中移除。

### [Remove-ADReplicationSite](./Remove-ADReplicationSite.md)
从 Active Directory 中删除指定的复制站点对象。

### [Remove-ADReplicationSiteLink](./Remove-ADReplicationSiteLink.md)
删除用于管理复制的 Active Directory 站点链接。

### [Remove-ADReplicationSiteLinkBridge](./Remove-ADReplicationSiteLinkBridge.md)
从 Active Directory 中删除复制站点链接桥（replication site link bridge）。

### [Remove-ADReplicationSubnet](./Remove-ADReplicationSubnet.md)
从目录中删除指定的 Active Directory 复制子网对象。

### [Remove-ADResourceProperty](./Remove-ADResourceProperty.md)
从 Active Directory 中删除某个资源属性。

### [Remove-ADResourcePropertyList](./Remove-ADResourcePropertyList.md)
从 Active Directory 中删除一个或多个资源属性列表。

### [Remove-ADResourcePropertyListMember](./Remove-ADResourcePropertyListMember.md)
从 Active Directory 中的资源属性列表中删除一个或多个资源属性。

### [Remove-ADServiceAccount](./Remove-ADServiceAccount.md)
删除一个由 Active Directory 管理的服务账户对象或组管理的服务账户对象。

### [Remove-ADUser](./Remove-ADUser.md)
删除一个 Active Directory 用户。

### [Rename-ADObject](./Rename-ADObject.md)
更改Active Directory对象的名称。

### [Reset-ADServiceAccountMigration](./Reset-ADServiceAccountMigration.md)
将委托管理的服务账户与用户账户解绑（即重置关联关系并断开链接）。

### [Reset-ADServiceAccountPassword](./Reset-ADServiceAccountPassword.md)
重置独立管理服务账户的密码。

### [Restore-ADObject](./Restore-ADObject.md)
恢复一个 Active Directory 对象。

### [Revoke-ADAuthenticationPolicySiloAccess](./Revoke-ADAuthenticationPolicySiloAccess.md)
撤销指定账户在某个身份验证策略组（即“认证策略孤岛”）中的成员资格。

### [Search-ADAccount](./Search-ADAccount.md)
获取 Active Directory 中的用户、计算机或服务账户信息。

### [Set-ADAccountAuthenticationPolicySilo](./Set-ADAccountAuthenticationPolicySilo.md)
修改某个账户的身份验证策略或身份验证策略配置（即该账户所使用的身份验证规则集合）。

### [Set-ADAccountControl](./Set-ADAccountControl.md)
修改Active Directory账户的用户账户控制（UAC）设置。

### [Set-ADAccountExpiration](./Set-ADAccountExpiration.md)
设置 Active Directory 账户的过期日期。

### [Set-ADAccountPassword](./Set-ADAccountPassword.md)
修改Active Directory账户的密码。

### [Set-ADAuthenticationPolicy](./Set-ADAuthenticationPolicy.md)
修改 Active Directory 域服务（AD DS）中的身份验证策略对象。

### [Set-ADAuthenticationPolicySilo](./Set-ADAuthenticationPolicySilo.md)
修改一个 Active Directory 域服务（AD DS）身份验证策略相关对象。

### [Set-ADCentralAccessPolicy](./Set-ADCentralAccessPolicy.md)
修改 Active Directory 中的核心访问策略。

### [Set-ADCentralAccessRule](./Set-ADCentralAccessRule.md)
修改 Active Directory 中的一条核心访问规则。

### [Set-ADClaimTransformLink](./Set-ADClaimTransformLink.md)
将声明转换（claims transformation）应用到一个或多个Active Directory中的跨林信任关系（cross-forest trust relationships）上。

### [Set-ADClaimTransformPolicy](./Set-ADClaimTransformPolicy.md)
用于设置 Active Directory 中声明转换策略（claims transformation policy）的属性。

### [Set-ADClaimType](./Set-ADClaimType.md)
修改 Active Directory 中的一种声明类型（claim type）。

### [Set-ADComputer](./Set-ADComputer.md)
修改一个 Active Directory 计算机对象。

### [Set-ADDefaultDomainPasswordPolicy](./Set-ADDefaultDomainPasswordPolicy.md)
修改Active Directory域的默认密码策略。

### [Set-ADDomain](./Set-ADDomain.md)
修改一个Active Directory域。

### [Set-ADDomainMode](./Set-ADDomainMode.md)
用于设置 Active Directory 域的域模式。

### [Set-ADFineGrainedPasswordPolicy](./Set-ADFineGrainedPasswordPolicy.md)
修改 Active Directory 的细粒度密码策略。

### [Set-ADForest](./Set-ADForest.md)
修改一个 Active Directory 林（即多个域组成的集合）。

### [Set-ADForestMode](./Set-ADForestMode.md)
为Active Directory林设置森林模式（forest mode）。

### [Set-ADGroup](./Set-ADGroup.md)
修改一个 Active Directory 组。

### [Set-ADObject](./Set-ADObject.md)
修改一个Active Directory对象。

### [Set-ADOrganizationalUnit](./Set-ADOrganizationalUnit.md)
修改一个 Active Directory 组织单元。

### [Set-ADReplicationConnection](./Set-ADReplicationConnection.md)
设置 Active Directory 复制连接的属性。

### [Set-ADReplicationSite](./Set-ADReplicationSite.md)
设置 Active Directory 站点的复制属性。

### [Set-ADReplicationSiteLink](./Set-ADReplicationSiteLink.md)
用于设置 Active Directory 站点链接的属性。

### [Set-ADReplicationSiteLinkBridge](./Set-ADReplicationSiteLinkBridge.md)
用于设置 Active Directory 中复制站点链接桥的属性。

### [Set-ADReplicationSubnet](./Set-ADReplicationSubnet.md)
用于设置 Active Directory 复制子网对象的属性。

### [Set-ADResourceProperty](./Set-ADResourceProperty.md)
修改 Active Directory 中的资源属性。

### [Set-ADResourcePropertyList](./Set-ADResourcePropertyList.md)
修改 Active Directory 中的资源属性列表。

### [Set-ADServiceAccount](./Set-ADServiceAccount.md)
修改一个由 Active Directory 管理的服务账户对象或组管理的服务账户对象。

### [Set-ADUser](./Set-ADUser.md)
修改一个 Active Directory 用户的信息。

### [Show-ADAuthenticationPolicyExpression](./Show-ADAuthenticationPolicyExpression.md)
显示“编辑访问控制条件”窗口，用于更新或创建安全描述符定义语言（SDDL）所定义的安全描述符。

### [Start-ADServiceAccountMigration](./Start-ADServiceAccountMigration.md)
开始将用户账户迁移到委托管理的服务账户。

### [Sync-ADObject](./Sync-ADObject.md)
在任意两个具有相同分区的域控制器之间复制单个对象。

### [Test-ADServiceAccount](./Test-ADServiceAccount.md)
从计算机上测试一个托管服务账户。

### [Undo-ADServiceAccountMigration](./Undo-ADServiceAccountMigration.md)
将委托管理的托管服务账户的迁移状态恢复到用户账户的状态。

### [Uninstall-ADServiceAccount](./Uninstall-ADServiceAccount.md)
从计算机上卸载由 Active Directory 管理的服务账户，或从计算机中删除缓存中的组管理服务账户。

### [Unlock-ADAccount](./Unlock-ADAccount.md)
解锁一个 Active Directory 账户。
