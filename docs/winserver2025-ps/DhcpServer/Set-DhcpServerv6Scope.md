---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV6Scope_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/set-dhcpserverv6scope?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DhcpServerv6Scope
---

# Set-DhcpServerv6Scope

## 摘要
修改DHCP服务器服务中IPv6作用域的属性。

## 语法

```
Set-DhcpServerv6Scope [-Prefix] <IPAddress> [-Name <String>] [-Description <String>] [-State <String>]
 [-Preference <UInt16>] [-PreferredLifeTime <TimeSpan>] [-ValidLifeTime <TimeSpan>] [-T1 <TimeSpan>]
 [-T2 <TimeSpan>] [-ComputerName <String>] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DhcpServerv6Scope` cmdlet 用于修改动态主机配置协议（DHCP）服务器服务中 IPv6 范围的属性。

## 示例

#### 示例 1：更改作用域（scope）的名称
```
PS C:\> Set-DhcpServerv6Scope -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -Name "Ext Lab Net VLAN100" -State "Active"
```

这个示例将指定的 DHCPv6 范围的名称更改为 “Ext Lab Net VLAN100”，并启用该范围。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行需要很长时间才能完成的命令。cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Description
指定要设置在该作用域上的描述信息。

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
指定要设置为该作用域的新名称。

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
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不生成任何输出。

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
指定DHCP服务器服务的优先级值。当DHCP客户端从多个DHCP服务器服务接收到响应时，会选择优先级最低的DHCP服务器服务进行连接。

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

### -PreferredLifeTime
该参数用于指定DHCP服务器服务租赁的IPv6地址的首选生命周期。其值应与*ValidLifeTime*参数的值相同或更短。

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
指定要修改属性的范围所对应的 IPv6 子网前缀。

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
指定作用域的状态。该参数的可接受值为：Active（激活）或Inactive（未激活）。

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
指定租约续期时间。DHCP客户端应使用单播消息，在此参数值指定的时间，从最初获取租约的同一DHCP服务器服务处重新续订租约。该参数值应小于相应作用域的*T2*和*PreferredLifetime*参数值。

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
指定租约重新绑定的时间。如果根据*T1*参数指定的时间尝试续租失败，客户端应使用多播消息从任意DHCP服务器服务处来续签租约（该时间等于此参数的值）。此参数值应大于*T1*参数的值，并且小于*PreferredLifetime*参数的值。

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
该参数用于指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不影响整个会话或计算机本身的运行状态。

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
该参数用于指定DHCP服务器服务租出的IPv6地址的有效生命周期。其值应与*PreferredLifetime*参数的值相同或大于后者。

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
展示了如果该cmdlet被运行会发生什么情况。但实际上该cmdlet并没有被运行。

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

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv6Scope](./Add-DhcpServerv6Scope.md)

[Get-DhcpServerv6Scope](./Get-DhcpServerv6Scope.md)

[Get-DhcpServerv6ScopeStatistics](./Get-DhcpServerv6ScopeStatistics.md)

[Remove-DhcpServerv6Scope](./Remove-DhcpServerv6Scope.md)

