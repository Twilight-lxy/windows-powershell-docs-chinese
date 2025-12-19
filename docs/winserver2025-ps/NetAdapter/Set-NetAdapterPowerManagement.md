---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterPowerManagement.cmdletDefinition.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/set-netadapterpowermanagement?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-NetAdapterPowerManagement
---

# 设置网络适配器的电源管理功能

## 摘要
设置网络适配器的电源管理属性。

## 语法

### 按名称排序（默认设置）
```
Set-NetAdapterPowerManagement [-Name] <String[]> [-IncludeHidden] [-ArpOffload <Setting>]
 [-D0PacketCoalescing <Setting>] [-DeviceSleepOnDisconnect <Setting>] [-NSOffload <Setting>]
 [-RsnRekeyOffload <Setting>] [-SelectiveSuspend <Setting>] [-WakeOnMagicPacket <Setting>]
 [-WakeOnPattern <Setting>] [-NoRestart] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ByInstanceID
```
Set-NetAdapterPowerManagement -InterfaceDescription <String[]> [-IncludeHidden] [-ArpOffload <Setting>]
 [-D0PacketCoalescing <Setting>] [-DeviceSleepOnDisconnect <Setting>] [-NSOffload <Setting>]
 [-RsnRekeyOffload <Setting>] [-SelectiveSuspend <Setting>] [-WakeOnMagicPacket <Setting>]
 [-WakeOnPattern <Setting>] [-NoRestart] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-NetAdapterPowerManagement -InputObject <CimInstance[]> [-ArpOffload <Setting>]
 [-D0PacketCoalescing <Setting>] [-DeviceSleepOnDisconnect <Setting>] [-NSOffload <Setting>]
 [-RsnRekeyOffload <Setting>] [-SelectiveSuspend <Setting>] [-WakeOnMagicPacket <Setting>]
 [-WakeOnPattern <Setting>] [-NoRestart] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-NetAdapterPowerManagement` cmdlet 用于设置网络适配器的电源管理属性。如果只需要更改这些属性的启用状态，可以运行 `Enable-NetAdapterPowerManagement` 或 `Disable-NetAdapterPowerManagement` cmdlet。

## 示例

### 示例 1：在指定的网络适配器上启用“断开连接时让设备进入睡眠状态”功能
```
PS C:\> Set-NetAdapterPowerManagement -Name "Ethernet" -DeviceSleepOnDisconnect Enabled
```

此命令启用名为“Ethernet”的网络适配器的断开连接后自动进入睡眠状态的功能，并重新启动该网络适配器。

## 参数

### -ArpOffload
指定网络适配器的地址解析协议（ARP）卸载功能。

当计算机处于低功耗模式并使用ARP卸载技术时，它能够将处理传入ARP协议请求的响应责任卸载给其他组件。

```yaml
Type: Setting
Parameter Sets: (All)
Aliases:
Accepted values: Enabled, Disabled

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，也可以输入会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

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

### -D0PacketCoalescing
指定网络适配器的D0数据包聚合功能。

该功能通过减少接收中断的次数来实现计算机的节能。它是通过合并随机广播或多播数据包来实现这一目标的。这样一来，计算机的处理开销和功耗都显著降低了。

```yaml
Type: Setting
Parameter Sets: (All)
Aliases:
Accepted values: Enabled, Disabled

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DeviceSleepOnDisconnect
指定网络适配器在断开连接后进入睡眠状态的功能。

该功能使得设备在媒体连接断开时可以进入低功耗待机状态，并在媒体再次连接时自动唤醒。

```yaml
Type: Setting
Parameter Sets: (All)
Aliases:
Accepted values: Enabled, Disabled

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeHidden
该参数表示cmdlet在操作过程中会同时包含可见网络适配器和隐藏网络适配器。默认情况下，只包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将用于匹配所有隐藏和可见的网络适配器。

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
指定要传递给此 cmdlet 的输入数据。你可以使用该参数，也可以将输入数据通过管道（pipe）传递给此 cmdlet。

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
指定一个网络适配器接口描述的数组。对于物理网络适配器而言，这通常是网络适配器的制造商名称后跟型号和描述，例如“Contoso 12345千兆网络设备”。

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
指定网络适配器的邻居请求（Neighbor Solicitation, NS）卸载功能。

当计算机处于低功耗模式并使用NS卸载技术时，它能够将处理传入的NS协议请求的任务卸载出去。

```yaml
Type: Setting
Parameter Sets: (All)
Aliases:
Accepted values: Enabled, Disabled

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
表示该cmdlet在完成操作后不会重启网络适配器。许多高级属性要求在新设置生效之前先重启网络适配器。

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
指定网络适配器的Wi-Fi强安全网络（RSN）密钥更新卸载功能。

当计算机进入睡眠状态时，它可以暂停无线局域网唤醒（WoWLAN）功能相关的临时密钥（GTK）重新加密过程。

```yaml
Type: Setting
Parameter Sets: (All)
Aliases:
Accepted values: Enabled, Disabled

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SelectiveSuspend
指定网络适配器具备选择性暂停（即根据需要暂时停止数据传输）的功能。

网络驱动接口规范（NDIS）中的选择性挂起功能允许NDIS通过将网络适配器切换到低功耗状态来使该适配器进入休眠模式。这样一来，计算机就可以降低处理器和网络适配器的功耗开销。

```yaml
Type: Setting
Parameter Sets: (All)
Aliases:
Accepted values: Enabled, Disabled

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最优限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
指定网络适配器是否支持通过“魔术数据包”（magic packet）来唤醒设备的功能。

“魔法数据包”是一种广播帧，其有效载荷中包含6个字节的全1（用十六进制表示为“FF FF FF FF FF FF”），随后是目标计算机的48位MAC地址的16次重复，总长度为102字节。

```yaml
Type: Setting
Parameter Sets: (All)
Aliases:
Accepted values: Enabled, Disabled

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WakeOnPattern
管理网络适配器的“唤醒模式”功能。

“唤醒模式”（Wake Pattern）指的是用于判断传入的网络流量是否应该使计算机进入活跃状态的网络数据包过滤器。这些模式可以在网络适配器上启用。

以下唤醒模式可能被网络适配器支持：  
- 基于新传入的TCP连接的唤醒模式（适用于IPv4和IPv6，例如TCP SYN IPv4和TCP SYN IPv6）；  
- 802.1x重新认证数据包；  
- 基于位图模式的唤醒方式：大多数网络适配器都可以通过位图模式过滤器进行编程。位图模式由一个位图掩码和一个模式过滤器共同定义。当接收到网络数据包时，会使用该位图掩码对数据包进行处理，然后将其与模式过滤器进行比较；如果匹配成功，网络适配器便会唤醒计算机。

```yaml
Type: Setting
Parameter Sets: (All)
Aliases:
Accepted values: Enabled, Disabled

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

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter PowerManagementSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter PowerManagementSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[禁用网卡电源管理功能](./Disable-NetAdapterPowerManagement.md)

[Enable-NetAdapterPowerManagement](./Enable-NetAdapterPowerManagement.md)

[Get-NetAdapterPowerManagement](./Get-NetAdapterPowerManagement.md)

