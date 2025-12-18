---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv6FreeIPAddress_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv6freeipaddress?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv6FreeIPAddress
---

# 获取 DHCP Server v6 的免费 IP 地址

## 摘要
从指定的范围内获取一个或多个免费或未分配的IPv6地址。

## 语法

```
Get-DhcpServerv6FreeIPAddress [-ComputerName <String>] [-Prefix] <IPAddress> [[-NumAddress] <UInt32>]
 [-StartAddress <IPAddress>] [-EndAddress <IPAddress>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DhcpServerv6FreeIPAddress` cmdlet 从指定的范围内获取一个或多个免费的 IPv6 地址。

如果您指定了*NumAddress*参数，系统会返回所需数量的免费IPv6地址；如果没有指定该参数，则仅返回一个免费的IPv6地址。返回的免费IPv6地址的最大数量被限制为1024个。

如果您指定了*StartAddress*参数但没有指定*EndAddress*参数，系统将返回从*StartAddress*值开始、直到该作用域内的IPv6地址范围结束为止的所有可用IPv6地址。

如果您指定了*EndAddress*参数而没有指定*StartAddress*参数，系统将返回从该作用域的IPv6地址范围起始处开始、直到*EndAddress*参数值为止的所有可用IPv6地址。

如果您同时指定了 *StartAddress*（起始地址）和 *EndAddress*（结束地址）参数，系统将返回位于这两个指定值之间的所有可用 IPv6 地址。

在返回免费的IPv6地址时，以下内容将被排除在外：排除地址范围、已预定的租赁资源、处于活动状态的租赁资源、已被提供的租赁资源以及那些状态不佳或已被拒绝的租赁资源。

在返回免费的IPv6地址时，会包含与该策略关联的IPv6地址范围信息。

在返回免费的IPv6地址时，系统中也会包含那些已经过期或处于“失效”状态的IPv6地址。

如果无法找到所需数量的免费IPv6地址，系统会显示一条警告信息。

## 示例

### 示例 1：获取一个免费的地址
```
PS C:\> Get-DhcpServerv6FreeIPAddress -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020::
```

这个示例从指定的范围内获取一个免费的 IPv6 地址。

### 示例 2：获取十个免费的电子邮件地址
```
PS C:\> Get-DhcpServerv6FreeIPAddress -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -NumAddress 10
```

这个示例从指定的范围内获取了10个免费的IPv6地址。

### 示例 3：从某个地址范围内获取一个免费的地址
```
PS C:\> Get-DhcpServerv6FreeIPAddress -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -StartAddress 2001:4898:7020:1020::10 -EndAddress 2001:4898:7020:1020::50
```

这个示例从指定的范围内获取一个免费的 IPv6 地址。该范围位于 IP 地址范围内，即从 2001:4898:7020:1020::10 到 2001:4898:7020:1020::50。

## 参数

### -AsJob
将该cmdlet作为后台作业运行。使用此参数来执行那些需要较长时间才能完成的任务。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称，或者提供一个会话对象（例如，通过[New-CimSession](/powershell/module/cimcmdlets/new-cimsession)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话结果）。

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
指定运行动态主机配置协议（DHCP）服务器服务的目标计算机的DNS名称，或IPv4地址或IPv6地址。

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

### -EndAddress
指定用于返回可用 IPv6 地址的范围的结束 IPv6 地址。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NumAddress
指定所请求的可用 IPv6 地址的数量。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: 1
Accept pipeline input: False
Accept wildcard characters: False
```

### -Prefix
指定请求一个或多个可用 IPv6 地址的范围所对应的 IPv6 子网前缀。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StartAddress
指定用于返回可用 IPv6 地址的范围的起始 IPv6 地址。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最优限制值。这个限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

## 输出

### System.String[]

## 备注

## 相关链接

[Get-DhcpServerv4FreeIPAddress](./Get-DhcpServerv4FreeIPAddress.md)
