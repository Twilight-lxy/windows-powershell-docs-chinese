---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4Lease_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/add-dhcpserverv4lease?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DhcpServerv4Lease
---

# Add-DhcpServerv4Lease

## 摘要
在DHCP服务器服务中添加一个新的IPv4地址租约。

## 语法

```
Add-DhcpServerv4Lease [-IPAddress] <IPAddress> [-ScopeId] <IPAddress> [-ClientId] <String>
 [-AddressState <String>] [-HostName <String>] [-Description <String>] [-ComputerName <String>] [-PassThru]
 [-DnsRR <String>] [-DnsRegistration <String>] [-ClientType <String>] [-LeaseExpiryTime <DateTime>]
 [-NapCapable <Boolean>] [-NapStatus <String>] [-ProbationEnds <DateTime>] [-PolicyName <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DhcpServerv4Lease` cmdlet 可用于在动态主机配置协议（DHCP）服务器服务上添加一个新的 IPv4 地址租约。此 cmdlet 仅支持运行在 Windows Server® 2012 上的 DHCP 服务器服务，并且仅用于测试目的。

## 示例

### 示例 1：在 DHCP 服务器服务上添加一个 IPv4 租约
```
PS C:\> Add-DhcpServerv4Lease -IPAddress 10.10.10.11 -ScopeId 10.10.10.0 -ClientId F0-DE-F1-7A-00-5E -LeaseExpiryTime "2012-01-28 01:38:13Z" -HostName "MyComputer.contoso.com"
```

这个示例为IPv4地址10.10.10.11在本地计算机上运行的DHCP服务器服务中添加了一个IP地址租约。

## 参数

### -AddressState
指定IPv4地址租约的状态。该参数的可接受值包括：Offered（提供中）、Active（活动状态）、Declined（拒绝）、Expired（已过期）和Inactive（非活动状态）。默认值为Active（活动状态）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Active, Declined, Expired, ActiveReservation, InactiveReservation

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将该 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列的 cmdlets。要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
指定要设置在 IPv4 地址租约上的客户端标识符（ID）。Windows 客户端使用 MAC 地址作为客户端 ID。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ClientType
用于指定客户端类型。该参数的可接受值包括：未指定（Unspecified）、DHCP、BootP、两者皆可（Both）、预留地址（Reservation）以及无（None）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: UnSpecified, Dhcp, BootP, None, Both

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定运行DHCP服务器服务的目标计算机的DNS名称，或IPv4地址或IPv6地址。

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

### -Description
指定要设置在 IPv4 地址租约上的描述字符串。

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

### -DnsRR
表示DHCP服务器服务为此租约要注册的DNS记录类型。该参数的可接受值包括：

- PTR.
Only PTR record to be registered by the DHCP server service.
- AandPTR.
Both A and PTR records to be registered by the DHCP server service.
- NoRegistration.
No DNS registration is performed by the DHCP server service.
If the dynamic DNS is turned off on the DHCP server service, this parameter is set to NoRegistration.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: A, PTR, AandPTR, NoRegistration

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DnsRegistration
表示租赁记录的DNS注册状态。该参数的可接受值为：

- Complete.
  - For an active lease, registration of the required records, as specified by the *DnsRR* parameter value of PTR or AandPTR, is complete.
  - For an expired lease, deletion of the required records is complete.
- Pending.
  - For an active lease, registration of the required records, as specified by the *DnsRR* parameter value of PTR or AandPTR, is pending.
  - For an expired lease, deletion of the required records is pending.
- Not applicable.
  - If the *DnsRR* parameter is set to NoRegistration, such as when no dynamic DNS registration is to be performed by the DHCP server service, this parameter is set to Not applicable.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Complete, Pending, NotApplicable

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -HostName
指定要为其添加 IP 地址租约的客户的 DNS 主机名称。

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

### -IPAddress
指定要在DHCP服务器服务上添加的IPv4地址租约记录所对应的IPv4地址。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LeaseExpiryTime
指定 IPv4 地址租约的过期时间。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NapCapable
表示客户端具备网络访问保护（Network Access Protection, NAP）功能。

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

### -NapStatus
指定客户端的NAP（网络访问保护）状态。该参数的可接受值包括：NoQuarantine、RestrictedAccess、DropPacket、Probation、Exempt、DefaultQuarSetting 和 NoQuarInfo。默认值为 NoQuarantine。

如果你将此参数设置为“Probation”且没有指定试用期，该cmdlet会返回错误。

如果您没有指定这个参数，或者指定的值不是“Probation”（试用期），并且也没有明确说明试用期的具体时长，那么试用期将被自动设置为0。

如果您没有指定此参数，并且指定了试用期，则该参数将被设置为“Probation”。

如果您没有指定此参数，或者指定的参数不是“Probation”，同时又指定了“ProbationEnds”参数，那么这个cmdlet会返回一个错误。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: FullAccess, RestrictedAccess, DropPacket, InProbation, Exempt, DefaultQuarantineSetting, NoQuarantineInfo

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -PolicyName
指定要设置在该新增的 IPv4 地址租约记录上的策略名称。

DHCP服务器服务不会检查服务器上是否确实存在所指定的策略。

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

### -ProbationEnds
指定要设置在 IPv4 地址租约记录上的试用期结束时间。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScopeId
指定要设置在新添加的 IPv4 地址租用记录上的子网掩码。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Lease
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Lease
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DhcpServerv4Lease](./Get-DhcpServerv4Lease.md)

[Remove-DhcpServerv4Lease](./Remove-DhcpServerv4Lease.md)

