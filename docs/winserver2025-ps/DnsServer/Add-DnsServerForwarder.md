---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerForwarder_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserverforwarder?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerForwarder
---

# Add-DnsServerForwarder

## 摘要
向DNS服务器添加服务器级转发器。

## 语法

```
Add-DnsServerForwarder [-IPAddress] <IPAddress[]> [-ComputerName <String>] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Add-DnsServerForwarder** cmdlet 用于将一个或多个转发器添加到域名系统（DNS）服务器的转发器列表中。如果您更倾向于使用某个特定的转发器，可以将该转发器的 IP 地址放在转发器地址序列的最前面。首次使用此 cmdlet 向 DNS 服务器添加转发器时，这些转发器会被添加到列表的末尾；之后再次使用该 cmdlet 添加新的转发器时，它们也会被添加到列表的末尾。

## 示例

### 示例 1：使用 IPv6 地址将转发器添加到 DNS 服务器
```
PS C:\> Add-DnsServerForwarder -IPAddress 2001:4898:7020:f100:458f:e6a2:fcaf:698c -PassThru
```

此命令将IPv6地址2001:4898:7020:f100:458f:e6a2:fCAF:698c添加到本地DNS服务器的转发器列表中。

### 示例 2：通过使用 IP 地址将转发器添加到 DNS 服务器
```
PS C:\> Add-DnsServerForwarder -IPAddress 172.23.90.124 -PassThru
```

此命令将 IP 地址 172.23.90.124 添加到本地 DNS 服务器的转发器列表中。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行那些需要很长时间才能完成的任务。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的字符串，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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

### -IPAddress
指定一组DNS服务器的IP地址，查询将转发到这些服务器。如果您更倾向于使用其中某个服务器，请将该服务器的IP地址放在转发器IP地址序列的首位。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
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
指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerForwarder

## 备注

## 相关链接

[Set-DnsServerForwarder](./Set-DnsServerForwarder.md)

[Remove-DnsServerForwarder](./Remove-DnsServerForwarder.md)

[Get-DnsServerForwarder](./Get-DnsServerForwarder.md)

[Add-DnsServerConditionalForwarderZone](./Add-DnsServerConditionalForwarderZone.md)

