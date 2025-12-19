---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamAddress.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamaddress?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamAddress
---

# Get-IpamAddress

## 摘要
从 IPAM 获取 IP 地址。

## 语法

### 按地址查找
```
Get-IpamAddress [-IpAddress] <IPAddress[]> [-ManagedByService <String[]>] [-ServiceInstance <String[]>]
 [-NetworkType <VirtualizationType[]>] [-AddressSpace <String[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 按地址族分类
```
Get-IpamAddress -AddressFamily <AddressFamily[]> [-AddressCategory <AddressCategory[]>]
 [-ManagedByService <String[]>] [-ServiceInstance <String[]>] [-NetworkType <VirtualizationType[]>]
 [-AddressSpace <String[]>] [-Unmapped] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ByBlock
```
Get-IpamAddress -MappingToBlock <CimInstance> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### BySubnet
```
Get-IpamAddress -MappingToSubnet <CimInstance> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

### ByRange
```
Get-IpamAddress -MappingToRange <CimInstance> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-IpamAddress` cmdlet 用于从 IP 地址管理（IPAM）系统获取 IP 地址。可以通过指定 `IpAddress` 参数来获取单个 IP 地址；通过指定 `AddressFamily` 参数可以获取某一地址家族下的所有 IP 地址。此外，还可以获取属于某个范围、子网或地址块的 IP 地址。

## 示例

### 示例 1：获取所有私有的物理 IPv4 地址
```
PS C:\> Get-IpamAddress -AddressFamily IPv4 -AddressCategory Private -AddressSpace "Default"
```

这个命令会获取IPAM中所有私有的物理IPv4地址。由于该命令指定了“默认地址空间”，因此它将从IPAM中的所有地址空间中获取提供商或非虚拟化的IP地址。

### 示例 2：获取提供商网络的私有 IPv4 地址
```
PS C:\> Get-IpamAddress -AddressFamily IPv4 -AddressCategory Private -NetworkType Provider
```

此命令会获取所有提供商网络对应的私有 IPv4 地址。由于该命令没有指定 `AddressSpace` 参数，因此它将获取属于 IPAM 中所有地址空间的地址。

### 示例 3：从默认地址空间中获取私有 IPv4 地址
```
PS C:\> Get-IpamAddress -AddressFamily IPv4 -AddressCategory Private -NetworkType Provider -AddressSpace "Default"
```

这个命令会获取所有提供商网络对应的私有IPv4地址。由于该命令指定了“默认地址空间”，因此它会从IPAM中配置的所有地址空间中检索IP地址。

### 示例 4：获取客户网络的私有 IPv4 地址
```
PS C:\> Get-IpamAddress -AddressFamily IPv4 -AddressCategory Private -NetworkType Customer
```

此命令用于获取客户网络的所有私有 IPv4 地址。由于该命令没有指定 *AddressSpace* 参数，因此它会获取所有在 IPAM 中配置的地址空间所属的地址。

### 示例 5：从一个地址空间中获取客户网络的私有 IPv4 地址
```
PS C:\> Get-IpamAddress -AddressFamily IPv4 -AddressCategory Private -NetworkType Customer -AddressSpace "ContosoAddSpace01"
```

此命令会获取属于名为“ContosoAddSpace01”的地址空间的所有客户网络的私有IPv4地址。

### 示例 6：从所有地址空间中获取物理 IP 地址
```
PS C:\> Get-IpamAddress -IpAddress 10.12.1.1, 10.12.3.1
```

这个命令会获取物理IP地址10.12.1.1和10.12.3.1。由于该命令没有指定*AddressSpace*参数，因此它会从所有与IP地址10.12.1.1和10.12.3.1相匹配的地址空间中获取这些IP地址。

### 示例 7：获取地址空间中的重复地址
```
PS C:\> Get-IpamAddress -AddressFamily IPv4 -AddressSpace Default | Where-Object {$_.duplicate -eq $true} | Format-List IPAddress, NetworkType, ManagedByService, ServiceInstance, ProviderAddressSpace
IpAddress            : 172.16.10.16

NetworkType          : Provider

ManagedByService     : VMM

ServiceInstance      : vmm1.contoso.com

ProviderAddressSpace : Default
IpAddress            : 172.16.10.16

NetworkType          : Provider

Duplicate            : True

ManagedByService     : IPAM

ServiceInstance      : Localhost

ProviderAddressSpace : Default
```

这个命令会获取默认提供者地址空间中所有重复的IPv4地址。默认地址空间是指IPAM实体所属的地址空间。该命令返回两个IP地址为172.16.10.16的地址：其中一个地址由IPAM管理，另一个地址由vmmblue_1管理。IPAM服务器将这两个地址都标记为重复地址。该命令使用**Format-List** cmdlet以表格的形式显示输出结果。如需更多信息，请输入`Get-Help Format-Table`。

### 示例 8：获取映射到某个子网的 IP 地址
```
PS C:\> $ContosoPhysicalSubnet = Get-IpamSubnet -NetworkId "10.12.0.0/16"
PS C:\> Get-IpamAddress -MappingToSubnet $ContosoPhysicalSubnet
```

