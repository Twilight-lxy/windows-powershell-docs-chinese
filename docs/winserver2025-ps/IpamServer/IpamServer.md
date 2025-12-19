---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.2.1
Locale: en-US
Module Guid: 69775f93-9317-4234-a558-13b6655fc41b
Module Name: IpamServer
ms.date: 12/20/2016
title: IpamServer
---

# IpamServer 模块
## 说明
本参考资料提供了所有与 IP 地址管理（IPAM）服务器相关的 cmdlet 的描述和语法信息。这些 cmdlet 按其开头所使用的动词（即命令操作）的字母顺序进行排列。

## IpamServer Cmdlets
### [Add-IpamAddress](./Add-IpamAddress.md)
将一个 IP 地址添加到 IPAM（IP 地址管理）系统中。

### [Add-IpamAddressSpace](./Add-IpamAddressSpace.md)
向 IPAM（IP Address Management）系统中添加一个地址空间。

### [Add-IpamBlock](./Add-IpamBlock.md)
将一个IP地址段添加到IPAM中。

### [Add-IpamCustomField](./Add-IpamCustomField.md)
向 IPAM 添加一个自由格式或多值的自定义字段。

### [Add-IpamCustomFieldAssociation](./Add-IpamCustomFieldAssociation.md)
在IPAM中定义的自定义字段的值之间建立关联关系。

### [Add-IpamCustomValue](./Add-IpamCustomValue.md)
向 IPAM 中的自定义字段添加一个值。

### [Add-IpamDiscoveryDomain](./Add-IpamDiscoveryDomain.md)
向用于识别IPAM基础设施服务器的域列表中添加一个新的Active Directory域。

### [Add-IpamRange](./Add-IpamRange.md)
将一个 IP 地址范围添加到 IPAM 服务器的配置中。

### [Add-IpamServerInventory](./Add-IpamServerInventory.md)
将一台基础设施服务器添加到 IPAM 数据库中。

### [Add-IpamSubnet](./Add-IpamSubnet.md)
向 IPAM（IP 地址管理）中添加一个子网。

### [禁用 Ipam 功能](./Disable-Ipam Capability.md)
禁用 IPAM 中的一项可选功能。

### [Enable-IpamCapability](./Enable-IpamCapability.md)
启用 IPAM 服务器上的一项可选功能。

### [Export-IpamAddress](./Export-IpamAddress.md)
从 IPAM 中导出 IP 地址。

### [Export-IpamRange](./Export-IpamRange.md)
将所有 IP 地址范围导出为一个文件、一个对象数组，或者同时以这两种形式进行导出。

### [Export-IpamSubnet](./Export-IpamSubnet.md)
在运行 IPAM 的计算机上，导出该地址家族中的 IP 地址子网信息。

### [Find-IpamFreeAddress](./Find-IpamFreeAddress.md)
从 IPAM 中的某个 IP 地址范围内获取一个或多个免费的 IP 地址。

### [Find-IpamFreeRange](./Find-IpamFreeRange.md)
从指定的子网中查找一个或多个可用的 IP 地址范围。

### [Find-IpamFreeSubnet](./Find-IpamFreeSubnet.md)
在指定的IP地址段中查找一个或多个空闲的IP子网。

### [Get-IpamAddress](./Get-IpamAddress.md)
从 IPAM 获取 IP 地址。

### [Get-IpamAddressSpace](./Get-IpamAddressSpace.md)
获取IPAM中的地址空间信息。

### [Get-IpamAddressUtilizationThreshold](./Get-IpamAddressUtilizationThreshold.md)
获取地址使用率警报的阈值配置信息。

### [Get-IpamBlock](./Get-IpamBlock.md)
从 IPAM 获取一组地址块。

### [Get-Ipam Capability](./Get-IpamCapability.md)
获取 IPAM 中的所有可选功能。

### [Get-IpamConfiguration](./Get-IpamConfiguration.md)
获取运行 IPAM 的计算机的配置信息。

### [Get-IpamConfigurationEvent](./Get-IpamConfigurationEvent.md)
从 IPAM 数据库中获取 IPAM 配置事件。

### [Get-IpamCustomField](./Get-IpamCustomField.md)
从 IPAM 中获取自定义字段信息。

### [Get-IpamCustomFieldAssociation](./Get-IpamCustomFieldAssociation.md)
获取在 IPAM 中定义的两个自定义字段之间的关联关系。

### [Get-IpamDatabase](./Get-IpamDatabase.md)
获取IPAM数据库的配置设置。

### [Get-IpamDhcpConfigurationEvent](./Get-IpamDhcpConfigurationEvent.md)
从 IPAM 数据库中获取 DHCP 服务器的配置事件信息。

### [Get-IpamDhcpScope](./Get-IpamDhcpScope.md)
从 IPAM 数据库中获取有关 DHCP 范围的信息。

### [Get-IpamDhcpServer](./Get-IpamDhcpServer.md)
从IPAM数据库中获取有关DHCP服务器的信息。

### [Get-IpamDhcpSuperscope](./Get-IpamDhcpSuperscope.md)
从 IPAM 数据库中获取有关 DHCP 超范围（superscope）的信息。

### [Get-IpamDiscoveryDomain](./Get-IpamDiscoveryDomain.md)
获取 Active Directory 域的列表，在这些域中，IPAM 可以发现基础设施服务器。

### [Get-IpamDnsConditionalForwarder](./Get-IpamDnsConditionalForwarder.md)
从 IPAM 数据库中获取有关 DNS 条件转发器的信息。

