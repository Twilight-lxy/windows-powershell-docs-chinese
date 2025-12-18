---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV4ScopeStatistics_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv4scopestatistics?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv4ScopeStatistics
---

# Get-DhcpServerv4ScopeStatistics

## 摘要
获取与为DHCP服务器服务指定的IPv4范围ID对应的IPv4范围统计信息。

## 语法

```
Get-DhcpServerv4ScopeStatistics [[-ScopeId] <IPAddress[]>] [-ComputerName <String>] [-Failover]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DhcpServerv4ScopeStatistics` cmdlet 可获取与动态主机配置协议（DHCP）服务器服务中指定的 IPv4 范围标识符（IDs）相对应的范围统计信息。如果您未指定 `ScopeId` 参数，该 cmdlet 会获取所有 IPv4 范围的统计信息。

## 示例

### 示例 1：获取 DHCP 服务器服务上各个作用域的范围统计信息
```
PS C:\> Get-DhcpServerv4ScopeStatistics -ComputerName "dhcpServer.contoso.com"
```

这个示例获取了指定DHCP服务器服务上各个作用域（scopes）的相关统计信息。

### 示例 2：获取 DHCP 服务器服务上某个作用域的范围统计信息
```
PS C:\> Get-DhcpServerv4ScopeStatistics -ComputerName "dhcpServer.contoso.com" -ScopeId 10.10.10.0
```

这个示例用于获取指定DHCP服务器服务上指定作用域的作用域统计信息。

### 示例 3：获取 DHCP 服务器服务上某个作用域（scope）的统计信息（包括故障转移情况）
```
PS C:\> Get-DhcpServerv4ScopeStatistics -ComputerName "dhcpServer.contoso.com" -ScopeId 10.10.10.0 -Failover
```

此示例会获取指定DHCP服务器服务上指定范围内的范围统计信息，包括与故障转移相关的统计信息（前提是该范围属于某个故障转移关系）。

### 示例 4：获取 DHCP 服务器服务上各个作用域（包括故障转移机制）的范围统计信息
```
PS C:\> Get-DhcpServerv4ScopeStatistics -ComputerName "dhcpServer.contoso.com" -Failover
```

此示例会获取指定DHCP服务器服务上所有作用域的范围统计信息，包括与故障转移相关的统计信息（如果该作用域属于某个故障转移关系的话）。

### 示例 5：获取 DHCP 服务器服务上那些部分 IP 地址范围已被耗尽的作用域的统计信息
```
PS C:\> Get-DhcpServerv4ScopeStatistics -ComputerName "dhcpServer.contoso.com" | Where-Object -FilterScript { $_.PercentageInUse -Gt 80 }
```

这个示例获取了指定DHCP服务器服务上那些IP地址范围已使用超过80%的命名空间的统计信息。

## 参数

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定运行DHCP服务器服务的目标计算机的DNS名称、IPv4地址或IPv6地址。

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

### -Failover
指定如果某个范围被配置为支持故障转移（failover），那么与该故障转移相关的统计信息也将作为该范围统计信息的一部分被返回。

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

### -ScopeId
指定用于返回统计数据的范围ID（以IPv4地址格式表示）。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行此cmdlet的最大操作数量。如果省略了此参数或输入了`0`，那么Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算一个最佳的限制值（即并发操作的上限）。这个限制仅适用于当前执行的cmdlet，而不适用于整个会话或整个计算机。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4ScopeStatistics[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv4Scope](./Add-DhcpServerv4Scope.md)

[Get-DhcpServerv4Scope](./Get-DhcpServerv4Scope.md)

[Remove-DhcpServerv4Scope](./Remove-DhcpServerv4Scope.md)

[Set-DhcpServerv4Scope](./Set-DhcpServerv4Scope.md)

