---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4Class_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv4class?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv4Class
---

# Get-DhcpServerv4Class

## 摘要
从DHCP服务器服务中检索IPv4供应商或用户类别信息。

## 语法

```
Get-DhcpServerv4Class [[-Name] <String[]>] [[-Type] <String>] [-ComputerName <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DhcpServerv4Class` cmdlet 用于从动态主机配置协议（DHCP）服务器服务中检索 IPv4供应商类或用户类信息。

如果您只指定了*类型*参数，那么系统将会检索该类型的所有类别。

如果您既没有指定*名称*参数，也没有指定*类型*参数，那么系统将会检索所有用户类和供应商类。

## 示例

#### 示例 1：获取所有类的定义
```
PS C:\> Get-DhcpServerv4Class -ComputerName "dhcpserver.contoso.com"
```

这个示例获取了所有DHCPv4类的定义信息，包括供应商（vendor）和用户（user）的定义。这些信息存在于运行在名为dhcpserver.contoso.com的计算机上的DHCP服务器服务中。

### 示例 2：获取供应商类定义
```
PS C:\> Get-DhcpServerv4Class -ComputerName "dhcpserver.contoso.com" -Type Vendor
```

这个示例获取了运行在名为dhcpserver.contoso.com的计算机上的DHCP服务器服务中存在的所有DHCPv4供应商类别定义。

### 示例 3：获取特定的供应商类定义
```
PS C:\> Get-DhcpServerv4Class -ComputerName "dhcpserver.contoso.com" -Name "MSUCClient"
```

这个示例从名为dhcpserver.contoso.com的计算机上运行的DHCP服务器服务中，获取指定供应商类（名为MSUCClient）的DHCPv4供应商类定义。

## 参数

### -AsJob
以后台作业的形式运行该 cmdlet。使用此参数来执行需要较长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
指定运行DHCP服务器服务的目标计算机的DNS名称，或IPv4地址或IPv6地址。

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
指定要检索的供应商名称或用户类别名称。

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
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值（即并发操作的最大数量）。此限制仅适用于当前执行的cmdlet，而不影响整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Class
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows Management Instrumentation (WMI) 对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstanceroot/Microsoft/Windows/DHCP/DhcpServerv4Class[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows Management Instrumentation (WMI) 对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerv4Class](./Add-DhcpServerv4Class.md)

[Remove-DhcpServerv4Class](./Remove-DhcpServerv4Class.md)

[Set-DhcpServerv4Class](./Set-DhcpServerv4Class.md)

