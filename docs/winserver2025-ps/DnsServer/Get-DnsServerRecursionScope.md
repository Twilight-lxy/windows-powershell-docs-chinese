---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerRecursionScope_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/get-dnsserverrecursionscope?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsServerRecursionScope
---

# 获取 DNS 服务器的递归范围

## 摘要
获取DNS服务器的递归作用域（recursion scopes）。

## 语法

```
Get-DnsServerRecursionScope [[-Name] <String>] [-ComputerName <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsServerRecursionScope` cmdlet 用于获取域名系统（DNS）服务器的递归作用域信息。可以通过指定作用域名称来仅获取该作用域的相关信息。

## 示例

### 示例 1：获取所有递归作用域
```
PS C:\> Get-DnsServerRecursionScope
Name                                             Forwarder                                        EnableRecursion
----                                             ---------                                        ---------------
.                                                                                                 True
scopeInternal                                    {10.0.0.1, 172.22.0.1}                           True
```

这个命令可以获取DNS服务器上的所有递归作用域信息。该命令还会获取默认的作用域，其标识为“.”（点）。默认作用域包含了传统的转发器和递归设置相关配置信息。

#### 示例 2：获取特定的递归作用域
```
PS C:\> Get-DnsServerRecursionScope -Name "ScopeInternal"
Name                                             Forwarder                                        EnableRecursion
----                                             ---------                                        ---------------
ScopeInternal                                    {10.0.0.1, 172.22.0.1}                           True
```

这个命令获取名为 ScopeInternal 的递归作用域。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
用于指定远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的字符串，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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

### -Name
指定要获取的递归作用域的名称。

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

### -ThrottleLimit
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值为`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。这个限制仅适用于当前的cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerRecursionScope[]

## 备注

## 相关链接

[Add-DnsServerRecursionScope](./Add-DnsServerRecursionScope.md)

[Remove-DnsServerRecursionScope](./Remove-DnsServerRecursionScope.md)

[Set-DnsServerRecursionScope](./Set-DnsServerRecursionScope.md)

