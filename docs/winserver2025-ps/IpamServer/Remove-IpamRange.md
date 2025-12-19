---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamRange.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/remove-ipamrange?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IpamRange
---

# 移除 Ipam 范围

## 摘要
从 IPAM 服务器配置中删除一组 IP 地址。

## 语法

### 查询（cdxml）（默认值）
```
Remove-IpamRange [-StartIPAddress] <IPAddress[]> [-EndIPAddress] <IPAddress[]> [-ManagedByService <String[]>]
 [-ServiceInstance <String[]>] [-NetworkType <VirtualizationType[]>] [-AddressSpace <String[]>]
 [-DeleteMappedAddresses] [-Force] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject（cdxml）
```
Remove-IpamRange -InputObject <CimInstance[]> [-DeleteMappedAddresses] [-Force] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-IpamRange` cmdlet 用于从 IP 地址管理（IPAM）服务器配置中删除指定的 IP 地址范围。您可以选择删除属于该范围的地址，或者选择保留这些地址。

## 示例

### 示例 1：删除一个 IP 地址范围
```
PS C:\> Get-IpamRange -StartIPAddress 10.12.3.1 -EndIPAddress 10.12.3.254|Remove-IpamRange
Confirm

This will permanently delete the given IP Range from IPAM. Do you want to continue?

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): Y
```

此命令会删除一个IP地址范围，但不会删除已映射的IP地址。这些已映射的地址会被标记为“未映射”状态，并移动到未映射地址空间中。

### 示例 2：移除一个 IP 地址范围及其对应的映射 IP 地址
```
PS C:\> Get-IpamRange -StartIPAddress 10.12.3.1 -EndIPAddress 10.12.3.254|Remove-IpamRange -DeleteMappedAddresses
Confirm

Deleting the range with start IP address 10.12.3.1 and end IP address 10.12.3.254 managed by localhost instance of IPAM. Any addresses mapped to this range will be deleted. Do you want to continue?

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):Y
```

此命令会删除一个IP地址范围及其对应的已映射IP地址。

### 示例 3：从地址空间中移除一个 IP 地址范围
```
PS C:\> Get-IpamRange -StartIPAddress 10.20.4.1 -EndIPAddress 10.20.4.99 -ManagedByService IPAM -ServiceInstance Localhost -Customer -CustomerAddressSpace Contoso | Remove-IpamRange -DeleteMappedAddresses
Confirm

This will permanently delete the given IP Range from IPAM. Do you want to continue?

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): Y
```

此命令通过使用名为“Contoso”的客户地址空间中的*StartIPAddress*（起始IP地址）和*EndIPAddress*（结束IP地址）参数来删除相应的客户IP地址范围。

## 参数

### -AddressSpace
指定一个要删除的IP地址范围数组。如果不指定任何值，该cmdlet将删除IPAM中所有非虚拟化（NonVirtualized）、提供商（Provider）和客户（Customer）地址空间的数据。

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
将 cmdlet 作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
在运行cmdlet之前，会提示您进行确认。

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

### -DeleteMappedAddresses
这表示该 cmdlet 会删除映射到某个 IP 范围内的 IP 地址，而不会保留这些地址。

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

### -EndIPAddress
指定一个IP地址数组。对于此参数而言，这些地址代表了需要移除的范围的高端值（即该范围内的最后一个地址）。

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

### -Force
强制命令运行，而无需请求用户确认。

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
指定要传递给此cmdlet的输入数据。你可以使用该参数，也可以将输入数据通过管道（pipe）传递给此cmdlet。

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
指定一个服务数组，这些服务用于管理需要删除的范围（即相关资源或数据）。

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
指定一个网络类型数组，用于确定需要移除的地址所属的网络类型。

该参数的可接受值为：

- Provider
- Customer
- NonVirtualized

If you do not specify a value, the cmdlet deletes all matching IP address ranges of network type Provider, Customer, and NonVirtualized.

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

### -ServiceInstance
指定一个服务实例数组，这些服务实例用于管理需要移除的地址范围。

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
指定一个IP地址数组。对于此参数而言，这些地址表示需要被移除的地址范围的下限。

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
该参数用于指定可以同时运行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令（cmdlets）的数量来计算一个最佳的限制值。这个限制仅适用于当前运行的命令，而不影响整个会话或计算机本身。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

### CimInstance#ROOT/microsoft/ipam/MSFT_IPAM_Range[]
此cmdlet返回一个对象，该对象表示从IPAM中删除的IP地址范围对象。

## 备注

## 相关链接

[Add-IpamRange](./Add-IpamRange.md)

[Export-IpamRange](./Export-IpamRange.md)

[Get-IpamRange](./Get-IpamRange.md)

[Import-IpamRange](./Import-IpamRange.md)

[Set-IpamRange](./Set-IpamRange.md)

