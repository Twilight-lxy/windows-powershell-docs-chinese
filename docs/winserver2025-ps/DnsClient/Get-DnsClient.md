---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DnsClient.cdxml-help.xml
Module Name: DnsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsclient/get-dnsclient?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsClient
---

# Get-DnsClient

## 摘要
获取指定计算机上配置的网络接口的详细信息。

## 语法

```
Get-DnsClient [-InterfaceIndex <UInt32[]>] [[-InterfaceAlias] <String[]>]
 [-ConnectionSpecificSuffix <String[]>] [-RegisterThisConnectionsAddress <Boolean[]>]
 [-UseSuffixWhenRegistering <Boolean[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-DnsClient` cmdlet 可以获取指定计算机上不同网络接口的特定配置信息。

## 示例

### 示例 1：获取网络接口配置
```
PS C:\> Get-DnsClient
```

该命令可以获取计算机上网络接口的配置详细信息。

### 示例 2：为计算机设置 DNS 服务器的 IP 地址
```
PS C:\> $dnsClient1 = Get-DnsClient -InterfaceAlias "Wired Ethernet Connection"
PS C:\> Set-DnsClientServerAddress -InputObject $dnsClient1 -ServerAddresses ("10.0.0.1","10.0.0.2")

This is a version of the cmdlet using the pipeline.
PS C:\> Get-DnsClient | Set-DnsClientServerAddress -ServerAddresses ("10.0.0.1","10.0.0.2")
```

此命令为计算机上所有有线以太网连接设置DNS服务器的IP地址。

### 示例 3：将 DNS 客户端重置为使用 DHCP 指定的默认 DNS 服务器地址
```
PS C:\> Get-DnsClient | Set-DnsClientServerAddress -ResetServerAddresses
```

这个命令会将所有网络接口的重置为使用DHCP指定的DNS服务器地址。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中操作。要管理作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -ConnectionSpecificSuffix
指定需要追加的、与特定连接相关的后缀。此参数表示每个连接对应的DNS后缀，它会被添加到计算机名称之后，从而构成一个完全限定域名（FQDN）。该FQDN将作为DNS客户端进行名称解析时使用的主机名。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: Suffix

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InterfaceAlias
指定该接口的友好名称（即用户易于理解的名称）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InterfaceIndex
指定接口的索引编号。

```yaml
Type: UInt32[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -RegisterThisConnectionsAddress
指定此接口的注册策略。

此参数表示计算机是否应自动将与此连接关联的IP地址注册到DNS服务器上。

```yaml
Type: Boolean[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -UseSuffixWhenRegistering
指定此接口的注册后缀策略。

此参数用于指示在注册 IP 地址时是否必须使用后缀。

```yaml
Type: Boolean[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root\StandardCimv2\MSFT_DNSClient
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root\StandardCimv2\MSFT_DNSClientServerAddress
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root\StandardCimv2\MSFT_NetAdapter
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root\StandardCimv2\MSFT_NetIPInterface
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root\StandardCimv2\MSFT_DNSClient
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Register-DnsClient](./Register-DnsClient.md)

[Set-DnsClient](./Set-DnsClient.md)

