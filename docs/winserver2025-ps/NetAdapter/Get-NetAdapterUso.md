---
description: 获取网络适配器的 USO（Universal System Operating）属性。
external help file: MSFT_NetAdapterUso.cdxml-help.xml
Module Name: NetAdapter
ms.date: 09/20/2021
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadapteruso?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapterUso
---

# Get-NetAdapterUso

## 摘要
获取网络适配器的 USO（Universal System Operating）属性。

## 语法

### 按名称查找（默认方式）
```
Get-NetAdapterUso [[-Name] <String[]>] [-IncludeHidden] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

### 按实例ID（ByInstanceID）
```
Get-NetAdapterUso -InterfaceDescription <String[]> [-IncludeHidden] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-NetAdapterUso` cmdlet 用于获取 UDP 分段卸载（UDP Segmentation Offload，简称 USO）功能。该功能允许网络接口卡（NIC）将大于网络介质最大传输单元（MTU）的 UDP 数据报的分段处理任务卸载到硬件层进行处理。这样一来，Windows 可以降低与每个数据包相关的 TCP/IP 处理所带来的 CPU 使用率。有关更多信息，请参阅 [UDP 分段卸载（USO）](/windows-hardware/drivers/network/udp-segmentation-offload-uso-)。

## 示例

### 示例 1：获取指定网络适配器的 USO 属性
```powershell
PS> Get-NetAdapterUso -Name "MyAdapter"
```

这条命令用于获取名为“MyAdapter”的网络适配器的USO属性。

### 示例 2：显示指定网络适配器的所有 USO 属性
```
PS> Get-NetAdapterUso -Name "MyAdapter" | Format-List -Property "*"
```

此命令会显示名为“MyAdapter”的网络适配器的所有USO属性。

### 示例 3：获取所有已启用 USO 功能的网络适配器
```
PS> Get-NetAdapterUso -Name "*" | Where-Object -FilterScript { $_.Enabled }
```

这个命令可以获取所有启用了USO功能的网络适配器。


## 参数

### -AsJob
该cmdlet会以后台作业的形式运行。使用此参数可以执行那些需要较长时间才能完成的任务。cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
该参数表示此cmdlet同时包含可见的网络适配器和隐藏的网络适配器。默认情况下，仅包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串会与所有（无论是隐藏的还是可见的）网络适配器进行匹配。

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
指定一个网络适配器接口描述数组。对于物理网络适配器而言，这通常是指网络适配器的供应商名称后跟型号编号和描述，例如“Contoso 12345 千兆网络设备”。

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
该参数用于指定可以同时运行的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell 会根据计算机上正在运行的 CIMcmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]
## 输出

### Microsoft.ManagementInfrastructure.CimInstance
### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterUsoSettingData
## 备注

## 相关链接
