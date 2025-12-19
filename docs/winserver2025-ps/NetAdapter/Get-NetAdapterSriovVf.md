---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterSriovVf.cmdletDefinition.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadaptersriovvf?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapterSriovVf
---

# Get-NetAdapterSriovVf

## 摘要
显示网络适配器的 SR-IOV（直接I/O虚拟化）虚拟功能设置。

## 语法

### 按名称排序（默认值）
```
Get-NetAdapterSriovVf [[-Name] <String[]>] [-SwitchID <UInt32[]>] [-FunctionID <UInt16[]>] [-IncludeHidden]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 按实例ID（ByInstanceID）
```
Get-NetAdapterSriovVf -InterfaceDescription <String[]> [-SwitchID <UInt32[]>] [-FunctionID <UInt16[]>]
 [-IncludeHidden] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-NetAdapterSriovVf` cmdlet 可以显示网络适配器的单根 I/O 虚拟化（SR-IOV）虚拟功能设置。默认情况下，会显示一个包含以下信息的表格：虚拟功能标识符（ID）、虚拟功能名称、网络适配器 ID 以及当前的 MAC 地址。如果指定了某个特定的虚拟功能，系统会提供更多关于该功能的详细信息。其他显示的字段还包括永久 MAC 地址、请求者 ID 以及虚拟端口（VPort）的相关信息。

要使用的网络适配器可以通过以下方式指定：网络适配器的名称、网络适配器的接口描述，或者绑定到 SR-IOV 网络适配器的虚拟交换机的 ID。

## 示例

### 示例 1：获取指定网络适配器的虚拟函数、虚拟机以及 MAC 地址的列表
```
PS C:\> Get-NetAdapterSriovVf -Name "Ethernet 1"
```

这个命令会获取一个虚拟函数列表，其中包含虚拟机的名称以及名为“Ethernet 1”的网络适配器的MAC地址。

### 示例 2：获取绑定到虚拟交换机的网络适配器的虚拟函数、虚拟机以及 MAC 地址的列表
```
PS C:\> Get-NetAdapterSriovVf -SwitchId 2
```

这个命令会获取一个列表，其中包含虚拟函数的名称、以及绑定到虚拟交换机2的网络适配器的虚拟机名称和MAC地址。

## 参数

### -AsJob
将该 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets。要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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

### -FunctionID
指定所指示网络适配器上的虚拟函数ID编号，以获取有关该虚拟函数的更详细信息。

```yaml
Type: UInt16[]
Parameter Sets: (All)
Aliases: VfID, Id

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeHidden
该参数表示此 cmdlet 在操作过程中会同时包含可见网络适配器和隐藏网络适配器。默认情况下，仅包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将用于匹配所有（无论是隐藏的还是可见的）网络适配器。

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
指定一个网络适配器接口描述的数组。对于物理网络适配器来说，这通常是网络适配器的供应商名称后跟型号和描述，例如 `Contoso 12345 Gigabit Network Device`。

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

### -SwitchID
指定虚拟交换机ID，该ID用于标识一个或多个虚拟函数所对应的网络适配器（以数组的形式提供）。

```yaml
Type: UInt32[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值（即并发操作的最大数量）。这个限制仅适用于当前执行的 cmdlet，而不影响整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterSriovVfSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[禁用网卡SRIOV功能](./Disable-NetAdapterSriov.md)

[Enable-NetAdapterSriov](./Enable-NetAdapterSriov.md)

[Get-NetAdapterSriov](./Get-NetAdapterSriov.md)

[Set-NetAdapterSriov](./Set-NetAdapterSriov.md)

