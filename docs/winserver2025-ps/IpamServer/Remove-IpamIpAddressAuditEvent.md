---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamIpAuditEvent.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/remove-ipamipaddressauditevent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IpamIpAddressAuditEvent
---

# 移除 IpamIpAddressAuditEvent

## 摘要
从 IPAM 数据库中删除与 IP 地址相关的审计事件记录。

## 语法

```
Remove-IpamIpAddressAuditEvent -EndDate <DateTime> [-Force] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-IpamIpAddressAuditEvent` cmdlet 会永久删除 IP 地址管理（IPAM）数据库中的所有 IP 地址审计事件，包括在 `endDate` 参数指定的日期之前收集的事件。

## 示例

### 示例 1：删除所有事件数据
```
PS C:\> $Today = Get-Date
PS C:\> Remove-IpamIpAuditEvent -EndDate $Today
Confirm

All Event catalog data up to and including the date selected by you will be deleted permanently. Do you want to

continue?

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):Y
```

第一个命令通过 `Get-Date` cmdlet 获取今天的日期，然后将结果存储在名为 `$Today` 的变量中。第二个命令则删除所有早于 `$Today` 变量所存储日期的 IP 地址审计事件数据。

## 参数

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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

### -EndDate
指定用于删除事件数据的结束日期，格式为YYYY/MM/DD hh:mm:ss。该cmdlet会删除截至该日期（包括该日期）的所有事件数据。该日期值不能与当前日期相同。

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

### -Force
强制命令运行，而无需请求用户确认。

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算出一个最优的节流限制（即允许同时运行的操作数量）。这个节流限制仅适用于当前的 cmdlet，而不适用于整个会话或整个计算机。

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
展示了如果该cmdlet运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamIpAuditEvent
此cmdlet返回一个对象，该对象表示IPAM中的IP地址审核事件。

## 备注

## 相关链接

[Get-IpamIpAddressAuditEvent](./Get-IpamIpAddressAuditEvent.md)

