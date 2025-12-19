---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamSubnet.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/add-ipamsubnet?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-IpamSubnet
---

# Add-IpamSubnet

## 摘要
向 IPAM（IP 地址管理）中添加一个子网。

## 语法

```
Add-IpamSubnet [-Name] <String> [-NetworkId] <String> [-NetworkType <VirtualizationType>]
 [-AddressSpace <String>] [-Owner <String>] [-Description <String>] [-VlanId <UInt16[]>]
 [-VmmLogicalNetwork <String>] [-NetworkSite <String>] [-VirtualSubnetId <UInt32>]
 [-CustomConfiguration <String>] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Add-IpamSubnet** cmdlet 可用于将 IP 子网添加到 IP 地址管理（IPAM）服务器中。使用此 cmdlet 可在 IPAM 中添加非虚拟化（NonVirtualized）、提供商（Provider）或客户（Customer）类型的 IP 子网。如果要添加的子网属于提供商或非虚拟化类型，除非指定了特定的地址空间，否则该子网将被添加到默认地址空间中；如果子网属于客户类型，则必须指定相应的地址空间。

您可以将虚拟化的子网（无论是供应商提供的还是客户自己的）与逻辑网络和网络站点关联起来。这些属性代表了对物理网络的抽象，并且会被所有映射到该子网的IP地址范围所继承。

## 示例

### 示例 1：添加一个子网
```
PS C:\> Add-IpamSubnet -Name "Contoso_2" -NetworkId "10.12.0.0/16" -VlanId 13,10 -PassThru
Name                 : Contoso_2

NetworkId            : 10.12.0.0/16

NetworkType          : NonVirtualized

Overlapping          : False

NetworkSite          :

VmmLogicalNetwork    :

ProviderAddressSpace : Default

CustomerAddressSpace :

VlanId               : {13, 10}

Owner                :
```

此命令将一个名为“Contoso_2”的IPv4子网添加到网络ID 10.12.0.0/16中，并将其与VLAN 13、10关联起来。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

#### 示例 2：向默认地址空间中添加一个子网
```
PS C:\> Add-IpamSubnet -Name "Contoso_3" -NetworkId "10.13.0.0/16" -NetworkType Provider -VmmLogicalNetwork Storage -NetworkSite "Site03" -VlanId 13,10 -PassThru

Name                 : Contoso_3

NetworkId            : 10.13.0.0/16

NetworkType          : Provider

Overlapping          : False

NetworkSite          : Site03

VmmLogicalNetwork    : Storage

ProviderAddressSpace : Default

CustomerAddressSpace :

VlanId               : {13, 10}

Owner                :
```

该命令将一个名为“Contoso_3”的IPv4子网添加到默认地址空间中，同时将该子网的类型设置为“provider”。此外，该命令还将这个IPv4子网添加到网络ID为10.13.0.0/16的范围内，并将NetworkSite名称设置为“Site03”。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

### 示例 3：为某种客户网络类型添加一个子网
```
PS C:\> Add-IpamSubnet -Name "Contoso_4" -NetworkId "10.13.0.0/16" -NetworkType Customer -AddressSpace "NetCat" -VmmLogicalNetwork Storage -NetworkSite "Site03 -VirtualSubnetId 10 -PassThru
Name                 : Contoso_4

NetworkId            : 10.13.0.0/16

NetworkType          : Customer

Overlapping          : False

NetworkSite          : Site03

VmmLogicalNetwork    : Storage

ProviderAddressSpace : ContosoDatacenter

CustomerAddressSpace : NetCat

VlanId               : {13, 10}

Owner                :
```

此命令添加了一个名为 Contoso_4 的 IPv4 子网，其网络地址范围为 10.13.0.0/16（前缀为 /16），网络类型为 customer。同时，该命令还将地址空间设置为 NetCat，并将网络站点指定为 Site03。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

### 示例 4：添加一个子网并附加元数据
```
PS C:\> Add-IpamSubnet -Name "Contosov6_10" -NetworkId 2001:db8::ff00/120 -CustomConfiguration "Country=United States;ADSite=Site01" | Format-List Name, NetworkId, Overlapping, CustomConfiguration
Name                : Contosov6_10

NetworkId           : 2001:db8::ff00/120

Overlapping         : False

CustomConfiguration : Country=United States;ADSite=Site01;
```

此命令创建了名为 Contosov6_10 的物理子网，并将 Active Directory （AD）站点元数据附加到这些子网上。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

## 参数

### -AddressSpace
指定该 IP 地址子网所属的地址空间。如果您未指定地址空间，此 cmdlet 将检索 IPAM 中配置的所有地址空间的数据。

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
将此cmdlet作为后台作业运行。使用该参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中执行其他操作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
在运行cmdlet之前会提示您进行确认。

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
指定用分号（;）分隔的名称/值对。此参数用于指定与地址空间关联的自定义元数据。

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
指定子网的描述信息。

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

### -Name
为子网指定一个名称。

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

### -NetworkId
指定给定子网的网络地址和前缀。请使用无类别域间路由（CIDR）表示法来指定网络ID，格式为“Network/Prefix”。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetworkSite
指定一个与逻辑网络相关联的网络站点，该站点构成了物理网络的抽象表示。一个逻辑网络可以包含多个网络站点。此属性会被与该子网相关的所有地址范围继承。

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

### -NetworkType
指定要添加的地址所对应的网络类型数组。该参数的可接受值包括：

- Provider
- Customer
- NonVirtualized

 If the value of the *AddressSpace* parameter is Default, then this parameter can take the value Provider or NonVirtualized.
If the value of the *AddressSpace* parameter is Provider, then the value of this parameter, if specified, must be Provider.
Specifying any other value for this parameter will result in an error.
Similarly, if the value of the *AddressSpace* parameter is Customer, then the value of this parameter, if specified, must be Customer.
Specifying any other value for this parameter will result in an error.

If you do not specify this parameter, the network type defaults to NonVirtualized.

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
指定子网的拥有者名称。

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
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不生成任何输出。

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

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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

### -VirtualSubnetId
指定一个虚拟子网ID。在使用网络虚拟化技术时，该属性会与客户地址（Customer Address）和提供商地址（Provider Address）一起被用来将数据包路由到特定的客户虚拟机（Customer Virtual Machine）。

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

### -VlanId
指定一组用于虚拟局域网（VLAN）的唯一标识符。

```yaml
Type: UInt16[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -VmmLogicalNetwork
用于指定物理网络的抽象层，该抽象层描述了环境中特定功能（例如后端或前端）的实现方式。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

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

### CimInstance#ROOT/microsoft/ipam/MSFT_IPAM_SUBnet
此cmdlet返回一个对象，该对象代表IPAM服务器中的一个IP子网。

## 备注

## 相关链接

[Export-IpamSubnet](./Export-IpamSubnet.md)

[Get-IpamSubnet](./Get-IpamSubnet.md)

[Import-IpamSubnet](./Import-IpamSubnet.md)

[Remove-IpamSubnet](./Remove-IpamSubnet.md)

[Set-IpamSubnet](./Set-IpamSubnet.md)

