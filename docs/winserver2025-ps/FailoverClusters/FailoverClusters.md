---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.3.3
Locale: en-US
Module Guid: cc3e946b-9141-48c2-95d8-d9e56594416a
Module Name: FailoverClusters
ms.date: 01/22/2025
title: FailoverClusters
---

# FailoverClusters 模块

## 说明

本参考资料提供了所有与故障转移集群相关的 cmdlet 的描述和语法。这些 cmdlet 按其开头命令动词的字母顺序进行排列。如果你的 PowerShell 会话中没有这些 cmdlet，你可能需要使用以下 PowerShell 命令来添加 “Failover Cluster Module for Windows PowerShell” 功能：

```powershell
Add-WindowsFeature RSAT-Clustering-PowerShell
```

> [!NOTE]
> The AccelNet cmdlets have a dependency on the Hyper-V role. To learn more, see
> [Install or Uninstall Roles, Role Services, or Features](/windows-server/administration/server-manager/install-or-uninstall-roles-role-services-or-features).
>
> This role can also be installed using PowerShell by running the following command:
>
> ```powershell
> Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
> ```

## FailoverClustersCmdlets

### [添加集群检查点](Add-ClusterCheckpoint.md)

为某个资源添加一个加密密钥检查点或注册表检查点。

### [Add-ClusterDisk](Add-ClusterDisk.md)

为故障转移集群创建一个可用的新磁盘。

### [Add-ClusterExcludedAdapter](Add-ClusterExcludedAdapter.md)

将一个网络适配器添加到被排除的适配器列表中。

### [Add-ClusterFileServerRole](Add-ClusterFileServerRole.md)

创建一个集群文件服务器资源组。

### [添加集群通用应用程序角色](Add-ClusterGenericApplicationRole.md)

为原本并未设计用于在故障转移集群中运行的应用程序配置高可用性。

### [Add-ClusterGenericScriptRole](Add-ClusterGenericScriptRole.md)

配置一个由脚本控制的应用程序，该脚本在 Windows 脚本宿主（Windows Script Host）中运行，并且属于一个故障转移集群（failover cluster）的一部分。

### [Add-ClusterGenericServiceRole](Add-ClusterGenericServiceRole.md)

为一项最初并未被设计为在故障转移集群中运行的服务配置高可用性。

### [添加集群组](Add-ClusterGroup.md)

向故障转移集群配置中添加一个空的资源组，为后续向该组中添加集群化资源做准备。

### [Add-ClusterGroupSetDependency](Add-ClusterGroupSetDependency.md)

向集群集添加一个依赖项。

### [将集群组添加到亲和性规则中](Add-ClusterGroupToAffinityRule.md)

将一个集群组添加到亲和规则中。

### [将集群组添加到集合中](Add-ClusterGroupToSet.md)

将一个组添加到集合中。

### [Add-ClusteriSCSITargetServerRole](Add-ClusteriSCSITargetServerRole.md)

创建一个高可用性的 iSCSI 目标服务器。

### [添加集群节点](Add-ClusterNode.md)

向故障转移集群中添加一个节点（服务器）。

### [Add-ClusterResource](Add-ClusterResource.md)

将资源添加到故障转移集群中的集群角色或资源组中。

### [添加集群资源依赖关系](Add-ClusterResourceDependency.md)

在故障转移集群中，将一个资源添加到另一个特定资源所依赖的资源列表中，使用“AND”作为连接符。

### [Add-ClusterResourceType](Add-ClusterResourceType.md)

向故障转移集群添加一种资源类型，并指定与该资源类型相关联的信息（例如要使用的动态链接库（DLL））。

### [Add-ClusterScaleOutFileServerRole](Add-ClusterScaleOutFileServerRole.md)

创建一个集群化的文件服务器，用于扩展应用程序数据存储容量。

### [Add-ClusterSharedVolume](Add-ClusterSharedVolume.md)

在故障转移集群中，将某个卷设置为可用状态，并将其添加到集群共享卷（Cluster Shared Volumes）中。

### [将集群共享卷添加到亲和性规则中](Add-ClusterSharedVolumeToAffinityRule.md)

将一个集群共享卷（Cluster Shared Volume，简称 CSV）添加到现有的亲和性规则中。

