---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamRange.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/set-ipamrange?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IpamRange
---

# 设置 IPAM 范围

## 摘要
修改现有的IP地址范围。

## 语法

### 查询（cdxml）（默认设置）
```
Set-IpamRange [-StartIPAddress] <IPAddress[]> [-EndIPAddress] <IPAddress[]> [-ManagedByService <String[]>]
 [-ServiceInstance <String[]>] [-NetworkType <VirtualizationType[]>] [-AddressSpace <String[]>]
 [-CreateSubnetIfNotFound] [-NewNetworkId <String>] [-NewStartIPAddress <IPAddress>]
 [-NewEndIPAddress <IPAddress>] [-NewManagedByService <String>] [-NewServiceInstance <String>]
 [-NewNetworkType <VirtualizationType>] [-NewAddressSpace <String>] [-AssignmentType <AddressAssignment>]
 [-AssignmentDate <DateTime>] [-UtilizationCalculation <UtilizationCalculation>] [-UtilizedAddresses <Double>]
 [-Description <String>] [-Owner <String>] [-ReservedAddress <String[]>] [-DnsServer <IPAddress[]>]
 [-DnsSuffix <String[]>] [-ConnectionSpecificDnsSuffix <String>] [-WinsServer <IPAddress[]>] [-VIP <String[]>]
 [-Gateway <String[]>] [-AddCustomConfiguration <String>] [-RemoveCustomConfiguration <String>]
 [-AssociatedReverseLookupZone <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-IpamRange -InputObject <CimInstance[]> [-CreateSubnetIfNotFound] [-NewNetworkId <String>]
 [-NewStartIPAddress <IPAddress>] [-NewEndIPAddress <IPAddress>] [-NewManagedByService <String>]
 [-NewServiceInstance <String>] [-NewNetworkType <VirtualizationType>] [-NewAddressSpace <String>]
 [-AssignmentType <AddressAssignment>] [-AssignmentDate <DateTime>]
 [-UtilizationCalculation <UtilizationCalculation>] [-UtilizedAddresses <Double>] [-Description <String>]
 [-Owner <String>] [-ReservedAddress <String[]>] [-DnsServer <IPAddress[]>] [-DnsSuffix <String[]>]
 [-ConnectionSpecificDnsSuffix <String>] [-WinsServer <IPAddress[]>] [-VIP <String[]>] [-Gateway <String[]>]
 [-AddCustomConfiguration <String>] [-RemoveCustomConfiguration <String>]
 [-AssociatedReverseLookupZone <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-IpamRange` cmdlet 用于修改由 IP 地址管理（IPAM）服务器管理的现有 IP 地址范围。

## 示例

### 示例 1：修改现有的 IP 地址范围
```
PS C:\> Get-IpamRange -StartIPAddress 10.12.1.1 -EndIPAddress 10.12.1.254|Set-IpamRange -NewManagedByService VMM -NewServiceInstance "vmm1.contoso.com" -PassThru

Overlapping      : False

NetworkID        : 10.12.0.0/16

StartAddress     : 10.12.1.1

EndAddress       : 10.12.1.254

ManagedByService : VMM

ServiceInstance  : vmm1.contoso.com

NetworkType      : NonVirtualized

Owner            :
```

此命令用于将当前由 IPAM 管理的现有 IP 地址范围更改为由虚拟机管理器（VMM）进行管理。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

### 示例 2：为某个 IP 地址范围添加自定义元数据
```
PS C:\> Get-IpamRange -StartIPAddress 10.12.1.1 -EndIPAddress 10.12.1.254|Set-IpamRange -AddCustomConfiguration "ADSite=ContosoCorporate" -PassThru| Format-List Overlapping, StartAddress, EndAddress, ManagedByService, ServiceInstance, CustomConfiguration

Overlapping         : False

StartAddress        : 10.12.1.1

EndAddress          : 10.12.1.254

ManagedByService    : VMM

ServiceInstance     : vmm1.contoso.com

CustomConfiguration : ADSite= ContosoCorporate;
```

该命令通过使用自定义字段来标识位置，从而为某个IP范围添加自定义元数据。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

