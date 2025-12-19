---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterEncapsulatedPacketTaskOffload.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/set-netadapterencapsulatedpackettaskoffload?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-NetAdapterEncapsulatedPacketTaskOffload
---

# 将 Set-NetAdapterEncapsulatedPacketTaskOffload 的状态设置为关闭

## 摘要
设置网络适配器的“封装数据包任务卸载”属性。

## 语法

### 按名称排序（默认值）
```
Set-NetAdapterEncapsulatedPacketTaskOffload [-Name] <String[]> [-IncludeHidden]
 [-NvgreEncapsulatedPacketTaskOffloadEnabled <Boolean>] [-VxlanEncapsulatedPacketTaskOffloadEnabled <Boolean>]
 [-VxlanUDPPortNumber <UInt16>] [-NoRestart] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ByInstanceID
```
Set-NetAdapterEncapsulatedPacketTaskOffload -InterfaceDescription <String[]> [-IncludeHidden]
 [-NvgreEncapsulatedPacketTaskOffloadEnabled <Boolean>] [-VxlanEncapsulatedPacketTaskOffloadEnabled <Boolean>]
 [-VxlanUDPPortNumber <UInt16>] [-NoRestart] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-NetAdapterEncapsulatedPacketTaskOffload -InputObject <CimInstance[]>
 [-NvgreEncapsulatedPacketTaskOffloadEnabled <Boolean>] [-VxlanEncapsulatedPacketTaskOffloadEnabled <Boolean>]
 [-VxlanUDPPortNumber <UInt16>] [-NoRestart] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-NetAdapterEncapsulatedPacketTaskOffload` cmdlet 用于设置网络适配器的封装数据包任务卸载（encapsulation packet task offloading）属性。该功能允许网络适配器对封装数据包的内部头部执行卸载操作，例如大型数据包发送卸载（Large Send Offload, LSO）和虚拟机队列（Virtual Machine Queue, VMQ）处理。`Enable-NetAdapterEncapsulatedPacketTaskOffload` 和 `Disable-NetAdapterEncapsulatedPacketTaskOffload` cmdlets 也可用于管理封装数据包任务的卸载功能。

## 示例

### 示例 1：在指定的网络适配器上启用封装数据包任务的卸载功能
```
PS C:\> Set-NetAdapterEncapsulatedPacketTaskOffload -Name "MyAdapter" -VxlanEncapsulatedPacketTaskOffloadEnabled $True
```

此命令可以在名为“MyAdapter”的网络适配器上启用VXLAN封装数据包任务的卸载功能，并重新启动该网络适配器。`Enable-NetAdapterEncapsulatedPacketTaskOffload` cmdlet是执行此操作的首选命令。

### 示例 2：禁用指定网络适配器上的封装数据包任务卸载功能
```
PS C:\> Set-NetAdapterEncapsulatedPacketTaskOffload -Name "MyAdapter" -VxlanEncapsulatedPacketTaskOffloadEnabled $False
```

此命令将名为“MyAdapter”的网络适配器上的VXLAN封装数据包任务卸载功能禁用，并重新启动该网络适配器。**Disable-NetAdapterEncapsulatedPacketTaskOffload** cmdlet是执行此操作的推荐工具。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成的过程中，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业的结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
在运行 cmdlet 之前会提示您进行确认。

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
该参数表示此cmdlet在操作过程中会同时包含可见的网络适配器和隐藏的网络适配器。默认情况下，仅包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将用于匹配所有类型（包括隐藏的和可见的）的网络适配器。

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
指定要输入到此cmdlet的数据。您可以使用该参数，也可以将数据通过管道（pipe）传递给此cmdlet。

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
指定一个网络适配器接口描述数组。对于物理网络适配器而言，通常表示为网络适配器的供应商名称后跟部件编号和描述，例如“Contoso 12345 千兆网络设备”。

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
表示该cmdlet在完成操作后不会重启网络适配器。许多高级属性在新设置生效之前需要重启网络适配器。

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

### -NvgreEncapsulatedPacketTaskOffloadEnabled
该参数用于指定网络适配器中支持Network Virtualization Generic Routing Encapsulation（NVGRE）封装数据包卸载功能的启用状态。有效取值为：$true或$false。

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

### -PassThru
返回一个表示您当前正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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
该参数用于指定可以同时运行的命令（cmdlet）的最大数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该命令的最佳限制值。这个限制仅适用于当前执行的命令，而不涉及整个会话或计算机本身。

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

### -VxlanEncapsulatedPacketTaskOffloadEnabled
指定网络适配器中支持虚拟可扩展局域网（VXLAN）封装数据包卸载功能的启用状态。该参数的有效值为：$true 或 $false。

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

### -VxlanUDPPortNumber
指定用于 VXLAN UDP 目标端口的端口号。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。不过实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter EncapsulatedPacketTaskOffloadSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter EncapsulatedPacketTaskOffloadSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[disable-NetAdapterEncapsulatedPacketTaskOffload](./Disable-NetAdapterEncapsulatedPacketTaskOffload.md)

[Enable-NetAdapterEncapsulatedPacketTaskOffload](./Enable-NetAdapterEncapsulatedPacketTaskOffload.md)

[Get-NetAdapterEncapsulatedPacketTaskOffload](./Get-NetAdapterEncapsulatedPacketTaskOffload.md)

