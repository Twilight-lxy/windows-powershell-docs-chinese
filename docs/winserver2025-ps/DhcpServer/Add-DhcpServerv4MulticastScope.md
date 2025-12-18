---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV4MulticastScope_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/add-dhcpserverv4multicastscope?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DhcpServerv4MulticastScope
---

# Add-DhcpServerv4MulticastScope

## 摘要
在DHCP服务器上添加一个多播作用域（multicast scope）。

## 语法

```
Add-DhcpServerv4MulticastScope [-ComputerName <String>] [-Name] <String> [-StartRange] <IPAddress>
 [-EndRange] <IPAddress> [-Description <String>] [-State <String>] [-LeaseDuration <TimeSpan>] [-PassThru]
 [-Ttl <UInt32>] [-ExpiryTime <DateTime>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DhcpServerv4MulticastScope` cmdlet 用于在动态主机配置协议（DHCP）服务器上添加一个多播作用域。

## 示例

### 示例 1：添加一个不活跃的多播作用域
```
PS C:\> Add-DhcpServerv4MulticastScope -ComputerName "DhcpServer01.Contoso.com" -Name "Multicast_AudioConference" -StartRange 224.0.0.0 -EndRange 224.0.0.30 -State Inactive -Ttl 20-LeaseDuration 20
```

该命令在名为DhcpServer01.Contoso.com的DHCP服务器上创建了一个名为Multicast_AudioConference的非活动多播范围。命令指定了地址分配给音频会议参与者的租约期限为20天。你可以将一个多播地址分配给多个客户端，并且该命令还规定了数据流量需要经过20个路由器才能传输完成。

### 示例 2：添加一个活动的多播作用域
```
PS C:\> Add-DhcpServerv4MulticastScope -ComputerName "DhcpServer01.Contoso.com" -Name "Multicast_VideoConference" -StartRange 224.0.0.50 -EndRange 224.0.0.80
```

此命令在名为DhcpServer01.Contoso.com的DHCP服务器上创建了一个名为Multicast_AudioConference的多播作用域。您可以在DHCP服务器服务中使用该多播作用域来为视频会议的参与者分配IP地址。您可以为一个多播组分配多个客户端使用同一个多播地址。数据包会经过32个路由器进行传输，租约的有效期为30天。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定运行DHCP服务器服务的目标计算机的DNS名称或IP地址。

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
在运行该cmdlet之前，会提示您确认是否要继续执行该操作。

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
指定多播范围的描述。默认值为 null。

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

### -EndRange
指定该作用域范围内的地址范围结束地址。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ExpiryTime
指定多播范围的过期时间。默认值为“无限”。

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

### -LeaseDuration
指定 IP 地址租约的有效期限。默认值为 30 天。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
为多播范围指定一个名称。

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
返回一个表示您当前正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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
指定该作用域内 IP 地址范围的起始地址。

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

### -State
用于指定作用域（scope）的状态。该参数的可接受值包括：

- Active
- Inactive

The default value is Active.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Active, InActive

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的最大操作数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前执行的 cmdlet，而不适用于整个会话或整个计算机。

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

### -Ttl
指定多播流量需要经过的路由器数量。默认值为 32。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DhcpServerv4MulticastScope

## 备注

## 相关链接

[Get-DhcpServerv4MulticastScope](./Get-DhcpServerv4MulticastScope.md)

[Set-DhcpServerv4MulticastScope](./Set-DhcpServerv4MulticastScope.md)

[Remove-DhcpServerv4MulticastScope](./Remove-DhcpServerv4MulticastScope.md)

