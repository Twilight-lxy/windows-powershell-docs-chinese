---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterVmq.cmdletDefinition.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/set-netadaptervmq?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-NetAdapterVmq
---

# Set-NetAdapterVmq

## 摘要
设置网络适配器的虚拟消息队列（VMQ）属性。

## 语法

### 按名称排序（默认值）
```
Set-NetAdapterVmq [-Name] <String[]> [-IncludeHidden] [-BaseProcessorGroup <UInt16>]
 [-BaseProcessorNumber <Byte>] [-MaxProcessors <UInt32>] [-MaxProcessorNumber <Byte>] [-NumaNode <UInt16>]
 [-Enabled <Boolean>] [-NoRestart] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 按实例ID（ByInstanceID）
```
Set-NetAdapterVmq -InterfaceDescription <String[]> [-IncludeHidden] [-BaseProcessorGroup <UInt16>]
 [-BaseProcessorNumber <Byte>] [-MaxProcessors <UInt32>] [-MaxProcessorNumber <Byte>] [-NumaNode <UInt16>]
 [-Enabled <Boolean>] [-NoRestart] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-NetAdapterVmq -InputObject <CimInstance[]> [-BaseProcessorGroup <UInt16>] [-BaseProcessorNumber <Byte>]
 [-MaxProcessors <UInt32>] [-MaxProcessorNumber <Byte>] [-NumaNode <UInt16>] [-Enabled <Boolean>] [-NoRestart]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-NetAdapterVmq` cmdlet 用于设置网络适配器的虚拟机队列（VMQ）属性。VMQ 是一种适用于 Hyper-V 交换机的可扩展网络技术，它通过将多个虚拟机器的网络流量处理分配到多个处理器上来提升网络吞吐量。在使用此 cmdlet 修改任何默认值之前，强烈建议先详细了解 VMQ 及其相关特性。

## 示例

#### 示例 1：在指定的网络适配器上启用 VMQ
```
PS C:\> Set-NetAdapterVmq -Name "MyAdapter" -Enabled $True
```

此命令用于在名为“MyAdapter”的网络适配器上启用VMQ（Virtual Message Queue）功能。**Enable-NetAdapterVmq** cmdlet是执行此操作的首选工具。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlet；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
指定 VMQ 将使用的处理器组。对于拥有超过 64 个逻辑处理器的系统，支持是基于“处理器组”的概念实现的；处理器组是一组静态的、最多包含 64 个逻辑处理器的集合。处理器组的编号从 0 开始。拥有少于 64 个逻辑处理器的计算机总是只有一个处理器组，即第 0 组。

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
指定在虚拟机队列（VMQ）的处理器组中使用的起始处理器。对于拥有超过64个逻辑处理器的系统，支持是基于“处理器组”这一概念实现的；处理器组是一组静态设置的、最多包含64个逻辑处理器的集合。处理器组的编号从0开始。拥有少于64个逻辑处理器的计算机总是只有一个处理器组，即第0组。逻辑处理器通过`BaseProcessorGroup`参数来标识其所属的组号，并通过该参数结合组内相对编号来确定具体的处理器序号。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如，通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Enabled
表示是否启用了VMQ（Virtual Message Queue）。该参数的有效取值为：$True 或 $False。

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
该参数表示该 cmdlet 在操作中会同时包含可见的网络适配器和隐藏的网络适配器。默认情况下，仅包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将会与所有（无论是隐藏的还是可见的）网络适配器进行匹配。

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
指定该 cmdlet 的输入内容。您可以使用此参数，也可以将输入数据通过管道（pipe）传递给该 cmdlet。

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
指定一个网络适配器接口描述数组。对于物理网络适配器来说，这通常是网络适配器制造商的名称后跟型号和描述，例如“Contoso 12345 千兆网络设备”。

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

### -MaxProcessorNumber
指定组中最大的处理器数量。

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
指定虚拟消息队列（VMQ）在负载均衡网络传输过程中使用的最大处理器数量。

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
指定优先使用的非一致性内存访问（NUMA）节点，以便分配到该网络适配器上的虚拟磁盘队列（VMQs）能够更好地利用该节点的资源。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases: NumaN

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您当前正在操作的项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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
该参数用于指定可以同时执行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或整个计算机。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterVmqSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterVmqSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[ Disable-NetAdapterVmq](./Disable-NetAdapterVmq.md)

[Enable-NetAdapterVmq](./Enable-NetAdapterVmq.md)

[Get-NetAdapterVmq](./Get-NetAdapterVmq.md)

[Get-NetAdapterVmqQueue](./Get-NetAdapterVmqQueue.md)

