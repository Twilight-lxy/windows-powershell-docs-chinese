---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterQos.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadapterqos?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapterQos
---

# Get-NetAdapterQos

## 摘要
获取网络适配器的服务质量（QoS）属性，特别是直流电平衡（DCB）设置。

## 语法

### 按名称排序（默认设置）
```
Get-NetAdapterQos [[-Name] <String[]>] [-IncludeHidden] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

### ByInstanceID
```
Get-NetAdapterQos -InterfaceDescription <String[]> [-IncludeHidden] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
**Get-NetAdapterQos** 这个 cmdlet 可以获取支持 DCB（Data Center Bridging）的网络适配器的服务质量 (QoS) 功能以及运行时配置信息。如果 QOS 被禁用，那么该 cmdlet 仅能获取网络适配器的硬件级 QoS 功能；如果 QOS 被启用，它还会同时显示流量分类和流控制配置信息。此外，如果该网络适配器支持 DCB Exchange 协议，并且连接到了同样支持该协议的交换机，那么该 cmdlet 还能够返回交换机上的 QoS 配置信息。

如果网络适配器不支持服务质量（QoS），特别是DCB（Data Center Bridging）功能，那么这个cmdlet将不会返回任何信息。

## 示例

### 示例 1：显示已启用 QoS 的网络适配器的硬件 QoS 功能和运行时配置
```
PS C:\> Get-NetAdapterQos -Name "*" | Where-Object -FilterScript { $_.Enabled }
Name                       : DCBADAPTER1
Enabled                    : True
Capabilities               :                       Hardware     Current
--------     -------
MacSecBypass        : NotSupported NotSupported
DcbxSupport         : IEEE         None
NumTCs(Max/ETS/PFC) : 8/8/8        8/8/8
OperationalTrafficClasses  : TC TSA    Bandwidth Priorities
-- ---    --------- ----------
0  ETS           40 0-3,5-7
1  ETS           60 4

OperationalFlowControl     : Priority 4 Enabled
OperationalClassifications : Not Available
```

此命令用于显示已启用QoS的网络适配器的硬件QoS功能以及运行时QoS配置。

### 示例 2：显示网络适配器的硬件服务质量（QoS）功能，即使这些适配器的 QoS 功能已被禁用
```
PS C:\> Get-NetAdapterQos -Name "*" | Where-Object -FilterScript { $_.Enabled -Eq "False" }
Name         : DCBADAPTER1
Enabled      : False
Capabilities :                       Hardware     Current
--------     -------
MacSecBypass        : NotSupported NotSupported
DcbxSupport         : None         None
NumTCs(Max/ETS/PFC) : 8/8/8        0/0/0
```

此命令仅显示已禁用QoS功能的网络适配器的硬件QoS（服务质量）支持能力。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job` cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

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

### -IncludeHidden
该参数表示此cmdlet在操作过程中会同时包含可见网络适配器和隐藏网络适配器。默认情况下，仅包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将用于匹配所有网络适配器（无论是可见的还是隐藏的）。

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
指定一个网络适配器接口描述数组。对于物理网络适配器而言，这通常是网络适配器的制造商名称后跟型号和描述，例如 `Contoso 12345 千兆网络设备`。

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算一个最优的节流限制（即并发操作的数量上限）。这个节流限制仅适用于当前的 cmdlet，而不适用于整个会话或整个计算机。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterQosSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）之后的路径表示底层 WMI 对象的命名空间和类名。该输出对象包含了网络适配器上的服务质量（QoS）相关功能和配置信息。

## 备注

## 相关链接

[禁用网卡QoS功能](./Disable-NetAdapterQos.md)

[Enable-NetAdapterQos](./Enable-NetAdapterQos.md)

[Set-NetAdapterQos](./Set-NetAdapterQos.md)

