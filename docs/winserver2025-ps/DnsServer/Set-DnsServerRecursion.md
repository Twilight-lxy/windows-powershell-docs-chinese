---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerRecursion_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverrecursion?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerRecursion
---

# Set-DnsServerRecursion

## 摘要
修改DNS服务器的递归设置。

## 语法

```
Set-DnsServerRecursion [-ComputerName <String>] [-AdditionalTimeout <UInt32>] [-RetryInterval <UInt32>]
 [-Timeout <UInt32>] [-Enable <Boolean>] [-PassThru] [-SecureResponse <Boolean>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsServerRecursion` cmdlet 用于修改域名系统（DNS）服务器的递归设置。当 DNS 服务器代表请求客户端向其他 DNS 服务器发起查询，并将查询结果返回给客户端时，就发生了递归过程。

## 示例

### 示例 1：设置重试间隔
```
PS C:\> Set-DnsServerRecursion -RetryInterval 15 -PassThru

Enable               : False
AdditionalTimeout(s) : 4
RetryInterval(s)     : 15
Timeout(s)           : 8
SecureResponse       : True
```

这个命令将重试间隔设置为15秒。

## 参数

### -AdditionalTimeout
指定 DNS 服务器在使用递归从远程 DNS 服务器获取资源记录时所等待的时间间隔（以秒为单位）。建议将此值限制在 0x00000000 到 0x0000000F 的范围内（即 0 秒到 15 秒，包括两端值）。不过，您也可以使用任何其他数值。默认情况下，我们建议将该值设置为 4。

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

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
用于指定一个DNS服务器。该参数的可接受值包括：IPv4地址；IPv6地址；以及任何能够解析为IP地址的其他值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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
在运行该cmdlet之前，会提示您确认是否要执行该操作。

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

### -Enable
指定服务器是否支持递归功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: EnableRecursion

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -RetryInterval
该参数指定DNS服务器在重试递归查询之前等待的秒数。如果该参数未定义或设置为0，则DNS服务器将在3秒后重试。有效取值范围为1秒到15秒之间。

我们建议一般情况下不要更改该参数的值。但在某些情况下，您应该考虑修改该参数的值。例如，如果一个DNS服务器通过速度较慢的链接与远程DNS服务器进行通信，并在收到响应之前重复尝试查询，那么您可以将重试间隔设置得稍长于实际观察到的响应时间。

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

### -SecureResponse
该选项用于指示DNS服务器是否会根据远程服务器的权威区域来筛选DNS记录，以防止缓存污染。如果将此值设置为$True，DNS服务器只会缓存属于所查询远程服务器权威区域的记录；否则，服务器会缓存远程服务器缓存中的所有记录。

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

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
指定 DNS 服务器在停止尝试联系远程服务器之前等待的秒数。有效值的范围是 0x1 到 0xFFFFFFFF（1 秒到 15 秒）。默认设置为 0x8（8 秒）。我们建议在通过较慢的网络链接进行递归查询时增加此值。

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerRecursion

## 备注

## 相关链接

[Get-DnsServerRecursion](./Get-DnsServerRecursion.md)