### [添加集群虚拟机角色](Add-ClusterVirtualMachineRole.md)

创建一个集群化的虚拟机，即这种虚拟机在需要时可以切换到故障转移集群中的另一台服务器上继续运行。

### [Add-ClusterVMMonitoredItem](Add-ClusterVMMonitoredItem.md)

配置对某个服务的监控机制，或者针对 Windows 事件跟踪（Event Tracing, ETW）事件的监控设置，以便在虚拟机上对这些服务或事件进行监控。

### [Add-WorkgroupClusterNode](Add-WorkgroupClusterNode.md)

向工作组集群中添加一个节点。

### [Block-ClusterAccess](Block-ClusterAccess.md)

阻止指定的用户访问故障转移集群。

### [Clear-ClusterDiskReservation](Clear-ClusterDiskReservation.md)

清除故障转移集群中磁盘上的永久性保留信息（即那些不会被自动删除的数据）。

### [Clear-ClusterNode](Clear-ClusterNode.md)

从被从故障转移集群中移除的节点清除集群配置信息。

### [ Disable-AccelNetManagement](Disable-AccelNetManagement.md)

在集群范围内禁用加速网络管理功能。

### [禁用AccelNetVM](Disable-AccelNetVM.md)

禁用虚拟机上的加速网络功能（Accelerated Networking）。

### [禁用-ClusterStorageSpacesDirect]( Disable-ClusterStorageSpacesDirect.md)

禁用S2D功能。

### [Enable-AccelNetManagement](Enable-AccelNetManagement.md)

在整个集群范围内启用加速网络管理功能。

### [Enable-AccelNetVM](Enable-AccelNetVM.md)

在虚拟机上启用加速网络功能。

### [Enable-ClusterStorageSpacesDirect](Enable-ClusterStorageSpacesDirect.md)

在故障转移集群上启用“Storage Spaces Direct”功能。

### [Get-AccelNetManagement](Get-AccelNetManagement.md)

启用加速网络管理（Accelerated Networking Management）相关的功能/设置。

### [Get-AccelNetManagementPreReq](Get-AccelNetManagementPreReq.md)

向用户提示集群节点是否支持加速网络（Accelerated Networking）功能。

### [Get-AccelNetVM](Get-AccelNetVM.md)

获取配备了加速网络功能的虚拟机（VMs）。

### [Get-Cluster](Get-Cluster.md)

获取关于给定域中的一个或多个故障转移集群的信息。

### [Get-ClusterAccess](Get-ClusterAccess.md)

获取有关控制对故障转移集群访问权限的信息。

### [Get-ClusterAffinityRule](Get-ClusterAffinityRule.md)

此cmdlet用于显示给定的规则及其类型。

### [Get-ClusterAvailableDisk](Get-ClusterAvailableDisk.md)

获取有关可以支持故障转移集群（Failover Clustering）的磁盘的信息，这些磁盘对所有节点都是可见的，但尚未成为集群磁盘集的一部分。

### [Get-ClusterCheckpoint](Get-ClusterCheckpoint.md)

检索资源的加密密钥检查点或注册表检查点。

### [Get-ClusterCredential](Get-ClusterCredential.md)

检索故障转移集群中指定节点的凭据信息。

### [Get-ClusterDiagnosticInfo](Get-ClusterDiagnosticInfo.md)

获取包含虚拟机（VM）的集群的诊断信息，并生成一个包含这些数据的压缩文件（zip文件）。

### [Get-ClusterExcludedAdapter](Get-ClusterExcludedAdapter.md)

从被排除的适配器列表中检索一个网络适配器。

### [Get-ClusterFaultDomain](Get-ClusterFaultDomain.md)

获取集群中的故障域信息。

### [Get-ClusterFaultDomainXML](Get-ClusterFaultDomainXML.md)

以XML字符串的形式获取故障域信息。

### [Get-ClusterGroup](Get-ClusterGroup.md)

获取关于故障转移集群中一个或多个聚类角色（资源组）的信息。

### [Get-ClusterGroupSet](Get-ClusterGroupSet.md)

获取集群中的组集（group sets）。

