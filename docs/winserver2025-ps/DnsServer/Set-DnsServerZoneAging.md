---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerZoneAging_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverzoneaging?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerZoneAging
---

# Set-DnsServerZoneAging

## 摘要
配置某个区域的DNS老化设置。

## 语法

```
Set-DnsServerZoneAging [[-Aging] <Boolean>] [-Name] <String> [-ComputerName <String>]
 [-ScavengeServers <IPAddress[]>] [-RefreshInterval <TimeSpan>] [-NoRefreshInterval <TimeSpan>] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsServerZoneAging` cmdlet 用于配置域名系统（DNS）服务器区域的老化设置。

即使某个资源已不再属于网络，其对应的资源记录仍可能保留在DNS服务器上。系统中的“老化设置”决定了这些记录何时会被删除（即被视为过时的记录并被清除）。

## 示例

#### 示例 1：设置一个资源收集服务器
```
PS C:\> Set-DnsServerZoneAging west01.contoso.com -Aging $True -ScavengeServers 172.18.1.1 -PassThru -Verbose
```

此命令启用名为 west01.contoso.com 的域的老化（即数据清除）功能，并指定了用于数据清理的服务器。

## 参数

### -Aging
用于指示是否为某个区域启用“老化”（aging）和“清理”（scavenging）功能。默认情况下，“老化”和“清理”功能是处于禁用状态的。

当 `$True` 为真时，DNS服务器在接收到动态更新请求时会刷新资源记录的时间戳。这使得DNS服务器能够收集这些资源记录。

当值为 `$False` 时，DNS服务器不会更新资源记录的时间戳，也不会扫描（或收集）资源记录。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: AgingEnabled

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -ComputerName
用于指定一个DNS服务器。如果未指定此参数，命令将在本地系统上运行。您可以指定一个IP地址，或任何能够解析为IP地址的值，例如完全合格域名（FQDN）、主机名或NETBIOS名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Cn

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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

### -Name
指定区域（zone）的名称。此 cmdlet 仅适用于主区域（primary zones）。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ZoneName

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NoRefreshInterval
该值以 `TimeSpan` 对象的形式表示时间长度。它表示记录的时间戳最后一次更新与时间戳能够被重新刷新之间的间隔。最小值为 0，最大值为 8760 小时。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
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

### -RefreshInterval
使用 `TimeSpan` 对象指定刷新间隔。在这段时间内，DNS 服务器可以更新那些具有非零时间戳的资源记录。

如果某个带有非零时间戳的资源记录在一段时间内未被更新（这段时间等于“NoRefreshInterval”参数与“RefreshInterval”参数所定义的数值之和），那么DNS服务器可以在下一次数据清理（scavenging）过程中删除该记录。

请不要选择一个小于该区域内已注册的资源记录最长刷新周期的值。

最小值为0，最大值为8760小时。默认值与该区域DNS服务器的**DefaultRefreshInterval**属性相同。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScavengeServers
指定用于DNS服务器的IP地址数组。这些服务器可以收集该区域中的记录信息。如果您没有指定任何记录收集服务器，那么对该区域具有权威性的任何主DNS服务器都可以进行记录收集操作。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerZoneAging

## 备注

## 相关链接

[Get-DnsServerZoneAging](./Get-DnsServerZoneAging.md)

