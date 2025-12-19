---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapter.cmdletDefinition.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/set-netadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-NetAdapter
---

# Set-NetAdapter

## 摘要
设置基本的网络适配器属性。

## 语法

### 按名称排序（默认值）
```
Set-NetAdapter [-Name] <String[]> [-IncludeHidden] [-VlanID <UInt16>] [-MacAddress <String>] [-NoRestart]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 按实例ID（ByInstanceID）
```
Set-NetAdapter -InterfaceDescription <String[]> [-IncludeHidden] [-VlanID <UInt16>] [-MacAddress <String>]
 [-NoRestart] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-NetAdapter -InputObject <CimInstance[]> [-VlanID <UInt16>] [-MacAddress <String>] [-NoRestart]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-NetAdapter` cmdlet 用于设置网络适配器的基本属性，如虚拟局域网（VLAN）标识符（ID）和 MAC 地址。这些更改可能会影响网络功能的正常运行。其他网络适配器的属性可以通过使用 `Set-NetAdapterRss`、`Set-NetAdapterLso` 或 `Set-NetAdapterAdvancedProperty` 等 cmdlet 来设置。

## 示例

### 示例 1：将指定的网络适配器设置为另一个 VLAN ID
```
PS C:\> Set-NetAdapter -Name "Ethernet 1" -VlanID 10
```

此命令将名为“Ethernet 1”的网络适配器设置为VLAN ID为10。

### 示例 2：设置指定网络适配器的 MAC 地址
```
PS C:\> Set-NetAdapter -Name "Ethernet 1" -MacAddress "00-10-18-57-1B-0D"
```

这个命令用于设置名为“Ethernet 1”的网络适配器的MAC地址。

#### 示例 3：为网络适配器设置 MAC 地址，使该地址与符合特定模式的接口描述相匹配
```
PS C:\> Set-NetAdapter -InterfaceDescription "B*2" -MacAddress "00-10-18-57-1B-0D"
```

该命令用于设置网络适配器的MAC地址，其接口描述符合“B*2”这个模式。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet将在本地计算机的当前会话中执行。

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
在运行 cmdlet 之前，会提示您确认是否要继续执行该操作。

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
表示该cmdlet在操作过程中会同时包含可见的网络适配器和隐藏的网络适配器。默认情况下，只包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，那么该通配符字符串将用于匹配所有类型的网络适配器（无论是可见的还是隐藏的）。

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
指定一个网络适配器接口描述数组。对于物理网络适配器来说，这通常是网络适配器的供应商名称后跟型号和描述，例如 `Contoso 12345 Gigabit Network Device`。

```yaml
Type: String[]
Parameter Sets: ByInstanceID
Aliases: ifDesc

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MacAddress
指定网络适配器的当前MAC地址。输入内容中可以包含破折号（-），但这并非必需；并非所有网络适配器都支持设置MAC地址。传递的MAC地址也会被保存在“网络地址”属性中，且该地址会去除其中的破折号。

```yaml
Type: String
Parameter Sets: (All)
Aliases: LinkLayerAddress

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoRestart
表示该 cmdlet 在完成操作后不会重新启动网络适配器。许多高级属性在新设置生效之前需要先重启网络适配器。

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
指定可以同时运行的最大并发操作数量。如果省略此参数或输入 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -VlanID
指定网络适配器的 VLAN ID。并非所有网络适配器都支持设置 VLAN ID。

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

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[禁用网卡](./Disable-NetAdapter.md)

[Enable-NetAdapter](./Enable-NetAdapter.md)

[Get-NetAdapter](./Get-NetAdapter.md)

[ Rename-NetAdapter](./Rename-NetAdapter.md)

[重启网络适配器](./Restart-NetAdapter.md)

[Set-NetAdapterAdvancedProperty](./Set-NetAdapterAdvancedProperty.md)

[Set-NetAdapterLso](./Set-NetAdapterLso.md)

[Set-NetAdapterRss](./Set-NetAdapterRss.md)

