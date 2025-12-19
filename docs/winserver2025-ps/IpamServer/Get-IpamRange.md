---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamRange.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamrange?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamRange
---

# Get-IpamRange

## 摘要
从 IPAM 服务器获取一组 IP 地址范围。

## 语法

### ByID
```
Get-IpamRange -StartIPAddress <IPAddress[]> -EndIPAddress <IPAddress[]> [-ManagedByService <String[]>]
 [-ServiceInstance <String[]>] [-NetworkType <VirtualizationType[]>] [-AddressSpace <String[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByAF
```
Get-IpamRange -AddressFamily <AddressFamily[]> [-AddressCategory <AddressCategory[]>]
 [-ManagedByService <String[]>] [-ServiceInstance <String[]>] [-NetworkType <VirtualizationType[]>]
 [-AddressSpace <String[]>] [-Unmapped] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ByBlock
```
Get-IpamRange -MappingToBlock <CimInstance> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### 按子网划分
```
Get-IpamRange -MappingToSubnet <CimInstance> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
**Get-IpamRange** cmdlet 用于从 IP 地址管理（IPAM）系统中获取一系列 IP 地址范围。您可以使用此 cmdlet 来获取特定地址族的 IP 地址范围，或者根据起始和结束 IP 地址来获取某个特定的地址范围。该 cmdlet 提供了多种参数选项，以便获取与给定 IP 地址块或子网相关联的所有地址范围。

## 示例

### 示例 1：获取所有 IPv4 地址范围
```
PS C:\> Get-IpamRange -AddressFamily IPv4 -AddressCategory Private -AddressSpace "Default"
```

此命令可以获取所有私有的物理IPv4地址范围，无论是来自服务提供商的还是未虚拟化的地址范围。

### 示例 2：获取某种网络类型的所有 IPv4 地址范围
```
PS C:\> Get-IpamRange -AddressFamily IPv4 -AddressCategory Private -NetworkType Provider
```

这个命令会获取属于任何提供商地址空间的、网络类型为“provider”的所有私有IPv4地址段。

### 示例 3：获取提供者网络类型默认地址空间中的所有 IPv4 范围
```
PS C:\> Get-IpamRange -AddressFamily IPv4 -AddressCategory Private -NetworkType Provider -AddressSpace "Default"
```

这个命令可以获取属于默认地址空间的、网络类型为“provider”的所有私有IPv4地址范围。

### 示例 4：获取某个客户网络类型的所有 IPv4 范围
```
PS C:\> $PrivateCustomerRanges = Get-IpamRange -AddressFamily IPv4 -AddressCategory Private -NetworkType Customer
```

该命令获取所有属于“customer”网络类型的私有IPv4地址范围，并将结果存储在名为$PrivateCustomerRanges的变量中。

### 示例 5：获取某种网络类型和地址空间下的所有 IPv4 地址范围
```
PS C:\> $PrivateCustomerRanges = Get-IpamRange -AddressFamily IPv4 -AddressCategory Private -NetworkType Customer -AddressSpace Contoso
```

这条命令会获取所有属于Contoso客户地址空间的、网络类型为“Customer”的私有IPv4地址，并将结果存储在名为$PrivateCustomerRanges的变量中。

### 示例 6：获取两个地址之间的所有 IPv4 地址范围
```
PS C:\> $Range= Get-IpamRange -StartIPAddress 10.12.1.1 -EndIPAddress 10.12.1.254 -ManagedByService IPAM -ServiceInstance "localhost"
```

这个命令会获取给定IP地址范围的详细信息，并将结果存储在名为$Range的变量中。

### 示例 7：获取所有重叠的范围
```
PS C:\> Get-IpamRange -AddressFamily IPv4 -AddressCategory Private -AddressSpace "Default" | where {$Overlapping -eq $True}
Overlapping      : True

NetworkID        : 172.16.19.0/24

StartAddress     : 172.16.19.10

EndAddress       : 172.16.19.110

ManagedByService : VMM

ServiceInstance  : vmm1.contoso.com

NetworkType      : Provider

Owner            :
Overlapping      : True

NetworkID        : 172.16.19.0/24

StartAddress     : 172.16.19.50

EndAddress       : 172.16.19.150

ManagedByService : IPAM

ServiceInstance  : Localhost

NetworkType      : NonVirtualized

Owner            :
```

