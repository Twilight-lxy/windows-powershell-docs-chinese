---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4Failover_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/add-dhcpserverv4failover?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DhcpServerv4Failover
---

# Add-DhcpServerv4Failover

## 摘要
在DHCP服务器服务上添加一个IPv4故障转移关系。

## 语法

### LoadBalance（默认值）
```
Add-DhcpServerv4Failover [-ComputerName <String>] [-Name] <String> [-PartnerServer] <String>
 [-ScopeId] <IPAddress[]> [-MaxClientLeadTime <TimeSpan>] [-AutoStateTransition <Boolean>]
 [-StateSwitchInterval <TimeSpan>] [-Force] [-SharedSecret <String>] [-PassThru] [-LoadBalancePercent <UInt32>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### HotStandby
```
Add-DhcpServerv4Failover [-ComputerName <String>] [-Name] <String> [-PartnerServer] <String>
 [-ScopeId] <IPAddress[]> [-MaxClientLeadTime <TimeSpan>] [-AutoStateTransition <Boolean>]
 [-StateSwitchInterval <TimeSpan>] [-Force] [-SharedSecret <String>] [-PassThru] [-ReservePercent <UInt32>]
 [-ServerRole <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-DhcpServerv4Failover` cmdlet 可用于向动态主机配置协议（DHCP）服务器服务添加新的 IPv4 故障转移关系。您可以选择通过负载均衡模式或热备模式来设置故障转移关系。

这个cmdlet会在使用指定参数的两个DHCP服务器服务上创建故障转移关系。在源DHCP服务器服务（或运行DHCP服务器服务的本地计算机）上指定的*ScopeId*参数值，会在对应的伙伴DHCP服务器服务上也进行相同的设置。

如果指定了*SharedSecret*参数，则新创建的故障转移关系将自动启用消息摘要认证功能。

默认情况下，如果指定了 *SharedSecret* 参数，则会要求用户进行确认。

## 示例

#### 示例 1：创建一种“active-active”类型的故障转移关系
```
PS C:\> Add-DhcpServerv4Failover -ComputerName "dhcpserver.contoso.com" -Name "SFO-SIN-Failover" -PartnerServer "dhcpserver2.contoso.com" -ScopeId 10.10.10.0,10.20.20.0 -SharedSecret "sEcReT"
```

这个示例在名为dhcpserver.contoso.com和dhcpserver2.contoso.com的两台计算机上创建了一个负载均衡（即主动-主动类型的故障转移）机制。在这两台计算机上运行的DHCP服务器服务分别负责管理10.10.10.0和10.20.20.0这两个IP地址范围。当在dhcpserver2.contoso.com上创建故障转移关系时，这些IP地址范围也会在该服务器上的DHCP服务器服务中被相应地配置起来。服务器之间的通信采用了消息认证机制，并使用了一个预先指定的共享密钥来进行身份验证。

### 示例 2：创建主动-被动故障转移关系
```
PS C:\> Add-DhcpServerv4Failover -ComputerName "dhcpserver.contoso.com" -Name "SFO-SIN-Failover" -PartnerServer "dhcpserver2.contoso.com" -ServerRole Standby -ScopeId 10.10.10.0,10.20.20.0
```

这个示例在名为dhcpserver.contoso.com和dhcpserver2.contoso.com的计算机上运行的DHCP服务器服务之间建立了一种热备（即主动-被动）故障转移关系。其中，名为dhcpserver.contoso.com的计算机上的DHCP服务器服务负责管理10.10.10.0和10.20.20.0这两个IP地址范围；这些地址范围也会被自动添加到名为dhcpserver2.contoso.com的计算机上运行的DHCP服务器服务中，作为故障转移关系的一部分。在该故障转移关系中，名为dhcpserver.contoso.com的计算机上的DHCP服务器服务将作为备用服务器（即“Standby DHCP Server”），而名为dhcpserver2.contoso.com的计算机上的DHCP服务器服务则作为主服务器（即“Active DHCP Server”）。

### 示例 3：创建一个主动-主动故障转移关系，并指定负载均衡的数量
```
PS C:\> Add-DhcpServerv4Failover -ComputerName "dhcpserver.contoso.com" -Name "SFO-SIN-Failover" -PartnerServer "dhcpserver2.contoso.com" -ScopeId 10.10.10.0,10.20.20.0 -LoadBalancePercent 70 -MaxClientLeadTime 2:00:00 -AutoStateTransition $True -StateSwitchInterval 2:00:00
```

这个示例创建了一个负载均衡机制，即“主动-主动”模式的故障转移关系。该机制应用于运行在名为 dhcpserver.contoso.com 和 dhcpserver2.contoso.com 的两台计算机上的 DHCP 服务器服务之间。其中，名为 dhcpserver.contoso.com 的 DHCP 服务器服务负责处理 10.10.10.0 和 10.20.20.0 这两个 IP 地址范围内的客户端请求；这两个地址范围也会被同步添加到运行在 dhcpserver2.contoso.com 上的 DHCP 服务器服务中，作为故障转移关系的一部分。70% 的客户端请求将由名为 dhcpserver.contoso.com 的 DHCP 服务器服务处理，30% 由名为 dhcpserver2.contoso.com 的 DHCP 服务器服务处理。故障转移关系的最大响应延迟时间被设置为 2 小时。同时，系统启用了从 “COMMUNICATION INTERRUPTED” 状态自动切换到 “PARTNER DOWN” 状态的功能，并将自动状态切换的定时器设置为 2 小时。

### 示例 4：创建具有备份功能的主动-被动故障转移关系
```
PS C:\> Add-DhcpServerv4Failover -ComputerName "dhcpserver.contoso.com" -Name "SFO-SIN-Failover" -PartnerServer "dhcpserver2.contoso.com" -ScopeId 10.10.10.0,10.20.20.0 -ReservePercent 10 -MaxClientLeadTime 2:00:00 -AutoStateTransition $True -StateSwitchInterval 2:00:00
```

这个示例在名为 dhcpserver.contoso.com 的计算机上运行的 DHCP 服务器服务与名为 dhcpserver2.contoso.com 的计算机上的 DHCP 服务器服务之间建立了一种热备（即主动-被动）故障转移关系。名为 dhcpserver.contoso.com 的计算机上的 DHCP 服务器服务负责管理 10.10.10.0 和 10.20.20.0 这两个 IP 地址范围；这些地址范围也会在名为 dhcpserver2.contoso.com 的计算机上的 DHCP 服务器服务上被创建，作为故障转移关系的一部分。在故障转移关系中，名为 dhcpserver2.contoso.com 的计算机上的 DHCP 服务器服务将作为备用 DHCP 服务器，而名为 dhcpserver.contoso.com 的计算机上的 DHCP 服务器服务将作为主 DHCP 服务器。这些地址范围内 10% 的可用 IP 地址将被预留给备用 DHCP 服务器使用。故障转移关系的最大客户端响应延迟时间被设置为 2 小时；同时，系统启用了从 “COMMUNICATED INTERUPTED” 状态自动切换到 “PARTNER DOWN” 状态的功能，该自动状态切换的定时器也被设置为 2 小时。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在处于“COMMUNICATION INTERRUPTED”状态时，根据*StateSwitchInterval*参数指定的时间间隔，指定从该状态自动切换到“PARTNER DOWN”状态的启用条件。这一切换过程发生在定时器到期之后。

此参数的可接受值为：True 或 False。默认值为 False。

如果指定了*StateSwitchInterval*参数，那么该参数将自动被设置为True。

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
在远程会话或远程计算机上运行该cmdlet。输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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
指定运行 DHCP 服务器服务的目标计算机的 DNS 名称或 IPv4/IPv6 地址。

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
说明：如果指定了 *SharedSecret* 参数，则需要用户进行确认，因为该参数的值可能会在远程管理过程中以明文形式传输。指定此参数将关闭用户确认功能。

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
指定应由本地DHCP服务器服务或运行在*ComputerName*参数所指定的计算机上的DHCP服务器服务处理的DHCP客户端请求的百分比。剩余的请求将由合作伙伴DHCP服务器服务进行处理。

默认值是50%。

```yaml
Type: UInt32
Parameter Sets: LoadBalance
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaxClientLeadTime
指定故障转移关系中客户端的最长等待时间（即从请求发送到响应返回所需的时间）。默认值为 1 小时。

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

### -Name
指定要创建的故障转移关系的名称。

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

### -PartnerServer
指定用于创建故障转移关系的合作伙伴DHCP服务器服务的IPv4地址或主机名。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
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

### -ReservePercent
指定在相应作用域的 IPv4 地址池中，应预留给备用 DHCP 服务器服务的免费 IPv4 地址所占的百分比。在发生故障转移时，备用 DHCP 服务器服务中的这些预留地址将会被租借给新的 DHCP 客户端。默认值为 5%。

```yaml
Type: UInt32
Parameter Sets: HotStandby
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScopeId
指定要添加到故障转移关系中的范围标识符（以 IPv4 地址格式表示）。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ServerRole
指定本地DHCP服务器服务在热备模式中的角色。该参数的合法取值为：Active（活动）或Standby（备用）。默认情况下，本地DHCP服务器服务处于Active状态；而指定的伙伴DHCP服务器服务则处于Standby状态。

```yaml
Type: String
Parameter Sets: HotStandby
Aliases:
Accepted values: Active, Standby

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SharedSecret
指定用于消息摘要认证的共享密钥。如果未指定，则消息摘要认证功能将被关闭。

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
指定DHCP服务器服务在处于“COMMUNICATION INTERRUPTED”状态期间持续运行的时间间隔，之后该服务会转换为“PARTNER DOWN”状态。

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最优限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Failover
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

## 备注

## 相关链接

[Add-DhcpServerv4FailoverScope](./Add-DhcpServerv4FailoverScope.md)

[Get-DhcpServerv4Failover](./Get-DhcpServerv4Failover.md)

[Invoke-DhcpServerv4FailoverReplication](./Invoke-DhcpServerv4FailoverReplication.md)

[Remove-DhcpServerv4Failover](./Remove-DhcpServerv4Failover.md)

[Remove-DhcpServerv4FailoverScope](./Remove-DhcpServerv4FailoverScope.md)

[Set-DhcpServerv4Failover](./Set-DhcpServerv4Failover.md)

