---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamRange.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/add-ipamrange?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-IpamRange
---

# Add-IpamRange

## 摘要
将一个 IP 地址范围添加到 IPAM 服务器的配置中。

## 语法

```
Add-IpamRange [-CreateSubnetIfNotFound] [-NetworkId] <String> [[-StartIPAddress] <IPAddress>]
 [[-EndIPAddress] <IPAddress>] [-ManagedByService <String>] [-ServiceInstance <String>]
 [-NetworkType <VirtualizationType>] [-AddressSpace <String>]
 [-UtilizationCalculation <UtilizationCalculation>] [-UtilizedAddresses <Double>] [-Description <String>]
 [-Owner <String>] [-AssignmentType <AddressAssignment>] [-AssignmentDate <DateTime>]
 [-ReservedAddress <String[]>] [-DnsServer <IPAddress[]>] [-DnsSuffix <String[]>]
 [-ConnectionSpecificDnsSuffix <String>] [-WinsServer <IPAddress[]>] [-VIP <String[]>] [-Gateway <String[]>]
 [-CustomConfiguration <String>] [-AssociatedReverseLookupZone <String>] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-IpamRange` cmdlet 用于将一个 IP 地址范围添加到 IP 地址管理（IPAM）服务器的配置中。您可以使用此 cmdlet 在 IPAM 中添加非虚拟化、供应商或客户类型的 IP 地址范围。如果网络类型为供应商或非虚拟化类型，并且未指定地址空间，则该地址范围将自动添加到默认地址空间中；如果网络类型为客户类型，则必须指定一个地址空间。

## 示例

### 示例 1：添加一个 IP 地址范围
```
PS C:\> Add-IpamRange -NetworkId "10.13.0.0/16" -PassThru
Overlapping      : False

NetworkID        : 10.13.0.0/16

StartAddress     : 10.13.0.1

EndAddress       : 10.13.255.254

ManagedByService : IPAM

ServiceInstance  : Localhost

NetworkType      : NonVirtualized

Owner            :
```

此命令添加了一个由当前IPAM服务器实例管理的IP地址范围。该地址范围会被添加到默认的地址空间中。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

### 示例 2：使用网络 ID 添加 IP 地址范围
```
PS C:\> Add-IpamRange -NetworkId "172.16.10.0/24"
Add-IpamRange : No subnet exists corresponding to the range.

At line:1 char:1

+ Add-IpamRange -NetworkId 172.16.10.0/24

+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+ CategoryInfo          : ResourceUnavailable: (MSFT_IPAM_Range:ROOT/microsoft/ipam/MSFT_IPAM_Range) [Add-IpamRang

e], CimException

+ FullyQualifiedErrorId : WIN32 8,Add-IpamRange
```

该命令添加了一个IP地址范围，其网络ID为172.16.10.0/24。IPAM不允许创建一个不存在相应子网的IP地址范围。

### 示例 3：使用网络 ID 添加 IP 地址范围并创建子网
```
PS C:\> Add-IpamRange -NetworkId "172.16.10.0/24" -CreateSubnetIfNotFound -WinsServer "10.10.1.1","10.10.1.2" -Gateway "10.10.5.1/Automatic","10.10.5.2/4"|Format-List Overlapping, NetworkID, StartAddress, EndAddress, ManagedByService, ServiceInstance, WinsServers, Gateway
Overlapping      : False

NetworkID        : 172.16.10.0/24

StartAddress     : 172.16.10.1

EndAddress       : 172.16.10.254

ManagedByService : IPAM

ServiceInstance  : Localhost

WinsServers      : {10.10.1.1, 10.10.1.2}

Gateway          : {10.10.5.1/Automatic, 10.10.5.2/4}
```

这个命令用于添加一个 IP 地址范围，其网络 ID 为 172.16.10.0/24。该命令使用了 *CreateSubnetIfNotFound* 参数来自动创建相应的子网，并向该地址范围内添加 WINS 和网关服务器。网关服务器的格式为 \<IP 地址\>/\<指标\>。

### 示例 4：向现有的 IPAM 配置中添加提供商 IP 地址范围
```
PS C:\> Add-IpamRange -NetworkId 172.16.19.0/24 -StartIPAddress 172.16.19.10 -EndIPAddress 172.16.19.110 -NetworkType Provider -CreateSubnetIfNotFound -PassThru
Overlapping      : False

NetworkID        : 172.16.19.0/24

StartAddress     : 172.16.19.10

EndAddress       : 172.16.19.110

ManagedByService : IPAM

ServiceInstance  : Localhost

NetworkType      : Provider

Owner            :
```

