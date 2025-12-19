---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterLso.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/enable-netadapterlso?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-NetAdapterLso
---

# 启用 NetAdapter LSO 功能

## 摘要
启用网络适配器的LSO（链接共享对象）属性，例如LSOv4和LSOv6。

## 语法

### ByName（默认值）
```
Enable-NetAdapterLso [-Name] <String[]> [-IncludeHidden] [-IPv4] [-IPv6] [-NoRestart] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 按实例ID（ByInstanceID）
```
Enable-NetAdapterLso -InterfaceDescription <String[]> [-IncludeHidden] [-IPv4] [-IPv6] [-NoRestart] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject（cdxml）
```
Enable-NetAdapterLso -InputObject <CimInstance[]> [-IPv4] [-IPv6] [-NoRestart] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-NetAdapterLso` cmdlet 可用于启用网络适配器上的大型数据发送卸载（Large Send Offload，简称 LSO）相关设置，例如 LSOv4 和 LSOv6。如果未指定具体的 LSO 技术（LSOv4 或 LSOv6），则两者都会被同时启用。LSO 是一种技术，它允许网络适配器而不是 TCP/IP 堆栈来负责将数据分段为网络帧的工作。通过使用 LSO，TCP/IP 协议会将非常大的数据包发送给网络适配器驱动程序及相应的硬件；网络适配器会将这些大数据包拆分成更小的网络帧格式。这种方式能够提升高端数据发送操作的效率，并降低计算机处理器的负担（因为相关处理工作是在网络适配器层面完成的）。若仅需要启用 LSOv4 或 LSOv6 中的某一项功能，可以使用 `Set-NetAdapterLso` cmdlet 来进行相应的配置。

## 示例

### 示例 1：在所有可见的网络适配器上为 IPv4 和 IPv6 启用 LSO（链接层安全）功能
```
PS C:\> Enable-NetAdapterLso -Name "*"
```

此命令为所有可见的网络适配器启用 IPv4 和 IPv6 的 LSO（Link State Offload）功能，并重新启动这些网络适配器。

#### 示例 2：为所有可见的网络适配器启用 IPv4 和 IPv6 的 LSO（Link State Optimization）功能
```
PS C:\> Enable-NetAdapterLso -Name "*" -IPv4 -IPv6
```

此命令通过明确指定参数，为所有可见的网络适配器启用IPv4和IPv6的LSO（Link State Oscillation）功能，之后会重启这些网络适配器。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行需要很长时间才能完成的命令。cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用`*-Job` cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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
在运行该 cmdlet 之前，会提示您进行确认。

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

### -IPv4
表示此 cmdlet 会影响 IPv4 流量。

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

### -IPv6
表示此cmdlet会影响IPv6流量。

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
该参数表示该cmdlet在操作过程中会同时考虑可见的网络适配器和隐藏的网络适配器。默认情况下，只包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，那么该通配符字符串将会与所有类型的网络适配器（无论是可见的还是隐藏的）进行匹配。

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

### -InterfaceDescription
指定一个网络适配器接口描述数组。对于物理网络适配器而言，这通常是网络适配器的制造商名称后跟型号和描述，例如“Contoso 12345 千兆网络设备”。

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
表示该cmdlet在完成操作后不会重新启动网络适配器。许多高级属性要求在新设置生效之前先重启网络适配器。

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

### -ThrottleLimit
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或整个计算机。

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
展示了如果该cmdlet被运行时会发生什么情况。但实际上这个cmdlet并没有被运行。

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

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterLsoSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterLsoSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[禁用网卡LSO功能](./ Disable-NetAdapterLso.md)

[Get-NetAdapterLso](./Get-NetAdapterLso.md)

[Set-NetAdapterLso](./Set-NetAdapterLso.md)

