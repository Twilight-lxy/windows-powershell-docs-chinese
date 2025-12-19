---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamIpAuditEvent.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamipaddressauditevent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamIpAddressAuditEvent
---

# Get-IpamIpAddressAuditEvent

## 摘要
获取 IPAM 中的所有 IP 地址审计事件。

## 语法

### ByUserName
```
Get-IpamIpAddressAuditEvent -UserName <String[]> -StartDate <DateTime> -EndDate <DateTime>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 按 IP 地址
```
Get-IpamIpAddressAuditEvent -IpAddress <String> -StartDate <DateTime> -EndDate <DateTime>
 [-CorrelateLogonEvents] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 根据 ClientId 进行筛选
```
Get-IpamIpAddressAuditEvent -ClientId <String> -StartDate <DateTime> -EndDate <DateTime>
 [-CorrelateLogonEvents] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByHostName
```
Get-IpamIpAddressAuditEvent -HostName <String> -StartDate <DateTime> -EndDate <DateTime>
 [-CorrelateLogonEvents] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-IpamIpAddressAuditEvent` cmdlet 可以在指定的时间间隔内从 IP 地址管理 (IPAM) 服务器中获取所有与 IP 地址相关的审计事件。IPAM 通过将托管的 DHCP 服务器上的动态主机配置协议 (DHCP) 租用事件与托管的域控制器和网络策略服务器 (NPS) 上的用户及计算机身份验证事件进行关联，来实现对 IP 地址的跟踪。你可以根据 IP 地址、客户端 ID、主机名或用户名来搜索相关的审计事件。该 cmdlet 还允许你指定开始日期和结束日期，以便仅获取这两个时间范围内的数据；返回的数据会同时包含开始日期和结束日期的相关信息。

如果查询结果超过了 10,000 行，该 cmdlet 只会返回前 10,000 行。在这种情况下，cmdlet 会显示一个警告。如果你缩小搜索范围以限制结果数量，就可以避免这种情况的发生。

## 示例

### 示例 1：获取所有 IP 地址审计事件
```
PS C:\> $Today = Get-Date
PS C:\> $LastMonth = $Today.AddDays(-30)
PS C:\> $IpamIpAddressAuditEvents = Get-IpamIpAddressAuditEvent -StartDate $LastMonth -EndDate $Today
```

第一个命令获取当前日期，并将结果存储在名为 $Today 的变量中。第二个命令从 $Today 变量中减去 30 天，然后将结果存储在名为 $LastMonth 的变量中。第三个命令获取 $LastMonth 变量与 $Today 变量之间所有的 IP 地址审计事件；该命令仅收集 DHCP 租约相关的数据，并将结果存储在名为 $IpamIpAddressAuditEvents 的变量中。

### 示例 2：获取指定结束日期和开始日期之间的所有 IP 地址审计事件
```
PS C:\> $Today = Get-Date
PS C:\> $LastMonth = $Today.AddDays(-30)
PS C:\> $IpamIpAddressAuditEvents = Get-IpamIpAddressAuditEvent -StartDate $LastMonth -EndDate $Today -IpAddress 10.10.1.1
```

第一个命令获取当前日期，并将结果存储在名为 `$Today` 的变量中。第二个命令从 `$Today` 变量中减去 30 天，并将结果存储在名为 `$LastMonth` 的变量中。第三个命令获取指定 IP 地址在起始日期和结束日期之间的所有 IP 地址审计事件，并将结果存储在名为 `$IpamIpAddressAuditEvents` 的变量中。此命令仅搜索 DHCP 租约事件。

### 示例 3：获取指定结束日期和开始日期之间的所有 IP 地址审计事件、用户事件以及登录事件
```
PS C:\> $Today = Get-Date
PS C:\> $LastMonth = $Today.AddDays(-30)
PS C:\> $IpamIpAddressAuditEvents = Get-IpamIpAddressAuditEvent -StartDate $lastMonth -EndDate $Today -IpAddress 10.10.1.1 -CorrelateLogonEvents
```

第一个命令获取当前日期，并将结果存储在名为 `$Today` 的变量中。第二个命令从 `$Today` 变量中减去 30 天，并将结果存储在名为 `$LastMonth` 的变量中。第三个命令获取指定 IP 地址在开始日期和结束日期之间的所有 IP 地址审计事件；该命令通过 `*CorrelateLogonEvents*` 参数包含了来自 DC 和 NPS 的用户及计算机登录事件。最终，这些结果被存储在名为 `$IpamIpAddressAuditEvents` 的变量中。

### 示例 4：按 MAC 地址获取所有 IP 地址审计事件
```
PS C:\> $Today = Get-Date
PS C:\> $LastMonth = $Today.AddDays(-30)
PS C:\> $IpamIpAddressAuditEvents = Get-IpamIpAddressAuditEvent -StartDate $LastMonth -EndDate $Today -ClientId "AA:BB:CC:DD:EE:FF" -CorrelateLogonEvents
```

第一个命令获取当前日期，并将结果存储在名为 `$Today` 的变量中。第二个命令从 `$Today` 变量中减去 30 天，并将结果存储在名为 `$LastMonth` 的变量中。第三个命令根据指定的开始日期和结束日期，获取某个客户端 ID 的所有 IP 地址审计事件；该命令通过 `*CorrelateLogonEvents` 参数包含了来自 DC 和 NPS 的用户及计算机登录事件信息。最后，这些结果被存储在名为 `$IpamIpAddressAuditEvents` 的变量中。

### 示例 5：根据主机名获取所有 IP 地址审核事件
```
PS C:\> $Today = Get-Date
PS C:\> $LastMonth = $Today.AddDays(-30)
PS C:\> $IpamIpAddressAuditEvents = Get-IpamIpAddressAuditEvent -StartDate $LastMonth -EndDate $Today -HostName "client1.contoso.com" -CorrelateLogonEvents
```

第一个命令获取当前日期，并将结果存储在名为 `$Today` 的变量中。第二个命令从 `$Today` 变量中减去 30 天，然后将结果存储在名为 `$LastMonth` 的变量中。第三个命令获取指定主机名在开始日期和结束日期之间的所有 IP 地址审计事件；该命令还通过 `*CorrelateLogonEvents*` 参数包含了来自 DC 和 NPS 的用户及计算机登录事件。最后，该命令将结果存储在名为 `$IpamIpAddressAuditEvents` 的变量中。

### 示例 6：按用户名获取所有 IP 地址审计事件
```
PS C:\> $Today = Get-Date
PS C:\> $LastMonth = $Today.AddDays(-30)
PS C:\> $IpamIpAddressAuditEvents = Get-IpamIpAddressAuditEvent -StartDate $LastMonth -EndDate $Today -HostName "client1.contoso.com"
```

第一个命令获取当前日期，并将结果存储在名为 `$Today` 的变量中。第二个命令从 `$Today` 变量中减去 30 天，然后将结果存储在名为 `$LastMonth` 的变量中。第三个命令查询指定用户名在开始日期和结束日期之间的所有 IP 地址审计事件。由于该用户名只能通过认证数据获得，在根据用户名查询审计事件时始终会包含这些认证数据。该命令将结果存储在名为 `$IpamIpAddressAuditEvents` 的变量中。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个代表该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -ClientId
指定一个客户端ID数组。使用此参数可以通过媒体访问控制（MAC）地址来搜索审核事件。在客户端ID中可以使用破折号（-），但这不是必须的。

```yaml
Type: String
Parameter Sets: ByClientId
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CorrelateLogonEvents
表示该cmdlet能够关联登录事件。使用此参数可以决定是否将用户和计算机事件包含在从域控制器及NPS服务器获取的事件集合中。如果指定了此参数，登录事件将被纳入该cmdlet检索到的关联事件集合中。

