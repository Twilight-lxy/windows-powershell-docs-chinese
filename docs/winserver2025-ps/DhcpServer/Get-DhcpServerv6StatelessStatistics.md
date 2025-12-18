---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv6StatelessStatistics_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv6statelessstatistics?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv6StatelessStatistics
---

# 获取 DHCP Server v6 无状态统计信息

## 摘要
获取包含无状态客户端的 IPv6 子网前缀，以及每个子网中正在使用的地址数量。

## 语法

```
Get-DhcpServerv6StatelessStatistics [-ComputerName <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DhcpServerv6StatelessStatistics` cmdlet 可以获取包含无状态客户端的 IPv6 子网前缀列表，以及每个子网中使用的地址数量。

## 示例

### 示例 1：从 DHCP 服务器服务中获取无状态统计信息
```
PS C:\> Get-DhcpServerv6StatelessStatistics -ComputerName "dhcpserver.contoso.com"
```

这个示例从名为dhcpserver.contoso.com的计算机上运行的DHCP服务器服务中获取与该网络上所有IPv6前缀相关的DHCPv6服务器服务的IPv6统计信息。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用`*-Job` cmdlets系列；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定目标计算机的DNS名称，或其IPv4或IPv6地址。该计算机运行动态主机配置协议（DHCP）服务器服务。

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
该参数用于指定可以同时运行的命令（cmdlet）的最大数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该命令的最佳执行限制（即并发操作的最大数量）。此限制仅适用于当前执行的命令，而不影响整个会话或整个计算机。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6StatelessStatistics[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DhcpServerv6StatelessStore](./Get-DhcpServerv6StatelessStore.md)

[Set-DhcpServerv6StatelessStore](./Set-DhcpServerv6StatelessStore.md)

