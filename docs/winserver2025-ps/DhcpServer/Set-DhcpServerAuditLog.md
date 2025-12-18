---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerAuditLog_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/set-dhcpserverauditlog?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DhcpServerAuditLog
---

# Set-DhcpServerAuditLog

## 摘要
设置计算机上运行的 DHCP 服务器服务上的 DHCP 服务器服务审计日志配置。

## 语法

```
Set-DhcpServerAuditLog [[-Enable] <Boolean>] [[-Path] <String>] [-MaxMBFileSize <UInt32>]
 [-DiskCheckInterval <UInt32>] [-MinMBDiskSpace <UInt32>] [-ComputerName <String>] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DhcpServerAuditLog` cmdlet 用于配置运行在该计算机上的 DHCP（动态主机配置协议）服务器服务的审计日志设置。此外，该 cmdlet 还会决定是否启用 DHCP 服务器服务的审计日志功能。

## 示例

### 示例 1：为 DHCP 服务器服务启用日志记录功能
```
PS C:\> Set-DhcpServerAuditLog -ComputerName "dhcpserver.contoso.com" -Enable $True -Path "D:\dhcpauditlog\" -MaxMBFileSize 100
```

这个示例启用了DHCP服务器服务的审计日志功能，并将审计日志的存储路径设置为D:\dhcpauditlog\目录。此外，该cmdlet还将审计日志文件的最大大小设置为100 MB。

## 参数

### -AsJob
以后台作业的形式运行该 cmdlet。使用此参数来执行需要很长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列的 cmdlets。要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
在运行cmdlet之前，会提示您进行确认。

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

### -DiskCheckInterval
指定在发生多少个审计日志事件后，DHCP服务器服务会根据 *MinMBDiskSpace* 参数中指定的要求来检查可用磁盘空间。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Enable
指定 DHCP 服务器服务审计日志的启用状态。该参数的有效值为：True（启用）或 False（禁用）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MaxMBFileSize
指定所有 DHCP 服务审计日志文件可使用的最大磁盘空间大小（以兆字节 MB 为单位）。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MinMBDiskSpace
指定用于存储审计日志的最低所需磁盘空间（以兆字节（MB）为单位）。在记录审计日志消息之前，DHCP服务器服务会检查磁盘上是否具有该参数所指定的最小磁盘空间。如果最小磁盘空间不可用，DHCP服务器服务将停止审计日志记录，直到所需的最低磁盘空间可用为止。如果您指定值为0或不指定此参数，则默认的最低磁盘空间为20 MB。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
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

### -Path
指定DHCP服务器服务创建审计日志文件的目录路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果运行该 cmdlet 会发生什么情况。不过实际上并没有运行这个 cmdlet。

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

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerAuditLog
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerAuditLog
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DhcpServerAuditLog](./Get-DhcpServerAuditLog.md)