```yaml
Type: SwitchParameter
Parameter Sets: ByIpAddress, ByClientId, ByHostName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EndDate
指定用于获取事件数据的结束日期，该日期以 **DateTime** 对象的形式提供。若要获取一个 **DateTime** 对象，可以使用 **Get-Date** cmdlet 并按照 **DD/MM/YYYY** 格式输入日期。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -HostName
指定一个主机名称数组。使用此参数可以通过主机名称来搜索相关的事件。

```yaml
Type: String
Parameter Sets: ByHostName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IpAddress
用于指定一个 IP 地址。可以使用此参数通过 IPv4 地址来搜索相关事件。该命令不支持 IPv6 地址的跟踪功能。

```yaml
Type: String
Parameter Sets: ByIpAddress
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StartDate
以 **DateTime** 对象的形式指定开始日期。要获取一个 **DateTime** 对象，可以使用 **Get-Date** cmdlet，并按照 **DD/MM/YYYY** 格式输入日期。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前运行的 cmdlet，而不影响整个会话或计算机本身。

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

### -UserName
指定一个用户名数组。使用此参数可以按用户名搜索相关事件。不支持按用户的域名进行搜索。登录事件也被包含在此搜索范围内，因为DHCP租约事件中并未包含用户名信息。

```yaml
Type: String[]
Parameter Sets: ByUserName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamIpAuditEvent
此cmdlet返回一个对象，该对象表示IPAM中的IP地址审核事件。

## 备注

## 相关链接

[Remove-IpamIpAddressAuditEvent](./Remove-IpamIpAddressAuditEvent.md)

