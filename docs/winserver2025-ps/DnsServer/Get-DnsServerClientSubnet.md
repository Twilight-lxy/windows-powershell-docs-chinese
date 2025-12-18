---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerClientSubnet_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/get-dnsserverclientsubnet?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsServerClientSubnet
---

# Get-DnsServerClientSubnet

## 摘要
获取DNS服务器对应的客户端子网信息。

## 语法

```
Get-DnsServerClientSubnet [[-Name] <String>] [-ComputerName <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsServerClientSubnet` cmdlet 可用于获取域名系统（DNS）服务器的客户端子网信息。如果通过名称指定某个客户端子网，那么仅会显示该客户端子网的相关信息。

## 示例

#### 示例 1：获取所有客户端子网
```
PS C:\> Get-DnsServerClientSubnet | Format-List
Name       : NorthAmericaSubnet
IPV4Subnet : {172.21.0.0/12}
IPV6Subnet :

Name       : AsiaSubnet
IPV4Subnet : {192.168.0.4/16}
IPV6Subnet : {0db8::1/8}

Name       : EuropeSubnet
IPV4Subnet :
IPV6Subnet : {0db8::1/28}
```

此命令可获取DNS服务器上的所有客户端子网信息。该命令使用了`Format-List` cmdlet来控制输出结果的显示格式。如需了解更多信息，请输入`Get-Help Format-List`。

#### 示例 2：获取一个已命名的客户端子网
```
PS C:\> Get-DnsServerClientSubnet -Name "AsiaSubnet" | Format-List
Name       : AsiaSubnet
IPV4Subnet : {196.168.0.4/16}
IPV6Subnet : { 0db8::1/8}
```

这个命令用于获取名为AsiaSubnet的客户端子网。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Name
指定要获取的客户端子网的名称。

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
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerClientSubnet[]

## 备注

## 相关链接

[Add-DnsServerClientSubnet](./Add-DnsServerClientSubnet.md)

[Remove-DnsServerClientSubnet](./Remove-DnsServerClientSubnet.md)

[Set-DnsServerClientSubnet](./Set-DnsServerClientSubnet.md)

