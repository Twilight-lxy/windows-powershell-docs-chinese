---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterVmq.cmdletDefinition.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadaptervmq?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapterVmq
---

# Get-NetAdapterVmq

## 摘要
获取网络适配器的VMQ属性。

## 语法

### 按名称排序（默认值）
```
Get-NetAdapterVmq [[-Name] <String[]>] [-IncludeHidden] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

### ByInstanceID
```
Get-NetAdapterVmq -InterfaceDescription <String[]> [-IncludeHidden] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-NetAdapterVmq` cmdlet 可以获取具备虚拟机队列（VMQ）功能的网卡的属性。VMQ 是一种用于 vmswitch 的可扩展网络技术，它根据数据包的目标 MAC 地址对数据包进行哈希处理。

## 示例

#### 示例 1：从指定的网络适配器获取 VMQ 属性
```
PS C:\> Get-NetAdapterVmq -Name "GuestTrafficAdapter"
```

此命令用于获取名为 GuestTrafficAdapter 的网络适配器的 VMQ（虚拟消息队列）属性。

### 示例 2：从指定的网络适配器中获取所有 VMQ 属性
```
PS C:\> Get-NetAdapterVmq -Name "GuestTrafficAdapter" | Format-List -Property "*"
```

此命令会显示名为 GuestTrafficAdapter 的网络适配器的所有 VMQ（虚拟消息队列）属性。

### 示例 3：获取所有启用了虚拟消息队列（VMQ）功能的网络适配器
```
PS C:\> Get-NetAdapterVmq -Name "*" | Where-Object -FilterScript { $_.Enabled }
```

此命令会获取所有启用了VMQ功能的、具备VMQ支持的网络适配器。

## 参数

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数来执行需要较长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlet；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
这表示该 cmdlet 在操作过程中会同时包含可见的网络适配器和隐藏的网络适配器。默认情况下，只有可见的网络适配器会被包括在内。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串会与所有（无论是隐藏的还是可见的）网络适配器进行匹配。

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
指定一个网络适配器接口描述数组。对于物理网络适配器来说，这通常是网络适配器的制造商名称后跟随型号和描述，例如“Contoso 12345 千兆网络设备”。

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
指定可以同时运行的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterVmqSettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[禁用 NetAdapterVmq](./Disable-NetAdapterVmq.md)

[Enable-NetAdapterVmq](./Enable-NetAdapterVmq.md)

[Get-NetAdapterVmqQueue](./Get-NetAdapterVmqQueue.md)

[Set-NetAdapterVmq](./Set-NetAdapterVmq.md)

