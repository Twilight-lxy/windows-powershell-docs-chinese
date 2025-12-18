---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.5.2
Locale: en-US
Module Guid: 46f598e5-9907-42b2-afbb-68e5f7e34604
Module Name: DnsServer
ms.date: 12/20/2016
title: DnsServer
---

# DnsServer 模块
## 描述
该参考文档提供了所有 DNS 服务器 cmdlet 的描述和语法信息。这些 cmdlet 按照其开头所使用的动词（即命令的动词部分）按字母顺序排列。可以通过安装“DNS 服务器”角色，或者添加“远程服务器管理工具”（Remote Server Administration Tools, RSAT）中的“DNS 服务器工具”组件来获取 DnsServer 模块。

## DnsServer Cmdlets
### [Add-DnsServerClientSubnet](./Add-DnsServerClientSubnet.md)
将一个客户端子网添加到DNS服务器中。

### [Add-DnsServerConditionalForwarderZone](./Add-DnsServerConditionalForwarderZone.md)
向DNS服务器添加一个条件转发器。

### [Add-DnsServerDirectoryPartition](./Add-DnsServerDirectoryPartition.md)
创建一个DNS应用程序目录分区。

### [Add-DnsServerForwarder](./Add-DnsServerForwarder.md)
向DNS服务器添加服务器级转发器。

### [Add-DnsServerPrimaryZone](./Add-DnsServerPrimaryZone.md)
向DNS服务器添加一个主区域。

### [Add-DnsServerQueryResolutionPolicy](./Add-DnsServerQueryResolutionPolicy.md)
为DNS服务器添加一个用于查询解析的策略。

### [Add-DnsServerRecursionScope](./Add-DnsServerRecursionScope.md)
在DNS服务器上添加一个递归作用域。

### [Add-DnsServerResourceRecord](./Add-DnsServerResourceRecord.md)
向指定的DNS区域添加一个指定类型的资源记录。

### [Add-DnsServerResourceRecordA](./Add-DnsServerResourceRecordA.md)
向DNS区域中添加一个A类型的资源记录。

### [Add-DnsServerResourceRecordAAAA](./Add-DnsServerResourceRecordAAAA.md)
向DNS服务器添加一个AAAA类型的资源记录。

### [Add-DnsServerResourceRecordCName](./Add-DnsServerResourceRecordCName.md)
向DNS区域添加一个CNAME类型资源记录。

### [Add-DnsServerResourceRecordDnsKey](./Add-DnsServerResourceRecordDnsKey.md)
向DNS区域添加一种类型的DNSKEY资源记录。

### [Add-DnsServerResourceRecordDS](./Add-DnsServerResourceRecordDS.md)
向DNS区域添加一种类型为DS的资源记录。

### [Add-DnsServerResourceRecordMX](./Add-DnsServerResourceRecordMX.md)
向DNS服务器添加一个MX资源记录。

### [Add-DnsServerResourceRecordPtr](./Add-DnsServerResourceRecordPtr.md)
向DNS服务器添加一种类型为PTR的资源记录。

### [Add-DnsServerResponseRateLimitingExceptionlist](./Add-DnsServerResponseRateLimitingExceptionlist.md)
在DNS服务器上添加一个RRL（Reverse Look-Up List，反向查找列表）异常列表。

### [Add-DnsServerRootHint](./Add-DnsServerRootHint.md)
在DNS服务器上添加根提示（root hints）。

### [Add-DnsServerSecondaryZone](./Add-DnsServerSecondaryZone.md)
添加一个DNS服务器的辅助区域（secondary zone）。

### [Add-DnsServerSigningKey](./Add-DnsServerSigningKey.md)
向已签名的区域添加KSK（Key Signing Key）或ZSK（Zone Signing Key）。

### [Add-DnsServerStubZone](./Add-DnsServerStubZone.md)
添加一个DNS存根区域（stub zone）。

### [Add-DnsServerTrustAnchor](./Add-DnsServerTrustAnchor.md)
向DNS服务器添加一个信任锚点。

