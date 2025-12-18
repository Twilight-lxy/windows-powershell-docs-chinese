---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerGlobalQueryBlockList_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverglobalqueryblocklist?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerGlobalQueryBlockList
---

# Set-DnsServerGlobalQueryBlockList

## 摘要
更改全局查询块列表的设置。

## 语法

```
Set-DnsServerGlobalQueryBlockList [-Enable <Boolean>] [[-List] <String[]>] [-ComputerName <String>] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsServerGlobalQueryBlockList` 这个 cmdlet 用于更改域名系统（DNS）服务器上的全局查询阻止列表的设置。该 cmdlet 会用您指定的名称替换 DNS 服务器无法解析的所有名称。

如果你需要DNS服务器来解析诸如ISATAP和WPAD之类的名称，请将这些名称从列表中删除。Web代理自动发现协议（WPAD）和站点内自动隧道寻址协议（ISATAP）是两种常见的部署协议，它们特别容易受到劫持攻击。

## 示例

### 示例 1：替换全局查询块列表中的名称
```
PS C:\> Set-DnsServerGlobalQueryBlockList -List "Isatap" -PassThru -Verbose
VERBOSE: Setting DNS server GlobalQueryBlockList on Fabrikam01 server.

VERBOSE: GlobalQueryBlockList successfully set on server Fabrikam01.
Enable : True

List   : {isatap}
```

该命令会替换全局查询块列表中所有包含“Isatap”作为主机名称的条目。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，随后再显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -ComputerName
指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的字符串，例如完全qualified域名（FQDN）、主机名或NETBIOS名称。

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

### -Enable
指定服务器是否支持全局查询块列表的功能；该列表用于阻止列表中列出的名称的解析。默认情况下，DNS服务器服务在首次启动时会创建并启用这个全局查询块列表。

当你禁用全局查询黑名单时，DNS服务器服务会响应对黑名单中名称的查询请求；而当你启用全局查询黑名单时，DNS服务器服务将不会响应对黑名单中名称的查询请求。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -List
指定一个主机名称数组。

这个cmdlet会将当前的全局查询块列表替换为你指定的名称列表。如果你想要向列表中添加一个新名称，就必须同时包含列表中已存在的所有名称；如果你没有指定任何名称，该cmdlet将会清除整个查询块列表。

默认情况下，全局查询块列表中包含以下两项：ISATAP 和 WPAD。当 DNS 服务器首次启动时，如果它在现有的区域中发现这些名称，会将其从列表中删除。如果您需要 DNS 服务器解析诸如 ISATAP 和 WPAD 这样的名称，请将它们从列表中移除。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
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
指定可以同时运行的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerGlobalQueryBlockList

## 备注

## 相关链接

[Get-DnsServerGlobalQueryBlockList](./Get-DnsServerGlobalQueryBlockList.md)

