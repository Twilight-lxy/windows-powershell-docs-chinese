---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4Policy_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/set-dhcpserverv4policy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DhcpServerv4Policy
---

# Set-DhcpServerv4Policy

## 摘要
在服务器级别或指定的范围级别设置策略的属性。

## 语法

```
Set-DhcpServerv4Policy [-ComputerName <String>] [-Description <String>] [-Name] <String>
 [[-ScopeId] <IPAddress>] [-Enabled <Boolean>] [-MacAddress <String[]>] [-Fqdn <String[]>]
 [-UserClass <String[]>] [-SubscriberId <String[]>] [-NewName <String>] [-ClientId <String[]>] [-PassThru]
 [-LeaseDuration <TimeSpan>] [-ProcessingOrder <UInt16>] [-RelayAgent <String[]>] [-RemoteId <String[]>]
 [-CircuitId <String[]>] [-Condition <String>] [-VendorClass <String[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DhcpServerv4Policy` cmdlet 可以在服务器级别或指定的作用域级别设置现有策略的属性。如果指定了 `CircuitId`、`ClientId`、`Fqdn`、`MACAddress`、`RelayAgent`、`RemoteId`、`SubscriberId`、`UserClass` 或 `VendorClass` 参数，则策略的条件将会被修改，此时该 cmdlet 的行为如下：

如果指定了 *VendorClass* 参数，并且正在修改的策略已经包含针对该参数值的条件，那么现有的 *VendorClass* 参数值将被删除，新的 *VendorClass* 参数值将会被添加。

然而，如果被修改的策略中对 *MacAddress* 参数值有相应的条件限制，那么 *MacAddress* 参数的值将不会被更改，而是会与基于 *VendorClass* 的条件进行逻辑组合（使用 OR 运算符）或逻辑对比（使用 AND 运算符）。

同样的规则也适用于任何在条件中使用到的参数，例如*CircuitId*、*ClientId*、*Fqdn*、*MACAddress*、*RelayAgent*、*RemoteId*、*SubscriberId*、*UserClass*或*VendorClass*。

## 示例

#### 示例 1：修改服务器级别的策略
```
PS C:\> Set-DhcpServerv4Policy -ComputerName "dhcpserver.contoso.com" -Name "DevicesPolicy" -NewName TabletPolicy -Description "policy for tablet devices" -ProcessingOrder 4 -Enabled $False
```

这个示例将服务器级别的策略“DevicesPolicy”重命名为“TabletPolicy”，为其设置一个描述字符串，禁用该策略，并将其处理顺序设置为第4位。

### 示例 2：修改服务器级别策略的条件
```
PS C:\> Set-DhcpServerv4Policy -Name "PhysicalMachinesPolicy" -Condition OR -MacAddress NE,00155D*,000569*
```

这个示例修改了服务器级别策略中针对非Hyper-V客户端的条件。如果该策略原本包含基于MAC地址的条件，那么这些条件将被替换为此cmdlet中指定的新条件。然而，如果策略中还包含基于其他字段（如*VendorClass*、*UserClass*、*ClientId*或*RelayAgent*参数）的条件，这些条件将会被保留下来，并与新添加的基于MAC地址的条件进行逻辑组合（使用“OR”运算符）。

#### 示例 3：修改非 Hyper-V 客户端的服务器级策略的条件
```
PS C:\> Set-DhcpServerv4Policy -Name "PhysicalMachinesPolicy" -Condition OR -MacAddress NE,00155D*,000569* -VendorClass ""
```

这个示例修改了针对非Hyper-V客户端的服务器级策略的条件。如果该策略之前包含基于MAC地址的条件、基于供应商类别的条件，或者同时包含这两种条件，那么这些条件将被替换为此cmdlet中指定的条件。

### 示例 4：为服务器级别策略设置租约持续时间
```
PS C:\> Set-DhcpServerv4Policy -Name "TabletPolicy" -ComputerName "dhcpserver.contoso.com" -LeaseDuration 10
```