### [Add-DnsServerVirtualizationInstance](./Add-DnsServerVirtualizationInstance.md)
添加一个虚拟化实例。

### [Add-DnsServerZoneDelegation](./Add-DnsServerZoneDelegation.md)
向现有的DNS区域添加一个新的委托DNS区域。

### [Add-DnsServerZoneScope](./Add-DnsServerZoneScope.md)
为现有的区域添加一个区域范围（zone scope）。

### [Add-DnsServerZoneTransferPolicy](./Add-DnsServerZoneTransferPolicy.md)
向DNS服务器添加一个区域传输策略。

### [Clear-DnsServerCache](./Clear-DnsServerCache.md)
从DNS服务器的缓存中清除资源记录。

### [Clear-DnsServerStatistics](./Clear-DnsServerStatistics.md)
清除所有DNS服务器的统计信息或各区域的统计信息。

### [将 zone 转换为 DNS 服务器的主区域](./ConvertTo-DnsServerPrimaryZone.md)
将某个区域转换为DNS主区域。

### [将区域转换为DNS服务器的辅助区域](./ConvertTo-DnsServerSecondaryZone.md)
将主区域（primary zone）或存根区域（stub zone）转换为辅助区域（secondary zone）。

### [Disable-DnsServerPolicy](./ Disable-DnsServerPolicy.md)
禁用DNS服务器策略。

### [Disable-DnsServerSigningKeyRollover](./Disable-DnsServerSigningKeyRollover.md)
禁用输入键上的按键悬停（鼠标悬停在按键上时显示相关信息的功能）。

### [Enable-DnsServerPolicy](./Enable-DnsServerPolicy.md)
启用DNS服务器策略。

### [Enable-DnsServer SigningKeyRollover](./Enable-DnsServerSigningKeyRollover.md)
启用对输入键的悬停功能（即当鼠标悬停在输入键上时发生的特定操作）。

### [Export-DnsServerDnsSecPublicKey](./Export-DnsServerDnsSecPublicKey.md)
导出DNSSEC签名区域的DS和DNSKEY信息。

### [Export-DnsServerZone](./Export-DnsServerZone.md)
将某个区域的内容导出到文件中。

### [Get-DnsServer](./Get-DnsServer.md)
检索DNS服务器配置信息。

### [Get-DnsServerCache](./Get-DnsServerCache.md)
检索DNS服务器缓存设置。

### [Get-DnsServerClientSubnet](./Get-DnsServerClientSubnet.md)
获取DNS服务器对应的客户端子网信息。

### [Get-DnsServerDiagnostics](./Get-DnsServerDiagnostics.md)
检索DNS事件日志记录的详细信息。

### [Get-DnsServerDirectoryPartition](./Get-DnsServerDirectoryPartition.md)
获取一个DNS应用程序目录分区。

### [Get-DnsServerDnsSecZoneSetting](./Get-DnsServerDnsSecZoneSetting.md)
获取某个区域的 DNSSEC 设置信息。

### [Get-DnsServerDsSetting](./Get-DnsServerDsSetting.md)
检索DNS服务器在Active Directory中的设置

### [Get-DnsServerEDns](./Get-DnsServerEDns.md)
获取DNS服务器上的EDNS配置设置信息。

### [Get-DnsServerForwarder](./Get-DnsServerForwarder.md)
获取DNS服务器上的转发器配置设置。

### [Get-DnsServerGlobalNameZone](./Get-DnsServerGlobalNameZone.md)
检索DNS服务器的GlobalName区域配置详细信息。

### [Get-DnsServerGlobalQueryBlockList](./Get-DnsServerGlobalQueryBlockList.md)
获取一个全局查询块列表。

### [Get-DnsServerQueryResolutionPolicy](./Get-DnsServerQueryResolutionPolicy.md)
从DNS服务器获取用于查询解析的策略。

### [Get-DnsServerRecursion](./Get-DnsServerRecursion.md)
检索DNS服务器的递归设置。

### [Get-DnsServerRecursionScope](./Get-DnsServerRecursionScope.md)
获取DNS服务器的递归作用域（recursion scopes）。

