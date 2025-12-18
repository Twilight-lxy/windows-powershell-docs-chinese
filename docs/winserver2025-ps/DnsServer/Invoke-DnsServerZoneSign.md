---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerZoneSign_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/invoke-dnsserverzonesign?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Invoke-DnsServerZoneSign
---

#Invoke-DnsServerZoneSign

## 摘要
用于签署DNS服务器区域的文件（或数据）。

## 语法

```
Invoke-DnsServerZoneSign [-ZoneName] <String> [-SignWithDefault] [-DoResign] [-ComputerName <String>] [-Force]
 [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Invoke-DnsServerZoneSign` cmdlet 用于签署域名系统（DNS）服务器区域文件。

如果该区域尚未被签名，请使用 *SignWithDefault* 参数，这将使该区域使用一个区域签名密钥（ZSK）和一个密钥签名密钥（KSK），并按照默认的 DNS 安全性（DNSSEC）设置进行签名。如果该区域已经被签名，则请使用 *DoResign* 参数。如果您在已签名的区域上同时使用了 *SignWithDefault* 和 *DoResign* 两个参数，此 cmdlet 将删除现有的区域签名密钥，并使用默认设置重新对该区域进行签名。

## 示例

### 示例 1：使用默认值签署一个区域（zone）
```
PS C:\> Invoke-DnsServerZoneSign -ZoneName "contoso.com" -SignWithDefault -PassThru -Verbose
```

此命令使用新的KSK（Key Signing Key）和ZSK（Zone Signing Key）密钥以及默认的DNSSEC设置来签署“contoso”区域。

### 示例 2：重新签署区域协议
```
PS C:\> Invoke-DnsServerZoneSign "contoso.com" -DoResign -PassThru -Verbose
```

此命令会再次对 contoso.com 区域进行签名处理。

## 参数

### -AsJob
以后台作业的方式运行此cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值为本地计算机上的当前会话。

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
用于指定一个 DNS 服务器。如果您不指定此参数，命令将在本地系统上运行。您可以指定一个 IP 地址，或者任何可以解析为 IP 地址的值，例如完全限定域名（FQDN）、主机名或 NETBIOS 名称。

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

### -DoResign
表示此 cmdlet 会重新签署一个已使用 DNSSEC 进行加密的 zones（域名区域）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Force
在未提示您确认的情况下直接签署DNS服务器区域文件。默认情况下，该cmdlet在执行操作之前会先提示您进行确认。

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

### -SignWithDefault
该参数表示此cmdlet会使用默认设置对DNS区域进行签名。如果某个区域已经过签名处理，那么使用该参数会删除该区域现有的KSK（Key Signing Key）和ZSK（Zone Signing Key）值，并将DNSSEC配置设置为默认值。随后会使用新的KSK和ZSK对该区域重新进行签名操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行该cmdlet的最大操作数量。如果省略此参数或输入值`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值（即并发操作的最大数量）。这个限制仅适用于当前执行的cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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
指定一个主区域的名称。此cmdlet会对该区域进行签名（即对该区域的安全设置进行更新）。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerPrimaryZone

## 备注

## 相关链接

[Invoke-DnsServerZoneUnsign](./Invoke-DnsServerZoneUnsign.md)

