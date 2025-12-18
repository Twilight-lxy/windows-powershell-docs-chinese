---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServer_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/restore-dhcpserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Restore-DhcpServer
---

#Restore-DhcpServer

## 摘要
从指定的位置恢复DHCP服务器服务的数据库。

## 语法

```
Restore-DhcpServer [-ComputerName <String>] [-Path] <String> [-Force] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Restore-DhcpServer` cmdlet 会从指定的位置恢复动态主机配置协议（DHCP）服务器服务的数据库。

## 示例

### 示例 1：恢复 DHCP 服务器服务数据库
```
PS C:\> Restore-DhcpServer -ComputerName "dhcpserver.contoso.com" -Path "C:\Windows\system32\dhcp\backup"
```

这个示例从指定的位置恢复DHCP服务器服务数据库。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

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

### -Confirm
在运行该cmdlet之前，会提示您确认是否要继续执行。

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

### -Force
强制命令运行，而无需请求用户确认。

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
指定备份数据库存储位置的路径。

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

### -ThrottleLimit
指定可以同时运行的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机。

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
展示了如果该cmdlet被运行时会发生什么情况。不过实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[备份-DhcpServer](./Backup-DhcpServer.md)

[Export-DhcpServer](./Export-DhcpServer.md)

[Import-DhcpServer](./Import-DhcpServer.md)

