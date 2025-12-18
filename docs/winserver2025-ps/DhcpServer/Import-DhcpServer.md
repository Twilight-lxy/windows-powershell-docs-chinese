---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DhcpServerMigration-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/import-dhcpserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-DhcpServer
---

# 导入 DHCP 服务器相关模块

## 摘要
从文件中导入动态主机配置协议（DHCP）服务器的服务配置信息，以及可选的租约数据。

## 语法

```
Import-DhcpServer [-File] <String> [-BackupPath] <String> [-ScopeId <IPAddress[]>] [-Prefix <IPAddress[]>]
 [-ScopeOverwrite] [-Leases] [-ServerConfigOnly] [-Force] [-ComputerName <String>] [-CimSession <CimSession>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Import-DhcpServer` cmdlet 用于从指定的文件中导入动态主机配置协议（DHCP）服务器的服务配置信息，以及可选的租约数据。

如果您指定了*ScopeId*或*Prefix*参数中的任意一个或多个，那么只有被指定的范围或前缀会被导入。

如果您既没有指定 *ScopeId* 参数，也没有指定 *Prefix* 参数，那么文件中包含的所有配置信息以及可选的租赁数据都会被导入。

如果您指定了*Leases*参数，除了配置数据之外，指定文件中的租赁数据也会被导入。

如果您指定了 *ScopeOverWrite* 参数，并且要导入的范围在目标服务器上也存在，那么目标 DHCP 服务器服务上的相应范围将会被覆盖。如果未指定该参数，而要导入的范围在目标 DHCP 服务器服务上确实存在，则会显示一条警告消息，之后系统会继续处理下一个要导入的范围。

如果您指定了 *ServerConfigOnly* 参数，则只有服务器级别的配置会被导入到目标 DHCP 服务器服务中。如果指定的文件包含任何作用域（scope）信息，这些信息将不会被导入到目标 DHCP 服务器服务中。

## 示例

### 示例 1：导入配置数据
```powershell
PS C:\> Import-DhcpServer -ComputerName "dhcpserver.contoso.com" -File "C:\exports\dhcpexport.xml" -BackupPath "C:\dhcpbackup\"
```

这个示例将指定文件中的配置数据导入到运行在名为dhcpserver.contoso.com的计算机上的DHCP服务器服务中。该文件可以包含DHCPv4和DHCPv6的配置数据。

### 示例 2：导入配置信息和租赁数据
```powershell
PS C:\> Import-DhcpServer -ComputerName "dhcpserver.contoso.com" -File "C:\exports\dhcpexport.xml" -BackupPath "C:\dhcpbackup\" -Leases
```

这个示例将指定文件中的配置数据和租约数据导入到运行在名为dhcpserver.contoso.com的计算机上的DHCP服务器服务中。该文件可以包含DHCPv4和DHCPv6的配置数据。

### 示例 3：为指定的范围导入配置数据
```powershell
PS C:\> Import-DhcpServer -ComputerName "dhcpserver.contoso.com" -File "C:\exports\dhcpexport.xml" -BackupPath "C:\dhcpbackup\" -ScopeId 10.10.10.0,10.20.20.0
```

这个示例将从指定的文件中导入范围 10.10.10.0 和 10.20.20.0 的配置数据，并将其应用到运行在名为 dhcpserver.contoso.com 的计算机上的 DHCP 服务器服务上。如果导出文件中包含除了 10.10.10.0 和 10.20.20.0 之外的其他范围，那么这些范围将被忽略。如果在导出文件中存在 DHCPv4 服务器级别的配置数据，它们也会被导入到 DHCP 服务器服务中。

### 示例 4：导入指定范围内的配置信息和租赁数据
```powershell
PS C:\> Import-DhcpServer -ComputerName dhcpserver.contoso.com -File "C:\exports\dhcpexport.xml" -BackupPath "C:\dhcpbackup\" -ScopeId 10.10.10.0,10.20.20.0 -Leases
```