### [Get-ClusterGroupSetDependency](Get-ClusterGroupSetDependency.md)

根据依赖关系获取集群组集合。

### [Get-ClusterLog](Get-ClusterLog.md)

为故障转移集群中的所有节点或特定节点创建一个日志文件。

### [Get-ClusterNetwork](Get-ClusterNetwork.md)

获取关于故障转移集群中一个或多个网络的信息。

### [Get-ClusterNetworkInterface](Get-ClusterNetworkInterface.md)

获取关于故障转移集群中一个或多个网络适配器的信息。

### [Get-ClusterNode](Get-ClusterNode.md)

获取关于故障转移集群中的一个或多个节点或服务器的信息。

### [Get-ClusterOwnerNode](Get-ClusterOwnerNode.md)

获取关于在故障转移集群中哪些节点可以拥有某个资源的信息，或者关于拥有该资源的节点之间的优先级顺序的信息。

### [Get-ClusterParameter](Get-ClusterParameter.md)

获取关于故障转移集群中某个对象（例如集群资源）的详细信息。

### [Get-ClusterQuorum](Get-ClusterQuorum.md)

获取有关故障转移集群的法定人数（quorum）配置的信息。

### [Get-ClusterResource](Get-ClusterResource.md)

获取关于故障转移集群中一个或多个资源的信息。

### [Get-ClusterResourceDependency](Get-ClusterResourceDependency.md)

获取有关故障转移集群中已配置的、用于连接集群资源的依赖项的信息。

### [Get-ClusterResourceDependencyReport](Get-ClusterResourceDependencyReport.md)

生成一份报告，列出故障转移集群中各资源之间的依赖关系。

### [Get-ClusterResourceType](Get-ClusterResourceType.md)

获取关于故障转移集群中一种或多种资源类型的信息。

### [Get-ClusterSharedVolume](Get-ClusterSharedVolume.md)

获取关于故障转移集群中集群共享卷（Cluster Shared Volumes）的信息。

### [Get-ClusterSharedVolumeState](Get-ClusterSharedVolumeState.md)

获取集群中Cluster Shared Volumes（群集共享卷）的状态。

### [Get-ClusterStorageSpacesDirect](Get-ClusterStorageSpacesDirect.md)

从集群中获取S2D设置。

### [Get-ClusterVMMonitoredItem](Get-ClusterVMMonitoredItem.md)

获取虚拟机中当前正在被监控的服务和事件的列表。

### [Get-VMAdaptersConnectedToEnabledIntentSwitch](Get-VMAdaptersConnectedToEnabledIntentSwitch.md)

获取连接到已启用意图切换器的虚拟机（VM）上的适配器。

### [Grant-ClusterAccess](Grant-ClusterAccess.md)

允许访问故障转移集群，可以是全权限访问，也可以是只读访问。

### [Move-ClusterGroup](Move-ClusterGroup.md)

将一个集群角色（即一个资源组）从故障转移集群中的一个节点移动到另一个节点。

### [Move-ClusterResource](Move-ClusterResource.md)

将一个集群资源从一个集群角色移动到另一个集群角色，该操作发生在故障转移集群内部。

### [Move-ClusterSharedVolume](Move-ClusterSharedVolume.md)

在故障转移集群中，将一个集群共享卷（Cluster Shared Volume，简称 CSV）的所有权转移到另一个节点上。

### [Move-ClusterVirtualMachineRole](Move-ClusterVirtualMachineRole.md)

将集群虚拟机的所有权转移到另一个节点上。

### [新集群](New-Cluster.md)

创建一个新的故障转移集群。

### [New-ClusterAffinityRule](New-ClusterAffinityRule.md)

创建新的亲和性规则。

### [New-ClusterFaultDomain](New-ClusterFaultDomain.md)

在集群中创建一个故障域。

### [New-ClusterGroupSet](New-ClusterGroupSet.md)

在集群中创建一组名称对应的组（groups）。

### [New-ClusterNameAccount](New-ClusterNameAccount.md)

在 Active Directory 域服务中创建一个用于管理集群名称的账户。

### [New-WorkgroupCluster](New-WorkgroupCluster.md)

创建一个新的工作组集群。

### [Remove-Cluster](Remove-Cluster.md)

