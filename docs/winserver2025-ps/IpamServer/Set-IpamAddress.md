---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamAddress.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/set-ipamaddress?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IpamAddress
---

# 设置 Ipam 地址

## 摘要
在IPAM中修改一个IP地址。

## 语法

### 按地址查找
```
Set-IpamAddress [-IpAddress] <IPAddress[]> [[-ManagedByService] <String[]>] [[-ServiceInstance] <String[]>]
 [-NetworkType <VirtualizationType[]>] [-AddressSpace <String[]>] [-NewIPAddress <IPAddress>]
 [-NewManagedByService <String>] [-NewServiceInstance <String>] [-NewNetworkType <VirtualizationType>]
 [-NewAddressSpace <String>] [-DeviceType <String>] [-IpAddressState <String>]
 [-AssignmentType <AddressAssignment>] [-AssignmentDate <DateTime>] [-MacAddress <String>]
 [-ExpiryDate <DateTime>] [-Description <String>] [-Owner <String>] [-AssetTag <String>]
 [-SerialNumber <String>] [-ClientId <String>] [-Duid <String>] [-Iaid <UInt32>] [-ReservationServer <String>]
 [-ReservationName <String>] [-ReservationType <DhcpReservationType>] [-ReservationDescription <String>]
 [-DeviceName <String>] [-ForwardLookupZone <String>] [-ForwardLookupPrimaryServer <String>]
 [-ReverseLookupZone <String>] [-ReverseLookupPrimaryServer <String>] [-AddCustomConfiguration <String>]
 [-RemoveCustomConfiguration <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject（cdxml）
```
Set-IpamAddress -InputObject <CimInstance[]> [-NewIPAddress <IPAddress>] [-NewManagedByService <String>]
 [-NewServiceInstance <String>] [-NewNetworkType <VirtualizationType>] [-NewAddressSpace <String>]
 [-DeviceType <String>] [-IpAddressState <String>] [-AssignmentType <AddressAssignment>]
 [-AssignmentDate <DateTime>] [-MacAddress <String>] [-ExpiryDate <DateTime>] [-Description <String>]
 [-Owner <String>] [-AssetTag <String>] [-SerialNumber <String>] [-ClientId <String>] [-Duid <String>]
 [-Iaid <UInt32>] [-ReservationServer <String>] [-ReservationName <String>]
 [-ReservationType <DhcpReservationType>] [-ReservationDescription <String>] [-DeviceName <String>]
 [-ForwardLookupZone <String>] [-ForwardLookupPrimaryServer <String>] [-ReverseLookupZone <String>]
 [-ReverseLookupPrimaryServer <String>] [-AddCustomConfiguration <String>]
 [-RemoveCustomConfiguration <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-IpamAddress` cmdlet 用于修改 IP 地址管理（IPAM）中的 IP 地址。您可以指定要修改的 IP 地址，或者使用 `InputObject` 参数来指定需要修改的 `IpamAddress` 对象。

您可以使用该cmdlet将动态主机配置协议（DHCP）的预留属性与IP地址关联起来。不过，该cmdlet本身并不会在DHCP服务器上创建相应的预留记录。若需在DHCP服务器上创建预留记录，建议您使用Windows PowerShell的相关功能来完成这一操作。

## 示例

### 示例 1：重新分配 IP 地址
```
PS C:\> Get-IpamAddress -IpAddress 172.16.10.10 | Set-IpamAddress -NewManagedByService "VMM" -NewServiceInstance "vmm1.contoso.com" -DeviceType "VM" -PassThru
IpAddress        : 172.16.10.10

NetworkType      : NonVirtualized

Duplicate        : False

ExpiryStatus     : Static

MacAddress       :

ManagedByService : VMM

ServiceInstance  : vmm1.contoso.com

DeviceName       :

DeviceType       : VM

IpAddressState   : In-Use

AssignmentType   : Static
```

该命令获取一个名为 **IpamAddress** 的对象，其中包含由 IPAM 管理的 IP 地址 172.16.10.10。通过使用管道运算符（pipeline operator），该命令将 **IpamAddress** 对象传递给 **Set-IpamAddress** cmdlet。**Set-IpamAddress** cmdlet 将管理该 IP 地址的服务从其他服务切换到 VMM，并将负责管理该 IP 地址的服务实例更改为 vmm1.contoso.com。最后，该命令将该 IP 地址分配给相应的虚拟机设备类型。

### 示例 2：为 IP 地址添加自定义元数据
```
PS C:\> Get-IpamAddress -IpAddress 172.16.10.10 | Set-IpamAddress -AddCustomConfiguration "ADSite=Main"
```

此命令为IP地址172.16.10.10添加自定义元数据。它将值“Main”添加到名为“ADSite”的自定义字段中。

### 示例 3：将 IP 地址的网络类型从非虚拟化更改为提供商虚拟化
```
PS C:\> Set-IpamAddress -IpAddress 172.16.10.10 -AddressSpace "Default" -NetworkType NonVirtualized -NewNetworkType Provider


IpAddress        : 172.16.10.10

NetworkType      : Provider

Duplicate        : False

ExpiryStatus     : Static

MacAddress       :

ManagedByService : VMM

ServiceInstance  : vmm1.contoso.com

DeviceName       :

DeviceType       : Host

IpAddressState   : In-Use

AssignmentType   : Static
```

这个命令将IP地址172.16.10.10的网络类型从“非虚拟化”更改为“提供商网络类型”。同时，该命令将该IP地址分配到默认的提供商地址空间中。

### 示例 4：将 IP 地址的网络类型从“虚拟化”类型转换为“非虚拟化”类型
```
PS C:\> Set-IpamAddress -IpAddress 172.16.10.10 -NetworkType Provider -NewNetworkType NonVirtualized -PassThru | Format-List IpAddress, NetworkType, ProviderAddressSpace, CustomerAddressSpace
IpAddress            : 172.16.10.10

NetworkType          : NonVirtualized

ProviderAddressSpace : Default

CustomerAddressSpace :
```

此命令将 IP 地址 172.16.10.10 的网络类型从“provider”更改为“non-virtualized”。默认情况下，该命令会将这个非虚拟化地址分配到“Default address space”中。通过使用管道运算符（pipeline operator），该命令将输出结果传递给 **Format-List** cmdlet，并将其格式化为表格形式。有关更多信息，请输入 `Get-Help Format-List`。

### 示例 5：为新地址空间分配一个 IP 地址
```
PS C:\> Set-IpamAddress -IpAddress 172.16.10.10 -NetworkType NonVirtualized -NewNetworkType Provider -NewAddressSpace MainDataCenter -PassThru | Format-List IpAddress, NetworkType, ProviderAddressSpace, CustomerAddressSpace
IpAddress            : 172.16.10.10

NetworkType          : Provider

ProviderAddressSpace : MainDataCenter

CustomerAddressSpace :
```

这个命令将 IP 地址 172.16.10.10 的网络类型从“非虚拟化”转换为“提供商虚拟化”。该命令将该 IP 地址分配到名为 MainDataCenter 的提供者地址空间中。接着，通过使用管道运算符（pipeline operator），该命令将输出结果传递给 **Format-List** cmdlet，并以表格的形式显示输出结果。

## 参数

### -AddCustomConfiguration
指定由分号（;）分隔的自定义元数据的名称和值对。该cmdlet会将这些自定义配置元数据添加到IP地址中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AddressSpace
指定与IP地址相关联的地址空间。默认值为“Default”。

```yaml
Type: String[]
Parameter Sets: ByAddress
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，随后再显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -AssetTag
指定与 IP 地址关联的资产标签。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AssignmentDate
指定您将 IP 地址分配给设备的日期。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AssignmentType
指定 IPAM 如何分配地址。默认值为 “Static”（静态）。

此参数的可接受值为：

- Static
- Dynamic
- Auto
- VIP
- Reserved

```yaml
Type: AddressAssignment
Parameter Sets: (All)
Aliases:
Accepted values: Static, Dynamic, Auto, VIP, Reserved

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，使用的是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ClientId
指定 IPAM 客户端的 ID。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Description
为设备的IP地址分配指定一个描述。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DeviceName
指定您已分配地址的设备名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DeviceType
指定您为其分配了地址的设备类型。请选择一个存在于内置自定义字段 **DeviceType** 中的有效值。

此参数的可接受值为：

- VM
- Host

The default value is Host.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Duid
指定客户端唯一的 DHCP 设备标识符（DUID）。客户端使用该 DUID 从 DHCPv6 服务器获取 IP 地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ExpiryDate
指定地址的有效期（即过期日期）。当 IP 地址失效时，IPAM 会向管理员发出警报。不过，IPAM 并不会自动回收已过期的地址。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ForwardLookupPrimaryServer
指定 IPAM 使用的域名系统（DNS）服务器的名称，该服务器用于将主机名解析为 IP 地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ForwardLookupZone
指定用于将主机名映射到IP地址的前向查找区域的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Iaid
用于指定 IPv6 地址的身份关联 ID（IAID）。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InputObject
指定要传递给此cmdlet的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给此cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -IpAddress
指定一个IP地址数组。

```yaml
Type: IPAddress[]
Parameter Sets: ByAddress
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IpAddressState
指定 IP 地址的使用状态。默认情况下，该 cmdlet 将地址设置为“正在使用”（In-Use）状态。

你可以为这个参数指定一个有效的自定义值。使用 **Add-IpamCustomValue** cmdlet 将自定义值添加到 IPAM 中的自定义字段中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MacAddress
指定该地址所分配到的设备的媒体访问控制（MAC）地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ManagedByService
指定用于管理 IP 地址的服务的名称。为此参数指定的值必须存在于您为 IPAM 中的 **ManagedByService** 自定义字段所定义的值集合中。

你可以使用 `Add-IpamCustomValue` cmdlet 向 IPAM 中的 `ManagedByService` 自定义字段添加一个值。你也可以使用 `Remove-IpamCustomValue` cmdlet 从 IPAM 中的 `ManagedByService` 自定义字段删除一个值。

```yaml
Type: String[]
Parameter Sets: ByAddress
Aliases: MB

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetworkType
指定地址的网络类型。

此参数的可接受值为：

- Provider
- Customer
- NonVirtualized

The default value is NonVirtualized.If you specify Default for the *AddressSpace* parameter, the valid values for this parameter are Provider and NonVirtualized.
If you specify a provider type of address space for the *AddressSpace* parameter, you must specify Provider for this parameter.
If you specify a customer type of address space for the *AddressSpace* parameter, you must specify Customer for this parameter.

```yaml
Type: VirtualizationType[]
Parameter Sets: ByAddress
Aliases:
Accepted values: NonVirtualized, Provider, Customer

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NewAddressSpace
Specifies the name of the new address space for the IP addresses.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NewIPAddress
Specifies an IP address.
The cmdlet assigns the new IP address to the IP addresses.

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NewManagedByService
Specifies a new value for the service that manages the IP addresses.
The value that you specify for this parameter must exist in the set of values that you defined for the **ManagedByService** custom field in IPAM.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NewNetworkType
Specifies a new value for network type for the IP addresses.
You can change the network type from NonVirtualized to Provider, and from Provider to NonVirtualized.
You cannot be change the network type from NonVirtualized or Provider to Customer.

```yaml
Type: VirtualizationType
Parameter Sets: (All)
Aliases:
Accepted values: NonVirtualized, Provider

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NewServiceInstance
Specifies a new value for the instance of the service that manages the IP addresses.
The value that you specify for this parameter must exist in the set of values that you defined for the **ServiceInstance** custom field in IPAM.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Owner
Specifies the name of the owner of the IP addresses.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
Returns an object representing the item with which you are working.
By default, this cmdlet does not generate any output.

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

### -RemoveCustomConfiguration
Specifies a semi-colon (;) separated string of custom field names.
The cmdlet removes the custom field names from the IP addresses.

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

### -ReservationDescription
Specifies a description for the DHCP reservation.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReservationName
Specifies the name of the reservation on the DHCP server for the device.
You must specify a value for this parameter if you specify the *ReservationServer* parameter.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReservationServer
Specifies the DHCP server on which the reservation is assigned.
The cmdlet stores the reservation data in IPAM.
The cmdlet does not create a reservation on the DHCP server.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReservationType
Specifies the protocols supported by the reservation.
You must specify a value for this parameter if you specify the *ReservationServer* parameter.

此参数的可接受值为：

- DHCP
- BootPr
- DHCP and BootPr

```yaml
Type: DhcpReservationType
Parameter Sets: (All)
Aliases:
Accepted values: None, Dhcp, Bootp, Both

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReverseLookupPrimaryServer
Specifies the DNS server that IPAM uses to resolve IP addresses to host names.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReverseLookupZone
Specifies the reverse lookup zone that contains mapping from IP addresses to fully qualified domain names (FQDN).

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SerialNumber
Specifies the serial number of the device to which you assigned the address.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ServiceInstance
指定一组用于管理 IP 地址的服务实例。这些服务实例应该是您为 *ManagedByService* 参数所指定的那些服务实例。如果您指定了这个参数，那么就必须同时指定 *IpAddress* 参数。您为该参数指定的值必须存在于您为 *ServiceInstance* 参数定义的数值集合中。

```yaml
Type: String[]
Parameter Sets: ByAddress
Aliases: SI

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时建立的、用于执行该cmdlet的操作的最大数量。如果省略此参数或输入值为`0`，那么Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。此限制仅适用于当前的cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamAddress
这个cmdlet返回一个对象，该对象代表IPAM服务器上的一个IP地址。

## 备注

## 相关链接

[Get-IpamAddress](./Get-IpamAddress.md)

[Add-IpamAddress](./Add-IpamAddress.md)

[Remove-IpamAddress](./Remove-IpamAddress.md)

[Import-IpamAddress](./Import-IpamAddress.md)

[Export-IpamAddress](./Export-IpamAddress.md)

