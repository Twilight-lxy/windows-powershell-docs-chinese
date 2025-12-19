---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmnetworkadapterisolation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMNetworkAdapterIsolation
---

# 设置虚拟机网络适配器的隔离状态

## 摘要
修改虚拟网络适配器的隔离设置。

## 语法

### VMName（默认值）
```
Set-VMNetworkAdapterIsolation [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-VMName] <String[]>
 [-IsolationMode <VMNetworkAdapterIsolationMode>] [-AllowUntaggedTraffic <Boolean>]
 [-DefaultIsolationID <Int32>] [-MultiTenantStack <OnOffState>] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ResourceObject
```
Set-VMNetworkAdapterIsolation [-VMNetworkAdapter] <VMNetworkAdapterBase[]>
 [-IsolationMode <VMNetworkAdapterIsolationMode>] [-AllowUntaggedTraffic <Boolean>]
 [-DefaultIsolationID <Int32>] [-MultiTenantStack <OnOffState>] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ManagementOS
```
Set-VMNetworkAdapterIsolation [-ManagementOS] [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-IsolationMode <VMNetworkAdapterIsolationMode>]
 [-AllowUntaggedTraffic <Boolean>] [-DefaultIsolationID <Int32>] [-MultiTenantStack <OnOffState>] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Set-VMNetworkAdapterIsolation [-VMNetworkAdapterName <String>] [-VM] <VirtualMachine[]>
 [-IsolationMode <VMNetworkAdapterIsolationMode>] [-AllowUntaggedTraffic <Boolean>]
 [-DefaultIsolationID <Int32>] [-MultiTenantStack <OnOffState>] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-VMNetworkAdapterIsolation` cmdlet 用于修改虚拟网络适配器的隔离设置。你可以通过使用虚拟局域网（VLAN）、Hyper-V 网络虚拟化或第三方虚拟化解决方案来对虚拟机适配器进行隔离。你可以指定隔离方法，并修改其他设置，其中包括多租户相关设置。有关多租户的更多信息，请参阅 `Add-VMNetworkAdapterRoutingDomainMapping` cmdlet。

## 示例

### 示例 1：为虚拟机设置隔离模式
```
PS C:\> Set-VMNetworkAdapterIsolation -VMName "TSQA01" -AllowUntaggedTraffic $False -IsolationMode NativeVirtualSubnet -MultiTenantStack On
```

此命令将名为TSQA01的虚拟机的隔离模式设置为NativeVirtualSubnet，该模式表示使用Hyper-V网络虚拟化技术。该虚拟机不接受未标记的流量；但由于**MultitenantStack**参数的值为“On”，因此该虚拟机可以为多个租户提供服务。

### 示例 2：为虚拟机设置隔离模式和未标记流量（untagged traffic）的相关配置
```
PS C:\> Set-VMNetworkAdapterIsolation -VMName "TSQA01" -AllowUntaggedTraffic $True -IsolationMode VLAN -DefaultIsolationID 1 -MultiTenantStack On
```

此命令将名为 TSQA01 的虚拟机的隔离模式设置为 VLAN。该虚拟机可以接收未标记的流量，这些流量在由 **DefaultIsolationID** 参数指定的 VLAN 1 上进行发送和接收。未标记的流量会被送入虚拟机中的默认区域。由于启用了多租户功能，因此该虚拟机会接收到关于隔离子网和路由域的信息。

## 参数

### -AllowUntaggedTraffic
该属性用于指示虚拟机是否发送和接收未标记（untagged）的数据包。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
指定一个Hyper-V主机的数组。该cmdlet会修改由所指定的计算机托管的虚拟机的隔离设置。

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
在运行 cmdlet 之前会提示您进行确认。

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

### -DefaultIsolationID
该参数用于指定虚拟机（已启用多租户功能）中通往默认隔间的网络ID。您指定的值仅适用于未标记的流量。只有当您为 *AllowUntaggedTraffic* 参数设置了 `$True` 时，此参数才会生效。

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

### -IsolationMode
指定适配器的隔离模式。此参数的可接受值包括：

- NativeVirtualSubnet.
Hyper-V Network Virtualization.
- ExternalVirtualSubnet.
A third party network virtualization solution.
- VLAN.
- None.

如果您指定值为 `None`，则网络适配器将使用其默认的隔离模式。您可以使用 `Set-VMNetworkAdapterVlan` cmdlet 或 `Set-VMNetworkAdapter` cmdlet 来设置默认的隔离模式。

```yaml
Type: VMNetworkAdapterIsolationMode
Parameter Sets: (All)
Aliases:
Accepted values: None, NativeVirtualSubnet, ExternalVirtualSubnet, Vlan

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagementOS
表示该 cmdlet 是在父操作系统或主机操作系统上运行的。如果您指定了此参数，该 cmdlet 将修改父操作系统或主机操作系统的隔离设置。

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

### -MultiTenantStack
指定是否为虚拟机使用多个隔离ID。该参数的可接受值为：

- On.
Indicate isolation IDs so that the virtual machine provides services to multiple tenants on different isolation subnets.
- Off.
Do not indicate isolation IDs to virtual machine.

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

### -Passthru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -VM
指定一个虚拟机对象数组。该cmdlet会修改属于所指定虚拟机的适配器的隔离设置。要获取虚拟机对象，请使用**Get-VM** cmdlet。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定一个虚拟机名称数组。该cmdlet会修改属于所指定虚拟机的适配器的隔离设置。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapter
指定一个由 **VMNetworkAdapterBase** 对象组成的虚拟机（VM）网络适配器数组。该 cmdlet 会修改所指定适配器的隔离设置。若要获取某个网络适配器，可以使用 **Get-VMNetworkAdapter** cmdlet。

```yaml
Type: VMNetworkAdapterBase[]
Parameter Sets: ResourceObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapterName
用于指定虚拟网络适配器的名称。该cmdlet会修改所指定适配器的隔离设置。

```yaml
Type: String
Parameter Sets: VMName, ManagementOS, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

```csharp
### Microsoft.HyperV.PowerShell.VMNetworkAdapterIsolationSetting
```

## 备注

## 相关链接

[Get-VMNetworkAdapterIsolation](./Get-VMNetworkAdapterIsolation.md)

[Get-VM](./Get-VM.md)

[Get-VMNetworkAdapter](./Get-VMNetworkAdapter.md)

[Set-VMNetworkAdapter](./Set-VMNetworkAdapter.md)

[Set-VMNetworkAdapterVlan](./Set-VMNetworkAdapterVlan.md)

