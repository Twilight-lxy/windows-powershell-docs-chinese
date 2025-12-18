---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerQueryResolutionPolicy_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/remove-dnsserverqueryresolutionpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DnsServerQueryResolutionPolicy
---

# 删除 DNS 服务器查询解析策略

## 摘要
从DNS服务器中删除用于查询解析的策略。

## 语法

### 服务器（默认设置）
```
Remove-DnsServerQueryResolutionPolicy [-Force] [-ComputerName <String>] [-PassThru] [-Name] <String>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 区域（Zone）
```
Remove-DnsServerQueryResolutionPolicy [-Force] [-ComputerName <String>] [-PassThru] [-Name] <String>
 [-ZoneName] <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-DnsServerQueryResolutionPolicy` cmdlet 用于从域名系统（DNS）服务器中删除与查询解析相关的策略。删除某个策略后，DNS 服务器会自动调整其余策略的处理顺序。

## 示例

### 示例 1：删除服务器级别的策略
```
PS C:\> Remove-DnsServerQueryResolutionPolicy -Name "DropPolicy" -PassThru

Confirm
Removing the server level policy DropPolicy from the DNS server SERVER01-T10. Do you want to continue?
[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): Y

Name                                 ProcessingOrder                      IsEnabled                            Action
----                                 ---------------                      ---------                            ------
DropPolicy                           1                                    True                                 Ignore
```

这个命令会删除一个名为“DropPolicy”的服务器级别策略。

### 示例 2：删除区域级别的策略
```
PS C:\> Remove-DnsServerQueryResolutionPolicy -Name "LBPolicy" -ZoneName "contoso.com"

Confirm
Removing the zone level policy LBPolicy from zone contoso.com on the DNS server SERVER01-T10. Do you want to continue?
[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): Y
```

此命令会从名为 contoso.com 的区域中删除名为 LBPolicy 的区域级策略。

### 示例 3：从某个区域中移除所有区域级别的策略
```
PS C:\> Get-DnsServerQueryResolutionPolicy -ZoneName "contoso.com" | Remove-DnsServerQueryResolutionPolicy -ZoneName "contoso.com" -Force -PassThru

Name                                 ProcessingOrder                      IsEnabled                            Action
----                                 ---------------                      ---------                            ------
NorthAmericaPolicy                   1                                    True                                 Allow
EuropePolicy                         1                                    True                                 Allow
```

该命令使用 `Get-DnsServerQueryResolutionPolicy` cmdlet 获取名为 `contoso.com` 的区域中的所有区域级策略。通过管道运算符（pipeline operator），这些策略被传递给当前的 cmdlet，然后当前 cmdlet 会删除该区域中的所有策略。此命令指定了 `Force` 参数，因此在不提示确认的情况下直接删除策略。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，随后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用 `-*Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如完全qualified domain name（FQDN）、主机名或NETBIOS名称。

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
强制命令运行，而无需请求用户确认。

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
指定要删除的策略的名称。

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算出适合该 cmdlet 的最佳限制值。这个限制仅适用于当前执行的 cmdlet，而不影响整个会话或整个计算机。

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
展示了如果该cmdlet被运行会发生的情景。不过实际上，这个cmdlet并没有被运行。

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
指定要从中删除区域级策略的DNS区域的名称。

```yaml
Type: String
Parameter Sets: Zone
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerPolicy

## 备注

## 相关链接

[Add-DnsServerQueryResolutionPolicy](./Add-DnsServerQueryResolutionPolicy.md)

[Get-DnsServerQueryResolutionPolicy](./Get-DnsServerQueryResolutionPolicy.md)

[Set-DnsServerQueryResolutionPolicy](./Set-DnsServerQueryResolutionPolicy.md)

