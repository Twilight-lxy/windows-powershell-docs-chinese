---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterChecksumOffload.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/enable-netadapterchecksumoffload?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-NetAdapterChecksumOffload
---

# 启用 NetAdapter 的校验和卸载功能（checksum offloading）

## 摘要
启用网络适配器上的校验和卸载功能。

## 语法

### 按名称查找（默认值）
```
Enable-NetAdapterChecksumOffload [-Name] <String[]> [-IncludeHidden] [-IpIPv4] [-TcpIPv4] [-TcpIPv6] [-UdpIPv4]
 [-UdpIPv6] [-NoRestart] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 按实例ID（ByInstanceID）
```
Enable-NetAdapterChecksumOffload -InterfaceDescription <String[]> [-IncludeHidden] [-IpIPv4] [-TcpIPv4]
 [-TcpIPv6] [-UdpIPv4] [-UdpIPv6] [-NoRestart] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject（cdxml）
```
Enable-NetAdapterChecksumOffload -InputObject <CimInstance[]> [-IpIPv4] [-TcpIPv4] [-TcpIPv6] [-UdpIPv4]
 [-UdpIPv6] [-NoRestart] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
**Enable-NetAdapterChecksumOffload** cmdlet 可用于启用网络适配器上的校验和卸载功能。当指定 IPv4、TCPv4 或 TCPv6 时，可以分别针对传输方向、接收方向或两者同时启用该功能。默认情况下，所有方向的校验和都会被启用。物理网络适配器支持多种校验和卸载机制，在这些机制中，校验和的计算会在网络适配器本身完成，而无需通过主处理器进行处理。这样做可以降低处理器的负载，并提高网络吞吐量。该 cmdlet 支持对 IPv4、TCPv4、TCPv6、UDPv4 和 UDPv6 的校验和卸载设置进行配置。此外，校验和卸载对于其他无状态卸载功能（如接收端扩展 (RSS)、接收数据段合并 (RSC) 和大包发送卸载 (LSO)）的正常运行也是必需的。

## 示例

### 示例 1：在所有网络适配器上启用 IPv4 校验和卸载功能
```
PS C:\> Enable-NetAdapterChecksumOffload -Name "*" -TcpIPv4 -UdpIPv4 -IpIPv4
```

此命令会启用所有可见网络适配器上的IPv4校验和卸载功能，并重新启动这些网络适配器。

### 示例 2：在所有网络适配器上启用所有的校验和卸载功能
```
PS C:\> Enable-NetAdapterChecksumOffload -Name "*"
```

此命令会启用所有可见网络适配器上的所有校验和卸载功能，并重新启动这些网络适配器。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行耗时较长的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
该参数表示该 cmdlet 在操作过程中会同时包含可见网络适配器和隐藏网络适配器。默认情况下，仅包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将匹配所有隐藏和可见的网络适配器。

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
指定要传递给此 cmdlet 的输入数据。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该 cmdlet。

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
用于指定一组网络适配器接口的描述。对于物理网络适配器来说，这通常是指网络适配器的制造商名称后跟型号编号和描述，例如“Contoso 12345 千兆网络设备”。

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

### -IpIPv4
表示此cmdlet支持对IPv4流量进行校验和卸载（即不计算校验和，而是将校验和计算任务委托给其他系统或进程）。

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
这表示该cmdlet在完成操作后不会重启网络适配器。许多高级属性要求在新的设置生效之前先重启网络适配器。

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

### -TcpIPv4
表示该cmdlet支持对TCP IPv4流量启用校验和卸载（checksum offloading）功能。

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

### -TcpIPv6
表示该cmdlet支持对TCP IPv6流量进行校验和卸载（即避免在传输过程中计算校验和）。

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
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -UdpIPv4
表示该cmdlet支持对UDP IPv4流量进行校验和卸载（即不计算校验和，而是将校验和计算任务委托给其他系统或进程）。

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

### -UdpIPv6
表示该cmdlet支持对UDP IPv6流量进行校验和卸载（即在校验和计算过程中将相关任务分配给其他系统或进程来处理）。

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被执行。

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

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter ChecksumOffloadSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter ChecksumOffloadSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

## 备注

## 相关链接

[禁用网络适配器校验和卸载功能](./Disable-NetAdapterChecksumOffload.md)

[Get-NetAdapterChecksumOffload](./Get-NetAdapterChecksumOffload.md)

[Set-NetAdapterChecksumOffload](./Set-NetAdapterChecksumOffload.md)

