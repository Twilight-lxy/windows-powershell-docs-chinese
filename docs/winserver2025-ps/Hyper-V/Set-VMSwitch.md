---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmswitch?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMSwitch
---

# Set-VMSwitch

## 摘要
配置一个虚拟交换机。

## 语法

### SwitchName_SwitchType（默认值）
```
Set-VMSwitch [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String[]> [-SwitchType <VMSwitchType>] [-AllowManagementOS <Boolean>]
 [-默认值；标准设置FlowMinimumBandwidthAbsolute <Int64>] [-默认值；标准设置FlowMinimumBandwidthWeight <Int64>]
 [-默认值；标准设置QueueVrssEnabled <Boolean>] [-默认值；标准设置QueueVmmqEnabled <Boolean>]
 [-默认值；标准设置QueueVmmqQueuePairs <UInt32>] [-Extensions <VMSwitchExtension[]>] [-Notes <String>] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SwitchObject_SwitchType
```
Set-VMSwitch [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMSwitch] <VMSwitch[]> [-SwitchType <VMSwitchType>] [-AllowManagementOS <Boolean>]
 [-默认值；标准设置FlowMinimumBandwidthAbsolute <Int64>] [-默认值；标准设置FlowMinimumBandwidthWeight <Int64>]
 [-默认值；标准设置QueueVrssEnabled <Boolean>] [-默认值；标准设置QueueVmmqEnabled <Boolean>]
 [-默认值；标准设置QueueVmmqQueuePairs <UInt32>] [-Extensions <VMSwitchExtension[]>] [-Notes <String>] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SwitchName_NetAdapterInterfaceDescription