这个示例获取了所有映射到某个子网的IP地址。由于该子网的网络类型是非虚拟化的，因此结果中只包含属于该子网的物理地址以及来自默认地址空间的结构化地址（fabric addresses）。

第一个命令使用 **Get-IpamSubnet** cmdlet 来获取包含在 IPAM 中为网络（其 ID 为 10.12.0.0/16）配置的子网的 **IpamSubnet** 对象。该命令将此对象存储在 `$ContosoPhysicalSubnet` 变量中。

第二个命令获取了所有属于存储在 `$ContosoPhysicalSubnet` 变量中的 IP 子网的 IP 地址。

### 示例 9：获取所有映射到某个 IP 范围内的 IP 地址
```
PS C:\> $Range = Get-IpamRange -StartIPAddress 10.12.1.1 -EndIPAddress 10.12.1.254
PS C:\> Get-IpamAddress -MappingToRange $Range
```

这个例子获取了属于某个IP地址范围的所有IP地址。

第一个命令使用 **Get-IpamRange** cmdlet 来获取一个包含在 IPAM 中配置的 IP 范围的 **IpamRange** 对象。该命令将这个对象存储在 `$Range` 变量中。

第二个命令会获取所有属于存储在 `$Range` 变量中的 IP 地址范围的 IP 地址。

## 参数

### -AddressCategory
指定一个包含IP地址类别的数组。如果指定了此参数，则必须同时指定*AddressFamily*参数。

该参数的可接受值为：  
- Public（公共）  
- Private（私有）

```yaml
Type: AddressCategory[]
Parameter Sets: ByAddressFamily
Aliases:
Accepted values: Public, Private, Global

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AddressFamily
指定一个包含 IP 地址地址族（address family）的数组。

此参数的可接受值为：

- IPv4
- IPv6

```yaml
Type: AddressFamily[]
Parameter Sets: ByAddressFamily
Aliases:
Accepted values: IPv4, IPv6

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AddressSpace
指定一个地址空间名称的数组。如果不指定此参数，该 cmdlet 将获取 IPAM 中所有地址空间的地址；如果指定了此参数，则必须同时指定 *AddressFamily* 参数。

```yaml
Type: String[]
Parameter Sets: ByAddress, ByAddressFamily
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认值是本地计算机上的当前会话。

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

### -ManagedByService
指定一个用于管理IP地址的服务名称数组。为此参数指定的值必须存在于您在IPAM中为**ManagedByService**自定义字段所定义的值集合中。

你可以使用 `Add-IpamCustomValue` 命令向 IPAM 中的 `ManagedByService` 自定义字段添加一个值；同样，也可以使用 `Remove-IpamCustomValue` 命令从该自定义字段中删除某个值。

```yaml
Type: String[]
Parameter Sets: ByAddress, ByAddressFamily
Aliases: MB

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MappingToBlock
用于指定一个 IP 地址段。该 cmdlet 会获取属于该 IP 地址段的所有地址。

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

### -MappingToRange
用于指定一个IP地址范围。该cmdlet会获取属于该IP地址范围内的所有地址。

```yaml
Type: CimInstance
Parameter Sets: ByRange
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -MappingToSubnet
用于指定一个 IP 子网。该 cmdlet 会获取属于该 IP 子网的地址信息。

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
指定地址的网络类型。该参数的可接受值为：

- Provider
- Customer
- NonVirtualized

The default value is NonVirtualized.

If you specify Default for the *AddressSpace* parameter, the valid values for this parameter are Provider and NonVirtualized.
If you specify a provider type of address space for the *AddressSpace* parameter, you must specify Provider for this parameter.
If you specify a customer type of address space for the *AddressSpace* parameter, you must specify Customer for this parameter.

```yaml
Type: VirtualizationType[]
Parameter Sets: ByAddress, ByAddressFamily
Aliases:
Accepted values: NonVirtualized, Provider, Customer

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ServiceInstance
请指定一个用于管理IP地址的服务实例数组。这些服务实例应该是您为*ManagedByService*参数所指定的那些服务实例。您为此参数指定的值必须存在于您在IPAM中为**ServiceInstance**自定义字段定义的数值集合中。

```yaml
Type: String[]
Parameter Sets: ByAddress, ByAddressFamily
Aliases: SI

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算一个最优的速率限制（即并发操作的最大数量）。这个速率限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
这表示该cmdlet获取的地址不属于IPAM中任何IP地址家族。

```yaml
Type: SwitchParameter
Parameter Sets: ByAddressFamily
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamAddress[]
这个cmdlet返回一个对象，该对象表示IPAM服务器上的一组IP地址。

## 备注

## 相关链接

[Set-IpamAddress](./Set-IpamAddress.md)

[Add-IpamAddress](./Add-IpamAddress.md)

[Remove-IpamAddress](./Remove-IpamAddress.md)

[Import-IpamAddress](./Import-IpamAddress.md)

[Export-IpamAddress](./Export-IpamAddress.md)

[Add-IpamCustomValue](./Add-IpamCustomValue.md)

[Remove-IpamCustomValue](./Remove-IpamCustomValue.md)

[Get-IpamSubnet](./Get-IpamSubnet.md)

[Get-IpamRange](./Get-IpamRange.md)

