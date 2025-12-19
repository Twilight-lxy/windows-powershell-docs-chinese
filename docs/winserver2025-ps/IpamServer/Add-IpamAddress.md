---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamAddress.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/add-ipamaddress?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-IpamAddress
---

# Add-IpamAddress

## 摘要
将一个 IP 地址添加到 IPAM（IP 地址管理）系统中。

## 语法

```
Add-IpamAddress [-IpAddress] <IPAddress> [[-ManagedByService] <String>] [[-ServiceInstance] <String>]
 [-NetworkType <VirtualizationType>] [-AddressSpace <String>] [-DeviceType <String>] [-IpAddressState <String>]
 [-AssignmentType <AddressAssignment>] [-MacAddress <String>] [-AssignmentDate <DateTime>]
 [-ExpiryDate <DateTime>] [-Description <String>] [-Owner <String>] [-AssetTag <String>]
 [-SerialNumber <String>] [-ClientId <String>] [-Duid <String>] [-Iaid <UInt32>] [-ReservationServer <String>]
 [-ReservationName <String>] [-ReservationType <DhcpReservationType>] [-ReservationDescription <String>]
 [-DeviceName <String>] [-ForwardLookupZone <String>] [-ForwardLookupPrimaryServer <String>]
 [-ReverseLookupZone <String>] [-ReverseLookupPrimaryServer <String>] [-CustomConfiguration <String>]
 [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-IpamAddress` cmdlet 用于将 IP 地址添加到 IP 地址管理（IPAM）系统中。你可以使用该 cmdlet 将动态主机配置协议（DHCP）的预留属性与相应的 IP 地址关联起来。不过，这个 cmdlet 并不会在 DHCP 服务器上创建实际的预留记录；你需要在 Windows PowerShell 中通过专门的 DHCP Server 功能来完成这一操作。

## 示例

### 示例 1：为 IPAM 服务器添加一个物理 IP 地址
```
PS C:\> Add-IpamAddress -IpAddress 10.12.3.5 -PassThru
IpAddress        : 10.12.3.5

Type             : NonVirtualized

Duplicate        : False

ExpiryStatus     : Not Expired

MacAddress       :

ManagedByService : IPAM

ServiceInstance  : Localhost

DeviceName       :

DeviceType       : Host

IpAddressState   : In-Use

AssignmentType   : Static
```

该命令将物理IP地址10.12.3.5添加到当前IPAM服务器实例所管理的默认地址空间中。该命令使用以下默认值来配置该IP地址：

- *ManagedByService* parameter uses the default value IPAM
- *ServiceInstance* parameter uses the default value Localhost
- *DeviceType* parameter uses the default value Host
- *AssignmentType* parameter uses the default value Static

### 示例 2：为虚拟机分配一个动态 IP 地址
```
PS C:\> Add-IpamAddress -IpAddress 10.12.4.9 -ManagedByService "TSQA DHCP" -ServiceInstance "dhcp1.contoso.com" -AssignmentType Dynamic -DeviceType VM -ExpiryDate $TwoWeeksFromNow -PassThru
IpAddress        : 10.12.4.9

Type             : NonVirtualized

Duplicate        : False

ExpiryStatus     : Not Expired

MacAddress       :

ManagedByService : MS DHCP

ServiceInstance  : dhcp1.contoso.com

DeviceName       :

DeviceType       : VM

IpAddressState   : In-Use

AssignmentType   : Dynamic
```

这条命令将 IP 地址 10.12.4.8 分配给一台虚拟机。同时，该命令指定了名为 dhcp1.contoso.com 的 DHCP 服务器负责管理这个地址。此外，还规定该地址将在两周后失效，届时你可以重新获取它。

### 示例 3：将提供商的 IP 地址添加到 IPAM 服务器中
```
PS C:\> Add-IpamAddress -NetworkType Provider -IpAddress 172.16.10.16 -PassThru
IpAddress         : 172.16.10.16

NetworkType       : Provider

Duplicate         : False

ExpiryStatus      : Not Expired

MacAddress        :

ManagedByService  : IPAM

ServiceInstance   : Localhost

DeviceName        :

DeviceType        : Host

IpAddressState    : In-Use

AssignmentType    : Static
```

此命令将提供商IP地址172.16.10.16（由当前IPAM实例管理）添加到默认地址空间中。

### 示例 4：添加一个由虚拟机管理器管理的提供者 IP 地址
```
PS C:\> Add-IpamAddress -IpAddress 172.16.10.16 -AddressSpace "Datacenter01" -ManagedByService VMM -ServiceInstance "vmm1.contoso.com" -PassThru
IpAddress         : 172.16.10.16

NetworkType       : Provider

Duplicate         : False

ExpiryStatus      : Not Expired

MacAddress        :

ManagedByService  : VMM

ServiceInstance   : vmm1.contoso.com

DeviceName        :

DeviceType        : Host

IpAddressState    : In-Use

AssignmentType    : Static
```

此命令添加了一个由 vmmblue_1 管理的提供者 IP 地址，该地址属于名为 “Datacenter01” 的提供者地址空间。vmmblue_2 负责静态管理地址分配工作。由于这个地址位于不同的地址空间中，IPAM 不会将其标记为重复地址。

