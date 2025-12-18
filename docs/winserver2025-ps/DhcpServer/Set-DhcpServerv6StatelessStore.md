---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv6StatelessStore_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/set-dhcpserverv6statelessstore?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DhcpServerv6StatelessStore
---

# Set-DhcpServerv6StatelessStore

## 摘要
设置用于某个 IPv6 前缀的 IPv6 无状态存储（stateless store）的相关属性。

## 语法

```
Set-DhcpServerv6StatelessStore [[-Prefix] <IPAddress>] [[-Enabled] <Boolean>] [[-PurgeInterval] <TimeSpan>]
 [-ComputerName <String>] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DhcpServerv6StatelessStore` 这个 cmdlet 用于设置指定 IPv6 前缀对应的 IPv6 无状态存储（stateless store）的属性。如果未指定 `Prefix` 参数，那么将设置服务器级别的 IPv6 无状态存储的属性。

## 示例

### 示例 1：为某个作用域启用无状态存储
```
PS C:\> Set-DhcpServerv6StatelessStore -ComputerName "dhcpserver.contoso.com" -Prefix 2001:4898:7020:1020:: -Enabled $True -PurgeInterval 2.00:00:00
```

这个示例为地址范围 2001:4898:7020:1020:: 启用了 DHCPv6 无状态存储功能，并将无状态客户端条目的清除间隔设置为 2 天。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行需要较长时间才能完成的命令。cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job` cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定目标计算机的DNS名称，或者是其IPv4或IPv6地址。该计算机运行着动态主机配置协议（DHCP）服务器服务。

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
在运行该cmdlet之前，会提示您进行确认。

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

### -Enabled
用于指定无状态存储的启用状态。该参数的可接受值为：True 或 False。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -Prefix
指定用于设置无状态存储属性的范围的 IPv6 子网前缀。

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

### -PurgeInterval
指定无状态存储的清除间隔。如果在这段时间内，DHCP客户端没有发送DHCPv6信息请求或选项请求，则认为该客户端已从该子网中消失，DHCP服务器服务会将对应的无状态存储条目清除。

你可以使用 `dd hh` 格式来配置这个值。如果你使用 `dd hh:mm:ss` 格式指定分钟或秒数，那么这些分钟和秒数将会被忽略。

```yaml
Type: TimeSpan
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6StatelessStore
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6StatelessStore
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DhcpServerv6StatelessStore](./Get-DhcpServerv6StatelessStore.md)

