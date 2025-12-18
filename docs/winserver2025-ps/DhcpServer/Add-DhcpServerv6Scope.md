---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV6Scope_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/add-dhcpserverv6scope?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DhcpServerv6Scope
---

# Add-DhcpServerv6Scope

## 摘要
使用指定的参数为DHCP服务器服务添加一个IPv6作用域。

## 语法

```
Add-DhcpServerv6Scope [-ValidLifeTime <TimeSpan>] [-ComputerName <String>] [-Prefix] <IPAddress>
 [-Name] <String> [-Description <String>] [-State <String>] [-Preference <UInt16>]
 [-PreferredLifetime <TimeSpan>] [-T1 <TimeSpan>] [-T2 <TimeSpan>] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DhcpServerv6Scope` cmdlet 使用指定的参数，将一个 IPv6 范围添加到动态主机配置协议（DHCP）服务器服务中。

## 示例

#### 示例 1：在本地计算机上添加服务器作用域
```
PS C:\> Add-DhcpServerv6Scope -Prefix 2001:4898:7020:1020:: -Name "IPv6 Lab-4 Network"
```

上述命令会在本地计算机上运行的DHCP服务器中添加一个DHCPv6作用域，该作用域的子网前缀为2001:4898:7020:1020::，并且指定了相应的作用域名称。

### 示例 2：添加服务器范围（server scope）
```
PS C:\> Add-DhcpServerv6Scope -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -Name "IPv6 Lab-4 Network" -PreferredLifeTime 4.00:00:00 -ValidLifeTime 6.00:00:00 -State "Inactive"
```

这个示例向名为dhcpserver.contoso.com的计算机上运行的DHCP服务器服务添加了一个不活跃的DHCPv6作用域，该作用域的子网前缀为2001:4898:7020:1020::；同时指定了作用域名称，并将优先生存时间设置为4天，有效生存时间设置为6天。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行耗时较长的命令。cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Description
指定与该作用域相关联的描述信息。

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

### -Name
指定与该作用域相关联的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
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

### -Preference
指定DHCP服务器服务在响应该子网中的客户端时所使用的偏好字段的值。此参数的可接受取值为：0到255之间。默认值为0。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 0
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PreferredLifetime
指定 DHCP 服务器服务租用的 IPv6 地址的首选生命周期。默认值为 8 天。

这个参数的值应该等于或小于 *ValidLifeTime* 参数的值。

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

### -Prefix
指定要添加的范围的 IPv6 前缀。

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

### -State
用于指定作用域（scope）的状态。该参数的可接受值为：Enabled（启用）和Disabled（禁用）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Active, Inactive

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -T1
指定租约续期时间。默认值为 4 天。DHCP 客户端应使用单播消息，在该参数值指定的时间，从最初获取租约的同一 DHCP 服务器服务处续期租约。

这个参数的值应该小于*T2*和*PreferredLifetime*参数的值。

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

### -T2
指定租约重新绑定的时间。默认值为6.4天。如果由*T1*参数指定的续租尝试失败，DHCP客户端应使用多播消息从任意DHCP服务器服务处重新续签租约，此时使用的时间为该参数值所表示的时长。

这个参数的值应该大于*T1*参数的值，并且小于*PreferredLifetime*参数的值。

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

### -ThrottleLimit
该参数用于指定可以同时运行的命令（cmdlet）的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该命令的最佳限制值。此限制仅适用于当前执行的命令，而不影响整个会话或计算机本身。

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

### -ValidLifeTime
指定DHCP服务器服务租赁的IPv6地址的有效生命周期。默认值为12天。

这个参数值应该与*PreferredLifetime*参数值的大小相同或更大。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DhcpServerv6Scope](./Get-DhcpServerv6Scope.md)

[Get-DhcpServerv6ScopeStatistics](./Get-DhcpServerv6ScopeStatistics.md)

[Remove-DhcpServerv6Scope](./Remove-DhcpServerv6Scope.md)

[Set-DhcpServerv6Scope](./Set-DhcpServerv6Scope.md)

