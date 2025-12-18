---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV6ExclusionRange_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/remove-dhcpserverv6exclusionrange?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DhcpServerv6ExclusionRange
---

# 移除 DHCP Server v6 排除范围

## 摘要
删除之前被从某个IPv6地址范围内排除掉的一组IPv6地址。

## 语法

```
Remove-DhcpServerv6ExclusionRange [-ComputerName <String>] [-Prefix] <IPAddress> [[-StartRange] <IPAddress>]
 [[-EndRange] <IPAddress>] [-Passthru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DhcpServerv6ExclusionRange` cmdlet 用于删除之前从某个 IPv6 范围中排除的 IPv6 地址范围。如果指定了 `StartRange` 和 `EndRange` 参数，则会删除具有指定起始地址和结束地址范围的排除范围；如果只指定了 `StartRange` 参数，则会删除仅包含该起始地址范围的排除范围；如果只指定了 `EndRange` 参数，则会删除仅包含该结束地址范围的排除范围；如果没有指定 `StartRange` 也没有指定 `EndRange` 参数，那么将删除该范围内所有被排除的 IPv6 地址范围。

## 示例

### 示例 1：从本地 DHCP 服务器服务中删除某个被排除在范围内的对象
```
PS C:\> Remove-DhcpServerv6ExclusionRange -Prefix 2001:4898:7020:1020:: -StartRange 2001:4898:7020:1020::1 -EndRange 2001:4898:7020:1020::10
```

这个示例会从本地计算机上运行的DHCP服务器服务中的DHCPv6作用域2001:4898:7020:1020::中，删除被排除在外的IPv6地址范围（即2001:4898:7020:1020::1到2001:4898:7020:1020::10）。

#### 示例 2：从远程 DHCP 服务器服务中删除那些被排除在以指定地址开头的作用域之外的设备
```
PS C:\> Remove-DhcpServerv6ExclusionRange -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -StartRange 2001:4898:7020:1020::1
```

这个示例会从名为 dhcpserver.contoso.com 的计算机上运行的 DHCP 服务器服务中，删除属于 DHCPv6 范围 2001:4898:7020:1020:: 内的、起始地址为 2001:4898:7020:1020::1 的 IPv6 地址段。

### 示例 3：从远程 DHCP 服务器服务中删除那些被排除在指定地址范围之外的设备
```
PS C:\> Remove-DhcpServerv6ExclusionRange -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -EndRange 2001:4898:7020:1020::10
```

这个示例会从名为dhcpserver.contoso.com的计算机上运行的DHCP服务器服务中，删除IPv6地址范围。该地址范围的最后一个IP地址为2001:4898:7020:1020::10，并且该地址范围属于DHCPv6作用域2001:4898:7020:1020::。

## 参数

### -AsJob
将该cmdlet作为后台作业运行。使用此参数来执行那些需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job` cmdlets系列命令；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如使用[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定目标计算机的DNS名称、IPv4地址或IPv6地址，该计算机运行动态主机配置协议（DHCP）服务器服务。

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
在运行该 cmdlet 之前，会提示您进行确认。

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

### -EndRange
指定被删除的排除IP范围所对应的IPv6地址的结束部分。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Passthru
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

### -Prefix
指定用于删除被排除的 IP 范围所在的IPv6子网前缀。

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

### -StartRange
指定被删除的排除IPv6范围的起始IPv6地址。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6ExclusionRange
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6ExclusionRange[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv6ExclusionRange](./Add-DhcpServerv6ExclusionRange.md)

[Get-DhcpServerv6ExclusionRange](./Get-DhcpServerv6ExclusionRange.md)

