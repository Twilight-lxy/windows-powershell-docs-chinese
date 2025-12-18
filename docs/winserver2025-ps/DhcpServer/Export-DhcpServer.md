---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DhcpServerMigration-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/export-dhcpserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-DhcpServer
---

# Export-DhcpServer

## 摘要
导出DHCP服务器的服务配置和租约数据。

## 语法

```
Export-DhcpServer [-File] <String> [-ScopeId <IPAddress[]>] [-Prefix <IPAddress[]>] [-Leases] [-Force]
 [-ComputerName <String>] [-CimSession <CimSession>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Export-DhcpServer` cmdlet 可将动态主机配置协议（DHCP）服务器的服务配置信息（以及可选的租约数据）导出到指定的文件中。

如果您指定了*ScopeId*或*Prefix*参数，那么只会导出指定的范围或前缀以及所有服务器级别的设置。

如果您既没有指定 *ScopeId*，也没有指定 *Prefix*，那么将导出 DHCP 服务器服务配置，其中包括所有的作用域（v4 和 v6）以及可选的租约数据。

如果您指定了*Leases*参数，除了配置数据之外，租赁数据也会被导出。

## 示例

#### 示例 1：导出所有 DHCP 配置信息
```
PS C:\> Export-DhcpServer -ComputerName "dhcpserver.contoso.com" -File "C:\exportdir\dhcpexport.xml"
```

这个示例会将DHCP服务器（包括DHCPv4和DHCPv6）的所有配置信息（以及相关的作用域设置）以XML文件格式导出到指定的输出文件中。

#### 示例 2：导出指定的作用域
```
PS C:\> Export-DhcpServer -ComputerName "dhcpserver.contoso.com" -File "C:\exportdir\dhcpexport.xml" -ScopeId 10.10.10.0,10.20.20.0
```

这个示例将DHCP服务器服务中存在的范围10.10.10.0和10.20.20.0以XML文件格式导出到指定的输出文件中。同时，DHCPv4服务器的配置信息也会被导出到该指定文件中。

### 示例 3：导出指定的作用域及其租赁信息
```
PS C:\> Export-DhcpServer -ComputerName "dhcpserver.contoso.com" -File "C:\exportdir\dhcpexport.xml" -ScopeId 10.10.10.0,10.20.20.0 -Leases
```

这个示例会将DHCP服务器服务中存在的范围10.10.10.0和10.20.20.0以XML文件格式导出到指定的输出文件中。这些范围内包含的所有租约信息也会被一起导出。同时，DHCPv4服务器的配置信息也会被导出到该文件中。

### 示例 4：导出指定的作用域和 DHCPv6 服务器级配置信息
```
PS C:\> Export-DhcpServer -ComputerName "dhcpserver.contoso.com" -File "C:\exportdir\dhcpexport.xml" -Prefix 2001:4898:7020:1020::,2001:4898:7020:1030::
```

这个示例会将DHCP服务器服务中存在的指定范围（2001:4898:7020:1020:: 和 2001:4898:7020:1030::）以XML文件格式导出到指定的输出文件中。同时，DHCPv6服务器的配置信息也会被导出到该文件中。

### 示例 5：导出指定的作用域、它们的租约以及 DHCPv6 服务器级配置
```
PS C:\> Export-DhcpServer -ComputerName "dhcpserver.contoso.com" -File "C:\exportdir\dhcpexport.xml" -Prefix 2001:4898:7020:1020::,2001:4898:7020:1030:: -Leases
```

这个示例将DHCP服务器服务中存在的指定作用域（2001:4898:7020:1020:: 和 2001:4898:7020:1030::）以XML文件格式导出到指定的输出文件中。这些导出的内容包括这些作用域中的所有租约信息。同时，DHCP服务器的配置参数也会被一并导出到该文件中。

### 示例 6：导出文件中指定的作用域
```
PS C:\> Import-Csv -Path "ScopeList.txt" | Export-DhcpServer -ComputerName "dhcpserver.contoso.com" -File "C:\exportdir\dhcpexport.xml" -Leases
```

这个示例会将 `ScopeList.txt` 文件中指定的作用域列表以 XML 文件格式导出到指定的目标文件中。`Import-Csv` cmdlet 会返回包含这些作用域 ID 的对象，并将这些对象传递给当前的 cmdlet，从而实现所需的作用域导出功能。

名为ScopeList.txt的文件应包含以下格式：

ScopeId

10.10.10.0

20.20.20.0

30.30.30.0

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定运行DHCP服务器服务的目标计算机的DNS名称，或IPv4地址，或IPv6地址。

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
在运行 cmdlet 之前会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -File
指定数据将被导出的文件的名称。如果未指定完整的文件路径，则文件将在当前工作目录中创建。如果已经存在同名文件，将会返回错误信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
指定如果已经存在一个具有指定名称的文件，则该文件将被覆盖。

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

### -Leases
指定也要导出 IP 地址租约信息。

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
指定一个或多个要导出的IPv6范围内的子网前缀。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScopeId
指定以 IPv4 地址格式表示的、将被导出的范围标识符。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

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
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv6Scope
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 输出

### 无

## 备注

## 相关链接

[备份 DHCP 服务器](./Backup-DhcpServer.md)

[Import-DhcpServer](./Import-DhcpServer.md)

[Restore-DhcpServer](./Restore-DhcpServer.md)

