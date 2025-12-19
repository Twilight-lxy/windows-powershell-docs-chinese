---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterQos.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/enable-netadapterqos?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-NetAdapterQos
---

# 启用 NetAdapterQoS 功能

## 摘要
在网络适配器上启用服务质量（QoS），特别是DCB（Data Center Bridge）功能。

## 语法

### 按名称排序（默认设置）
```
Enable-NetAdapterQos [-Name] <String[]> [-IncludeHidden] [-NoRestart] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 按实例ID（ByInstanceID）
```
Enable-NetAdapterQos -InterfaceDescription <String[]> [-IncludeHidden] [-NoRestart] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Enable-NetAdapterQos -InputObject <CimInstance[]> [-NoRestart] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-NetAdapterQos` cmdlet 可以为网络适配器启用服务质量 (QoS) 功能。这些 QoS 功能包括流量类别带宽分配和基于优先级的流控制，其具体规范位于 IEEE 数据中心桥接 (DCB) 标准中。当 QoS 被启用且计算机被配置为不接受来自远程设备的配置时，计算机会将用户自定义的 QoS 配置发送给网络适配器。有关如何配置计算机以拒绝接收远程设备提供的配置的更多信息，请参阅 `Set-NetQosDcbxSetting` cmdlet。在其他情况下，网络适配器会根据出厂默认配置或从远程设备接收到的配置来启用相应的 QoS 功能。

要在计算机上配置流量类带宽分配以及基于优先级的流控功能，您可以使用 `New-NetQosTrafficClass` 和 `Enable-NetQosFlowControl` 这两个 cmdlet。

有些交换机要求终端设备（例如运行 Windows Server® 2012 或更高版本的计算机）能够接收来自交换机的配置信息。如果交换机通过数据中心桥接交换（DCBX）协议检测到配置不匹配的情况，它们会禁用 DCBX 功能。为了克服这一限制，用户可以在交换机或网络适配器上禁用 DCBX 功能，并手动配置两端的相应设置。

## 示例

### 示例 1：在指定的网络适配器上启用服务质量（QoS）
```
PS C:\> Enable-NetAdapterQos -Name "DCBNIC1"
```

此命令为名为“DCBNIC1”的网络适配器启用服务质量（QoS）功能，并重新启动该网络适配器。

#### 示例 2：在所有支持 QoS 的网络适配器上启用 QoS 功能
```
This command gets all network adapters that support QoS, enables QoS on all of them, and restarts the network adapter.
PS C:\> $NetAdapter1 = Get-NetAdapterQos -Name "*"
PS C:\> Enable-NetAdapterQos -InputObject $NetAdapter1

This command is a version of the cmdlet that gets all network adapters that support QoS and enables QoS on all of them via the pipeline, then restarts the network adapter.
PS C:\> Get-NetAdapterQos -Name "*" | Enable-NetAdapterQos
```

## 参数

### -AsJob
该 cmdlet 以后台作业的形式运行。使用此参数来执行那些需要较长时间才能完成的命令。cmdlet 会立即返回一个表示该作业的对象，随后会显示命令提示符。在作业完成期间，您可以继续在同一会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlet；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
该参数表示该cmdlet在操作过程中会同时包含可见网络适配器和隐藏网络适配器。默认情况下，仅包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将用于匹配所有类型的网络适配器（无论是隐藏的还是可见的）。

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
指定一个网络适配器接口描述数组。对于物理网络适配器而言，这通常表示网络适配器的厂商名称后跟型号编号和描述，例如“Contoso 12345 千兆网络设备”。

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
表示该cmdlet在完成操作后不会重新启动网络适配器。许多高级属性要求在新的设置生效之前重新启动网络适配器。

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterQosSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows Management Instrumentation (WMI) 对象。井号 (`#`) 后面的路径表示底层 WMI 对象的命名空间和类名。输入对象是一组网络适配器对象，例如通过 `Get-NetAdapter` cmdlet 所获得的输出结果。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterQosSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows Management Instrumentation (WMI) 对象。井号（`#`）之后的路径表示底层 WMI 对象的命名空间和类名。该输出对象包含了网络适配器的相关服务质量（QoS）功能及配置信息。只有当指定了 `PassThru` 参数时，才会返回这个输出对象。

## 备注

## 相关链接

[禁用网络适配器服务质量（Disable-NetAdapterQos）](./ Disable-NetAdapterQos.md)

[Get-NetAdapter](./Get-NetAdapter.md)

[Get-NetAdapterQos](./Get-NetAdapterQos.md)

