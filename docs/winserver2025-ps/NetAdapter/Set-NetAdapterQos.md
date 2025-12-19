---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterQos.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/set-netadapterqos?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-NetAdapterQos
---

# 设置 NetAdapterQoS

## 摘要
为网络适配器设置服务质量（QoS）属性。

## 语法

### ByName（默认值）
```
Set-NetAdapterQos [-Name] <String[]> [-IncludeHidden] [-Enabled <Boolean>] [-NoRestart]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ByInstanceID
```
Set-NetAdapterQos -InterfaceDescription <String[]> [-IncludeHidden] [-Enabled <Boolean>] [-NoRestart]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-NetAdapterQos -InputObject <CimInstance[]> [-Enabled <Boolean>] [-NoRestart] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-NetAdapterQos` cmdlet 用于设置网络适配器上的服务质量（QoS）属性，特别是数据中心桥接（DCB）相关配置。目前，该 cmdlet 仅支持启用或禁用网络适配器上的 QoS 功能。此外，也可以使用 `Enable-NetAdapterQos` 和 `DisableNetAdapterQos` cmdlets 来完成相同操作。

## 示例

### 示例 1：在指定的网络适配器上启用服务质量（QoS）
```
PS C:\> Set-NetAdapterQos -Name "DCBAdapter2" -Enabled $True
```

此命令用于为名为“DCBAdapter2”的网络适配器启用服务质量（QoS）功能。`Enable-NetAdapterQos` cmdlet是执行此操作的首选工具。

### 示例 2：禁用指定网络适配器上的服务质量（QoS）功能
```
PS C:\> Set-NetAdapterQos -Name "DCBAdapter2" -Enabled $False
```

此命令将名为“DCBAdapter2”的网络适配器上的QoS（服务质量）功能禁用。用于执行此操作的推荐cmdlet是**Disable-NetAdapterQos**。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成的过程中，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -Enabled
该参数用于指示网络适配器上的 QoS（服务质量）设置是否已启用。有关更多详细信息，请参阅 **Enable-NetAdapterQos** 和 **Disable-NetAdapterQos** cmdlets；将此参数设置为 True 等同于使用 **Enable-NetAdapterQos** cmdlet，将其设置为 False 则等同于使用 **Disable-NetAdapterQos** cmdlet。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IncludeHidden
这表示该cmdlet在操作过程中会同时考虑可见网络适配器和隐藏网络适配器。默认情况下，仅包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，那么该通配符字符串将会与所有（无论是隐藏的还是可见的）网络适配器进行匹配。

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
指定要输入到此 cmdlet 的数据。您可以使用这个参数，也可以将数据通过管道（pipe）传递给该 cmdlet。

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
指定一个网络适配器接口描述的数组。对于物理网络适配器来说，这通常是网络适配器供应商的名称后跟型号和描述，例如 `Contoso 12345 千兆网络设备`。

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
这表示该cmdlet在完成操作后不会重新启动网络适配器。许多高级属性要求在新的设置生效之前重新启动网络适配器。

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
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入`0`，Windows PowerShell®将根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值（即并发操作的最大数量）。这个限制仅适用于当前正在运行的cmdlet，而不适用于整个会话或整个计算机。

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
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows Management Instrumentation (WMI) 对象。符号 `#` 后的路径表示底层 WMI 对象的命名空间和类名。输入对象是一组网络适配器对象，例如通过 **Get-NetAdapter** cmdlet 所获得的输出结果。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterQosSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows Management Instrumentation (WMI) 对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。该输出对象包含了网络适配器上的服务质量（QoS）相关功能及配置信息。只有当指定了 `PassThru` 参数时，才会返回这个输出对象。

## 备注

## 相关链接

[禁用网络适配器服务质量（Disable-NetAdapterQos）](./Disable-NetAdapterQos.md)

[Enable-NetAdapterQos](./Enable-NetAdapterQos.md)

[Get-NetAdapter](./Get-NetAdapter.md)

[Get-NetAdapterQos](./Get-NetAdapterQos.md)

