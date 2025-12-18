---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServer_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/set-dnsserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DnsServer
---

# Set-DnsServer

## 摘要
覆盖DNS服务器配置。

## 语法

```
Set-DnsServer [-InputObject] <CimInstance> [-ComputerName <String>] [-Force] [-CreateFileBackedPrimaryZones]
 [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-DnsServer` cmdlet 使用一个输入对象来覆盖指定的域名系统（DNS）服务器配置。你可以通过使用以下任意一个 cmdlet 生成的 XML 文件来创建该输入对象：`Get-DnsServer`、`Export-Clixml` 或 `Import-Clixml`。

有关 **Export-Clixml** 的更多信息，请参阅 [Export-Clixml](https://technet.microsoft.com/en-us/library/hh849916.aspx)。有关 **Import-Clixml** 的更多信息，请参阅 [Import-Clixml](https://technet.microsoft.com/en-us/library/hh849906.aspx)。

## 示例

### 示例 1：使用输入对象覆盖 DNS 服务器配置
```
PS C:\> Get-DnsServer -ComputerName "DNSServer13.Contoso.com" | Export-Clixml -Path "c:\DnsServerConfig.xml"
PS C:\> $x = Import-Clixml "c:\DnsServerConfig.xml"
PS C:\> Set-DnsServer -InputObject $x -ComputerName "DNSServer22.Contoso.com"
```

这组命令使用一个输入对象来覆盖DNS服务器的配置信息。

如代码块所示，第一个命令使用 **Get-DnsServer** cmdlet 获取 DNS 服务器配置信息，然后将这些信息传递给 **Export-Clixml** cmdlet，后者将这些数据导出到一个 XML 文件中。

第二条命令将XML文件的数据获取并存储到变量$x$中。

第三个命令使用存储在变量$x`中的数据来覆盖现有的DNS服务器配置。

### 示例 2：使用 Cimsession 参数设置 DNS 服务器配置
```
PS C:\> Get-DnsServer -CimSession 172.22.50.137 | Set-DnsServer
```

此命令从 IP 地址为 172.22.50.137 的服务器获取 DNS 服务器配置，并将其应用到运行 **Set-DnsServer** cmdlet 的服务器上。

### 示例 3：使用 IP 地址迁移 DNS 服务器配置
```
PS C:\> Get-DnsServer -CimSession 172.22.50.137 | Set-DnsServer -ComputerName 172.22.50.138
```

该命令将DNS服务器配置从IP地址为172.22.50.137的服务器迁移到IP地址为172.22.50.138的服务器上。

### 示例 4：创建一个基于文件的主区域（primary zone）
```
PS C:\> Get-DnsServer -CimSession 172.22.50.137 | Set-DnsServer -CreateFileBackedPrimaryZones
```

此命令在指定的本地DNS服务器上创建基于文件的primary zone（主区域）。包含资源记录的文件必须位于%windir%\system32\dns目录中。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` 系列的 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet将在本地计算机的当前会话中执行。

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
指定一个 DNS 服务器。此参数的可接受值为：IP v4 地址；IP v6 地址；任何能够解析为 IP 地址的其他值，例如完全限定域名（FQDN）、主机名或 NETBIOS 名称。

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
在运行cmdlet之前会提示您确认是否要继续执行该操作。

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

### -CreateFileBackedPrimaryZones
这表示您必须在输入对象中创建新的、基于文件的主区域（primary zones）。包含资源记录的文件必须位于 `%windir%\system32\dns` 目录下。

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

### -Force
在 cmdlet 执行操作之前，会覆盖默认的确认设置。

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

### -InputObject
指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给此 cmdlet。

```yaml
Type: CimInstance
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此 cmdlet 不会生成任何输出。

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
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最优限制值。此限制仅适用于当前执行的cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServer

## 备注

## 相关链接

[Get-DnsServer](./Get-DnsServer.md)

[测试DNS服务器](./Test-DnsServer.md)