### 示例 5：添加一个由虚拟机管理器实例管理的客户 IP 地址
```
PS C:\> Add-IpamAddress -IpAddress 172.16.10.16 -Virtual -AddressSpace "Datacenter01" -ManagedByService VMM -ServiceInstance "vmm01.contoso.com" -DeviceType VM
IpAddress         : 172.16.10.16

NetworkType       : Customer

Duplicate         : False

ExpiryStatus      : Not Expired

MacAddress        :

ManagedByService  : VMM

ServiceInstance   : vmm01.contoso.com

DeviceName        :

DeviceType        : VM

IpAddressState    : In-Use

AssignmentType    : Static
```

此命令添加了一个由 vmmblue_1 实例 vmm01.contoso.com 管理的客户 IP 地址。该地址被添加到名为 Datacenter01 的租户的客户地址空间中。

## 参数

### -AddressSpace
指定与 IP 地址关联的地址空间。默认值为 “Default”。

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

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个代表该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
指定您将 IP 地址分配给设备的日期。要获取一个 **DateTime** 对象，请使用 **Get-Date** cmdlet。有关更多信息，请输入 `Get-Help Get-Date`。

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
指定 IPAM 如何分配此地址。该参数的可接受值包括：

- Static
- Dynamic
- Auto
- VIP
- Reserved

The default value is Static.

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定客户端 的 ID。

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

### -CustomConfiguration
指定用分号分隔的名称/值对。此参数用于指定与地址关联的自定义元数据。

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

### -Description
用于指定设备IP地址分配的描述信息。

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
指定您已为其分配地址的设备名称。

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
指定您分配地址的设备类型。请选择一个存在于内置的 **DeviceType** 自定义字段中的有效值。该参数的可接受值为：

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
为客户端指定唯一的DHCP设备标识符（DUID）。客户端使用该DUID从DHCPv6服务器获取IP地址。

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
该参数用于指定IP地址的有效期限。当IP地址过期时，IPAM会向管理员发出警报。不过，IPAM不会自动回收已过期的IP地址。

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
指定 IPAM 使用的 DNS 服务器的名称，该服务器用于将主机名解析为 IP 地址。

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
指定用于存储主机名与IP地址映射关系的正向查找区域的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: FwdLookupZone

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

### -IpAddress
指定一个该cmdlet将添加到IPAM中的IP地址。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IpAddressState
指定IP地址的使用状态。默认情况下，该cmdlet会将地址设置为“正在使用”（In-Use）。您可以为此参数指定一个有效的自定义值。

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
Type: String
Parameter Sets: (All)
Aliases: MB

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetworkType
指定地址的网络类型。此参数的可接受值为：

- Provider
- Customer
- NonVirtualized

The default value is NonVirtualized.

If you specify Default for the **AddressSpace** parameter, the valid values for this parameter are Provider and NonVirtualized.
If you specify a provider type of address space for the **AddressSpace** parameter, you must specify Provider for this parameter.
If you specify a customer type of address space for the **AddressSpace** parameter, you must specify Customer for this parameter.

```yaml
Type: VirtualizationType
Parameter Sets: (All)
Aliases:
Accepted values: NonVirtualized, Provider, Customer

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Owner
指定地址所有者的名称。

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
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -ReservationDescription
为 DHCP 预留资源指定一个描述性说明。

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
指定设备在DHCP服务器上的预订名称。如果您指定了*ReservationServer*参数，则必须为该参数提供一个值。

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
指定用于分配预留地址的 DHCP 服务器。该 cmdlet 将预留数据存储在 IPAM 中，但不会在 DHCP 服务器上实际创建相应的预留记录。

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
指定预订支持的协议。如果您指定了*ReservationServer*参数，则必须为该参数指定一个值。此参数的可接受值为：

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
指定 IPAM 使用的 DNS 服务器，以便将 IP 地址解析为主机名。

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
指定用于反向查找的区域，该区域包含将 IP 地址映射到完全限定域名（FQDN）的信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases: RevLookupZone

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SerialNumber
指定与IP地址关联的设备序列号。

```yaml
Type: String
Parameter Sets: (All)
Aliases: SN

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ServiceInstance
指定用于管理 IP 地址的服务实例。请使用您为 *ManagedByService* 参数所指定的服务实例。为此参数指定的值必须存在于您在 IPAM 中为 **ServiceInstance** 自定义字段所定义的值集合中。

```yaml
Type: String
Parameter Sets: (All)
Aliases: SI

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamAddress
表示 IPAM 服务器上的一个 IP 地址。

## 备注

## 相关链接

[Get-IpamAddress](./Get-IpamAddress.md)

[Set-IpamAddress](./Set-IpamAddress.md)

[Remove-IpamAddress](./Remove-IpamAddress.md)

[Import-IpamAddress](./Import-IpamAddress.md)

[Export-IpamAddress](./Export-IpamAddress.md)

[Get-IpamCustomField](./Get-IpamCustomField.md)

[Get-IpamAddressSpace](./Get-IpamAddressSpace.md)

