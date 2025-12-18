---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerScavenging_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/start-dnsserverscavenging?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-DnsServerScavenging
---

# 启动 DNS 服务器数据扫描功能

## 摘要
通知DNS服务器尝试查找过期的资源记录。

## 语法

```
Start-DnsServerScavenging [-ComputerName <String>] [-Force] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Start-DnsServerScavenging` cmdlet 用于通知域名系统（DNS）服务器尝试搜索失效的资源记录。该命令成功执行后，会立即启动资源记录的清理（scavenging）过程。

尽管用于启动清理任务的命令看起来执行成功了，但实际上只有满足以下前提条件，清理任务才会真正开始：

- Scavenging is enabled for both the server and the zone.
- The zone is started.
- The resource records have a time stamp.

你可以使用 `Verbose` 参数来显示该命令删除的所有记录。你可以按 Ctrl + C 来结束在 DNS 服务器上运行的清理操作。如果 DNS 服务器无法执行清理操作，该 cmdlet 会显示导致清理操作无法启动的原因。

## 示例

### 示例 1：启动 DNS 服务器扫描程序
```
PS C:\> Start-DnsServerScavenging -Verbose
```

此命令通知本地DNS服务器立即尝试搜索过期的资源记录。

## 参数

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `-*Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

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
在运行该cmdlet之前，会提示您确认是否要继续执行。

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
该命令会通知DNS服务器尝试进行数据收集操作，而无需先询问用户是否确认。默认情况下，此cmdlet在执行操作之前会先提示用户进行确认。

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
该参数用于指定可以同时运行的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前执行的 cmdlet，而不适用于整个会话或整个计算机。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Set-DnsServerScavenging](./Set-DnsServerScavenging.md)

[Get-DnsServerScavenging](./Get-DnsServerScavenging.md)