### [Get-DnsServerResourceRecord](./Get-DnsServerResourceRecord.md)
从指定的DNS区域获取资源记录。

### [Get-DnsServerResponseRateLimiting](./Get-DnsServerResponseRateLimiting.md)
在DNS服务器上显示RRL（Real-Time Routing Layer）配置信息。

### [Get-DnsServerResponseRateLimitingExceptionlist](./Get-DnsServerResponseRateLimitingExceptionlist.md)
枚举DNS服务器上的RRL异常列表。

### [Get-DnsServerRootHint](./Get-DnsServerRootHint.md)
从DNS服务器获取根提示信息（root hints）。

### [Get-DnsServerScavenging](./Get-DnsServerScavenging.md)
获取DNS老化（ aged）和数据清除（scavenging）的相关设置。

### [Get-DnsServerSetting](./Get-DnsServerSetting.md)
检索DNS服务器设置。

### [Get-DnsServerSigningKey](./Get-DnsServerSigningKey.md)
获取区域签名密钥。

### [Get-DnsServerStatistics](./Get-DnsServerStatistics.md)
检索DNS服务器的统计数据或区域的统计数据。

### [Get-DnsServerTrustAnchor](./Get-DnsServerTrustAnchor.md)
在DNS服务器上获取信任锚点（trust anchors）。

### [Get-DnsServerTrustPoint](./Get-DnsServerTrustPoint.md)
在DNS服务器上获得信任点（即增加服务器的可信度）。

### [Get-DnsServerVirtualizationInstance](./Get-DnsServerVirtualizationInstance.md)
获取DNS服务器上的虚拟化实例。

### [Get-DnsServerZone](./Get-DnsServerZone.md)
获取DNS服务器上DNS区域的详细信息。

### [Get-DnsServerZoneAging](./Get-DnsServerZoneAging.md)
获取某个区域的DNS老化设置（即DNS记录更新的时间间隔相关配置）。

### [Get-DnsServerZoneDelegation](./Get-DnsServerZoneDelegation.md)
获取DNS服务器区域的区域委托信息（zone delegations）。

### [Get-DnsServerZoneScope](./Get-DnsServerZoneScope.md)
获取DNS服务器上某个区域的权限范围（scope）。

### [Get-DnsServerZoneTransferPolicy](./Get-DnsServerZoneTransferPolicy.md)
获取DNS服务器上的区域转移策略信息。

### [Import-DnsServerResourceRecordDS](./Import-DnsServerResourceRecordDS.md)
从文件中导入DS资源记录信息。

### [Import-DnsServerRootHint](./Import-DnsServerRootHint.md)
从DNS服务器复制根提示信息。

### [Import-DnsServerTrustAnchor](./Import-DnsServerTrustAnchor.md)
导入用于DNS服务器的信任锚点。

### [Invoke-DnsServerSigningKeyRollover](./Invoke-DnsServerSigningKeyRollover.md)
启动该区域签名密钥的滚动更新（即定期替换或重新生成签名密钥）过程。

### [Invoke-DnsServerZoneSign](./Invoke-DnsServerZoneSign.md)
用于签署DNS服务器区域文件。

### [Invoke-DnsServerZoneUnsign](./Invoke-DnsServerZoneUnsign.md)
取消对DNS服务器区域的签名（即解绑该区域）。

### [Register-DnsServerDirectoryPartition](./Register-DnsServerDirectoryPartition.md)
在DNS应用程序目录分区中注册一台DNS服务器。

### [Remove-DnsServerClientSubnet](./Remove-DnsServerClientSubnet.md)
从DNS服务器中删除某个客户端子网。

### [Remove-DnsServerDirectoryPartition](./Remove-DnsServerDirectoryPartition.md)
删除一个DNS应用程序目录分区。

### [Remove-DnsServerForwarder](./Remove-DnsServerForwarder.md)
从DNS服务器中删除服务器级别的转发器（forwarders）。

### [Remove-DnsServerQueryResolutionPolicy](./Remove-DnsServerQueryResolutionPolicy.md)
从DNS服务器中删除用于查询解析的策略。

