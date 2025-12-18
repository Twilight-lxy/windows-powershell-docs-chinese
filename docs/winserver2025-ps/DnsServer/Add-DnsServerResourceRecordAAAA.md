---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerResourceRecordAAAA_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserverresourcerecordaaaa?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerResourceRecordAAAA
---

# Add-DnsServerResourceRecordAAAA

## 摘要
向DNS服务器添加一个AAAA类型的资源记录。

## 语法

```
Add-DnsServerResourceRecordAAAA [-AllowUpdateAny] [-CreatePtr] [-IPv6Address] <IPAddress[]> [-Name] <String>
 [-ComputerName <String>] [-TimeToLive <TimeSpan>] [-ZoneName] <String> [-AgeRecord] [-PassThru]
 [-ZoneScope <String>] [-VirtualizationInstance <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DnsServerResourceRecordAAAA` cmdlet 用于将指定的主机 IPv6 地址（AAAA 格式）记录添加到指定的域名系统（DNS）区域中。AAAA 记录用于指定一个 IPv6 地址。

## 示例

### 示例 1：添加一个 DNS 记录
```
PS C:\> Add-DnsServerResourceRecordAAAA -Name "host24" -ZoneName "contoso.com" -AllowUpdateAny -IPv6Address "3ffe::1" -TimeToLive 01:00:00
```

这个示例为名为 `host24` 的主机在名为 `contoso.com` 的区域中添加了一个类型为 AAAA 的 DNS 记录。该命令指定了 `AllowUpdateAny`，并提供了一个 TTL 值。

## 参数

### -AgeRecord
表示DNS服务器会为该cmdlet添加的资源记录使用时间戳。DNS服务器可以根据时间戳来清除那些已过期的资源记录。

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

### -AllowUpdateAny
表示任何已通过身份验证的用户都可以更新拥有相同所有者名称的资源记录。

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
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
用于指定一个DNS服务器。如果您不指定此参数，命令将在本地系统上执行。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如完全qualified域名（FQDN）、主机名或NETBIOS名称。

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

### -CreatePtr
这表示DNS服务器会自动为AAAA记录创建一个相应的指针（PTR）资源记录。PTR资源记录用于将IP地址映射到完全 Qualified Domain Name（FQDN）。

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

### -IPv6Address
指定一个 IPv6 地址数组。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定一个主机名称。

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

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值（即并发操作的最大数量）。该限制仅适用于当前运行的 cmdlet，而不影响整个会话或整个计算机。

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

### -VirtualizationInstance
指定将要添加区域的虚拟化实例。虚拟化实例是DNS服务器中的逻辑分区，它能够独立托管区域和区域范围。具有相同名称的区域和区域范围可以托管在不同的虚拟化实例中。此参数是可选的；如果未提供该参数，则区域将被添加到默认的虚拟化实例中，而该默认虚拟化实例在功能上等同于一个标准的DNS服务器。

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

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
指定要添加记录的DNS区域的名称。

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
指定区域范围（zone scope）的名称。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerResourceRecord[]

## 备注

## 相关链接

