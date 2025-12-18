---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4Policy_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/add-dhcpserverv4policy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DhcpServerv4Policy
---

# Add-DhcpServerv4Policy

## 摘要
在服务器级别或作用域级别添加新的策略。

## 语法

```
Add-DhcpServerv4Policy [-ComputerName <String>] [-Name] <String> [-Condition] <String> [-Description <String>]
 [-ScopeId <IPAddress>] [-ProcessingOrder <UInt16>] [-RelayAgent <String[]>] [-RemoteId <String[]>]
 [-SubscriberId <String[]>] [-PassThru] [-LeaseDuration <TimeSpan>] [-Fqdn <String[]>] [-Enabled <Boolean>]
 [-VendorClass <String[]>] [-UserClass <String[]>] [-MacAddress <String[]>] [-CircuitId <String[]>]
 [-ClientId <String[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
**Add-DhcpServerv4Policy** cmdlet 可以在服务器级别或特定范围级别添加新的 DHCP 策略。策略名称在该级别（无论是服务器级别还是特定范围）必须是唯一的，并且必须至少包含一个条件，这些条件的具体类型由 *CircuitId*、*ClientId*、*Fqdn*、*MACAddress*、*RelayAgent*、*RemoteId*、*SubscriberId*、*UserClass* 或 *VendorClass* 参数来确定。

## 示例

### 示例 1：为虚拟机客户端创建服务器级策略
```
PS C:\> Add-DhcpServerv4Policy -Name "HyperVPolicy" -Condition OR -MacAddress EQ,00155D*,000569*
```

这个示例为虚拟机客户端创建了一个服务器级别的策略。该策略中使用了Hyper-V虚拟机（MAC地址为00-15-5D）和VMWare虚拟机（MAC地址为00-05-69）的MAC地址作为条件。

### 示例 2：为非虚拟机客户端创建服务器级别的策略
```
PS C:\> Add-DhcpServerv4Policy -Name "PhysicalComputersPolicy" -Condition OR -MacAddress NE,00155D*,000569*
```

这个示例为非虚拟机客户端创建了一个服务器级别的策略。在该策略中，Hyper-V虚拟机（MAC地址为00-15-5D）和VMware虚拟机（MAC地址为000569）的MAC地址被用作否定条件（即这些虚拟机不被该策略所覆盖）。

### 示例 3：为虚拟机客户端创建一个作用域级别策略
```
PS C:\> Add-DhcpServerv4Policy -Name "VMPolicy" -ScopeId 10.10.10.0 -Condition OR -MacAddress EQ,00155D*,000569*
```

这个示例为位于 IP 地址范围 10.10.10.0 内的虚拟机客户端创建了一个策略。在策略中，使用了 Hyper-V 虚拟机（MAC 地址为 00-15-5D）和 VMware 虚拟机（MAC 地址为 00-05-69）的 MAC 地址作为条件。

### 示例 4：根据供应商类别在某个范围内创建打印机策略
```
PS C:\> Add-DhcpServerv4Policy -Name "PrinterPolicy" -ScopeId 10.10.10.0 -Condition OR -VendorClass EQ,"HP Printer","Xerox Printer"
```

这个示例在 10.10.10.0 的范围内，根据打印机的厂商类别创建了一个打印机策略。在使用这些厂商类别之前，必须先定义它们。

### 示例 5：根据用户类别在某个范围内创建打印机策略
```
PS C:\> Add-DhcpServerv4Policy -Name "LabComputerPolicy" -ScopeId 10.10.10.0 -Condition OR -UserClass EQ,LabComputers
```

这个示例根据用户类别，在 10.10.10.0 网段范围内创建了一项实验室计算机策略。在用户类别被用于该策略之前，必须先对其进行定义。

### 示例 6：根据作用域内的中继代理信息创建策略
```
PS C:\> Add-DhcpServerv4Policy -Name "RelayAgentBasedPolicy" -ScopeId 10.10.10.0 -Condition OR -RelayAgent EQ,01030a0b0c02050000000123
```

这个示例根据中继代理信息（选项82）在10.10.10.0范围内的设置来创建一个策略。DHCP中继代理必须被配置为使用该中继代理信息选项（选项82）。

### 示例 7：根据 MAC 地址前缀和供应商类别组合条件来创建策略
```
PS C:\> Add-DhcpServerv4Policy -Name "DevicesPolicy" -ScopeId 10.10.10.0 -Condition OR -MacAddress EQ,F8DB7F* -VendorClass EQ,Android
```

这个示例通过结合条件（使用“OR”逻辑运算符）来创建一条策略。这些条件的依据是HTC手机设备的MAC地址前缀以及Android系统的厂商类别，且该策略的应用范围为10.10.10.0网络。在策略中使用某个厂商类别之前，必须先对该类别进行定义。

### 示例 8：为虚拟机客户端创建服务器级别的策略，并指定处理顺序
```
PS C:\> Add-DhcpServerv4Policy -Name "HyperVPolicy" -Condition OR -MacAddress EQ,00155D*,000569* -ProcessingOrder 2 -Enabled $False
```

这个示例为虚拟机客户端创建了一个服务器级别的策略，并为其分配了处理顺序（编号为2），同时将该策略设置为“禁用”状态。在策略中，使用了Hyper-V虚拟机（MAC地址：00-15-5D）和VMWare虚拟机（MAC地址：00-05-69）的MAC地址作为判断条件。

### 示例 9：通过结合基于 MAC 地址前缀和供应商类别的条件以及租约持续时间来创建策略
```
PS C:\> Add-DhcpServerv4Policy -Name "DevicesPolicy" -Condition OR -LeaseDuration 10 -MacAddress EQ,F8DB7F -ScopeId 10.10.10.0 -VendorClass "EQ","Android"
```

这个示例通过结合条件（使用 OR 运算符）来创建一个策略，这些条件的依据是 HTC 手机设备的 MAC 地址前缀以及 Android 系统的供应商类别，作用范围为 10.10.10.0。在策略中使用某个供应商类别之前，必须先对该类别进行定义。此外，该命令将客户端的租约持续时间设置为 10 天。

### 示例 10：为加入工作组的客户端创建服务器级别的策略
```
PS C:\> Add-DhcpServerv4Policy -Name "WorkgroupDevices" -Condition OR -Fqdn "Isl"
```

这个示例为加入了工作组的客户端创建了一个服务器级别的策略。该策略会匹配那些在策略条件中包含单个标签FQDN的客户端。

### 示例 11：为不属于某个域的客户端创建服务器级别的策略
```
PS C:\> Add-DhcpServerv4Policy -Name "ForeignDevices" -Condition OR -Fqdn NE,*.contoso.com
```

这个示例为所有不属于本地域（contoso.com）的远程客户端创建了一个服务器级别的策略。该策略适用于那些FQDN中不包含“contoso.com”这一字符串的客户端。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行耗时较长的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。您可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定要使用的比较器以及用于比较电路ID子选项的值。第一个元素是比较器（可以是EQ或NE），其后是一个单独的值。

如果一个值中的最后一个字符是星号（*），那么后续的字符将被视为通配符，用于进行比较。如果一个值元素中的第一个字符是星号，那么前面的字符也将被视为通配符，用于进行比较。

该值后面可以再接另一个比较器（可以是 EQ 或 NE），然后是另一个用于比较的值。

该值的输入格式为十六进制字符串，可以包含连字符（-）进行分隔，也可以不包含连字符。

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
指定要使用的比较器以及用于比较客户端标识符的值。第一个元素是比较器（可以是“EQ”或“NE”），后续的元素则是具体的值。

如果一个值中的最后一个字符是星号（*），那么后续的字符将被视为通配符，用于进行比较。如果一个值元素中的第一个字符是星号，那么前面的字符也将被视为通配符，用于进行比较。

这些值之后可以再次使用另一个比较器（可以是“EQ”或“NE”），然后是另一组用于比较的值。

输入格式是一个十六进制字符串，可以包含连字符（-）也可以不包含连字符。例如：`EQ, 00-11-22-33-44-55, AA-BB-CC-DD-EE*`。

请将以下Markdown内容转换为中文：

输出格式是一个用连字符分隔的十六进制字符串。

紧跟在“EQ”操作符后面的值被视为多个断言，这些断言通过逻辑运算（“或”）进行组合。

跟随 NE 运算符的值被视为多个断言，这些断言在逻辑上是通过与操作（AND）进行连接的。

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

### -Condition
当指定了多个条件时，该参数用于指定这些条件之间的逻辑运算符。可接受的值有：AND 和 OR。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: And, Or

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
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
指定所添加策略的描述字符串。

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
指定策略的启用状态。

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
指定要使用的比较器以及用于比较客户端请求中完全限定域名（FQDN）的值。第一个元素是比较器，可以是 EQ、NE、Isl 或 Insl；后续的元素则是相应的值。对于 Island 和 Insl 类型的比较器，应使用空值作为比较依据。如果某个值的最后一个字符是星号（*），则该值中的其余字符将被视为通配符用于匹配；同样地，如果某个值元素的第一个字符是星号，那么该值前面的字符也将被视为通配符。

这些值后面可以再跟着另一个比较器（EQ 或 NE），然后再是一组新的值。

输入格式是一串字符串。字符串末尾可以包含通配符（*），以表示部分匹配。

紧跟在“EQ”操作符后面的值被视为多个断言，这些断言通过逻辑运算（“或”）进行组合。

跟随 NE 运算符的值被视为多个断言，这些断言在逻辑上是通过与操作（AND）进行连接的。

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
指定符合该策略的客户所获得的租赁期限（即使用资源的时长）。

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
指定要使用的比较器以及用于在客户端请求中比较MAC地址的值。第一个元素是比较器（EQ或NE），随后的元素则是待比较的值。如果某个值的最后一个字符是星号（*），则该值中的后续字符将被视为通配符用于比较；如果某个值元素的第一个字符是星号，那么该值前面的所有字符也将被用于比较。

这些值后面可以再跟着另一个比较器（EQ 或 NE），然后再是一组新的值。

输入格式是一个十六进制字符串，可以包含连字符（-）也可以不包含。字符串末尾可以有一个通配符（*），表示部分匹配。例如：`00-1F-3B-7C-B7-89`, `00-1F-3B-7C-B7-*, `001F3B7CB789`。输出格式也是一个十六进制字符串，但必须使用连字符（-）进行分隔。

