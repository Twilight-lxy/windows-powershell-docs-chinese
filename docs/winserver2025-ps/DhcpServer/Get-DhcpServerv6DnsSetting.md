---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv6DnsSetting_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv6dnssetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv6DnsSetting
---

# Get-DhcpServerv6DnsSetting

## 摘要
用于获取DHCP服务器服务上为特定范围、预留资源或整个服务器配置的DNS设置。

## 语法

```
Get-DhcpServerv6DnsSetting [-ComputerName <String>] [[-Prefix] <IPAddress>] [[-IPAddress] <IPAddress>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DhcpServerv6DnsSetting` cmdlet 可以获取在动态主机配置协议（DHCP）服务器服务上为特定范围、预留地址或整个服务器配置的 DNS 设置。

如果您既没有指定 *Prefix* 参数，也没有指定 *IPAddress* 参数，那么将会获取服务器级别的 DNS 设置。如果您指定了 *Prefix* 或 *IPAddress* 参数，此 cmdlet 会获取指定级别（如预留区、作用域或服务器）的有效 DNS 设置。如果在指定级别没有配置 DNS 设置值，则会从上一层级别获取相应的 DNS 设置（如果这些设置已经被配置的话）。如果在服务器级别没有指定 DNS 设置，系统将会返回 DHCP 服务器服务的默认行为（例如 DNS 更新的相关操作）。

## 示例

#### 示例 1：获取服务器级别的 DNS 注册设置
```
PS C:\> Get-DhcpServerv6DnsSetting -ComputerName "dhcpserver.contoso.com"
```

这个示例获取了DHCPv6服务器级别的或整个服务器范围内的DNS注册设置。

### 示例 2：获取某个范围内的 DNS 注册设置
```
PS C:\> Get-DhcpServerv6DnsSetting -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020::
```

这个示例用于配置作用域 2001:4898:7020:1020:: 的 DNS 注册设置。

#### 示例 3：获取预留地址的 DNS 注册设置
```
PS C:\> Get-DhcpServerv6DnsSetting -ComputerName "dhcpserver.contoso.com" -IPAddress 2001:4898:7020:1020::10
```

这个示例用于配置预分配的IP地址2001:4898:7020:1020:10的DNS注册设置。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 获取的会话对象）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

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
指定运行 DHCP 服务器服务的目标计算机的 DNS 名称、IPv4 地址或 IPv6 地址。

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

### -IPAddress
指定用于获取DNS设置的预留资源的IPv6地址。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases: ReservedIP

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Prefix
指定用于获取DNS设置的IPv6地址范围的子网前缀。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6 Reservation
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6DnsSetting
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Set-DhcpServerv6DnsSetting](./Set-DhcpServerv6DnsSetting.md)

