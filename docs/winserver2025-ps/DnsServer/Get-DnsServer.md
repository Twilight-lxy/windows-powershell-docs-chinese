---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServer_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/get-dnsserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsServer
---

# Get-DnsServer

## 摘要
检索DNS服务器配置信息。

## 语法

```
Get-DnsServer [-ComputerName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-DnsServer` cmdlet 用于检索域名系统（DNS）服务器的配置信息。

您可以使用管道运算符将 `Get-DnsServer` cmdlet 的输出传递给 `Export-Clixml` cmdlet。该 cmdlet 会生成一个包含 DNS 配置信息的 XML 文件。您可以利用这个 XML 文件来备份 DNS 设置或在不同的计算机之间传输这些设置。有关 `Export-Clixml` 的更多信息，请参阅 [使用 Export-Clixml cmdlet](/powershell/module/microsoft.powershellUTILITY/export-clixml)。

## 示例

### 示例 1：获取 DNS 服务器配置信息
```powershell
PS C:\> Get-DnsServer -ComputerName "10.255.255.254"
```

这个命令用于获取DNS服务器的配置信息。

### 示例 2：获取本地 DNS 服务器配置信息并将其导出
```powershell
PS C:\> Get-DnsServer | Export-Clixml -Path "c:\config\DnsServerConfig.xml"
```

这个命令会获取本地服务器上的DNS服务器配置信息，并将其传递给**Export-Clixml** cmdlet，以便将其转换成XML文件。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
用于指定一个DNS服务器。该参数的可接受值包括：IP V4地址；IP V6地址；以及任何能够解析为IP地址的其他值，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

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

### -ThrottleLimit
指定可以同时运行的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServer

## 备注

## 相关链接

[Set-DnsServer](./Set-DnsServer.md)

[测试DNS服务器](./Test-DnsServer.md)
