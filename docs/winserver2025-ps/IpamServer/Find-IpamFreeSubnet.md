---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamSubnet.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/find-ipamfreesubnet?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Find-IpamFreeSubnet
---

# 查找 Ipam 免费子网

## 摘要
在指定的IP地址段中查找一个或多个空闲的IP子网。

## 语法

```
Find-IpamFreeSubnet [-InputObject] <CimInstance> [-SubnetPrefix] <UInt32> [[-NumberOfSubnets] <UInt32>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Find-IpamFreeSubnet` cmdlet 可以在指定的 IP 块中查找 IP 地址管理（IPAM）数据库中可用的空闲子网。需要搜索空闲子网的 IP 块通过 `InputObject` 参数传递进来。

## 示例

### 示例 1：查找具有指定子网前缀的空闲子网
```
PS C:\> $IPAMBlock= Get-IpamBlock -NetworkId 10.1.0.0/16 -StartIPAddress 10.1.0.0 -EndIPAddress 10.1.255.255
PS C:\> Find-IpamFreeSubnet -InputObject $IPAMBlock -SubnetPrefix 24
```

第一个命令从网络ID 10.1.0.0/16中获取特定范围内的所有IP地址，并将结果存储在名为$IPAMBlock的变量中。然后，第二个命令在名为$IPAMBlock的变量中查找所有子网前缀为24的空闲子网。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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
指定要传递给此 cmdlet 的输入数据。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该 cmdlet。

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

### -NumberOfSubnets
指定要返回的空闲子网的数量。

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

### -SubnetPrefix
指定要返回的子网的前缀。该前缀是一个整数值，表示子网掩码中设置的比特位数。

子网前缀可以告诉你该子网上可用的IP地址数量。例如，一个前缀值为24的子网拥有256个IP地址。

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

### -ThrottleLimit
指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前的 cmdlet，而不适用于会话或整个计算机。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Find-IpamFreeAddress](./Find-IpamFreeAddress.md)

[Find-IpamFreeRange](./Find-IpamFreeRange.md)

