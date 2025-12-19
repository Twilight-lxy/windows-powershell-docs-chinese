---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmnetworkadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMNetworkAdapter
---

# 设置虚拟机网络适配器

## 摘要
用于配置虚拟机或管理操作系统中的虚拟网络适配器的各项功能。

## 语法

### VMName（默认值）
```
Set-VMNetworkAdapter [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String> [-Name <String>] [-DynamicMacAddress] [-StaticMacAddress <String>]
 [-MacAddressSpoofing <OnOffState>] [-DhcpGuard <OnOffState>] [-RouterGuard <OnOffState>]
 [-PortMirroring <VMNetworkAdapterPortMirroringMode>] [-IeeePriorityTag <OnOffState>] [-VmqWeight <UInt32>]
 [-IovQueuePairsRequested <UInt32>] [-IovInterruptModeration <IovInterruptModerationValue>]
 [-IovWeight <UInt32>] [-IPsecOffloadMaximumSecurityAssociation <UInt32>] [-MaximumBandwidth <Int64>]
 [-MinimumBandwidthAbsolute <Int64>] [-MinimumBandwidthWeight <UInt32>] [-MandatoryFeatureId <String[]>]
 [-ResourcePoolName <String>] [-TestReplicaPoolName <String>] [-TestReplicaSwitchName <String>]
 [-VirtualSubnetId <UInt32>] [-AllowTeaming <OnOffState>] [-NotMonitoredInCluster <Boolean>]
 [-StormLimit <UInt32>] [-DynamicIPAddressLimit <UInt32>] [-DeviceNaming <OnOffState>]
 [-FixSpeed10G <OnOffState>] [-PacketDirectNumProcs <UInt32>] [-PacketDirectModerationCount <UInt32>]
 [-PacketDirectModerationInterval <UInt32>] [-VrssEnabled <Boolean>] [-VmmqEnabled <Boolean>]
 [-VmmqQueuePairs <UInt32>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ManagementOS
```
Set-VMNetworkAdapter [-ManagementOS] [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-Name <String>] [-MacAddressSpoofing <OnOffState>] [-DhcpGuard <OnOffState>]
 [-RouterGuard <OnOffState>] [-PortMirroring <VMNetworkAdapterPortMirroringMode>]
 [-IeeePriorityTag <OnOffState>] [-VmqWeight <UInt32>] [-IovQueuePairsRequested <UInt32>]
 [-IovInterruptModeration <IovInterruptModerationValue>] [-IovWeight <UInt32>]
 [-IPsecOffloadMaximumSecurityAssociation <UInt32>] [-MaximumBandwidth <Int64>]
 [-MinimumBandwidthAbsolute <Int64>] [-MinimumBandwidthWeight <UInt32>] [-MandatoryFeatureId <String[]>]
 [-ResourcePoolName <String>] [-TestReplicaPoolName <String>] [-TestReplicaSwitchName <String>]
 [-VirtualSubnetId <UInt32>] [-AllowTeaming <OnOffState>] [-NotMonitoredInCluster <Boolean>]
 [-StormLimit <UInt32>] [-DynamicIPAddressLimit <UInt32>] [-DeviceNaming <OnOffState>]
 [-FixSpeed10G <OnOffState>] [-PacketDirectNumProcs <UInt32>] [-PacketDirectModerationCount <UInt32>]
 [-PacketDirectModerationInterval <UInt32>] [-VrssEnabled <Boolean>] [-VmmqEnabled <Boolean>]
 [-VmmqQueuePairs <UInt32>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ResourceObject
```
Set-VMNetworkAdapter [-VMNetworkAdapter] <VMNetworkAdapterBase> [-DynamicMacAddress]
 [-StaticMacAddress <String>] [-MacAddressSpoofing <OnOffState>] [-DhcpGuard <OnOffState>]
 [-RouterGuard <OnOffState>] [-PortMirroring <VMNetworkAdapterPortMirroringMode>]
 [-IeeePriorityTag <OnOffState>] [-VmqWeight <UInt32>] [-IovQueuePairsRequested <UInt32>]
 [-IovInterruptModeration <IovInterruptModerationValue>] [-IovWeight <UInt32>]
 [-IPsecOffloadMaximumSecurityAssociation <UInt32>] [-MaximumBandwidth <Int64>]
 [-MinimumBandwidthAbsolute <Int64>] [-MinimumBandwidthWeight <UInt32>] [-MandatoryFeatureId <String[]>]
 [-ResourcePoolName <String>] [-TestReplicaPoolName <String>] [-TestReplicaSwitchName <String>]
 [-VirtualSubnetId <UInt32>] [-AllowTeaming <OnOffState>] [-NotMonitoredInCluster <Boolean>]
 [-StormLimit <UInt32>] [-DynamicIPAddressLimit <UInt32>] [-DeviceNaming <OnOffState>]
 [-FixSpeed10G <OnOffState>] [-PacketDirectNumProcs <UInt32>] [-PacketDirectModerationCount <UInt32>]
 [-PacketDirectModerationInterval <UInt32>] [-VrssEnabled <Boolean>] [-VmmqEnabled <Boolean>]
 [-VmmqQueuePairs <UInt32>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Set-VMNetworkAdapter [-VM] <VirtualMachine> [-Name <String>] [-DynamicMacAddress] [-StaticMacAddress <String>]
 [-MacAddressSpoofing <OnOffState>] [-DhcpGuard <OnOffState>] [-RouterGuard <OnOffState>]
 [-PortMirroring <VMNetworkAdapterPortMirroringMode>] [-IeeePriorityTag <OnOffState>] [-VmqWeight <UInt32>]
 [-IovQueuePairsRequested <UInt32>] [-IovInterruptModeration <IovInterruptModerationValue>]
 [-IovWeight <UInt32>] [-IPsecOffloadMaximumSecurityAssociation <UInt32>] [-MaximumBandwidth <Int64>]
 [-MinimumBandwidthAbsolute <Int64>] [-MinimumBandwidthWeight <UInt32>] [-MandatoryFeatureId <String[]>]
 [-ResourcePoolName <String>] [-TestReplicaPoolName <String>] [-TestReplicaSwitchName <String>]
 [-VirtualSubnetId <UInt32>] [-AllowTeaming <OnOffState>] [-NotMonitoredInCluster <Boolean>]
 [-StormLimit <UInt32>] [-DynamicIPAddressLimit <UInt32>] [-DeviceNaming <OnOffState>]
 [-FixSpeed10G <OnOffState>] [-PacketDirectNumProcs <UInt32>] [-PacketDirectModerationCount <UInt32>]
 [-PacketDirectModerationInterval <UInt32>] [-VrssEnabled <Boolean>] [-VmmqEnabled <Boolean>]
 [-VmmqQueuePairs <UInt32>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-VMNetworkAdapter` cmdlet 用于配置虚拟机或管理操作系统中的虚拟网络适配器的各项功能。

## 示例

### 示例 1
```
PS C:\> Set-VMNetworkAdapter -VMName Redmond -DhcpGuard On
```

这个示例为虚拟机Redmond的所有虚拟网络适配器启用了DHCP Guard功能。当DHCP Guard被启用后，如果虚拟机Redmond响应来自DHCP客户端的数据包请求，这些响应会被直接丢弃。

### 示例 2
```
PS C:\> Set-VMNetworkAdapter -VMName Kirkland -PortMirroring Source
```

这个示例使得虚拟机Kirkland上的所有虚拟网络适配器都能够支持端口镜像功能。当端口镜像功能被启用后，该虚拟机发送或接收的每个数据包都会被复制并发送到一台监控用虚拟机上。

### 示例 3
```
PS C:\> Set-VMNetworkAdapter -VMName Bellevue -Name PM_Dest -PortMirroring Destination
```

这个示例将名为 PM_Dest 的虚拟网络适配器配置为端口镜像的目标端，从而使得名为 Bellevue 的虚拟机能够监控网络流量。也就是说，任何由连接到同一虚拟交换机的被监控虚拟机发送或接收的数据包都会通过虚拟网络适配器 PM_Dest 被传输到 Bellevue 虚拟机。

### 示例 4
```
PS C:\> Get-VMNetworkAdapter -All | Set-VMNetworkAdapter -VmqWeight 100
```

这个示例启用了VMQ（虚拟消息队列），并为本地主机上的每个虚拟网络适配器设置了100的权重。

### 示例 5
```
PS C:\> Get-VM Redmond | Set-VMNetworkAdapter -AllowTeaming On
```

这个示例为名为“Redmond”的虚拟机的所有虚拟网络适配器配置了NIC组（NIC Teaming）。

### 示例 6
```
PS C:\> Get-VMNetworkAdapter -VMName Redmond,Kirkland,Bellevue | Set-VMNetworkAdapter -MinimumBandwidthWeight 1
```

这个示例为三台虚拟机（Redmond、Kirkland和Bellevue）的所有虚拟网络适配器设置了相同的最低带宽权重。这种配置会在这三台虚拟机的所有虚拟网络适配器之间平均分配带宽。

## 参数

### -AllowTeaming
指定该虚拟网络适配器是否可以与连接到同一虚拟交换机的其他网络适配器组合使用。可选值为 **On**（允许）或 **Off**（不允许）。

```yaml
Type: OnOffState
Parameter Sets: (All)
Aliases:
Accepted values: On, Off

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: VMName, ManagementOS
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于配置网络适配器功能的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行识别。默认值为本地计算机；可以通过使用 “localhost” 或句点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName, ManagementOS
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName, ManagementOS
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DeviceNaming
指定此适配器是否使用设备命名机制。

```yaml
Type: OnOffState
Parameter Sets: (All)
Aliases:
Accepted values: On, Off

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DhcpGuard
该设置用于指定是否拒绝来自声称自己是 DHCP 服务器的虚拟机的 DHCP 消息。可选值为：**On**（表示拒绝接收这些消息，因为认为该虚拟化的 DHCP 服务器不可信）；**Off**（表示允许接收这些消息，因为认为该虚拟化的 DHCP 服务器是可信的）。

```yaml
Type: OnOffState
Parameter Sets: (All)
Aliases:
Accepted values: On, Off

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DynamicIPAddressLimit
指定动态IP地址的最大数量限制，该值为一个整数。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DynamicMacAddress
为虚拟网络适配器分配一个动态生成的MAC地址。

```yaml
Type: SwitchParameter
Parameter Sets: VMName, ResourceObject, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FixSpeed10G
指定适配器是否使用固定的传输速度（10G）。

```yaml
Type: OnOffState
Parameter Sets: (All)
Aliases:
Accepted values: On, Off

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPsecOffloadMaximumSecurityAssociation
指定可以卸载到绑定到虚拟交换机且支持IPSec任务卸载功能的物理网络适配器的最大安全关联数量。如果设置为0，则禁用该功能。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IeeePriorityTag
该设置用于指定是否应信任来自虚拟机的带有IEEE 802.1p标记的数据包。可选值只有两个：**On**（表示信任）或**Off**（表示不信任）。如果设置为**On**，则这些数据包将按原样被传输；如果设置为**Off**，则它们的优先级会被重置为0。

```yaml
Type: OnOffState
Parameter Sets: (All)
Aliases:
Accepted values: On, Off

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IovInterruptModeration
该选项用于指定分配给虚拟网络适配器的单根I/O虚拟化（SR-IOV）虚拟函数的中断调节值。允许的取值为：**Default**、**Adaptive**、**Off**、**Low**、**Medium** 和 **High**。如果选择 **Default**，则该值由物理网络适配器制造商的设置决定；如果选择 **Adaptive**，中断调节率将根据运行时的流量模式进行动态调整。

```yaml
Type: IovInterruptModerationValue
Parameter Sets: (All)
Aliases:
Accepted values: Default, Adaptive, Off, Low, Medium, High

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IovQueuePairsRequested
指定要分配给一个 SR-IOV 虚拟函数的硬件队列对的数量。如果需要接收端扩展（RSS），并且连接到虚拟交换机的物理网络适配器支持在 SR-IOV 虚拟函数上使用 RSS，那么就需要多个队列对。允许的值范围是从 1 到 4294967295。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IovWeight
指定是否要在此虚拟网络适配器上启用单根I/O虚拟化（SR-IOV）。该数值的相对权重决定了虚拟网络适配器与所分配的SR-IOV虚拟函数的关联程度。数值范围为0到100；若要禁用虚拟网络适配器上的SR-IOV功能，请指定0。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MacAddressSpoofing
该设置用于指定虚拟机在发送数据包时是否可以将源MAC地址更改为未分配给它的MAC地址。允许的值为“On”（允许虚拟机使用其他MAC地址）和“Off”（仅允许虚拟机使用分配给它的MAC地址）。

```yaml
Type: OnOffState
Parameter Sets: (All)
Aliases:
Accepted values: On, Off

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagementOS
指定在管理操作系统中需要配置的虚拟网络适配器。

```yaml
Type: SwitchParameter
Parameter Sets: ManagementOS
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MandatoryFeatureId
指定了该虚拟网络适配器正常运行所需的虚拟交换机扩展功能的唯一标识符。

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

### -MaximumBandwidth
该参数用于指定虚拟网络适配器的最大带宽（单位：比特每秒）。指定的值会四舍五入到最接近的8的倍数。如果设置为0，则表示禁用此功能。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinimumBandwidthAbsolute
指定虚拟网络适配器的最小带宽（单位：比特每秒）。所指定的值会四舍五入到最接近的8的倍数。建议使用大于100 Mbps的带宽值。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MinimumBandwidthWeight
指定虚拟网络适配器的最小带宽（以相对权重表示）。该“权重”用于说明应向该虚拟网络适配器分配多少带宽，相对于连接到同一虚拟交换机的其他虚拟网络适配器而言。该值的取值范围为 0 到 100。若要禁用此功能，请指定值为 0。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
用于指定虚拟网络适配器的名称。此cmdlet会将名称更改为您指定的值。

```yaml
Type: String
Parameter Sets: VMName, ManagementOS, VMObject
Aliases: VMNetworkAdapterName

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NotMonitoredInCluster
该设置用于指示：当某个虚拟机所属的集群包含多个虚拟机时，是否仍需监控该虚拟机所连接的网络适配器。默认情况下，集群中的所有虚拟机所使用的网络适配器都会被监控。

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

### -PacketDirectModerationCount
指定在发出中断信号之前需要等待的数据包数量。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PacketDirectModerationInterval
指定在数据包到达后等待多久（以毫秒为单位），再发出中断信号。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PacketDirectNumProcs
指定在主机内部用于虚拟交换机处理的处理器数量。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定一个对象需要被传递给代表要配置的虚拟网络适配器的管道。如果指定了 `ManagementOS`，则该对象为 `Microsoft.HyperV.PowerShell.VMInternalNetworkAdapter`；否则为 `Microsoft.HyperV.PowerShell.VMNetworkAdapter` 对象。

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

### -PortMirroring
指定要配置的网络适配器的端口镜像模式。允许的值有 **None**（禁用）、**Source**（源）和 **Destination**（目标）。如果将虚拟网络适配器配置为 **Source**，则其发送或接收的每个数据包都会被复制并转发到另一个被配置为接收这些数据包的虚拟网络适配器；如果将虚拟网络适配器配置为 **Destination**，它将从源虚拟网络适配器接收复制的数据包。源虚拟网络适配器和目标虚拟网络适配器必须连接到同一个虚拟交换机上。若要禁用此功能，请指定 **None**。

```yaml
Type: VMNetworkAdapterPortMirroringMode
Parameter Sets: (All)
Aliases:
Accepted values: None, Destination, Source

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourcePoolName
指定资源池的名称。

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

### -RouterGuard
指定是否删除来自未经授权的虚拟机的**路由器广告（Router Advertisement）**和**重定向（Redirection）**消息。该值可以是**开（On）**或**关（Off）**。如果设置为**开**，则这些消息会被删除；如果设置为**关**，则这些消息会被发送。

```yaml
Type: OnOffState
Parameter Sets: (All)
Aliases:
Accepted values: On, Off

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StaticMacAddress
为虚拟网络适配器分配一个特定的MAC地址。

```yaml
Type: String
Parameter Sets: VMName, ResourceObject, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StormLimit
该参数指定虚拟机每秒通过指定的虚拟网络适配器发送的广播包、多播包以及未知单播包的数量。在某一秒钟内超过这个限制的广播包、多播包和未知单播包将会被丢弃。如果值为 0，则表示没有数量限制。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TestReplicaPoolName
此参数仅适用于已启用复制的虚拟机。它指定了在测试故障转移过程中创建该虚拟机时，该虚拟网络适配器将使用的网络资源池的名称。

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

### -TestReplicaSwitchName
此参数仅适用于已启用复制的虚拟机。它指定了在测试故障转移过程中创建虚拟机时，虚拟网络适配器应连接的虚拟交换机的名称。

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

### -VM
指定包含您想要配置的虚拟网络的虚拟机。

```yaml
Type: VirtualMachine
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定包含您想要配置的虚拟网络适配器的虚拟机的名称。

```yaml
Type: String
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapter
指定虚拟网络适配器。

```yaml
Type: VMNetworkAdapterBase
Parameter Sets: ResourceObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VirtualSubnetId
指定用于Hyper-V网络虚拟化的虚拟子网ID。允许的值范围是4096到16777215（2^24 - 1），以及0。使用0可以清除此参数的设置。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VmmqEnabled


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

### -VmmqQueuePairs


```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VmqWeight
指定是否要在虚拟网络适配器上启用虚拟机队列（VMQ）。相对权重表示虚拟网络适配器使用 VMQ 的优先级。该数值的范围是从 0 到 100。如果指定值为 0，则表示在虚拟网络适配器上禁用 VMQ。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VrssEnabled


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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无

默认情况下，此cmdlet不会返回任何输出。

### Microsoft.HyperV.PowerShell.VMNetworkAdapter

当你使用 **PassThru** 参数时，此cmdlet会返回一个 **Microsoft.HyperV POWERShell.VMNetworkAdapter** 对象。

### Microsoft.HyperV.PowShell.VMInternalNetworkAdapter

当你使用 **PassThru** 和 **-ManagementOS** 参数时，此 cmdlet 会返回一个 **Microsoft.HyperV POWERShell.VMInternalNetworkAdapter** 对象。

## 备注

## 相关链接

