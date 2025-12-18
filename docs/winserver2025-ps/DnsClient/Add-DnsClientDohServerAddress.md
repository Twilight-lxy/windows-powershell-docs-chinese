---
description: `Add-DnsClientDohServerAddress` cmdlet 用于将基于 HTTPS 的 DNS（DoH）服务器配置添加到支持的 DoH 服务器列表中。
external help file: MSFT_DnsClientDohServerAddress.cdxml-help.xml
Module Name: DnsClient
ms.date: 08/31/2021
online version: https://learn.microsoft.com/powershell/module/dnsclient/add-dnsclientdohserveraddress?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsClientDohServerAddress
---

# Add-DnsClientDohServerAddress

## 摘要
将一个 DoH（Domain Name System over HTTPS）服务器配置添加到受支持的 DoH 服务器列表中。

## 语法

```
Add-DnsClientDohServerAddress [-ServerAddress] <String> [[-DohTemplate] <String>]
 [[-AllowFallbackToUdp] <Boolean>] [[-AutoUpgrade] <Boolean>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DnsClientDohServerAddress` cmdlet 可将基于 HTTPS 的 DNS（DoH）服务器配置添加到受支持的 DoH 服务器列表中。

## 示例

### 示例 1：添加一个 DoH（DNS over HTTPS）服务器
```powershell
Add-DnsClientDohServerAddress -ServerAddress 10.23.1.1 -DohTemplate https://adatum.com/dns-query
```

这个示例使用指定的 URI 模板，将 10.23.1.1 添加到系统的 DoH（Domain Name System）列表中。

### 示例 2：添加一个具有自动升级功能的 DoH（DNS over HTTPS）服务器
```powershell
Add-DnsClientDohServerAddress -ServerAddress 10.23.1.1 -DohTemplate https://adatum.com/dns-query -AllowFallbackToUdp $True -AutoUpgrade $True
```

这个示例使用指定的 URI 模板，将 10.23.1.1 添加到系统的 DoH（DNS over HTTPS）列表中。该命令会将所有指向 10.23.1.1 的域名解析请求重定向到 DoH 服务器。如果加密的域名解析失败，系统会自动回退到未加密的 DNS 解析方式。

## 参数

### -AllowFallbackToUdp
指定在向服务器发起的 DoH 查询失败时是否允许使用未加密的 DNS 作为备用方案。此参数仅在 **AutoUpgrade** 设置为 `True` 时生效。默认值为 `False`。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -AutoUpgrade
指定是否使用 DoH 设置来加密所有发送到该服务器的名称解析请求。如果服务器配置在适配器上，或者它是名称解析策略表（NRPT）规则的一部分，则会执行此升级操作。默认值为 `False`。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -DohTemplate
指定一个有效的 URI 模板，用于连接到 DNS-over-HTTP (DoH) 服务器。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ServerAddress
指定DoH服务器的IP地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值为`0`，则Windows PowerShell会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。该限制仅适用于当前执行的cmdlet，而不影响整个会话或计算机本身。

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

### -Confirm
在运行 cmdlet 之前会提示您确认是否要继续执行该操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System(Boolean)

## 输出

### System.Object

## 备注

## 相关链接

[Add-DnsClientNrptRule](Add-DnsClientNrptRule.md)

[Get-DnsClientDohServerAddress](Get-DnsClientDohServerAddress.md)

[Remove-DnsClientDohServerAddress](Remove-DnsClientDohServerAddress.md)

[Set-DnsClientDohServerAddress](Set-DnsClientDohServerAddress.md)
