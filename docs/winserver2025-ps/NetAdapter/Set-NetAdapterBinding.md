---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterBinding.cmdletDefinition.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/set-netadapterbinding?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-NetAdapterBinding
---

# 设置网络适配器绑定

## 摘要
设置网络适配器上某个传输层组件或过滤组件的绑定状态。

## 语法

### 按名称查找（默认方式）
```
Set-NetAdapterBinding [-Name] <String[]> [-ComponentID <String[]>] [-DisplayName <String[]>] [-IncludeHidden]
 [-AllBindings] [-Enabled <Boolean>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ByInstanceID
```
Set-NetAdapterBinding -InterfaceDescription <String[]> [-ComponentID <String[]>] [-DisplayName <String[]>]
 [-IncludeHidden] [-AllBindings] [-Enabled <Boolean>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-NetAdapterBinding -InputObject <CimInstance[]> [-Enabled <Boolean>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-NetAdapterBinding` cmdlet 用于设置网络适配器上某个传输机制（transport）或过滤器（filter）的绑定状态。默认情况下，只有可见的绑定才会被修改，除非指定了 `AllBindings` 参数。如果只是需要启用或禁用某些绑定，可以使用 `Enable-NetAdapterBinding` 或 `Disable-NetAdapterBinding` cmdlet。在禁用或启用某个网络适配器的绑定时，该 cmdlet 可以自动地同时启用或禁用其他与该适配器相关的绑定设置。

## 示例

#### 示例 1：在指定的网络适配器上启用 TCP/IPv4 协议
```
PS C:\> Set-NetAdapterBinding -Name "MyAdapter" -DisplayName "Internet Protocol Version 4 (TCP/IPv4)" -Enabled $True
```

此命令会启用名为“MyAdapter”的网络适配器上的TCP/IPv4功能。

### 示例 2：禁用指定网络适配器上的 TCP/IPv4 协议
```
PS C:\> Set-NetAdapterBinding -Name "MyAdapter" -DisplayName "Internet Protocol Version 4 (TCP/IPv4)" -Enabled $False
```

此命令会禁用名为“MyAdapter”的网络适配器上的TCP/IPv4功能。

### 示例 3：使用组件 ID 在指定的网络适配器上启用 TCP/IPv4
```
PS C:\> Set-NetAdapterBinding -Name "MyAdapter" -ComponentID ms_tcpip -Enabled $True
```

此命令使用组件ID，在名为“MyAdapter”的网络适配器上启用TCP/IPv4协议。

## 参数

### -AllBindings
表示该cmdlet设置了默认情况下不可见的过滤器或传输方式。

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

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称，或者提供一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -ComponentID
请以数组的形式指定传输层或过滤层的底层名称，格式如下：`ms_xxxx`（例如 `ms.tcpip`）。

```yaml
Type: String[]
Parameter Sets: ByName, ByInstanceID
Aliases:

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

### -DisplayName
用于指定一组传输方式或过滤器的名称，这些名称会显示在 Windows Server® 2012 及更高版本中网络适配器属性下的“Networking”（网络）选项卡中。

```yaml
Type: String[]
Parameter Sets: ByName, ByInstanceID
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Enabled
表示传输功能或过滤功能是否处于启用状态。该参数的可接受值为：$True 或 $False。

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
该参数表示该cmdlet在操作过程中会同时考虑可见网络适配器和隐藏网络适配器。默认情况下，仅包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则通配符字符串将会与所有网络适配器（无论是可见的还是隐藏的）进行匹配。

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
指定一个网络适配器接口描述数组。对于物理网络适配器而言，这通常是指网络适配器的制造商名称后跟部件编号和描述，例如 `Contoso 12345 Gigabit Network Device`。

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
该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不影响整个会话或计算机本身。

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterBindingSettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter BindingSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[ Disable-NetAdapterBinding](./Disable-NetAdapterBinding.md)

[Enable-NetAdapterBinding](./Enable-NetAdapterBinding.md)

[Get-NetAdapterBinding](./Get-NetAdapterBinding.md)

