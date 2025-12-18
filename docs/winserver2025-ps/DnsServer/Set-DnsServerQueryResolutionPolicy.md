---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerQueryResolutionPolicy_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverqueryresolutionpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerQueryResolutionPolicy
---

# Set-DnsServerQueryResolutionPolicy

## 摘要
更新DNS服务器上查询解析策略的设置。

## 语法

### 服务器（默认设置）
```
Set-DnsServerQueryResolutionPolicy [-PassThru] [-ComputerName <String>] -Name <String>
 [-TransportProtocol <String>] [-TimeOfDay <String>] [-RecursionScope <String>] [-ServerInterfaceIP <String>]
 [-QType <String>] [-ProcessingOrder <UInt32>] [-ECS <String>] [-ClientSubnet <String>] [-Condition <String>]
 [-InternetProtocol <String>] [-Fqdn <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 区域（Zone）
```
Set-DnsServerQueryResolutionPolicy [-PassThru] [-ComputerName <String>] [-ZoneName] <String> -Name <String>
 [-TransportProtocol <String>] [-TimeOfDay <String>] [-ServerInterfaceIP <String>] [-QType <String>]
 [-ProcessingOrder <UInt32>] [-ECS <String>] [-ClientSubnet <String>] [-Condition <String>] [-InternetProtocol <String>]
 [-Fqdn <String>] [-ZoneScope <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

请帮我将这段下面的以下Markdown文档转换成中文：
```
Set-DnsServerQueryResolutionPolicy [-PassThru] [-ComputerName <String>] [-InputObject] <CimInstance>
 [[-ZoneName] <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-DnsServerQueryResolutionPolicy` cmdlet 用于更新域名系统（DNS）服务器上查询解析策略的设置。

## 示例

### 示例 1：向策略中添加一个标准
```
PS C:\> Set-DnsServerQueryResolutionPolicy -Name "PolicyMalicious" -InternetProtocol "eq,IPv4" -PassThru | Format-List *

Action                : Ignore
AppliesOn             : QueryProcessing
Condition             : And
Content               :
Criteria              : {DnsServerPolicyCriteria, DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Server
Name                  : PolicyMalicious
ProcessingOrder       : 2
ZoneName              :
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties
```

此命令为名为“PolicyMalicious”的策略添加了一个与互联网协议相关的设置。该命令使用了`Format-List` cmdlet来控制输出内容的显示方式。如需更多信息，请输入`Get-Help Format-List`。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -ClientSubnet
指定客户端子网的标准。请按照以下格式来指定标准：

操作符，value01，value02，……，操作符，value03，value04，……

运算符只能是“EQ”（等于）或“NE”（不等于）。在一个条件中，每种运算符最多只能使用一次。

该策略将使用“EQ”运算符的值视为多个断言，并将这些断言在逻辑上进行组合（使用“OR”操作）。同样，该策略也将使用“NE”运算符的值视为多个断言，并在这些断言之间进行逻辑差异判断（使用“AND”操作）。当请求的子网与某个“EQ”值匹配，但与任何“NE”值都不匹配时，则认为满足该标准。

```yaml
Type: String
Parameter Sets: Server, Zone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如FQDN、主机名或NETBIOS名称。

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
指定策略如何处理多个标准。该参数的可接受值包括：

- OR.
The policy evaluates criteria as multiple assertions which are logically combined (OR'd).
- AND.
The policy evaluates criteria as multiple assertions which are logically differenced (AND'd).

默认值是“AND”。

```yaml
Type: String
Parameter Sets: Server, Zone
Aliases:
Accepted values: AND, OR

Required: False
Position: Named
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

### -ECS

此参数仅供内部使用。

```yaml
Type: String
Parameter Sets: Server, Zone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Fqdn
指定 FQDN 标准。请按照以下格式来指定标准：

操作符，value01，value02，……，操作符，value03，value04，……

运算符只能是“EQ”（等于）或“NE”（不等于）。每个条件最多只能指定一个这样的运算符。

该策略将使用“EQ”运算符的值视为多个断言，并将这些断言在逻辑上进行组合（使用“OR”操作）。同样，该策略也将使用“NE”运算符的值视为多个断言，并在这些断言之间进行逻辑上的差异判断（使用“AND”操作）。只有当请求的完全 qualified domain name（FQDN）与某个“EQ”值匹配，但不与任何“NE”值匹配时，才满足这一条件。你可以使用星号（*）作为通配符。例如：`EQ,*.contoso.com,NE,*.fabrikam.com`。

```yaml
Type: String
Parameter Sets: Server, Zone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InputObject
指定要传递给此cmdlet的输入数据。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

```yaml
Type: CimInstance
Parameter Sets: InputObject
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -InternetProtocol
指定互联网协议（IP）的相关标准。请按照以下格式来提供标准：

操作符，value01，value02，……，操作符，value03，value04，……

运算符只能是“EQ”（等于）或“NE”（不等于）。在一个条件中，每种运算符最多只能使用一次。

该策略将紧跟在“EQ”（等于）运算符之后的值视为多个断言，并将这些断言在逻辑上进行组合（使用“OR”操作）。同样，该策略也将紧跟在“NE”（不等于）运算符之后的值视为多个断言，并在这些断言之间进行逻辑上的区分（使用“AND”操作）。只有当请求的IP地址与某个“EQ”值匹配，但不与任何“NE”值匹配时，才认为满足了该条件。

```yaml
Type: String
Parameter Sets: Server, Zone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定要修改的政策名称。

```yaml
Type: String
Parameter Sets: Server, Zone
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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
用于指定策略的优先级。整数数值越大，优先级越低。默认情况下，此cmdlet会添加一个新策略，并将其优先级设置为最低级别。

如果此cmdlet将处理顺序更改为与现有策略的处理顺序相同，则DNS服务器会更新这些现有策略的处理顺序。

```yaml
Type: UInt32
Parameter Sets: Server, Zone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -QType
指定查询类型的标准。请按照以下格式来指定标准：

操作符，value01，value02，……，操作符，value03，value04，……

运算符只能是“EQ”（等于）或“NE”（不等于）。在一个条件中，每种运算符最多只能使用一次。

该政策将使用 EQ 运算符的值视为多个断言，并将这些断言在逻辑上进行组合（通过 OR 运算）。同样地，该政策也将使用 NE 运算符的值视为多个断言，并在这些断言之间进行逻辑上的差异比较（通过 AND 运算）。当请求的查询类型与某个 EQ 值匹配，但与任何 NE 值都不匹配时，即认为满足了该条件。

```yaml
Type: String
Parameter Sets: Server, Zone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RecursionScope
指定递归的范围。如果该策略是一个递归策略，并且某个查询与该策略匹配，那么DNS服务器将使用此范围内的设置来进行该查询的递归处理。

```yaml
Type: String
Parameter Sets: Server
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ServerInterfaceIP
指定DNS服务器监听的服务器接口的IP地址。请按照以下格式提供相关信息：

操作符，value01，value02，……，操作符，value03，value04，……

运算符只能是“EQ”（等于）或“NE”（不等于）。在条件中，每种运算符最多只能使用一次。

该策略将使用“EQ”运算符的值视为多个逻辑上组合在一起的断言（即通过“OR”连接）。同样，该策略也将使用“NE”运算符的值视为多个逻辑上区分开来的断言（即通过“AND”连接）。当接口的IP地址与某个“EQ”值匹配，但与任何“NE”值都不匹配时，则认为该标准得到满足。

```yaml
Type: String
Parameter Sets: Server, Zone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时执行的操作的最大数量。如果省略此参数或输入 `0`，则 Windows PowerShell 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -TimeOfDay
指定一天中的时间标准。请按照以下格式来指定标准：

操作符，value01，value02，……，操作符，value03，value04，……

运算符只能是“EQ”（等于）或“NE”（不等于）。在条件中，每种运算符最多只能使用一次。

该策略将使用“EQ”运算符的值视为多个断言，并将这些断言在逻辑上进行组合（即使用“OR”操作）。同样地，该策略将使用“NE”运算符的值也视为多个断言，并在这些断言之间进行逻辑上的差异判断（即使用“AND”操作）。只有当请求的时间与某个“EQ”值匹配，但不与任何“NE”值匹配时，才认为满足了该条件。

```yaml
Type: String
Parameter Sets: Server, Zone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TransportProtocol
指定传输协议的标准。请按照以下格式来指定标准：

操作符，value01，value02，……，操作符，value03，value04，……

运算符只能是“EQ”（等于）或“NE”（不等于）。在字符串中，每种运算符最多只能出现一次。

该策略将使用EQ运算符的值视为多个相互逻辑连接（通过OR操作）的断言；同时，也将使用NE运算符的值视为多个相互逻辑区分（通过AND操作）的断言。当请求的传输协议与某个EQ值匹配，但与任何NE值都不匹配时，则认为该标准得到满足。

```yaml
Type: String
Parameter Sets: Server, Zone
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

### -ZoneName
指定DNS区域的名称，该区域级别策略将应用于此DNS区域。该区域必须存在于DNS服务器上。

```yaml
Type: String
Parameter Sets: Zone
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

```yaml
Type: String
Parameter Sets: InputObject
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ZoneScope
用于指定该区域的权限范围（scope）及其对应的权重（weight）。请以如下格式的字符串来输入该值：

Scope01, Weight01；Scope02, Weight02；

如果您没有指定权重，那么默认值为一（1）。

```yaml
Type: String
Parameter Sets: Zone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerPolicy

## 备注

## 相关链接

[Add-DnsServerQueryResolutionPolicy](./Add-DnsServerQueryResolutionPolicy.md)

[Get-DnsServerQueryResolutionPolicy](./Get-DnsServerQueryResolutionPolicy.md)

[Remove-DnsServerQueryResolutionPolicy](./Remove-DnsServerQueryResolutionPolicy.md)

[Add-DnsServerZoneTransferPolicy](./Add-DnsServerZoneTransferPolicy.md)

