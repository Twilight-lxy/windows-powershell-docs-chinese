---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamSubnet.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamsubnet?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamSubnet
---

# Get-IpamSubnet

## 摘要
从 IPAM 中获取一组子网。

## 语法

### ById
```
Get-IpamSubnet -NetworkId <String[]> [-NetworkType <VirtualizationType[]>] [-AddressSpace <String[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByAF
```
Get-IpamSubnet [-AddressFamily] <AddressFamily[]> [-NetworkType <VirtualizationType[]>]
 [-AddressSpace <String[]>] [-Unmapped] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ByBlock
```
Get-IpamSubnet -MappingToBlock <CimInstance> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-IpamSubnet` cmdlet 用于从 IP 地址管理（IPAM）系统中获取一组 IP 子网。默认情况下，该 cmdlet 会从 IPAM 配置的所有地址空间中获取指定地址家族的所有 IP 地址。您可以使用 `NetworkType` 和 `AddressSpace` 参数来过滤结果，以便仅显示属于特定提供商或客户的子网，或者仅显示非虚拟化的子网。

此cmdlet还提供了参数集，用于检索所有映射到给定IP地址块的子网。

## 示例

#### 示例 1：获取所有重叠的子网
```
PS C:\> Get-IpamSubnet -AddressFamily IPv4 -AddressSpace "Default" | where {$_.Overlapping -eq $false}
```

这个命令可以获取默认地址空间中所有重叠的子网，包括属于默认地址空间的“Provider”（提供商）子网和“NonVirtualized”（非虚拟化）子网。

### 示例 2：获取站点中所有未虚拟化的子网
```
PS C:\> Get-IpamSubnet -AddressFamily IPv4 -NetworkType NonVirtualized | where {$_.CustomConfiguration -Like "*ADSite=Contoso*"}| Format-List Name, NetworkId, CustomConfiguration
Name                : Contoso_1

NetworkId           : 10.10.0.0/16

CustomConfiguration : ADSite=Contoso;
Name                : Contoso_1

NetworkId           : 10.11.0.0/16

CustomConfiguration : ADSite=Contoso;
Name                : Contoso_2

NetworkId           : 10.12.0.0/16

CustomConfiguration : ADSite=Contoso;
```

此命令会获取所有分配给名为“Contoso AD-Site”的站点的非虚拟化子网。

### 示例 3：获取所有 IPv4 子网
```
PS C:\> Get-IpamSubnet -AddressFamily IPv4 -NetworkType Provider -AddressSpace "Default"

Name                 : Contoso_3

NetworkId            : 10.13.0.0/16

NetworkType          : Provider

Overlapping          : False

NetworkSite          :

VmmLogicalNetwork    :

ProviderAddressSpace : Default

CustomerAddressSpace :

VlanId               :

Owner                :
```

此命令可获取默认地址空间中所有提供者的IPv4子网信息。

### 示例 4：获取所有未映射且未虚拟化的子网
```
PS C:\> Get-IpamSubnet -AddressFamily IPv4 -NetworkType NonVirtualized -Unmapped
Name                 : 10.0.0.0/24

NetworkId            : 10.0.0.0/24

NetworkType          : NonVirtualized

Overlapping          : False

NetworkSite          :

VmmLogicalNetwork    :

ProviderAddressSpace : Default

CustomerAddressSpace :

VlanId               :

Owner                :
Name                 : Contoso_1

NetworkId            : 10.10.1.0/24

NetworkType          : NonVirtualized

Overlapping          : True

NetworkSite          :

VmmLogicalNetwork    :

ProviderAddressSpace : Default

CustomerAddressSpace :

VlanId               :

Owner                :
```

此命令会获取默认地址空间中所有未映射且未虚拟化的子网。

### 示例 5：获取客户地址空间中的所有子网
```
PS C:\> Get-IpamSubnet -AddressFamily IPv4 -NetworkType Customer -AddressSpace ContosoWest|Where {$_.VmmLogicalNetwork -eq "Storage"}
Name                 : ContosoWest_3

NetworkId            : 192.168.64.0/24

Type                 : Virtual

Overlapping          : False

NetworkSite          : Contoso

VmmLogicalNetwork    : Storage

ProviderAddressSpace : ContosoDatacenter

CustomerAddressSpace : ContosoWest

VlanId               :

Owner                :
Name                 : ContosoWest_4

NetworkId            : 20.22.16.0/24

Type                 : Virtual

Overlapping          : False

NetworkSite          : Contoso

VmmLogicalNetwork    : Storage

ProviderAddressSpace : ContosoDatacenter

CustomerAddressSpace : ContosoWest

VlanId               :

Owner                :
```

此命令会获取所有属于 ContosoWest 客户地址空间以及某个逻辑网络的子网。

## 参数

### -AddressFamily
指定一类 IP 地址的地址族。

该参数的可接受值包括：

- IPv4
- IPv6

```yaml
Type: AddressFamily[]
Parameter Sets: ByAF
Aliases:
Accepted values: IPv4, IPv6

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AddressSpace
指定一个地址空间名称数组。如果未指定任何地址空间，该cmdlet将从IPAM中配置的所有地址空间获取数据。

```yaml
Type: String[]
Parameter Sets: ById, ByAF
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `-*Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -MappingToBlock
指定那些映射到某个地址块的子网。

```yaml
Type: CimInstance
Parameter Sets: ByBlock
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -NetworkId
指定一个网络和前缀的数组。请使用无类别域间路由（CIDR）表示法来指定网络ID，格式为“Network/Prefix”。

```yaml
Type: String[]
Parameter Sets: ById
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetworkType
指定给定子网的网络类型。

该参数的可接受值包括：

- Provider
 --  Customer
 --  NonVirtualized

如果该参数的值为“Default”，那么它可以取“Provider”或“NonVirtualized”作为其值。如果该参数的值为“Provider”，则必须指定“Provider”作为其值；否则将会导致错误。同样地，如果该参数的值为“Customer”，也必须指定“Customer”作为其值；否则也会导致错误。

如果您不指定此参数，该cmdlet将返回所有符合条件的子网，而不考虑网络类型。

```yaml
Type: VirtualizationType[]
Parameter Sets: ById, ByAF
Aliases:
Accepted values: NonVirtualized, Provider, Customer

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -Unmapped
表示该 cmdlet 会获取未映射到任何 IP 地址块的子网。

```yaml
Type: SwitchParameter
Parameter Sets: ByAF
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamSubnet

## 备注

## 相关链接

[Add-IpamSubnet](./Add-IpamSubnet.md)

[Export-IpamSubnet](./Export-IpamSubnet.md)

[Import-IpamSubnet](./Import-IpamSubnet.md)

[Remove-IpamSubnet](./Remove-IpamSubnet.md)

[Set-IpamSubnet](./Set-IpamSubnet.md)

