---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerTrustAnchor_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/import-dnsservertrustanchor?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-DnsServerTrustAnchor
---

# 导入DNS服务器信任锚点

## 摘要
导入用于DNS服务器的信任锚点。

## 语法

### KeySet（默认值）
```
Import-DnsServerTrustAnchor [-ComputerName <String>] [-PassThru] [-KeySetFile] <String>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### DSSet
```
Import-DnsServerTrustAnchor [-ComputerName <String>] -DSSetFile <String> [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Import-DnsServerTrustAnchor` cmdlet 用于从指定的文件中导入信任锚点（trust anchor），以便用于域名系统（DNS）服务器。如果您指定了一个密钥集文件，该 cmdlet 会从输入的密钥集文件中导入 DNS 公钥（DNSKEY）记录集。这是默认的参数设置。

如果您指定了一个授权签名者（Delegation Signer，简称DS）配置文件，该cmdlet会从输入的dsset文件中导入相应的DS记录集。如果系统中不存在信任锚点（trust anchor），则在导入数据之前，cmdlet会先创建一个信任锚点。

## 示例

### 示例 1：使用密钥集文件导入信任锚点
```
PS C:\> Import-DnsServerTrustAnchor -KeySetFile "C:\Windows\System32\dns\keyset-west.contoso.com" -PassThru -Verbose
```

此命令使用指定的密钥集文件，为名为 west.contoso.com 的区域导入一个信任锚点。

### 示例 2：使用 DS 集合文件导入信任记录
```
PS C:\> Import-DnsServerTrustAnchor -DSSetFile "C:\Windows\System32\dns\dsset-west.contoso.com" -PassThru -Verbose
```

此命令使用指定的 DNS 配置文件（DS 配置文件），为名为 west.contoso.com 的区域导入一个信任锚点（即 DNS 记录）。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如使用[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个远程DNS服务器。请提供该DNS服务器的IP地址，或任何能够解析为IP地址的值，例如完全qualified域名（FQDN）、主机名或NETBIOS名称。

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

### -DSSetFile
指定一个DS集文件的路径。

```yaml
Type: String
Parameter Sets: DSSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -KeySetFile
指定密钥集文件的路径。

```yaml
Type: String
Parameter Sets: KeySet
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个对象，代表您正在操作的该项。默认情况下，此cmdlet不会生成任何输出。

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算一个最佳的限流值。该限流值仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并未执行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerTrustAnchor[]

## 备注

## 相关链接

[Add-DnsServerTrustAnchor](./Add-DnsServerTrustAnchor.md)

[Get-DnsServerTrustAnchor](./Get-DnsServerTrustAnchor.md)

[Remove-DnsServerTrustAnchor](./Remove-DnsServerTrustAnchor.md)

