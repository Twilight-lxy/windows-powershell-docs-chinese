---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerResponseRateLimitingExceptionlist_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/remove-dnsserverresponseratelimitingexceptionlist?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DnsServerResponseRateLimitingExceptionlist
---

# 删除 DNS 服务器响应速率限制异常列表

## 摘要
从DNS服务器中移除一个RRL（Reverse Look-Up List）异常列表。

## 语法

```
Remove-DnsServerResponseRateLimitingExceptionlist [-ComputerName <String>] [-Force] [[-Name] <String>]
 [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-DnsServerResponseRateLimitingExceptionlist` cmdlet 用于从域名系统（DNS）服务器中删除响应速率限制（Response Rate Limiting，简称 RRL）异常列表。

## 示例

#### 示例 1：移除 RRL 异常列表
```
PS C:\> Remove-DnsServerResponseRateLimitingExceptionlist -Name "SafeList1" -force
```

此命令会从DNS服务器中删除名为SafeList1的RRL（Reverse Resolution List）异常列表。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，随后会显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
指定用于运行命令的远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如完全 Qualified Domain Name（FQDN）、主机名或NetBIOS名称。

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
强制命令运行，而无需询问用户的确认。

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
指定 RRL 异常列表的名称。

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

### -PassThru
返回一个表示您当前正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或整个计算机。

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
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerResponseRateLimitingExceptionList
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DnsServerResponseRateLimitingExceptionlist](./Add-DnsServerResponseRateLimitingExceptionlist.md)

[Get-DnsServerResponseRateLimitingExceptionlist](./Get-DnsServerResponseRateLimitingExceptionlist.md)

[Set-DnsServerResponseRateLimitingExceptionlist](./Set-DnsServerResponseRateLimitingExceptionlist.md)

