---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerResourceRecordDS_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserverresourcerecordds?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerResourceRecordDS
---

# Add-DnsServerResourceRecordDS

## 摘要
向DNS区域添加一种类型为DS的资源记录。

## 语法

```
Add-DnsServerResourceRecordDS [-Name] <String> [-CryptoAlgorithm] <String> [-TimeToLive <TimeSpan>]
 [-AgeRecord] [-Digest] <String> [-DigestType] <String> [-KeyTag] <UInt16> [-ComputerName <String>]
 [-ZoneName] <String> [-PassThru] [-ZoneScope <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DnsServerResourceRecordDS` cmdlet 用于向指定的域名系统（DNS）区域中添加一个委托签名者（Delegation Signer，简称 DS）资源记录。

*AgeRecord* 参数与 DS 资源记录无关。

## 示例

#### 示例 1：导入并添加一个 DNS 记录
```
PS C:\> $b = Get-DnsServerResourceRecord -RRType DS -ZoneName "contoso.com" -computerName "Server1"
PS C:\> $b[0].RecordData | Add-DnsServerResourceRecordDS -ZoneName "contoso.com" -Name "west02" -computerName "Server2"
```

此命令从名为 West02.contoso.com 的区域导入一个 DNS 记录，并将其添加到父区域 contoso.com 中。

第一个命令获取DS记录，并将其存储在名为**$b**的变量中。

第二个命令从 `$b` 中获取 DNS 记录，并将其添加到 contoso.com 上。

## 参数

### -AgeRecord
这表示DNS服务器会为该cmdlet添加的资源记录使用时间戳。DNS服务器可以根据时间戳来清除那些已经过期的资源记录。

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

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业的结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
用于指定一个 DNS 服务器。如果未指定此参数，命令将在本地系统上运行。您可以指定一个 IP 地址，或者任何能够解析为 IP 地址的数值，例如完全qualified 域名（FQDN）、主机名或 NETBIOS 名称。

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

### -CryptoAlgorithm
指定服务器用于生成密钥的加密算法。该参数的可接受值包括：

- RsaSha1
- RsaSha256
- RsaSha512
- RsaSha1NSec3
- ECDsaP256Sha256
- ECDsaP384Sha384

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: RsaSha1, RsaSha256, RsaSha512, RsaSha1NSec3, ECDsaP256Sha256, ECDsaP384Sha384

Required: True
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Digest
指定DS摘要数据。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 6
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DigestType
指定摘要数据的类型。该参数的可接受值包括：

- Sha1
- Sha256
- Sha384

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Sha1, Sha256, Sha384

Required: True
Position: 5
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -KeyTag
指定一个键标签（key tag）。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定此 cmdlet 添加到 DNS 服务器中的资源记录的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
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

### -ThrottleLimit
该参数用于指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -TimeToLive
指定资源记录的生存时间（TTL）值，单位为秒。其他DNS服务器会利用这个时间长度来决定记录的缓存时长。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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
指定一个DNS区域的名称。该cmdlet会将记录添加到该区域中。

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

### -ZoneScope
指定区域范围的名称。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerResourceRecord

## 备注

## 相关链接

[Import-DnsServerResourceRecordDS](./Import-DnsServerResourceRecordDS.md)

