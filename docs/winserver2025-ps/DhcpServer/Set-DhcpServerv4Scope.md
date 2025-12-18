---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV4Scope_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/set-dhcpserverv4scope?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DhcpServerv4Scope
---

# Set-DhcpServerv4Scope

## 摘要
用于在DHCP服务器服务上设置现有IPv4地址范围的属性。

## 语法

### WithoutRange（默认值）
```
Set-DhcpServerv4Scope [-ActivatePolicies <Boolean>] [-PassThru] [-Type <String>] [-ScopeId] <IPAddress>
 [-Description <String>] [-LeaseDuration <TimeSpan>] [-Name <String>] [-NapEnable <Boolean>]
 [-NapProfile <String>] [-Delay <UInt16>] [-State <String>] [-SuperscopeName <String>] [-ComputerName <String>]
 [-MaxBootpClients <UInt32>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### WithRange
```
Set-DhcpServerv4Scope [-ActivatePolicies <Boolean>] [-PassThru] [-Type <String>] [-ScopeId] <IPAddress>
 [-Description <String>] [-LeaseDuration <TimeSpan>] [-Name <String>] [-NapEnable <Boolean>]
 [-NapProfile <String>] [-Delay <UInt16>] [-State <String>] [-SuperscopeName <String>] [-ComputerName <String>]
 [-MaxBootpClients <UInt32>] -StartRange <IPAddress> -EndRange <IPAddress> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DhcpServerv4Scope` cmdlet 用于设置动态主机配置协议（DHCP）服务器服务中现有 IPv4 范围的属性。

## 示例

#### 示例 1：为某个作用域设置值
```
PS C:\> Set-DhcpServerv4Scope -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -Name "Ext Lab Net VLAN100" -State Active -LeaseDuration 4.00:00:00
```

这个示例将指定的 DHCPv4 范围的名称设置为 “Ext Lab Net VLAN100”，激活该范围，并将租约持续时间设置为 4 天。

## 参数

### -ActivatePolicies
指定在该范围内策略执行的启用状态。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数来执行需要较长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -Delay
指定 DHCP 服务器服务延迟向客户端发送响应的时间（以毫秒为单位）。该参数应用于分域配置中的备用 DHCP 服务器服务。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Description
指定要为该作用域设置的描述信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EndRange
指定要为该作用域设置的IPv4范围的结束地址。如果正在设置一个新的IPv4范围，则之前为此作用域设置的IPv4范围将被弃用。

```yaml
Type: IPAddress
Parameter Sets: WithRange
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LeaseDuration
指定为该范围内的客户端提供的IPv4地址租约的有效期限。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MaxBootpClients
指定允许从该范围获取 IP 地址租约的 Bootp 客户端的最大数量。仅当 *Type* 参数值为 “Both” 时，才能使用此参数。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定该作用域的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NapEnable
指定该范围内网络访问保护（NAP）功能的启用状态。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NapProfile
指定范围内客户端的 NAP 配置文件的名称。NAP 配置文件指的是“Microsoft 服务类别”（Microsoft Service Class），这是一种在网络策略服务器（NPS）上的网络策略中使用的条件。只有当 *NapEnable* 参数的值为 $True 时，才能使用此参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
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
指定属性所设置的范围内标识符（ID）的范围，该范围需采用 IPv4 地址格式表示。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StartRange
指定要为该范围设置的 IPv4 地址范围的起始地址。如果要设置一个新的 IP 范围，则会丢弃该范围之前已设置的 IP 范围。

```yaml
Type: IPAddress
Parameter Sets: WithRange
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -State
用于指定作用域的状态。该参数的可接受值为：Active（活动）和Inactive（非活动）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Active, InActive

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SuperscopeName
指定要将此作用域添加到的超作用域（superscope）的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
用于指定作用域的类型。该参数的可接受值为：DHCP、BootP 和 Both。作用域的类型决定了 DHCP 服务器服务是仅响应 DHCP 客户端请求，还是仅响应 BootP 客户端请求，或者同时响应这两种类型的客户端请求。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Dhcp, Bootp, Both

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径指定了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径指定了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv4Scope](./Add-DhcpServerv4Scope.md)

[Get-DhcpServerv4Scope](./Get-DhcpServerv4Scope.md)

[Get-DhcpServerv4ScopeStatistics](./Get-DhcpServerv4ScopeStatistics.md)

[Remove-DhcpServerv4Scope](./Remove-DhcpServerv4Scope.md)