紧跟在“EQ”操作符后面的值被视为多个断言，这些断言通过逻辑运算（“或”）进行组合。

跟随 NE 运算符的值被视为多个断言，这些断言在逻辑上是通过与操作（AND）进行连接的。

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
指定要添加的策略的名称。

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

### -ProcessingOrder
指定该策略在作用域或服务器内相对于其他策略的优先级顺序。DHCP服务器服务在处理客户端请求时会按照指定的顺序来执行这些策略。

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
指定用于比较中继代理信息的比较器以及用于进行比较的值。第一个元素是比较器（EQ或NE），后续的元素则是具体的值。如果某个值中的最后一个字符是星号（*），那么该值中的其他字符将被视为通配符，用于进行匹配；如果某个值元素的首个字符是星号，那么该值前面的所有字符也将被视为通配符。

这些值后面可以再跟着另一个比较器（EQ 或 NE），然后再是一组新的值。

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
指定用于比较远程ID子选项的比较器以及比较所使用的值。第一个元素是比较器（EQ或NE），后面跟着一个具体的数值。如果某个数值的最后一个字符是星号（*），则后续的字符将被视为通配符用于比较；如果某个数值元素的第一个字符是星号，那么前面的字符也会被视为通配符用于比较。

该值之后可以再次跟随另一个比较运算符（EQ或NE），然后再是另一个值。