这个示例从指定的文件中导入范围 10.10.10.0 和 10.20.20.0 的配置数据及租约信息，并将这些数据应用到运行在名为 dhcpserver.contoso.com 的计算机上的 DHCP 服务器服务上。如果导出文件中包含除 10.10.10.0 和 10.20.20.0 之外的其他范围，那么这些范围将被忽略。如果导出文件中还包含了 DHCPv4 服务器级别的配置数据，这些数据也会被导入到 DHCP 服务器服务中。

### 示例 5：导入指定范围内的配置和租约数据，并进行覆盖
```powershell
PS C:\> Import-DhcpServer -ComputerName "dhcpserver.contoso.com" -File "C:\exports\dhcpexport.xml" -BackupPath "C:\dhcpbackup\" -ScopeId 10.10.10.0,10.20.20.0 -Leases -ScopeOverwrite
```

此示例从指定的文件中导入范围 10.10.10.0 和 10.20.20.0 的配置和租约数据，并将这些数据应用到运行在名为 dhcpserver.contoso.com 的计算机上的 DHCP 服务器服务上。如果导出文件中包含除 10.10.10.0 和 10.20.20.0 之外的其他范围，那么这些其他范围将被忽略。如果导出文件中存在 DHCPv4 服务器级别的配置数据，这些数据也会被导入到服务器上。如果在名为 dhcpserver.contoso.com 的计算机上的 DHCP 服务器服务中已经存在范围 10.10.10.0 和 10.20.20.0，那么这些范围将被删除，并根据导出文件中的数据重新创建。

### 示例 6：导入服务器级别的配置数据
```powershell
PS C:\> Import-DhcpServer -ComputerName "dhcpserver.contoso.com" -File "C:\exports\dhcpexport.xml" -BackupPath "C:\dhcpbackup\" -ServerConfigOnly
```

这个示例仅将指定文件中的服务器级配置数据导入到运行在名为dhcpserver.contoso.com的计算机上的DHCP服务器服务中。如果文件中包含任何作用域配置数据，这些数据将被忽略。

#### 示例 7：为指定的 DHCPv6 范围导入配置数据
```powershell
PS C:\> Import-DhcpServer -ComputerName "dhcpserver.contoso.com" -File "C:\exports\dhcpexport.xml" -BackupPath "C:\dhcpbackup\" -Prefix 2001:4898:7020:1020::,2001:4898:7020:1030::
```

这个示例从指定的文件中导入范围 2001:4898:7020:1020:: 和 2001:4898:7020:1030:: 的配置数据，并将这些数据应用到运行在名为 dhcpserver.contoso.com 的计算机上的 DHCP 服务器服务中。如果导出文件中包含除这两个范围之外的其他范围，那么这些其他范围将被忽略。如果导出文件中还包含了 DHCPv6 服务器级别的配置数据，这些数据也会被导入到 DHCP 服务器服务中。

### 示例 8：为指定的作用域导入 DHCPv6 的配置数据和租约数据
```powershell
PS C:\> Import-DhcpServer -ComputerName "dhcpserver.contoso.com" -File "C:\exports\dhcpexport.xml" -BackupPath "C:\dhcpbackup\" -Prefix 2001:4898:7020:1020::,2001:4898:7020:1030:: -Leases
```

这个示例从指定的文件中导入范围 2001:4898:7020:1020:: 和 2001:4898:7020:1030:: 的配置和租约数据，并将其加载到运行在名为 dhcpserver.contoso.com 的计算机上的 DHCP 服务器服务中。如果导出文件中包含除 2001:4898:7020:1020:: 和 2001:4898:7020:1030:: 之外的其他范围，那么这些范围将被忽略。如果在导出文件中存在 DHCPv6 服务器级别的配置数据，这些数据也会被导入到 DHCP 服务器服务中。

