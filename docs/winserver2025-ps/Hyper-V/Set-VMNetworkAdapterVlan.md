---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmnetworkadaptervlan?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMNetworkAdapterVlan
---

# 设置虚拟机网络适配器的 VLAN

## 摘要
配置虚拟局域网（VLAN）设置，以便通过虚拟网络适配器传输数据流量。

## 语法

### VMName（默认值）
```
Set-VMNetworkAdapterVlan [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-VMName] <String[]> [-Untagged] [-Access]
 [-VlanId <Int32>] [-Trunk] [-NativeVlanId <Int32>] [-AllowedVlanIdList <String>] [-Isolated] [-Community]
 [-Promiscuous] [-PrimaryVlanId <Int32>] [-SecondaryVlanId <Int32>] [-SecondaryVlanIdList <String>] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ResourceObject
```
Set-VMNetworkAdapterVlan [-VMNetworkAdapter] <VMNetworkAdapterBase[]> [-Untagged] [-Access] [-VlanId <Int32>]
 [-Trunk] [-NativeVlanId <Int32>] [-AllowedVlanIdList <String>] [-Isolated] [-Community] [-Promiscuous]
 [-PrimaryVlanId <Int32>] [-SecondaryVlanId <Int32>] [-SecondaryVlanIdList <String>] [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### ManagementOS
```
Set-VMNetworkAdapterVlan [-ManagementOS] [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-Untagged] [-Access] [-VlanId <Int32>] [-Trunk]
 [-NativeVlanId <Int32>] [-AllowedVlanIdList <String>] [-Isolated] [-Community] [-Promiscuous]
 [-PrimaryVlanId <Int32>] [-SecondaryVlanId <Int32>] [-SecondaryVlanIdList <String>] [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### VMObject
```
Set-VMNetworkAdapterVlan [-VMNetworkAdapterName <String>] [-VM] <VirtualMachine[]> [-Untagged] [-Access]
 [-VlanId <Int32>] [-Trunk] [-NativeVlanId <Int32>] [-AllowedVlanIdList <String>] [-Isolated] [-Community]
 [-Promiscuous] [-PrimaryVlanId <Int32>] [-SecondaryVlanId <Int32>] [-SecondaryVlanIdList <String>] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-VMNetworkAdapterVlan` cmdlet 用于配置通过虚拟网络适配器传输数据的虚拟局域网（LAN）设置。选项包括 “Access”、“Trunk”、“Private VLAN”（隔离模式、共享模式或混杂模式）以及 “Untagged”；这些选项之间是互斥的，即只能选择其中一个选项。

## 示例

### 示例 1
```
PS C:\> Set-VMNetworkAdapterVlan -VMName Redmond -Access -VlanId 121
```

将虚拟机 Redmond 中的虚拟网络适配器设置为“访问”模式。该虚拟机发送的流量会被标记上 VLAN ID 121。

### 示例 2
```
PS C:\> Set-VMNetworkAdapterVlan -VMName Redmond -Trunk -AllowedVlanIdList 1-100 -NativeVlanId 10
```

将虚拟机 Redmond 中的虚拟网络适配器设置为“Trunk”模式。任何带有允许的 VLAN 列表中某个 VLAN ID 标签的流量都将被允许发送或接收到该 VLAN。如果流量没有标签，则会被视为属于 VLAN 10。

### 示例 3
```
PS C:\> Get-VMNetworkAdapter -VMName Redmond | Set-VMNetworkAdapterVlan -Isolated -PrimaryVlanId 10 -SecondaryVlanId 200
```

从名为“Redmond”的虚拟机中获取虚拟网络适配器，并将它们设置为私有VLAN隔离模式。在此模式下，主VLAN的编号为10，次级VLAN的编号为200。

### 示例 4
```
PS C:\> Get-VMNetworkAdapter -VMName WA | Set-VMNetworkAdapterVlan -Promiscuous -PrimaryVlanId 10 -SecondaryVlanIdList 200-201
```

从虚拟机WA中获取虚拟网络适配器，并将它们设置为“私有VLAN混杂模式”（private VLAN promiscuous mode）。其中，主VLAN的编号为10，次级VLAN的编号分别为201和202。

### 示例 5
```
PS C:\> Get-VM Redmond | Set-VMNetworkAdapterVlan -Untagged
```

获取名为“Redmond”的虚拟机，并将该虚拟机中的虚拟网络适配器设置为“未标记”模式（untagged mode）。

### 示例 5
```
PS C:\> Set-VMNetworkAdapterVlan -ManagementOS -Access -VlanID 20
```

将管理操作系统中的虚拟交换机设置为“访问模式”。通过该虚拟交换机发送的流量会被标记上VLAN ID 20。

## 参数

### -Access
指定虚拟机网络适配器的访问（Access）模式。此参数用于配置一个未标记的虚拟端口，并关联相应的 VLANID（基于端口的 VLAN），因此必须与 VLANID 一起进行设置。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: a

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowedVlanIdList
指定允许在虚拟机网络适配器上使用的虚拟局域网（VLAN）列表。此参数必须与 **Trunk** 参数一起使用。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: VMName, ManagementOS
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Community
指定要配置的虚拟机网络适配器的**社区（Community）**模式。此参数必须与**PrimaryVlanId**和**SecondaryVlanId**参数一起使用。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: c

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个Hyper-V主机，在这些主机上需要配置虚拟机网络适配器的虚拟局域网（VLAN）设置。可以使用NetBIOS名称、IP地址或完全合格的域名进行指定。默认值是本地计算机。可以使用“localhost”或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName, ManagementOS
Aliases:

Required: False
Position: Named
默认值 value: None
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
默认值 value: False
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
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Isolated
指定用于配置虚拟机网络适配器的“隔离（Isolated）”模式。此参数必须与 **PrimaryVlanId** 和 **SecondaryVlanId** 参数一起使用。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: i

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagementOS
指定管理系统（例如父系统或宿主操作系统）的类型。

```yaml
Type: SwitchParameter
Parameter Sets: ManagementOS
Aliases:

Required: True
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NativeVlanId
用于指定虚拟机网络适配器的本地虚拟局域网（VLAN）标识符。此参数必须与 **Trunk** 参数一起使用。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 `Microsoft.HyperV.PowerShell.VMNetworkAdapterVlanSetting` 对象传递给管道，该对象表示要配置的虚拟机网络适配器的虚拟局域网（VLAN）设置。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PrimaryVlanId
用于指定处于“社区模式”（Community）、“隔离模式”（Isolated）或“混杂模式”（Promiscuous）下的虚拟网络适配器的主要虚拟局域网标识符。

如果虚拟机网络适配器处于“Community”或“Isolated”模式，必须结合参数**SecondaryVlanId**来指定此参数。如果虚拟机网络适配器处于“Promiscuous”模式，则必须结合参数**SecondaryVlanIdList**来使用该参数。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Promiscuous
为虚拟机网络适配器指定“混杂模式”（Promiscuous mode）。

此参数必须与参数 **PrimaryVlanId** 和 **SecondaryVlanIdList** 一起指定。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: p

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SecondaryVlanId
用于指定处于“社区模式”（Community）或“隔离模式”（Isolated）下的虚拟网络适配器的次级虚拟局域网标识符。

此参数必须与参数 **PrimaryVlanId** 一起指定，并且还需要配合交换机参数 **Community** 或 **Isolated** 使用。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SecondaryVlanIdList
用于指定虚拟机网络适配器上的一系列私有虚拟局域网（secondary VLAN）。此参数必须与参数 **PrimaryVlanId** 以及交换机参数 **Promiscuous** 一起使用。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Trunk
指定虚拟机网络适配器的**Trunk**模式。该参数配置了一个带标签的虚拟端口，该端口会将所有允许的VLANId标签传递给虚拟机适配器；而带有NativeVLANId的数据包则会以未标记的形式传递给虚拟机适配器。此参数必须与**AllowedVlanIdList**和**NativeVlanId**参数一起使用。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: t

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Untagged
为虚拟机网络适配器指定“未标记（Untagged）”模式。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: u

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapter
指定虚拟机的网络适配器。

```yaml
Type: VMNetworkAdapterBase[]
Parameter Sets: ResourceObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapterName
指定虚拟机网络适配器的名称。

```yaml
Type: String
Parameter Sets: VMName, ManagementOS, VMObject
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VlanId
指定虚拟机网络适配器的虚拟局域网（VLAN）标识符。此参数必须与切换参数 **Access** 一起使用。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases: AccessVlanId

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.VMNetworkAdapterVlanSetting
如果指定了 `-PassThru` 参数的话……

## 备注

## 相关链接
[配置并查看Hyper-V虚拟交换机端口的VLAN设置](/windows-server/virtualization/hyper-v-virtual-switch/configure-and-view-vlan-settings-on-hyper-v-virtual-switch-ports)
