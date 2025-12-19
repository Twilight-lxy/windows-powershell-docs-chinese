---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterLso.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/disable-netadapterlso?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-NetAdapterLso
---

# 禁用 NetAdapterLSO 功能

## 摘要
禁用网络适配器的所有LSO属性（如LSOv4和LSOv6）。

## 语法

### 按名称排序（默认方式）
```
Disable-NetAdapterLso [-Name] <String[]> [-IncludeHidden] [-IPv4] [-IPv6] [-NoRestart] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ByInstanceID
```
Disable-NetAdapterLso -InterfaceDescription <String[]> [-IncludeHidden] [-IPv4] [-IPv6] [-NoRestart]
 [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### InputObject（cdxml）
```
Disable-NetAdapterLso -InputObject <CimInstance[]> [-IPv4] [-IPv6] [-NoRestart] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Disable-NetAdapterLso` cmdlet 用于禁用网络适配器上的大数据包发送卸载（Large Send Offload，简称 LSO）相关设置，例如 LSOv4 和 LSOv6。如果未指定 LSOv4 或 LSOv6，则两者都会被禁用。LSO 是一种技术，它允许网络适配器而不是 TCP/IP 堆栈来负责将数据分割成网络帧的工作。通过使用 LSO，TCP/IP 将非常大的数据包发送给网络适配器驱动程序及硬件，然后由网络适配器将这些数据包拆分成较小的网络帧。这样可以提高大数据包传输的速度，并降低计算机处理器的负担（因为数据处理工作是在网络适配器上完成的）。如果需要单独禁用 LSOv4 或 LSOv6，请运行 `Set-NetAdapterLso` cmdlet。

## 示例

### 示例 1：禁用指定网络适配器上的 IPv6 的 LSO（Link State Optimization）功能
```
PS C:\> Disable-NetAdapterLso -Name "MyAdapter" -IPv6
```

此命令将名为“MyAdapter”的网络适配器上的IPv6协议中的LSO（Link State Optimization，链接状态优化）功能禁用，并重新启动该网络适配器。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -IPv4
表示该 cmdlet 会影响 IPv4 流量。

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
表示该cmdlet会影响IPv6流量。

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
该参数表示该cmdlet在操作过程中会同时包含可见的网络适配器和隐藏的网络适配器。默认情况下，仅包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将匹配所有类型的网络适配器（无论是可见的还是隐藏的）。

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
指定一个网络适配器接口描述的数组。对于物理网络适配器来说，这通常是网络适配器的供应商名称后跟型号和描述，例如 `Contoso 12345 千兆网络设备`。

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
表示该cmdlet在完成操作后不会重新启动网络适配器。许多高级设置需要先重启网络适配器，新的配置才能生效。

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
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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
指定可以同时执行该cmdlet的最大操作数量。如果省略此参数或输入`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值（即并发操作的最多数量）。这个限制仅适用于当前执行的cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter LsoSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter LsoSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Enable-NetAdapterLso](./Enable-NetAdapterLso.md)

[Get-NetAdapterLso](./Get-NetAdapterLso.md)

[Set-NetAdapterLso](./Set-NetAdapterLso.md)