### 示例 9：为指定的范围导入 DHCPv6 的配置和租约数据，并允许覆盖现有数据
```powershell
PS C:\> Import-DhcpServer -ComputerName "dhcpserver.contoso.com" -File "C:\exports\dhcpexport.xml" -BackupPath "C:\dhcpbackup\" -Prefix 2001:4898:7020:1020::,2001:4898:7020:1030:: -Leases -ScopeOverwrite
```

此示例将从指定的文件中导入范围 2001:4898:7020:1020:: 和 2001:4898:7020:1030:: 的配置数据及租约信息，并将这些数据应用到运行在名为 dhcpserver.contoso.com 的计算机上的 DHCP 服务器服务中。如果导出文件中包含除这两个范围之外的其他范围，那么这些其他范围将被忽略。如果导出文件中还包含了 DHCPv6 服务器级别的配置数据，这些数据也会被导入到 DHCP 服务器服务中。如果在名为 dhcpserver.contoso.com 的计算机上运行的 DHCP 服务器服务中已经存在范围 2001:4898:7020:1020:: 和 2001:4898:7020:1030::，那么这些现有范围将会被删除，并根据导出文件中的数据重新创建。

### 示例 10：从文件中导入指定的作用域
```powershell
PS C:\> $ScopeIdList = Import-Csv -Path ".\ScopeList.txt"

PS C:\> Import-DhcpServer -ComputerName "dhcpserver.contoso.com" -File "C:\exportdir\dhcpexport.xml" -Leases -ScopeId $ScopeIdList.ScopeId -BackupPath "C:\dhcpbackup\"
```

此示例将名为 `_ScopeList.txt` 的文件中指定的作用域列表导入到运行在计算机 `dhcpserver.contoso.com` 上的 DHCP 服务器服务中。

`Import-Csv` cmdlet 用于获取需要导入的 scope 列表，并将该列表存储在名为 `$ScopeIdList_` 的变量中。第二行代码使用 `$ScopeIdList_` 变量作为 `_ScopeId_` 参数的输入值来导入这些 scope。

名为 `_ScopeList.txt_` 的文件应包含以下格式：

ScopeID：10.10.10.0、10.20.20.0、10.30.30.0

## 参数

### -BackupPath
在导入操作过程中进行任何配置更改之前，该命令用于指定备份DHCP服务器数据库的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
指定运行DHCP服务器服务的目标计算机的DNS名称，或其IPv4或IPv6地址。

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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -File
指定用于导入数据的文件的名称。如果未指定完整的文件路径，则该文件将从当前工作目录中读取。

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
强制命令运行，而不会请求用户确认。

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
指定也要导入租赁数据。

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
指定被导入的 IPv6 范围内的子网前缀。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScopeId
指定必须导入的范围标识符（ID），这些标识符采用IPv4地址格式。

```yaml
Type: IPAddress[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ScopeOverwrite
指定：如果导入的范围在目标服务器上已经存在，则目标 DHCP 服务器服务上的该范围将被覆盖。

如果未指定此参数，并且要导入的范围在目标DHCP服务器服务上已经存在，系统会显示一条警告消息，然后继续处理下一个要导入的范围。

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

### -ServerConfigOnly
指定仅将服务器级别的配置导入到目标DHCP服务器服务中。如果指定的文件包含任何范围（scope）信息，这些信息不会被导入到目标DHCP服务器服务中。

DHCPv4和DHCPv6服务器级别的配置都已被导入。

服务器级配置包括（v4和v6版本均适用）：

- Class definitions.
- Option definitions.
- Option values.
- Server level Policies (DHCPv4).
- MAC address filters (DHCPv4).
- Other Server Properties (ConflictDetectionAttempts, DHCPv6 stateless store).

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

### 无

## 输出

### 无

## 备注

## 相关链接

[Import-Csv](https://go.microsoft.com/fwlink/p/?LinkId=113341)

[备份-DhcpServer](./Backup-DhcpServer.md)

[Export-DhcpServer](./Export-DhcpServer.md)

[恢复 DHCP 服务器](./Restore-DhcpServer.md)
