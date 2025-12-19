---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamDnsServer.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamdnsserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamDnsServer
---

# Get-IpamDnsServer

## 摘要
从 IPAM 数据库中获取有关 DNS 服务器的信息。

## 语法

```
Get-IpamDnsServer [[-ServerFqdn] <String[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-IpamDnsServer` cmdlet 可以返回有关在 IPAM（IP 地址管理）服务器数据库中找到的域名系统（DNS）服务器的信息。

## 示例

### 示例 1：获取所有 DNS 服务器的信息
```
PS C:\> Get-IpamDnsServer
```

这个命令会返回有关所有 IPAM DNS 服务器的信息。

### 示例 2：获取有关特定 DNS 服务器的信息
```
PS C:\> Get-IpamDnsServer -ServerFqdn "dns.contoso.com"
```

该命令会返回名为 dns.contoso.com 的单个 IPAM DNS 服务器的相关信息。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的任务。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在该会话中执行其他操作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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

### -ServerFqdn
指定要获取的DNS服务器的全限定域名。例如：

`-ServerFqdn "dns.contoso.com"`

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在执行的 cmdlet，而不影响整个会话或计算机本身。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamDnsServer

此cmdlet返回一个**IpamDnsServer**对象的实例。

## 备注

## 相关链接

[Get-IpamDnsConditionalForwarder](./Get-IpamDnsConditionalForwarder.md)

[Get-IpamDnsResourceRecord](./Get-IpamDnsResourceRecord.md)

[Get-IpamDnsZone](./Get-IpamDnsZone.md)
