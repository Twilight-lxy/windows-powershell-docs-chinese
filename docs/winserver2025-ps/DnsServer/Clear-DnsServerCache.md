---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerCache_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/clear-dnsservercache?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-DnsServerCache
---

# 清除 DNS 服务器缓存

## 摘要
从DNS服务器的缓存中清除资源记录。

## 语法

```
Clear-DnsServerCache [-ComputerName <String>] [-Force] [-CacheScope <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Clear-DnsServerCache** cmdlet 用于清除域名系统（DNS）服务器缓存中的资源记录。

## 示例

#### 示例 1：从缓存中清除资源记录
```
PS C:\> Clear-DnsServerCache -ComputerName "Win12S-05.DNSServer-01.Contoso.com" -Force
```

此命令用于清除指定DNS服务器上的DNS缓存。如果您没有使用“Force”参数，则在执行该操作之前必须先确认是否真的要执行这一操作。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

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

### -CacheScope
指定要清除的缓存范围的名称。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
用于指定一个 DNS 服务器。该参数的可接受值包括：IP V4 地址；IP V6 地址；以及任何能够解析为 IP 地址的其他值，例如完全限定域名（FQDN）、主机名或 NETBIOS 名称。

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
在运行cmdlet之前会提示您进行确认。

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
强制命令运行，而不会要求用户确认。

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
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入`0`，Windows PowerShell®将根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最优限制值。该限制仅适用于当前运行的cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-DnsServerCache](./Get-DnsServerCache.md)

[Set-DnsServerCache](./Set-DnsServerCache.md)

[显示DNS服务器缓存](./Show-DnsServerCache.md)