这个命令会获取默认地址空间中所有重叠的IP范围。默认地址空间中可以同时存在Provider类型的IP范围和非虚拟化（NonVirtualized）类型的IP范围。在IPAM系统中，如果两个IP范围属于同一个地址空间，并且它们的起始IP地址和结束IP地址有重叠，那么这两个IP范围就被标记为“重叠”的（overlapping）。

### 示例 8：获取子网的所有 IPv4 范围
```
PS C:\> $ContosoPhysicalSubnet = Get-IpamSubnet -NetworkId 10.12.0.0/16
PS C:\> $AddressMappingToSubnet = Get-IpamRange -MappingToSubnet $ContosoPhysicalSubnet
```

这个示例获取了所有映射到给定子网的IP地址范围。由于该子网的网络类型是非虚拟化的，因此结果中仅包含来自默认地址空间的物理地址和与该子网关联的架构（fabric）地址。

第一个命令使用了 **Get-IpamSubnet** cmdlet 来获取一个子网，并将结果存储在名为 $ContosoPhysicalSubnet 的变量中。

第二个命令获取IP地址范围，并将结果存储在$AddressMappingToSubnet变量中。

## 参数

### -AddressCategory
指定一个包含 IP 地址地址族的数组。此参数的可接受值为：

- IPv4
- IPv6

```yaml
Type: AddressCategory[]
Parameter Sets: ByAF
Aliases:
Accepted values: Public, Private, Global

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AddressFamily
Specifies an array of address families of IP address range objects that this cmdlet gets.
此参数的可接受值为：

- IPv4
- IPv6

```yaml
Type: AddressFamily[]
Parameter Sets: ByAF
Aliases:
Accepted values: IPv4, IPv6

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AddressSpace
指定一个用于查询的 IP 地址范围地址空间数组。如果您不指定值，该 cmdlet 将获取 IPAM 中所有地址空间的数据。

```yaml
Type: String[]
Parameter Sets: ByID, ByAF
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将此 cmdlet 作为后台作业运行。使用该参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，随后会显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用 `*-Job` 系列的 cmdlets；要获取作业的结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -EndIPAddress
指定一个IP地址数组。对于此参数而言，这些地址代表所需获取的IP地址范围的高端部分。

```yaml
Type: IPAddress[]
Parameter Sets: ByID
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ManagedByService
指定一个服务数组，这些服务用于管理要获取的范围。

```yaml
Type: String[]
Parameter Sets: ByID, ByAF
Aliases: MB

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MappingToBlock
指定映射到地址块的范围内。

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

### -MappingToSubnet
指定一个 IP 范围，该范围对应于某个子网。

```yaml
Type: CimInstance
Parameter Sets: BySubnet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -NetworkType
为该cmdlet获取的地址指定一系列网络类型。

此参数的可接受值为：

- Provider
 --  Customer
 --  NonVirtualized

如果该参数的值为“Default”，那么它可以选择“Provider”或“NonVirtualized”作为其值。如果该参数的值为“Provider”，则必须指定“Provider”作为其值；否则会导致错误。同样地，如果该参数的值为“Customer”，也必须指定“Customer”作为其值；否则也会导致错误。

如果您指定了*NetworkType*参数，但未指定*AddressType*参数，该cmdlet将返回给定网络类型的所有IP地址范围。

```yaml
Type: VirtualizationType[]
Parameter Sets: ByID, ByAF
Aliases:
Accepted values: NonVirtualized, Provider, Customer

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ServiceInstance
指定一个服务实例数组，这些实例用于管理需要获取的地址范围。

```yaml
Type: String[]
Parameter Sets: ByID, ByAF
Aliases: SI

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StartIPAddress
指定一个IP地址数组。对于此参数而言，这些地址代表所需获取的IP地址范围的高端部分。

```yaml
Type: IPAddress[]
Parameter Sets: ByID
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不影响整个会话或计算机本身。

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
表示该cmdlet会获取未映射的范围（即尚未被分配到任何特定值的地址范围）。

```yaml
Type: SwitchParameter
Parameter Sets: ByAF
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### CimInstance#ROOT/microsoft/ipam/MSFT_IPAM_Range
此 cmdlet 返回一个包含 IPAM 数据库中存在的 IP 地址范围数组。

## 备注

## 相关链接

[Add-IpamRange](./Add-IpamRange.md)

[Export-IpamRange](./Export-IpamRange.md)

[Import-IpamRange](./Import-IpamRange.md)

[Remove-IpamRange](./Remove-IpamRange.md)

[Set-IpamRange](./Set-IpamRange.md)

[Get-IpamSubnet](./Get-IpamSubnet.md)

