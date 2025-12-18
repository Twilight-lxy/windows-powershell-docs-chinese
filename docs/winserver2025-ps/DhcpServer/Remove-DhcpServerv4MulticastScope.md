---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV4MulticastScope_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/remove-dhcpserverv4multicastscope?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DhcpServerv4MulticastScope
---

# 移除 DHCP Server v4 多播范围

## 摘要
移除多播作用域（multicast scopes）。

## 语法

```
Remove-DhcpServerv4MulticastScope [-ComputerName <String>] -Name <String[]> [-Force] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DhcpServerv4MulticastScope` cmdlet 用于从动态主机配置协议（DHCP）服务器中删除指定的多播范围。一旦某个多播范围被删除，DHCP 服务器就无法再将该 IP 地址段分配给 DHCP 客户端了。

## 示例

### 示例 1：通过名称移除多播范围
```
PS C:\> Remove-DhcpServerv4MulticastScope -Name "Multicast_VideoConference" -ComputerName "DhcpServer01.Contoso.com"
```

该命令将从名为DhcpServer01.Contoso.com的DHCP服务器中删除名为Multicast_VideoConference的多播范围。

### 示例 2：在不进行确认的情况下删除多播范围
```
PS C:\> Remove-DhcpServerv4MulticastScope -Name "Multicast_AudioConference" -ComputerName "DhcpServer01.Contoso.com" -Force
```

此命令会从名为DhcpServer01.Contoso.com的DHCP服务器中删除名为Multicast_AudioConference的多播作用域。无论该多播作用域是否处于活动状态，或者其中是否包含正在使用的客户端租约，该cmdlet都不会提示用户进行确认。

#### 示例 3：删除不活跃的多播作用域
```
PS C:\> Get-DhcpServerv4MulticastScope | Where-Object -FilterScript { $_.State -Eq "Inactive" } | Remove-DhcpServerv4MulticastScope -Force -PassThru
```

此命令会删除DHCP服务器服务中所有被禁用的多播作用域。`Get-DhcpServerv4MulticastScope` cmdlet会返回多播作用域对象，并通过管道运算符将这些对象传递给`Where-Object` cmdlet。有关更多信息，请输入`Get-Help Where-Object`。

`Where-Object` cmdlet 用于过滤多播范围对象，筛选出不活跃的多播范围，并通过管道运算符将这些对象传递给 `Remove-DhcpServerv4MulticastScope` cmdlet。`Remove-DhcpServerv4MulticastScope` cmdlet 则会删除这些不活跃的多播范围。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job` cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -ComputerName
指定运行 DHCP 服务器服务的目标计算机的 DNS 名称或 IP 地址。

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

### -Force
强制命令运行，而无需请求用户确认。

如果您指定了这个参数，该cmdlet将会删除相应的范围，无论该范围内是否存在正在使用的租约（active leases）。

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

### -Name
指定一个多播作用域名称的数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不生成任何输出。

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

### -ThrottleLimit
指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DhcpServerv4MulticastScope[]

## 备注

## 相关链接

[Get-DhcpServerv4MulticastScope](./Get-DhcpServerv4MulticastScope.md)

[Set-DhcpServerv4MulticastScope](./Set-DhcpServerv4MulticastScope.md)

[Add-DhcpServerv4MulticastScope](./Add-DhcpServerv4MulticastScope.md)

[Get-DhcpServerv4MulticastScopeStatistics](./Get-DhcpServerv4MulticastScopeStatistics.md)

