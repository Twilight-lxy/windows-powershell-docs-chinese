---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterEncapsulatedPacketTaskOffload.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/enable-netadapterencapsulatedpackettaskoffload?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-NetAdapterEncapsulatedPacketTaskOffload
---

# 启用 NetAdapterEncapsulatedPacketTask 的卸载功能

## 摘要
支持封装数据包任务的卸载处理（即将数据包处理任务从主机系统转移到专用硬件设备上执行）。

## 语法

### 按名称排序（默认值）
```
Enable-NetAdapterEncapsulatedPacketTaskOffload [-Name] <String[]> [-IncludeHidden] [-NoRestart] [-PassThru]
 [-EncapsulationType <EncapsulationType>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 按实例ID（ByInstanceID）
```
Enable-NetAdapterEncapsulatedPacketTaskOffload -InterfaceDescription <String[]> [-IncludeHidden] [-NoRestart]
 [-PassThru] [-EncapsulationType <EncapsulationType>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Enable-NetAdapterEncapsulatedPacketTaskOffload -InputObject <CimInstance[]> [-NoRestart] [-PassThru]
 [-EncapsulationType <EncapsulationType>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-NetAdapterEncapsulatedPacketTaskOffload` cmdlet 可以在网络适配器上启用封装数据包任务的卸载功能。这样一来，网络适配器就可以根据内部数据包头部或封装数据包本身，执行诸如大容量数据发送卸载（LSO, Large Send Offload）、虚拟机队列（VMQ, Virtual Machine Queue）以及接收端扩展（RSS, Receive Side Scaling）等任务卸载操作。

## 示例

### 示例 1：在指定的网络适配器上启用封装数据包任务的卸载功能
```
PS C:\> Enable-NetAdapterEncapsulatedPacketTaskOffload -Name "MyAdapter"
```

此命令为名为“MyAdapter”的网络适配器启用封装数据包任务的卸载功能，并重启该网络适配器。

### 示例 2：在所有支持该功能的网络适配器上启用封装数据包任务的卸载（offloading）
```
PS C:\> Enable-NetAdapterEncapsulatedPacketTaskOffload -Name "*"
```

该命令可启用所有支持封装数据包任务卸载功能的网络适配器上的封装数据包任务卸载功能。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

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

### -EncapsulationType
指定封装类型。该参数的可接受值包括：  
- NVGRE（Network Virtualization Generic Routing Encapsulation）：网络虚拟化通用路由封装；  
- VXLAN（Virtual eXtensible Local Area Network）：虚拟可扩展局域网。

```yaml
Type: EncapsulationType
Parameter Sets: (All)
Aliases:
Accepted values: NVGRE, VXLAN

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeHidden
表示该cmdlet在操作过程中会同时考虑可见网络适配器和隐藏网络适配器。默认情况下，仅包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将用于匹配所有网络适配器（无论是隐藏的还是可见的）。

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
指定该 cmdlet 的输入数据。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该 cmdlet。

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
指定一个网络适配器接口描述的数组。对于物理网络适配器来说，这通常是网络适配器制造商的名称后跟型号编号和描述，例如“Contoso 12345 千兆网络设备”。

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
表示该 cmdlet 在完成操作后不会重新启动网络适配器。许多高级属性要求在新的设置生效之前先重启网络适配器。

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
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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
该参数用于指定可以同时执行的cmdlet操作的最大数量。如果省略此参数或输入值`0`，Windows PowerShell®将根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。这个限制仅适用于当前正在执行的cmdlet，而不适用于整个会话或计算机本身。

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

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter EncapsulatedPacketTaskOffloadSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter EncapsulatedPacketTaskOffloadSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[ Disable-NetAdapterEncapsulatedPacketTaskOffload](./Disable-NetAdapterEncapsulatedPacketTaskOffload.md)

[Get-NetAdapterEncapsulatedPacketTaskOffload](./Get-NetAdapterEncapsulatedPacketTaskOffload.md)

[Set-NetAdapterEncapsulatedPacketTaskOffload](./Set-NetAdapterEncapsulatedPacketTaskOffload.md)

