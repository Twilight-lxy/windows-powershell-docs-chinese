---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerResponseRateLimitingExceptionlist_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserverresponseratelimitingexceptionlist?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerResponseRateLimitingExceptionlist
---

# Add-DnsServerResponseRateLimitingExceptionlist

## 摘要
在DNS服务器上添加一个RRL（Reverse Look-Up List，反向查找列表）异常列表。

## 语法

```
Add-DnsServerResponseRateLimitingExceptionlist [[-ClientSubnet] <String>] [[-Fqdn] <String>]
 [[-ServerInterfaceIP] <String>] [[-Name] <String>] [[-Condition] <String>] [-PassThru]
 [-ComputerName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-DnsServerResponseRateLimiting` cmdlet 用于在 DNS 服务器上添加响应速率限制（Response Rate Limiting，简称 RRL）的例外列表。该例外列表表示：针对特定完全限定域名（Fully Qualified Domain Names，简称 FQDN）的查询、来自指定客户端子网的查询、在指定服务器接口接收到的查询，或者这些情况的任意组合所产生的响应，均不受 RRL 约束（即不会被限制响应速率）。

## 示例

### 示例 1：将一个域名添加到 RRL 异常列表中
```
PS C:\> Add-DnsServerResponseRateLimitingExceptionlist -Name "SafeList1" -Fqdn "EQ,*.contoso.com"
```

此命令为域名 contoso.com 添加了一个 RRL（Reverse Lookup List）异常规则。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后会显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定异常列表中的客户端子网值。

此参数必须采用以下格式：`COMparator, value1, value2,..., COMPARATOR, value3, value4,...`，其中 `COMparator` 可以是 `EQ` 或 `NE`。每个值中最多只能包含一个 `EQ` 和一个 `NE`。

EQ运算符后面的值将被视为多个断言，这些断言通过OR运算符进行逻辑组合。NE运算符后面的值也将被视为多个断言，这些断言通过AND运算符进行逻辑判断（即判断它们之间是否存在差异）。

多个值是通过使用 *Condition* 参数作为逻辑运算符来组合的。这个相同的运算符也用于在一个值内部组合 EQ（等于）和 NE（不等于）表达式。

例如，`EQ, America, Asia, NE, Europe` 表示：美洲和亚洲的客户端子网被包含在例外列表中，而欧洲的客户端子网则不在例外列表中。

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
指定一个用于运行命令的远程 DNS 服务器。您可以指定一个 IP 地址，或者任何能够解析为 IP 地址的值，例如完全合格的域名（FQDN）、主机名或 NetBIOS 名称。

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
用于指定一个逻辑运算符，以组合 **ClientSubnet**、**Fqdn** 和 **ServerIp** 参数的多个值。这些参数的值是使用 *Condition* 参数作为逻辑运算符进行合并的；相同的运算符也用于在一个值内部合并 EQ（等于）和 NE（不等于）表达式。默认值为 AND。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: AND, OR

Required: False
Position: 5
Default value: None
Accept pipeline input: True (ByPropertyName)
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

### -Fqdn
为异常列表指定 FQDN 值。

该值的格式必须如下：`COMparator, value1, value2,..., COMPARATOR, value3, value4,...`，其中 `COMPARATOR` 可以是 `EQ` 或 `NE`。在一个值中只能包含一个 `EQ` 和一个 `NE`。

EQ运算符后面的值将被视为多个断言，这些断言通过OR运算符进行逻辑组合。NE运算符后面的值也将被视为多个断言，这些断言通过AND运算符进行逻辑判断（即判断它们之间是否存在差异）。

多个值是通过使用 *Condition* 参数作为逻辑运算符来组合的。这个相同的运算符也用于在一个值内部组合 EQ（等于）和 NE（不等于）表达式。

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

### -ServerInterfaceIP
指定DNS服务器正在监听的服务器接口。

该值的格式必须如下：`COMparator, value1, value2,..., COMPARATOR, value3, value4,...`，其中 `COMPARATOR` 可以是 `EQ` 或 `NE`。在一个值中只能包含一个 `EQ` 和一个 `NE`。

紧跟在“EQ”操作符后面的值被视为多个断言，这些断言通过“OR”操作符进行逻辑组合。紧跟在“NE”操作符后面的值同样被视为多个断言，但这些断言是通过“AND”操作符进行逻辑比较的（即判断它们之间是否存在差异）。

多个值是通过使用 *Condition* 参数作为逻辑运算符来组合的。这个相同的运算符也用于在一个值内部组合 EQ（等于）和 NE（不等于）表达式。

例如，`EQ,10.0.0.3` 表示所有通过 IP 地址为 10.0.0.3 的服务器接口接收到的查询都应该被免除 RRL（Rate Limiting）的限制。

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
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值为`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。此限制仅适用于当前执行的cmdlet，而不适用于整个会话或计算机本身。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerResponseRateLimitingException列表
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名称。

## 备注

## 相关链接

[Add-DnsServerClientSubnet](./Add-DnsServerClientSubnet.md)

[Get-DnsServerResponseRateLimitingExceptionlist](./Get-DnsServerResponseRateLimitingExceptionlist.md)

[Set-DnsServerResponseRateLimiting](./Set-DnsServerResponseRateLimiting.md)

[Set-DnsServerResponseRateLimitingExceptionlist](./Set-DnsServerResponseRateLimitingExceptionlist.md)

