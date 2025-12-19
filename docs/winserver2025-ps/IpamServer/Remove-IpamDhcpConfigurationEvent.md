---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamDhcpConfigurationEvent.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/remove-ipamdhcpconfigurationevent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IpamDhcpConfigurationEvent
---

# 删除 IpamDhcpConfigurationEvent

## 摘要
从 IPAM 数据库中删除与 DHCP 服务器相关的配置事件。

## 语法

```
Remove-IpamDhcpConfigurationEvent -EndDate <DateTime> [-PassThru] [-Force] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-IpamDhcpConfigurationEvent` 这个cmdlet用于从IP地址管理（IPAM）数据库中删除与动态主机配置协议（DHCP）服务器相关的配置事件。该cmdlet会永久性地删除所有在指定结束日期之前的配置事件，且该结束日期采用的是IPAM服务器所在时区的时间。

使用 **Get-IpamDhcpConfigurationEvent** cmdlet 来查看来自 IPAM 数据库的配置事件。

请不要将当前日期指定为结束日期。IPAM服务器会在下一次数据收集任务中从DHCP服务器获取配置事件，因此指定当前日期并不会导致当天发生的事件被永久删除。

该cmdlet并不会从DHCP服务器本身删除配置事件记录。

## 示例

### 示例 1：删除发生在前一天之前的事件
```
PS C:\> $Today = Get-Date
PS C:\> Remove-IpamConfigurationEvent -EndDate $Today.AddDays(-1)
```

这个示例会删除前一天之前的所有配置事件。

第一个命令使用 `Get-Date` cmdlet 创建一个 `DateTime` 对象，然后将其存储在 `$Today` 变量中。默认情况下，`Get-Date` 会返回当前日期。有关 `Get-Date` 和 `DateTime` 对象的更多信息，请输入 `Get-Help Get-Date`。

第二个命令用于从 IPAM 数据库中删除截至前一天为止的所有配置事件。该命令会从存储在 `$Today` 变量中的 `DateTime` 对象中减去一天的时间，然后将这个时间值设置为 `endDate` 参数的值。

## 参数

### -AsJob
以后台作业的形式运行此cmdlet。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` 类型的 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

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

### -EndDate
指定结束日期为一个 **DateTime** 对象。该 cmdlet 会从 IPAM 数据库中删除在该日期之后的所有事件。若要获取一个 **DateTime** 对象，可以使用 **Get-Date** cmdlet。有关更多信息，请输入 `Get-Help Get-Date`。

请不要指定当前日期。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
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

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此 cmdlet 不会生成任何输出。

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
该参数用于指定可以同时执行的命令（cmdlet）操作的最大数量。如果省略此参数或输入值`0`，Windows PowerShell®将根据计算机上正在运行的CIM命令（cmdlets）的数量来计算该命令的最佳限制次数。此限制仅适用于当前正在执行的命令，而不适用于整个会话或计算机本身。

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
展示了如果运行该 cmdlet 会发生什么情况。但实际上，这个 cmdlet 并没有被执行。

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

## 输出

### IpamDhcpConfigurationEvent
此cmdlet返回一个对象，该对象代表IPAM中的DHCP服务器配置事件。

## 备注

## 相关链接

[Get-IpamDhcpConfigurationEvent](./Get-IpamDhcpConfigurationEvent.md)

