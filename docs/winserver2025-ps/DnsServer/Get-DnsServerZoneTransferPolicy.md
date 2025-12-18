---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerZoneTransferPolicy_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/get-dnsserverzonetransferpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsServerZoneTransferPolicy
---

# Get-DnsServerZoneTransferPolicy

## 摘要
获取DNS服务器上的区域传输策略。

## 语法

### 服务器（默认设置）
```
Get-DnsServerZoneTransferPolicy [[-Name] <String>] [-ComputerName <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 区域（Zone）
```
Get-DnsServerZoneTransferPolicy [[-Name] <String>] [-ComputerName <String>] [-ZoneName] <String>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsServerZoneTransferPolicy` cmdlet 用于获取域名系统（DNS）服务器上的区域传输策略。可以通过名称指定某个区域以获取该区域的策略；如果未指定区域，则此 cmdlet 会获取服务器级别的策略。

## 示例

### 示例 1：获取所有服务器级别的区域传输策略
```
PS C:\> Get-DnsServerZoneTransferPolicy
Name                                 ProcessingOrder                      IsEnabled                            Action
----                                 ---------------                      ---------                            ------
NorthAmericaPolicy                   1                                    True                                 Ignore
InternalTransfers                    2                                    True                                 Ignore
```

这个cmdlet可以获取所有服务器级别的区域传输策略（zone transfer policies）。

### 示例 2：获取某个区域的所有区域传输策略
```
PS C:\> Get-DnsServerZoneTransferPolicy -ZoneName "contoso.com"
Name                                 ProcessingOrder                      IsEnabled                            Action
----                                 ---------------                      ---------                            ------
InternalTransfers                    1                                    True                                 Ignore
```

此命令可以获取名为“contoso.com”的区域的所有区域传输策略信息。

### 示例 3：获取特定区域的策略设置
```
PS C:\> Get-DnsServerZoneTransferPolicy -ZoneName "contoso.com" -Name "InternalTransfers"
Name                                 ProcessingOrder                      IsEnabled                            Action
----                                 ---------------                      ---------                            ------
InternalTransfers                    1                                    True                                 Ignore
```

该命令用于获取名为“contoso.com”的区域中的区域传输策略（该策略的名称为“InternalTransfers”）。

### 示例 4：获取服务器级别的区域传输策略
```
PS C:\> Get-DnsServerZoneTransferPolicy -Name "InternalTransfers"
Name                                 ProcessingOrder                      IsEnabled                            Action
----                                 ---------------                      ---------                            ------
InternalTransfers                    2                                    True                                 Ignore
```

这个命令用于获取名为“InternalTransfers”的服务器级区域传输策略。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的数值，例如完全 Qualified Domain Name（FQDN）、主机名或NETBIOS名称。

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
指定要获取的策略的名称。

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
指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -ZoneName
用于指定DNS区域的名称。此cmdlet会从这个参数指定的区域中获取相应的策略信息。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerPolicy[]

## 备注

## 相关链接

[Add-DnsServerZoneTransferPolicy](./Add-DnsServerZoneTransferPolicy.md)

[Remove-DnsServerZoneTransferPolicy](./Remove-DnsServerZoneTransferPolicy.md)

[Set-DnsServerZoneTransferPolicy](./Set-DnsServerZoneTransferPolicy.md)

[开始DNS服务器区域传输](./Start-DnsServerZoneTransfer.md)

[Add-DnsServerQueryResolutionPolicy](./Add-DnsServerQueryResolutionPolicy.md)

