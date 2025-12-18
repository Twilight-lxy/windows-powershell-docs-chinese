---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv6Lease_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/remove-dhcpserverv6lease?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DhcpServerv6Lease
---

# 删除 DHCP Serverv6 的租约

## 摘要
从DHCP服务器服务中删除IPv6租约记录。

## 语法

### IP地址（默认值）
```
Remove-DhcpServerv6Lease [-ComputerName <String>] [-PassThru] -IPAddress <IPAddress[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 前缀
```
Remove-DhcpServerv6Lease [-ComputerName <String>] [-PassThru] [-Prefix] <IPAddress>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DhcpServerv6Lease` cmdlet 用于从动态主机配置协议（DHCP）服务器服务中删除一个或多个 IPv6 租约记录。如果指定了 `Prefix` 参数，该 cmdlet 将删除与该前缀相关的所有租约；如果指定了 `IPAddress` 参数，则会删除指定的租约。

## 示例

### 示例 1：删除某个范围内的所有租约
```
PS C:\> Remove-DhcpServerv6Lease -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020::
```

这个示例将从名为dhcpserver.contoso.com的计算机上运行的DHCP服务器服务中，删除所有属于范围2001:4898:7020:1020::内的IP地址租约。

### 示例 2：删除指定地址的租约
```
PS C:\> Remove-DhcpServerv6Lease -ComputerName "dhcpserver.contoso.com" -IPAddress 2001:4898:7020:1020::10,2001:4898:7020:1030::20
```

此示例将从名为 dhcpserver.contoso.com 的计算机上运行的 DHCP 服务器服务中删除 IP 地址租约，这些租约对应的地址分别是 2001:4898:7020:1020::10 和 2001:4898:7020:1030::20。

### 示例 3：使用管道删除某个范围内的租约
```
PS C:\> Get-DhcpServerv6Lease -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: | Remove-DhcpServerv6Lease -ComputerName "dhcpserver.contoso.com"
```

这个示例会删除所有属于范围 2001:4898:7020:1020:: 的 IPv6 地址租约。`Get-DhcpServerv6Lease` cmdlet 会返回这些 IP 地址租约对象，并将这些对象传递给当前的 cmdlet，从而删除每一个租约。

### 示例 4：删除某台计算机上所有作用域中的所有租约
```
PS C:\> Get-DhcpServerv6Scope -ComputerName "dhcpserver.contoso.com" | Remove-DhcpServerv6Lease -ComputerName "dhcpserver.contoso.com"
```

上述命令会从所有 DHCPv6 范围中删除所有的 IPv6 地址租约。`Get-DhcpServerv6Scope` cmdlet 用于获取 DHCPv6 范围对象，并将这些对象传递给该命令，从而删除通过管道传输的每个地址租约。

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

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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

### -IPAddress
指定一个或多个IPv6地址，这些地址的相关租约记录将从DHCP服务器服务中删除。

```yaml
Type: IPAddress[]
Parameter Sets: IPAddress
Aliases:

Required: True
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

### -Prefix
指定要从中删除租约的范围对应的 IPv6 子网前缀。

```yaml
Type: IPAddress
Parameter Sets: Prefix
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Lease
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Lease[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv6Lease](./Add-DhcpServerv6Lease.md)

[Get-DhcpServerv6Lease](./Get-DhcpServerv6Lease.md)

[Get-DhcpServerv6Scope](./Get-DhcpServerv6Scope.md)

