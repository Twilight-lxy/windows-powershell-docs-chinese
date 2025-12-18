---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerScavenging_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverscavenging?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerScavenging
---

# Set-DnsServerScavenging

## 摘要
更改DNS服务器扫描设置。

## 语法

```
Set-DnsServerScavenging [-ApplyOnAllZones] [-ComputerName <String>] [[-ScavengingState] <Boolean>]
 [[-RefreshInterval] <TimeSpan>] [[-ScavengingInterval] <TimeSpan>] [[-NoRefreshInterval] <TimeSpan>]
 [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-DnsServerScavenging` cmdlet 用于更改域名系统（DNS）服务器的扫描设置。如果任何设置操作失败，该 cmdlet 会继续配置其他设置。该 cmdlet 会显示它已更改的设置以及未更改的设置。

## 示例

### 示例 1：更改资源记录的刷新间隔
```
PS C:\> Set-DnsServerScavenging -RefreshInterval 1.00:00:00 -Verbose -PassThru
```

这个命令将本地DNS服务器上的数据扫描（scavenging）的刷新间隔设置为1天。

## 参数

### -ApplyOnAllZones
表示服务器设置适用于所有区域。

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
以后台作业的方式运行该cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。您可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的字符串，例如完全qualified域名（FQDN）、主机名或NETBIOS名称。

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
在运行该cmdlet之前，会提示您进行确认。

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

### -NoRefreshInterval
将一段时间指定为一个 **TimeSpan** 对象。**NoRefreshInterval** 设置了一个时间段，在此期间不会接受对动态更新记录的刷新请求。服务器上的各个区域会自动继承这个值。

这个值表示记录的时间戳最后一次更新与时间戳能够被刷新的最早时间之间的间隔。最小值为0，最大值为8760小时（即7天）。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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
以 `Timespan` 对象的形式指定刷新间隔。在这段时间内，DNS 服务器可以更新具有非零时间戳的资源记录。服务器上的区域会自动继承这个值。

如果DNS服务器没有更新某个具有非零时间戳的资源记录，那么在该DNS服务器下一次进行资源清理（scavenging）时，它可能会删除该记录。

请不要选择一个小于该区域中注册的资源记录的最长刷新周期的值。

最小值为0。最大值为8760小时（即7天）。默认值与该区域DNS服务器的**DefaultRefreshInterval**属性相同。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScavengingInterval
以 **TimeSpan** 对象的形式指定一段时间长度。**ScavengingInterval** 决定了 DNS 服务器的清除功能是否启用，并设置了清除周期之间的时间间隔（以小时为单位）。

默认设置为 0，此时 DNS 服务器的扫描功能将被禁用。如果设置值大于 0，则会启用扫描功能，并指定扫描周期之间的时间间隔（以 **dd.hh:mm:ss** 的格式表示，单位为天、小时、分钟和秒）。最小值为 0，最大值为 365.00:00:00（即 1 年）。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScavengingState
指定是否启用对过期记录的自动清理功能。**ScavengingState** 参数用于确定在新创建的区域中，默认情况下是否启用 DNS 清理功能。该参数的可接受值为：  
- `$False`：禁用清理功能。这是默认设置。  
- `$True`：启用清理功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的命令行脚本（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令行脚本的数量来计算一个最优的操作限制值。这个操作限制仅适用于当前正在运行的命令行脚本，而不适用于整个会话或计算机本身。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerScavenging

## 备注

## 相关链接

[Get-DnsServerScavenging](./Get-DnsServerScavenging.md)

[开始DNS服务器扫描任务](./Start-DnsServerScavenging.md)

