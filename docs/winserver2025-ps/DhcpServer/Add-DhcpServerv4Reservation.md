---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV4Reservation_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/add-dhcpserverv4reservation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DhcpServerv4Reservation
---

# Add-DhcpServerv4Reservation

## 摘要
为客户在指定的地址范围内预留一个IPv4地址。

## 语法

```
Add-DhcpServerv4Reservation [-ComputerName <String>] [-ScopeId] <IPAddress> [-IPAddress] <IPAddress>
 [-ClientId] <String> [-Name <String>] [-Description <String>] [-Type <String>] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DhcpServerv4 Reservation` 这个 cmdlet 会在指定的作用域内为某个客户端预留一个 IPv4 地址。一旦地址被预留，它将仅出租给通过特定客户端标识符（ID）识别的那个客户端使用。

## 示例

#### 示例 1：添加一个预留的 IP 地址
```
PS C:\> Add-DhcpServerv4Reservation -ScopeId 10.10.10.0 -IPAddress 10.10.10.8 -ClientId "F0-DE-F1-7A-00-5E" -Description "Reservation for Printer"
```

这个示例为通过指定的客户端ID识别的客户端添加了一个预留的IP地址。

### 示例 2：从文件中添加预订信息
```
PS C:\> Import-Csv -Path "Reservations.csv" | Add-DhcpServerv4Reservation -ComputerName "dhcpserver.contoso.com"
```

这个示例会将名为 `Reservations.csv` 的文件中的所有预留信息添加到运行在 `dhcpserver.contoso.com` 这台计算机上的 DHCP 服务器服务中。`Import-Csv` cmdlet 会返回包含预留信息的对象，并将这些对象传递给另一个 cmdlet，从而将这些预留信息添加到 DHCP 服务器服务中。`Reservations.csv` 文件应采用以下逗号分隔值（CSV）格式来存储预留信息：

ScopeId、IPAddress、Name、ClientId、Description

10.10.10.0, 10.10.10.10, Computer1, 1a-1b-1c-1d-1e-1f，保留给Computer1使用

20.20.20.0, 20.20.20.11, Computer2, 2a-2b-2c-2d-2e-2f，这些资源已预留给Computer2使用。

30.30.30.0, 30.30.30.12, Computer3, 3a-3b-3c-3d-3e-3f，保留给Computer3使用

### 示例 3：将租赁协议转换为预订协议
```
PS C:\> Get-DhcpServerv4Lease -ComputerName "dhcpserver.contoso.com" -IPAddress 10.10.10.11 | Add-DhcpServerv4Reservation -ComputerName "dhcpserver.contoso.com"
```

这个示例将其中一个租赁协议转换为预留资源。`Get-DhcpServerv4Lease` cmdlet 会返回 IP 地址租赁对象，并将该对象传递给另一个 cmdlet，后者会根据租赁对象中的 IP 地址和客户端 ID 创建相应的预留资源。

#### 示例 4：在某个范围内创建预订记录
```
PS C:\> $FreeIP = Get-DhcpServerv4FreeIPAddress -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0
PS C:\> Add-DhcpServerv4Reservation -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -IPAddress $FreeIP -ClientId "F0-DE-F1-7A-00-5E" -Description "Reservation for Printer"
```

这个示例为通过指定的客户端 ID 标识的客户，在地址范围 10.10.10.0 内的任意一个可用 IP 地址上创建一个预订。`Get-DhcpServerv4FreeIPAddress` cmdlet 用于获取该范围内的一个可用 IP 地址，然后使用该 cmdlet 为指定的客户端 ID 预订这个地址。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后继续显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。请输入一个计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
用于指定客户端的唯一标识符（ID）。对于Windows客户端，MAC地址被用作客户端ID。

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

### -ComputerName
指定目标计算机的DNS名称、IPv4地址或IPv6地址，该计算机运行动态主机配置协议（DHCP）服务器服务。

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
指定为创建的预订提供的描述信息。

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
指定要为客户端预留的 IPv4 地址。

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

### -Name
指定所创建的预留资源的名称。该参数值可以是客户端的主机名，也可以是在DHCP服务器服务中用于标识该预留资源的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: HostName, ReservationName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您当前正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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
指定创建预订的范围的标识符（ID）。

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
指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -Type
指定该IP地址所预留的客户端请求类型。此参数的可接受值为：DHCP、BootP或Both。默认值为Both。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ReservationType
Accepted values: Dhcp, Bootp, Both

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Lease
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Reservation
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Reservation
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DhcpServerv4FreeIPAddress](./Get-DhcpServerv4FreeIPAddress.md)

[Get-DhcpServerv4Lease](./Get-DhcpServerv4Lease.md)

[Get-DhcpServerv4Reservation](./Get-DhcpServerv4Reservation.md)

[Remove-DhcpServerv4Reservation](./Remove-DhcpServerv4Reservation.md)

[Set-DhcpServerv4Reservation](./Set-DhcpServerv4 Reservation.md)

