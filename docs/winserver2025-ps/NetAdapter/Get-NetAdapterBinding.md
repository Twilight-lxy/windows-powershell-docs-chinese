---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterBinding.cmdletDefinition.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadapterbinding?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapterBinding
---

# 获取网络适配器绑定信息

## 摘要
获取网络适配器的绑定信息列表。

## 语法

### 按名称查找（默认方式）
```
Get-NetAdapterBinding [[-Name] <String[]>] [-ComponentID <String[]>] [-DisplayName <String[]>] [-IncludeHidden]
 [-AllBindings] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 按实例ID（ByInstanceID）
```
Get-NetAdapterBinding -InterfaceDescription <String[]> [-ComponentID <String[]>] [-DisplayName <String[]>]
 [-IncludeHidden] [-AllBindings] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-NetAdapterBinding` cmdlet 可以获取网络适配器的绑定信息列表。默认情况下，仅会返回在 Windows 用户界面中“网络适配器”属性下的“网络”选项卡中显示的可见绑定信息。如果要获取网络适配器的所有属性，请使用 `AllProperties` 参数。

## 示例

### 示例 1：获取指定网络适配器的绑定信息
```
PS C:\> Get-NetAdapterBinding -Name "MyAdapter"
```

这个命令用于获取名为“MyAdapter”的网络适配器的绑定信息。

### 示例 2：以未格式化的列表形式获取指定网络适配器的所有绑定信息
```
PS C:\> Get-NetAdapterBinding -Name "MyAdapter" -AllBindings
```

这个命令会获取名为“MyAdapter”的网络适配器的所有绑定信息，并以未格式化的列表形式返回结果。

### 示例 3：使用显示名称获取指定网络适配器上的 TCP/IPv4 状态
```
PS C:\> Get-NetAdapterBinding -Name "MyAdapter" -DisplayName "Internet Protocol Version 4 (TCP/IPv4)"
```

这个命令用于获取名为“MyAdapter”的网络适配器上TCP/IPv4协议的状态，该适配器是通过显示名称来识别的。

### 示例 4：获取指定网络适配器上的 TCP/IPv4 传输状态
```
PS C:\> Get-NetAdapterBinding -Name "MyAdapter"  -ComponentID ms_tcpip
```

该命令使用组件ID来获取MyAdapter上TCP/IPv4传输层的状态信息。

### 示例 5：使用搜索字符串获取所有可见网络适配器上的 TCP/IPv4 和 TCP/IPv6 状态
```
PS C:\> Get-NetAdapterBinding -Name "*" -DisplayName "Internet*"
```

该命令使用通配符来获取所有可见网络适配器上的TCP/IPv4和TCP/IPv6协议的状态。

## 参数

### -AllBindings
表示该 cmdlet 会获取网络适配器的所有绑定信息。

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

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行耗时较长的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

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
以以下形式指定传输层或过滤器的基础名称数组：`ms_xxxx`（例如 `ms_tcpip`）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisplayName
用于指定在 Windows Server® 2012 及更高版本中网络适配器属性的“网络”选项卡下显示的传输方式或过滤器名称数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeHidden
这表示该cmdlet在操作中会包含所有可见和隐藏的网络适配器。默认情况下，只包括可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，那么该通配符字符串将会与所有隐藏和可见的网络适配器进行匹配。

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
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterBindingSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Disable-NetAdapterBinding](./Disable-NetAdapterBinding.md)

[Enable-NetAdapterBinding](./Enable-NetAdapterBinding.md)

[Set-NetAdapterBinding](./Set-NetAdapterBinding.md)