此示例将为名为 TablePolicy 的服务器级策略设置租约期限为 10 天，适用于指定的计算机。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job` cmdlets系列命令；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。您可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -CircuitId
指定要使用的比较器以及用于比较电路标识符（ID）的数值。第一个元素是比较器（EQ或NE），后面跟着一个具体的数值。如果某个数值的最后一个字符是星号（*），那么该数值后面的所有字符都将作为通配符用于比较；同样地，如果某个数值元素的第一个字符是星号，那么该数值前面的所有字符也将作为通配符用于比较。

该值之后可以跟另一个比较器（EQ或NE），然后再是一个值。

该值的输入格式是一个十六进制字符串，可以包含连字符（-）进行分隔，也可以不包含连字符。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ClientId
指定要使用的比较器以及用于比较客户端标识符的值。第一个元素是比较器（EQ或NE），后面跟着一组值。如果某个值的最后一个字符是星号（*），则该值中的后续字符将被视为通配符用于比较；如果某个值元素的第一个字符是星号，那么该值前面的字符也将被视为通配符用于比较。

这些值后面可以跟另一个比较运算符（EQ或NE），然后再是一组新的值。

输入格式是一个十六进制字符串，可以包含也可以不包含连字符作为分隔符。输出格式也是一个十六进制字符串，但必须使用连字符作为分隔符。

EQ运算符后面的值被视为多个断言，这些断言在逻辑上是组合在一起的（使用OR操作符）。

NE运算符后面的值被视为多个断言（assertions），这些断言在逻辑上是通过“与”（AND）进行连接的。

格式的一个例子是：`EQ, 00-11-22-33-44-55, AA-BB-CC-DD-EE*`。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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

### -Condition
当指定了多个条件时，该参数用于指定这些条件之间的逻辑运算符。可接受的值有：AND（与）或 OR（或）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: And, Or

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前，会提示您进行确认。

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
指定要设置在策略上的描述信息。

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

### -Enabled
指定该策略的启用状态。

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

### -Fqdn
用于指定要使用的比较器以及用于比较客户端请求中的完全限定域名（FQDN）的值。第一个元素是比较器，可以是 EQ、NE、Isl 或 Insl；后续的元素则是具体的值。对于 Island 和 Insl 这两种比较器类型，应使用空字符串作为对应的值。如果某个值的最后一个字符是星号（*），则该值中的其余字符将被视为通配符用于匹配操作；同样地，如果某个值元素的第一个字符是星号，那么该值前面的字符也会被视为通配符。

这些值之后可以再跟随另一个比较器（EQ或NE），然后再是一组新的值。

输入格式是一个字符串。字符串末尾可以包含通配符（*），表示部分匹配。

EQ运算符后面的值被视为多个断言，这些断言在逻辑上被组合在一起（使用“OR”操作）。

NE运算符后面的值被视为多个断言，这些断言在逻辑上是通过“与”（AND）操作进行连接的。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LeaseDuration
指定符合该策略的客户所使用的租约期限。

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

### -MacAddress
指定要使用的比较器以及用于在客户端请求中比较MAC地址的值。第一个元素是比较器（EQ或NE），其后是一组值。如果某个值的最后一个字符是星号（*），则该值中的后续字符将被视为通配符用于比较；如果某个值元素的第一个字符是星号，那么该值前面的字符也将被视为通配符用于比较。

这些值后面可以跟另一个比较运算符（EQ或NE），然后再是一组新的值。

输入格式是一个十六进制字符串，可以包含连字符（-）也可以不包含。在字符串末尾可以使用通配符（*）来表示部分匹配。输出格式也是一个十六进制字符串，但必须使用连字符（-）进行分隔。

EQ运算符后面的值被视为多个断言，这些断言在逻辑上是组合在一起的（使用OR操作符）。

NE运算符后面的值被视为多个断言（assertions），这些断言在逻辑上是通过“与”（AND）进行连接的。

该格式的一个示例是：`00-1F-3B-7C-B7-89, 00-1F-3B-7C-B7-*, 001F3B7CB789`。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定正在修改的策略的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NewName
指定要为该策略设置的新名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不生成任何输出。

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

### -ProcessingOrder
该属性用于指定此策略在作用域内或其他策略以及DHCP服务器服务中的优先级顺序。DHCP服务器服务在处理客户端请求时会按照指定的顺序来应用这些配置好的策略。

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

### -RelayAgent
指定要使用的比较器以及用于比较中继代理信息的值。第一个元素是比较器（EQ或NE），后面跟着一组值。如果某个值的最后一个字符是星号（*），那么该值中的后续字符将被视为通配符用于比较；同样地，如果某个值元素的第一个字符是星号，那么该值前面的字符也将被视为通配符用于比较。

这些值后面可以跟另一个比较运算符（EQ或NE），然后再是一组新的值。

输入格式是一个十六进制字符串，可以带有连字符分隔，也可以不带连字符分隔。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RemoteId
指定要使用的比较器以及用于比较远程ID的数值。第一个元素是比较器（EQ或NE），后面跟着一个具体的数值。如果某个数值的最后一个字符是星号（*），那么该数值中的后续字符将作为通配符参与比较；同样地，如果某个数值元素的第一个字符是星号，那么该数值前面的字符也会被视为通配符。

该值之后可以再次跟一个比较运算符（EQ或NE），然后是另一个值。

该值的输入格式是一个十六进制字符串，可以包含连字符（-）进行分隔，也可以不包含连字符。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScopeId
指定包含该策略的作用域的范围ID（采用IPv4地址格式）。如果未指定此参数，则会修改服务器级别的策略。

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

### -SubscriberId
该选项用于指定用于比较订阅者ID的比较器以及比较所使用的值。第一个元素是比较器（EQ或NE），其后是一个具体的数值。如果某个数值的最后一个字符是星号（*），则后续的所有字符将被视为通配符，用于进行匹配操作；同样地，如果某个数值元素的第一个字符是星号，那么前面的所有字符也会被视为通配符。

该值之后可以再次跟一个比较运算符（EQ或NE），然后是另一个值。

输入格式是一个十六进制字符串，可以带有连字符分隔，也可以不带连字符分隔。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
指定要使用的比较器以及用于在客户端请求中比较用户类字段的用户类值。首先需要指定的是比较器（EQ或NE），然后是一组值。如果某个值的最后一个字符是星号（*），则后续的字符将作为通配符用于比较；如果某个值元素的第一个字符是星号，那么前面的字符也将作为通配符用于比较。

这些值后面可以跟另一个比较运算符（EQ或NE），然后再是一组新的值。

需要指定的值必须是已经存在于 DHCP 服务器服务中的用户类别名称。

该值的格式应该是一个以 `0x` 开头的十六进制字符串。

EQ运算符后面的值被视为多个断言，这些断言在逻辑上被组合在一起（使用“或”（OR）操作）。

NE操作符后面的值被视为多个断言，这些断言之间是通过逻辑与（AND）进行连接的。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -VendorClass
指定要使用的比较器以及用于比较客户端请求中“vendor class”字段的供应商类值的集合。第一个元素是比较器（EQ或NE），后面跟着一组值。如果某个值中的最后一个字符是星号（*），那么该值后面的所有字符都将被视为通配符，用于进行比较；同样地，如果某个值元素中的第一个字符是星号，那么该值前面的所有字符也将被视为通配符。

这些值之后可以跟随另一个比较运算符（如 EQ 或 NE），然后再是一组新的值。

需要指定的值必须是已经在DHCP服务器服务中存在的供应商类名称。

该值的格式应该是一个以 `0x` 开头的十六进制字符串。

EQ运算符后面的值被视为多个断言，这些断言在逻辑上被组合在一起（使用“或”（OR）操作）。

NE操作符后面的值被视为多个断言，这些断言之间是通过逻辑与（AND）进行连接的。

```yaml
Type: String[]
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Policy
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名称。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名称。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Policy
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名称。

## 备注

## 相关链接

[Add-DhcpServerv4Policy](./Add-DhcpServerv4Policy.md)

[Add-DhcpServerv4PolicyIPRange](./Add-DhcpServerv4PolicyIPRange.md)

[Get-DhcpServerv4Policy](./Get-DhcpServerv4Policy.md)

[Get-DhcpServerv4PolicyIPRange](./Get-DhcpServerv4PolicyIPRange.md)

[Remove-DhcpServerv4Policy](./Remove-DhcpServerv4Policy.md)

[Remove-DhcpServerv4PolicyIPRange](./Remove-DhcpServerv4PolicyIPRange.md)

