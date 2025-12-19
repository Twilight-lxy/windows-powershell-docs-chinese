---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterPowerManagement.cmdletDefinition.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/enable-netadapterpowermanagement?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-NetAdapterPowerManagement
---

# 启用网卡电源管理功能

## 摘要
启用网络适配器上的特定电源管理功能。

## 语法

### 按名称排序（默认值）
```
Enable-NetAdapterPowerManagement [-Name] <String[]> [-IncludeHidden] [-ArpOffload] [-D0PacketCoalescing]
 [-DeviceSleepOnDisconnect] [-NSOffload] [-RsnRekeyOffload] [-SelectiveSuspend] [-WakeOnMagicPacket]
 [-WakeOnPattern] [-NoRestart] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ByInstanceID
```
Enable-NetAdapterPowerManagement -InterfaceDescription <String[]> [-IncludeHidden] [-ArpOffload]
 [-D0PacketCoalescing] [-DeviceSleepOnDisconnect] [-NSOffload] [-RsnRekeyOffload] [-SelectiveSuspend]
 [-WakeOnMagicPacket] [-WakeOnPattern] [-NoRestart] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject（cdxml）
```
Enable-NetAdapterPowerManagement -InputObject <CimInstance[]> [-ArpOffload] [-D0PacketCoalescing]
 [-DeviceSleepOnDisconnect] [-NSOffload] [-RsnRekeyOffload] [-SelectiveSuspend] [-WakeOnMagicPacket]
 [-WakeOnPattern] [-NoRestart] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-NetAdapterPowerManagement` cmdlet 可以启用网络适配器上的特定电源管理功能。如果没有指定任何电源管理选项，那么所有支持的电源管理功能都会被启用。

## 示例

### 示例 1：为指定的网络适配器启用电源管理功能
```
PS C:\> Enable-NetAdapterPowerManagement -Name "Ethernet 1"
```

此命令可对名为“Ethernet 1”的网络适配器启用电源管理功能，并重启该网络适配器。

### 示例 2：为指定的网络适配器启用电源管理功能
```
The first command gets the network adapter named Ethernet 2 and stores the result in the variable named $NetAdapter2. The second command and enables power management for the network adapter stored in the $NetAdapter variable.
PS C:\> $NetAdapter2 = Get-NetAdapter -Name "Ethernet 2"
PS C:\> Enable-NetAdapterPowerManagement -InputObject $NetAdapter2

This command is a version of the cmdlet that uses the pipeline to select the network adapter named Ethernet 3 and pipes that object into this cmdlet.
PS C:\> Get-NetAdapter -Name "Ethernet 3" | Enable-NetAdapterPowerManagement
```

## 参数

### -ArpOffload
表示该cmdlet用于管理网络适配器的地址解析协议（ARP）卸载功能。

当计算机处于低功耗模式并使用ARP卸载技术时，它可以将处理传入的ARP协议请求的响应任务卸载给其他组件。

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

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用 `-*Job` 系列 cmdlet。要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
在运行 cmdlet 之前会提示您进行确认。

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

### -D0PacketCoalescing
表示该cmdlet用于管理网络适配器的D0数据包聚合功能。

此功能通过减少接收中断的次数来帮助计算机节省电力。它通过合并随机广播或多播数据包来实现这一目标，从而减少了接收中断的数量。这样一来，计算机的处理开销和功耗都显著降低了。

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

### -DeviceSleepOnDisconnect
表示该cmdlet用于管理网络适配器的“断开连接后设备进入睡眠状态”的功能。

此功能允许设备在媒体连接断开时进入低功耗待机状态，并在媒体重新连接时唤醒设备。

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

### -IncludeHidden
该参数表示此 cmdlet 在操作过程中会同时包含可见网络适配器和隐藏网络适配器。默认情况下，仅包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将用于匹配所有（包括隐藏和可见的）网络适配器。

```yaml
Type: SwitchParameter
Parameter Sets: ByName, ByInstanceID
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定要输入到此 cmdlet 的数据。你可以使用这个参数，也可以将数据通过管道（pipe）传递给该 cmdlet。

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

### -InterfaceDescription
指定一个网络适配器接口描述数组。对于物理网络适配器而言，这通常是网络适配器制造商的名称后跟型号和描述，例如“Contoso 12345 千兆网络设备”。

```yaml
Type: String[]
Parameter Sets: ByInstanceID
Aliases: ifDesc, InstanceID

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NSOffload
表示该cmdlet用于管理网络适配器的邻居请求（Neighbor Solicitation，简称NS）卸载功能。

当计算机处于低功耗模式并使用NS卸载技术时，它能够将处理传入的NS协议请求的响应任务交给其他系统或组件来完成。

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

### -Name
指定一个网络适配器名称数组。

```yaml
Type: String[]
Parameter Sets: ByName
Aliases: ifAlias, InterfaceAlias

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NoRestart
表示该cmdlet在完成操作后不会重启网络适配器。许多高级功能需要在设置生效之前重新启动网络适配器才能正常使用。

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

### -RsnRekeyOffload
表示该cmdlet用于管理网络适配器的Wi-Fi强安全网络（RSN）密钥重加密卸载功能。

当计算机进入睡眠状态时，它可以暂停无线局域网（WoWLAN）唤醒功能所需的时间密钥（GTK）重新生成过程。

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

### -SelectiveSuspend
表示该cmdlet用于管理网络适配器的选择性暂停功能。

网络驱动接口规范（NDIS）中的选择性暂停功能允许NDIS通过将网络适配器切换到低功耗状态来使其进入休眠模式。这样一来，计算机就可以降低处理器和网络适配器的功耗开销。

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -WakeOnMagicPacket
表示该cmdlet用于管理网络适配器的“唤醒魔法数据包”（Wake-on-Magic Packet）功能。

“魔术数据包”是一种广播帧，其有效载荷中包含6个字节的所有二进制位均为1（用十六进制表示为“FF FF FF FF FF FF”），其后是目标计算机的48位MAC地址的重复内容，共16次，因此整个数据包的总长度为102字节。

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

### -WakeOnPattern
表示该cmdlet用于管理网络适配器的“唤醒模式”功能。“唤醒模式”是指那些用于判断传入的网络流量是否应触发计算机唤醒的网络数据包过滤器。这些模式可以在网络适配器上被启用。

以下唤醒模式可能被网络适配器支持：

- Wake Pattern.
- Wake on new incoming TCP connection for IPv4 and IPv6 including TCP SYN IPv4 and TCP SYN IPv6.
- 802.1x re-authentication packets.
- Bitmapped Patterns: Most network adapters can be programmed with bit-mapped pattern filters.
Bitmapped patterns are defined by a bit-map mask and a pattern filter.
As a network packet is received, it is masked using the bitmap mask and then compared to the pattern filter.
If there is a match, then the network adapter wakes the computer.

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterPowerManagementSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterPowerManagementSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[禁用网络适配器电源管理功能](./ Disable-NetAdapterPowerManagement.md)

[Get-NetAdapter](./Get-NetAdapter.md)

[Get-NetAdapterPowerManagement](./Get-NetAdapterPowerManagement.md)

[Set-NetAdapterPowerManagement](./Set-NetAdapterPowerManagement.md)

