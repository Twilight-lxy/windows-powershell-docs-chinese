---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV4Reservation_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv4reservation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv4Reservation
---

# 获取 DHCP Server v4 的预留信息

## 摘要
用于获取 IP 地址或客户端 ID 的 IPv4 预留地址。

## 语法

### ScopeId（默认值）
```
Get-DhcpServerv4Reservation [-ComputerName <String>] [-ScopeId] <IPAddress> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### IP地址
```
Get-DhcpServerv4Reservation [-ComputerName <String>] -IPAddress <IPAddress[]> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ClientId
```
Get-DhcpServerv4Reservation [-ComputerName <String>] [-ClientId] <String[]> [-ScopeId] <IPAddress>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DhcpServerv4 Reservation` 这个 cmdlet 可以获取一个或多个与指定 IP 地址或客户端标识符（ID）相关的 IPv4 预留地址。如果仅指定了 `ScopeId` 参数，那么将返回该范围内所有的 IPv4 预留地址。

## 示例

#### 示例 1：获取指定范围内的预订信息
```
PS C:\> Get-DhcpServerv4Reservation -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0
```

这个cmdlet用于获取在名为dhcpserver.contoso.com的计算机上运行的指定DHCP服务器服务中、位于指定范围内的所有预订信息。

### 示例 2：为指定的客户预订服务
```
PS C:\> Get-DhcpServerv4Reservation -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -ClientId "F0-DE-F1-7A-00-5E"
```

这个cmdlet用于获取指定范围内、属于指定客户端ID的预订信息。

### 示例 3：获取指定地址的预订信息
```
PS C:\> Get-DhcpServerv4Reservation -ComputerName "dhcpserver.contoso.com" -IPAddress 10.10.10.5
```

这个cmdlet用于获取指定IP地址的预留信息。

### 示例 4：获取所有范围内的所有预订信息
```
PS C:\> Get-DhcpServerv4Scope -ComputerName dhcpserver.contoso.com | Get-DhcpServerv4Reservation -ComputerName dhcpserver.contoso.com
```

这个 cmdlet 会从服务器 dhcpserver.contoso.com 上的所有作用域中获取所有预留的 IP 地址。**Get-DhcpServerv4Scope** cmdlet 会返回所有的作用域对象，并将这些对象传递给这个 cmdlet，后者则会从中提取出所有作用域中的预留地址信息。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行耗时较长的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlet；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个或多个需要检索的预订记录对应的客户端ID。对于Windows客户端来说，MAC地址即为该客户端的ID。

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
指定目标计算机的DNS名称或IPv4/IPv6地址，该计算机运行动态主机配置协议（DHCP）服务器服务。

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
指定一个或多个需要检索的预留IPv4地址。

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

### -ScopeId
指定用于检索预留资源的范围ID（采用IPv4地址格式）。

```yaml
Type: IPAddress
Parameter Sets: ScopeId, ClientId
Aliases: ReservationScopeID

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算一个最优的限流值（即并发操作的最大数量）。这个限流值仅适用于当前的 cmdlet，而不适用于整个会话或整个计算机。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4 Reservation
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Reservation[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv4Reservation](./Add-DhcpServerv4 Reservation.md)

[Get-DhcpServerv4Scope](./Get-DhcpServerv4Scope.md)

[Remove-DhcpServerv4Reservation](./Remove-DhcpServerv4 Reservation.md)

[Set-DhcpServerv4 Reservation](./Set-DhcpServerv4Reservation.md)

