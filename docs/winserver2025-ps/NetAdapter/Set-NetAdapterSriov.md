---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterSriov.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/set-netadaptersriov?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-NetAdapterSriov
---

# 设置 NetAdapter 为 Sriov 模式

## 摘要
设置网络适配器的SR-IOV属性，例如虚拟函数的数量，以及默认和非默认VPort对应的队列对数量。

## 语法

### 按名称排序（默认值）
```
Set-NetAdapterSriov [-Name] <String[]> [-IncludeHidden] [-NumVFs <UInt32>] [-Enabled <Boolean>] [-NoRestart]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ByInstanceID
```
Set-NetAdapterSriov -InterfaceDescription <String[]> [-IncludeHidden] [-NumVFs <UInt32>] [-Enabled <Boolean>]
 [-NoRestart] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-NetAdapterSriov -InputObject <CimInstance[]> [-NumVFs <UInt32>] [-Enabled <Boolean>] [-NoRestart]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-NetAdapterSriov` cmdlet 用于设置网络适配器的单根 I/O 虚拟化（SR-IOV）属性。这些属性包括虚拟函数的数量、虚拟端口（VPorts）的数量，以及默认和非默认虚拟端口的队列对数量。该 cmdlet 还可以用来启用或禁用 SR-IOV 功能。

这些操作所需的网络适配器可以通过适配器名称、接口描述来指定，或者作为输入对象通过管道（pip）传递。

## 示例

### 示例 1：设置指定网络适配器上的虚拟函数数量
```
PS C:\> Set-NetAdapterSriov -Name "Ethernet 2" -NumVFs 31
```

此命令将名为“Ethernet 2”的网络适配器上可用的虚拟函数数量设置为31个。

### 示例 2：为指定的网络适配器设置虚拟函数的数量和 VPort 的数量
```
PS C:\> Set-NetAdapterSriov -Name "Ethernet 2" -NumVFs 31 -NumQueuePairsForDefaultVPort 2 -NumQueuePairsForNonDefaultVPort 2
```

这个命令将虚拟函数的数量设置为 31。因此，会有 31 个虚拟函数和 32 个虚拟机队列（VMQ），另外还有一个队列被物理函数使用。由于默认端口和非默认端口的队列对数量都设置为 2，所以总共使用的队列对数量为 128 个。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行耗时较长的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
该属性用于指示网络适配器上是否启用了SR-IOV（Direct I/O Virtualization）功能。如果设置为 `$True`，则表示SR-IOV已启用；如果设置为 `$False`，则表示SR-IOV已禁用。

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
该参数表示该cmdlet在操作过程中会同时涉及可见网络适配器和隐藏网络适配器。默认情况下，仅包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将匹配所有（无论是隐藏的还是可见的）网络适配器。

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
指定要传递给此cmdlet的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给此cmdlet。

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
指定一个网络适配器接口描述数组。对于物理网络适配器来说，这通常是网络适配器制造商的名称后跟部件编号和描述，例如“Contoso 12345 千兆网络设备”。

可以通过使用*Name*参数来选择网络适配器；也可以通过使用*InputObject*参数来传递该适配器的信息。

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

可以使用这个参数、*InterfaceDescription* 参数来选择网络适配器，或者通过 *InputObject* 参数来传递网络适配器的信息。

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
表示该cmdlet在完成操作后不会重启网络适配器。许多高级属性在新设置生效之前需要先重启网络适配器。

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

### -NumVFs
指定网络适配器为 SR-IOV（Server Side I/O Virtualization）提供的虚拟函数的数量。这是 Windows Server 2012 及更高版本在该网络适配器上可分配的最大虚拟函数数量。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: Vf

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
指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterSriovSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）之后的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterSriovSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）之后的路径表示底层 WMI 对象的命名空间和类名。输出对象将具有更新后的 SR-IOV 设置。

## 备注

## 相关链接

[禁用 NetAdapterSRIOV 功能](./ Disable-NetAdapterSriov.md)

[Enable-NetAdapterSriov](./Enable-NetAdapterSriov.md)

[Get-NetAdapterSriov](./Get-NetAdapterSriov.md)

[Get-NetAdapterSriovVf](./Get-NetAdapterSriovVf.md)

