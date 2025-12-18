---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4FreeIPAddress_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv4freeipaddress?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv4FreeIPAddress
---

# Get-DhcpServerv4FreeIPAddress

## 摘要
从指定的范围内获取一个或多个免费或未分配的IPv4地址。

## 语法

```
Get-DhcpServerv4FreeIPAddress [-ComputerName <String>] [-ScopeId] <IPAddress> [[-NumAddress] <UInt32>]
 [-StartAddress <IPAddress>] [-EndAddress <IPAddress>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

## 描述
这个 `Get-DhcpServerv4FreeIPAddress` cmdlet 可以从指定的范围内获取一个或多个空闲的 IP 地址。

如果您指定了 *NumAddress* 参数，系统会返回所需数量的可用 IPv4 地址；如果没有指定该参数，则仅返回一个可用 IP 地址。系统返回的可用 IP 地址的最大数量被限制为 1024 个。

如果您指定了*StartAddress*参数而没有指定*EndAddress*参数，系统将返回从*StartAddress*值开始的所有可用IP地址，直到该IP地址范围内的最后一个地址为止。

如果您指定了 *EndAddress* 参数而未指定 *StartAddress* 参数，系统将返回从该作用域的 IP 地址范围起始处开始、直到 *EndAddress* 参数值为止的所有可用 IP 地址。

如果您同时指定了*StartAddress*（起始地址）和*EndAddress*（结束地址）参数，系统将返回位于这两个地址之间的所有可用IP地址。

在返回免费的IP地址时，会排除那些被排除在外的地址范围、已预留的地址、处于活动状态的租赁协议、已被提供的租赁协议，以及那些状态不佳或已被拒绝的租赁协议。

在返回免费的IP地址时，会同时包含与该策略关联的IP地址范围。

在返回免费的IP地址时，那些已经过期或处于失效状态的IP地址也会被包含在内。

如果无法找到所需数量的免费 IP 地址，此 cmdlet 会显示一条警告信息。

## 示例

#### 示例 1：获取一个免费的地址
```
PS C:\> Get-DhcpServerv4FreeIPAddress -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0
```

这个示例从指定的范围内获取免费的IPv4地址。

### 示例 2：获取十个免费地址
```
PS C:\> Get-DhcpServerv4FreeIPAddress -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -NumAddress 10
```

这个示例从指定的范围内获取了10个免费的IPv4地址。

### 示例 3：从指定范围内获取一个免费的地址
```
PS C:\> Get-DhcpServerv4FreeIPAddress -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0 -StartAddress 10.10.10.10 -EndAddress 10.10.10.50
```

这个示例从指定的地址范围内获取一个免费的IPv4地址。该地址范围是10.10.10.10到10.10.10.50。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成过程中，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job` cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，使用的是本地计算机上的当前会话。

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
指定运行动态主机配置协议（DHCP）服务器服务的目标计算机的DNS名称、IPv4地址或IPv6地址。

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
指定用于返回空闲IP地址的范围的结束IP地址。

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
指定所请求的可用IP地址的数量。

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

### -ScopeId
指定一个范围标识符（ID），该标识符采用 IPv4 地址格式，用于请求一个或多个空闲的 IP 地址。

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
指定用于返回空闲IP地址的范围的起始IP地址。

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
该参数用于指定可以同时运行的最大操作数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### System.String[]

## 备注

## 相关链接

[Get-DhcpServerv6FreeIPAddress](./Get-DhcpServerv6FreeIPAddress.md)