### [Remove-DnsServerRecursionScope](./Remove-DnsServerRecursionScope.md)
从DNS服务器中移除一个递归作用域。

### [Remove-DnsServerResourceRecord](./Remove-DnsServerResourceRecord.md)
从某个区域中删除指定的DNS服务器资源记录。

### [Remove-DnsServerResponseRateLimitingExceptionlist](./Remove-DnsServerResponseRateLimitingExceptionlist.md)
从DNS服务器中删除RRL（Reverse Resolution List，反向解析列表）异常列表。

### [Remove-DnsServerRootHint](./Remove-DnsServerRootHint.md)
从DNS服务器中移除根提示信息（即与根域名相关的标识信息）。

### [Remove-DnsServerSigningKey](./Remove-DnsServerSigningKey.md)
删除签名密钥。

### [Remove-DnsServerTrustAnchor](./Remove-DnsServerTrustAnchor.md)
从DNS服务器中删除一个信任锚点（trust anchor）。

### [Remove-DnsServerVirtualizationInstance](./Remove-DnsServerVirtualizationInstance.md)
删除一个虚拟化实例。

### [Remove-DnsServerZone](./Remove-DnsServerZone.md)
从DNS服务器中删除某个区域（zone）。

### [Remove-DnsServerZoneDelegation](./Remove-DnsServerZoneDelegation.md)
从DNS区域中删除名称服务器或委托记录。

### [Remove-DnsServerZoneScope](./Remove-DnsServerZoneScope.md)
从现有的区域中移除某个区域范围（zone scope）。

### [Remove-DnsServerZoneTransferPolicy](./Remove-DnsServerZoneTransferPolicy.md)
从DNS服务器中删除区域传输策略。

### [Reset-DnsServerZoneKeyMasterRole](./Reset-DnsServerZoneKeyMasterRole.md)
转移DNS区域的关键管理角色（Key Master的角色）。

### [Restore-DnsServerPrimaryZone](./Restore-DnsServerPrimaryZone.md)
从 Active Directory 或文件中恢复主 DNS 区域的内容。

### [ Restore-DnsServerSecondaryZone](./Restore-DnsServerSecondaryZone.md)
从源位置恢复次级区域的信息。

### [Resume-DnsServerZone](./Resume-DnsServerZone.md)
在已暂停的区域上恢复名称解析功能。

### [Set-DnsServer](./Set-DnsServer.md)
覆盖DNS服务器配置。

### [Set-DnsServerCache](./Set-DnsServerCache.md)
修改DNS服务器的缓存设置。

### [Set-DnsServerClientSubnet](./Set-DnsServerClientSubnet.md)
更新客户端子网中的IP地址。

### [Set-DnsServerConditionalForwarderZone](./Set-DnsServerConditionalForwarderZone.md)
更改DNS条件转发器的设置。

### [Set-DnsServerDiagnostics](./Set-DnsServerDiagnostics.md)
设置调试和日志记录参数。

### [Set-DnsServerDnsSecZoneSetting](./Set-DnsServerDnsSecZoneSetting.md)
更改某个区域的DNSSEC相关设置。

### [Set-DnsServerDsSetting](./Set-DnsServerDsSetting.md)
修改DNS和Active Directory的设置。

### [Set-DnsServerEDns](./Set-DnsServerEDns.md)
更改DNS服务器上的EDNS设置。

### [Set-DnsServerForwarder](./Set-DnsServerForwarder.md)
在DNS服务器上更改转发器的设置。

### [Set-DnsServerGlobalNameZone](./Set-DnsServerGlobalNameZone.md)
更改 GlobalNames 区域的配置设置。

### [Set-DnsServerGlobalQueryBlockList](./Set-DnsServerGlobalQueryBlockList.md)
更改全局查询块列表的设置。

### [Set-DnsServerPrimaryZone](./Set-DnsServerPrimaryZone.md)
更改DNS主区域的设置。

### [Set-DnsServerQueryResolutionPolicy](./Set-DnsServerQueryResolutionPolicy.md)
更新DNS服务器上查询解析策略的设置。

