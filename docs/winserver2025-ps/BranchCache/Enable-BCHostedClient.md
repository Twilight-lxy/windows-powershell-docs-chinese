---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BranchCacheOrchestrator.cdxml-help.xml
Module Name: BranchCache
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/branchcache/enable-bchostedclient?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-BCHostedClient
---

# 启用BCH托管客户端

## 摘要
将 BranchCache 配置为以托管缓存客户端模式运行。

## 语法

### ServerNames（默认值）
```
Enable-BCHostedClient [-Force] [-ServerNames] <String[]> [-UseVersion <HostedCacheVersion>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 使用SCP
```
Enable-BCHostedClient [-Force] [-UseSCP] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-BCHostedClient` cmdlet 用于将 BranchCache 配置为以托管缓存客户端模式运行。

## 示例

### 示例 1：启用主机缓存客户端模式
```
PS C:\> Enable-BCHostedClient -ServerNames "HC.contoso.com" -UseVersion Windows7
```

此命令启用托管缓存客户端模式，使用 HC.contos.com 作为托管缓存服务器。对于 HTTPS 连接，请选择 Windows® 7 模式（`Windows7`）。

### 示例 2：为两台服务器启用主机缓存客户端模式
```
PS C:\> Enable-BCHostedClient -ServerNames "HC1.contoso.com","HC2.contoso.com" -UseVersion Windows8
```

此命令启用托管缓存客户端模式，并使用两台托管缓存服务器：HC1.contoso.com 和 HC2.contoso.com。对于 HTTP 请求，請使用 Windows 8 模式（`Windows8`）。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该 cmdlet。请输入一个计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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
在运行cmdlet之前会提示您确认是否要执行该操作。

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
强制命令运行，而无需询问用户确认。

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

### -ServerNames
指定客户端计算机可以用来存储和获取内容的托管缓存服务器的名称。

```yaml
Type: String[]
Parameter Sets: ServerNames
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值为`0`，那么Windows PowerShell®将根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。此限制仅适用于当前运行的cmdlet，而不适用于整个会话或计算机本身。

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

### -UseSCP
表示客户端应使用服务连接点（Service Connection Point，简称SCP）来查找托管的缓存服务器。服务连接点是 Active Directory 中用于发布特定服务数据的对象；托管的缓存服务器可以将其关联的服务连接点对象注册到其所所在的 Active Directory 站点中。这一操作是通过 **Enable-BCHostedServer** cmdlet 中的 *RegisterSCP* 参数来实现的。

如果指定了此参数，那么这台计算机会尝试通过搜索SCP（Secure Copy Protocol）来自动发现与所分配的活动目录站点相关联的托管缓存服务器。

```yaml
Type: SwitchParameter
Parameter Sets: UseSCP
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseVersion
指定在联系该托管缓存服务器时使用的报价协议版本。

此参数用于控制客户端在与托管缓存服务器通信时应使用哪种协议。值 `Windows8` 表示客户端使用 HTTP 协议；值 `Windows7` 表示客户端使用 HTTPS 协议。如果未指定此参数但提供了托管缓存服务器的名称，则系统会默认使用 `Windows8` 作为协议。如果同时指定了 `UseSCP` 参数，那么系统将使用 `Windows7` 作为协议。

运行 Windows Server® 2012 的托管缓存服务器无需注册证书；客户端计算机可以通过在 TCP 端口 `80` 上使用 HTTP 协议来与这些服务器进行通信，以存储或获取内容。但是，基于 Windows® 7 的托管缓存服务器必须注册证书，并且只有当客户端计算机在 TCP 端口 `443` 上使用 HTTPS 协议时才能与之建立连接。

注意：基于 Windows® 7 的计算机只能通过 HTTPS 协议与托管缓存服务器进行通信。因此，可以配置运行 Windows Server 2012 的托管缓存服务器以同时接受 HTTP 和 HTTPS 请求，这样该托管缓存服务器就能与基于 Windows® 7 的计算机以及运行 Windows® 8 的客户端计算机协同工作。

```yaml
Type: HostedCacheVersion
Parameter Sets: ServerNames
Aliases:
Accepted values: Windows7, Windows8

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Enable-BCHostedServer](./Enable-BCHostedServer.md)

