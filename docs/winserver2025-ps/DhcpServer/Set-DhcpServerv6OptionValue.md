---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV6OptionValue_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/set-dhcpserverv6optionvalue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DhcpServerv6OptionValue
---

# Set-DhcpServerv6OptionValue

## 摘要
在服务器、作用域或预留级别设置一个 IPv6 选项值。

## 语法

### OptionIds（默认值）
```
Set-DhcpServerv6OptionValue [-PassThru] [-Force] [[-Prefix] <IPAddress>] [-UserClass <String>]
 [-ComputerName <String>] [-ReservedIP <IPAddress>] [-Value] <String[]> [-OptionId] <UInt32>
 [-VendorClass <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### CommonOptions
```
Set-DhcpServerv6OptionValue [-PassThru] [-Force] [[-Prefix] <IPAddress>] [-UserClass <String>]
 [-DnsServer <IPAddress[]>] [-DomainSearchList <String[]>] [-InfoRefreshTime <UInt32>] [-ComputerName <String>]
 [-ReservedIP <IPAddress>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-DhcpServerv6OptionValue` cmdlet 可用于在服务器、作用域或保留池级别设置 IPv6 选项的值。该选项的定义必须已存在于动态主机配置协议 (DHCP) 服务器服务中。如果您指定了 `ReservedIP` 参数，选项值将在保留池级别被设置；如果您仅指定了 `Prefix` 参数，选项值将在作用域级别被设置；如果您既没有指定 `Prefix` 参数也没有指定 `ReservedIP` 参数，选项值将在服务器级别被设置。需要注意的是，`Prefix` 和 `ReservedIP` 参数不能同时被使用。

如果您指定了 *VendorClass* 参数，此 cmdlet 会设置指定供应商类的选项值。如果您指定了 *UserClass* 参数，此 cmdlet 会设置指定用户类的选项值。

## 示例

### 示例 1：设置服务器级别的选项值
```
PS C:\> Set-DhcpServerv6OptionValue -ComputerName "dhcpserver.contoso.com" -DnsServer 2001:4898:7020:1020::2 -DomainSearchList "contoso.com"
```

这个示例设置了 DHCPv6 服务器级别的选项值，包括 DNS 服务器相关选项和域名搜索列表相关的选项。

### 示例 2：为某个范围设置选项值
```
PS C:\> Set-DhcpServerv6OptionValue -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -DnsServer 2001:4898:7020:1020::2 -DomainSearchList "contoso.com"
```

这个示例为作用域 2001:4898:7020:1020:: 设置了 DHCPv6 选项值，包括 DNS 服务器的相关选项以及域名搜索列表的选项。

### 示例 3：为 DNS 服务器设置全局服务级别的选项值
```
PS C:\> Set-DhcpServerv6OptionValue -ComputerName "dhcpserver.contoso.com" -OptionId 23 -Value "2001:4898:7020:1020::2"
```

这个示例为服务器范围内的所有设备设置了DHCPv6选项23（即DNS服务器相关选项）的默认值。

### 示例 4：为某个作用域设置 DNS 服务器的选项值
```
PS C:\> Set-DhcpServerv6OptionValue -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -OptionId 23 -Value "2001:4898:7020:1020::2"
```

这个例子为指定的 DHCPv6 范围设置了选项 ID 23（即 DNS 服务器）对应的 DHCPv6 选项值。

### 示例 5：为预订设置 DNS 服务器的选项值
```
PS C:\> Set-DhcpServerv6OptionValue -ComputerName "dhcpserver.contoso.com" -ReservedIP 2001:4898:7020:1020::5 -OptionId 23 -Value "2001:4898:7020:1020::2"
```

这个示例为指定的预留资源设置了 DHCPv6 选项的值，该选项的 ID 为 23（即 DNS 服务器相关设置）。

### 示例 6：为特定供应商类设置一个选项值
```
PS C:\> Set-DhcpServerv6OptionValue -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -VendorClass "MSUCClient" -OptionId 5 -Value "6874747073"
```

此示例为名为 MSUCClient 的指定供应商类，在指定的作用域内设置了该供应商类特定的 DHCPv6 选项值。

### 示例 7：为 DNS 服务器设置用户类特定的选项值
```
PS C:\> Set-DhcpServerv6OptionValue -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -UserClass "LabComputer" -OptionId 23 -Value "2001:4898:7020:1020::20"
```

这个示例为指定用户类在指定范围内设置了DHCPv6选项ID 23（即DNS服务器）的特定值。

## 参数

### -AsJob
将该cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job` cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。您可以输入一台计算机的名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定运行 DHCP 服务器服务的目标计算机的 DNS 名称或 IPv4 或 IPv6 地址。

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

### -DnsServer
为DNS服务器选项指定一个或多个值。

```yaml
Type: IPAddress[]
Parameter Sets: CommonOptions
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DomainSearchList
为“域名搜索列表”选项指定一个或多个值。

```yaml
Type: String[]
Parameter Sets: CommonOptions
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Force
指定跳过DNS服务器验证步骤。此参数仅在使用*DNSServer*参数或选项ID 23时才有效。

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

### -InfoRefreshTime
用于指定信息刷新选项的值。该参数值定义了客户端在从 DHCPv6 服务器获取信息后等待的最长时间上限。此参数仅适用于无状态（stateless）DHCPv6 场景，因为在无地址或其他具有生命周期的实体可供参考的情况下，客户端无法自行判断何时需要与 DHCPv6 服务器联系以更新其配置。

```yaml
Type: UInt32
Parameter Sets: CommonOptions
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -OptionId
指定已设置值的选项的数值标识符（ID）。

```yaml
Type: UInt32
Parameter Sets: OptionIds
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个对象，该对象表示您正在操作的项。默认情况下，此cmdlet不会生成任何输出。

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
指定该选项值所设置的范围的 IPv6 子网前缀。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReservedIP
指定设置了该选项值的预留资源的IPv6地址。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases: IPAddress

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值为`0`，那么Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算出一个最佳的限速值。这个限速值仅适用于当前执行的cmdlet，而不影响整个会话或计算机本身。

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

### -UserClass
为指定的用户类别指定相应的选项值。

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

### -Value
指定要为该选项设置的值。

```yaml
Type: String[]
Parameter Sets: OptionIds
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -VendorClass
指定所选供应商类别对应的选项值。

```yaml
Type: String
Parameter Sets: OptionIds
Aliases:

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6OptionDefinition
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6OptionValue
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6 Reservation
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6OptionValue
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DhcpServerv6OptionValue](./Get-DhcpServerv6OptionValue.md)

[Remove-DhcpServerv6OptionValue](./Remove-DhcpServerv6OptionValue.md)

