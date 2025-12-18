---
description: `Get-DnsClientDohServerAddress` cmdlet 从支持的 DoH（DNS over HTTPS）服务器中获取相应的服务器配置信息。
external help file: MSFT_DnsClientDohServerAddress.cdxml-help.xml
Module Name: DnsClient
ms.date: 08/31/2021
online version: https://learn.microsoft.com/powershell/module/dnsclient/get-dnsclientdohserveraddress?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsClientDohServerAddress
---

# 获取 DNS 客户端的 DoH 服务器地址

## 摘要
获取域名系统（DoH）服务器的配置信息。

## 语法

```
Get-DnsClientDohServerAddress [[-ServerAddress] <String[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsClientDohServerAddress` cmdlet 可用于获取受支持的 DoH（DNS over HTTPS）服务器的配置信息。如果您没有指定特定的服务器，该命令会显示所有受支持的 DoH 服务器。

## 示例

#### 示例 1：获取所有 DoH 服务器的配置信息
```powershell
Get-DnsClientDohServerAddress
```

这个示例获取了所有支持的 DoH 服务器的配置信息。

### 示例 2：获取特定 DoH 服务器的配置信息
```powershell
Get-DnsClientDohServerAddress -ServerAddress 10.23.1.1,10.18.1.1
```

这个示例获取了服务器 10.23.1.1 和 10.18.1.1 的 DoH（域名系统）配置信息。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -ServerAddress
指定用于检索系统 DNS-over-HTTP (DoH) 配置的 IP 地址。这些地址必须存在于系统列表中，命令才能成功执行。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不影响整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_DNSClientDohServerAddress

## 备注

## 相关链接

[Add-DnsClientDohServerAddress](Add-DnsClientDohServerAddress.md)

[Add-DnsClientNrptRule](Add-DnsClientNrptRule.md)

[Remove-DnsClientDohServerAddress](Remove-DnsClientDohServerAddress.md)

[Set-DnsClientDohServerAddress](Set-DnsClientDohServerAddress.md)
