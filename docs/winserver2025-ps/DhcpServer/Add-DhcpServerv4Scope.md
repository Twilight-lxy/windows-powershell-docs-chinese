---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV4Scope_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/add-dhcpserverv4scope?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DhcpServerv4Scope
---

# Add-DhcpServerv4Scope

## 摘要
在DHCP服务器服务上添加一个IPv4地址范围。

## 语法

```
Add-DhcpServerv4Scope [-ComputerName <String>] [-StartRange] <IPAddress> [-EndRange] <IPAddress>
 [-Name] <String> [-Description <String>] [-State <String>] [-SuperscopeName <String>]
 [-MaxBootpClients <UInt32>] [-ActivatePolicies <Boolean>] [-PassThru] [-NapEnable] [-NapProfile <String>]
 [-Delay <UInt16>] [-LeaseDuration <TimeSpan>] [-SubnetMask] <IPAddress> [-Type <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DhcpServerv4Scope` cmdlet 用于在动态主机配置协议（DHCP）服务器服务上添加一个 IPv4 范围，并设置指定的参数。

## 示例

### 示例 1：为子网添加一个新的作用域
```
PS C:\> Add-DhcpServerv4Scope -Name "Lab-4 Network" -StartRange 10.10.10.1 -EndRange 10.10.10.254 -SubnetMask 255.255.255.0
```

这个示例为本地计算机上运行的DHCP服务器服务添加了一个新的作用域（scope），该作用域适用于子网10.10.10.0/24。

### 示例 2：为支持 NAP（Network Access Protection）功能的子网添加一个新的作用域
```
PS C:\> Add-DhcpServerv4Scope -ComputerName dhcpserver.contoso.com -Name "Lab-5 Network" -StartRange 10.20.20.1 -EndRange 10.20.20.254 -SubnetMask 255.255.255.0 -State InActive -NapEnable
```

这个示例将指定的非活动作用域添加到DHCP服务器服务中，该作用域适用于20.20.20.0/24子网，并且已为NAP（网络访问保护）功能启用。

### 示例 3：为子网添加一个新的作用域（scope），作为超作用域（superscope）的一部分
```
PS C:\> Add-DhcpServerv4Scope -Name "Lab-6 Network" -StartRange 10.30.30.1 -EndRange 10.30.30.254 -SubnetMask 255.255.255.0 -SuperScope "Expanded Lab-6 Network"
```

这个示例为本地计算机上运行的DHCP服务器服务添加了一个新的作用域（scope），该作用域适用于10.30.30.0/24子网。这个新作用域是被添加到名为“Expanded Lab-6 Network”的超级作用域（superscope）中的。

## 参数

### -ActivatePolicies
指定在所添加的作用域上策略执行的启用状态。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: True
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定运行DHCP服务器服务的目标计算机的DNS名称，或IPv4地址或IPv6地址。

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

### -Delay
指定DHCP服务器服务在响应客户端请求之前应等待的毫秒数。如果该作用域属于分片部署的一部分，并且此DHCP服务器服务需要作为所添加作用域的辅助DHCP服务器服务来使用，请设置此参数。

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

### -Description
用于指定所添加的 IPv4 范围的描述字符串。

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
指定子网中该IP地址范围的结束IP地址，DHCP服务器服务将从该子网中租用IP地址。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LeaseDuration
指定在此范围内应将 IP 地址租给客户端的时间间隔。时间间隔应采用 `day.hrs:mins:secs` 的格式进行表示。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: 8.00:00:00
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MaxBootpClients
如果范围类型被设置为“Both”（即同时允许DHCP客户端和BootP客户端使用该范围），则该条款指定了从这个范围内分配IP地址给BootP客户端的最大数量。

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
指定要添加的 IPv4 范围的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NapEnable
指定此范围内网络访问保护（Network Access Protection，简称NAP）的启用状态。如果启用了NAP，DHCP服务器服务会将从客户端接收到的健康状况报告（Statement of Health，简称SoH）传递给网络策略服务器（Network Policy Server，简称NPS）。根据所设置的NAP配置文件，NPS会决定是否允许该客户端访问网络。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NapProfile
指定只有在范围内启用了NAP（网络访问保护）时，才应设置NAP配置文件。这里的NAP配置文件指的是MS服务类别（MS Service Class），这是NPS（Network Policy Server）中的网络策略所使用的一个条件。

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
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -StartRange
指定子网中该地址范围的起始IP地址，DHCP服务器服务将从该地址范围中租赁IP地址给客户端。

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
指定作用域创建时的状态。该参数的可接受值为：Active（激活）和Inactive（非激活）。只有处于激活状态的作用域才会响应客户端请求。默认值为Active。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Active, InActive

Required: False
Position: Named
Default value: Active
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SubnetMask
指定以 IP 地址格式表示的范围所对应的子网掩码。例如：`255.255.255.0`。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SuperscopeName
指定要将该范围添加到的超范围的名称。

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
该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机。

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
指定该作用域所要服务的客户端类型。此参数的可接受值为：DHCP、BootP 或 Both。作用域的类型决定了 DHCP 服务器服务是仅响应 DHCP 客户端的请求，还是仅响应 BootP 客户端的请求，或者同时响应这两种类型的客户端的请求。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Dhcp, Bootp, Both

Required: False
Position: Named
Default value: DHCP
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径指定了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径指定了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DhcpServerv4Scope](./Get-DhcpServerv4Scope.md)

[Get-DhcpServerv4ScopeStatistics](./Get-DhcpServerv4ScopeStatistics.md)

[Remove-DhcpServerv4Scope](./Remove-DhcpServerv4Scope.md)

[Set-DhcpServerv4Scope](./Set-DhcpServerv4Scope.md)

