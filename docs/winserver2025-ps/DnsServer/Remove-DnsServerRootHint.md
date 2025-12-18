---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerRootHint_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/remove-dnsserverroothint?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DnsServerRootHint
---

# 移除DNS服务器根目录提示信息

## 摘要
从DNS服务器中移除与根节点相关的提示信息。

## 语法

### InputObject（默认值）
```
Remove-DnsServerRootHint [-ComputerName <String>] [-PassThru] [-Force] [-InputObject] <CimInstance>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 参数
```
Remove-DnsServerRootHint [-ComputerName <String>] [-PassThru] [-Force] [[-IPAddress] <IPAddress[]>]
 [-NameServer] <String> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-DnsServerRootHint` cmdlet 用于从域名系统（DNS）服务器的根提示列表中删除根提示。当您从 DNS 服务器上删除某个根提示后，该 DNS 服务器在启动时将无法与根 DNS 服务器建立连接，也无法响应其自身权威区域之外的名称查询。

## 示例

### 示例 1：删除 DNS 服务器上的所有根提示信息
```
PS C:\> Get-DnsServerRootHint | Remove-DnsServerRootHint
```

此命令会删除本地DNS服务器上的所有根提示信息。`Get-DnsServerRootHint` cmdlet用于获取本地DNS服务器上的所有根提示信息，并将这些结果传递给`Remove-DnsServerRootHint` cmdlet进行处理。

### 示例 2：使用资源记录来移除根提示（root hint）
```
PS C:\> Get-DnsServerRootHint | Where-Object {$_.NameServer.RecordData.NameServer -eq "H.Root-Servers.net."} | Remove-DnsServerRootHint
```

在这个例子中，`Get-DnsServerRootHint` cmdlet 会获取本地 DNS 服务器上所有的根提示（root hints）列表。随后，该命令会将这个列表传递给 `Where-Object` cmdlet。

`Where-Object` 过滤资源记录，以获取名为 `H.Root-Servers.net` 的 DNS 名称服务器的根提示（root hint）。随后，`Where-Object` 将过滤后的 `DnsServerRootHint` 对象传递给 `Remove-DnsServerRootHint` cmdlet，该 cmdlet 会删除相应的根提示。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行那些需要较长时间才能完成的命令。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

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
用于指定远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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
该命令会直接删除根提示信息，而不会询问用户是否确认。默认情况下，此cmdlet在执行操作前会先提示用户进行确认。

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

### -IPAddress
指定一个包含要删除的DNS服务器的IPv4或IPv6地址数组。如果不指定**IPAddress**，此cmdlet将删除指定DNS服务器上的所有根提示（root hints）。

```yaml
Type: IPAddress[]
Parameter Sets: Parameters
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InputObject
指定该cmdlet的输入内容。您可以使用此参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

```yaml
Type: CimInstance
Parameter Sets: InputObject
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -NameServer
指定要删除的根提示（root hint）的名称。

```yaml
Type: String
Parameter Sets: Parameters
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不生成任何输出。

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
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为`0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerRootHint

## 备注

## 相关链接

[Get-DnsServerRootHint](./Get-DnsServerRootHint.md)

[Add-DnsServerRootHint](./Add-DnsServerRootHint.md)

[Set-DnsServerRootHint](./Set-DnsServerRootHint.md)

[Import-DnsServerRootHint](./Import-DnsServerRootHint.md)

