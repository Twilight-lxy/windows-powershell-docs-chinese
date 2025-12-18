---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerResourceRecordAging_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverresourcerecordaging?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerResourceRecordAging
---

# 设置 DNS 服务器资源记录的更新策略（Ageing）

## 摘要
指定DNS区域中的资源记录开始老化（即数据逐渐变得陈旧或不再有效）。

## 语法

```
Set-DnsServerResourceRecordAging [-ComputerName <String>] [-ZoneName] <String> [[-NodeName] <String>]
 [-Recurse] [-Force] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-DnsServerResourceRecordAging` cmdlet 用于设置域名系统（DNS）区域中资源记录的过期时间。您必须先使用 `Set-DnsServerZoneAging` cmdlet 在区域级别启用资源记录的过期机制。

即使某个资源已经不再属于该网络，其对应的资源记录仍然会保留下来。系统的老化设置决定了这些记录何时会被视为“失效”（即不再有效）并因此被删除。在达到这个时间点之后，指定的DNS服务器会负责删除这些失效的记录。

此cmdlet会将当前时间的时间戳设置到指定DNS服务器上特定区域的记录中（前提是您已为该区域启用了老化机制）。

## 示例

### 示例 1：某个区域内的年龄记录
```
PS C:\> Set-DnsServerResourceRecordAging -ZoneName "contoso.com" -Force -Recurse
```

此命令会递归地使所有属于“contoso.com”域下的记录“过期”（即不再被视为有效数据）。参数“Force”会覆盖默认的确认提示信息。

### 示例 2：节点下的年龄记录
```
PS C:\> Set-DnsServerResourceRecordAging -NodeName "three.two" -ZoneName "contoso.com"
```

此命令会更新 zone contoso.com 中所有位于 “3.2” 节点下的记录的时效信息（即使这些记录“老化”）。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，随后再显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
用于指定一个 DNS 服务器。如果您不指定此参数，命令将在本地系统上运行。您可以指定一个 IP 地址，或者任何能够解析为 IP 地址的值，例如完全合格的域名（FQDN）、主机名或 NETBIOS 名称。

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
在运行 cmdlet 之前，会提示您进行确认。

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
执行该操作时不会显示确认消息。

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

### -NodeName
用于指定DNS区域中的某个节点或子树。该参数的可接受值为：

- @ for root node.
- The FQDN of a node (the name with a period (.) at the end).
- A single label for the name relative to the zone root.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Recurse
表示DNS服务器会更新指定节点下所有子节点的信息（即使这些子节点“老化”）。可以使用此参数来更新某个区域内的所有记录。

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
指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet被运行时会发生什么情况。但实际上该cmdlet并没有被运行。

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

### -ZoneName
指定一个DNS区域的名称。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-DnsServerZoneAging](./Get-DnsServerZoneAging.md)

[Set-DnsServerZoneAging](./Set-DnsServerZoneAging.md)

