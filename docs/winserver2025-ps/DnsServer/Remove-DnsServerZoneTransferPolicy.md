---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerZoneTransferPolicy_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/remove-dnsserverzonetransferpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DnsServerZoneTransferPolicy
---

# 移除DNS服务器区域传输策略

## 摘要
从DNS服务器中删除区域传输策略。

## 语法

### 服务器（默认设置）
```
Remove-DnsServerZoneTransferPolicy [-PassThru] [-Name] <String> [-ComputerName <String>] [-Force]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 区域（Zone）
```
Remove-DnsServerZoneTransferPolicy [-PassThru] [-Name] <String> [-ComputerName <String>] [-Force]
 [-ZoneName] <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-DnsServerZoneTransferPolicy` 这个 cmdlet 用于从域名系统（DNS）服务器中删除区域传输策略。你需要指定一个区域名称来移除该区域的策略；如果没有指定区域，此 cmdlet 会删除服务器级别的所有策略。

## 示例

### 示例 1：删除某个区域的所有区域传输策略
```
PS C:\> Get-DnsServerZoneTransferPolicy -ZoneName "contoso.com" | Remove-DnsServerZoneTransferPolicy -ZoneName "contoso.com" -Force
```

此命令使用 **Get-DnsServerZoneTransferPolicy** cmdlet 获取名为 contoso.com 的区域的所有区域传输策略。该命令通过管道运算符将这些策略传递给当前的 cmdlet，然后当前 cmdlet 会删除该区域中的所有策略。此命令指定了 *Force* 参数，因此会在不提示确认的情况下直接删除策略。

### 示例 2：删除服务器级别的区域传输策略
```
PS C:\> Remove-DnsServerZoneTransferPolicy -Name "InternalTransfers" -PassThru
Confirm
Removing the server level policy InternalTransfers from the DNS server SERVER01-T10. Do you want to continue?
[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): Y

Name                                 ProcessingOrder                      IsEnabled                            Action
----                                 ---------------                      ---------                            ------
InternalTransfers                    2                                    True                                 Ignore
```

此命令会删除名为“InternalTransfers”的服务器级区域传输策略。

### 示例 3：删除区域级别的区域传输策略
```
PS C:\> Remove-DnsServerZoneTransferPolicy -Name "InternalTransfers" -ZoneName "contoso.com" -Force
```

此命令会删除名为“contoso.com”的区域上的名为“InternalTransfers”的区域传输策略。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
用于指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的数值，例如FQDN（完全 Qualified Domain Name，全称域名）、主机名或NETBIOS名称。

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
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算 해당 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
用于指定DNS区域的名称。此cmdlet会从该参数所指定的区域中删除相应的策略。

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

[Add-DnsServerZoneTransferPolicy](./Add-DnsServerZoneTransferPolicy.md)

[Get-DnsServerZoneTransferPolicy](./Get-DnsServerZoneTransferPolicy.md)

[Set-DnsServerZoneTransferPolicy](./Set-DnsServerZoneTransferPolicy.md)

[开始DNS服务器区域传输](./Start-DnsServerZoneTransfer.md)

[Add-DnsServerQueryResolutionPolicy](./Add-DnsServerQueryResolutionPolicy.md)

