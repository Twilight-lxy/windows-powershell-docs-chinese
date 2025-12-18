---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV6Scope_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/remove-dhcpserverv6scope?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DhcpServerv6Scope
---

# 删除 DHCP Serverv6 范围

## 摘要
从DHCP服务器服务中删除与指定前缀对应的IPv6地址范围。

## 语法

```
Remove-DhcpServerv6Scope [-Prefix] <IPAddress[]> [-Force] [-Passthru] [-ComputerName <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DhcpServerv6Scope` cmdlet 用于删除动态主机配置协议（DHCP）服务器服务中与指定前缀相对应的 IPv6 范围。删除某个范围会同时删除与该范围关联的所有设置和租约（如果存在的话）。

## 示例

### 示例 1：删除一个作用域
```
PS C:\> Remove-DhcpServerv6Scope -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020::
```

这个示例会从指定的DHCP服务器服务中删除指定的DHCPv6范围（scope）。

### 示例 2：即使某个作用域包含正在使用的租约，也将其删除
```
PS C:\> Remove-DhcpServerv6Scope -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -Force
```

这个示例会从指定的 DHCP 服务器服务中删除指定的 DHCPv6 范围，而无需请求用户确认。即使该范围处于活动状态或包含正在使用的客户端租约，系统也会执行删除操作。

### 示例 3：删除 DHCP 服务器服务上所有被禁用的作用域
```
PS C:\> Get-DhcpServerv6Scope | Where-Object -FilterScript { $_.State -Eq "Inactive" } | Remove-DhcpServerv6Scope -Force -Passthru
```

这个示例会删除DHCP服务器服务中所有被禁用的作用域。`Get-DhcpServerv6Scope` cmdlet用于获取作用域对象，并将这些对象传递给`Where-Object` cmdlet。`Where-Object` cmdlet会根据对象的“状态”（是否处于“InActive”或“禁用”状态）对这些对象进行筛选，然后将符合条件的对象传递给下一个cmdlet，从而删除这些被禁用的作用域。如果在没有使用`Force`参数的情况下删除了非空的作用域，该cmdlet会显示错误提示。需要注意的是，这个cmdlet不会要求用户进行确认；而已为空的、处于活动状态的作用域同样会在没有`Force`参数的情况下被删除。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业的结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
指定运行DHCP服务器服务的目标计算机的DNS名称或IPv4/IPv6地址。

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
该参数指定：即使某个作用域中存在有效的租约（即租用关系仍在生效），此 cmdlet 也会删除该作用域。

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

### -Passthru
返回一个表示您正在操作的该项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -Prefix
指定一个或多个将被删除的IPv6子网前缀（及其所属的范围）。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果运行该 cmdlet 会发生什么情况。但实际上并没有运行该 cmdlet。

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

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Scope[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv6Scope](./Add-DhcpServerv6Scope.md)

[Get-DhcpServerv6Scope](./Get-DhcpServerv6Scope.md)

[Get-DhcpServerv6ScopeStatistics](./Get-DhcpServerv6ScopeStatistics.md)

[Set-DhcpServerv6Scope](./Set-DhcpServerv6Scope.md)