### [Get-IpamDnsResourceRecord](./Get-IpamDnsResourceRecord.md)
从 IPAM 数据库中获取 DNS 资源记录。

### [Get-IpamDnsServer](./Get-IpamDnsServer.md)
从 IPAM 数据库中获取有关 DNS 服务器的信息。

### [Get-IpamDnsZone](./Get-IpamDnsZone.md)
从 IPAM 数据库中获取有关 DNS 区域的信息。

### [Get-IpamIpAddressAuditEvent](./Get-IpamIpAddressAuditEvent.md)
获取 IPAM 中的所有 IP 地址审计事件。

### [Get-IpamRange](./Get-IpamRange.md)
从 IPAM 服务器获取一组 IP 地址范围。

### [Get-IpamServerInventory](./Get-IpamServerInventory.md)
获取IPAM服务器库存中托管服务器的属性信息。

### [Get-IpamSubnet](./Get-IpamSubnet.md)
从 IPAM 中获取一组子网。

### [Import-IpamAddress](./Import-IpamAddress.md)
将IP地址导入到IPAM服务器中。

### [Import-IpamRange](./Import-IpamRange.md)
从指定的文件中导入一个或多个IP地址范围对象到IPAM服务器中。

### [Import-IpamSubnet](./Import-IpamSubnet.md)
从指定的文件中导入IP地址子网对象到IPAM系统中。

### [Invoke-IpamGpoProvisioning](./Invoke-IpamGpoProvisioning.md)
在指定的域中创建并链接组策略，以便为运行IPAM服务器的计算机管理的服务器提供所需的访问设置。

### [Invoke-IpamServerProvisioning](./Invoke-IpamServerProvisioning.md)
自动化IPAM服务器的配置过程。

### [Move-IpamDatabase](./Move-IpamDatabase.md)
将 IPAM 数据库迁移到 SQL Server 数据库中。

### [Remove-IpamAddress](./Remove-IpamAddress.md)
从 IPAM 中删除一组地址。

### [Remove-IpamAddressSpace](./Remove-IpamAddressSpace.md)
从 IPAM 中删除地址空格。

### [Remove-IpamBlock](./Remove-IpamBlock.md)
从 IPAM 中删除一个地址块。

### [Remove-IpamConfigurationEvent](./Remove-IpamConfigurationEvent.md)
删除 IPAM 服务器配置事件。

### [Remove-IpamCustomField](./Remove-IpamCustomField.md)
从 IPAM 中删除一个自定义字段。

### [Remove-IpamCustomFieldAssociation](./Remove-IpamCustomFieldAssociation.md)
删除在 IPAM 中定义的两个自定义字段之间的关联关系。

### [Remove-IpamCustomValue](./Remove-IpamCustomValue.md)
从 IPAM 中删除自定义值。

### [Remove-IpamDhcpConfigurationEvent](./Remove-IpamDhcpConfigurationEvent.md)
从 IPAM 数据库中删除与 DHCP 服务器相关的配置事件。

### [Remove-IpamDiscoveryDomain](./Remove-IpamDiscoveryDomain.md)
从 IPAM 中删除一个域名。

### [Remove-IpamIpAddressAuditEvent](./Remove-IpamIpAddressAuditEvent.md)
从 IPAM 数据库中删除与 IP 地址相关的审计事件记录。

### [Remove-IpamRange](./Remove-IpamRange.md)
从 IPAM 服务器配置中删除一系列 IP 地址。

### [Remove-IpamServerInventory](./Remove-IpamServerInventory.md)
从 IPAM 服务器清单中删除一台服务器。

### [Remove-IpamSubnet](./Remove-IpamSubnet.md)
从 IPAM 中删除一个子网。

### [Remove-IpamUtilizationData](./Remove-IpamUtilizationData.md)


### [Rename-IpamCustomField](./Rename-IpamCustomField.md)
在 IPAM 中重命名一个自定义字段。

### [Rename-IpamCustomValue](./Rename-IpamCustomValue.md)
更改自定义字段的值。

### [Set-IpamAccessScope](./Set-IpamAccessScope.md)
配置 IPAM 访问范围。

### [Set-IpamAddress](./Set-IpamAddress.md)
在IPAM中修改一个IP地址。

### [Set-IpamAddressSpace](./Set-IpamAddressSpace.md)
修改 IPAM 中的地址空间。

### [Set-IpamAddressUtilizationThreshold](./Set-IpamAddressUtilizationThreshold.md)
修改IPAM中的地址利用率阈值。

### [Set-IpamBlock](./Set-IpamBlock.md)
修改 IPAM 中的 IP 地址段。

### [Set-IpamConfiguration](./Set-IpamConfiguration.md)
修改运行 IPAM 服务器的计算机的配置。

### [Set-IpamCustomFieldAssociation](./Set-IpamCustomFieldAssociation.md)
修改在 IPAM 中定义的自定义字段的值之间的关联关系。

### [Set-IpamDatabase](./Set-IpamDatabase.md)
修改 IPAM 用于连接 IPAM 数据库的设置。

### [Set-IpamDiscoveryDomain](./Set-IpamDiscoveryDomain.md)
修改 IPAM 发现配置。

### [Set-IpamRange](./Set-IpamRange.md)
修改现有的 IP 地址范围。

### [Set-IpamServerInventory](./Set-IpamServerInventory.md)
修改IPAM服务器库存中某台基础设施服务器的属性。

### [Set-IpamSubnet](./Set-IpamSubnet.md)
在IPAM中修改现有的IP子网。

### [更新 IpamServer](./Update-IpamServer.md)
在操作系统升级后，更新IPAM服务器的相关配置。


