---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4Lease_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/remove-dhcpserverv4lease?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DhcpServerv4Lease
---

# 移除 DHCP Server v4 的租约

## 摘要
从DHCP服务器服务中删除IPv4地址租用记录。

## 语法

### IP地址（默认值）
```
Remove-DhcpServerv4Lease [-PassThru] [-ComputerName <String>] -IPAddress <IPAddress[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ScopeId
```
Remove-DhcpServerv4Lease [-PassThru] [-ComputerName <String>] [-ScopeId] <IPAddress>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ClientId
```
Remove-DhcpServerv4Lease [-PassThru] [-ComputerName <String>] [-ScopeId] <IPAddress> [-ClientId] <String[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### BadLeases
```
Remove-DhcpServerv4Lease [-PassThru] [-ComputerName <String>] [-BadLeases] [[-ScopeId] <IPAddress>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DhcpServerv4Lease` cmdlet 用于从动态主机配置协议（DHCP）服务器服务中删除一个或多个 IPv4 租约记录。

如果您指定了 *ScopeId* 参数，那么指定范围内的所有租约都将被删除。

如果您指定了 *IPAddress* 参数，那么系统会删除由一个或多个指定 IP 地址标识的客户端对应的租约。如果您同时指定了 *ClientId* 和 *ScopeId* 参数，那么系统会删除来自指定范围的、对应于该指定客户端标识符（ID）的租约。

如果您指定了 *BadLeases* 和 *ScopeId* 参数，此cmdlet将删除指定范围内所有不良租赁记录。

如果你指定了 *BadLeases* 参数但没有指定 *ScopeId* 参数，此cmdlet将从DHCP服务器服务中的所有作用域中删除所有的不良租约。

## 示例

### 示例 1：删除某个范围内的租约
```
PS C:\> Remove-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0
```

这个示例会从名为dhcpserver.contoso.com的计算机上运行的DHCP服务器服务中，删除所有属于10.10.10.0范围内的IPv4地址租约。

### 示例 2：删除多个地址的租赁信息
```
PS C:\> Remove-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com" -IPAddress 10.10.10.10,20.20.20.20
```

这个示例会从名为dhcpserver.contoso.com的计算机上运行的DHCP服务器服务中，删除与IP地址10.10.10.10和10.20.20.20相关的租约信息。

### 示例 3：删除指定客户的租赁记录
```
PS C:\> Remove-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -ClientId "F0-DE-F1-7A-00-5E","00-24-D7-C5-25-B0"
```

此示例会从 DHCPv4 范围 10.10.10.0 中删除由客户端 ID F0-DE-F1-7A-00-5E 和 00-24-D7-C5-25-B0 标识的客户的 IPv4 地址租约。

### 示例 4：删除指定范围内的已拒绝租约
```
PS C:\> Remove-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -BadLeases
```

这个示例会从运行在名为dhcpserver.contoso.com的计算机上的DHCP服务器服务中，删除所有属于10.10.10.0范围内的无效（或被拒绝的）IPv4地址租约。

### 示例 5：使用管道删除已被拒绝的租赁协议
```
PS C:\> Get-DhcpServerv4Scope -ComputerName "dhcpserver.contoso.com" | Get-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com" -BadLeases | Remove-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com" -BadLeases
```

这个示例会从运行在名为 dhcpserver.contoso.com 的计算机上的 DHCP 服务器服务中的所有作用域中，删除所有无效或被拒绝的 IPv4 地址租约。**Get-DhcpServerv4Scope** cmdlet 会返回所有的作用域对象，这些对象随后会被传递给 **Get-DhcpServerv4Lease** cmdlet。**Get-DhcpServerv4Lease** cmdlet 会从所有作用域中筛选出无效的地址租约信息，并将这些信息传递给另一个 cmdlet，最终该 cmdlet 会删除所有无效的地址租约。

#### 示例 6：使用管道删除指定范围内的租约
```
PS C:\> Get-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -AllLeases | Remove-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com"
```

这个示例会删除所有属于范围 10.10.10.0 的 IPv4 地址租约。该命令通过管道机制实现：首先使用 `Get-DhcpServerv4Lease` cmdlet 获取 IPv4 地址租约对象，然后将这些对象传递给另一个 cmdlet，后者会删除其中无效的租约。

### 示例 7：删除计算机上所有作用域中的所有租约
```
PS C:\> Get-DhcpServerv4Scope -ComputerName "dhcpserver.contoso.com" | Remove-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com"
```

这个示例会从运行在名为dhcpserver.contoso.com的计算机上的DHCP服务器服务中的所有DHCPv4作用域中删除所有的IPv4地址租约。**Get-DhcpServerv4Scope** cmdlet用于返回DHCPv4作用域对象，这些对象随后会被传递给另一个cmdlet，该cmdlet会逐一删除所有的地址租约。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -BadLeases
指定删除所有无效的 IP 地址租约。如果客户端因 IP 地址冲突而拒绝某个 IPv4 地址租约，DHCP 服务器服务会将该租约标记为无效状态。

```yaml
Type: SwitchParameter
Parameter Sets: BadLeases
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
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

### -ClientId
指定要删除其IPv4地址租约的客户端ID。Windows客户端使用MAC地址作为客户端ID。

```yaml
Type: String[]
Parameter Sets: ClientId
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
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

### -IPAddress
指定一个或多个要删除租约记录的 IP 地址。

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

### -ScopeId
指定用于删除 IP 地址租约的范围 ID，该 ID 采用 IPv4 地址格式表示。

```yaml
Type: IPAddress
Parameter Sets: ScopeId, ClientId
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

```yaml
Type: IPAddress
Parameter Sets: BadLeases
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Lease
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Reservation
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Lease[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv4Lease](./Add-DhcpServerv4Lease.md)

[Get-DhcpServerv4Lease](./Get-DhcpServerv4Lease.md)

[Get-DhcpServerv4Scope](./Get-DhcpServerv4Scope.md)

