---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4Failover_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv4failover?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv4Failover
---

# Get-DhcpServerv4Failover

## 摘要
获取DHCP服务器服务上为特定故障转移关系名称配置的故障转移关系信息。

## 语法

### 名称（默认值）
```
Get-DhcpServerv4Failover [-ComputerName <String>] [[-Name] <String[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ScopeId
```
Get-DhcpServerv4Failover [-ComputerName <String>] -ScopeId <IPAddress[]> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DhcpServerv4Failover` cmdlet 用于获取在动态主机配置协议（DHCP）服务器服务上配置的故障转移关系，具体针对指定的故障转移关系名称。如果未指定 `Name` 参数，该 cmdlet 会返回 DHCP 服务器服务上定义的所有故障转移关系；如果 `Name` 参数与任何已存在的故障转移关系不匹配，则会为该参数值返回一个无法终止的错误信息。

如果指定了 *ScopeId* 参数，那么将会返回包含指定范围的故障转移关系。*ScopeId* 参数的值应该代表相应的故障转移范围。

## 示例

### 示例 1：获取关系的故障转移信息
```
PS C:\> Get-DhcpServerv4Failover -ComputerName "dhcpserver.contoso.com" -Name "SFO-SIN-Failover"
```

这个示例获取了名为“SFO-SIN-Failover”的关系在dhcpserver.contoso.com计算机上运行的DHCP服务器服务上的故障转移关系信息。

### 示例 2：获取所有关系的故障转移信息
```
PS C:\> Get-DhcpServerv4Failover -ComputerName "dhcpserver.contoso.com"
```

这个示例获取了在名为dhcpserver.contoso.com的计算机上运行的DHCP服务器服务上的所有故障转移关系相关的信息。

### 示例 3：获取包含作用域（scope）的关系对象的故障转移信息
```
PS C:\> Get-DhcpServerv4Failover -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0
```

这个示例用于获取与范围为 10.10.10.0 的故障转移关系相关的信息。这些信息来自运行在名为 dhcpserver.contoso.com 的计算机上的 DHCP 服务器服务。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行那些需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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
指定运行DHCP服务器服务的目标计算机的DNS名称、IPv4地址或IPv6地址。

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

### -Name
指定一个或多个用于返回属性的故障转移关系的名称。

```yaml
Type: String[]
Parameter Sets: Name
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScopeId
指定一个或多个范围标识符（ID），采用IPv4地址格式。系统会返回与这些范围关联的DHCP服务器服务上的故障转移关系的相关属性信息。

```yaml
Type: IPAddress[]
Parameter Sets: ScopeId
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或整个计算机。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Failover[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

## 备注

## 相关链接

[Add-DhcpServerv4Failover](./Add-DhcpServerv4Failover.md)

[Add-DhcpServerv4FailoverScope](./Add-DhcpServerv4FailoverScope.md)

[Invoke-DhcpServerv4FailoverReplication](./Invoke-DhcpServerv4FailoverReplication.md)

[Remove-DhcpServerv4Failover](./Remove-DhcpServerv4Failover.md)

[Remove-DhcpServerv4FailoverScope](./Remove-DhcpServerv4FailoverScope.md)

[Set-DhcpServerv4Failover](./Set-DhcpServerv4Failover.md)

