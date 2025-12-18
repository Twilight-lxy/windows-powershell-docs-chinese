---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerClientSubnet_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/remove-dnsserverclientsubnet?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DnsServerClientSubnet
---

# 删除DNS服务器客户端子网

## 摘要
从DNS服务器中删除某个客户端子网。

## 语法

```
Remove-DnsServerClientSubnet [-Name] <String> [-PassThru] [-Force] [-ComputerName <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DnsServerClientSubnet` cmdlet 用于从域名系统（DNS）服务器中删除某个客户端子网。如果某个客户端子网被包含在任何 DNS 策略中，那么就无法删除该子网。

## 示例

#### 示例 1：删除一个客户端子网
```
PS C:\> Remove-DnsServerClientSubnet -Name AsiaSubnet -PassThru -Force | Format-List
Name       : AsiaSubnet
IPV4Subnet : {192.168.0.4/16}
IPV6Subnet : {0db8::1/8}
```

此命令会从 DNS 服务器中删除名为 AsiaSubnet 的客户端子网。该命令指定了 *Force* 参数，因此不会提示您进行确认。此外，该命令使用了 **Format-List** cmdlet 来控制输出内容的显示方式。如需更多信息，请输入 `Get-Help Format-List`。

### 示例 2：使用流水线删除所有客户端子网
```
PS C:\> Get-DnsServerClientSubnet | Remove-DnsServerClientSubnet -PassThru -Force | Format-List
Name       : EuropeSubnet
IPV4Subnet :
IPV6Subnet : {0db8::1/28}

Name       : NorthAmericaSubnet
IPV4Subnet : {172.21.0.0/16}
IPV6Subnet :
```

该命令使用 `Get-DnsServerClientSubnet` cmdlet 来获取所有客户端子网，并通过管道运算符将这些子网传递给当前的 cmdlet。当前 cmdlet 会移除每一个客户端子网。由于指定了 `Force` 参数，因此系统不会提示用户进行确认操作。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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
指定要删除的客户端子网的名称。

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
返回一个对象，该对象表示您正在操作的项目。默认情况下，此 cmdlet 不会生成任何输出。

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
该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerClientSubnet

## 备注

## 相关链接

[Add-DnsServerClientSubnet](./Add-DnsServerClientSubnet.md)

[Get-DnsServerClientSubnet](./Get-DnsServerClientSubnet.md)

[Set-DnsServerClientSubnet](./Set-DnsServerClientSubnet.md)

