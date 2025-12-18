---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.0.1
Locale: en-US
Module Guid: 90eaa9df-133a-450c-8728-91055cd946a1
Module Name: DhcpServer
ms.date: 12/20/2016
title: DhcpServer
---

# DhcpServer 模块
## 描述
本参考资料提供了所有与动态主机配置协议（DHCP）服务器服务相关的cmdlet的描述和语法信息。这些cmdlet按照每个cmdlet开头所使用的动词（即命令操作关键字）的字母顺序进行排列。

另请参阅[DHCP类别](https://go.microsoft.com/FWLink/p/?LinkId=260590)。


## DhcpServerCmdlets
### [Add-DhcpServerInDC](./Add-DhcpServerInDC.md)
将运行DHCP服务器服务的计算机添加到Active Directory中授权的DHCP服务器服务列表中。

### [Add-DhcpServerSecurityGroup](./Add-DhcpServerSecurityGroup.md)
将安全组添加到DHCP服务器中。

### [Add-DhcpServerv4Class](./Add-DhcpServerv4Class.md)
向DHCP服务器服务添加一个IPv4供应商或用户类别。

### [Add-DhcpServerv4ExclusionRange](./Add-DhcpServerv4ExclusionRange.md)
为某个 IPv4 范围添加一系列需要排除的 IP 地址。

### [Add-DhcpServerv4Failover](./Add-DhcpServerv4Failover.md)
在DHCP服务器服务上添加一个IPv4故障转移关系。

### [Add-DhcpServerv4FailoverScope](./Add-DhcpServerv4FailoverScope.md)
将一个或多个指定的作用域添加到故障转移关系中。

### [Add-DhcpServerv4Filter](./Add-DhcpServerv4Filter.md)
向DHCP服务器服务添加一个MAC地址过滤器。

### [Add-DhcpServerv4Lease](./Add-DhcpServerv4Lease.md)
在DHCP服务器服务中添加一个新的IPv4地址租约。

### [Add-DhcpServerv4MulticastExclusionRange](./Add-DhcpServerv4MulticastExclusionRange.md)
添加一系列地址，以将这些地址从多播范围内排除掉。

### [Add-DhcpServerv4MulticastScope](./Add-DhcpServerv4MulticastScope.md)
在DHCP服务器上添加一个多播作用域（multicast scope）。

### [Add-DhcpServerv4OptionDefinition](./Add-DhcpServerv4OptionDefinition.md)
在DHCP服务器服务上添加一个DHCPv4选项定义。

### [Add-DhcpServerv4Policy](./Add-DhcpServerv4Policy.md)
在服务器级别或作用域级别添加新的策略。

### [Add-DhcpServerv4PolicyIPRange](./Add-DhcpServerv4PolicyIPRange.md)
在范围级别（scope level）将一个IP地址段添加到现有的策略中。

### [Add-DhcpServerv4Reservation](./Add-DhcpServerv4Reservation.md)
为客户在指定的地址范围内预留一个IPv4地址。

### [Add-DhcpServerv4Scope](./Add-DhcpServerv4Scope.md)
在DHCP服务器服务上添加一个IPv4地址范围。

### [Add-DhcpServerv4Superscope](./Add-DhcpServerv4Superscope.md)
向一个超范围（superscope）添加作用域（scopes）。

### [Add-DhcpServerv6Class](./Add-DhcpServerv6Class.md)
向DHCP服务器服务添加一个IPv6供应商或用户类别。

### [Add-DhcpServerv6ExclusionRange](./Add-DhcpServerv6ExclusionRange.md)
用于指定要从某个 IPv6 范围中排除的 IPv6 地址范围。

### [Add-DhcpServerv6Lease](./Add-DhcpServerv6Lease.md)
向DHCP服务器服务添加一个IPv6地址租约。

### [Add-DhcpServerv6OptionDefinition](./Add-DhcpServerv6OptionDefinition.md)
向DHCP服务器服务添加一个DHCPv6选项定义。

### [Add-DhcpServerv6Reservation](./Add-DhcpServerv6 Reservation.md)
将一个 IPv6 预留地址添加到某个 IPv6 前缀或作用域中。

### [Add-DhcpServerv6Scope](./Add-DhcpServerv6Scope.md)
使用指定的参数为DHCP服务器服务添加一个IPv6作用域。

### [备份DHCP服务器](./Backup-DhcpServer.md)
备份DHCP服务器服务的DHCP数据库。

### [Export-DhcpServer](./Export-DhcpServer.md)
导出DHCP服务器的服务配置和租约数据。

### [Get-DhcpServerAuditLog](./Get-DhcpServerAuditLog.md)
获取与DHCP服务器服务的审计日志相关的配置参数。

### [Get-DhcpServerDatabase](./Get-DhcpServerDatabase.md)
获取与DHCP服务器服务的数据库相关的配置参数。

### [Get-DhcpServerDnsCredential](./Get-DhcpServerDnsCredential.md)
获取一个DHCP服务器服务用于在DNS服务器上注册或注销客户端记录的账户。

### [Get-DhcpServerInDC](./Get-DhcpServerInDC.md)
从 Active Directory 中检索运行 DHCP 服务器服务的授权计算机的列表。

### [Get-DhcpServerSetting](./Get-DhcpServerSetting.md)
获取DHCP服务器服务数据库的配置参数。

### [Get-DhcpServerv4Binding](./Get-DhcpServerv4Binding.md)
获取DHCP服务器服务所绑定的计算机上的IPv4接口信息。

### [Get-DhcpServerv4Class](./Get-DhcpServerv4Class.md)
从DHCP服务器服务中检索IPv4供应商或用户类别信息。

### [Get-DhcpServerv4DnsSetting](./Get-DhcpServerv4DnsSetting.md)
用于获取在DHCP服务器服务中为特定作用域、预留地址或服务器级别配置的DNS设置。

### [Get-DhcpServerv4ExclusionRange](./Get-DhcpServerv4ExclusionRange.md)
返回从指定范围ID中排除的IPv4地址段。

### [Get-DhcpServerv4Failover](./Get-DhcpServerv4Failover.md)
获取在DHCP服务器服务上为特定故障转移关系名称配置的故障转移关系信息。

### [Get-DhcpServerv4Filter](./Get-DhcpServerv4Filter.md)
从DHCP服务器服务的允许列表或拒绝列表中获取MAC地址。

### [Get-DhcpServerv4FilterList](./Get-DhcpServerv4FilterList.md)
获取DHCP服务器服务上设置的“允许过滤列表”（allow filter list）和“拒绝过滤列表”（deny filter list）的启用状态。

### [Get-DhcpServerv4FreeIPAddress](./Get-DhcpServerv4FreeIPAddress.md)
从一个指定的范围内获取免费的IPv4地址。

### [Get-DhcpServerv4Lease](./Get-DhcpServerv4Lease.md)
从DHCP服务器服务中获取一个或多个租约记录。

### [Get-DhcpServerv4MulticastExclusionRange](./Get-DhcpServerv4MulticastExclusionRange.md)
获取指定多播范围的排除范围（即不允许使用的地址范围）。

### [Get-DhcpServerv4MulticastLease](./Get-DhcpServerv4MulticastLease.md)
检索指定作用域名称的多播租约信息。

### [Get-DhcpServerv4MulticastScope](./Get-DhcpServerv4MulticastScope.md)
获取多播作用域对象（multicast scope objects）。

### [Get-DhcpServerv4MulticastScopeStatistics](./Get-DhcpServerv4MulticastScopeStatistics.md)
获取组播范围统计信息。

### [Get-DhcpServerv4OptionDefinition](./Get-DhcpServerv4OptionDefinition.md)
获取指定选项ID对应的DHCPv4选项定义。

### [Get-DhcpServerv4OptionValue](./Get-DhcpServerv4OptionValue.md)
返回服务器、作用域或预留级别上与 IPv4 选项相关的值。

### [Get-DhcpServerv4Policy](./Get-DhcpServerv4Policy.md)
可以在服务器级别或作用域级别获取策略。

### [Get-DhcpServerv4PolicyIPRange](./Get-DhcpServerv4PolicyIPRange.md)
从指定范围内的策略中获取 IP 地址范围。

### [Get-DhcpServerv4Reservation](./Get-DhcpServerv4 Reservation.md)
用于获取IPv4地址或客户端ID的预留资源。

### [Get-DhcpServerv4Scope](./Get-DhcpServerv4Scope.md)
返回指定范围的IPv4地址范围配置信息。

### [Get-DhcpServerv4ScopeStatistics](./Get-DhcpServerv4ScopeStatistics.md)
获取与为DHCP服务器服务指定的IPv4范围ID相对应的IPv4范围统计信息。

### [Get-DhcpServerv4Statistics](./Get-DhcpServerv4Statistics.md)
获取IPv4地址对应的DHCP服务器服务统计信息。

### [Get-DhcpServerv4Superscope](./Get-DhcpServerv4Superscope.md)
获取指定超范围的配置信息。

### [Get-DhcpServerv4SuperscopeStatistics](./Get-DhcpServerv4SuperscopeStatistics.md)
返回关于超范围（superscopes）的统计信息。

### [Get-DhcpServerv6Binding](./Get-DhcpServerv6Binding.md)
返回DHCP服务器服务所绑定的IPv6接口。

### [Get-DhcpServerv6Class](./Get-DhcpServerv6Class.md)
从DHCP服务器服务中获取IPv6供应商或用户类别信息。

### [Get-DhcpServerv6DnsSetting](./Get-DhcpServerv6DnsSetting.md)
用于获取在DHCP服务器服务上为特定范围、预订项配置的DNS设置，或者全局适用的DNS设置。

### [Get-DhcpServerv6ExclusionRange](./Get-DhcpServerv6ExclusionRange.md)
获取从指定的 IPv6 子网前缀中排除的 IPv6 地址范围。

### [Get-DhcpServerv6FreeIPAddress](./Get-DhcpServerv6FreeIPAddress.md)
从一个地址范围内获取免费的IPv6地址。

### [Get-DhcpServerv6Lease](./Get-DhcpServerv6Lease.md)
从DHCP服务器服务中获取IPv6租赁记录。

### [Get-DhcpServerv6OptionDefinition](./Get-DhcpServerv6OptionDefinition.md)
获取由选项ID标识的选项的定义信息。

### [Get-DhcpServerv6OptionValue](./Get-DhcpServerv6OptionValue.md)
返回一个或多个IPv6选项的值，这些值可以针对特定的保留IP地址、作用域或服务器级别进行查询。

### [Get-DhcpServerv6Reservation](./Get-DhcpServerv6Reservation.md)
返回DHCP服务器服务中预留的IPv6地址。

### [Get-DhcpServerv6Scope](./Get-DhcpServerv6Scope.md)
从DHCP服务器服务中获取指定IPv6前缀的相关范围信息。

### [Get-DhcpServerv6ScopeStatistics](./Get-DhcpServerv6ScopeStatistics.md)
获取为 DHCP 服务器服务指定的 IPv6 前缀的统计信息。

### [Get-DhcpServerv6StatelessStatistics](./Get-DhcpServerv6StatelessStatistics.md)
获取包含无状态客户端（stateless clients）的 IPv6 子网前缀，以及每个子网中正在使用的地址数量。

### [Get-DhcpServerv6StatelessStore](./Get-DhcpServerv6StatelessStore.md)
获取指定IPv6子网的IPv6无状态存储（stateless storage）的相关属性。

### [Get-DhcpServerv6Statistics](./Get-DhcpServerv6Statistics.md)
获取IPv6的DHCP服务器服务统计数据。

### [Get-DhcpServerVersion](./Get-DhcpServerVersion.md)
获取DHCP服务器服务的版本信息。

### [Import-DhcpServer](./Import-DhcpServer.md)
从文件中导入DHCP服务器服务配置信息（以及可选的租约数据）。

### [Invoke-DhcpServerv4FailoverReplication](./Invoke-DhcpServerv4FailoverReplication.md)
在故障转移伙伴DHCP服务器服务之间复制作用域配置。

### [Remove-DhcpServerDnsCredential](./Remove-DhcpServerDnsCredential.md)
删除DHCP服务器服务用于在DNS服务器上注册或注销客户端记录的凭据。

### [Remove-DhcpServerInDC](./Remove-DhcpServerInDC.md)
从 Active Directory 中授权的 DHCP 服务器服务列表中删除指定的 DHCP 服务器服务。

### [Remove-DhcpServerv4Class](./Remove-DhcpServerv4Class.md)
从DHCP服务器服务中删除IPv4供应商类别或用户类别。

### [Remove-DhcpServerv4ExclusionRange](./Remove-DhcpServerv4ExclusionRange.md)
删除之前被排除在某个IPv4地址范围之外的那些IPv4地址。

### [Remove-DhcpServerv4Failover](./Remove-DhcpServerv4Failover.md)
删除故障转移关系。

### [Remove-DhcpServerv4FailoverScope](./Remove-DhcpServerv4FailoverScope.md)
从故障转移关系中移除指定的作用域。

### [Remove-DhcpServerv4Filter](./Remove-DhcpServerv4Filter.md)
从DHCP服务器服务的允许列表或拒绝列表中删除某个MAC地址或MAC地址模式。

### [Remove-DhcpServerv4Lease](./Remove-DhcpServerv4Lease.md)
从DHCP服务器服务中删除IPv4地址租用记录。

### [Remove-DhcpServerv4MulticastExclusionRange](./Remove-DhcpServerv4MulticastExclusionRange.md)
将之前被排除在多播范围之外的地址重新添加到该范围内。

### [Remove-DhcpServerv4MulticastLease](./Remove-DhcpServerv4MulticastLease.md)
删除某个多播范围或多播地址的多播范围租约。

### [Remove-DhcpServerv4MulticastScope](./Remove-DhcpServerv4MulticastScope.md)
移除多播范围（multicast scopes）。

### [Remove-DhcpServerv4OptionDefinition](./Remove-DhcpServerv4OptionDefinition.md)
从DHCP服务器服务中删除IPv4选项定义。

### [Remove-DhcpServerv4OptionValue](./Remove-DhcpServerv4OptionValue.md)
在服务器、作用域或预留级别删除一个或多个 IPv4 选项值，这些选项值既可以是标准的 IPv4 选项，也可以是特定供应商或用户类别的选项。

### [Remove-DhcpServerv4Policy](./Remove-DhcpServerv4Policy.md)
在服务器级别或作用域级别删除IPv4策略。

### [Remove-DhcpServerv4PolicyIPRange](./Remove-DhcpServerv4PolicyIPRange.md)
从现有策略中删除某个 IP 范围（操作在范围级别进行）。

### [Remove-DhcpServerv4Reservation](./Remove-DhcpServerv4 Reservation.md)
从指定的范围内删除该IPv4预留地址。

### [Remove-DhcpServerv4Scope](./Remove-DhcpServerv4Scope.md)
从DHCP服务器服务中删除指定的IPv4地址范围。

### [Remove-DhcpServerv4Superscope](./Remove-DhcpServerv4Superscope.md)
从父作用域中移除子作用域。

### [Remove-DhcpServerv6Class](./Remove-DhcpServerv6Class.md)
从DHCP服务器服务中删除指定的IPv6供应商类别或用户类别。

### [Remove-DhcpServerv6ExclusionRange](./Remove-DhcpServerv6ExclusionRange.md)
删除之前从某个 IPv6 范围中被排除在外的一系列 IPv6 地址。

### [Remove-DhcpServerv6Lease](./Remove-DhcpServerv6Lease.md)
从DHCP服务器服务中删除IPv6租约记录。

### [Remove-DhcpServerv6OptionDefinition](./Remove-DhcpServerv6OptionDefinition.md)
从DHCP服务器服务中删除IPv6选项的定义。

### [Remove-DhcpServerv6OptionValue](./Remove-DhcpServerv6OptionValue.md)
删除在保留级别、作用域级别或服务器级别设置的 DHCPv6 选项值，这些选项值适用于标准的 IPv6 选项或特定供应商的类别。

### [Remove-DhcpServerv6Reservation](./Remove-DhcpServerv6Reservation.md)
从指定的范围内删除IPv6预留地址。

### [Remove-DhcpServerv6Scope](./Remove-DhcpServerv6Scope.md)
从DHCP服务器服务中删除与指定前缀对应的IPv6地址范围。

### [Rename-DhcpServerv4Superscope](./Rename-DhcpServerv4Superscope.md)
重命名一个超范围（superscope）。

### [Repair-DhcpServerv4IPRecord](./Repair-DhcpServerv4IPRecord.md)
协调DHCP数据库中不一致的租赁记录。

### [Restore-DhcpServer](./Restore-DhcpServer.md)
从指定位置恢复DHCP服务器服务的数据库。

### [Set-DhcpServerAuditLog](./Set-DhcpServerAuditLog.md)
在计算机上运行的DHCP服务器服务上，设置DHCP服务器服务的审计日志配置。

### [Set-DhcpServerDatabase](./Set-DhcpServerDatabase.md)
修改DHCP服务器服务的数据库中的一个或多个配置参数。

### [Set-DhcpServerDnsCredential](./Set-DhcpServerDnsCredential.md)
设置DHCP服务器服务用于在DNS服务器上注册或注销客户端记录的凭据。

### [Set-DhcpServerSetting](./Set-DhcpServerSetting.md)
设置DHCP服务器服务的服务器级配置参数。

### [Set-DhcpServerv4Binding](./Set-DhcpServerv4Binding.md)
用于设置计算机上运行的DHCP服务器服务的IPv4接口的绑定状态。

### [Set-DhcpServerv4Class](./Set-DhcpServerv4Class.md)
使用指定的参数，在DHCP服务器服务上修改IPv4供应商类别或用户类别。

### [Set-DhcpServerv4DnsSetting](./Set-DhcpServerv4DnsSetting.md)
配置DHCP服务器服务如何将与客户端相关的信息更新到DNS服务器上。

### [Set-DhcpServerv4Failover](./Set-DhcpServerv4Failover.md)
修改现有故障转移关系的属性。

### [Set-DhcpServerv4FilterList](./Set-DhcpServerv4FilterList.md)
设置DHCP服务器服务上“允许”和“拒绝”MAC地址过滤列表的启用状态。

### [Set-DhcpServerv4MulticastScope](./Set-DhcpServerv4MulticastScope.md)
修改多播作用域的属性。

### [Set-DhcpServerv4OptionDefinition](./Set-DhcpServerv4OptionDefinition.md)
修改 IPv4 选项定义的属性。

### [Set-DhcpServerv4OptionValue](./Set-DhcpServerv4OptionValue.md)
在服务器、范围或预留级别设置一个IPv4选项的值。

### [Set-DhcpServerv4Policy](./Set-DhcpServerv4Policy.md)
在服务器级别或指定的范围级别设置策略的属性。

### [Set-DhcpServerv4Reservation](./Set-DhcpServerv4 Reservation.md)
修改IPv4预留资源的属性。

### [Set-DhcpServerv4Scope](./Set-DhcpServerv4Scope.md)
用于在DHCP服务器服务上设置现有IPv4地址段的属性。

### [Set-DhcpServerv6Binding](./Set-DhcpServerv6Binding.md)
设置DHCP服务器服务中IPv6接口的绑定状态。

### [Set-DhcpServerv6Class](./Set-DhcpServerv6Class.md)
在DHCP服务器服务上修改IPv6供应商或用户类别的属性。

### [Set-DhcpServerv6DnsSetting](./Set-DhcpServerv6DnsSetting.md)
配置DHCP服务器服务如何将与客户端相关的信息更新到DNS服务器上。

### [Set-DhcpServerv6OptionDefinition](./Set-DhcpServerv6OptionDefinition.md)
修改 DHCPv6 选项定义的属性。

### [Set-DhcpServerv6OptionValue](./Set-DhcpServerv6OptionValue.md)
在服务器、范围或预留级别设置一个IPv6选项的值。

### [Set-DhcpServerv6Reservation](./Set-DhcpServerv6Reservation.md)
修改指定的IPv6预留资源的属性。

### [Set-DhcpServerv6Scope](./Set-DhcpServerv6Scope.md)
修改DHCP服务器服务中IPv6作用域的属性。

### [Set-DhcpServerv6StatelessStore](./Set-DhcpServerv6StatelessStore.md)
为某个 IPv6 前缀设置 IPv6 无状态存储（stateless store）的相关属性。


