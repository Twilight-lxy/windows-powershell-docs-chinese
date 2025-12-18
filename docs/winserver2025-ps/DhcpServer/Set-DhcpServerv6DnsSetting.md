---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv6DnsSetting_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/set-dhcpserverv6dnssetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DhcpServerv6DnsSetting
---

# Set-DhcpServerv6DnsSetting

## 摘要
配置DHCP服务器服务如何将与客户端相关的信息更新到DNS服务器上。

## 语法

```
Set-DhcpServerv6DnsSetting [-ComputerName <String>] [-NameProtection <Boolean>]
 [-DeleteDnsRROnLeaseExpiry <Boolean>] [-DynamicUpdates <String>] [[-IPAddress] <IPAddress>]
 [[-Prefix] <IPAddress>] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DhcpServerv6DnsSetting` cmdlet 用于配置动态主机配置协议（DHCP）服务器服务如何将与客户端相关的信息更新到 DNS 服务器中。请指定 `Prefix` 或 `IPAddress` 参数，并至少选择一个可选参数；不要同时指定 `Prefix` 和 `IPAddress`。如果两者都不指定，该 cmdlet 将在服务器级别设置 DNS 更新参数。

这个cmdlet会修改有效的DNS更新设置，并将其应用到指定的预留资源、作用域或服务器级别。

## 示例

### 示例 1：设置服务器级别的 DNS 更新配置
```
PS C:\> Set-DhcpServerv6DnsSetting -ComputerName "dhcpserver.contoso.com" -DynamicUpdates "Always" -DeleteDnsRRonLeaseExpiry $True
```

这个示例将 DHCPv6 服务器级别的（即全服务器范围的）DNS 更新配置设置为：始终使用租约信息来更新 DNS；通过创建动态主机配置标识符（DHCID）资源记录来启用 NAP（网络访问保护）功能；并在租约到期时从 DNS 服务器中删除相应的客户端条目。

### 示例 2：为某个范围设置 DNS 更新参数
```
PS C:\> Set-DhcpServerv6DnsSetting -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -DynamicUpdates "OnClientRequest" -NameProtection $True
```

这个示例为范围 2001:4898:7020:1020:: 设置了 DNS 更新配置。该配置允许根据客户端请求以及全qualified domain name（FQDN）选项（ID 81）来更新 DNS 服务器上的租约信息，并通过创建动态主机配置标识符（DHCID）资源记录来实现名称保护功能。

### 示例 3：为某个地址设置 DNS 更新配置
```
PS C:\> Set-DhcpServerv6DnsSetting -ComputerName dhcpserver.contoso.com -IPAddress 2001:4898:7020:1020::5 -DynamicUpdates Never
```

这个示例为预留的IP地址2001:4898:7020:1020::5设置了DNS更新配置，使其永远不会更新与客户端租赁条目相关的DNS服务器信息。

## 参数

### -AsJob
以后台作业的形式运行该 cmdlet。使用此参数来执行需要较长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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

### -ComputerName
指定运行DHCP服务器服务的目标计算机的DNS名称，或者IPv4或IPv6地址。

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

### -DeleteDnsRROnLeaseExpiry
该参数用于指定DHCP服务器服务在租约到期后是否会删除与该DHCP客户端相关的DNS资源记录。只有当*DynamicUpdate*参数被设置为“Always”或“OnClientRequest”时，才能设置此参数。

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

### -DynamicUpdates
指定在何种条件下对DNS服务器执行动态更新。该参数的可接受值为：

- Always.
The DHCP server service always performs dynamic DNS registration of A and PTR records for the DHCP clients.
- Never.
The DHCP server service does not perform any dynamic DNS registration.
- OnClientRequest.
The DHCP server service performs dynamic DNS registration of A and PTR records if the DHCP client has requested for the same in the DHCP client message.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Always, Never, OnClientRequest

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IPAddress
指定用于配置DNS更新行为的预留IPv6地址。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases: ReservedIP

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NameProtection
该参数用于设置DHCP服务器服务中名称保护的启用状态。如果您指定了此参数，而系统中已存在同名DNS记录，则客户端的DNS更新操作将会失败（而不会导致原有DNS记录被覆盖）。

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

### -Prefix
指定用于配置DNS更新行为的IPv6地址范围内的子网前缀。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行该cmdlet的最大操作数量。如果省略此参数或输入`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算出一个最优的并发限制。这个并发限制仅适用于当前执行的cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6DnsSetting
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Reservation
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6DnsSetting
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DhcpServerv6DnsSetting](./Get-DhcpServerv6DnsSetting.md)

