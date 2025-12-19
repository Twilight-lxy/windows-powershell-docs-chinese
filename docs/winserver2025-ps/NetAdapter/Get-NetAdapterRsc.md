---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterRsc.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadapterrsc?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapterRsc
---

# Get-NetAdapterRsc

## 摘要
获取支持 RSC 的网络适配器。

## 语法

### 按名称排序（默认设置）
```
Get-NetAdapterRsc [[-Name] <String[]>] [-IPv4OperationalState <Boolean[]>] [-IPv6OperationalState <Boolean[]>]
 [-IPv4FailureReason <FailureReason[]>] [-IPv6FailureReason <FailureReason[]>] [-IncludeHidden]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 按实例ID（ByInstanceID）
```
Get-NetAdapterRsc -InterfaceDescription <String[]> [-IPv4OperationalState <Boolean[]>]
 [-IPv6OperationalState <Boolean[]>] [-IPv4FailureReason <FailureReason[]>]
 [-IPv6FailureReason <FailureReason[]>] [-IncludeHidden] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

## 描述
`Get-NetAdapterRsc` cmdlet 用于获取支持接收数据段合并（Receive Segment Coalescing，简称 RSC）功能的网络适配器。RSC 技术会将同一中断周期内接收到的多个数据包合并成一个较大的数据包，然后由网络堆栈进行处理。这样不仅可以降低数据包处理的开销，还能减少处理器所需的循环次数，从而提高系统的可扩展性。

## 示例

### 示例 1：获取指定网络适配器的 RSC 属性
```
PS C:\> Get-NetAdapterRsc -Name "MyAdapter"
```

这条命令用于获取名为“MyAdapter”的网络适配器的RSC属性。

#### 示例 2：获取所有支持 RSC（Remote Switching Capability）的网络适配器
```
PS C:\> Get-NetAdapterRsc -Name "*"
```

这个命令可以获取所有支持RSC（Remote Secure Computing）功能的网络适配器。

#### 示例 3：获取所有支持 RSC（Remote Storage Controller）功能的网络适配器，并检查这些适配器的 RSC 功能是否已启用
```
PS C:\> Get-NetAdapterRsc -Name "*" | Where-Object -FilterScript { $_.Enabled }
```

这个命令可以获取所有启用了RSC功能、且支持RSC协议的网络适配器。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，随后再显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称，或者一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -IPv4FailureReason
说明了为什么RSC可能无法处理IPv4流量。

该参数的可接受值包括：

- NoFailure
- NicPropertyDisabled
- WFPCompatibility
- NDISCompatibility
- ForwardingEnabled
- NetOffloadGlobalDisabled

```yaml
Type: FailureReason[]
Parameter Sets: (All)
Aliases:
Accepted values: NoFailure, NicPropertyDisabled, WFPCompatibility, NDISCompatibility, ForwardingEnabled, NetOffloadGlobalDisabled, Capability, Unknown

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IPv4OperationalState
Specifies the state of the TCP/IP protocol driver for RSC.
See the *IPv4FailureReason* parameter value for more information.

```yaml
Type: Boolean[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IPv6FailureReason
Returns the reason that of RSC may not be working on IPv6 traffic.

该参数的可接受值包括：

- NoFailure
- NicPropertyDisabled
- WFPCompatibility
- NDISCompatibility
- ForwardingEnabled
- NetOffloadGlobalDisabled

If RSC is desired, then the following actions can be taken:

- NicPropertyDisabled: Run the **Enable-NetAdapterRsc** cmdlet to enable RSC on the specified network adapter.
- WFPCompatibility: Disable the WFP filters.
- NDISCompatibility: Upgrade to an NDIS 6.30 driver.
- ForwardingEnabled: Disable forwarding.
- NetOffloadGlobalDisabled: Run the **Set-NetOffloadGlobalSetting** cmdlet with the *ReceiveSegmentCoalescing* parameter set to Enabled.

```yaml
Type: FailureReason[]
Parameter Sets: (All)
Aliases:
Accepted values: NoFailure, NicPropertyDisabled, WFPCompatibility, NDISCompatibility, ForwardingEnabled, NetOffloadGlobalDisabled, Capability, Unknown

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IPv6OperationalState
Specifies the state of the TCP/IP protocol driver for RSC.
See the *IPv6FailureReason* parameter value for more information.

```yaml
Type: Boolean[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IncludeHidden
这表示该cmdlet在操作过程中会同时考虑可见网络适配器和隐藏网络适配器。默认情况下，仅包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将会与所有网络适配器（无论是可见的还是隐藏的）进行匹配。

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

### -InterfaceDescription
指定一个网络适配器接口描述数组。对于物理网络适配器而言，这些描述通常包括网络适配器的厂商名称、型号以及相关说明，例如“Contoso 12345 千兆网络设备”。

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

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该命令的最佳限制次数。此限制仅适用于当前执行的命令，而不适用于整个会话或计算机本身。

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

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterRscSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[disable-NetAdapterRsc](./ Disable-NetAdapterRsc.md)

[Enable-NetAdapterRsc](./Enable-NetAdapterRsc.md)

[Set-NetAdapterRsc](./Set-NetAdapterRsc.md)

