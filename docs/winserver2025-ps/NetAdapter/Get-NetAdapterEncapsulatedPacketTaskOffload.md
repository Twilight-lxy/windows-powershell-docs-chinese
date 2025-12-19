---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterEncapsulatedPacketTaskOffload.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadapterencapsulatedpackettaskoffload?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapterEncapsulatedPacketTaskOffload
---

# Get-NetAdapterEncapsulatedPacketTaskOffload

## 摘要
获取支持封装任务卸载的网络适配器。

## 语法

### 按名称排序（默认值）
```
Get-NetAdapterEncapsulatedPacketTaskOffload [[-Name] <String[]>] [-IncludeHidden] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByInstanceID
```
Get-NetAdapterEncapsulatedPacketTaskOffload -InterfaceDescription <String[]> [-IncludeHidden]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-NetAdapterEncapsulatedPacketTaskOffload` cmdlet 可以获取支持封装任务卸载（encapsulated task offloading）的网络适配器。封装任务卸载功能允许网络适配器对封装数据包的内层头部执行诸如大块数据发送卸载（Large Send Offload, LSO）和虚拟机队列（Virtual Machine Queue, VMQ）等相关操作。

## 示例

### 示例 1：从所有网络适配器中获取封装数据包任务的卸载属性
```
PS C:\> Get-NetAdapterEncapsulatedPacketTaskOffload -Name "*"
```

这个命令会从所有支持该功能的网络适配器中获取所有的封装数据包任务卸载相关属性。

### 示例 2：获取指定网络适配器的封装数据包任务卸载属性
```
PS C:\> Get-NetAdapterEncapsulatedPacketTaskOffload -Name "MyAdapter"
```

此命令用于获取名为“MyAdapter”的网络适配器的封装数据包任务卸载相关属性。

### 示例 3：从已启用该功能的网络适配器中获取封装数据包任务的卸载属性
```
PS C:\> Get-NetAdapterEncapsulatedPacketTaskOffload -Name "*" | Where-Object -FilterScript { $_.Enabled }
```

该命令用于启用封装数据包任务卸载功能的封装数据包任务卸载适配器。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后继续显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
表示该cmdlet在操作过程中会同时包含可见网络适配器和隐藏网络适配器。默认情况下，只包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串会与所有网络适配器（无论是可见的还是隐藏的）进行匹配。

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
指定一个网络适配器接口描述数组。对于物理网络适配器而言，这通常是网络适配器的厂商名称后跟型号和描述，例如“Contoso 12345 千兆网络设备”。

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算出一个最优的运行限制（即并发操作的数量）。这个限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter EncapsulatedPacketTaskOffloadSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Disable-NetAdapterEncapsulatedPacketTaskOffload](./Disable-NetAdapterEncapsulatedPacketTaskOffload.md)

[Enable-NetAdapterEncapsulatedPacketTaskOffload](./Enable-NetAdapterEncapsulatedPacketTaskOffload.md)

[Set-NetAdapterEncapsulatedPacketTaskOffload](./Set-NetAdapterEncapsulatedPacketTaskOffload.md)

