---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4DnsSetting_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv4dnssetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv4DnsSetting
---

# Get-DhcpServerv4DnsSetting

## 摘要
获取在DHCP服务器服务上为特定范围、预留资源或服务器级别配置的DNS设置信息。

## 语法

```
Get-DhcpServerv4DnsSetting [[-IPAddress] <IPAddress>] [[-ScopeId] <IPAddress>] [-ComputerName <String>]
 [-PolicyName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DhcpServerv4DnsSetting` cmdlet 可用于获取动态主机配置协议（DHCP）服务器服务上针对特定范围、预留地址或服务器级别所配置的 DNS 设置。

如果您既没有指定 *ScopeId* 参数，也没有指定 *IPAddress* 参数，系统将返回来自服务器级别的DNS更新设置。

这个cmdlet用于获取指定级别（如预留、范围或服务器）上的有效DNS设置。如果在指定级别上未配置DNS设置值，则会从上级级别中获取相应的DNS设置（如果这些设置已被配置的话）。如果在服务器级别上没有指定DNS设置，那么系统会返回DHCP服务器服务在DNS更新方面的默认行为。

## 示例

### 示例 1：获取服务器级别的 DNS 注册设置
```
PS C:\> Get-DhcpServerv4DnsSetting -ComputerName "dhcpserver.contoso.com"
```

这个示例用于获取名为 dhcpserver.contoso.com 的计算机上的 DHCPv4 服务器级或全服务器范围的 DNS 注册设置。

### 示例 2：获取某个范围内的服务器级别 DNS 注册设置
```
PS C:\> Get-DhcpServerv4DnsSetting -ComputerName "dhcpserver.contoso.com" -ScopeId 10.10.10.0
```

这个示例用于配置名为dhcpserver.contoso.com的计算机上的DNS注册设置，该设置的生效范围是10.10.10.0。

### 示例 3：获取某个地址的服务器级 DNS 注册设置
```
PS C:\> Get-DhcpServerv4DnsSetting -ComputerName "dhcpserver.contoso.com" -IPAddress 10.10.10.10
```

这个示例用于配置名为dhcpserver.contoso.com的计算机上的DNS注册设置，以便为预留的IP地址10.10.10.10使用该设置。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行耗时较长的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成过程中，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

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
指定运行DHCP服务器服务的目标计算机的DNS名称、IPv4地址或IP6地址。

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
指定用于获取DNS更新设置的预订记录的IP地址。

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

### -PolicyName
指定策略的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScopeId
指定用于获取DNS更新设置的范围内标识符（ID）的范围，该标识符采用IPv4地址格式表示。

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
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4 Reservation
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4DnsSetting
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Set-DhcpServerv4DnsSetting](./Set-DhcpServerv4DnsSetting.md)

