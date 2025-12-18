---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV6Reservation_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv6reservation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv6Reservation
---

# Get-DhcpServerv6Reservation

## 摘要
返回DHCP服务器服务中预留的IPv6地址。

## 语法

### 前缀（默认值）
```
Get-DhcpServerv6Reservation [-ComputerName <String>] [-Prefix] <IPAddress> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### IP地址
```
Get-DhcpServerv6Reservation [-ComputerName <String>] -IPAddress <IPAddress[]> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DhcpServerv6Reservation` cmdlet 从动态主机配置协议（DHCP）服务器服务中返回预留的 IPv6 地址以及相关的客户端信息（DUID、IAID）。

## 示例

#### 示例 1：获取某个作用域内所有已预留的 IPv6 地址的信息
```
PS C:\> Get-DhcpServerv6Reservation -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020::
```

这个示例会获取指定 DHCPv6 范围内所有保留的 IPv6 地址的相关信息。

### 示例 2：获取已预留的 IPv6 地址的相关信息
```
PS C:\> Get-DhcpServerv6Reservation -ComputerName "dhcpserver.contoso.com" -IPAddress 2001:4898:7020:1020::5
```

这个示例用于获取在名为dhcpserver.contoso.com的计算机上运行的DHCP服务器服务中，关于某个指定保留IPv6地址的信息。

### 示例 3：获取所有范围内所有已预留的 IPv6 地址的信息
```
PS C:\> Get-DhcpServerv6Scope -ComputerName "dhcpserver.contoso.com" | Get-DhcpServerv6Reservation -ComputerName "dhcpserver.contoso.com"
```

这个示例从运行在名为dhcpserver.contoso.com的计算机上的DHCP服务器服务中，获取所有DHCPv6作用域内的预留IP地址。**Get-DhcpServerv6Scope** cmdlet会返回所有的作用域对象，并将这些对象传递给另一个cmdlet；该cmdlet会从每个通过管道传来的作用域中提取预留的IP地址。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

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
Aliases: Cn, ReservationServer

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPAddress
指定用于请求预留信息的 IPv6 地址。

```yaml
Type: IPAddress[]
Parameter Sets: IPAddress
Aliases: ReservedIP

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Prefix
指定用于请求预留地址的 DHCP 服务器服务的 IPv6 前缀。

```yaml
Type: IPAddress
Parameter Sets: Prefix
Aliases: ReservationScopeID

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值为`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。此限制仅适用于当前运行的cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6 Reservation
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6 Reservation[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv6 Reservation](./Add-DhcpServerv6Reservation.md)

[Get-DhcpServerv6Scope](./Get-DhcpServerv6Scope.md)

[Remove-DhcpServerv6Reservation](./Remove-DhcpServerv6Reservation.md)

[Set-DhcpServerv6Reservation](./Set-DhcpServerv6 Reservation.md)

