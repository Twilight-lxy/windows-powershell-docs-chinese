---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4Failover_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/set-dhcpserverv4failover?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DhcpServerv4Failover
---

# Set-DhcpServerv4Failover

## 摘要
修改现有故障转移关系的属性。

## 语法

```
Set-DhcpServerv4Failover [-ComputerName <String>] [-Name] <String> [-AutoStateTransition <Boolean>]
 [-MaxClientLeadTime <TimeSpan>] [-SharedSecret <String>] [-StateSwitchInterval <TimeSpan>] [-PartnerDown]
 [-Force] [-LoadBalancePercent <UInt32>] [-ReservePercent <UInt32>] [-PassThru] [-Mode <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DhcpServerv4Failover` cmdlet 用于修改现有故障转移关系的属性。

如果关系的故障转移模式是负载均衡，或者正在被设置为负载均衡，则可以指定 *LoadBalancePercent*、*MaxClientLeadTime*、*StateSwitchInterval*、*AutoStateTransition* 和 *SharedSecret* 等参数。

如果关系的故障转移模式是“热备份”（hot standby），或者正在被设置为“热备份”，则可以指定以下参数：*ReservePercent*、*MaxClientLeadTime*、*StateSwitchInterval*、*AutoStateTransition* 和 *SharedSecret*。

如果 *SharedSecret* 参数的值为 `$Null`，则数据结构中的 **enableauth** 被设置为 `$False`；如果 *SharedSecret* 参数的值不为 `$Null`，则数据结构中的 **enableauth** 被设置为 `$True`。

如果指定了 *SharedSecret* 参数，则会请求用户确认是否允许在网络中以明文形式传输该共享密钥。

如果您指定了*Mode*参数来更改故障转移关系的模式，则系统会默认请求确认（即需要用户的确认操作）。

## 示例

### 示例 1：修改负载均衡故障转移关系中的参数
```
PS C:\> Set-DhcpServerv4Failover -ComputerName "dhcpserver.contoso.com" -Name "SFO-SIN-Failover" -LoadBalancePercent 70 -MaxClientLeadTime 2:00:00 -AutoStateTransition $True -StateSwitchInterval 2:00:00
```

此示例修改了名为 SFO-SIN-Failover 的负载均衡故障转移关系的相关参数，该关系位于名为 dhcpserver.contoso.com 的计算机上：70% 的客户端请求将由运行在 dhcpserver.contoso.com 上的 DHCP 服务器服务处理，30% 的客户端请求将由运行在 dhcpserver2.contoso.com 上的 DHCP 服务器服务处理。故障转移关系的最大延迟时间被设置为 2 小时。自动状态转换功能（从 COMMUNICATION INTERRUPTED 状态转换为 PARTNER DOWN 状态）已被启用，且该自动状态转换的定时器也被设置为 2 小时。

### 示例 2：修改带有备用的负载均衡故障转移关系的参数
```
PS C:\> Set-DhcpServerv4Failover -ComputerName "dhcpserver.contoso.com" -Name "SFO-SIN-Failover" -ReservePercent 10 -MaxClientLeadTime 2:00:00 -AutoStateTransition $True -StateSwitchInterval 2:00:00
```

此示例修改了名为 SFO-SIN-Failover 的热备切换关系的相关参数，该关系位于名为 dhcpserver.contoso.com 的计算机上：范围内 10% 的可用 IP 地址将被预留用于备用 DHCP 服务器服务。故障切换关系的最大客户端延迟时间被设置为 2 小时。从 “COMMUNICATION INTERRUPTED” 状态自动转换为 “PARTNER DOWN” 状态的功能已被启用，且自动状态转换的定时器也被设置为 2 小时。

### 示例 3：更改故障转移关系的模式
```
PS C:\> Set-DhcpServerv4Failover -Name "SFO-SIN-Failover" -ComputerName "dhcpserver.contoso.com" -Mode "LoadBalance" -LoadBalancePercent 60
```

这个示例将故障转移关系 SFO-SIN-Failover 的模式更改为 *LoadBalance*。名为 dhcpserver.contoso.com 的计算机负责为 60% 的客户端提供服务。

## 参数

### -AsJob
以后台作业的形式运行该 cmdlet。使用此参数来执行耗时较长的命令。cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `-*Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -AutoStateTransition
该参数用于指定在处于“COMMUNICATION INTERRUPTED”状态时，根据定时器的超时情况，是否自动从“COMMUNICATION INTERRUPTED”状态切换到“PARTNER DOWN”状态。切换的启用与否由参数*StateSwitchInterval*控制。默认值为$False。

如果指定了*StateSwitchInterval*参数，则该参数的值将为$True。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
指定目标计算机的DNS名称，或IPv4或IPv6地址。该计算机运行动态主机配置协议（DHCP）服务器服务。

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

### -Force
如果指定了 `SharedSecret` 参数，则需要用户确认，因为该参数的值可能会在远程管理过程中以明文形式传输。指定此参数将关闭用户确认功能。

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

### -LoadBalancePercent
指定应由本地DHCP服务器服务或运行在*ComputerName*参数所指定的计算机上的DHCP服务器服务处理的DHCP客户端请求的百分比。剩余的DHCP客户端请求将由合作伙伴DHCP服务器服务进行处理。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaxClientLeadTime
指定故障转移关系中客户端的最大延迟时间（即从请求发送到响应返回所需的最长时间）。

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

### -Mode
指定故障转移关系的模式。该参数的可接受值包括：

- HotStandby.
Changes the mode to hot standby.
- LoadBalance.
Changes the mode to load balance.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: LoadBalance, HotStandby

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定要修改属性的故障转移关系的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PartnerDown
将DHCP服务器服务的状态从“COMMUNICATION INTERRUPTED”更改为“PARTNER DOWN”。

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

### -ReservePercent
指定应在备用DHCP服务器服务上预留的、来自免费IPv4地址池的百分比。

在发生故障转移的情况下，备用DHCP服务器服务中从这个预留地址池分配的IPv4地址将会被租给新的DHCP客户端。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SharedSecret
指定用于消息认证的共享密钥。要关闭消息认证功能，请将此参数值设置为 `$Null`。

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

### -StateSwitchInterval
指定 DHCP 服务器服务在处于“通信中断”（COMMUNICATION INTERRUPTED）状态时应当继续运行的时间间隔，之后才会切换到“合作伙伴故障”（PARTNER DOWN）状态。

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

### -ThrottleLimit
指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于会话或整个计算机。

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
展示了如果该cmdlet运行会会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Failover
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名称。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Failover
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名称。

## 备注

## 相关链接

[Add-DhcpServerv4Failover](./Add-DhcpServerv4Failover.md)

[Add-DhcpServerv4FailoverScope](./Add-DhcpServerv4FailoverScope.md)

[Get-DhcpServerv4Failover](./Get-DhcpServerv4Failover.md)

[Invoke-DhcpServerv4FailoverReplication](./Invoke-DhcpServerv4FailoverReplication.md)

[Remove-DhcpServerv4Failover](./Remove-DhcpServerv4Failover.md)

[Remove-DhcpServerv4FailoverScope](./Remove-DhcpServerv4FailoverScope.md)