会销毁现有的故障转移集群。

### [Remove-ClusterAccess](Remove-ClusterAccess.md)

从集群的访问列表中移除某个用户。

### [Remove-ClusterAffinityRule](Remove-ClusterAffinityRule.md)

删除指定的亲和性规则。

### [Remove-ClusterCheckpoint](Remove-ClusterCheckpoint.md)

删除某个资源的加密密钥检查点或注册表检查点。

### [Remove-ClusterExcludedAdapter](Remove-ClusterExcludedAdapter.md)

从被排除的适配器列表中移除一个网络适配器。

### [Remove-ClusterFaultDomain](Remove-ClusterFaultDomain.md)

删除一个故障域。

### [Remove-ClusterGroup](Remove-ClusterGroup.md)

从故障转移集群中删除一个聚类角色（也称为资源组）。

### [从亲和性规则中移除集群组](Remove-ClusterGroupFromAffinityRule.md)

从一个亲和性规则中删除一个集群组。

### [Remove-ClusterGroupFromSet](Remove-ClusterGroupFromSet.md)

从一个集合中移除一个组。

### [Remove-ClusterGroupSet](Remove-ClusterGroupSet.md)

从集群中删除一组（group set）。

### [Remove-ClusterGroupSetDependency](Remove-ClusterGroupSetDependency.md)

从一个组集中移除一个依赖项。

### [Remove-ClusterNode](Remove-ClusterNode.md)

从一个故障转移集群中删除一个节点。

### [Remove-ClusterResource](Remove-ClusterResource.md)

从故障转移集群中移除一个已聚类的资源。

### [Remove-ClusterResourceDependency](Remove-ClusterResourceDependency.md)

在故障转移集群中，移除集群角色内两个资源之间的依赖关系。

### [Remove-ClusterResourceType](Remove-ClusterResourceType.md)

从故障转移集群中删除某种资源类型。

### [Remove-ClusterSharedVolume](Remove-ClusterSharedVolume.md)

从故障转移集群中的集群共享卷中删除某个卷，并将其放入该集群的可用存储空间中。

### [从亲和性规则中移除集群共享卷](Remove-ClusterSharedVolumeFromAffinityRule.md)

将某个集群共享卷从关联规则中移除。

### [Remove-ClusterVMMonitoredItem](Remove-ClusterVMMonitoredItem.md)

## 语法 ## 概述

### [Remove-WorkgroupCluster](Remove-WorkgroupCluster.md)

删除一个工作组集群。

### [Remove-WorkgroupClusterNode](Remove-WorkgroupClusterNode.md)

从一个工作组集群中删除一个节点。

### [Repair-ClusterNameAccount](Repair-ClusterNameAccount.md)

修复集群名称相关的账户问题，并确保集群能够继续正常运行。

### [Repair-ClusterStorageSpacesDirect](Repair-ClusterStorageSpacesDirect.md)

修复存储空间直接（Storage Spaces Direct, S2D）系统中的磁盘问题。

### [Reset-ClusterVMMonitoredState](Reset-ClusterVMMonitoredState.md)

将虚拟机的应用程序关键状态重置为正常状态，从而使该虚拟机在集群中不再被标记为处于关键状态。

### [Resume-ClusterNode]( Resume-ClusterNode.md)

将节点从暂停状态恢复过来，或者将之前被“消耗”（即无法正常运行）的工作负载重新分配回该节点，或者同时执行这两项操作。

### [Resume-ClusterResource]( Resume-ClusterResource.md)

在故障转移集群中，会关闭对某个磁盘资源或集群共享卷（Cluster Shared Volume）的维护操作。

### [Set-AccelNetManagement](Set-AccelNetManagement.md)

在整个集群范围内设置加速网络管理功能。

### [Set-AccelNetVM](Set-AccelNetVM.md)

在虚拟机上启用加速网络功能（Accelerated Networking）。

### [Set-ClusterAffinityRule](Set-ClusterAffinityRule.md)

启用或禁用亲和性规则，并更新规则类型。

### [Set-ClusterExcludedAdapter](Set-ClusterExcludedAdapter.md)

将某个网络适配器添加到被排除的适配器列表中。

