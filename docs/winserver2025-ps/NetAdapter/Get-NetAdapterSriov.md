---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterSriov.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadaptersriov?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapterSriov
---

# Get-NetAdapterSriov

## 摘要
获取网络适配器的 SR-IOV（直接内存访问）属性。

## 语法

### 按名称排序（默认值）
```
Get-NetAdapterSriov [[-Name] <String[]>] [-IncludeHidden] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

### ByInstanceID
```
Get-NetAdapterSriov -InterfaceDescription <String[]> [-IncludeHidden] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-NetAdapterSriov` cmdlet 用于获取支持 Single-Root I/O Virtualization（SR-IOV）功能的网络适配器的相关属性。SR-IOV 允许网络流量直接绕过 Hyper-V 虚拟化堆栈中的软件交换层，从而减少软件仿真层的 I/O 开销，并实现接近于非虚拟化环境下的网络性能。运行此 cmdlet 可以查看硬件是如何配置以支持 SR-IOV 的。该 cmdlet 会显示与 SR-IOV 相关的网络适配器属性，例如端口数量和虚拟功能（VFs）等。`SriovSupport` 属性可以提示 SR-IOV 功能可能无法正常工作的原因。

SriovSupport的可能取值包括以下几种：

- Unknown: Ensure that the computer has hardware support for SR-IOV and that I/O virtualization is enabled in the BIOS.
Also ensure that the computer is running Windows Server® 2012 and later.
- Supported: SR-IOV is supported and should be functioning properly.
- MissingAcs: SR-IOV cannot be used on this network adapter as the PCI Express hardware does not support Access Control Services (ACS).
This device may work in an alternate PCI Express slot.
Contact your hardware vendor for further information.
- MissingPfDriver: SR-IOV cannot be used on this network adapter as the device or device driver does not support SR-IOV.
If the network adapter supports SR-IOV, contact the hardware vendor for an updated driver.
- NoBusResources: SR-IOV cannot be used on this network adapter as there are not enough PCI Express bus numbers available.
- NoIoMmuSupport: SR-IOV cannot be used on this computer because of one or more of the following reasons.
- - The processor does not support second level address translation (SLAT).
For processors manufactured by Intel Corporation™ (Intel™), this feature might be referred to as Extended Page Tables (EPT).
For processors manufactured by Advanced Micro Devices™ (AMD™), this feature might be referred to as Rapid Virtualization Indexing (RVI) or Nested Page Tables (NPT).
- - The chipset on the computer does not do Interrupt and/or DMA remapping, without which SR-IOV cannot be supported.
- - This computer has been configured to disable the use of I/O remapping hardware.
- NoVfBarSpace: SR-IOV cannot be used on this network adapter as there are not enough PCI Express BAR resources available.
This may be due to incorrect or partial configuration in the computer BIOS for Interrupt and DMA remapping.
These settings may be referred to as SR-IOV or input/output memory management unit (IOMMU) support.
If the computer BIOS is correctly configured, this device may work in an alternate PCI Express slot.
Contact the original equipment manufacturer of the computer for further information.
- NoOscSupport: To use SR-IOV on this computer, the computer BIOS must be updated to allow Windows Server 2012 and later to control PCI Express using `_OSC HandOff`.
Contact the original equipment manufacturer of the computer for an update.

## 示例

### 示例 1：显示所有支持 SR-IOV 的网络适配器的 SR-IOV 属性
```
PS C:\> Get-NetAdapterSriov -Name "*"
```

此命令会显示所有支持SR-IOV功能的网络适配器的SR-IOV属性。

### 示例 2：显示指定网络适配器的 SR-IOV 属性
```
PS C:\> Get-NetAdapterSriov -Name "Ethernet 2"
```

此命令会显示名为“Ethernet 2”的网络适配器的SR-IOV属性。

### 示例 3：显示具有指定接口描述的网络适配器的 SR-IOV 属性
```
PS C:\> Get-NetAdapterSriov -InterfaceDescription "Contoso 12345 Gigabit Network Device"
```

此命令会显示名为“Contoso 12345 Gigabit Network Device”的网络适配器的SR-IOV属性。

### 示例 4：获取所有启用了 SR-IOV 的网络适配器的所有 SR-IOV 属性
```
PS C:\> Get-NetAdapterSriov -Name "*" | Where-Object -FilterScript { $_.Enabled -Eq $true }
```

该命令用于获取已启用SR-IOV功能的网络适配器的SR-IOV属性。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job` cmdlets系列命令；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
这表示该 cmdlet 在操作过程中会同时考虑所有可见和隐藏的网络适配器。如果使用通配符来标识网络适配器，那么该通配符将会与所有可见和隐藏的适配器都进行匹配。

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
指定一个网络适配器名称数组。此cmdlet从其中获取SR-IOV属性的网络适配器的名称。

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
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值（即并发操作的最大数量）。此限制仅适用于当前运行的cmdlet，而不适用于整个会话或计算机本身。

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

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterSriovSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[禁用NetAdapterSriov功能](./Disable-NetAdapterSriov.md)

[Enable-NetAdapterSriov](./Enable-NetAdapterSriov.md)

[Get-NetAdapterSriovVf](./Get-NetAdapterSriovVf.md)

[Set-NetAdapterSriov](./Set-NetAdapterSriov.md)

