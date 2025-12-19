---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterRss.cmdletDefinition.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadapterrss?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapterRss
---

# Get-NetAdapterRss

## 摘要
获取网络适配器的RSS属性信息。

## 语法

### ByName（默认值）
```
Get-NetAdapterRss [[-Name] <String[]>] [-IncludeHidden] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

### ByInstanceID
```
Get-NetAdapterRss -InterfaceDescription <String[]> [-IncludeHidden] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-NetAdapterRss` cmdlet 可用于获取支持 RSS（接收端扩展）功能的网络适配器的相关属性。RSS 是一种可扩展性技术，它通过哈希传入数据包的头部并使用间接表，将网络接收流量分配到多个处理器上。在 Windows Server® 2012 及更高版本系统中，如果没有启用 RSS 功能，所有网络流量都会被发送到第一个处理器上，这可能导致该处理器迅速达到满负荷状态，从而限制了网络的接收吞吐量。可以通过配置各种属性来优化 RSS 的性能。

## 示例

### 示例 1：获取所有支持 RSS 的网络适配器
```
PS C:\> Get-NetAdapterRss -Name "*"
```

这个示例会获取所有支持RSS协议的网络适配器。

### 示例 2：获取指定网络适配器的 RSS 属性
```
PS C:\> Get-NetAdapterRss -Name "MyAdapter"
```

这个示例获取了名为“MyAdapter”的网络适配器的RSS属性信息。

### 示例 3：显示指定网络适配器的所有 RSS 属性
```
PS C:\> Get-NetAdapterRss -Name MyAdapter | Format-List -Property "*"
```

这个示例显示了名为“MyAdapter”的网络适配器的所有RSS属性。

### 示例 4：获取所有支持 RSS 功能且已启用 RSS 的网络适配器
```
PS C:\> Get-NetAdapterRss -Name "*" | Where-Object -FilterScript { $_.Enabled }
```

这个示例会获取所有支持RSS功能的网络适配器，并确保这些适配器的RSS功能已启用。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用该参数来执行需要较长时间才能完成的命令。cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用 `*-Job` 系列 cmdlets。要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
该参数表示此cmdlet在操作过程中会同时考虑可见网络适配器和隐藏网络适配器。默认情况下，仅包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了该参数，则通配符字符串会与所有网络适配器（无论是可见的还是隐藏的）进行匹配。

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
用于指定一组网络适配器接口的描述信息。对于物理网络适配器来说，这些描述通常包括网络适配器的制造商名称、部件编号以及产品描述，例如“Contoso 12345 千兆网络设备”。

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最优限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterRssSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）之后的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Disable-NetAdapterRss](./Disable-NetAdapterRss.md)

[Enable-NetAdapterRss](./Enable-NetAdapterRss.md)

[Set-NetAdapterRss](./Set-NetAdapterRss.md)

