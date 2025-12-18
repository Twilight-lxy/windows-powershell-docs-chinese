---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerResourceRecordPTR_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserverresourcerecordptr?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerResourceRecordPtr
---

# Add-DnsServerResourceRecordPtr

## 摘要
向DNS服务器添加一种类型为PTR的资源记录。

## 语法

```
Add-DnsServerResourceRecordPtr [-AllowUpdateAny] [-PtrDomainName] <String> [-Name] <String>
 [-ComputerName <String>] [-ZoneName] <String> [-TimeToLive <TimeSpan>] [-AgeRecord] [-PassThru]
 [-ZoneScope <String>] [-VirtualizationInstance <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DnsServerResourceRecordPtr` cmdlet 将指定的指针（PTR）记录添加到指定的域名系统（DNS）区域中。

PTR（Reverse Pointer）资源记录支持基于in-addr.arpa域的反向查找功能。PTR记录可以通过计算机的IP地址来定位该计算机，并将该IP地址解析为对应的DNS域名。

## 示例

### 示例 1：添加一个 PTR 记录
```
PS C:\> Add-DnsServerResourceRecordPtr -Name "17" -ZoneName "0.168.192.in-addr.arpa" -AllowUpdateAny -TimeToLive 01:00:00 -AgeRecord -PtrDomainName "host17.contoso.com"
```

此命令在名为 contoso.com 的区域中添加一个类型为 PTR 的 DNS 记录。该记录将 IP 地址 192.168.0.17 映射到名称 host17.contoso.com。该命令包含了 **AllowUpdateAny** 和 **AgeRecord** 参数，并指定了一个 TTL 值。由于该命令中包含了 **AgeRecord** 参数，DNS 服务器可以回收（清除）这个记录。

## 参数

### -AgeRecord
表示该DNS服务器在使用时间戳来处理此cmdlet添加的资源记录。DNS服务器可以根据时间戳来清除那些已过期的资源记录。

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
这表示任何经过身份验证的用户都可以更新拥有相同所有者名称的资源记录。

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
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。输入一个计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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
用于指定一个DNS服务器。如果您不指定此参数，命令将在本地系统上运行。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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
在运行该 cmdlet 之前，会提示您确认是否要继续执行。

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

### -Name
用于指定主机对应的 IP 地址的一部分。您可以使用 IPv4 或 IPv6 地址。例如，如果您使用的是 IPv4 C 类反向查找区域，则 “Name” 指定 IP 地址的最后一个八位字节；如果您使用的是 B 类反向查找区域，则 “Name” 指定 IP 地址的最后两个八位字节。

```yaml
Type: String
Parameter Sets: (All)
Aliases: RecordName

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

### -PtrDomainName
为DNS命名空间中的资源记录指定一个FQDN（完全 Qualified Domain Name）。该值是使用此PTR进行反向查找时获得的响应结果。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不影响整个会话或计算机本身。

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
指定资源记录的“生存时间”（Time to Live，简称TTL）值，单位为秒。其他DNS服务器会利用这个时间长度来决定缓存记录的时长。

“权威起始（SOA）”记录定义了默认的TTL值。

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
指定该区域将被添加到的虚拟化实例。虚拟化实例是 DNS 服务器中的逻辑分区，它能够独立托管多个区域及其对应的范围。具有相同名称的区域和区域范围可以托管在不同的虚拟化实例中。此参数是可选的；如果未提供该参数，系统会将该区域添加到默认的虚拟化实例中，而这个默认实例在功能上等同于一个标准的 DNS 服务器。

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

### -ZoneName
指定反向查找区域的名称。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.Management.ManagementBaseObject

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerResourceRecord
DnsServerResourceRecord对象包含以下字段：

- **DistinguishedName**
- **HostName**
- **RecordClass**
- **RecordData**
- **RecordType**
- **Timestamp**
- **TimeToLive**
- **PtrDomainName**

## 备注

## 相关链接

