---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterQos.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/disable-netadapterqos?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-NetAdapterQos
---

# 禁用 NetAdapterQos 功能

## 摘要
禁用网络适配器上的QoS（服务质量）功能。

## 语法

### 按名称排序（默认值）
```
Disable-NetAdapterQos [-Name] <String[]> [-IncludeHidden] [-NoRestart] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ByInstanceID
```
Disable-NetAdapterQos -InterfaceDescription <String[]> [-IncludeHidden] [-NoRestart] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Disable-NetAdapterQos -InputObject <CimInstance[]> [-NoRestart] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Disable-NetAdapterQos** 这个 cmdlet 用于禁用网络适配器上的服务质量（QoS）功能。QoS 功能包括带宽分配和基于优先级的流量控制，这些功能在 IEEE 数据中心桥接（DCB）标准中有所规定。当 QoS 被禁用后，计算机将不再向网络适配器发送任何与 QoS 相关的配置信息。不过，这个 cmdlet 并不会阻止网络适配器自行设置配置或使用其硬件支持的 QoS 功能。

支持DCB（Direct Connect Bus）的网络适配器通常被称为“融合网络适配器”。这类适配器同时具备存储和网络传输的功能。在某些使用场景中，必须启用DCB功能才能实现存储相关的操作。即使从计算机的角度来看网络适配器上的DCB功能被禁用了，该适配器仍然可以在网络环境中正常工作。

## 示例

#### 示例 1：禁用所有网络适配器上的 QoS（服务质量）设置
```
PS C:\> Disable-NetAdapterQos -Name "*"
```

此命令会禁用所有网络适配器上的QoS（服务质量）设置，并重新启动这些网络适配器。

### 示例 2：禁用指定网络适配器上的服务质量（QoS）功能
```
PS C:\> Disable-NetAdapterQos -Name "Ethernet 2"
```

此命令会禁用名为“Ethernet 2”的网络适配器上的服务质量（QoS）设置，并重新启动该网络适配器。

### 示例 3：获取所有支持服务质量（QoS）的网络适配器，并将它们禁用
```
PS C:\> $NetAdapterQoS1 = Get-NetAdapterQos -Name "*"
PS C:\> Disable-NetAdapterQos -InputObject $NetAdapterQoS1
```

第一个命令会获取所有支持QoS（服务质量）的网络适配器，并将结果存储在名为$NetAdapterQoS1的变量中。

第二个命令会禁用所有存储在 $NetAdapterQoS1 中的网络适配器，然后重新启动它们。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -IncludeHidden
表示该 cmdlet 在操作中会包含所有可见和隐藏的网络适配器。默认情况下，仅包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将同时应用于隐藏和可见的网络适配器。

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
指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给此 cmdlet。

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
指定一个网络适配器接口描述数组。对于物理网络适配器来说，这通常是网络适配器的制造商名称后跟型号和描述，例如“Contoso 12345 千兆网络设备”。

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

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算一个最优的流量限制（throttle limit）。这个流量限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterQosSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。输入对象是一组网络适配器对象，例如通过 `Get-NetAdapter` cmdlet 执行后获得的输出结果。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance# ROOT/StandardCimv2/MSFT_NetAdapterQosSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows Management Instrumentation (WMI) 对象。井号 (`#`) 后的路径表示底层 WMI 对象的命名空间和类名。该输出对象包含了网络适配器上的服务质量（QoS）相关功能及配置信息。只有当指定了 `PassThru` 参数时，才会返回这个输出对象。

## 备注

## 相关链接

[Enable-NetAdapterQos](./Enable-NetAdapterQos.md)

[Get-NetAdapter](./Get-NetAdapter.md)

[Get-NetAdapterQos](./Get-NetAdapterQos.md)

