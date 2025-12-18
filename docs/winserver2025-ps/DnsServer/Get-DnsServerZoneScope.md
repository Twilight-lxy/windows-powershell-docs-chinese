---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerZoneScope_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/get-dnsserverzonescope?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsServerZoneScope
---

# Get-DnsServerZoneScope

## 摘要
获取DNS服务器上某个区域的权限范围（scopes）。

## 语法

```
Get-DnsServerZoneScope [-ZoneName] <String> [-ComputerName <String>] [[-Name] <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsServerZoneScope` cmdlet 可用于获取域名系统（DNS）服务器上现有区域的权限范围。该 cmdlet 默认返回所有可用的权限范围；如果需要获取特定范围的详细信息，可以指定所需的权限范围名称。

## 示例

### 示例 1：获取所有区域范围（zone scopes）
```
PS C:\> Get-DnsServerZoneScope -ZoneName "contoso.com"
ZoneScope            FileName
---------            --------
contoso.com          contoso.com.dns
contoso_NorthAmerica contoso_NorthAmerica.dns
contoso_Europe       contoso_Europe.dns
```

这个命令会获取名为 contoso.com 的区域中的所有作用域（scopes）。

### 示例 2：通过名称获取区域范围
```
PS C:\> Get-DnsServerZoneScope -ZoneName "contoso.com" -Name "contoso_Europe"
ZoneScope            FileName
---------            --------
contoso_Europe       contoso_Europe.dns
```

这个命令用于获取名为“contoso_Europe”的作用域（scope），该作用域属于指定的区域（zone）。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Name
指定要获取的作用域名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ZoneScope

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大操作数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前运行的 cmdlet，而不影响整个会话或计算机本身的运行状态。

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
用于指定一个区域的名称。此cmdlet会从该参数所指定的区域中获取相应的区域信息。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsZoneScope[]

## 备注

## 相关链接

[Add-DnsServerZoneScope](./Add-DnsServerZoneScope.md)

[Remove-DnsServerZoneScope](./Remove-DnsServerZoneScope.md)

