---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamAddress.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/remove-ipamaddress?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IpamAddress
---

# 删除 IPAM 地址

## 摘要
从 IPAM 中移除一组地址。

## 语法

### 按地址查找
```
Remove-IpamAddress [-IpAddress] <IPAddress[]> [[-ManagedByService] <String[]>] [[-ServiceInstance] <String[]>]
 [-NetworkType <VirtualizationType[]>] [-AddressSpace <String[]>] [-Force] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject（cdxml）
```
Remove-IpamAddress -InputObject <CimInstance[]> [-Force] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-IpamAddress` cmdlet 用于从 IP 地址管理（IPAM）系统中删除一组地址。该 cmdlet 会永久性地从 IPAM 数据库中移除指定的 IP 地址记录。您可以指定要删除的 IP 地址，或者使用 `InputObject` 参数来指定要删除的 `IpamAddress` 对象。

该 cmdlet 不会删除动态主机配置协议（DHCP）服务器或域名系统（DNS）记录中的任何预留信息。你可以使用 Windows PowerShell 来管理 DHCP 服务器，从而从 DHCP 服务器中删除相应的预留信息；同样地，你也可以使用 Windows PowerShell 来管理 DNS，以删除与被删除的 IP 地址相关联的 DNS 记录。

## 示例

### 示例 1：移除指定范围内的所有 IP 地址
```
PS C:\> $Range = Get-IpamRange -StartIPAddress 10.12.3.1 -EndIPAddress 10.12.3.254
PS C:\> Get-IpamAddress -MappingToRange $Range | Remove-IpamAddress
Confirm

Deleting the given IP Address from IPAM database. You will not be able to undo this action. Do you want to continue?

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):
```

这个示例会删除某个范围内的所有IP地址。

第一个命令使用了 **Get-IpamRange** cmdlet 来获取一个 **IpamRange** 对象，该对象包含了属于某个 IP 地址范围的地址信息。这个命令将获得的对象存储在 `$Range` 变量中。

第二个命令使用了 `Get-IpamAddress` cmdlet 来获取一个 `IpamAddress` 对象，该对象包含了与存储在 `$Range` 变量中的 IP 地址范围相匹配的地址信息。然后，通过管道运算符（pipeline operator）将该 `IpamAddress` 对象传递给 `Remove-IpamAddress` cmdlet，从而删除 `$Range` 变量中所存储的那些 IP 地址。

### 示例 2：删除 IPAM 管理的所有已过期的物理地址
```
PS C:\> Get-IpamAddress -AddressFamily IPv4 -AddressCategory Private -ManagedByService IPAM | Where-Object {$_.ExpiryStatus -eq "Expired"} | Remove-IpamAddress
```

这个命令会获取一个 `IPamAddress` 对象，其中包含由 IPAM 管理的已过期的物理地址信息。该命令通过管道操作符将 `IPamAddress` 对象传递给 `Remove-IpamAddress` cmdlet，然后 `Remove-IpamAddress` cmdlet 会删除这个 `IPamAddress` 对象。

### 示例 3：移除客户的 IP 地址
```
PS C:\> Remove-IpamAddress -IpAddress 172.16.10.16 -AddressSpace "Default"
```

此命令将客户IP地址172.16.10.16从默认地址空间中删除。

#### 示例 4：移除提供商的 IP 地址
```
PS C:\> Remove-IpamAddress -IpAddress 172.16.10.19 -AddressSpace "Default" -NetworkType Provider
```

此命令将提供商IP地址172.16.10.19从默认地址空间中删除。

## 参数

### -AddressSpace
指定一个地址空间数组。该cmdlet会删除属于所指定地址空间的所有地址。如果指定了此参数，则必须同时指定*IpAddress*参数。

```yaml
Type: String[]
Parameter Sets: ByAddress
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个代表该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
在运行cmdlet之前会提示您确认是否要继续执行该操作。

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
指定要传递给此cmdlet的输入数据。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

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
指定一个服务数组，这些服务用于管理在 *IpAddress* 参数中指定的 IP 地址。如果您指定了此参数，则必须同时指定 *IpAddress* 参数。

您为该参数指定的值必须存在于您在 IPAM 中为 **ManagedByService** 自定义字段所定义的值集合中。

```yaml
Type: String[]
Parameter Sets: ByAddress
Aliases: MB

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NetworkType
指定地址的网络类型。该参数的可接受值包括：

- Provider
- Customer
- NonVirtualized

The default value is NonVirtualized.

If you specify Default for the *AddressSpace* parameter, the valid values for this parameter are Provider and NonVirtualized.
If you specify a provider type of address space for the *AddressSpace* parameter, you must specify Provider for this parameter.
If you specify a customer type of address space for the *AddressSpace* parameter, you must specify Customer for this parameter.

```yaml
Type: VirtualizationType[]
Parameter Sets: ByAddress
Aliases:
Accepted values: NonVirtualized, Provider, Customer

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的该项的对象。默认情况下，此cmdlet不会生成任何输出。

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
请指定一组用于管理 IP 地址的服务实例。这些服务实例应与在 *ManagedByService* 参数中指定的服务相对应。如果您指定了该参数，则必须同时指定 *IpAddress* 参数。您为该参数设置的值必须存在于您在 IPAM 中为 **ServiceInstance** 自定义字段所定义的值集合中。

```yaml
Type: String[]
Parameter Sets: ByAddress
Aliases: SI

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时建立的、用于运行该cmdlet的操作的最大数量。如果省略此参数或输入值`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlets的数量来计算该cmdlet的最佳限制值。此限制仅适用于当前运行的cmdlet，而不适用于整个会话或计算机本身。

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

### IpamAddress
此cmdlet返回一个对象，该对象表示IPAM服务器上的一个IP地址。

## 备注

## 相关链接

[Get-IpamAddress](./Get-IpamAddress.md)

[Add-IpamAddress](./Add-IpamAddress.md)

[Set-IpamAddress](./Set-IpamAddress.md)

[Import-IpamAddress](./Import-IpamAddress.md)

[Export-IpamAddress](./Export-IpamAddress.md)

[Get-IpamAddressSpace](./Get-IpamAddressSpace.md)

