---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterRss.cmdletDefinition.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/set-netadapterrss?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-NetAdapterRss
---

# 设置 NetAdapterRss

## 摘要
为网络适配器设置RSS属性。

## 语法

### 按名称排序（默认值）
```
Set-NetAdapterRss [-Name] <String[]> [-IncludeHidden] [-NumberOfReceiveQueues <UInt32>] [-Profile <Profile>]
 [-BaseProcessorGroup <UInt16>] [-BaseProcessorNumber <Byte>] [-MaxProcessorGroup <UInt16>]
 [-MaxProcessorNumber <Byte>] [-MaxProcessors <UInt32>] [-NumaNode <UInt16>] [-Enabled <Boolean>] [-NoRestart]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ByInstanceID
```
Set-NetAdapterRss -InterfaceDescription <String[]> [-IncludeHidden] [-NumberOfReceiveQueues <UInt32>]
 [-Profile <Profile>] [-BaseProcessorGroup <UInt16>] [-BaseProcessorNumber <Byte>]
 [-MaxProcessorGroup <UInt16>] [-MaxProcessorNumber <Byte>] [-MaxProcessors <UInt32>] [-NumaNode <UInt16>]
 [-Enabled <Boolean>] [-NoRestart] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-NetAdapterRss -InputObject <CimInstance[]> [-NumberOfReceiveQueues <UInt32>] [-Profile <Profile>]
 [-BaseProcessorGroup <UInt16>] [-BaseProcessorNumber <Byte>] [-MaxProcessorGroup <UInt16>]
 [-MaxProcessorNumber <Byte>] [-MaxProcessors <UInt32>] [-NumaNode <UInt16>] [-Enabled <Boolean>] [-NoRestart]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-NetAdapterRss` cmdlet 用于设置网络适配器的接收端扩展（RSS）相关属性。RSS 是一种可扩展性技术，它通过哈希传入数据包的头部来将接收到的网络流量分配到多个处理器上。如果禁用了 RSS，所有网络流量都将由单个处理器核心进行处理。随着处理器利用率的增加，这可能会影响网络性能。可以使用各种参数来配置多种属性，从而优化 RSS 的性能。选择用于处理 RSS 流量的处理器是负载均衡的重要环节。该 cmdlet 的大多数参数用于确定 RSS 所使用的处理器。在修改各个参数之前，建议先充分了解 RSS 的工作原理。在大多数情况下，只需选择合适的配置文件即可满足需求。

## 示例

### 示例 1：为没有动态负载均衡功能的 NUMA 服务器设置 RSS 配置文件
```
PS C:\> Set-NetAdapterRss -Name "Ethernet" -Profile NUMAStatic
```

此命令为名为“Ethernet”的网络适配器上的NUMA服务器设置了一个RSS配置文件（该服务器不使用动态负载均衡功能）。

## 参数

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

### -BaseProcessorGroup
指定非统一内存访问（NUMA）节点的基本处理器组。这会影响RSS所使用的处理器阵列。该参数是处理器阵列中出现的所有处理器中的最低组编号。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases: BaseG

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -BaseProcessorNumber
指定 NUMA 节点的基本处理器编号。该参数是来自 *BaseProcessorGroup* 参数的所有处理器中数值最小的那个处理器编号，这些处理器会出现在处理器数组中。这样就可以将处理器分配到不同的网络适配器上。

```yaml
Type: Byte
Parameter Sets: (All)
Aliases: BaseN

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
在运行该cmdlet之前，会提示您确认是否要继续执行。

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

### -Enabled
表示某个界面是否启用了RSS功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeHidden
该参数表示此cmdlet在操作过程中会同时包含可见网络适配器和隐藏网络适配器。默认情况下，仅包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将用于匹配所有（无论是隐藏的还是可见的）网络适配器。

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
指定一个网络适配器接口描述的数组。对于物理网络适配器而言，这通常是由网络适配器的制造商名称后跟型号编号和描述组成的字符串，例如 `Contoso 12345 Gigabit Network Device`。

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

### -MaxProcessorGroup
指定 NUMA 节点的最大处理器组编号。该参数表示与此网络适配器相关的处理器数组中所有处理器的最高组编号。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases: MaxG

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaxProcessorNumber
指定 NUMA 节点的最大处理器数量。该参数等于在该网络适配器的处理器数组中出现的、属于 *MaxProcessorGroup* 参数所定义的任何处理器组中的最高处理器编号。

```yaml
Type: Byte
Parameter Sets: (All)
Aliases: MaxN

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaxProcessors
指定 RSS 从处理器数组中同时使用的最大处理器数量，以实现来自单个网络适配器的负载均衡网络传输。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: Max

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
表示该cmdlet在完成操作后不会重新启动网络适配器。许多高级属性在新设置生效之前需要先重启网络适配器。

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

### -NumaNode
用于指定网络适配器的 NUMA 节点亲和性。这样可以确保在 NUMA 节点内，通过 RSS（资源共享）机制实现网络传输的负载均衡。这不仅会影响内存分配，还会影响处理器阵列中处理器的优先级排序。虽然该设置不会改变处理器阵列中的全部处理器，但可能会影响到 RSS 实际使用的那部分处理器。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NumberOfReceiveQueues
指定每个网络适配器上将用于该接口的接收队列的数量。

```yaml
Type: UInt32
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

### -Profile
指定RSS配置文件（profile）。

此参数的可接受值包括：

- Closest: Behavior is consistent with the behavior of Windows Server® 2008 R2.
- ClosestStatic: No dynamic load balancing, such as distributing but not load balancing at runtime.
- NUMA: Assigns RSS processors in a round robin basis across every NUMA node to enable applications that are running on NUMA servers to scale well.
- NUMAStatic: Default behavior.
RSS processor selection is the same as for NUMA scalability without dynamic load balancing.
- Conservative: RSS uses as few processors as possible to sustain the load.
This option helps reduce the number of interrupts.

```yaml
Type: Profile
Parameter Sets: (All)
Aliases:
Accepted values: Closest, ClosestStatic, NUMA, NUMAStatic, Conservative

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet被运行会发生的结果。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterRssSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）之后的路径表示底层 WMI 对象的命名空间和类名称。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterRssSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）之后的路径表示底层 WMI 对象的命名空间和类名称。

## 备注

## 相关链接

[ Disable-NetAdapterRss ](/Disable-NetAdapterRss.md)

[Enable-NetAdapterRss](./Enable-NetAdapterRss.md)

[Get-NetAdapterRss](./Get-NetAdapterRss.md)