该值的输入格式为十六进制字符串，可以包含连字符（-）进行分隔，也可以不包含连字符。

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
指定策略所添加的范围标识符（采用 IPv4 地址格式）。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SubscriberId
指定要使用的比较器以及用于比较订阅者ID的数值。第一个元素是比较器（EQ或NE），其后是一个具体的数值。如果某个数值的最后一个字符是星号（*），那么该数值中的后续字符将被视为通配符，用于进行比较；同样地，如果某个数值元素的第一个字符是星号，那么该数值前面的字符也将被视为通配符，用于进行比较。

该值之后可以再次跟随另一个比较运算符（EQ或NE），然后再是另一个值。

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
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
指定要使用的比较器以及用于与客户端请求中的用户类字段进行比较的用户类值。需要指定的第一个元素是比较器（EQ或NE），随后的元素则是具体的值。如果某个值的最后一个字符是星号（*），那么该值中的后续字符将被视为通配符，用于进行匹配操作；同样地，如果某个值元素的第一个字符是星号，那么该值前面的字符也会被视为通配符。

这些值后面可以再跟着另一个比较器（EQ 或 NE），然后再是一组新的值。

需要指定的值是用户类名称，这些名称已经存在于服务器上。

紧跟在“EQ”操作符后面的值被视为多个断言，这些断言通过逻辑运算（“或”）进行组合。

跟随 NE 运算符的值被视为多个断言，这些断言在逻辑上是通过与操作（AND）进行连接的。

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
指定要使用的比较器以及用于与客户端请求中的 vendor class 字段进行比较的 vendor class 值。第一个元素是比较器（EQ 或 NE），随后的元素则是相应的值。如果某个值的最后一个字符是星号（*），则该值中的后续字符将被视为通配符；如果某个值元素的第一个字符是星号，那么该值前面的字符也将被视为通配符。

这些值后面可以再跟着另一个比较器（EQ 或 NE），然后再是一组新的值。

需要指定的值是供应商类名称，这些名称已经存在于服务器上。

紧跟在“EQ”操作符后面的值被视为多个断言，这些断言通过逻辑运算（“或”）进行组合。

跟随 NE 运算符的值被视为多个断言，这些断言在逻辑上是通过与操作（AND）进行连接的。

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
展示了如果该cmdlet运行会发生什么情况。但实际上这个cmdlet并没有被执行。

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

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Policy
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Policy
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv4PolicyIPRange](./Add-DhcpServerv4PolicyIPRange.md)

[Get-DhcpServerv4Policy](./Get-DhcpServerv4Policy.md)

[Get-DhcpServerv4PolicyIPRange](./Get-DhcpServerv4PolicyIPRange.md)

[Remove-DhcpServerv4Policy](./Remove-DhcpServerv4Policy.md)

[Remove-DhcpServerv4PolicyIPRange](./Remove-DhcpServerv4PolicyIPRange.md)

[Set-DhcpServerv4Policy](./Set-DhcpServerv4Policy.md)

