---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV6Reservation_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/add-dhcpserverv6reservation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DhcpServerv6Reservation
---

# Add-DhcpServerv6Reservation

## 摘要
将一个 IPv6 预留地址添加到某个 IPv6 前缀或作用域中。

## 语法

```
Add-DhcpServerv6Reservation [-ComputerName <String>] [-IPAddress] <IPAddress> [-ClientDuid] <String>
 [-Iaid] <UInt32> [[-Name] <String>] [-Description <String>] [-Prefix] <IPAddress> [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DhcpServerv6Reservation` cmdlet 为通过指定的动态主机配置协议（DHCP）v6唯一标识符（DUID）和身份关联标识符（IAID）识别的客户端预留一个指定的 IPv6 地址。

## 示例

### 示例 1：预留一个 IP 地址
```
PS C:\> Add-DhcpServerv6Reservation -Prefix 2001:4898:7020:1020:: -IPAddress 2001:4898:7020:1020::1 -ClientDuid "00-01-00-01-15-F9-7F-AB-F0-DE-F1-7A-00-5E" -Iaid 234890455
```

此示例为指定的 *ClientDuid* 和 *Iaid* 参数值预留了相应的 IPv6 地址。在完成地址预留后，DHCP 服务器服务只会将预留给这些参数值的 IP 地址分配给那些包含相应参数值的客户端请求。

### 示例 2：从文件中预分配 IP 地址
```
PS C:\> Import-Csv -Path "Reservations.csv" | Add-DhcpServerv6Reservation -ComputerName "dhcpserver.contoso.com"
```

这个示例将名为 `Reservations.csv` 的文件中的所有预留信息添加到运行在 `dhcpserver.contoso.com` 这台计算机上的 DHCP 服务器服务中。`Import-Csv` cmdlet 会检索包含预留信息的对象，并将这些对象传递给另一个 cmdlet，从而将这些预留信息添加到 DHCP 服务器服务中。`Reservations.csv` 文件应该以逗号分隔值（CSV）格式存储预留信息，具体内容如下：

前缀、IP地址、名称、客户端唯一标识符（ClientDuid）、内部唯一标识符（Iaid）以及描述：  
2001:4898:7020:1020::, 2001:4898:7020:1020::1, Computer1, 00-01-00-01-15-F9-7F-AB-F0-DE-F1-7A-00-5E, 234890455（预留给Computer1）  
2001:4898:7020:1020::, 2001:4898:7020:1020::2, Computer2, 00-01-00-01-15-F9-7F-AB-F0-DE-F1-7A-00-6E, 234890465（预留给Computer2）  
2001:4898:7020:1020::, 2001:4898:7020:1020::3, Computer3, 00-01-00-01-15-F9-7F-AB-F0-DE-F1-7A-00-7E, 234890475（预留给Computer3）

### 示例 3：在某个范围内预留任意 IP 地址
```
PS C:\> $FreeIP = Get-DhcpServerv6FreeIPAddress -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020::
PS C:\> Add-DhcpServerv6Reservation -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020::  -IPAddress $FreeIP -ClientDuid "00-01-00-01-15-F9-7F-AB-F0-DE-F1-7A-00-5E" -Iaid 234890455 -Description "Reservation for Printer"
```

这个示例为指定客户端ID对应的客户创建一个预订请求，使用的是来自范围2001:4898:7020:1020::内的任意一个空闲IP地址。`Get-DhcpServerv6FreeIPAddress` cmdlet会从该范围内获取一个空闲的IP地址，然后使用这个cmdlet将所获取的IP地址预订给指定的客户端ID。

### 示例 4：将租约转换为预订（reservation）
```
PS C:\> Get-DhcpServerv6Lease -ComputerName "dhcpserver.contoso.com" -IPAddress 2001:4898:7020:1020::11 | Add-DhcpServerv6Reservation -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020::
```

这个示例将其中一个租约转换为预订（reservation）。`Get-DhcpServerv6Lease` cmdlet 返回一个 IP 地址租约对象，并将该对象传递给另一个 cmdlet，后者会根据该租约对象中的 IP 地址、客户端 DUID 和 IAID 创建相应的预订。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -ClientDuid
指定客户的DUID（设备唯一标识符）。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Duid

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定运行 DHCP 服务器服务的目标计算机的 DNS 名称、IPv4 地址或 IPv6 地址。

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

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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

### -Description
指定为创建的 IPv6 预留地址所设置的描述字符串。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ReservationDescription

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IPAddress
指定要为客户端预留的 IPv6 地址。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases: ReservedIP

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Iaid
指定客户端特定网络接口的 DHCPv6 IAID（Identity Association Identifier）。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: True
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定客户端的名称。此参数值可以是客户端的实际主机名，也可以是一个用于在DHCP服务器服务中标识该预留客户端的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: HostName, ReservationName

Required: False
Position: 5
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不生成任何输出。

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
指定用于标识创建预留范围的IPv6前缀。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases: ReservationScopeID

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行的命令操作（cmdlet）的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令操作的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不影响整个会话或计算机本身。

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

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Reservation
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Reservation
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DhcpServerv6FreeIPAddress](./Get-DhcpServerv6FreeIPAddress.md)

[Get-DhcpServerv6Lease](./Get-DhcpServerv6Lease.md)

[Get-DhcpServerv6Reservation](./Get-DhcpServerv6 Reservation.md)

[Remove-DhcpServerv6Reservation](./Remove-DhcpServerv6Reservation.md)

[Set-DhcpServerv6Reservation](./Set-DhcpServerv6 Reservation.md)

