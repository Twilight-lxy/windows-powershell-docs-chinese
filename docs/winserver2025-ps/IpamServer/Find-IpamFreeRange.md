---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamRange.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/find-ipamfreerange?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Find-IpamFreeRange
---

# 查找 Ipam 自由范围

## 摘要
从指定的子网中查找一个或多个可用的 IP 地址范围。

## 语法

```
Find-IpamFreeRange [-InputObject] <CimInstance> [-NumberOfAddresses] <UInt32> [[-NumberOfRanges] <UInt32>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
**Find-IpamFreeRange** cmdlet 用于从 IP 地址管理（IPAM）数据库中查找指定子网内的可用 IP 地址范围。IP 范围是一组唯一的 IP 地址，通常对应于动态主机配置协议（DHCP）的作用域。需要搜索空闲 IP 地址范围的子网通过 InputObject 参数传递进来。

## 示例

### 示例 1：查找拥有 256 个 IP 地址的空闲地址范围
```
PS C:\> $Subnet = Get-IpamSubnet -NetworkId 12.1.0.0/16
PS C:\> Find-IpamFreeRange -InputObject $Subnet -NumberOfAddresses 256
StartIPAddress : 12.1.0.0
EndIPAddress   : 12.1.0.255
NetworkId      : 12.1.0.0/16
```

第一个命令获取特定网络ID对应的IPAM子网，并将其存储在名为$Subnet的变量中。第二个命令则在该$Subnet变量指定的子网范围内，查找所有地址为256的自由IP地址范围。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认值是本地计算机上的当前会话。

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

### -InputObject
指定要输入到此 cmdlet 的数据。您可以使用该参数，也可以将数据通过管道（pipe）传递给此 cmdlet。

```yaml
Type: CimInstance
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -NumberOfAddresses
指定要返回的 IP 范围的大小。该数字表示 IP 范围内所需的可用 IP 地址的数量。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NumberOfRanges
指定要返回的空闲 IP 范围的数量。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时执行该 cmdlet 的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamFreeRange

该cmdlet返回一个**IpamFreeRange**对象的实例。

## 备注

## 相关链接

[Find-IpamFreeAddress](./Find-IpamFreeAddress.md)

[Find-IpamFreeSubnet](./Find-IpamFreeSubnet.md)