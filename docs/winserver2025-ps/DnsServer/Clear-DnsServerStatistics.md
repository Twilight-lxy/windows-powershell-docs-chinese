---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerStatistics_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/clear-dnsserverstatistics?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-DnsServerStatistics
---

# 清除 DNS 服务器统计信息

## 摘要
清除所有DNS服务器的统计信息或各区域的统计信息。

## 语法

### ZoneStatistics
```
Clear-DnsServerStatistics [-ComputerName <String>] [-Force] -ZoneName <String[]> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### Clear0
```
Clear-DnsServerStatistics [-ComputerName <String>] [-Force] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Clear-DnsServerStatistics` cmdlet 用于清除所有域名系统（DNS）服务器的统计信息。一旦这些统计信息被清除，就无法再次获取了。

如果您指定了 *ZoneName* 参数，该 cmdlet 会清除指定区域的统计信息。如果您没有指定 *ZoneName* 参数，该 cmdlet 会清除服务器级别的汇总统计信息。

## 示例

### 示例 1：清除 DNS 服务器统计信息
```
PS C:\> Clear-DnsServerStatistics
Confirm
Cleared statistics cannot be retrieved later, do you want to continue?
[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):
```

这个命令用于清除DNS服务器上的统计信息。

### 示例 2：清除某个区域中的 DNS 服务器统计信息
```
PS C:\> Clear-DnsServerStatistics -ZoneName "Contoso.com"
```

这个命令会清除DNS服务器中名为Contoso.com的区域的统计信息。

## 参数

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后会显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
用于指定一个 DNS 服务器。该参数的可接受值包括：IP V4 地址；IP V6 地址；以及任何能够解析为 IP 地址的其他值，例如完全限定域名（FQDN）、主机名或 NETBIOS 名称。请输入远程计算机的 NETBIOS 名称或完全限定域名。

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
该命令指示cmdlet在执行操作时无需提示用户确认即可直接进行操作。

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
指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果运行该cmdlet会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
指定一个包含DNS区域名称的数组。该cmdlet会清除所指定区域的DNS服务器统计信息。此参数对于“ZoneStatistics”参数集来说是必需的。

```yaml
Type: String[]
Parameter Sets: ZoneStatistics
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-DnsServerStatistics](./Get-DnsServerStatistics.md)

