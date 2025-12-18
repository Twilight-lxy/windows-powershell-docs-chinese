---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4Lease_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv4lease?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv4Lease
---

# Get-DhcpServerv4Lease

## 摘要
从DHCP服务器服务中获取一个或多个租约记录。

## 语法

### ScopeId（默认值）
```
Get-DhcpServerv4Lease [-ComputerName <String>] [-ScopeId] <IPAddress> [-AllLeases] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### IP地址
```
Get-DhcpServerv4Lease [-ComputerName <String>] -IPAddress <IPAddress[]> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ClientId
```
Get-DhcpServerv4Lease [-ComputerName <String>] [-ScopeId] <IPAddress> [-ClientId] <String[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### BadLeases
```
Get-DhcpServerv4Lease [-ComputerName <String>] [-BadLeases] [[-ScopeId] <IPAddress>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DhcpServerv4Lease` cmdlet 从动态主机配置协议（DHCP）服务器服务中获取一个或多个租约记录。

如果您指定了 *ScopeId* 参数，系统将返回来自指定范围内的有效租赁信息。如果要获取包括“有效”（Active）、“已提供”（Offered）、“已被拒绝”（Declined）和“已过期”（Expired）在内的所有类型的租赁信息，则必须指定 *AllLeases* 参数。

如果您指定了 *IPAddress* 参数，系统将返回与该指定 IP 地址相关的租约记录。

如果您指定了 *ClientId* 和 *ScopeId* 参数，系统将返回在指定范围内、与指定的 *ClientId* 值对应的租约信息。

如果您指定了 *BadLeases* 和 *ScopeId* 参数，系统将返回指定范围内所有不良租赁记录。

如果您指定了 *BadLeases* 参数但没有指定 *ScopeId* 参数，那么将从 DHCP 服务器服务中返回所有不良的租约记录。

## 示例

### 示例 1：获取某个范围内的所有有效租约
```powershell
PS C:\> Get-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0
```

这个示例从 DHCPv4 范围 10.10.10.0 中获取所有有效的 IPv4 地址租约。

### 示例 2：获取指定地址的租赁信息
```powershell
PS C:\> Get-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com" -IPAddress 10.10.10.10,10.20.20.20
```

这个示例用于获取IPv4地址10.10.10.10和10.20.20.20的IP地址租用信息。

### 示例 3：租约申请被拒绝的情况
```powershell
PS C:\> Get-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -BadLeases
```

这个示例从 DHCPv4 范围 10.10.10.0 中获取所有无效或被拒绝的 IPv4 地址租约。

### 示例 4：获取指定客户的租约信息
```powershell
PS C:\> Get-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -ClientId "F0-DE-F1-7A-00-5E", "00-24-D7-C5-25-B0"
```

这个示例从 DHCPv4 范围 10.10.10.0 中获取 IPv4 地址租约，这些地址是分配给客户端 ID 为 F0-DE-F1-7A-00-5E 和 00-24-D7-C5-25-B0 的客户端的。

### 示例 5：获取某个范围内的所有租约
```powershell
PS C:\> Get-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -AllLeases
```

这个示例从 DHCPv4 范围 10.10.10.0 中获取了所有类型的 IPv4 地址租约，包括“活动”（Active）、“拒绝”（Declined）和“过期”（Expired）状态的租约。

### 示例 6：从计算机上的所有作用域中获取活动的租约
```powershell
PS C:\> Get-DhcpServerv4Scope -ComputerName "dhcpserver.contoso.com" | Get-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com"
```

这个示例从名为dhcpserver.contoso.com的计算机上运行的DHCP服务器服务中获取所有作用域内的活动IP地址租约信息。`Get-DhcpServerv4Scope` cmdlet会返回相应的作用域对象，并将这些对象传递给另一个cmdlet，后者再从中提取出所有作用域内的活动地址租约信息。

## 参数

### -AllLeases
表示该cmdlet会返回所有IPv4地址租约，而不论地址的状态如何。默认情况下，该cmdlet仅返回处于活动状态的租约。

```yaml
Type: SwitchParameter
Parameter Sets: ScopeId
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成过程中，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
表示此cmdlet仅返回无效的IP地址租约信息。当某个IP地址租约因与其他客户端发生冲突而被客户端拒绝，或者该租约记录被DHCP服务器服务标记为无效/已被拒绝时，系统会相应地处理这些情况。

在这种状态下，IP地址租赁在计时器到期（时间为10分钟）之前不会提供给任何客户端。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如 `[New-CimSession](/powershell/module/cimcmdlets/new-cimsession)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
指定要获取其IP地址租用记录的客户端标识符（ID）。

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

### -IPAddress
指定用于检索租约记录的 IP 地址。

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

### -ScopeId
指定用于获取IPv4地址租约的范围ID，该范围ID采用IPv4地址格式表示。

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
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Lease[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv4Lease](./Add-DhcpServerv4Lease.md)

[Get-DhcpServerv4Scope](./Get-DhcpServerv4Scope.md)

[Remove-DhcpServerv4Lease](./Remove-DhcpServerv4Lease.md)
