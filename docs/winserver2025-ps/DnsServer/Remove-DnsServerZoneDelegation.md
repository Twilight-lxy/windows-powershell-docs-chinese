---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerZoneDelegation_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/remove-dnsserverzonedelegation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DnsServerZoneDelegation
---

# 移除DNS服务器区域委派（Remove-DnsServerZoneDelegation）

## 摘要
从DNS区域中删除名称服务器或委托设置。

## 语法

### InputObject（默认值）
```
Remove-DnsServerZoneDelegation [-ComputerName <String>] [-PassThru] [-Force] [[-ZoneScope] <String>]
 [-VirtualizationInstance <String>] [-InputObject] <CimInstance> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 参数
```
Remove-DnsServerZoneDelegation [-ComputerName <String>] [-PassThru] [-Force] [[-ZoneScope] <String>]
 [-VirtualizationInstance <String>] [[-NameServer] <String>] [-ChildZoneName] <String> [-Name] <String>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DnsServerZoneDelegation` cmdlet 用于从域名系统（DNS）区域中删除名称服务器或相关委托设置。

如果你在这个 cmdlet 中为子域指定了一个 DNS 服务器，该 cmdlet 会将该服务器从委托关系中移除。如果你移除了最后一个 DNS 服务器，或者没有指定任何 DNS 服务器，该 cmdlet 在确认后会将委托关系从相应的区域中移除。

## 示例

### 示例 1：移除委托关系
```
PS C:\> Remove-DnsServerZoneDelegation -Name "contoso.com" -ChildZoneName "west05" -PassThru -Verbose
```

该命令会从域 contoso.com 中移除 delegation west05。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在该作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -ChildZoneName
指定一个子区域的名称。该cmdlet会取消对该区域的委托（即停止将该区域的管理权限传递给其他系统或用户）。

```yaml
Type: String
Parameter Sets: Parameters
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
用于指定一个DNS服务器。如果您不指定此参数，命令将在本地系统上运行。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如完全合格的域名（FQDN）、主机名或NETBIOS名称。

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
该命令会直接删除名称服务器或相关配置（如域名委托设置），而不会先询问您是否确认。默认情况下，该cmdlet在执行操作之前会先提示您进行确认。

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

### -InputObject
指定要传递给此cmdlet的输入数据。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

```yaml
Type: CimInstance
Parameter Sets: InputObject
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name
指定父区域的名称。

```yaml
Type: String
Parameter Sets: Parameters
Aliases: ZoneName

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NameServer
指定子区域的DNS服务器名称。

```yaml
Type: String
Parameter Sets: Parameters
Aliases:

Required: False
Position: 3
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

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前正在运行的 cmdlet，而不适用于整个会话或整个计算机。

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

### -VirtualizationInstance
指定用于添加区域的虚拟化实例。虚拟化实例是 DNS 服务器中的逻辑分区，它能够独立托管多个区域及其相关范围。相同名称的区域和区域范围可以托管在不同的虚拟化实例中。此参数是可选的；如果未提供该参数，则系统会将区域添加到默认的虚拟化实例中，该实例在功能上等同于一个标准的 DNS 服务器。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。不过实际上这个cmdlet并没有被运行。

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

### -ZoneScope
指定区域范围（zone scope）的名称。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerZoneDelegation

## 备注

## 相关链接

[Add-DnsServerZoneDelegation](./Add-DnsServerZoneDelegation.md)

[Get-DnsServerZoneDelegation](./Get-DnsServerZoneDelegation.md)

[Set-DnsServerZoneDelegation](./Set-DnsServerZoneDelegation.md)

