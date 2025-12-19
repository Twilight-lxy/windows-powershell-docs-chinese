---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterChecksumOffload.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadapterchecksumoffload?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapterChecksumOffload
---

# Get-NetAdapterChecksumOffload

## 摘要
从支持这些校验和卸载功能的网络适配器中获取各种校验和卸载设置。

## 语法

### 按名称排序（默认值）
```
Get-NetAdapterChecksumOffload [[-Name] <String[]>] [-IncludeHidden] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 按实例ID（ByInstanceID）
```
Get-NetAdapterChecksumOffload -InterfaceDescription <String[]> [-IncludeHidden] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
**Get-NetAdapterChecksumOffload** cmdlet 可以获取各种校验和卸载（checksum offloading）设置。物理网络适配器支持多种校验和卸载功能，这些功能允许在校验和计算过程中使用网络适配器本身而不是主板上的处理器来执行计算。这种方式可以降低处理器的负载，并提高网络传输效率。该 cmdlet 支持获取与 IPv4、TCPv4、TCPv6、UDPv4 和 UDPv6 相关的校验和卸载设置。

## 示例

### 示例 1：获取指定网络适配器的校验和卸载属性
```
PS C:\> Get-NetAdapterChecksumOffload -Name "MyAdapter"
```

这个命令用于获取名为“MyAdapter”的网络适配器的校验和卸载属性（checksum offload properties）的状态信息。

### 示例 2：获取指定网络适配器的校验和卸载属性并显示它们
```
PS C:\> $NetworkAdapterC01 = Get-NetAdapterChecksumOffload -Name "MyAdapter"
PS C:\> $NetworkAdapterC01.ChecksumOffloadHardwareCapabilities
```

第一个命令从名为“MyAdapter”的网络适配器中获取校验和卸载属性的状态，并将结果存储在变量$NetworkAdapterC01中。

第二个命令显示了存储在 $NetworkAdapterC01 中的网络适配器的校验和卸载硬件功能。

## 参数

### -AsJob
该cmdlet以后台作业的形式运行。使用此参数可以执行耗时较长的命令。cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成过程中，您可以继续在当前会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

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
表示该cmdlet在操作过程中会包含所有可见和隐藏的网络适配器。默认情况下，仅包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，那么该通配符字符串将同时应用于所有隐藏和可见的网络适配器。

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
指定一个网络适配器接口描述数组。对于物理网络适配器而言，通常表示为网络适配器的厂商名称后跟部件编号和描述，例如 `Contoso 12345 Gigabit Network Device`。

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
指定可以同时运行的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，不适用于整个会话或计算机本身。

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

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter ChecksumOffloadSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[ Disable-NetAdapterChecksumOffload](./Disable-NetAdapterChecksumOffload.md)

[Enable-NetAdapterChecksumOffload](./Enable-NetAdapterChecksumOffload.md)

[Set-NetAdapterChecksumOffload](./Set-NetAdapterChecksumOffload.md)

