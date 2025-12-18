---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV6OptionValue_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv6optionvalue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv6OptionValue
---

# Get-DhcpServerv6OptionValue

## 摘要
返回一个或多个IPv6选项的值，这些值可以针对特定的预留IP地址、作用域或服务器级别进行获取。

## 语法

```
Get-DhcpServerv6OptionValue [-ComputerName <String>] [-VendorClass <String>] [[-Prefix] <IPAddress>]
 [-ReservedIP <IPAddress>] [-UserClass <String>] [[-OptionId] <UInt32[]>] [-All] [-Brief]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DhcpServerv6OptionValue` cmdlet 可以返回一个或多个 IPv6 选项的值，这些选项可以针对特定的保留 IP 地址、作用域或服务器级别。选项标识符（ID）可以是标准选项，也可以是特定供应商类别的选项。如果您不指定 `OptionId` 参数，那么将返回所请求级别上的所有选项值（例如保留信息、作用域信息或服务器信息）。

如果您指定了 *ReservedIP* 参数，将会返回在预留级别设置的选项值。如果您指定了 *Prefix* 参数，将会返回在指定范围级别设置的选项值。如果您既没有指定 *Prefix* 参数，也没有指定 *ReservedIP* 参数，那么将会返回在服务器级别设置的选项值。

如果您既没有指定 *VendorClass* 参数，也没有指定 *UserClass* 参数，此 cmdlet 将返回标准的选项值。

## 示例

#### 示例 1：在服务器级别获取标准选项值
```
PS C:\> Get-DhcpServerv6OptionValue -ComputerName "dhcpserver.contoso.com"
```

这个例子获取了所有在服务器级别配置的标准 DHCPv6 选项值（这些选项值不属于任何特定类别）。

### 示例 2：获取某个作用域的标准选项值
```
PS C:\> Get-DhcpServerv6OptionValue -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020::
```

这个示例获取了为指定作用域配置的所有标准 DHCPv6 选项值（非类别特定的选项）。

### 示例 3：获取预订的标准选项值
```
PS C:\> Get-DhcpServerv6OptionValue -ComputerName "dhcpserver.contoso.com" -ReservedIP 2001:4898:7020:1020::5
```

这个示例获取了为指定预留配置的所有标准 DHCPv6 选项值（非类特定的选项）。

### 示例 4：获取特定于 verdor 类别的选项值（针对某个供应商类别）
```
PS C:\> Get-DhcpServerv6OptionValue -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -VendorClass "MSUCClient"
```

这个示例会获取指定供应商类别在指定作用域内配置的所有与该供应商类别相关的 DHCPv6 选项值。

### 示例 5：通过使用选项 ID 来获取某个范围内的选项值
```
PS C:\> Get-DhcpServerv6OptionValue -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -OptionId 23
```

这个示例用于为指定的选项标识符，在指定的作用域内配置 DHCPv6 选项的值。

### 示例 6：获取某个作用域内的所有选项值
```
PS C:\> Get-DhcpServerv6OptionValue -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -All
```

这个示例会获取指定作用域中配置的所有 DHCPv6 选项值。返回的 DHCPv6 选项值包括标准选项，以及供应商特定类别或用户特定类别的选项。

### 示例 7：简要获取某个作用域内的标准选项值
```
PS C:\> Get-DhcpServerv6OptionValue -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -Brief
```

这个示例会配置指定范围内所有标准的 DHCPv6 选项值。返回的对象不包含这些选项的名称。“Brief”参数通过避免从 DHCP 服务器服务中请求选项的名称，从而提高了该cmdlet的执行效率。

### 示例 8：获取用户类中特定于用户的选项值
```
PS C:\> Get-DhcpServerv6OptionValue -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -UserClass "LabComputer"
```

这个示例会获取为指定用户类在指定作用域内配置的所有与该用户类相关的 DHCPv6 选项值。

## 参数

### -All
表示此cmdlet用于获取某个范围（scope）、服务器或预订（reservation）的选项值。这些选项值可能包括与供应商类别（vendor class）或用户类别（user class）相关的特定设置。

如果仅指定了这个参数，那么此cmdlet将获取指定范围、预订或服务器的所有选项值。

如果您指定了 *OptionId* 参数，系统将返回所有供应商类别和用户类别中对应于该选项ID的所有选项值。

如果您指定了 *VendorClass* 参数，那么将返回该指定供应商类别的所有选项值，包括任何用户类别的选项值。

如果您指定了 *UserClass* 参数，那么将返回该用户类所有的选项值，包括任何特定于供应商的选项。

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

### -Brief
该参数指定选项的名称不会被包含在返回的选项值对象中。通过避免从动态主机配置协议（DHCP）服务器服务中获取选项名称，可以提升此cmdlet的性能。如果需要使用此cmdlet反复获取大量选项值，建议使用*Brief*参数。

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
在远程会话或远程计算机上运行该cmdlet。您可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定运行DHCP服务器服务的目标计算机的DNS名称，或IPv4地址，或IPv6地址。

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

### -OptionId
用于指定那些需要一个或多个值的选项的数值标识符。如果您不指定此参数，则会返回所有已配置的选项值。

```yaml
Type: UInt32[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Prefix
指定请求选项值的范围的 IPv6 子网前缀。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReservedIP
指定用于请求相应选项值的预留IPv6地址。

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
该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最优限制。这个限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或整个计算机。

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
指定返回指定用户类的选项值。

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

### -VendorClass
指定应返回所选供应商类别的相关选项值。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4OptionDefinition
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Policy
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Reservation
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6OptionValue[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Remove-DhcpServerv6OptionValue](./Remove-DhcpServerv6OptionValue.md)

[Set-DhcpServerv6OptionValue](./Set-DhcpServerv6OptionValue.md)

