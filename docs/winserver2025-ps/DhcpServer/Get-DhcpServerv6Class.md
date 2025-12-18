---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv6Class_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv6class?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv6Class
---

# Get-DhcpServerv6Class

## 摘要
从DHCP服务器服务中获取IPv6供应商或用户类别信息。

## 语法

```
Get-DhcpServerv6Class [[-Name] <String[]>] [[-Type] <String>] [-ComputerName <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DhcpServerv6Class` cmdlet 用于从动态主机配置协议（DHCP）服务器服务中获取 IPv6 的供应商类别或用户类别信息。

如果您仅指定*类型*参数，那么DHCP服务器服务上所有属于该类型的类都会被检索出来。

如果您既没有指定*名称*参数，也没有指定*类型*参数，那么DHCP服务器服务上的所有用户类和供应商类都会被检索出来。

如果您只指定了*名称*参数，那么将返回与该*名称*参数值对应的类。

## 示例

### 示例 1：获取所有 DHCPv6 类的定义
```
PS C:\> Get-DhcpServerv6Class -ComputerName "dhcpserver.contoso.com"
```

这个示例获取了DHCP服务器服务上所有的DHCPv6类别定义，包括供应商提供的定义和用户自定义的定义。

### 示例 2：获取所有 DHCPv6 厂商类别（vendor class）的定义
```
PS C:\> Get-DhcpServerv6Class -ComputerName "dhcpserver.contoso.com" -Type "Vendor"
```

这个示例获取了DHCP服务器服务上所有的DHCPv6供应商类别定义。

### 示例 3：获取特定的 DHCPv6 公司（vendor）类别定义
```
PS C:\> Get-DhcpServerv6Class -ComputerName "dhcpserver.contoso.com" -Name "MSUCClient"
```

这个示例获取了名为 MSUCClient 的供应商类的 DHCPv6 供应商类定义。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用 `*-Job` 系列 cmdlet。要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
指定要检索的供应商名称或用户类别的名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值为`0`，那么Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最优限制值。此限制仅适用于当前执行的cmdlet，而不适用于整个会话或计算机本身。

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

### -Type
指定类的类型。该参数的可接受值为：Vendor（供应商）和User（用户）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Vendor, User

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Class
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径指定了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Class[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径指定了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv6Class](./Add-DhcpServerv6Class.md)

[Remove-DhcpServerv6Class](./Remove-DhcpServerv6Class.md)

[Set-DhcpServerv6Class](./Set-DhcpServerv6Class.md)

