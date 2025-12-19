---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterIPsecOffload.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadapteripsecoffload?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapterIPsecOffload
---

# Get-NetAdapterIPsecOffload

## 摘要
获取网络适配器的 IPsec 负载卸载属性。

## 语法

### 按名称排序（默认值）
```
Get-NetAdapterIPsecOffload [[-Name] <String[]>] [-IncludeHidden] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByInstanceID
```
Get-NetAdapterIPsecOffload -InterfaceDescription <String[]> [-IncludeHidden] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-NetAdapterIPsecOffload` cmdlet 可用于获取支持 IPsec 转发（IPsec Offload）功能的网络适配器的相关属性。当 IPsec 转发功能被启用后，该网络适配器会负责执行每个数据包的加密操作，从而降低处理器的使用负担。

## 示例

### 示例 1：获取指定网络适配器的 IPsec 分载属性
```
PS C:\> Get-NetAdapterIPsecOffload -Name "MyAdapter"
```

这个命令用于获取名为“MyAdapter”的网络适配器的IPsec卸载属性（即与IPsec协议相关的配置信息）。

### 示例 2：显示指定网络适配器的所有 IPsec 转发（offload）属性
```
PS C:\> Get-NetAdapterIPsecOffload -Name "MyAdapter" | Format-List -Property "*"
```

此命令会显示名为“MyAdapter”的网络适配器的所有IPsec卸载（offload）相关属性。

### 示例 3：获取所有启用了 IPsec 转发功能的网络适配器
```
PS C:\> Get-NetAdapterIPsecOffload -Name "*" | Where-Object -FilterScript { $_.Enabled }
```

这个命令会获取所有支持IPsec卸载功能且已启用IPsec卸载的网络适配器。

## 参数

### -AsJob
该cmdlet以后台作业的形式运行。使用此参数可执行需要较长时间才能完成的命令。cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
该参数表示此 cmdlet 在操作过程中会同时考虑可见网络适配器和隐藏网络适配器。默认情况下，仅包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了该参数，则该通配符字符串将用于匹配所有网络适配器（无论是可见的还是隐藏的）。

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
指定一个网络适配器接口描述数组。对于物理网络适配器来说，这通常是指网络适配器的供应商名称后跟型号编号和描述，例如“Contoso 12345 千兆网络设备”。

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
该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter IPsecOffloadV2SettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows Management Instrumentation（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[禁用网络适配器的 IPsec 批量处理功能](./Disable-NetAdapterIPsecOffload.md)

[Enable-NetAdapterIPsecOffload](./Enable-NetAdapterIPsecOffload.md)

[Set-NetAdapterIPsecOffload](./Set-NetAdapterIPsecOffload.md)

