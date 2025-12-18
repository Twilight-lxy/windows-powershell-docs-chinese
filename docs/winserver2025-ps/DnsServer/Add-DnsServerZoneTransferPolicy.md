---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerZoneTransferPolicy_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserverzonetransferpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerZoneTransferPolicy
---

# Add-DnsServerZoneTransferPolicy

## 摘要
向DNS服务器添加一个区域传输策略。

## 语法

### 服务器（默认设置）
```
Add-DnsServerZoneTransferPolicy [-ComputerName <String>] [-PassThru] [[-Action] <String>]
 [-ClientSubnet <String>] [[-Condition] <String>] [-InternetProtocol <String>] [-Disable] [-Name] <String>
 [-ProcessingOrder <UInt32>] [-ServerInterfaceIP <String>] [-TimeOfDay <String>] [-TransportProtocol <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 区域（Zone）
```
Add-DnsServerZoneTransferPolicy [-ComputerName <String>] [-PassThru] [-ZoneName] <String> [[-Action] <String>]
 [-ClientSubnet <String>] [[-Condition] <String>] [-InternetProtocol <String>] [-Disable] [-Name] <String>
 [-ProcessingOrder <UInt32>] [-ServerInterfaceIP <String>] [-TimeOfDay <String>] [-TransportProtocol <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject
```
Add-DnsServerZoneTransferPolicy [-ComputerName <String>] [-PassThru] [-InputObject] <CimInstance>
 [[-ZoneName] <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-DnsServerZoneTransferPolicy` cmdlet 用于向域名系统（DNS）服务器添加区域传输策略。该策略会根据您在策略中指定的标准来决定区域传输的方式。

一项政策由标准（criteria）和行动（action）两部分组成。

这些标准是客户端子网、服务器接口IP地址、完全限定域名（FQDN）、互联网协议（IPv4/IPv6）、传输协议（UDP/TCP）、时间以及查询类型等元素的逻辑组合。

请按照以下格式指定标准：

操作符，值01，值02，……，操作符，值03，值04，……

运算符只能是“EQ”（等于）或“NE”（不等于）。在一个条件中，每种运算符最多只能使用一次。

该策略将紧跟在“EQ”操作符之后的值视为多个断言，并对这些断言进行逻辑组合（使用“OR”运算）。同样，该策略也将紧跟在“NE”操作符之后的值视为多个断言，并对这些断言进行逻辑区分（使用“AND”运算）。

此cmdlet通过使用*Condition*参数的值作为逻辑运算符来结合多个条件。该参数可以取以下值之一：

- OR.
The policy evaluates criteria as multiple assertions which are logically combined (OR'd).
- AND.
The policy evaluates criteria as multiple assertions which are logically differenced (AND'd).

如果某个查询符合某项策略的标准，那么该策略所要求的响应动作就会被执行。你可以选择“DENY”（拒绝）或“IGNORE”（忽略）。

你可以在服务器级别或区域级别创建用于区域传输的策略。服务器级别的策略会应用于DNS服务器上发生的所有区域传输请求；而区域级别的策略仅适用于针对该DNS服务器上托管的区域所发出的请求。区域级别策略最常见的用途是实现“阻止列表”或“安全列表”的功能。

区域级别策略适用于您创建它们的那个区域。在没有区域的情况下，您无法创建区域级别策略。如果您删除了一个区域，那么与该区域关联的所有区域级别策略也会被一并删除。

## 示例

### 示例 1：创建服务器级别的区域传输策略
```
PS C:\> Add-DnsServerClientSubnet -Name "AllowedSubnet" -IPv4Subnet 172.21.33.0/24 -PassThru
PS C:\> Add-DnsServerZoneTransferPolicy -Name "NorthAmericaPolicy" -Action IGNORE -ClientSubnet "ne,AllowedSubnet" -PassThru | Format-List *
Name                                             IPV4Subnet                                       IPV6Subnet
----                                             ----------                                       ----------
AllowedSubnet                                    {172.21.33.0/24}



Action                : Ignore
AppliesOn             : ZoneTransfer
Condition             : And
Content               :
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Server
Name                  : NorthAmericaPolicy
ProcessingOrder       : 1
ZoneName              :
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties
```

第一个命令使用 **Add-DnsServerClientSubnet** cmdlet 创建了一个名为 AllowedSubnet 的客户端子网。该子网包含了指定的 IP 子网地址。

第二个命令创建了一个区域传输策略，该策略禁止所有不属于 AllowedSubnet 子网的客户进行访问。这是一个服务器级别的策略，因此它会应用于服务器上的所有区域。

### 示例 2：通过服务器接口禁止区域转移
```
PS C:\> Add-DnsServerZoneTransferPolicy -Name "InternalTransfers" -Action IGNORE -ServerInterfaceIP "ne,10.0.0.33" -PassThru
Name                                 ProcessingOrder                      IsEnabled                            Action
----                                 ---------------                      ---------                            ------
internalTransfers1                   3                                    True                                 Ignore
```

此命令创建了一个区域传输策略，该策略禁止所有未通过服务器接口 10.0.0.33 到达的区域传输请求。

### 示例 3：创建区域级别的区域传输策略
```
PS C:\> Add-DnsServerZoneTransferPolicy -Name "InternalTransfers" -Action IGNORE -ServerInterfaceIP "ne,10.0.0.33" -PassThru -ZoneName "contoso.com" | Format-List *
Action                : Ignore
AppliesOn             : ZoneTransfer
Condition             : And
Content               :
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Zone
Name                  : InternalTransfers
ProcessingOrder       : 1
ZoneName              : contoso.com
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties
```

此命令为 contoso.com 创建了一个区域级别的区域传输策略。

## 参数

### -Action
指定当区域传输符合此策略时应执行的操作。该参数的可接受值为：

- DENY.
Respond with SERV_FAIL.
- IGNORE.
Do not respond.

```yaml
Type: String
Parameter Sets: Server, Zone
Aliases:
Accepted values: DENY, IGNORE

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
指定客户端子网的标准。有关更多信息，请参阅 **Add-DnsServerClientSubnet**。按照以下格式指定标准：

操作符，值01，值02，……，操作符，值03，值04，……

运算符只能是“EQ”（等于）或“NE”（不等于）。在一个条件中，每种运算符最多只能使用一次。

该策略将遵循“EQ”（Equal to）操作符的值视为多个断言，并对这些断言进行逻辑组合（使用“OR”运算）。同样，遵循“NE”（Not Equal to）操作符的值也被视为多个断言，并对这些断言进行逻辑区分（使用“AND”运算）。当区域传输的子网与某个“EQ”值相匹配，但与任何“NE”值都不匹配时，该准则就得到了满足。

示例标准：`"EQ,NorthAmerica,Asia,NE,Europe"`

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
指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如完全 qualified domain name（FQDN）、主机名或NETBIOS名称。

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
指定策略如何处理多个标准。该参数的可接受值如下：

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
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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

### -Disable
表示此 cmdlet 会禁用该策略。如果您不指定此参数，cmdlet 会创建该策略并启用它。

```yaml
Type: SwitchParameter
Parameter Sets: Server, Zone
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InputObject
指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给此 cmdlet。

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
指定互联网协议（IP协议）的相关标准。有效的值有：IPv4 和 IPv6。请按照以下格式来指定相应的标准：

操作符，值01，值02，……，操作符，值03，值04，……

运算符只能是“EQ”（等于）或“NE”（不等于）。在一个条件中，每种运算符最多只能使用一次。

该策略将遵循“EQ”（等于）运算符的值视为多个断言，并将这些断言在逻辑上进行组合（使用“OR”操作）。同样地，该策略也将遵循“NE”（不等于）运算符的值视为多个断言，并在这些断言之间进行逻辑比较（使用“AND”操作）。只有当区域传输的IP地址与某个“EQ”值匹配，但不与任何“NE”值匹配时，才满足该条件。

示例标准：`"EQ,IPv4"` 和 `"EQ,IPv6"`

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
为新策略指定一个名称。

```yaml
Type: String
Parameter Sets: Server, Zone
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
用于指定策略的优先级。整数值越大，优先级越低。默认情况下，此cmdlet添加的新策略具有最低的优先级。

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

### -ServerInterfaceIP
指定DNS服务器监听的服务器接口的IP地址。请按照以下格式提供相应的信息：

操作符，值01，值02，……，操作符，值03，值04，……

运算符只能是“EQ”（等于）或“NE”（不等于）。在条件中，每个类型的运算符最多只能指定一个。

该策略将遵循“EQ”运算符的值视为多个断言，并将这些断言在逻辑上进行组合（使用“OR”操作）。同样地，该策略也将遵循“NE”运算符的值视为多个断言，并在这些断言之间进行逻辑判断（使用“AND”操作）。当接口的IP地址与某个“EQ”值匹配，但与任何“NE”值都不匹配时，则认为该标准得到了满足。

示例标准：`"EQ,10.0.0.1"` 和 `"NE,192.168.1.1"`

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
用于指定一天中的时间条件。请按照以下格式来指定条件：

操作符，值01，值02，……，操作符，值03，值04，……

运算符只能是“EQ”（等于）或“NE”（不等于）。在条件中，每个类型的运算符最多只能指定一个。

该策略将使用“EQ”运算符的值视为多个相互逻辑组合（通过“OR”连接）的断言；同时，也将使用“NE”运算符的值视为多个相互逻辑区分（通过“AND”连接）的断言。当区域转移发生的时间与某个“EQ”值匹配，但与任何“NE”值都不匹配时，该条件就被认为是满足的。

示例标准：`"EQ,10:00-12:00,22:00-23:00"`

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
指定传输协议的标准。有效值有：TCP 和 UDP。请按照以下格式指定标准：

操作符，值01，值02，……，操作符，值03，值04，……

运算符只能是 EQ（等于）或 NE（不等于）。在字符串中，每种运算符最多只能使用一次。

该策略将使用“EQ”运算符的值视为多个断言，并将这些断言在逻辑上进行组合（即使用“OR”操作）。同样，该策略也将使用“NE”运算符的值视为多个断言，并在这些断言之间进行逻辑上的区分（即使用“AND”操作）。当区域传输的协议与某个“EQ”值匹配，但与任何“NE”值都不匹配时，则认为该条件得到满足。

示例标准：`"EQ,TCP,NE,UDP"`

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
展示了如果该cmdlet运行会发生什么情况。但实际上并没有运行这个cmdlet。

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
指定一个DNS区域的名称，该cmdlet将在该区域上创建区域级别的策略。该区域必须存在于DNS服务器上。

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

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerPolicy

## 备注

## 相关链接

[Get-DnsServerZoneTransferPolicy](./Get-DnsServerZoneTransferPolicy.md)

[Remove-DnsServerZoneTransferPolicy](./Remove-DnsServerZoneTransferPolicy.md)

[Set-DnsServerZoneTransferPolicy](./Set-DnsServerZoneTransferPolicy.md)

[Start-DnsServerZoneTransfer](./Start-DnsServerZoneTransfer.md)

[Add-DnsServerClientSubnet](./Add-DnsServerClientSubnet.md)

[Add-DnsServerQueryResolutionPolicy](./Add-DnsServerQueryResolutionPolicy.md)

