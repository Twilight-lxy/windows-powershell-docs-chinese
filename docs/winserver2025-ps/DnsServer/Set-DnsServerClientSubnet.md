---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerClientSubnet_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserverclientsubnet?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServerClientSubnet
---

# Set-DnsServerClientSubnet

## 摘要
更新客户端子网中的IP地址。

## 语法

```
Set-DnsServerClientSubnet [-Name] <String> [[-IPv4Subnet] <String[]>] [[-IPv6Subnet] <String[]>]
 [-Action] <String> [-PassThru] [-ComputerName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DnsServerClientSubnet` cmdlet 用于更新域名系统（DNS）服务器上客户端子网中的 IP 地址。您可以添加、删除或替换地址，同时也可以修改 IPv4 地址、IPv6 地址或这两种类型的地址。

## 示例

### 示例 1：向客户端子网添加一个 IPv4 地址
```
PS C:\> Add-DnsServerClientSubnet -Name "AsiaSubnet" -IPv6Subnet 0db8::1/28 -PassThru -IPv4Subnet 1.10.0.1/8
PS C:\> Set-DnsServerClientSubnet -Name "AsiaSubnet" -Action ADD -IPv4Subnet 192.168.0.4/16 -PassThru | Format-List

Name       : AsiaSubnet
IPV4Subnet : {10.10.0.1/8, 192.168.0.4/16}
IPV6Subnet : {0db8::1/28}
```

第一个命令使用 `Add-DnsServerClientSubnet` cmdlet 创建了一个名为 AsiaSubnet 的客户端子网。

第二个命令向AsiaSubnet客户端子网添加了一个IPv4子网。该命令使用了`Format-List` cmdlet来控制输出的外观。如需更多信息，请输入`Get-Help Format-List`。

该命令包含了*PassThru*参数。添加的IPv4地址会显示在计算机输出结果中。

### 示例 2：替换客户端子网中的 IPv6 地址
```
PS C:\> Add-DnsServerClientSubnet -Name "AsiaSubnet" -IPv6Subnet 0db8::1/28 -PassThru -IPv4Subnet 10.0.0.1/8
PS C:\> Set-DnsServerClientSubnet -Name "AsiaSubnet" -Action REPLACE -IPv6Subnet 0db8::1/8 -PassThru |  Format-List

Name       : AsiaSubnet
IPV4Subnet : {10.0.0.1/8}
IPV6Subnet : {0db8::1/8}
```

第一个命令创建了一个名为AsiaSubnet的客户子网，该子网包含了IPv6地址0db8::1/28。

第二个命令用于替换客户端子网的IPv6地址。计算机输出结果显示，原来的地址0db8::1/28已被替换为0db8::1/8。

### 示例 3：从客户端子网中删除一个 IPv4 地址
```
PS C:\> Add-DnsServerClientSubnet -Name "AsiaSubnet" -IPv6Subnet 0db8::1/28 -PassThru -IPv4Subnet 10.0.0.1/8
PS C:\> Set-DnsServerClientSubnet -Name "AsiaSubnet" -Action REMOVE -IPv4Subnet 10.0.0.1/8 -PassThru | Format-List

Name       : AsiaSubnet
IPV4Subnet :
IPV6Subnet : {0db8::1/8}
```

第一个命令创建了一个名为AsiaSubnet的客户端子网，该子网同时包含一个IPv4地址和一个IPv6地址。

第二个命令会删除IPv4地址，因此计算机输出只显示IPv6地址。

## 参数

### -Action
指定是添加、删除还是替换客户端子网中的IP地址。该参数的可接受值如下：

- ADD
- REMOVE
- REPLACE

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: ADD, REMOVE, REPLACE

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在会话中工作。要管理作业，请使用 `*-Job` cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
用于指定远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如完全qualified域名（FQDN）、主机名或NETBIOS名称。

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
在运行cmdlet之前会提示您进行确认。

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
使用无类别域间路由（CIDR）表示法指定一个IPv4子网地址数组。

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

### -IPv6Subnet
以 CIDR 表示法指定一个 IPv6 子网地址数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定要修改的客户端子网的名称。

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
该参数用于指定可以同时执行的并发操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerClientSubnet

## 备注

## 相关链接

[Add-DnsServerClientSubnet](./Add-DnsServerClientSubnet.md)

[Get-DnsServerClientSubnet](./Get-DnsServerClientSubnet.md)

[Remove-DnsServerClientSubnet](./Remove-DnsServerClientSubnet.md)

