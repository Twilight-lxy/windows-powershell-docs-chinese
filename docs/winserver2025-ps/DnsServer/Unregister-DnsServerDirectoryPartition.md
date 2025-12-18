---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerDirectoryPartition_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/unregister-dnsserverdirectorypartition?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Unregister-DnsServerDirectoryPartition
---

# 注销 DNS 服务器目录分区

## 摘要
将一个DNS服务器从DNS应用程序目录分区中删除（即将其从该目录中移除）。

## 语法

```
Unregister-DnsServerDirectoryPartition [-ComputerName <String>] [-PassThru] [-Name] <String> [-Force]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`UnRegister-DnsServerDirectoryPartition` cmdlet 用于将一个域名系统（DNS）服务器从指定的 DNS 应用程序目录分区中注销。在将 DNS 服务器从该目录分区中注销后，该 DNS 服务器会自动退出该分区的复制范围。

## 示例

### 示例 1：从目录应用程序分区中取消注册 DNS 服务器
```
PS C:\> UnRegister-DnsServerDirectoryPartition -Name "ADpart" -Verbose
```

此命令会将一台DNS服务器从名为ADpart的DNS目录应用程序分区中注销（即停止将该DNS服务器注册在该分区中）。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如完全 Qualified Domain Name（FQDN）、主机名或NETBIOS名称。

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
该命令会从DNS应用程序目录分区中删除DNS服务器，而不会提示您进行确认。默认情况下，在执行此操作之前，该cmdlet会先询问您的确认意见。

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

### -Name
指定DNS应用程序目录分区的FQDN（完全 Qualified Domain Name）。

```yaml
Type: String
Parameter Sets: (All)
Aliases: DirectoryPartitionName

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的该项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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
该参数用于指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet被运行会会发生什么情况。但实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerDirectoryPartition

## 备注

## 相关链接

[Add-DnsServerDirectoryPartition](./Add-DnsServerDirectoryPartition.md)

[Get-DnsServerDirectoryPartition](./Get-DnsServerDirectoryPartition.md)

[注册 DNS 服务器目录分区](./Register-DnsServerDirectoryPartition.md)

[Remove-DnsServerDirectoryPartition](./Remove-DnsServerDirectoryPartition.md)

