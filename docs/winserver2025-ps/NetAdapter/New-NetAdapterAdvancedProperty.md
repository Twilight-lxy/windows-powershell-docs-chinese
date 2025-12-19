---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterAdvancedProperty.cmdletDefinition.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/new-netadapteradvancedproperty?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-NetAdapterAdvancedProperty
---

# New-NetAdapterAdvancedProperty

## 摘要
为网络适配器创建一个高级属性。

## 语法

### 名称（默认值）
```
New-NetAdapterAdvancedProperty -RegistryKeyword <String> [-RegistryDataType <RegDataType>]
 -RegistryValue <String[]> [-NoRestart] [-IncludeHidden] [-Name] <String> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InstanceID
```
New-NetAdapterAdvancedProperty -InterfaceDescription <String> -RegistryKeyword <String>
 [-RegistryDataType <RegDataType>] -RegistryValue <String[]> [-NoRestart] [-IncludeHidden]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-NetAdapterAdvancedProperty` cmdlet 用于为网络适配器创建高级属性。其目的是让网络适配器制造商能够使用该 cmdlet 来管理 Windows Server® 2012 及更高版本系统中不直接支持的高级属性。这个 cmdlet 属于网络适配器相关的一系列 cmdlets 中的一个，专门用于在注册表中创建新的键值对；而其他所有 cmdlet 都只是用于读取或修改已存在的注册表条目。需要注意的是，在网络适配器的标识符（无论是 `Name` 参数还是 `InterfaceDescription` 参数）中使用通配符是不被支持的。

## 示例

### 示例 1：在指定的网络适配器上创建一个高级属性
```
PS C:\> New-NetAdapterAdvancedProperty -Name "MyAdapter" -RegistryKeyword "MyKeyword" -RegistryValue "1" -RegistryDataType REG_SZ
```

此命令在网络适配器“MyAdapter”上创建一个高级属性，该属性使用注册表关键字“MyKeyword”，类型为REG_SZ（字符串值），其值为1。

### 示例 2：在指定的网络适配器上创建一个高级属性，该属性不会导致系统重启
```
PS C:\> New-NetAdapterAdvancedProperty -Name "MyAdapter" -RegistryKeyword "MyKeyword" -RegistryValue "1" -RegistryDataType REG_SZ -NoRestart
```

此命令在名为“MyAdapter”的网络适配器上创建一个高级属性，该属性使用注册表关键字“MyKeyword”，类型为REG_SZ（字符串值），其值为1。同时，该命令还指定网络适配器在应用新设置后不会自动重启。不过，许多高级属性确实需要先重启网络适配器才能使新设置生效。

### 示例 3：在指定的网络适配器上创建一个高级属性
```
PS C:\> $NetworkAdapter3 = Get-NetAdapter -Name "Ethernet 3"
PS C:\> New-NetAdapterAdvancedProperty -InputObject $NetworkAdapter3 -RegistryKeyword "MyKeyword" -RegistryValue "1" -RegistryDataType REG_SZ

This command is  a version of the cmdlet that creates an advanced property on the network adapter named Ethernet 3 using wildcard characters and the pipeline. Use of wildcard characters is not allowed for the network adapter identifier as part of this cmdlet, but can be used via the pipeline.
PS C:\> Get-NetAdapter -Name "Ethernet 3" | New-NetAdapterAdvancedProperty -RegistryKeyword "MyKeyword" -RegistryValue "1" -RegistryDataType REG_SZ
```

第一个命令获取名为“Ethernet 3”的网络适配器，并将结果存储在名为$NetworkAdapter3的变量中。

第二个命令为网络适配器创建了一个高级属性，该属性存储在变量$NetworkAdapter3中，并以“MyKeyword”作为关键字，在注册表中对应的值为1。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行那些需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
在运行cmdlet之前，会提示您进行确认。

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
表示该 cmdlet 在操作中会同时包含可见的网络适配器和隐藏的网络适配器。默认情况下，仅包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将匹配所有隐藏和可见的网络适配器。

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
指定网络适配器接口的描述。对于物理网络适配器来说，这通常是网络适配器的供应商名称后跟型号和描述，例如“Contoso 12345 千兆网络设备”。

```yaml
Type: String
Parameter Sets: InstanceID
Aliases: ifDesc, InstanceID

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定网络适配器的名称。

```yaml
Type: String
Parameter Sets: Name
Aliases: ifAlias, InterfaceAlias

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NoRestart
这表示该cmdlet在完成操作后不会重启网络适配器。许多高级属性要求在新设置生效之前必须先重启网络适配器。

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

### -RegistryDataType
指定要设置在注册表中的值数据的类型。此参数的可接受值为：

- None
- REG_SZ
- REG_DWORD
- REG_QWORD
- REG_MULTI_SZ

```yaml
Type: RegDataType
Parameter Sets: (All)
Aliases:
Accepted values: None, REG_SZ, REG_DWORD, REG_MULTI_SZ, REG_QWORD

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RegistryKeyword
指定此cmdlet创建的注册表键字的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RegistryValue
以数组的形式指定高级属性的值。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于会话或整个计算机。

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
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterAdvancedPropertySettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-NetAdapterAdvancedProperty](./Get-NetAdapterAdvancedProperty.md)

[Remove-NetAdapterAdvancedProperty](./Remove-NetAdapterAdvancedProperty.md)

[Reset-NetAdapterAdvancedProperty](./Reset-NetAdapterAdvancedProperty.md)

[Set-NetAdapterAdvancedProperty](./Set-NetAdapterAdvancedProperty.md)

