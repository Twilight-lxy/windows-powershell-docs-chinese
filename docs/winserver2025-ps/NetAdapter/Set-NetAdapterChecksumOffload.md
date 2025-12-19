---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterChecksumOffload.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/set-netadapterchecksumoffload?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-NetAdapterChecksumOffload
---

# 将 NetAdapter 的校验和卸载功能设置为关闭（Set-NetAdapterChecksumOffload）

## 摘要
设置各种校验和卸载相关选项。

## 语法

### 按名称排序（默认值）
```
Set-NetAdapterChecksumOffload [-Name] <String[]> [-IncludeHidden] [-IpIPv4Enabled <Direction>]
 [-TcpIPv4Enabled <Direction>] [-TcpIPv6Enabled <Direction>] [-UdpIPv4Enabled <Direction>]
 [-UdpIPv6Enabled <Direction>] [-NoRestart] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ByInstanceID
```
Set-NetAdapterChecksumOffload -InterfaceDescription <String[]> [-IncludeHidden] [-IpIPv4Enabled <Direction>]
 [-TcpIPv4Enabled <Direction>] [-TcpIPv6Enabled <Direction>] [-UdpIPv4Enabled <Direction>]
 [-UdpIPv6Enabled <Direction>] [-NoRestart] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject（cdxml）
```
Set-NetAdapterChecksumOffload -InputObject <CimInstance[]> [-IpIPv4Enabled <Direction>]
 [-TcpIPv4Enabled <Direction>] [-TcpIPv6Enabled <Direction>] [-UdpIPv4Enabled <Direction>]
 [-UdpIPv6Enabled <Direction>] [-NoRestart] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-NetAdapterChecksumOffload` cmdlet 用于设置校验和卸载（checksum offloading）功能的状态。网络适配器本身会负责计算校验和，从而减少了处理器的负担（因为处理器无需再执行这些计算任务）。该 cmdlet 可配置 IPv4、TCPv4、TCPv6、UDPv4 和 UDPv6 等协议的校验和卸载相关设置；它可以在某些情况下启用某些类型的校验和功能，同时禁用其他类型的功能。如果仅需要更改启用的状态，可以直接运行 `Enable-NetAdapterChecksumOffload` 或 `Disable-NetAdapterChecksumOffload` cmdlet。

## 示例

#### 示例 1：在所有网络适配器上，为接收和发送方向启用 IPv4 校验和功能
```
PS C:\> Set-NetAdapterChecksumOffload -Name "*" -IpIPv4Enabled RxTxEnabled
```

此命令为所有可见的网络适配器启用IPv4校验和卸载功能（即允许将校验和计算任务卸载到硬件设备上），适用于接收和发送方向。

### 示例 2：在所有网络适配器上，启用接收和发送方向的 IPv4、UDPv4 以及 TCPv4 校验和功能
```
PS C:\> Set-NetAdapterChecksumOffload -Name "MyAdapter" -IpIPv4Enabled RxTxEnabled -TcpIpv4Enabled RxTxEnabled -UdpIpv4Enabled RxTxEnabled
```

此命令在名为“MyAdapter”的网络适配器上，启用IPv4校验和、UDPv4校验和以及TCPv4校验和的功能，并且这些功能同时支持接收方向和发送方向。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行耗时较长的命令。该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用`*-Job`系列cmdlet；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -IncludeHidden
该参数表示此cmdlet在操作过程中会同时包含可见的网络适配器和隐藏的网络适配器。默认情况下，仅包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串会与所有（无论是可见的还是隐藏的）网络适配器进行匹配。

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
指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给该 cmdlet。

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
指定一个网络适配器接口描述数组。对于物理网络适配器来说，这通常是指网络适配器的供应商名称后跟型号和描述，例如 `Contoso 12345 千兆网络设备`。

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

### -IpIPv4Enabled
用于指定IPv4协议的IP流量的方向。该参数的可接受值包括：

