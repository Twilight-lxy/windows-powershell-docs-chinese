---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsNamespaceServerConfig.cdxml-help.xml
Module Name: DFSN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsn/set-dfsnserverconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DfsnServerConfiguration
---

# Set-DfsnServerConfiguration

## 摘要
更改DFS命名空间根服务器的设置。

## 语法

```
Set-DfsnServerConfiguration [-ComputerName] <String> [[-SyncIntervalSec] <UInt32>]
 [[-EnableSiteCostedReferrals] <Boolean>] [[-EnableInsiteReferrals] <Boolean>]
 [[-LdapTimeoutSec] <UInt32>] [[-PreferLogonDC] <Boolean>] [[-UseFqdn] <Boolean>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Set-DfsnServerConfiguration` cmdlet 用于更改分布式文件系统（DFS）命名空间根服务器的设置。一个 DFS 命名空间根服务器会托管一个或多个命名空间根目标对象。

您可以使用此 cmdlet 启用站内引用功能，或者根据站点中的目标来组织引用操作。此外，还可以更改连接到主域控制器（PDC）模拟器的服务器的同步间隔，以及调整轻量级目录访问协议（LDAP）的超时设置。您可以指定引用信息是优先使用哪个登录域控制器；同时也可以指定服务器是以完全 Qualified Domain Name (FQDN) 的形式还是以 NETBios 名称的形式提供引用信息的。

要查看这些设置的当前值，请使用 **Get-DfsnServerConfiguration** cmdlet。

## 示例

### 示例 1：为 DFS 命名空间服务器设置 LDAP 超时时间

```powershell
Set-DfsnServerConfiguration -ComputerName 'localhost' -LdapTimeoutSec 60
```

此命令为本地计算机（该计算机是一台DFS命名空间服务器）设置了60秒的LDAP超时值。

## 参数

### -AsJob

将此 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

```yaml
Type: Microsoft.Management.Infrastructure.CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName

指定要修改其设置的 DFS 命名空间服务器的主机名称或完全 qualified domain name (FQDN)。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: Server, name, NamespaceServer

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm

在运行该 cmdlet 之前，会提示您进行确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableInsiteReferrals

该字段用于指示服务器是否仅提供同一网站内的推荐链接。如果将值设置为 `$true`，则服务器只会返回与客户端位于相同网站内的目标相关的推荐链接；如果将值设置为 `$false$`，则服务器会同时返回同一网站内的推荐链接以及其他来源的推荐链接。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: insite

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableSiteCostedReferrals

该属性用于指示服务器是否支持基于成本的选择机制。如果您指定值为 `$true`，则 DFS 命名空间服务器会按以下顺序为客户端提供文件夹目标的引用：

- Folder targets in the same site as a client, in random order.
- Folder targets for which the DFS namespace server has information. The referrals for the nearest
  site are first, in random order, followed by the next nearest site, in random order.
- Targets for which DFS namespace server has no site information, in random order.

如果您指定值为 `$false`，DFS命名空间服务器将按以下顺序为客户端提供文件夹目标的引用：

- Folder targets in the same site as the client, in random order.
- Other folder targets, in random order.

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: Sitecosted, SiteCostedReferrals

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LdapTimeoutSec

为分布式文件系统（DFS）命名空间服务器的轻量级目录访问协议（LDAP）请求指定一个超时值，单位为秒。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: LdapTimeout

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PreferLogonDC

该参数用于指示在引用过程中是否优先选择登录域控制器。如果您为该参数指定 `$true` 的值，DFS 命名空间服务器会将指向登录域控制器的引用置于引用列表的最前面。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 5
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SyncIntervalSec

指定一个以秒为单位的间隔时间。该间隔时间决定了基于域的DFS命名空间根服务器和域控制器与PDC模拟器连接的频率，以便获取DFS命名空间元数据的更新信息。

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: SyncInterval

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前执行的 cmdlet，而不影响整个会话或计算机本身。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseFqdn

该参数用于指示DFS命名空间服务器在引用（referrals）过程中是否使用FQDN。如果参数值为`$true`，则表示服务器在引用时使用FQDN；如果参数值为`$false`，则表示服务器使用NetBIOS名称。DFS命名空间服务器的默认设置是在引用时使用NetBIOS名称。

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases: Fqdn, dfsdnsconfig, UseFullyQualifiedDomainNames

Required: False
Position: 6
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf

展示了如果该cmdlet运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.UInt32

### System(Boolean)

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接

[Get-DfsnServerConfiguration](./Get-DfsnServerConfiguration.md)
