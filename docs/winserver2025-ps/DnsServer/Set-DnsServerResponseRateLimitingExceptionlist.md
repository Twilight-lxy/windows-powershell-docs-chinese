---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerResponseRateLimitingExceptionlist_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverresponseratelimitingexceptionlist?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerResponseRateLimitingExceptionlist
---

# Set-DnsServerResponseRateLimitingExceptionlist

## 摘要
更新 RRL 异常列表的设置。

## 语法

```
Set-DnsServerResponseRateLimitingExceptionlist [[-ClientSubnet] <String>] [[-Fqdn] <String>]
 [[-ServerInterfaceIP] <String>] [[-Name] <String>] [[-Condition] <String>] [-ComputerName <String>]
 [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-DnsServerResponseRateLimitingExceptionlist` cmdlet 用于更新响应速率限制（Response Rate Limiting，简称 RRL）异常列表的设置。

## 示例

### 示例 1：设置 RRL 异常列表
```
PS C:\> Set-DnsServerResponseRateLimitingExceptionlist -Name "SafeList1" -ServerInterfaceIP "EQ,10.0.0.1"
```

该命令将名为SafeList1的RRL异常列表中的**ServerInterfaceIP**值设置为EQ,10.0.0.1。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，随后会显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定异常列表中客户端子网的值。

该值的格式必须如下：`COMPARATOR, value1, value2,..., COMPARATOR, value3, value4,...`，其中 `COMparator` 可以是 `EQ` 或 `NE`。在一个值中只能包含一个 `EQ` 和一个 `NE`。

在EQ运算符后面的值将被视为多个断言，并使用OR运算符进行逻辑组合。在NE运算符后面的值也将被视为多个断言，并使用AND运算符进行逻辑判断（即判断这些值之间是否存在差异）。

多个值是通过使用 *Condition* 参数（作为逻辑运算符）来组合的。在同一参数内，也可以使用相同的运算符来组合 EQ 和 NE 表达式。

例如，`EQ, America, Asia, NE, Europe` 表示：美洲和亚洲地区的客户端子网被列入例外列表中，而欧洲地区的客户端子网则不在例外列表中。

有关详细信息，请参阅 **Add-DnsServerClientSubnet**。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定用于运行该命令的远程 DNS 服务器。您可以指定一个 IP 地址，或者任何能够解析为 IP 地址的值，例如完全限定域名（FQDN）、主机名或 NetBIOS 名称。

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
用于指定一个逻辑运算符，以组合 **ClientSubnet**、**Fqdn** 和 **ServerIp** 参数的多个值。这些参数的值是通过使用 *Condition* 参数作为逻辑运算符来合并在一起的。相同的运算符也用于在同一值内合并 EQ（等于）和 NE（不等于）表达式。默认值为 AND。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: AND, OR

Required: False
Position: 5
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

### -Fqdn
为异常列表指定FQDN（完全 Qualified Domain Name）值。

该值的格式必须如下：`COMPARATOR, value1, value2,..., COMPARATOR, value3, value4,...`，其中 `COMparator` 可以是 `EQ` 或 `NE`。在一个值中只能包含一个 `EQ` 和一个 `NE`。

在EQ运算符后面的值将被视为多个断言，并使用OR运算符进行逻辑组合。在NE运算符后面的值也将被视为多个断言，并使用AND运算符进行逻辑判断（即判断这些值之间是否存在差异）。

多个值是通过使用 *Condition* 参数（作为逻辑运算符）来组合的。在同一参数内，也可以使用相同的运算符来组合 EQ 和 NE 表达式。

例如，`EQ,*.contoso.com` 表示应该将 contoso.com 域名添加到例外列表中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定 RRL 异常列表的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
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

### -ServerInterfaceIP
指定DNS服务器正在监听的服务器接口。

该值的格式必须如下：`COMPARATOR, value1, value2,..., COMPARATOR, value3, value4,...`，其中 `COMparator` 可以是 `EQ` 或 `NE`。在一个值中只能包含一个 `EQ` 和一个 `NE`。

在EQ运算符后面的值将被视为多个断言，并使用OR运算符进行逻辑组合。在NE运算符后面的值也将被视为多个断言，并使用AND运算符进行逻辑判断（即判断这些值之间是否存在差异）。

多个值通过使用 `*Condition` 参数作为逻辑运算符来组合在一起。同一个运算符也用于在单个值内部组合 `EQ`（等于）和 `NE`（不等于）表达式。

例如，`EQ,10.0.0.3` 指定了一个服务器接口，其 IP 地址为 10.0.0.3。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM コマンド的数量来计算该コマンド的最佳限制值。该限制仅适用于当前正在运行的コマンド，而不适用于整个会话或计算机本身。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerResponseRateLimitingException
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DnsServerResponseRateLimitingExceptionlist](./Add-DnsServerResponseRateLimitingExceptionlist.md)

[Get-DnsServerResponseRateLimitingExceptionlist](./Get-DnsServerResponseRateLimitingExceptionlist.md)

[Set-DnsServerResponseRateLimiting](./Set-DnsServerResponseRateLimiting.md)

