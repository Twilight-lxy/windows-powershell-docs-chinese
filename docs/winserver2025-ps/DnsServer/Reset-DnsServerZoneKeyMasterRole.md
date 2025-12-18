---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerZoneKeyMasterRole_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/reset-dnsserverzonekeymasterrole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Reset-DnsServerZoneKeyMasterRole
---

# 重置 DNS 服务器区域密钥主角色

## 摘要
转移DNS区域的密钥管理角色（Key Master）。

## 语法

```
Reset-DnsServerZoneKeyMasterRole [-ZoneName] <String> [-Force] [[-KeyMasterServer] <String>] [-SeizeRole]
 [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Reset-DnsServerZoneKeyMasterRole` cmdlet 用于转移 DNS 安全（DNSSEC）密钥主服务器的角色。任何托管该区域主要副本的权威域名系统（DNS）服务器都可以作为密钥主服务器。

此cmdlet尝试连接到当前的Key Master服务器。如果无法连接到该服务器，则除非您指定了“SeizeRole”，否则该cmdlet不会执行任何更改。

除非使用了 **Force** 切换开关，否则此cmdlet在转移角色之前会提示用户进行确认。

## 示例

#### 示例 1：转移角色
```
PS C:\> Reset-DnsServerZoneKeyMasterRole -ZoneName "west01.contoso.com" -KeyMasterServer "root.contoso.com"
```

此命令将名为west01.contoso.com的区域的密钥管理器（Key Master）角色转移到名为keys.contoso.com的服务器上。如果该cmdlet无法与当前的密钥管理器服务器进行验证，那么它将不会执行角色的转移操作。

### 示例 2：转移所需的角色
```
PS C:\> Reset-DnsServerZoneKeyMasterRole -ZoneName "west01.contoso.com" -KeyMasterServer "keys.contoso.com" -SeizeRole
```

此命令将名为 west01.contoso.com 的区域的密钥主控角色（Key Master role）转移到名为 keys.contoso.com 的服务器上。即使该 cmdlet 无法与当前的密钥主控服务器进行验证，它仍会执行角色转移操作。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
该命令会直接转移角色，而不会询问您是否确认。默认情况下，此cmdlet在执行操作之前会先提示您进行确认。

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

### -KeyMasterServer
指定DNS服务器的名称。可以使用NetBIOS名称、IP地址或完全限定域名。该cmdlet会将此服务器设置为指定区域的关键主机（Key Master）服务器。指定的区域必须作为主区域存在于DNS服务器上。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
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

### -SeizeRole
表示此cmdlet会夺取“Key Master”角色。除非指定了该开关，否则如果无法连接到当前的“Key Master”服务器，该cmdlet将不会进行任何更改。

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
该参数用于指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最优限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -ZoneName
指定一个区域的名称。此cmdlet会将该区域的关键主机（Key Master）角色进行转移。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.String

## 备注

## 相关链接