### 示例 3：修改某个 IP 地址范围的网络类型
```
PS C:\> Set-IpamRange -StartIPAddress 10.12.3.1 -EndIPAddress 10.12.3.254 -ManagedByService IPAM -ServiceInstance localhost -AddressSpace "Default" -NetworkType NonVirtualized -NewNetworkType Provider -PassThru

Overlapping      : False

NetworkID        : 10.12.0.0/16

StartAddress     : 10.12.3.1

EndAddress       : 10.12.3.254

ManagedByService : IPAM

ServiceInstance  : Localhost

NetworkType      : Provider

Owner            :
```

此命令将一个IP地址范围的网络类型从“非虚拟化”修改为“供应商（provider）”类型。默认情况下，该IP地址范围会被分配到默认的供应商地址空间中。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

### 示例 4：将某个 IP 地址范围的网络类型修改回其之前的状态
```
PS C:\> Set-IpamRange -StartIPAddress 10.12.3.1 -EndIPAddress 10.12.3.254 -ManagedByService IPAM -ServiceInstance localhost -AddressSpace Default -NetworkType Provider -NewNetworkType NonVirtualized -PassThru

Overlapping      : False

NetworkID        : 10.12.0.0/16

StartAddress     : 10.12.3.1

EndAddress       : 10.12.3.254

ManagedByService : IPAM

ServiceInstance  : Localhost

NetworkType      : NonVirtualized

Owner            :
```

此命令会将一个IP地址范围的网络类型从“provider”修改为“non-virtualized”。修改后的非虚拟化地址范围将被添加到默认地址空间中。在这种情况下，您无法指定相应的提供商地址空间。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

### 示例 5：修改某个 IP 地址范围的网络类型，并分配相应的 IP 地址
```
PS C:\> Set-IpamRange -StartIPAddress 10.12.3.1 -EndIPAddress 10.12.3.254 -ManagedByService IPAM -ServiceInstance localhost -AddressSpace Default -NetworkType NonVirtualized -NewNetworkType Provider -NewAddressSpace ContosoDataCenter -PassThru | Format-List IpAddress, NetworkType, ProviderAddressSpace, CustomerAddressSpace
Overlapping       : False

NetworkID         : 10.12.0.0/16

StartAddress      : 10.12.3.1

EndAddress        : 10.12.3.254

ManagedByService  : IPAM

ServiceInstance   : Localhost

NetworkType       : Provider

ProviderAddressSpace : ContosoDataCenter

CustomerAddressSpace :
```

此命令将某个IP地址的网络类型从“非虚拟化”更改为“提供商网络类型”，并将该IP地址分配到ContosoDataCenter这个提供商的地址空间中。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

## 参数

### -AddCustomConfiguration
指定用分号（;）分隔的名/值对。该参数用于定义与地址空间关联的自定义元数据。

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
指定一个地址空间名称的数组。如果您没有指定值，该cmdlet将修改来自所有地址空间的匹配范围。

```yaml
Type: String[]
Parameter Sets: Query (cdxml)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -AssignmentDate
指定用于分配此范围内地址的日期。

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
指定从这个范围内选择的地址分配类型。

此参数的可接受值包括：

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

### -AssociatedReverseLookupZone


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

### -CimSession
Runs the cmdlet in a remote session or on a remote computer.
Enter a computer name or a session object, such as the output of a [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) or [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet.
The default is the current session on the local computer.

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

### -Confirm
Prompts you for confirmation before running the cmdlet.

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

### -ConnectionSpecificDnsSuffix
Specifies the connection-specific DNS suffix to associate with this range.

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

### -CreateSubnetIfNotFound
Indicates that the cmdlet creates a parent subnet for this range of addresses.
If you specify this parameter, the cmdlet automatically creates a parent subnet for this range, if no parent subnet exists.

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

### -Description
Specifies a description for the range to modify.

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

### -DnsServer
Specifies an array of Domain Name System (DNS) servers to associate with this range.
Specify the names of the DNS servers in the order of preference, highest to lowest.

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DnsSuffix
Specifies an array of suffixes.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EndIPAddress
Specifies an array of IP addresses.
For this parameter, the addresses represent the high end of the range to modify.

```yaml
Type: IPAddress[]
Parameter Sets: Query (cdxml)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Gateway
Specifies an array of gateway servers, imported from a Dynamic Host Configuration Protocol (DHCP) scope, to associate with a range in IPAM.
Specify the names of the gateway servers in the order of preference, highest to lowest.
The format for specification is \<ipaddress\>\\\<metric\>.
To specify Automatic metric, the format is \<Ipaddress\>\Automatic.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InputObject
Specifies the input to this cmdlet.
You can use this parameter, or you can pipe the input to this cmdlet.

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

