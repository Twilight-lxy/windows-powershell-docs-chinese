---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerZoneTransferPolicy_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverzonetransferpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerZoneTransferPolicy
---

# Set-DnsServerZoneTransferPolicy

## 摘要
更新DNS服务器上的区域传输策略。

## 语法

### 服务器（默认设置）
```
Set-DnsServerZoneTransferPolicy [-PassThru] [-ComputerName <String>] [-ClientSubnet <String>]
 [-Condition <String>] [-InternetProtocol <String>] [-Name] <String> [-ProcessingOrder <UInt32>]
 [-ServerInterfaceIP <String>] [-TimeOfDay <String>] [-TransportProtocol <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 区域（Zone）
```
Set-DnsServerZoneTransferPolicy [-PassThru] [-ComputerName <String>] [-ZoneName] <String>
 [-ClientSubnet <String>] [-Condition <String>] [-InternetProtocol <String>] [-Name] <String>
 [-ProcessingOrder <UInt32>] [-ServerInterfaceIP <String>] [-TimeOfDay <String>] [-TransportProtocol <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject
```
Set-DnsServerZoneTransferPolicy [-PassThru] [-ComputerName <String>] [-InputObject] <CimInstance>
 [[-ZoneName] <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-DnsServerZoneTransferPolicy` cmdlet 用于更新域名系统（DNS）服务器上的区域传输策略。

## 示例

### 示例 1：更新区域传输策略
```
PS C:\> Set-DnsServerZoneTransferPolicy -Name "InternalTransfers" -TransportProtocol "NE,TCP" -ServerInterfaceIP $Null
```

这个命令用于更新名为“InternalTransfers”的区域传输策略。该命令修改了传输协议以及服务器接口IP地址的相关设置。对于服务器接口IP地址，命令使用了$Null作为值，从而取消了之前设定的筛选条件。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，随后会显示命令提示符。在作业完成期间，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

运算符只能是“EQ”（等于）或“NE”（不等于）。在一个条件中，每种运算符最多只能指定一个。

该策略将紧跟“EQ”（Equal）操作符后的值视为多个断言，并将这些断言进行逻辑组合（使用“OR”运算）。同样地，它也将紧跟“NE”（Not Equal）操作符后的值视为多个断言，并对这些断言进行逻辑区分（使用“AND”运算）。当区域传输的子网与某个“EQ”值匹配，但与任何“NE”值都不匹配时，该条件就得到满足。

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
用于指定远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的字符串，例如完全qualified domain name（FQDN）、主机名或NETBIOS名称。

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
指定策略如何处理多个标准。此参数的可接受值为：

- OR.
The policy evaluates criteria as multiple assertions which are logically combined (OR'd).
- AND.
The policy evaluates criteria as multiple assertions which are logically differenced (AND'd).

默认值为“AND”。

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
指定互联网协议（IP）的相关标准。请按照以下格式来指定该标准：

操作符，value01，value02，……，操作符，value03，value04，……

运算符只能是“EQ”（等于）或“NE”（不等于）。在一个条件中，每种运算符最多只能指定一个。

该策略将使用 EQ（等于）运算符的值视为多个断言，并将这些断言在逻辑上进行组合（使用 OR 运算）。同样，该策略也将使用 NE（不等于）运算符的值视为多个断言，并在这些断言之间进行逻辑上的区分（使用 AND 运算）。当区域传输的 IP 地址与某个 EQ 值相匹配，但与任何 NE 值都不匹配时，则满足该条件。

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
指定要更新的政策名称。

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
用于指定策略的优先级。整数数值越大，优先级越低。默认情况下，此cmdlet会添加一个优先级最低的新策略。

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
指定DNS服务器监听的服务器接口的IP地址。请按照以下格式提供相应的参数：

操作符，value01，value02，……，操作符，value03，value04，……

运算符只能是 EQ（等于）或 NE（不等于）。在条件中，每种运算符最多只能指定一个。

该策略将使用“EQ”运算符的值视为多个断言，并将这些断言在逻辑上进行组合（即使用“OR”操作）。同样，该策略将使用“NE”运算符的值也视为多个断言，并在这些断言之间进行逻辑上的区分（即使用“AND”操作）。只有当接口的IP地址与某个“EQ”值匹配，但不与任何“NE”值匹配时，才认为满足该条件。

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
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

运算符只能是 EQ（等于）或 NE（不等于）。在条件中，每种运算符最多只能指定一个。

该策略将遵循“EQ”运算符的值视为多个断言，这些断言在逻辑上是通过“OR”操作组合起来的；同样地，遵循“NE”运算符的值也被视为多个断言，但这些断言在逻辑上是通过“AND”操作组合起来的。当区域转移发生的时间与某个“EQ”值匹配，但与任何“NE”值都不匹配时，该条件就得到了满足。

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

该策略将使用“EQ”运算符的值视为多个断言，并将这些断言在逻辑上进行组合（使用“OR”操作）。同样，该策略也将使用“NE”运算符的值视为多个断言，并在这些断言之间进行逻辑上的区分（使用“AND”操作）。只有当区域传输的协议与某个“EQ”值匹配，但不与任何“NE”值匹配时，才满足这一标准。

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
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
指定包含区域级别策略的DNS区域的名称。该区域必须存在于DNS服务器上。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerPolicy

## 备注

## 相关链接

[Add-DnsServerZoneTransferPolicy](./Add-DnsServerZoneTransferPolicy.md)

[Get-DnsServerZoneTransferPolicy](./Get-DnsServerZoneTransferPolicy.md)

[Remove-DnsServerZoneTransferPolicy](./Remove-DnsServerZoneTransferPolicy.md)

[Start-DnsServerZoneTransfer](./Start-DnsServerZoneTransfer.md)

[Add-DnsServerQueryResolutionPolicy](./Add-DnsServerQueryResolutionPolicy.md)

