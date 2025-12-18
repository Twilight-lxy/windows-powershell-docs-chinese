---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV4Reservation_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/remove-dhcpserverv4reservation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DhcpServerv4Reservation
---

# 删除 DHCP Server v4 的预留资源

## 摘要
从指定的范围内删除该IPv4预留地址。

## 语法

### IP地址（默认值）
```
Remove-DhcpServerv4Reservation [-ComputerName <String>] [-PassThru] -IPAddress <IPAddress[]>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ScopeId
```
Remove-DhcpServerv4Reservation [-ScopeId] <IPAddress> [-ComputerName <String>] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ClientId
```
Remove-DhcpServerv4Reservation [-ScopeId] <IPAddress> [-ClientId] <String[]> [-ComputerName <String>]
 [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
**Remove-DhcpServerv4Reservation** cmdlet 用于从指定的范围中删除 IPv4 预留地址。如果指定了 *ScopeId* 参数，那么该范围内的所有预留地址都将被删除；如果指定了 *IPAddress* 或 *ClientId* 参数，则会删除一个或多个由 IP 地址或客户端标识符（ID）所标识的特定预留地址。

## 示例

### 示例 1：删除某个范围内的所有预订记录
```
PS C:\> Remove-DhcpServerv4Reservation -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0
```

这个示例会删除指定范围内所有的预订记录。

### 示例 2：删除指定的预订记录
```
PS C:\> Remove-DhcpServerv4Reservation -ComputerName "dhcpserver.contoso.com" -IPAddress 10.10.10.5, 10.10.10.6
```

这个示例会从DHCP服务器服务中删除指定的预订信息。

### 示例 3：删除指定客户的预订记录
```
PS C:\> Remove-DhcpServerv4Reservation -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -ClientId "F0-DE-F1-7A-00-5E"
```

这个示例会从DHCP服务器服务中删除由客户端ID标识的指定预订信息。对于运行Windows操作系统的计算机，MAC地址被用作客户端标识符。

### 示例 4：从所有作用域中删除预留的 IP 地址
```
PS C:\> Get-DhcpServerv4Scope -ComputerName "dhcpserver.contoso.com" | Remove-DhcpServerv4Reservation -ComputerName "dhcpserver.contoso.com"
```

这个示例会从名为dhcpserver.contoso.com的计算机上运行的DHCP服务器服务中的所有作用域中删除所有预分配的IP地址。`Get-DhcpServerv4Scope` cmdlet会返回所有的作用域对象，并将这些对象传递给当前的cmdlet，该cmdlet会删除通过管道传入的每个作用域中的预分配IP地址。

## 参数

### -AsJob
以后台作业的形式运行该 cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后继续显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `-*Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
指定一个或多个要删除的预订对应的客户端ID。对于Windows客户端，MAC地址被用作客户端标识符。

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
指定目标计算机的DNS名称，或者其IPv4或IPv6地址。该目标计算机正在运行动态主机配置协议（DHCP）服务器服务。

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
在运行cmdlet之前会提示您进行确认。

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
为一个或多个将被删除的预订指定一个或多个IPv4地址。

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
指定保留删除的起始范围ID（以IPv4地址格式表示）。

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
该参数用于指定可以同时运行的命令（cmdlet）的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该 cmdlet 的最优限制值。此限制仅适用于当前运行的命令本身，而不涉及会话或整个计算机。

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
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Reservation
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于展示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于展示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Reservation[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于展示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv4Reservation](./Add-DhcpServerv4Reservation.md)

[Get-DhcpServerv4Reservation](./Get-DhcpServerv4Reservation.md)

[Get-DhcpServerv4Scope](./Get-DhcpServerv4Scope.md)

[Set-DhcpServerv4 Reservation](./Set-DhcpServerv4Reservation.md)

