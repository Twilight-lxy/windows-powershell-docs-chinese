---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamDnsZone.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamdnszone?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamDnsZone
---

# Get-IpamDnsZone

## 摘要
从 IPAM 数据库中获取有关 DNS 区域的信息。

## 语法

```
Get-IpamDnsZone [-ZoneType] <ZoneType[]> [[-ZoneName] <String[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
**Get-IpamDnsZone** cmdlet 可以获取 IPAM（IP 地址管理）服务器数据库中所有域名系统（DNS）区域的信息。DNS 区域是域名系统中用于表示某个组织的独立部分。例如，`northamerica.contoso.com` 这个 DNS 区域会存储 `contoso.com` 的 `northamerica` 子域的 DNS 记录；同样地，`southamerica.contoso.com` 这个 DNS 区域会存储 `contoso.com` 的 `southamerica` 子域的 DNS 记录。

## 示例

### 示例 1：获取所有前置区域的信息
```
PS C:\> Get-IpamDnsZone -ZoneType "Forward"
```

此命令会返回有关 IPAM 数据库中所有转发区域的信息。

### 示例 2：获取特定 DNS 区域中转发区域的信息
```
PS C:\> Get-IpamDnsZone -ZoneType "Forward" -ZoneName "northamerica.contoso.com"
```

此命令会返回名为 northamerica.contoso.com 的 DNS 区域的相关信息。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，随后再显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -ThrottleLimit
该参数用于指定可以同时执行的命令（cmdlet）的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM 命令（cmdlets）的数量来计算一个最优的限制值。这个限制仅适用于当前正在执行的命令，而不适用于整个会话或计算机本身。

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
指定要返回的DNS区域的名称。例如：

`-ZoneName "northamerica.contoso.com"`

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

### -ZoneType
指定要返回的DNS区域的类型。

此参数的可接受值为：

- Forward.
Resolves host names to IP addresses.
- IPv4Reverse.
Resolves IPv4 addresses to host names.
- IPv6Reverse.
Resolves IPv6 addresses to host names.

例如：

`-ZoneType "IPv4Reverse"`

```yaml
Type: ZoneType[]
Parameter Sets: (All)
Aliases:
Accepted values: Forward, IPv4Reverse, IPv6Reverse

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

### IpamDnsZone

此cmdlet返回一个**IpamDnsZone**对象的实例。

## 备注

## 相关链接

[Get-IpamDnsConditionalForwarder](./Get-IpamDnsConditionalForwarder.md)

[Get-IpamDnsResourceRecord](./Get-IpamDnsResourceRecord.md)

[Get-IpamDnsServer](./Get-IpamDnsServer.md)
