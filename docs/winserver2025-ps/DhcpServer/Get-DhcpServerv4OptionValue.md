---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV4OptionValue_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv4optionvalue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv4OptionValue
---

# Get-DhcpServerv4OptionValue

## 摘要
返回服务器、作用域或保留级别上的 IPv4 选项对应的 IPv4 选项值。

## 语法

```
Get-DhcpServerv4OptionValue [-VendorClass <String>] [-ComputerName <String>] [[-ScopeId] <IPAddress>]
 [-ReservedIP <IPAddress>] [[-OptionId] <UInt32[]>] [-UserClass <String>] [-All] [-Brief]
 [-PolicyName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
**Get-DhcpServerv4OptionValue** cmdlet 可以返回服务器、作用域或预留级别上一个或多个 IPv4 选项的数值。可以使用 *VendorClass* 和 *UserClass* 参数来获取特定供应商类别或特定用户类别对应的选项值。如果未指定 *OptionId* 参数，该 cmdlet 将返回在指定级别（无论是服务器、作用域还是预留级别）上配置的所有选项的数值。

如果您仅指定 `ReservedIP` 参数，则会返回在 `rReservation` 级别设置的选项值；如果您仅指定 `ScopeId` 参数，则会返回在 `scope` 级别设置的选项值；如果您既不指定 `ScopeId` 也不指定 `ReservedIP` 参数，那么会返回在服务器级别设置的选项值。

如果您既没有指定 *VendorClass* 参数，也没有指定 *UserClass* 参数，此cmdlet会使用默认的选项值。

不能同时指定 *PolicyName* 和 *UserClass* 这两个参数。

如果指定了 *ReservedIP* 参数，则不能指定 *PolicyName* 参数。

这些策略选项值仅适用于在 Windows Server® 2012 上运行的 DHCP 服务器服务。对于旧版本，仅支持基于用户类别的选项值。

要获取旧版用户类选项，必须指定 *UserClass* 参数。

## 示例

#### 示例 1：在服务器级别获取标准选项值
```
PS C:\> Get-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com"
```

这个示例获取了所有在服务器层面配置的标准 DHCPv4 选项值（即非特定类的选项值）。

### 示例 2：获取某个作用域的标准选项值
```
PS C:\> Get-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0
```

这个示例获取了为指定范围配置的所有标准的 DHCPv4 选项值（即非类别特定的选项值）。

### 示例 3：获取预订的标准选项值
```
PS C:\> Get-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ReservedIP 10.10.10.5
```

这个示例获取了为指定预订配置的所有标准 DHCPv4 选项值（即非特定类的选项值）。

### 示例 4：获取特定于“verdor”类的供应商类别的相关选项值
```
PS C:\> Get-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -VendorClass MSUCClient
```

这个示例会获取指定供应商类别在指定作用域内配置的所有与该供应商类别相关的DHCPv4选项值。

### 示例 5：通过使用选项 ID 获取某个作用域下的选项值
```
PS C:\> Get-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -OptionId 23
```

这个示例用于为指定的选项ID，在指定的作用域内配置DHCPv4选项的值。

### 示例 6：获取某个作用域下的所有选项值
```
PS C:\> Get-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -All
```

这个示例获取了指定范围内配置的所有DHCPv4选项值，包括标准选项值以及供应商特定类或用户特定类的选项值。

### 示例 7：简要获取某个作用域内的标准选项值
```
PS C:\> Get-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -Brief
```

这个示例会配置指定作用域内所有的标准 DHCPv4 选项值。返回的对象中不包含这些选项的名称。通过使用 “Brief” 参数，可以消除从 DHCP 服务器获取选项名称所需的时间延迟，从而提高性能。

### 示例 8：获取用户类别对应的特定选项值
```
PS C:\> Get-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -UserClass "LabComputer"
```

这个示例会获取指定用户类别在指定作用域内配置的所有与该用户类别相关的DHCPv4选项值。

### 示例 9：获取策略的标准选项值
```
PS C:\> Get-DhcpServerv4OptionValue -ComputerName dhcpserver.contoso.com -ScopeId 10.10.10.0 -Policy SmartPhonePolicy
```

这个示例会将指定策略中配置的所有标准 DHCPv4 选项值应用到指定的作用域中。

### 示例 10：获取策略和供应商类别的选项值
```
PS C:\> Get-DhcpServerv4OptionValue -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -Policy "SmartPhonePolicy" -VendorClass "HTC Phone"
```

这个示例会获取在指定范围内、针对指定的策略和供应商类别所配置的所有标准（即非特定于类的）DHCPv4选项值。

## 参数

### -All
用于获取某个范围（scope）、服务器或预订（reservation）的选项值。这些选项值可以包括供应商类别（vendor class）、用户类别（user class）以及与特定策略相关的设置。如果仅指定了该参数，此 cmdlet 将获取该范围、服务器或预订的所有选项值；如果同时指定了 *OptionId* 参数和该参数，则会返回与该指定选项标识符（ID）相关联的所有供应商类别、用户类别及策略的选项值；如果同时指定了 *VendorClass* 参数和该参数，则会返回该指定供应商类别的所有选项值（包括适用于任何用户类别或策略的选项）；如果同时指定了 *UserClass* 参数和该参数，则会返回该指定用户类别的所有选项值（包括任何与特定供应商相关的设置）；如果同时指定了 *PolicyName* 参数和该参数，则会返回该指定策略的所有选项值（包括任何与特定供应商相关的设置）。

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
该参数指定选项的名称不会被包含在返回的选项值对象中。通过避免从DHCP服务器服务中获取选项名称，可以提高此cmdlet的执行效率。对于需要反复使用此cmdlet来获取大量选项值的情况，建议使用*Brief*参数。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定运行动态主机配置协议（DHCP）服务器服务的目标计算机的DNS名称、IPv4地址或IPv6地址。

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
指定所请求选项的数字ID。

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

### -PolicyName
指定需要一个或多个选项值的策略名称。

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

### -ReservedIP
指定用于请求选项值的预留资源的IPv4地址。

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

### -ScopeId
指定所需一个或多个选项值的范围的ID，该ID采用IP地址格式表示。

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

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值（即并发操作的最大数量）。这个限制仅适用于当前正在运行的 cmdlet，而不适用于整个会话或整个计算机。

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
获取该用户类的选项值。

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
获取该供应商类别的选项值。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4OptionDefinition
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Policy
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4 Reservation
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstanceroot/Microsoft/Windows/DHCP/DhcpServerv4OptionValue[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Remove-DhcpServerv4OptionValue](./Remove-DhcpServerv4OptionValue.md)

[Set-DhcpServerv4OptionValue](./Set-DhcpServerv4OptionValue.md)