- Disabled
- RxTxEnabled
- RxEnabled
- TxEnabled.

如果选择了“RxEnabled”或“TxEnabled”，那么相反的方向（分别对应发送或接收）就会被禁用。例如，当状态为“RxEnabled”时，接收数据的校验和计算是启用的，而发送数据的校验和计算则被禁用。

```yaml
Type: Direction
Parameter Sets: (All)
Aliases:
Accepted values: Disabled, TxEnabled, RxEnabled, RxTxEnabled

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
Specifies an array of network adapter names.

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
Indicates that the cmdlet does not restart the network adapter after completing the operation.
Many advanced properties require restarting the network adapter before the new settings take effect.

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
Returns an object representing the item with which you are working.
By default, this cmdlet does not generate any output.

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

### -TcpIPv4Enabled
Specifies the direction of the TCP traffic for IPv4.
The acceptable values for this parameter are:

- Disabled
- RxTxEnabled
- RxEnabled
- TxEnabled

如果选择了“RxEnabled”或“TxEnabled”，那么相反的方向（分别对应发送或接收）就会被禁用。例如，当状态为“RxEnabled”时，接收数据的校验和计算是启用的，而发送数据的校验和计算则被禁用。

```yaml
Type: Direction
Parameter Sets: (All)
Aliases:
Accepted values: Disabled, TxEnabled, RxEnabled, RxTxEnabled

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TcpIPv6Enabled
Specifies the direction of the TCP traffic for IPv6.
The acceptable values for this parameter are:

- Disabled
- RxTxEnabled
- RxEnabled
- TxEnabled

如果选择了“RxEnabled”或“TxEnabled”，那么相反的方向（分别对应发送或接收）就会被禁用。例如，当状态为“RxEnabled”时，接收数据的校验和计算是启用的，而发送数据的校验和计算则被禁用。

```yaml
Type: Direction
Parameter Sets: (All)
Aliases:
Accepted values: Disabled, TxEnabled, RxEnabled, RxTxEnabled

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
Specifies the maximum number of concurrent operations that can be established to run the cmdlet.
If this parameter is omitted or a value of `0` is entered, then Windows PowerShell® calculates an optimum throttle limit for the cmdlet based on the number of CIM cmdlets that are running on the computer.
The throttle limit applies only to the current cmdlet, not to the session or to the computer.

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

### -UdpIPv4Enabled
Specifies the direction of the UDP traffic for IPv4.
The acceptable values for this parameter are:

- Disabled
- RxTxEnabled
- RxEnabled
- TxEnabled

如果选择了“RxEnabled”或“TxEnabled”，那么相反的方向（分别对应发送或接收）就会被禁用。例如，当状态为“RxEnabled”时，接收数据的校验和计算是启用的，而发送数据的校验和计算则被禁用。

```yaml
Type: Direction
Parameter Sets: (All)
Aliases:
Accepted values: Disabled, TxEnabled, RxEnabled, RxTxEnabled

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UdpIPv6Enabled
Specifies the direction of the UDP traffic for IPv6.
The acceptable values for this parameter are:

- Disabled
- RxTxEnabled
- RxEnabled
- TxEnabled.

如果选择了“RxEnabled”或“TxEnabled”，那么相反的方向（分别对应发送或接收）就会被禁用。例如，当状态为“RxEnabled”时，接收数据的校验和计算是启用的，而发送数据的校验和计算则被禁用。

```yaml
Type: Direction
Parameter Sets: (All)
Aliases:
Accepted values: Disabled, TxEnabled, RxEnabled, RxTxEnabled

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter ChecksumOffloadSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter ChecksumOffloadSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Disable-NetAdapterChecksumOffload](./Disable-NetAdapterChecksumOffload.md)

[Enable-NetAdapterChecksumOffload](./Enable-NetAdapterChecksumOffload.md)

[Get-NetAdapterChecksumOffload](./Get-NetAdapterChecksumOffload.md)

