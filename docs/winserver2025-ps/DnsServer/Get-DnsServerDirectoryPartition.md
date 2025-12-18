---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerDirectoryPartition_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/get-dnsserverdirectorypartition?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsServerDirectoryPartition
---

# Get-DnsServerDirectoryPartition

## 摘要
获取一个用于存储DNS应用程序的目录分区。

## 语法

### 自定义（默认值）
```
Get-DnsServerDirectoryPartition [-ComputerName <String>] [-Custom] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 名称
```
Get-DnsServerDirectoryPartition [-ComputerName <String>] [-Name] <String> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsServerDirectoryPartition` cmdlet 可以获取 DNS 服务器上一个或多个域名系统（DNS）应用服务器的目录分区。

## 示例

### 示例 1：获取所有的 DNS 应用目录分区
```
PS C:\> Get-DnsServerDirectoryPartition

server.DirectoryPartitionName        State                         Flags                         ZoneCount
-----------------------------        -----                         -----                         ---------
DomainDnsZones.mytest.cont...        0(DNS_DP_OKAY)                Enlisted Auto Domain          3
ForestDnsZones.mytest.cont...        0(DNS_DP_OKAY)                Enlisted Auto Forest          2
```

这个命令会获取本地计算机上所有的DNS应用程序目录分区信息。

### 示例 2：获取所有自定义应用程序目录分区
```
PS C:\> Get-DnsServerDirectoryPartition -Custom

DirectoryPartitionName        State                         Flags                         ZoneCount
----------------------        -----                         -----                         ---------
DomainDnsZones.mytest.cont... 0(DNS_DP_OKAY)                Enlisted Auto Domain          3
```

这个命令会获取本地计算机上所有的自定义应用程序目录分区。

### 示例 3：通过名称获取应用程序目录的分区
```
PS C:\> Get-DnsServerDirectoryPartition -Name "DomainDnsZones.dept.contoso.com"
```

这个命令会获取本地计算机上名为 DomainDnsZones.dept.contoso.com 的 DNS 应用程序目录分区。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的数值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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

### -Custom
表示此cmdlet返回自定义的目录分区信息。

```yaml
Type: SwitchParameter
Parameter Sets: Custom
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定DNS应用程序目录分区的FQDN（完全限定域名）。

```yaml
Type: String
Parameter Sets: Name
Aliases: DirectoryPartitionName

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行该cmdlet的最大操作数量。如果省略此参数或输入`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。此限制仅适用于当前执行的cmdlet，而不适用于整个会话或整个计算机。

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

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerDirectoryPartition

## 备注

## 相关链接

[Add-DnsServerDirectoryPartition](./Add-DnsServerDirectoryPartition.md)

[注册 DNS 服务器目录分区](./Register-DnsServerDirectoryPartition.md)

[Unregister-DnsServerDirectoryPartition](./Unregister-DnsServerDirectoryPartition.md)

[Remove-DnsServerDirectoryPartition](./Remove-DnsServerDirectoryPartition.md)

