---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerv4Filter_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/add-dhcpserverv4filter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DhcpServerv4Filter
---

# Add-DhcpServerv4Filter

## 摘要
向DHCP服务器服务添加一个MAC地址过滤器。

## 语法

```
Add-DhcpServerv4Filter [-ComputerName <String>] [-Description <String>] [-MacAddress] <String[]>
 [-List] <String> [-Force] [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DhcpServerv4Filter` cmdlet 用于将指定的 MAC 地址过滤器添加到动态主机配置协议（DHCP）服务器服务中。该 MAC 地址可以被添加到允许列表或拒绝列表中。

## 示例

### 示例 1：将某个客户端添加到允许访问的列表中
```
PS C:\> Add-DhcpServerv4Filter -List Allow -MacAddress "F0-DE-F1-7A-00-5E" -Description "Laptop 09"
```

这个示例将通过MAC地址识别的指定客户端添加到允许使用的MAC地址过滤器列表中。

### 示例 2：将多个客户端添加到允许访问的列表中
```
PS C:\> Add-DhcpServerv4Filter -List Allow -MacAddress "F0-DE-F1-7A-00-5E", "F0-DE-F1-7A-00-5C"
```

这个示例将那些通过其MAC地址被识别的客户端添加到允许的MAC地址过滤器的列表中。

### 示例 3：从文件中添加地址过滤器
```
PS C:\> Import-Csv -Path "MacAddressFilters.csv" | Add-DhcpServerv4Filter -ComputerName "dhcpserver.contoso.com" -List Allow
```

这个示例将名为 `MacAddressFilters.csv` 的文件中的所有 MAC 地址过滤器添加到运行在 `dhcpserver.contoso.com` 这台计算机上的 DHCP 服务器服务的允许 MAC 地址列表中。`Import-Csv` cmdlet 会返回包含 MAC 地址过滤字段的对象，这些对象随后会被添加到服务器上。`MacAddressFilters.csv` 文件应采用以下逗号分隔值（CSV）格式：

`MacAddress,Description`

`1a-1b-1c-1d-1e-1f,Computer1`

`2a-2b-2c-2d-2e-2f,Computer2`

`3a-3b-3c-3d-3e-3f,Computer3`

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job` cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -Confirm
在运行该cmdlet之前，会提示您确认是否要继续执行该操作。

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

### -Description
指定要添加的MAC地址过滤器的描述字符串。

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

### -Force
该规则规定：如果一个或多个MAC地址已经存在于“允许”或“拒绝”列表中，则会删除这些匹配的MAC地址，并创建新的条目。

当指定的MAC地址已经存在于某个列表中（例如允许列表）时，这个参数非常有用。此时需要将该MAC地址添加到另一个列表中（例如拒绝列表）。

如果未指定此参数，当指定的MAC地址已经存在于某个列表中时，该cmdlet将会失败。

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

### -List
指定要将一个或多个MAC地址添加到的列表。该参数的有效取值为：Allow（允许）或Deny（拒绝）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: Allow, Deny

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MacAddress
指定一个或多个要添加到MAC地址过滤列表中的MAC地址。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: ClientId

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或整个计算机。

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
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Filter
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4Filter[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DhcpServerv4Filter](./Get-DhcpServerv4Filter.md)

[Get-DhcpServerv4FilterList](./Get-DhcpServerv4FilterList.md)

[Get-DhcpServerv4Lease](./Get-DhcpServerv4Lease.md)

[Remove-DhcpServerv4Filter](./Remove-DhcpServerv4Filter.md)

[Set-DhcpServerv4FilterList](./Set-DhcpServerv4FilterList.md)