### -ManagedByService
Specifies an array of services that manage the range to modify.

```yaml
Type: String[]
Parameter Sets: Query (cdxml)
Aliases: MB

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetworkType
Specifies an array of network types for the addresses to modify.

此参数的可接受值包括：

- Provider
- Customer
- NonVirtualized

If you do not specify a value, the cmdlet modifies all matching IP address ranges of network type Provider, Customer, and NonVirtualized.

```yaml
Type: VirtualizationType[]
Parameter Sets: Query (cdxml)
Aliases:
Accepted values: NonVirtualized, Provider, Customer

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NewAddressSpace
Specifies the name of a new address space for the IP address range.
A range with network type NonVirtualized can only belong to Default address space.
A range with network type Provider can belong to either the Default address space or a Provider address space.
A range with network type Customer can only belong to a Customer address space.

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

### -NewEndIPAddress
Specifies a new IP address.
For this parameter, the address represents the new high end of the range.
An error occurs if the value is not compatible with the network ID and the starting IP address.

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
Specifies the name of a new value of the **ManagedByService** property.

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

### -NewNetworkId
Specifies the name of a new value of the **NetworkId** property.
Choose a value compatible with the existing beginning and ending IP addresses for the range, or specify new values for starting and ending IP addresses.

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
Specifies the name of a new value of network type for this address.
You can change the network type from NonVirtualized to Provider, or from Provider to NonVirtualized.
However, you cannot convert network type from NonVirtualized or Provider to Customer.

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
Specifies the name of a new value of the service instance property.
Choose a new value compatible with the value of *ManagedByService* parameter.

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

### -NewStartIPAddress
Specifies a new IP address.
For this parameter, the address represents the new low end of the range.
An error occurs if the value is not compatible with the network ID and the ending IP address.

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

### -Owner
Specifies the name of an owner for an address range.

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
Specifies a list of custom metadata fields to remove from the range object.
The list is a string of name-value pairs, separated by semicolons (;).

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

### -ReservedAddress
Specifies an array of reserved addresses from the given range.
This list will overwrite the existing list of reserved addresses for the given range.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ServiceInstance
Specifies an array of service instances that manage the address ranges to modify.

```yaml
Type: String[]
Parameter Sets: Query (cdxml)
Aliases: SI

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StartIPAddress
Specifies an array of IP addresses.
For this parameter, the addresses represent the low end of the range to modify.

```yaml
Type: IPAddress[]
Parameter Sets: Query (cdxml)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
Specifies the maximum number of concurrent operations that can be established to run the cmdlet.
If this parameter is omitted or a value of `0` is entered, then Windows PowerShell® calculates an optimum throttle limit for the cmdlet based on the number of CIM cmdlets that are running on the computer.
The throttle limit applies only to the current cmdlet, not to the session or to the computer.

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

### -UtilizationCalculation
Specifies whether the utilization information will be automatically calculated by IPAM or specified by the user.
The utilization calculation provides a visual alert when the utilization level of IP addresses is greater than a threshold value.

```yaml
Type: UtilizationCalculation
Parameter Sets: (All)
Aliases:
Accepted values: Auto, UserSpecified

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -UtilizedAddresses
Specifies the number of addresses to utilize from the pool of IP addresses.
Use this parameter when the utilization calculation is set to the value in **UserSpecified**.

```yaml
Type: Double
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -VIP
Specifies an array of virtual IP addresses, usually set aside for load balancers, from the range.
Specify the Virtual IPs (VIP) as a list, in descending order of precedence.
This list overwrites any existing VIPs specified for the given range.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
Shows what would happen if the cmdlet runs.
The cmdlet is not run.

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

### -WinsServer
Specifies an array of Windows Internet Name Service (WINS) servers to associate with this range.
Specify the WINS servers in decreasing order of precedence.
This list overwrites any existing list of WINS servers.

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### CimInstance#ROOT/microsoft/ipam/MSFT_IPAM_Range
此cmdlet返回一个对象，其中包含修改后的IP地址范围。

## 备注

## 相关链接

[Add-IpamRange](./Add-IpamRange.md)

[Export-IpamRange](./Export-IpamRange.md)

[Get-IpamRange](./Get-IpamRange.md)

[Import-IpamRange](./Import-IpamRange.md)

[Remove-IpamRange](./Remove-IpamRange.md)

