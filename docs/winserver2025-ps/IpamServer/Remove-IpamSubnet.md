---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamSubnet.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/remove-ipamsubnet?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IpamSubnet
---

# 移除 Ipam 子网

## 摘要
从 IPAM 中删除一个子网。

## 语法

### 查询（cdxml）（默认值）
```
Remove-IpamSubnet -NetworkId <String[]> [-NetworkType <VirtualizationType[]>] [-AddressSpace <String[]>]
 [-DeleteAssociatedRanges] [-DeleteAssociatedAddresses] [-Force] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Remove-IpamSubnet -InputObject <CimInstance[]> [-DeleteAssociatedRanges] [-DeleteAssociatedAddresses] [-Force]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
**Remove-IpamSubnet** cmdlet 用于从 IP 地址管理 (IPAM) 系统中删除指定的子网。默认情况下，如果该子网关联有地址范围，此 cmdlet 会返回错误信息。您可以使用 *DeleteAssociatedRanges* 参数来删除这些关联的地址范围，或者使用 *DeleteAssociatedAddresses* 参数来删除关联的 IP 地址。

## 示例

### 示例 1：删除一个具有已映射 IP 范围的非虚拟化子网
```
PS C:\> Remove-IpamSubnet -NetworkId 10.12.0.0/16 -NetworkType NonVirtualized

Confirm

Deleting the non-virtualized subnet Contoso_2 with network 10.12.0.0/16.

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): y

Remove-IpamSubnet : There are ranges associated with this subnet.

At line:1 char:1

+ Remove-IpamSubnet -InputObject $subnet

+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+ CategoryInfo          : ResourceUnavailable: (MSFT_IPAM_Subnet (InstanceID = "86-2"):ROOT/microsoft/ipam/MSFT_IP

AM_Subnet) [Remove-IpamSubnet], CimException

+ FullyQualifiedErrorId : WIN32 8,Remove-IpamSubnet
```

此命令用于删除一个已映射了 IP 范围的非虚拟化子网。由于如果某个子网已映射了 IP 范围，则无法删除该子网，因此会引发错误。

#### 示例 2：删除一个未虚拟化的子网
```
PS C:\> Remove-IpamSubnet -NetworkId 10.12.0.0/16 -NetworkType NonVirtualized -DeleteAssociatedRanges

Confirm

Deleting the non-virtualized subnet Contoso_2 with network 10.12.0.0/16. Ranges mapped to this subnet will also be

deleted.

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):Y
```

此命令会删除一个非虚拟化的子网以及所有映射到该子网的IP地址范围。该cmdlet会将这些已映射的IP地址移至未映射的地址空间中。

### 示例 3：删除一个未进行虚拟化的子网
```
PS C:\> Remove-IpamSubnet -NetworkId 10.12.0.0/16 -NetworkType NonVirtualized -DeleteAssociatedRanges -DeleteAssociatedAddresses

Confirm

Deleting the non-virtualized subnet Contoso_2 with network 10.12.0.0/16. Ranges mapped to this subnet and IP Addresses

associated via Ranges with this Subnet will also be deleted.

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):Y
```

该命令会删除一个非虚拟化的子网及其对应的IP地址范围。同时，也会移除所有通过这些IP地址范围映射到该子网的IP地址。

### 示例 4：移除某个提供商网络类型对应的子网
```
PS C:\> Remove-IpamSubnet -NetworkId 10.13.0.0/16 -NetworkType Provider -AddressSpace Default -DeleteAssociatedRanges

Confirm

Deleting the fabric subnet Contoso_3 with network 10.13.0.0/16. Ranges mapped to this subnet will also be deleted.

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):Y
```

此命令会将从提供者网络类型关联的子网从默认地址空间中删除。

### 示例 5：删除某个客户网络类型对应的子网
```
PS C:\> Remove-IpamSubnet -NetworkId 10.11.8.0/24 -NetworkType Customer -AddressSpace Contoso -DeleteAssociatedRanges

Confirm

Deleting the virtual subnet Contoso_1 with network 10.11.8.0/24. Ranges mapped to this subnet will also be deleted.

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):Y
```

该命令会从名为“Contoso”的客户地址空间中删除某个特定客户网络类型对应的子网。

## 参数

### -AddressSpace
指定一个地址空间名称的数组。如果您没有指定任何地址空间，该 cmdlet 将删除 IPAM 中配置的所有地址空间。

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
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 类型的 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。您可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -DeleteAssociatedAddresses
表示该cmdlet会删除与这些地址范围相关联的地址信息。

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

### -DeleteAssociatedRanges
表示该 cmdlet 会删除子网及其关联的所有 IP 范围。如果您不指定此参数，当子网存在关联的 IP 范围时，cmdlet 会生成错误。

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

### -Force
强制命令运行，而不需要用户确认。

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

### -NetworkId
指定一个网络数组，用于标识需要删除的子网。

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

### -NetworkType
指定要删除的子网所使用的网络类型数组。

此参数的可接受值为：

- Provider
 --  Customer
 --  NonVirtualized

如果您不指定值，则所有类型为“Provider”、“Customer”和“NonVirtualized”的匹配IP子网都将被删除。

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

### -ThrottleLimit
该参数用于指定可以同时运行的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamSubnet
此 cmdlet 返回一个对象，该对象表示从 IPAM 服务器中删除的子网。

## 备注

## 相关链接

[Add-IpamSubnet](./Add-IpamSubnet.md)

[Export-IpamSubnet](./Export-IpamSubnet.md)

[Get-IpamSubnet](./Get-IpamSubnet.md)

[Import-IpamSubnet](./Import-IpamSubnet.md)

[Set-IpamSubnet](./Set-IpamSubnet.md)

