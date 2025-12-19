---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterLso.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadapterlso?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapterLso
---

# Get-NetAdapterLso

## 摘要
获取网络适配器的LSO（链接状态对象）属性。

## 语法

### 按名称排序（默认值）
```
Get-NetAdapterLso [[-Name] <String[]>] [-IncludeHidden] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

### ByInstanceID
```
Get-NetAdapterLso -InterfaceDescription <String[]> [-IncludeHidden] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-NetAdapterLso` cmdlet 可用于获取网络适配器上的“大块数据发送卸载”（Large Send Offload，简称 LSO）设置的状态。LSO 是一种技术，它允许网络适配器负责将数据分段为网络帧的工作，而不是由 TCP/IP 堆栈来执行这一任务。通过使用 LSO，TCP/IP 将非常大的数据包发送给网络适配器驱动程序及相应的硬件；网络适配器会将这些数据拆分成较小的网络帧格式。这样一来，不仅提高了高端数据传输操作的效率，还减少了计算机处理器的负担（因为相关处理工作是在网络适配器层面完成的）。

## 示例

### 示例 1：获取指定网络适配器的 LSO 属性
```
PS C:\> Get-NetAdapterLso -Name "MyAdapter"
```

此命令用于获取名为“MyAdapter”的网络适配器的LSO属性。

### 示例 2：显示指定网络适配器的所有 LSO 属性
```
PS C:\> Get-NetAdapterLso -Name "MyAdapter" | Format-List -Property "*"
```

此命令会显示名为“MyAdapter”的网络适配器的所有LSO属性。

### 示例 3：获取所有启用了 LSO（Large Send Offload）功能的网络适配器
```
PS C:\> Get-NetAdapterLso -Name "*" | Where-Object -FilterScript { $_.Enabled }
```

这条命令会获取所有启用了LSO（Large Send Offload）功能的网络适配器。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列cmdlet；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
该参数表示此cmdlet在操作过程中会同时考虑可见的网络适配器和隐藏的网络适配器。默认情况下，仅包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将用于匹配所有类型的网络适配器（无论是隐藏的还是可见的）。

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
指定一个网络适配器接口描述数组。对于物理网络适配器来说，这通常是网络适配器的供应商名称后跟型号和描述，例如 `Contoso 12345 千兆网络设备`。

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值（即并发操作的数量）。此限制仅适用于当前正在执行的 cmdlet，而不影响整个会话或整个计算机。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter LsoSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Disable-NetAdapterLso](./Disable-NetAdapterLso.md)

[Enable-NetAdapterLso](./Enable-NetAdapterLso.md)

[Set-NetAdapterLso](./Set-NetAdapterLso.md)

