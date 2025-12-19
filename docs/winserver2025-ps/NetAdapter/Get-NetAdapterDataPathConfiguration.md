---
description: 获取网络适配器的名称、配置文件（profile）以及该配置文件的来源信息。
external help file: MSFT_NetAdapterDataPathConfiguration.cdxml-help.xml
Module Name: NetAdapter
ms.date: 09/23/2021
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadapterdatapathconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapterDataPathConfiguration
---

# 获取-NetAdapterDataPathConfiguration

## 摘要
获取网络适配器的名称、配置文件（profile）以及该配置文件的来源信息。

## 语法

### 按名称查找（默认方式）
```
Get-NetAdapterDataPathConfiguration [[-Name] <String[]>] [-Profile <String[]>] [-ProfileSource <UInt32[]>]
 [-IncludeHidden] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 按实例ID（ByInstanceID）
```
Get-NetAdapterDataPathConfiguration -InterfaceDescription <String[]> [-Profile <String[]>]
 [-ProfileSource <UInt32[]>] [-IncludeHidden] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-NetAdapterDataPathConfiguration` cmdlet 可以获取网络适配器的名称、配置文件（profile）以及该配置文件的来源。该配置文件描述了 NDIS 轮询模式（NDIS Poll Mode）下的数据路径行为。NDIS 轮询模式是一种由操作系统控制的轮询执行模型，用于驱动网络接口的数据路径。

## 示例

### 示例 1：获取网络适配器的数据路径信息
```powershell
PS> Get-NetAdapterDataPathConfiguration -Name "Ethernet"
```

获取名为“Ethernet”的网络适配器的数据路径配置文件及其配置文件的来源信息。

## 参数

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数可以执行需要较长时间才能完成的命令。cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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
该参数表示此 cmdlet 包含可见的网络适配器和隐藏的网络适配器。默认情况下，仅包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串会与所有（无论是隐藏的还是可见的）网络适配器进行匹配。

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
指定一个网络适配器接口描述的数组。对于物理网络适配器来说，这通常是网络适配器供应商的名称后跟型号和描述，例如 `Contoso 12345 千兆网络设备`。

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

### -Profile
操作系统内置的四个配置文件之一名称。

该描述文件介绍了NDIS轮询模式（NDIS Poll Mode）的数据路径行为。NDIS轮询模式是一种由操作系统控制的轮询执行模型，用于驱动网络接口的数据路径。

此参数允许的值有：**传统模式（Legacy mode）**、**平衡模式（Balanced）**、**被动模式（Passive）** 和 **分发模式（Dispatch）**。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ProfileSource

表示配置文件的来源。可选值包括 **BuiltIn**（内置的）和 **Custom**（自定义的）。

```yaml
Type: UInt32[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]
## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接
