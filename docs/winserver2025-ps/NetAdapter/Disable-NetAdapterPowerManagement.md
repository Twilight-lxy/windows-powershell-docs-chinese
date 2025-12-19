---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterPowerManagement.cmdletDefinition.cdxml-help.xml
Module Name: NetAdapter
ms.date: 02/14/2018
online version: https://learn.microsoft.com/powershell/module/netadapter/disable-netadapterpowermanagement?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-NetAdapterPowerManagement
---

# 禁用网卡电源管理功能

## 摘要
禁用网络适配器上的特定电源管理功能。

## 语法

### 按名称查找（默认方式）
```
Disable-NetAdapterPowerManagement [-Name] <String[]> [-IncludeHidden] [-ArpOffload] [-D0PacketCoalescing]
 [-DeviceSleepOnDisconnect] [-NSOffload] [-RsnRekeyOffload] [-SelectiveSuspend] [-WakeOnMagicPacket]
 [-WakeOnPattern] [-NoRestart] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 按实例ID（ByInstanceID）
```
Disable-NetAdapterPowerManagement -InterfaceDescription <String[]> [-IncludeHidden] [-ArpOffload]
 [-D0PacketCoalescing] [-DeviceSleepOnDisconnect] [-NSOffload] [-RsnRekeyOffload] [-SelectiveSuspend]
 [-WakeOnMagicPacket] [-WakeOnPattern] [-NoRestart] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject（cdxml）
```
Disable-NetAdapterPowerManagement -InputObject <CimInstance[]> [-ArpOffload] [-D0PacketCoalescing]
 [-DeviceSleepOnDisconnect] [-NSOffload] [-RsnRekeyOffload] [-SelectiveSuspend] [-WakeOnMagicPacket]
 [-WakeOnPattern] [-NoRestart] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
` Disable-NetAdapterPowerManagement ` cmdlet 用于禁用网络适配器上的特定电源管理功能。如果没有指定任何电源参数，则会禁用所有电源管理功能。

## 示例

### 示例 1：禁用指定网络适配器上的电源管理功能
```
PS C:\> Disable-NetAdapterPowerManagement -Name "Ethernet 1"
```

此命令将禁用名为“Ethernet 1”的网络适配器的电源管理功能，并重新启动该网络适配器。

### 示例 2：使用 InputObject 禁用指定网络适配器的电源管理功能
```
PS C:\> $NetAdapter1 = Get-NetAdapter -Name "Ethernet 3"
PS C:\> Disable-NetAdapterPowerManagement -InputObject $NetAdapter1
```

第一个命令获取名为“Ethernet 3”的网络适配器，并将结果存储在名为$NetAdapter1的变量中。

第二个命令会禁用存储在 `$NetAdapter1` 变量中的网络适配器。

### 示例 3：禁用指定网络适配器的电源管理功能，并且不要重启该适配器
```
PS C:\> Disable-NetAdapterPowerManagement -Name "Ethernet 4" -NoRestart
```

此命令会禁用名为“Ethernet 4”的网络适配器的电源管理功能，并指定该网络适配器不会被重新启动。

## 参数

### -ArpOffload
表示该 cmdlet 可以管理适配器的地址解析协议（ARP）卸载功能。

当计算机处于低功耗模式并使用ARP卸载技术时，它能够将处理传入的ARP协议请求的响应任务卸载给其他组件或系统。

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
以后台作业的形式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job` cmdlets系列命令；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -Confirm
在运行cmdlet之前会提示您确认是否要执行该操作。

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
表示该 cmdlet 管理网络适配器的 D0 数据包聚合功能。

该功能通过减少接收中断的次数来实现电脑的节能。具体来说，它是通过合并随机广播或多播数据包来减少接收中断次数的。这样一来，电脑的处理开销和功耗都得到了显著降低。

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

该功能允许设备在媒体连接断开时进入低功耗待机状态，并在媒体再次连接时唤醒设备。

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
表示该cmdlet在操作过程中会同时考虑可见的网络适配器和隐藏的网络适配器。默认情况下，仅包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串会与所有（无论是隐藏的还是可见的）网络适配器进行匹配。

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
指定要传递给此cmdlet的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给此cmdlet。

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
指定一个网络适配器接口描述的数组。对于物理网络适配器来说，这通常是网络适配器制造商的名称后跟型号和描述，例如 `Contoso 12345 千兆网络设备`。

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

当计算机处于低功耗模式并使用NS卸载技术时，它能够将处理传入的NS协议请求的响应任务卸载出去（即不再由该计算机直接负责这些任务的执行）。

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
表示该cmdlet在完成操作后不会重启网络适配器。许多高级设置需要在新配置生效之前先重启网络适配器。

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
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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
表示该cmdlet用于管理网络适配器的Wi-Fi强密码安全网络（RSN）密钥更新卸载功能。

当计算机进入睡眠状态时，它可以暂停用于无线局域网唤醒（WoWLAN）功能的组临时密钥（GTK）重新加密过程。

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
表示该cmdlet可以管理网络适配器的选择性暂停功能。

网络驱动接口规范（NDIS）中的“选择性挂起”功能允许NDIS通过将网络适配器切换到低功耗状态来使其进入暂停状态。这样一来，计算机就能够降低CPU和网络适配器的能耗开销。

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
该参数用于指定可以同时运行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前执行的命令本身，而不涉及整个会话或整个计算机。

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
表示该cmdlet用于管理网络适配器的“唤醒魔法数据包”（Wake-on-Magic-Packet）功能。

“魔法数据包”是一种广播帧，其有效载荷中包含6个字节的内容，这些内容全部由十六进制数“FF FF FF FF FF FF”组成；之后是目标计算机的48位MAC地址的重复部分，共16次，因此整个数据包的总长度为102字节。

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
表示该cmdlet用于管理网络适配器的“唤醒模式”功能（即通过网络信号来唤醒设备）。

“唤醒模式”（Wake Pattern）指的是用于判断传入的网络流量是否应该使计算机进入激活状态（即“唤醒”状态）的网络数据包过滤器。这些过滤规则可以在网络适配器上启用。

以下唤醒模式可能被网络适配器支持：  
- 唤醒模式：  
  - 在收到新的 TCP 连接时唤醒（适用于 IPv4 和 IPv6，包括 TCP SYN IPv4 以及 TCP SYN IPv6）；  
  - 使用 802.1x 重新认证数据包进行唤醒；  
- 位图模式（Bitmapped Patterns）。  

大多数网络适配器都可以通过编程来配置位图模式过滤器。位图模式由一个位图掩码（bit-map mask）和一个模式过滤器（pattern filter）共同定义。当收到网络数据包时，会使用该位图掩码对数据包进行过滤，然后将其与模式过滤器进行比较；如果匹配成功，网络适配器就会唤醒计算机。

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
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter PowerManagementSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter PowerManagementSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Enable-NetAdapterPowerManagement](./Enable-NetAdapterPowerManagement.md)

[Get-NetAdapter](./Get-NetAdapter.md)

[Get-NetAdapterPowerManagement](./Get-NetAdapterPowerManagement.md)

[Set-NetAdapterPowerManagement](./Set-NetAdapterPowerManagement.md)

