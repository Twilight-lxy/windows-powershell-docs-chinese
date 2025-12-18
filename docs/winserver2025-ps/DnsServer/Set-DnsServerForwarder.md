---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerForwarder_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverforwarder?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerForwarder
---

# Set-DnsServerForwarder

## 摘要
在DNS服务器上更改转发器的设置。

## 语法

```
Set-DnsServerForwarder [[-IPAddress] <IPAddress[]>] [-ComputerName <String>] [-UseRootHint <Boolean>]
 [-Timeout <UInt32>] [-EnableReordering <Boolean>] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsServerForwarder` cmdlet 用于更改域名系统（DNS）服务器上的转发器设置。该 cmdlet 可以设置或重置 DNS 服务器在无法本地解析查询时将查询转发到的 IP 地址。此 cmdlet 会覆盖现有的服务器级转发器配置。

使用此 cmdlet 设置 IP 地址时，DNS 服务器会向指定的 IP 地址对应的 DNS 服务器发送递归查询。默认情况下，DNS 服务器会等待 5 秒以获取来自某个转发器的响应，然后再尝试另一个转发器。您可以使用 *Timeout* 参数来更改 DNS 服务器的等待时间（以秒为单位）。当所有转发器都无法提供帮助时，DNS 服务器会尝试进行标准递归查询。另外，默认情况下，如果 DNS 服务器无法解析某个请求，它会使用迭代查询方法来进行处理。

## 示例

#### 示例 1：在 DNS 服务器上设置转发器
```
PS C:\> Set-DnsServerForwarder -IPAddress "10.0.0.1" -PassThru
```

此命令会覆盖DNS服务器上现有的转发器列表，并指定查询应被转发的DNS服务器的IP地址。

### 示例 2：禁用 DNS 服务器上转发器的重新排序功能
```
PS C:\> Set-DnsServerForwarder -EnableReordering $False -PassThru
```

此命令会禁用DNS服务器上转发器的动态重新排序功能。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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
指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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

### -EnableReordering
指定是否启用DNS服务器动态重新排序转发器的功能。

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

### -IPAddress
指定一个包含DNS服务器IP地址的数组，这些服务器用于转发查询请求。按照您希望配置的顺序来列出这些DNS服务器的地址。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个对象，该对象表示您正在操作的项。默认情况下，此cmdlet不会生成任何输出。

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
指定可以同时运行的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -Timeout
指定DNS服务器等待转发器响应的秒数。最小值为0，最大值为15，默认值为5。

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

### -UseRootHint
指定是否阻止DNS服务器执行迭代查询。如果您将**UseRootHint**设置为$false，那么DNS服务器只会将未解析的查询转发给转发器列表中的DNS服务器；如果这些转发器也无法解析这些查询，DNS服务器将不会尝试进行迭代查询。

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

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上该cmdlet并未被执行。

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

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerForwarder

## 备注

## 相关链接

[Get-DnsServerForwarder](./Get-DnsServerForwarder.md)

[Add-DnsServerForwarder](./Add-DnsServerForwarder.md)

[Remove-DnsServerForwarder](./Remove-DnsServerForwarder.md)

