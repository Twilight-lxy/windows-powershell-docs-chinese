---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerQueryResolutionPolicy_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 01/03/2022
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserverqueryresolutionpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerQueryResolutionPolicy
---

# Add-DnsServerQueryResolutionPolicy

## 摘要
为DNS服务器添加一个用于查询解析的策略。

## 语法

### 服务器（默认设置）
```
Add-DnsServerQueryResolutionPolicy [-PassThru] [-ComputerName <String>] [-Name] <String> [-Fqdn <String>]
 [-ECS <String>] [-ClientSubnet <String>] [-TimeOfDay <String>] [-TransportProtocol <String>] [-InternetProtocol <String>]
 [[-Action] <String>] [-ApplyOnRecursion] [-ServerInterfaceIP <String>] [-QType <String>]
 [-ProcessingOrder <UInt32>] [[-Condition] <String>] [-RecursionScope <String>] [-Disable]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 区域（Zone）
```
Add-DnsServerQueryResolutionPolicy [-PassThru] [-ComputerName <String>] [-ZoneName] <String> [-Name] <String>
 [-Fqdn <String>] [-ECS <String>] [-ClientSubnet <String>] [-TimeOfDay <String>] [-TransportProtocol <String>]
 [-InternetProtocol <String>] [[-Action] <String>] [-ServerInterfaceIP <String>] [-QType <String>]
 [-ProcessingOrder <UInt32>] [[-Condition] <String>] [-Disable] [-ZoneScope <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject
```
Add-DnsServerQueryResolutionPolicy [-PassThru] [-ComputerName <String>] [-InputObject] <CimInstance>
 [[-ZoneName] <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-DnsServerQueryResolutionPolicy` cmdlet 用于为域名系统（DNS）服务器添加查询解析策略。该策略根据您在策略中指定的标准来确定查询的解析方式。

一项政策包括标准、行动和范围三个要素。

这些标准是客户端子网、服务器接口IP地址、完全限定域名（FQDN）、互联网协议（IPv4/IPv6）、传输协议（UDP/TCP）、时间以及查询类型等要素的逻辑组合。

请按照以下格式指定标准：

操作符，值01，值02，……；操作符，值03，值04，……

运算符只能是 EQ（等于）或 NE（不等于）。在一条标准中，每种运算符最多只能指定一个。

该策略将紧跟在“EQ”运算符后的值视为多个断言，并将这些断言在逻辑上进行组合（使用“OR”操作）。同样地，该策略也将紧跟在“NE”运算符后的值视为多个断言，并在这些断言之间进行逻辑上的差异判断（使用“AND”操作）。

此cmdlet通过使用*Condition*参数的值作为逻辑运算符来结合多个条件。该参数可以取以下值之一：

- OR.
The policy evaluates criteria as multiple assertions which are logically combined (OR'd).
- AND.
The policy evaluates criteria as multiple assertions which are logically differenced (AND'd).

如果某个查询符合某项策略的规定，那么该策略所要求的响应动作就会随之发生。你可以选择允许（ALLOW）、拒绝（DENY）或忽略（IGNORE）。

如果您在为某个服务器制定的策略中指定了“ALLOW”操作（该服务器具有查询的权威处理能力），那么该策略将决定使用哪些区域范围来响应查询以及使用这些范围的比率。如果查询的结果已被缓存，策略会进一步确定使用哪些缓存范围及其使用比例；否则，策略会决定使用哪种递归范围来进行处理。

你可以在服务器级别或区域级别创建用于查询解析的策略。服务器级别的策略适用于所有发送到 DNS 服务器的查询；而区域级别的策略仅适用于那些可以从 DNS 服务器托管的区域中解析出来的查询。服务器级别的策略可以应用于传入的查询，也可以应用于递归输出的查询。对于传入的查询，服务器级别的策略只能执行“拒绝”（DENY）或“忽略”（IGNORE）操作。服务器级别策略最常见的用途是实现黑名单或白名单功能。

递归策略是一类特殊的服务器级策略。它们用于控制DNS服务器在处理查询时如何执行递归操作。递归策略仅在查询处理过程中到达递归路径时才会生效。您可以为一组查询选择“DENY”或“IGNORE”作为递归响应方式；或者，您也可以为这些查询指定一组转发器来替代递归功能。要配置这种行为，请在递归策略中明确指定递归的范围。利用递归策略可以实现“分裂脑”（Split-brain）DNS配置方案：在这种方案下，DNS服务器会对某些客户端执行递归操作，而对其他客户端则不执行递归处理。

区域级别策略适用于您创建它们的该区域。只有当查询过程中找到该区域时，这些策略才会生效。没有对应的区域，您无法创建区域级别策略；如果您删除某个区域，与该区域关联的所有区域级别策略也会随之被删除。在区域级别策略中，您可以指定针对某一区域内记录的一组查询应采用“DENY”或“IGNORE”这两种处理方式之一。另外，如果策略设置为“Allow”，则可以决定使用哪些区域范围来响应查询以及使用的具体比例。这类区域级别策略的一个应用场景是通过DNS实现应用程序负载均衡。

DNS服务器首先应用服务器级别的策略（递归策略除外），然后应用区域级别的策略，最后再应用递归策略。每种策略都具有优先级值。您可以使用*ProcessingOrder*参数来指定这些策略的优先级顺序。DNS服务器会根据每种策略的优先级顺序来处理查询请求。

如果服务器级别策略的条件与某个查询相匹配，并且该策略规定的操作是“DENY”（拒绝），那么DNS服务器会返回“REFUSED”（拒绝响应）。如果策略规定的操作是“IGNORE”（忽略），则DNS服务器会直接丢弃该查询。如果某个查询不符合任何服务器级别的策略，但该服务器是对应区域的权威DNS服务器，那么服务器会根据区域级别的策略来处理该查询。

如果某个区域级别策略中的条件与查询相匹配，并且该策略的响应动作是“DENY”（拒绝），那么服务器会返回“REFUSED”（拒绝）作为响应。如果响应动作是“IGNORE”（忽略），则服务器会直接丢弃该查询；如果响应动作是“ALLOW”（允许），DNS服务器会从策略中指定的某个区域范围内响应该查询。你可以选择按照特定的比例来分配来自不同区域范围的响应结果。

在策略处理过程中，缓存被视为一个区域（zone）。DNS服务器会对缓存的区域级策略重复执行相应的处理流程。

如果接收查询的服务器对该区域没有权威解析能力（即该服务器无法为该区域提供正确的DNS响应），并且查询结果既不在缓存中，也不在指定的缓存范围内找到，那么DNS服务器会按照递归策略的优先级顺序来处理该查询。  
- 如果某个递归策略的条件与查询内容匹配，并且其配置的动作是“DENY”（拒绝），则DNS服务器会返回“REFUSED”作为响应；  
- 如果动作是“IGNORE”（忽略），DNS服务器会直接放弃对该查询的处理；  
- 如果动作是“ALLOW”（允许），DNS服务器会从已配置的递归范围内获取相应的设置，并根据这些设置通过递归方式来获取查询结果。

## 示例

#### 示例 1：创建流量管理策略
```
The first two commands create client subnets by using the **Add-DnsServerClientSubnet** cmdlet. The client subnets are for clients in North America and clients in Europe.
PS C:\> Add-DnsServerClientSubnet -Name "NorthAmericaSubnet" -IPv4Subnet "172.21.33.0/24" -PassThru
PS C:\> Add-DnsServerClientSubnet -Name "EuropeSubnet" -IPv4Subnet "172.17.44.0/24" -PassThru
Name                                             IPV4Subnet                                       IPV6Subnet
----                                             ----------                                       ----------
NorthAmericaSubnet                                    {172.21.33.0/24}
EuropeSubnet                                     {172.17.44.0/24}

The next two commands create zone scopes for North America and for Europe by using the **Add-DnsServerZoneScope** cmdlet.
PS C:\> Add-DnsServerZoneScope -ZoneName "Contoso.com" -Name "NorthAmericaZoneScope" -PassThru
PS C:\> Add-DnsServerZoneScope -ZoneName "Contoso.com" -Name "EuropeZoneScope" -PassThru
FileName       : NorthAmericaZoneScope.dns
ZoneName       : contoso.com
ZoneScope      : NorthAmericaZoneScope
PSComputerName :


FileName       : EuropeZoneScope.dns
ZoneName       : contoso.com
ZoneScope      : EuropeZoneScope
PSComputerName :

The next two commands add resource records for the zone Contoso.com by using the **Add-DnsServerResourceRecord** cmdlet. The name for both records is the same, career, but the two records point to different addresses. The records also have different scopes.
PS C:\> Add-DnsServerResourceRecord -ZoneName "Contoso.com" -A -Name "career" -IPv4Address "172.17.97.97" -ZoneScope "EuropeZoneScope" -PassThru
PS C:\> Add-DnsServerResourceRecord -ZoneName "Contoso.com" -A -Name "career" -IPv4Address "172.21.21.21" -ZoneScope "NorthAmericaZoneScope" -PassThru
DistinguishedName : career
HostName          : career
RecordClass       : IN
RecordData        : DnsServerResourceRecordA
RecordType        : A
Timestamp         :
TimeToLive        : 01:00:00
PSComputerName    :


DistinguishedName : career
HostName          : career
RecordClass       : IN
RecordData        : DnsServerResourceRecordA
RecordType        : A
Timestamp         :
TimeToLive        : 01:00:00
PSComputerName    :

The final two commands create two policies. The policies allow queries for members of different subnets. The policies differ in scope, so that some clients receive one response to a query, while other clients receive a different response to the same query.
PS C:\> Add-DnsServerQueryResolutionPolicy -Name "NorthAmericaPolicy" -Action ALLOW -ClientSubnet "eq,NorthAmericaSubnet" -ZoneScope "NorthAmericaZoneScope,1" -ZoneName "Contoso.com" -PassThru
PS C:\> Add-DnsServerQueryResolutionPolicy -Name "EuropePolicy" -Action ALLOW -ClientSubnet "eq,EuropeSubnet" -ZoneScope "EuropeZoneScope,1" -ZoneName contoso.com -PassThru
Action          : Allow
AppliesOn       : QueryProcessing
Condition       : And
Content         : {DnsServerPolicyContent}
Criteria        : {DnsServerPolicyCriteria}
IsEnabled       : True
Level           : Zone
Name            : NorthAmericaPolicy


ProcessingOrder : 1
ZoneName        : contoso.com
PSComputerName  :


Action          : Allow
AppliesOn       : QueryProcessing
Condition       : And
Content         : {DnsServerPolicyContent}
Criteria        : {DnsServerPolicyCriteria}
IsEnabled       : True
Level           : Zone
Name            : EuropePolicy
ProcessingOrder : 2
ZoneName        : contoso.com
PSComputerName  :
```

这个示例展示了如何创建流量管理策略，以将来自某个子网的客户引导至北美数据中心，将来自另一个子网的客户引导至欧洲数据中心。

### 示例 2：允许对某个区域进行查询
```
PS C:\> Add-DnsServerQueryResolutionPolicy -Name "LBPolicy" -ZoneName "contoso.com" -Action ALLOW -FQDN "EQ,career.contoso.com" -ZoneScope "NorthAmericaZoneScope,7;EuropeZoneScope,3" -PassThru
Name                                               ProcessingOrder                                    IsEnabled                                         Action
----                                               ---------------                                    ---------                                         ------
LBPolicy                                           3                                                  True                                              Allow
```

这个命令创建了一个名为 LBPolicy 的策略，用于允许对 contoso.com 区域的查询。该策略包含了两个带有权重的区域范围（weighted zone scopes）。

### 示例 3：将一个服务器上的策略添加到另一个服务器上
```
PS C:\> $Policies = Get-DnsServerQueryResolutionPolicy -ComputerName "Server01"
PS C:\> $Policies | Add-DnsServerQueryResolutionPolicy -ComputerName "Server07" -ThrottleLimit 1
```

第一个命令获取名为Server01的DNS服务器上的所有服务器级策略，并将这些策略的属性存储在$Policies变量中。

第二个命令将存储在 `$Policies` 中的策略添加到另一台 DNS 服务器上。该命令为 `*ThrottleLimit*` 参数指定了值 1（one）。这个值用于保持策略在处理流程中的顺序不变。

### 示例 4：针对某个域名的阻止查询
```
PS C:\> Add-DnsServerQueryResolutionPolicy -Name "BlackholePolicy" -Action IGNORE -FQDN "EQ,*.contoso.com" -PassThru | Format-List *
Action                : Ignore
AppliesOn             : QueryProcessing
Condition             : And
Content               :
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Server
Name                  : BlackholePolicy
ProcessingOrder       : 1
ZoneName              :
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties
```

此命令创建一个策略，用于阻止来自特定域的查询。该命令使用 **Format-List** cmdlet 来控制输出的外观。有关更多信息，请输入 `Get-Help Format-List`。

#### 示例 5：阻止来自子网的查询
```
PS C:\> Add-DnsServerClientSubnet -Name "MaliciousSubnet06" -IPv4Subnet 172.0.33.0/24 -PassThru
PS C:\> Add-DnsServerQueryResolutionPolicy -Name "BlackholePolicyMalicious06" -Action IGNORE -ClientSubnet  "EQ,MaliciousSubnet06" -PassThru | Format-List *
Action                : Ignore
AppliesOn             : QueryProcessing
Condition             : And
Content               :
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Server
Name                  : BlackholePolicyMalicious
ProcessingOrder       : 2
ZoneName              :
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties
```

第一个命令创建了一个名为 MaliciousSubnet06 的客户端子网。

第二个命令创建了一个策略，用于阻止来自名为“MaliciousSubnet06”的子网的查询。该策略采取的动作是“IGNORE”（忽略），即直接丢弃这些查询请求。

### 示例 6：阻止某种类型的查询
```
PS C:\> Add-DnsServerQueryResolutionPolicy -Name "BlackholePolicyQType" -Action IGNORE -QType "EQ,ANY" -PassThru | Format-List *
Action                : Ignore
AppliesOn             : QueryProcessing
Condition             : And
Content               :
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Server
Name                  : BlackholePolicyQType
ProcessingOrder       : 3
ZoneName              :
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties
```

此命令创建了一个策略，用于阻止针对特定查询类型的请求。该策略会拒绝所有此类请求（即“删除”所有相关请求）。

### 示例 7：允许内部客户端进行递归调用
```
PS C:\> Add-DnsServerRecursionScope -Name "InternalClients" -EnableRecursion $True
PS C:\> Set-DnsServerRecursionScope -Name . -EnableRecursion $False
PS C:\> Add-DnsServerQueryResolutionPolicy -Name "SplitBrainPolicy" -Action ALLOW -ApplyOnRecursion -RecursionScope "InternalClients" -ServerInterfaceIP  "EQ,10.0.0.34" -PassThru
Action          : Allow
AppliesOn       : Recursion
Condition       : And
Content         : {DnsServerPolicyContent}
Criteria        : {DnsServerPolicyCriteria}
IsEnabled       : True
Level           : Server
Name            : SplitBrainPolicy
ProcessingOrder : 1
ZoneName        :
PSComputerName  :
```

第一个命令创建了一个名为“InternalClients”的递归作用域，并为该作用域启用了递归功能。

第二个命令使用 **Set-DnsServerRecursionScope** cmdlet 来修改默认的递归范围。默认的递归范围用点（.）表示，该范围内的递归功能是禁用的。

最后一个命令创建了一条使用 `InternalClients` 作用域的策略。对于这个作用域，在指定的服务器接口地址上，该策略允许递归操作。

## 参数

### -Action
指定当查询与该策略匹配时应执行的操作。此参数的可接受值包括：

- ALLOW.
- DENY.
Respond with SERV_FAIL.
- IGNORE.
Do not respond.

```yaml
Type: String
Parameter Sets: Server, Zone
Aliases:
Accepted values: ALLOW, DENY, IGNORE

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ApplyOnRecursion
表示此策略是服务器级别的递归策略。

递归策略是一类特殊的服务器级策略，用于控制DNS服务器如何对查询执行递归处理。递归策略仅在查询处理过程中进入递归路径时才会生效。

```yaml
Type: SwitchParameter
Parameter Sets: Server
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` 系列的 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
指定客户端子网的条件。该子网是用于发送查询的客户端所在的网络环境。有关更多信息，请参阅 **Add-DnsServerClientSubnet**。请按照以下格式指定条件：

操作符，值01，值02，……；操作符，值03，值04，……

运算符只能是 EQ（等于）或 NE（不等于）。在一条标准中，每种运算符最多只能指定一个。

该策略将遵循“EQ”（等于）运算符的值视为多个断言，这些断言在逻辑上是组合在一起的（使用“OR”操作）。同样地，遵循“NE”（不等于）运算符的值也被视为多个断言，但这些断言在逻辑上是相互排斥的（使用“AND”操作）。当请求中的子网与某个“EQ”值匹配，但与任何“NE”值都不匹配时，则认为该条件得到满足。

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
指定策略如何处理多个标准（即多个条件）。该参数的可接受值为：

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
在运行该cmdlet之前，会提示您确认是否要执行该操作。

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
表示此cmdlet会禁用该策略。如果您不指定此参数，cmdlet将创建该策略并启用它。

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
指定 FQDN（完全 Qualified Domain Name）的标准。这是查询中的记录对应的 FQDN。请按照以下格式指定标准：

操作符，值01，值02，……；操作符，值03，值04，……

运算符只能是“EQ”（等于）或“NE”（不等于）。每个标准最多只能指定一个这样的运算符。

该策略将使用“EQ”运算符的值视为多个断言，并将这些断言在逻辑上进行组合（使用“OR”操作）。同样地，该策略也将使用“NE”运算符的值视为多个断言，并对这些断言在逻辑上进行区分（使用“AND”操作）。如果请求的完全限定域名（FQDN）与某个“EQ”值匹配，但与任何“NE”值都不匹配，则满足该条件。您可以使用星号（*）作为通配符。例如：`EQ,*.contoso.com,NE,*.fabrikam.com`。

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
指定要传递给此cmdlet的输入数据。你可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

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
指定互联网协议（IP）的相关标准。这是查询中涉及的IP版本。有效值包括：IPv4 和 IPv6。请按照以下格式来指定相应的标准：

操作符，值01，值02，……；操作符，值03，值04，……

运算符只能是 EQ（等于）或 NE（不等于）。在一条标准中，每种运算符最多只能指定一个。

该策略将遵循“EQ”（等于）运算符的值视为多个断言，并将这些断言在逻辑上进行组合（使用“OR”运算）。同样地，该策略将遵循“NE”（不等于）运算符的值也视为多个断言，并在这些断言之间进行逻辑比较（使用“AND”运算）。当请求的 IP 地址与某个“EQ”值匹配，但与任何“NE”值都不匹配时，就满足了该规则的要求。

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
返回一个表示您正在操作的该项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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
用于指定策略的优先级。整数值越大，优先级越低。默认情况下，此cmdlet添加的策略具有最低的优先级。

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
指定查询类型的标准。这表示正在被查询的记录类型。请按照以下格式指定标准：

操作符，值01，值02，……；操作符，值03，值04，……

运算符只能是 EQ（等于）或 NE（不等于）。在一条标准中，每种运算符最多只能指定一个。

该策略将使用“EQ”运算符的值视为多个断言，并将这些断言在逻辑上进行组合（即使用“OR”操作）。同样，该策略将使用“NE”运算符的值也视为多个断言，并在这些断言之间进行逻辑上的差异判断（即使用“AND”操作）。当请求的查询类型与某个“EQ”值匹配，但与任何“NE”值都不匹配时，则认为该准则得到了满足。

示例标准：`"EQ,TXT,SRV;NE,MX"`

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
指定递归的范围。如果该策略是一个递归策略，并且某个查询与该策略匹配，则DNS服务器会使用此范围内的设置来执行对该查询的递归处理。

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
指定DNS服务器监听的服务器接口的IP地址。请按照以下格式提供相应的参数：

操作符，值01，值02，……；操作符，值03，值04，……

运算符只能是 EQ（等于）或 NE（不等于）。在条件中，每种运算符最多只能指定一个。

该策略将使用 EQ（等于）运算符的值视为多个断言，并将这些断言在逻辑上进行组合（使用 OR 运算）。同样，该策略也将使用 NE（不等于）运算符的值视为多个断言，并在这些断言之间进行逻辑上的比较（使用 AND 运算）。当接口的 IP 地址与某个 EQ 值相匹配，但与任何 NE 值都不匹配时，则认为该标准得到满足。

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
指定一天中的时间标准，即服务器接收查询的时间。请按照以下格式指定该标准：

操作符，值01，值02，……；操作符，值03，值04，……

运算符只能是 EQ（等于）或 NE（不等于）。在条件中，每种运算符最多只能指定一个。

该策略将遵循“EQ”（等于）运算符的值视为多个逻辑上组合在一起的断言（即使用“OR”进行连接）。同样，该策略也将遵循“NE”（不等于）运算符的值视为多个逻辑上相异的断言（即使用“AND”进行连接）。当请求的时间与某个“EQ”值匹配，但与任何“NE”值都不匹配时，就认为满足了该条件。

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
指定传输协议的标准。这是查询所使用的传输协议。有效值为：TCP 和 UDP。请按照以下格式指定标准：

操作符，值01，值02，……；操作符，值03，值04，……

运算符只能是“EQ”（等于）或“NE”（不等于）。在字符串中，每种运算符最多只能使用一次。

该策略将使用“EQ”运算符的值视为多个断言，并将这些断言在逻辑上进行组合（即使用“OR”操作）。同样地，该策略也将使用“NE”运算符的值视为多个断言，并在这些断言之间进行逻辑上的比较（即使用“AND”操作）。只有当请求的传输协议与某个“EQ”值匹配，但不与任何“NE”值匹配时，才能认为该条件得到满足。

示例标准：`"EQ,TCP"` 和 `"NE,UDP"`

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
指定一个DNS区域的名称，此cmdlet将在该区域上创建区域级策略。该区域必须存在于DNS服务器上。

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
指定该区域的权限范围（scopes）和权重（weights）列表。请以以下格式将数值作为字符串来输入：

Scope01，Weight01；Scope02，Weight02；

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerPolicy

## 备注

## 相关链接

[Get-DnsServerQueryResolutionPolicy](./Get-DnsServerQueryResolutionPolicy.md)

[Remove-DnsServerQueryResolutionPolicy](./Remove-DnsServerQueryResolutionPolicy.md)

[Set-DnsServerQueryResolutionPolicy](./Set-DnsServerQueryResolutionPolicy.md)

[Add-DnsServerClientSubnet](./Add-DnsServerClientSubnet.md)

[Add-DnsServerZoneScope](./Add-DnsServerZoneScope.md)

[Add-DnsServerResourceRecord](./Add-DnsServerResourceRecord.md)

[Set-DnsServerRecursionScope](./Set-DnsServerRecursionScope.md)

[Add-DnsServerZoneTransferPolicy](./Add-DnsServerZoneTransferPolicy.md)

