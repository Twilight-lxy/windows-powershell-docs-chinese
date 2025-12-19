---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamConfigurationEvent.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/remove-ipamconfigurationevent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IpamConfigurationEvent
---

# 删除 Ipam 配置事件

## 摘要
删除 IPAM 服务器配置事件。

## 语法

```
Remove-IpamConfigurationEvent -EndDate <DateTime> [-PassThru] [-Force] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-IpamConfigurationEvent` cmdlet 会永久性地从 IPAM 数据库中删除与 IP 地址管理（IPAM）服务器相关的配置事件。该 cmdlet 会清除所有在指定结束日期之前由 IPAM 收集到的配置事件。

请不要将当前日期指定为结束日期。IPAM服务器会在下一次数据收集任务中从动态主机配置协议（DHCP）服务器那里收集配置事件，因此，指定当前日期并不会导致当天发生的事件被永久删除。

## 示例

### 示例 1：移除所有配置事件
```
PS C:\> $Today = Get-Date
PS C:\> Remove-IpamConfigurationEvent -EndDate $Today
Confirm

All Event catalogue data upto and including the date selected by you will be deleted permanently. Do you want to

continue?

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):Y
```

第一个命令通过 `Get-Date` cmdlet 获取今天的日期，并将结果存储在名为 `$Today` 的变量中。第二个命令则删除所有与日期相关的配置事件数据（这些数据存储在 `$Today` 变量中）。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的任务。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（about_Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -EndDate
指定结束日期，该日期以 **DateTime** 对象的形式提供。此 cmdlet 会从 IPAM 数据库中删除在该日期之后的所有配置事件。若需获取一个 **DateTime** 对象，可以使用 **Get-Date** cmdlet。有关更多信息，请输入 `Get-Help Get-Date`。

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
强制命令在不需要用户确认的情况下运行。

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
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

### IpamConfigurationEvent
此 cmdlet 返回一个对象，该对象表示 IPAM 服务器配置事件。

## 备注

## 相关链接

[Get-IpamConfigurationEvent](./Get-IpamConfigurationEvent.md)

