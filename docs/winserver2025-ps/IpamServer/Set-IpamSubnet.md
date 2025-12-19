---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamSubnet.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/set-ipamsubnet?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IpamSubnet
---

# 设置 Ipam 子网

## 摘要
在 IPAM 中修改现有的 IP 子网。

## 语法

### 查询（CDXML）（默认值）
```
Set-IpamSubnet -NetworkId <String[]> [-NetworkType <VirtualizationType[]>] [-AddressSpace <String[]>]
 [-NewNetworkId <String>] [-NewNetworkType <VirtualizationType>] [-NewAddressSpace <String>] [-Name <String>]
 [-Owner <String>] [-Description <String>] [-VlanId <UInt16[]>] [-VmmLogicalNetwork <String>]
 [-NetworkSite <String>] [-VirtualSubnetId <Int32>] [-AddCustomConfiguration <String>]
 [-RemoveCustomConfiguration <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-IpamSubnet -InputObject <CimInstance[]> [-NewNetworkId <String>] [-NewNetworkType <VirtualizationType>]
 [-NewAddressSpace <String>] [-Name <String>] [-Owner <String>] [-Description <String>] [-VlanId <UInt16[]>]
 [-VmmLogicalNetwork <String>] [-NetworkSite <String>] [-VirtualSubnetId <Int32>]
 [-AddCustomConfiguration <String>] [-RemoveCustomConfiguration <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-IpamSubnet` cmdlet 用于修改 IP 地址管理（IPAM）中现有的 IP 子网。

## 示例

### 示例 1：为子网添加元数据
```
PS C:\> Get-IpamSubnet -AddressFamily IPv4|where {$_.Name -Like "Site*"}|Set-IpamSubnet -AddCustomConfiguration "ADSite=Site01" -PassThru | Format-List Name, NetworkId, CustomConfiguration

Name                : Site01_1

NetworkId           : 20.20.128.0/24

CustomConfiguration : ADSite=Site01; Name                : Site01_2

NetworkId           : 10.20.1.0/24

CustomConfiguration : ADSite=Site01;
Name                : Site01_3

NetworkId           : 10.20.2.0/24

CustomConfiguration : ADSite=Site01;
Name                : Site01_4

NetworkId           : 10.20.4.0/24

CustomConfiguration : ADSite=Site01;
Name                : Site01_5

NetworkId           : 10.20.8.0/24

CustomConfiguration : ADSite=Site01;
```

此命令将 ADSite 信息作为元数据添加到所有分配给 Site01 的子网中。

该命令包含了 *PassThru* 参数，因此它会将结果显示在控制台中。

### 示例 2：修改网络ID
```
PS C:\> Set-IpamSubnet -NetworkId 10.10.1.0/16 -NetworkType NonVirtualized -NewNetworkId 10.10.1.0/17
```

此命令用于修改子网的“非虚拟化”网络ID（NonVirtualized Network ID）。

### 示例 3：重命名子网
```
PS C:\> Set-IpamSubnet -NetworkId 10.10.1.0/17 -Name "Site01_2"
```

此命令将一个子网重命名为Site01_2。

### 示例 4：将网络类型转换为提供商类型
```
PS C:\> Set-IpamSubnet -NetworkId 10.10.1.0/17 -NetworkType NonVirtualized -NewNetworkType Provider
```

此命令将子网的网络类型从“NonVirtualized”转换为“Provider”。默认情况下，该子网将被分配到默认的提供商地址空间中。

### 示例 5：将网络类型转换为非虚拟化类型
```
PS C:\> Set-IpamSubnet -NetworkId 10.10.1.0/17 -NetworkType Provider -NewNetworkType NonVirtualized
```

此命令将子网的网络类型从“Provider”转换为“NonVirtualized”。

### 示例 6：转换网络类型，并将其分配给提供商的地址空间
```
PS C:\> Set-IpamSubnet -NetworkId 10.10.1.0/17 -NetworkType NonVirtualized -NewNetworkType Provider -NewAddressSpace ContosoDataCenter
```

此命令将子网的网络类型从“非虚拟化”（NonVirtualized）修改为“提供者”（Provider），并将该子网分配到提供商地址空间“ContosoDataCenter”。

## 参数

### -AddCustomConfiguration
指定用分号（;）分隔的名/值对。此参数用于定义与地址空间相关联的自定义元数据。

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
指定该 IP 地址范围所属的地址空间数组。如果您不指定任何值，此 cmdlet 将修改所有地址空间中符合条件的地址范围。

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
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
为子网指定一个描述信息。

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

### -InputObject
指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给此 cmdlet。

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

### -Name
指定子网的名称。

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

### -NetworkId
指定给定子网的网络地址和前缀。请使用无类别域间路由（CIDR）表示法来指定网络ID，格式为“Network/Prefix”。

```yaml
Type: String[]
Parameter Sets: Query (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetworkSite
用于指定一个网络站点。网络站点与逻辑网络相关联，并构成了物理网络的抽象表示。一个逻辑网络可以包含多个网络站点。与该子网关联的所有范围和地址都会继承此属性。

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
指定一个网络类型数组，用于修改相应的子网。

此参数的可接受值为：

- Provider
 --  Customer
 --  NonVirtualized

如果您没有指定具体的值，那么所有类型为“Provider”、“Customer”和“NonVirtualized”的匹配 IP 子网都将被修改。

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
指定用于该 IP 子网的新地址空间的名称。非虚拟化（NonVirtualized）类型的网络子网只能属于默认地址空间（Default address space）。提供者类型（Provider）的网络子网可以属于默认地址空间或提供者地址空间（Provider address space）。客户类型（Customer）的网络子网只能属于客户地址空间（Customer address space）。

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
为这个子网指定一个新的网络ID值的名称。

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
指定此地址的新网络类型的名称。您可以将网络类型从“NonVirtualized”更改为“Provider”，或从“Provider”更改为“NonVirtualized”。但是，您不能将网络类型从“NonVirtualized”或“Provider”更改为“Customer”。

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

### -Owner
为子网指定一个所有者。

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

### -RemoveCustomConfiguration
指定一个需要修改的自定义元数据字段列表。该列表由名称-值对组成，各对之间用分号（;）分隔。

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

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前正在运行的 cmdlet，而不适用于整个会话或计算机本身。

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
指定一个虚拟子网的ID。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -VlanId
用于指定虚拟局域网（VLAN）的唯一标识符数组。

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
用于指定物理网络的抽象层，该抽象层描述了环境中某个特定功能（例如后端或前端服务）。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

### IpamSubnet
这个cmdlet返回一个对象，该对象表示IPAM服务器中的一个子网。

## 备注
* When converting the network type of a subnet from Provider to NonVirtualized, the address space of  the subnet is reset to Default.

## 相关链接

[Add-IpamSubnet](./Add-IpamSubnet.md)

[Export-IpamSubnet](./Export-IpamSubnet.md)

[Get-IpamSubnet](./Get-IpamSubnet.md)

[Import-IpamSubnet](./Import-IpamSubnet.md)

[Remove-IpamSubnet](./Remove-IpamSubnet.md)

