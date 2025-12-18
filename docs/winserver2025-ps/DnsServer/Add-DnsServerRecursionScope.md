---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerRecursionScope_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserverrecursionscope?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerRecursionScope
---

# Add-DnsServerRecursionScope

## 摘要
在DNS服务器上添加一个递归作用域。

## 语法

```
Add-DnsServerRecursionScope [-Name] <String> [[-Forwarder] <IPAddress[]>] [[-EnableRecursion] <Boolean>]
 [-PassThru] [-ComputerName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DnsServerRecursionScope` cmdlet 用于在域名系统（DNS）服务器上添加一个递归范围。递归范围是一组设置的具体实例，这些设置用于控制 DNS 服务器上的递归操作。每个递归范围都包含一组转发器的列表，并指定是否启用递归功能。一台 DNS 服务器可以拥有多个递归范围。

DNS服务器的递归策略允许您为一组查询选择相应的递归范围。如果DNS服务器对某些查询不具备权威解析能力，这些递归策略可以帮助您控制这些查询的解析方式。您可以指定使用哪些转发器，以及是否启用递归功能。

“legacy recursion settings”（旧版递归设置）以及“list of forwarders”（转发器列表）现在被称为“default recursion scope”（默认递归范围）。您无法添加或删除这个默认递归范围，它的名称标识为“.”（点号）。

## 示例

### 示例 1：添加递归作用域
```
PS C:\> Add-DnsServerRecursionScope -Name "ScopeInternal" -Forwarder 10.0.0.1,172.22.0.1 -EnableRecursion $True -PassThru
Name                                             Forwarder                                        EnableRecursion
----                                             ---------                                        ---------------
ScopeInternal                                    {10.0.0.1, 172.22.0.1}                             True
```

该命令为DNS服务器添加了一个递归作用域（recursion scope）。这个作用域允许DNS服务器进行递归查询，并指定了两个转发器（forwarders）。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的任务。

该cmdlet会立即返回一个表示该作业的对象，随后会显示命令提示符。在该作业完成之前，您可以继续在当前会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业的结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
用于指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的字符串，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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

### -EnableRecursion
用于指示是否启用递归功能。

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

### -Forwarder
指定一个用于此递归范围的转发器的IP地址数组。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
为递归作用域指定一个名称。

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
该参数用于指定可以同时进行的操作的最大数量，以便运行相应的cmdlet。如果省略了此参数或输入的值为`0`，那么Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。这个限制仅适用于当前的cmdlet，而不适用于整个会话或整个计算机。

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
展示了如果该 cmdlet 被运行会发生什么情况。不过实际上，这个 cmdlet 并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerRecursionScope

## 备注

## 相关链接

[Get-DnsServerRecursionScope](./Get-DnsServerRecursionScope.md)

[Remove-DnsServerRecursionScope](./Remove-DnsServerRecursionScope.md)

[Set-DnsServerRecursionScope](./Set-DnsServerRecursionScope.md)