```
Set-VMSwitch [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String[]> [-NetAdapterInterfaceDescription] <String> [-AllowManagementOS <Boolean>]
 [-默认值；标准设置FlowMinimumBandwidthAbsolute <Int64>] [-默认值；标准设置FlowMinimumBandwidthWeight <Int64>]
 [-默认值；标准设置QueueVrssEnabled <Boolean>] [-默认值；标准设置QueueVmmqEnabled <Boolean>]
 [-默认值；标准设置QueueVmmqQueuePairs <UInt32>] [-Extensions <VMSwitchExtension[]>] [-Notes <String>] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SwitchName_NetAdapterName
```
Set-VMSwitch [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String[]> [-NetAdapterName] <String> [-AllowManagementOS <Boolean>]
 [-默认值；标准设置FlowMinimumBandwidthAbsolute <Int64>] [-默认值；标准设置FlowMinimumBandwidthWeight <Int64>]
 [-默认值；标准设置QueueVrssEnabled <Boolean>] [-默认值；标准设置QueueVmmqEnabled <Boolean>]
 [-默认值；标准设置QueueVmmqQueuePairs <UInt32>] [-Extensions <VMSwitchExtension[]>] [-Notes <String>] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SwitchObject_NetAdapterInterfaceDescription
```
Set-VMSwitch [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMSwitch] <VMSwitch[]> [-NetAdapterInterfaceDescription] <String> [-AllowManagementOS <Boolean>]
 [-默认值；标准设置FlowMinimumBandwidthAbsolute <Int64>] [-默认值；标准设置FlowMinimumBandwidthWeight <Int64>]
 [-默认值；标准设置QueueVrssEnabled <Boolean>] [-默认值；标准设置QueueVmmqEnabled <Boolean>]
 [-默认值；标准设置QueueVmmqQueuePairs <UInt32>] [-Extensions <VMSwitchExtension[]>] [-Notes <String>] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SwitchObject_NetAdapterName
```
Set-VMSwitch [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMSwitch] <VMSwitch[]> [-NetAdapterName] <String> [-AllowManagementOS <Boolean>]
 [-默认值；标准设置FlowMinimumBandwidthAbsolute <Int64>] [-默认值；标准设置FlowMinimumBandwidthWeight <Int64>]
 [-默认值；标准设置QueueVrssEnabled <Boolean>] [-默认值；标准设置QueueVmmqEnabled <Boolean>]
 [-默认值；标准设置QueueVmmqQueuePairs <UInt32>] [-Extensions <VMSwitchExtension[]>] [-Notes <String>] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-VMSwitch` cmdlet 用于配置虚拟交换机。

## 示例

### 示例 1
```
PS C:\> Set-VMSwitch WA -SwitchType Internal
```

这个示例将一个名为“WA”的虚拟交换机转换为内部交换机。

### 示例 2
```
PS C:\> Set-VMSwitch VMNetwork -NetAdapterName "Ethernet 2"
```

这个示例将一个名为“VMNetwork”的虚拟交换机连接到名为“Ethernet 2”的物理以太网适配器上。同时，这也会自动将“VMNetwork”交换机转换为外部交换机。

### 示例 3
```
PS C:\> Set-VMSwitch CA -默认值；标准设置FlowMinimumBandwidthAbsolute 500000000
```

这个示例将名为“CA”的虚拟交换机上所有虚拟机的最低带宽分配设置为500 Mbps，前提是这些虚拟机没有明确配置最低带宽限制。

## 参数

### -AllowManagementOS
该参数用于指定管理操作系统是否可以使用绑定到虚拟交换机的物理网络适配器。将 **AllowManagementOS** 设置为 `$true` 会在父分区中创建管理操作系统的虚拟网络适配器（VMNetworkAdapters），并将其连接到虚拟交换机；将 **AllowManagementOS** 设置为 `$false` 则会移除所有连接到该虚拟交换机的 VMNetworkAdapters。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；标准设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。您可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: SwitchName_SwitchType, SwitchName_NetAdapterInterfaceDescription, SwitchName_NetAdapterName
Aliases:

Required: False
Position: Named
默认值；标准设置 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

```yaml
Type: CimSession[]
Parameter Sets: SwitchObject_SwitchType, SwitchObject_NetAdapterInterfaceDescription, SwitchObject_NetAdapterName
Aliases:

Required: False
Position: Named
默认值；标准设置 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于配置虚拟交换机的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行识别。默认值为本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: PSComputerName

Required: False
Position: Named
默认值；标准设置 value: None
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
默认值；标准设置 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；标准设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -默认值；标准设置FlowMinimumBandwidthAbsolute
指定分配给一个名为“默认流量”（default flow）的特殊类别的最小带宽，单位为比特每秒（bits per second）。任何由连接到该虚拟交换机的虚拟网络适配器发送的、且未分配到最小带宽的数据流都会被归入这一类别。仅当该虚拟交换机处于“绝对最小带宽模式”时（请参阅**New-VMSwitch** cmdlet），才需要设置此参数的值。默认情况下，虚拟交换机会将总带宽的10%分配给这个特殊类别；具体百分比取决于它所绑定的物理网络适配器的性能。例如，如果一个虚拟交换机绑定到了一个1 GbE的网络适配器，那么该特殊类别至少可以使用100 Mbps的带宽。如果输入的带宽值不是8的倍数，系统会将其向下取整为最接近的8的倍数。例如，输入的值为1234567时，实际分配的带宽将为1234560 Mbps。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；标准设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -默认值；标准设置FlowMinimumBandwidthWeight
指定分配给一个名为“默认流量”（default flow）的特殊类别的最小带宽（以相对权重表示）。任何由连接到该虚拟交换机的虚拟网络适配器发送的、且未分配到最小带宽的数据包都会被归入这个类别。只有当该虚拟交换机处于基于权重的最小带宽模式时，才需要设置此参数的值（请参阅**New-VMSwitch** cmdlet）。默认情况下，这个特殊类别的权重为1。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；标准设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -默认值；标准设置QueueVmmqEnabled


```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；标准设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -默认值；标准设置QueueVmmqQueuePairs


```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；标准设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -默认值；标准设置QueueVrssEnabled


```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；标准设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Extensions
指定一个有序的网络扩展列表，用于重新排列虚拟交换机上的绑定关系。

```yaml
Type: VMSwitchExtension[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；标准设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要配置的虚拟交换机的名称。

```yaml
Type: String[]
Parameter Sets: SwitchName_SwitchType, SwitchName_NetAdapterInterfaceDescription, SwitchName_NetAdapterName
Aliases: SwitchName

Required: True
Position: 0
默认值；标准设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NetAdapterInterfaceDescription
指定外部虚拟交换机应绑定的物理网络适配器的接口描述。如果您指定此参数以转换一个虚拟交换机，那么该外部虚拟交换机将被配置为允许管理操作系统共享对物理网络适配器的访问权限。要覆盖此行为，请在命令中包含 `AllowManagementOs $false`。

```yaml
Type: String
Parameter Sets: SwitchName_NetAdapterInterfaceDescription, SwitchObject_NetAdapterInterfaceDescription
Aliases:

Required: True
Position: 1
默认值；标准设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NetAdapterName
指定外部虚拟交换机应绑定的物理网络适配器的名称。如果您指定此参数以转换一个虚拟交换机，则该外部虚拟交换机会被配置为允许管理操作系统共享对物理网络适配器的访问权限。要覆盖此行为，请在命令中包含 `AllowManagementOs $false`。

```yaml
Type: String
Parameter Sets: SwitchName_NetAdapterName, SwitchObject_NetAdapterName
Aliases: InterfaceAlias

Required: True
Position: 1
默认值；标准设置 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Notes
指定要与虚拟交换机关联的注释信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；标准设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定要将一个 **Microsoft.HyperV.PowShell.EthernetSwitch** 对象传递给管道，该对象代表需要配置的虚拟交换机。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；标准设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SwitchType
将虚拟交换机从一种类型转换为另一种类型。允许的值有 **Internal**（内部）和 **Private**（私有）。你可以通过在命令中包含 **NetAdapterInterfaceDescription** 或 **NetAdapterName** 参数，将内部或私有的虚拟交换机转换为外部虚拟交换机。这样做后，外部虚拟交换机会被配置为允许管理操作系统共享对物理网络适配器的访问权限。如果你想覆盖这一行为，可以在命令中添加 `AllowManagementOs $false`。

```yaml
Type: VMSwitchType
Parameter Sets: SwitchName_SwitchType, SwitchObject_SwitchType
Aliases:
Accepted values: Private, Internal, External

Required: False
Position: Named
默认值；标准设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMSwitch
指定要配置的虚拟交换机。

```yaml
Type: VMSwitch[]
Parameter Sets: SwitchObject_SwitchType, SwitchObject_NetAdapterInterfaceDescription, SwitchObject_NetAdapterName
Aliases:

Required: True
Position: 0
默认值；标准设置 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并未执行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值；标准设置 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值；标准设置

### Microsoft.HyperV.PowerShell.EthernetSwitch
如果指定了 **-PassThru**。

## 备注

## 相关链接