### [Set-DnsServerRecursion](./Set-DnsServerRecursion.md)
修改DNS服务器的递归设置。

### [Set-DnsServerRecursionScope](./Set-DnsServerRecursionScope.md)
修改DNS服务器上的递归作用域（recursion scope）。

### [Set-DnsServerResourceRecord](./Set-DnsServerResourceRecord.md)
修改DNS区域中的资源记录。

### [Set-DnsServerResourceRecordAging](./Set-DnsServerResourceRecordAging.md)
指定DNS区域中的资源记录开始老化（即逐渐失去有效性）。

### [Set-DnsServerResponseRateLimiting](./Set-DnsServerResponseRateLimiting.md)
在DNS服务器上启用RRL（Real-Time Load Balancing，实时负载均衡）功能。

### [Set-DnsServerResponseRateLimitingExceptionlist](./Set-DnsServerResponseRateLimitingExceptionlist.md)
更新 RRL 异常列表的设置。

### [Set-DnsServerRootHint](./Set-DnsServerRootHint.md)
用于替换一组根提示（root hints）。

### [Set-DnsServerScavenging](./Set-DnsServerScavenging.md)
更改DNS服务器扫描设置。

### [Set-DnsServerSecondaryZone](./Set-DnsServerSecondaryZone.md)
更改DNS备用区域的设置。

### [Set-DnsServerSetting](./Set-DnsServerSetting.md)
修改DNS服务器设置。

### [Set-DnsServerSigningKey](./Set-DnsServerSigningKey.md)
更改签名密钥的设置。

### [Set-DnsServerStubZone](./Set-DnsServerStubZone.md)
修改DNS服务器存根区域的设置。

### [Set-DnsServerVirtualizationInstance](./Set-DnsServerVirtualizationInstance.md)
更新DNS服务器上的虚拟化实例。

### [Set-DnsServerZoneAging](./Set-DnsServerZoneAging.md)
为某个区域配置DNS老化设置（即DNS记录的过期时间相关设置）。

### [Set-DnsServerZoneDelegation](./Set-DnsServerZoneDelegation.md)
更改子区域的委托设置。

### [Set-DnsServerZoneTransferPolicy](./Set-DnsServerZoneTransferPolicy.md)
在DNS服务器上更新区域传输策略。

### [Show-DnsServerCache](./Show-DnsServerCache.md)
显示DNS服务器缓存中的记录。

### [Show-DnsServerKeyStorageProvider](./Show-DnsServerKeyStorageProvider.md)
返回一个关键存储提供商的列表。

### [开始DNS服务器信息收集过程](./Start-DnsServerScavenging.md)
通知DNS服务器尝试查找过期的资源记录。

### [Start-DnsServerZoneTransfer](./Start-DnsServerZoneTransfer.md)
从主服务器开始对辅助DNS区域进行区域传输（zone transfer）操作。

### [Step-DnsServerSigningKeyRollover](./Step-DnsServerSigningKeyRollover.md)
该过程会覆盖一个正在等待父DS更新的KSK（Key Signing Key）。

### [Suspend-DnsServerZone](./Suspend-DnsServerZone.md)
在DNS服务器上暂停某个区域的解析服务。

### [Sync-DnsServerZone](./Sync-DnsServerZone.md)
检查DNS服务器内存中的变化，并将这些变化写入持久存储介质中。

### [Test-DnsServer](./Test-DnsServer.md)
测试指定的计算机是否能够正常运行作为DNS服务器的功能。

### [Test-DnsServerDnsSecZoneSetting](./Test-DnsServerDnsSecZoneSetting.md)
验证某个区域的 DNSSEC 设置是否正确。

### [Unregister-DnsServerDirectoryPartition](./Unregister-DnsServerDirectoryPartition.md)
将DNS服务器从DNS应用程序目录分区中注销（即停止将其注册为可使用的DNS服务器）。

### [Update-DnsServerTrustPoint](./Update-DnsServerTrustPoint.md)
更新DNS信任锚区域中的所有信任点。