### [Set-ClusterFaultDomain](Set-ClusterFaultDomain.md)

更新现有的集群故障域（cluster fault domain）。

### [Set-ClusterFaultDomainXML](Set-ClusterFaultDomainXML.md)

使用XML设置集群故障域。

### [Set-ClusterGroupSet](Set-ClusterGroupSet.md)

更新集群组集合。

### [Set-ClusterLog](Set-ClusterLog.md)

设置集群日志的大小和详细程度级别。

### [Set-ClusterOwnerNode](Set-ClusterOwnerNode.md)

指定在故障转移集群中哪些节点可以拥有资源；或者为集群角色或资源组确定各拥有节点之间的优先顺序。

### [Set-ClusterParameter](Set-ClusterParameter.md)

用于控制故障转移集群中对象的特定属性，例如资源、组或网络。

### [Set-ClusterQuorum](Set-ClusterQuorum.md)

为故障转移集群配置法定人数（quorum）选项。

### [Set-ClusterResourceDependency](Set-ClusterResourceDependency.md)

指定了在故障转移集群中某个特定资源所依赖的其他资源。

### [Set-ClusterStorageSpacesDirect](Set-ClusterStorageSpacesDirect.md)

设置S2D缓存参数。

### [Set-ClusterStorageSpacesDirectDisk](Set-ClusterStorageSpacesDirectDisk.md)

配置系统以决定S2D是否可以申请或放弃特定的物理磁盘。

### [Set-WorkgroupClusterRemotingConfiguration](Set-WorkgroupClusterRemotingConfiguration.md)

配置作为工作组一部分的故障转移集群的远程管理设置。

### [启动集群](Start-Cluster.md)

在集群中所有尚未启动该服务的节点上，启动该服务。

### [Start-ClusterGroup](Start-ClusterGroup.md)

在故障转移集群上启动一个或多个集群角色（也称为资源组）。

### [Start-ClusterNode](Start-ClusterNode.md)

在故障转移集群中的一个节点上启动Cluster服务。

### [Start-ClusterResource](Start-ClusterResource.md)

在故障转移集群中，将某个资源在线化（即使其能够正常使用）。

### [停止集群](Stop-Cluster.md)

在故障转移集群中，该操作会停止所有节点上的Cluster服务，从而导致集群中配置的所有服务和应用程序也一并终止运行。

### [Stop-ClusterGroup](Stop-ClusterGroup.md)

在故障转移集群中，停止一个或多个集群角色（clustered role）的运行。

### [Stop-ClusterNode](Stop-ClusterNode.md)

在故障转移集群中，停止某个节点上的Cluster服务。

### [Stop-ClusterResource](Stop-ClusterResource.md)

在故障转移集群中，将某个资源置于离线状态。

### [Suspend-ClusterNode](Suspend-ClusterNode.md)

暂停故障转移集群节点上的活动，即让该节点处于休眠状态。

### [Suspend-ClusterResource](Suspend-ClusterResource.md)

启用磁盘资源或CSV文件的维护模式，这样就可以运行磁盘维护工具而不会触发故障转移（failover）机制。

### [测试集群](Test-Cluster.md)

运行验证测试，以检查故障转移集群的硬件和配置是否正常。

### [Test-ClusterResourceFailure](Test-ClusterResourceFailure.md)

模拟集群资源的故障。

### [Test-WorkgroupCluster](Test-WorkgroupCluster.md)

测试工作组集群的配置。

### [Test-WorkgroupClusterRemoting](Test-WorkgroupClusterRemoting.md)

测试所有节点上是否都配置了远程连接功能。

### [更新集群功能级别](Update-ClusterFunctionalLevel.md)

更新混合版本集群的功能级别。

### [更新-ClusterIP资源](Update-ClusterIPResource.md)

在故障转移集群中，续订或释放某个IP地址资源的DHCP租约。

### [更新集群网络名称资源](Update-ClusterNetworkNameResource.md)

将现有的网络名称资源注册到DNS服务器上，同时不会影响集群的正常运行（即不会中断集群的服务可用性）。

### [更新集群虚拟机配置](Update-ClusterVirtualMachineConfiguration.md)

刷新故障转移集群中集群化虚拟机的配置。
