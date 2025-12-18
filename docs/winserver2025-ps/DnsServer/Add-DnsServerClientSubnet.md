---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerClientSubnet_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/add-dnsserverclientsubnet?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DnsServerClientSubnet
---

# Add-DnsServerClientSubnet

## 摘要
将一个客户端子网添加到DNS服务器中。

## 语法

```
Add-DnsServerClientSubnet [-Name] <String> [[-IPv4Subnet] <String[]>] [[-IPv6Subnet] <String[]>] [-PassThru]
 [-ComputerName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-DnsServerClientSubnet` cmdlet 用于将一个客户端子网添加到域名系统（DNS）服务器中。客户端子网是由多个 IP 子网组成的集合，每个客户端子网都有一个唯一的名称。该子网包含两个 IP 地址列表：一个是 IPv4 子网的地址列表，另一个是 IPv6 子网的地址列表。客户端子网可以代表一个逻辑上的组，例如某个地理区域、数据中心或一组可信赖的 DNS 解析器。您可以在 DNS 策略中使用这些客户端子网作为筛选条件；多个 DNS 策略也可以引用同一个客户端子网。

## 示例

### 示例 1：添加一个使用 IPv4 地址指定的客户端子网
```
PS C:\> Add-DnsServerClientSubnet -Name "NorthAmericaSubnet" -IPv4Subnet 172.21.33.0/16 -PassThru
Name                                                                                       IPV4Subnet
----                                                                                       ----------
NorthAmericaSubnet                                                                         {172.21.33.0/16}
```

此命令将一个名为 NorthAmericaSubnet 的客户端子网添加到 DNS 服务器中。该命令通过使用 IPv4 地址来指定这个子网。

### 示例 2：添加一个使用 IPv6 地址指定的客户端子网
```
PS C:\> Add-DnsServerClientSubnet -Name "EuropeSubnet" -IPv6Subnet 0db8::1/28 -PassThru | Format-List
Name       : EuropeSubnet
IPV4Subnet :
IPV6Subnet : {3ffe::1/28}
```

此命令向DNS服务器添加了一个名为“EuropeSubnet”的客户端子网。该命令通过使用IPv6地址来指定这个子网，并利用`Format-List` cmdlet来控制输出内容的显示格式。如需更多信息，可以输入`Get-Help Format-List`进行查询。

### 示例 3：添加在 IPv4 和 IPv6 中都指定的客户端子网
```
PS C:\> Add-DnsServerClientSubnet -Name "AsiaSubnet" -IPv6Subnet 0db8::1/28 -PassThru -IPv4Subnet 172.16.0.1/8 | Format-List
Name       : AsiaSubnet
IPV4Subnet : {172.0.0.1/8}
IPV6Subnet : {4ffe::1/28}
```

此命令向DNS服务器添加了一个名为AsiaSubnet的客户端子网。该命令通过同时使用IPv4和IPv6地址来指定该子网。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。您可以输入计算机名称，或者输入一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的数值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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
在运行该 cmdlet 之前，会提示您进行确认。

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

### -IPv4Subnet
指定一个包含IPv4子网地址的数组，这些地址采用无类别域间路由（CIDR）表示法。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IPv6Subnet
指定一个以CIDR表示法的IPv6子网地址数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
“ Species”是新客户端子网名称的组成部分。

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
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最优限制（即并发操作的最大数量）。此限制仅适用于当前正在运行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet运行会发生什么情况。不过实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerClientSubnet

## 备注

## 相关链接

[Get-DnsServerClientSubnet](./Get-DnsServerClientSubnet.md)

[Remove-DnsServerClientSubnet](./Remove-DnsServerClientSubnet.md)

[Set-DnsServerClientSubnet](./Set-DnsServerClientSubnet.md)