此命令添加了一个由当前IPAM实例管理的提供商IP地址范围。该地址范围将被添加到默认地址空间中。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

### 示例 5：添加一系列提供商的 IP 地址
```
PS C:\> Add-IpamRange -NetworkId 172.16.19.0/24 -StartIPAddress 172.16.19.10 -EndIPAddress 172.16.19.110 -NetworkType Provider -AddressSpace ContosoDataCenter -PassThru -CreateSubnetIfNotFound
Overlapping      : False

NetworkID        : 172.16.19.0/24

StartAddress     : 172.16.19.10

EndAddress       : 172.16.19.110

ManagedByService : IPAM

ServiceInstance  : Localhost

NetworkType      : Provider

Owner            :
```

此命令添加了一个提供者IP地址范围（172.16.19.0/24），其起始地址为172.16.19.10，结束地址为172.16.19.110。该地址范围被添加到一个名为“ContosoDataCenter”的提供者地址空间中。由于这个地址范围属于不同的地址空间，IPAM系统不会将其标记为与现有地址范围重叠。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

## 参数

### -AddressSpace
指定该 IP 地址范围所属的地址空间。一个地址空间包含 IP 子网、IP 范围和 IP 地址。如果未指定此参数，则使用默认地址空间。默认地址空间是提供商提供的地址空间。

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
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
指定一个日期，在该日期将地址分配到这个范围内。

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
指定 IPAM 如何分配地址。此参数的可接受值为：

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

### -CustomConfiguration
Specifies semicolon-separated name/value pairs.
This parameter specifies custom metadata that is associated with the address space.

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
Specifies a description for the range.

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
Specifies an array of DNS servers to associate with this range.
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
Specifies an array of search suffixes to associate with the given range.

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
Specifies an IP address.
For this parameter, the address represents the high end of the range to add.

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Gateway
Specifies an array of gateway servers, imported from a DHCP Scope, to associate with a range in IPAM.
Specify the names of the gateway servers in the order of preference, highest to lowest.
The format for specification is \<ipaddress\>\\\<metric\>.
To specify the Automatic metric, use the format \<Ipaddress\>\Automatic.

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

### -ManagedByService
Specifies the value of the managing service of the IP address ranges being added.

```yaml
Type: String
Parameter Sets: (All)
Aliases: MB

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetworkId
Specifies the network and the prefix for the given range.
Specify the network ID in Classless Interdomain Routing (CIDR) notation in the format Network/Prefix.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetworkType
Specifies an array of network types for the addresses to be added.
The acceptable values for this parameter are:

- Provider
- Customer
- NonVirtualized

 If the value of the *AddressSpace* parameter is Default, then this parameter can use the value Provider or NonVirtualized.
If the value of the *AddressSpace* parameter is Provider, then the value of this parameter, if specified, must be Provider.
Specifying any other value for this parameter will result in an error.
Similarly, if the value of the *AddressSpace* parameter is Customer, then the value of this parameter, if specified, must be Customer.
Specifying any other value for this parameter will result in an error.

If you do not specify this parameter, network type defaults to NonVirtualized.

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

### -ReservedAddress
Specifies the reserved addresses in the range.
Specify the reserved addresses as a list, in descending order of precedence.

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
Specifies the service instance that manages the address ranges to add.
The value specified for this field should be present in the set of values defined for the ServiceInstance custom field in IPAM.
The cmdlet will report an error if this is not found to be a valid value for the ServiceInstance custom field.
The user can edit the associated custom field to add or delete values.

```yaml
Type: String
Parameter Sets: (All)
Aliases: SI

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StartIPAddress
Specifies an IP address.
For this parameter, the address represents the low end of the range to add.

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
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
Specifies the utilization information type that will be automatically calculated by IPAM or specified by the user.

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
Specifies an array of virtual IP addresses that are usually set aside for load balancers.
Specify the VIPs as a list, in descending order of precedence.

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### CimInstance#ROOT/microsoft/ipam/MSFT_IPAM_Range
此cmdlet返回添加到IPAM数据存储中的IP地址范围对象。

## 备注

## 相关链接

[Export-IpamRange](./Export-IpamRange.md)

[Get-IpamRange](./Get-IpamRange.md)

[Import-IpamRange](./Import-IpamRange.md)

[Remove-IpamRange](./Remove-IpamRange.md)

[Set-IpamRange](./Set-IpamRange.md)

