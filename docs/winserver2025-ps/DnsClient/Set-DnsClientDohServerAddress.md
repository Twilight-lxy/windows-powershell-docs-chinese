---
description: `Set-DnsClientDohServerAddress` cmdlet 用于修改现有的基于 HTTPS 的 DNS（DoH）服务器配置。
external help file: MSFT_DnsClientDohServerAddress.cdxml-help.xml
Module Name: DnsClient
ms.date: 08/31/2021
online version: https://learn.microsoft.com/powershell/module/dnsclient/set-dnsclientdohserveraddress?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsClientDohServerAddress
---

# 设置 DNS 客户端的 DOH 服务器地址

## 摘要
修改现有的 DoH（Domain Name System over HTTPS）服务器配置。

## 语法

### 查询（CDXML）（默认值）
```
Set-DnsClientDohServerAddress [-ServerAddress] <String[]> [[-DohTemplate] <String>]
 [[-AllowFallbackToUdp] <Boolean>] [[-AutoUpgrade] <Boolean>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-DnsClientDohServerAddress -InputObject <CimInstance[]> [[-DohTemplate] <String>]
 [[-AllowFallbackToUdp] <Boolean>] [[-AutoUpgrade] <Boolean>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsClientDohServerAddress` cmdlet 用于修改现有的基于 HTTPS 的 DNS（DoH）服务器配置。

## 示例

#### 示例 1：更改 DNS 服务器的 URI 模板
```powershell
Set-DnsClientDohServerAddress -ServerAddress 10.23.1.1 -DohTemplate https://adatum.com/dns-query
```

这个示例修改了地址为 10.23.1.1 的 URI 模板。该命令将 **AutoUpgrade** 和 **AllowFallbackToUdp** 的值设置为默认值 `False`。

### 示例 2：更改 DoH 服务器的 URI 模板以实现自动升级
```powershell
Set-DnsClientDohServerAddress -ServerAddress 10.23.1.1 -DohTemplate https://adatum.com/dns-query -AutoUpgrade $True
```

这个示例会修改地址为 10.23.1.1 的 URI 模板。该命令还会将所有与该地址相关的解析方式升级为使用 10.23.1.1。参数 **AllowFallbackToUdp** 的默认值为 `False`；如果加密名称解析失败，系统不会自动切换回未加密的 DNS 解析方式。


## 参数

### -AllowFallbackToUdp
指定当向服务器发送的 DoH 查询失败时，是否允许使用未加密的 DNS 作为备用方案。此参数仅在 **AutoUpgrade** 设置为 `True` 时生效。默认值为 `False`。

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
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` 系列的 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
该参数用于指定是否使用 DNS-over-HTTP（DoH）设置来加密所有发送到此服务器的名称解析请求。如果该服务器配置在适配器上，或者属于某个名称解析策略表（Name Resolution Policy Table, NRPT）规则的一部分，则会触发升级。默认值为 `False`。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个有效的 URI 模板，用于连接到 DoH 服务器。

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

### -InputObject
指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给该 cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
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

### -ServerAddress
指定DoH服务器的IP地址。

```yaml
Type: String[]
Parameter Sets: Query (cdxml)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入`0`，则Windows PowerShell会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。此限制仅适用于当前运行的cmdlet，而不适用于整个会话或计算机本身。

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
在运行 cmdlet 之前，会提示您进行确认。

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
展示了如果该cmdlet运行会发生什么情况。但实际上这个cmdlet并没有被运行。

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

### System.String[]

### Microsoft.ManagementInfrastructure.CimInstance[]

### System.String

### SystemBoolean

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_DNSClientDohServerAddress

## 备注

## 相关链接

[Add-DnsClientDohServerAddress](Add-DnsClientDohServerAddress.md)

[Add-DnsClientNrptRule](Add-DnsClientNrptRule.md)

[Get-DnsClientDohServerAddress](Get-DnsClientDohServerAddress.md)

[Remove-DnsClientDohServerAddress](Remove-DnsClientDohServerAddress.md)
