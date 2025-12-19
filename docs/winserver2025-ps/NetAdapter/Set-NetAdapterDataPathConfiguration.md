---
description: 设置网络适配器的名称、配置文件以及配置文件的来源。
external help file: MSFT_NetAdapterDataPathConfiguration.cdxml-help.xml
Module Name: NetAdapter
ms.date: 09/22/2021
online version: https://learn.microsoft.com/powershell/module/netadapter/set-netadapterdatapathconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-NetAdapterDataPathConfiguration
---

# 设置 NetAdapterDataPath 的配置

## 摘要
设置网络适配器的名称、配置文件以及配置文件的来源。

## 语法

### 按名称排序（默认值）
```
Set-NetAdapterDataPathConfiguration [-Name] <String[]> [-IncludeHidden] [-Profile <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ByInstanceID
```
Set-NetAdapterDataPathConfiguration -InterfaceDescription <String[]> [-IncludeHidden] [-Profile <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-NetAdapterDataPathConfiguration -InputObject <CimInstance[]> [-Profile <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-NetAdapterDataPathConfiguration` cmdlet 用于设置网络适配器的名称、配置文件以及配置文件的来源。该配置文件描述了 NDIS 轮询模式（NDIS Poll Mode）下的数据路径行为。NDIS 轮询模式是一种由操作系统控制的轮询执行模型，用于驱动网络接口的数据路径。目前，Windows 为服务器提供了四种内置配置文件，为客户端提供了两种内置配置文件。这些内置配置文件只能通过 PowerShell 进行设置。

## 示例

### 示例 1：设置网络适配器的配置信息
```powershell
PS> Set-NetAdapterDataPathConfiguration -Name "Ethernet" -Profile Legacy
```

将名为“Ethernet”的网络适配器的配置文件设置为“Legacy”（旧版/传统设置）。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值为本地计算机上的当前会话。

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
该参数表示此Cmdlet既包括可见的网络适配器，也包括隐藏的网络适配器。默认情况下，仅包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串会与所有（无论是隐藏的还是可见的）网络适配器进行匹配。

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
指定要输入到此 cmdlet 的数据。你可以使用这个参数，也可以将数据通过管道（pipe）传递给这个 cmdlet。

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
指定一个网络适配器接口描述数组。对于物理网络适配器而言，这通常是网络适配器制造商的名称后跟型号和描述，例如 `Contoso 12345 千兆网络设备`。

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
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -Profile

操作系统内置的四个配置文件之一名称。

该描述文件说明了NDIS轮询模式（NDIS Poll Mode）的数据路径行为。NDIS轮询模式是一种由操作系统控制的轮询执行模型，用于驱动网络接口的数据路径。

此参数的允许值如下：  
- Windows Server：**Dispatch**（默认值）、**Balanced**、**Legacy mode** 和 **Passive**。  
- Windows 客户端：**Balanced**（默认值）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

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
### Microsoft.ManagementInfrastructure.CimInstance[]
## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接
