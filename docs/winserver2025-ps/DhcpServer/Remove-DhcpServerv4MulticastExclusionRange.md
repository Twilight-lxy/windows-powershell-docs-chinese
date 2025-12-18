---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4MulticastExclusionRange_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/remove-dhcpserverv4multicastexclusionrange?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DhcpServerv4MulticastExclusionRange
---

# 移除 DHCP Server v4 多播排除范围

## 摘要
将之前被排除在多播范围之外的地址重新添加到该范围内。

## 语法

```
Remove-DhcpServerv4MulticastExclusionRange [-ComputerName <String>] [[-EndRange] <IPAddress>] [-Name] <String>
 [[-StartRange] <IPAddress>] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DhcpServerv4MulticastExclusionRange` cmdlet 用于移除之前从多播范围内排除的一组地址。该 cmdlet 运行完成后，这些地址即可立即被重新使用。地址被排除的目的是为了防止动态主机配置协议（DHCP）服务器将这些地址分配给其他设备。

## 示例

### 示例 1：根据范围名称删除被排除的地址段
```
PS C:\> Remove-DhcpServerv4MulticastExclusionRange -Name "Multicast_VideoConference" -ComputerName "DhcpServer01.Contoso.com"
```

此命令会从运行在计算机DhcpServer01.Contoso.com上的DHCP服务器服务中，删除名为Multicast_VideoConference的多播作用域中所有被排除的多播IP地址范围。

### 示例 2：通过 IP 地址移除被排除的地址范围
```
PS C:\> Remove-DhcpServerv4MulticastExclusionRange -Name "Multicast_VideoConference" -StartRange 224.0.0.21 -EndRange 224.0.0.25 -ComputerName "DhcpServer01.Contoso.com"
```

此命令将从名为“Multicast_VideoConference”的多播范围内删除被排除的多播IP地址范围（224.0.0.21至224.0.0.25）。

### 示例 3：通过起始地址范围移除被排除的地址范围
```
PS C:\> Remove-DhcpServerv4MulticastExclusionRange -Name "Multicast_VideoConference" -StartRange 224.0.0.21 -ComputerName "DhcpServer01.Contoso.com"
```

此命令用于移除那些被排除在外的多播IP地址范围（这些地址的起始值为224.0.0.21）。该命令指定了名为“Multicast_VideoConference”的多播作用域，该作用域应用于运行在DhcpServer01.Contoso.com这台计算机上的DHCP服务器服务。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成的过程中，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job` cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定运行DHCP服务器服务的目标计算机的域名系统（DNS）名称或IP地址。

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
在运行cmdlet之前会提示您进行确认。

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
该参数用于指定之前被排除在范围内的IP地址的上限。请使用*StartRange*参数来指定要从排除范围内移除的IP地址的下限。如果您未通过*StartRange*参数指定范围的下限，该cmdlet将删除以该参数结尾的排除范围。如果DHCP服务器服务并未排除以指定值结尾的IP地址，则cmdlet会返回错误并退出。

如果您没有指定排除范围的下限或上限，该 cmdlet 将删除指定范围内的所有排除范围。

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

### -Name
指定要从其中移除 IP 地址排除范围的多播作用域（multicast scope）的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
**Pass thru**：如果指定了此参数，该cmdlet会返回被删除的PowerShell对象。

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

### -StartRange
该参数用于指定之前被排除在范围之外的 IP 地址范围的低端地址。请使用 *EndRange* 参数来指定要从排除范围内移除的 IP 地址范围的高端地址。如果您不使用 *EndRange* 参数来指定高端地址，那么此 cmdlet 将删除以该参数起始的排除范围。如果 DHCP 服务器服务没有排除从指定值开始的地址，cmdlet 将返回错误并退出。

如果您没有指定排除范围的下限或上限，该 cmdlet 将删除指定范围内的所有排除范围。

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
指定可以同时建立的最大并发操作数量，以便运行该 cmdlet。如果省略此参数或输入 `0` 作为值，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DhcpServerv4MulticastExclusionRange[]

## 备注

## 相关链接

[Add-DhcpServerv4MulticastExclusionRange](./Add-DhcpServerv4MulticastExclusionRange.md)

[Get-DhcpServerv4MulticastExclusionRange](./Get-DhcpServerv4MulticastExclusionRange.md)

