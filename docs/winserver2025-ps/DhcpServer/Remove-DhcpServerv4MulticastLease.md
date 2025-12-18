---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4MulticastLease_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/remove-dhcpserverv4multicastlease?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DhcpServerv4MulticastLease
---

# 删除 DHCP Serverv4 多播租约

## 摘要
移除特定多播范围或多播IP地址的相关租约信息。

## 语法

```
Remove-DhcpServerv4MulticastLease [-ComputerName <String>] [-PassThru] [-Name] <String>
 [[-IPAddress] <IPAddress[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DhcpServerv4MulticastLease` cmdlet 用于删除指定多播范围内的一个或多个多播租约。您可以通过指定 IP 地址来指示要删除的哪些租约；如果不指定 `IPAddress` 参数，该 cmdlet 将删除指定多播范围内的所有租约。

## 示例

### 示例 1：移除一系列地址的租约信息
```
PS C:\> Remove-DhcpServerv4MulticastLease -Name "Multicast_VideoConference" -IPAddress 224.0.0.50,224.0.0.51 -ComputerName "DhcpServer01.Contoso.com"
```

此命令将删除地址 224.0.0.50 到 224.0.0.51 的多播 IP 地址租约。该命令指定了名为 DhcpServer01.Contoso.com 的计算机上的多播作用域“Multicast_VideoConference”。

### 示例 2：按范围名称删除地址租约
```
PS C:\> Remove-DhcpServerv4MulticastLease -Name "Multicast_AudioConference" -ComputerName "DhcpServer01.Contoso.com"
```

此命令会删除名为“Multicast_AudioConference”的作用域中所有的多播IP地址租约。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行耗时较长的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成过程中，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
指定运行动态主机配置协议（DHCP）服务器服务的目标计算机的域名系统（DNS）名称或IP地址。

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

### -IPAddress
指定一个要删除的IP地址数组。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定多播作用域（multicast scope）的名称。

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

### -ThrottleLimit
该参数用于指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet运行会发生的结果。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DhcpServerv4MulticastLease[]

## 备注

## 相关链接

[Get-DhcpServerv4MulticastLease](./Get-DhcpServerv4MulticastLease.md)

