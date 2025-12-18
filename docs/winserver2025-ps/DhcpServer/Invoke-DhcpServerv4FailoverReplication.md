---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4FailoverReplication_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/invoke-dhcpserverv4failoverreplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Invoke-DhcpServerv4FailoverReplication
---

# 调用 DHCPServerv4FailoverReplication

## 摘要
在故障转移伙伴（DHCP服务器服务）之间复制作用域配置。

## 语法

### 名称（默认值）
```
Invoke-DhcpServerv4FailoverReplication [-ComputerName <String>] [-Force] [[-Name] <String[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ScopeId
```
Invoke-DhcpServerv4FailoverReplication [-ComputerName <String>] [-Force] -ScopeId <IPAddress[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Invoke-DhcpServerv4FailoverReplication` cmdlet 可以在故障转移伙伴（即使用动态主机配置协议 [DHCP] 的服务器服务）之间复制作用域配置信息。

如果您指定了 *ScopeId* 参数，并且该范围属于某个故障转移关系（failover relationship）的一部分，那么指定范围内的配置信息将会被复制到故障转移对应的 DHCP 服务器上。这些配置信息包括所有的范围属性、预留项（reservations）、范围选项值（scope option values）以及相关策略（policies）。

如果您指定了“名称”参数，则与故障转移关系相关的所有范围的配置信息都会被复制到合作伙伴的DHCP服务器服务中。

如果您不指定任何参数，DHCP服务器服务上所有故障转移范围的配置将会被复制到相应的合作伙伴DHCP服务器服务中。

## 示例

#### 示例 1：复制用于故障转移关系的作用域配置
```
PS C:\> Invoke-DhcpServerv4FailoverReplication -ComputerName "dhcpserver.contoso.com" -Name "SFO-SIN-Failover"
```

这个示例将名为“SFO-SIN-Failover”的故障转移关系中涉及的所有范围的配置，从运行在计算机dhcpserver.contoso.com上的DHCP服务器服务复制到对应的合作伙伴DHCP服务器服务。

### 示例 2：复制服务器故障转移关系中作用域（scopes）的配置
```
PS C:\> Invoke-DhcpServerv4FailoverReplication -ComputerName "dhcpserver.contoso.com"
```

这个示例将根据一个或多个包含DHCP服务器服务的故障转移关系，将运行在名为dhcpserver.contoso.com的计算机上的DHCP服务器服务中的所有故障转移设置复制到一个或多个相应的合作伙伴DHCP服务器服务上。

### 示例 3：复制作用域（scopes）的配置
```
PS C:\> Invoke-DhcpServerv4FailoverReplication -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0,10.20.20.0
```

这个示例将作用域 10.10.10.0 和 10.20.20.0 的配置复制到相应的合作伙伴计算机上，这些计算机运行着包含这些作用域的故障转移关系中的 DHCP 服务器服务。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行耗时较长的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
指定运行 DHCP 服务器服务的目标计算机的 DNS 名称、IPv4 地址或 IPv6 地址。

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
强制命令运行，而无需询问用户确认。

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

### -Name
指定故障转移关系的名称。一个或多个指定关系的所有配置信息都会被复制到合作伙伴的 DHCP 服务器服务上。

```yaml
Type: String[]
Parameter Sets: Name
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScopeId
指定配置被复制的范围标识符（ID），该标识符采用 IPv4 地址格式表示。

```yaml
Type: IPAddress[]
Parameter Sets: ScopeId
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为`0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前执行的 cmdlet，而不影响整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Failover
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径指定了底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径指定了底层 WMI 对象的命名空间和类名。

## 输出

### System.String[]

## 备注

## 相关链接

[Add-DhcpServerv4Failover](./Add-DhcpServerv4Failover.md)

[Add-DhcpServerv4FailoverScope](./Add-DhcpServerv4FailoverScope.md)

[Get-DhcpServerv4Failover](./Get-DhcpServerv4Failover.md)

[Remove-DhcpServerv4Failover](./Remove-DhcpServerv4Failover.md)

[Remove-DhcpServerv4FailoverScope](./Remove-DhcpServerv4FailoverScope.md)

[Set-DhcpServerv4Failover](./Set-DhcpServerv4Failover.md)

