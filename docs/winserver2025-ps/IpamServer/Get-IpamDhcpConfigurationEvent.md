---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamDhcpConfigurationEvent.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamdhcpconfigurationevent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamDhcpConfigurationEvent
---

# Get-IpamDhcpConfigurationEvent

## 摘要
从 IPAM 数据库中获取 DHCP 服务器的配置事件信息。

## 语法

```
Get-IpamDhcpConfigurationEvent [-ServerName <String[]>] [-StartDate <DateTime>] [-EndDate <DateTime>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-IpamDhcpConfigurationEvent` cmdlet 从 IP 地址管理（IPAM）数据库中获取动态主机配置协议（DHCP）服务器的配置事件。您可以指定 DHCP 服务器的全限定域名（FQDN）、开始日期和结束日期。如果未指定 DHCP 服务器，该 cmdlet 将获取所有服务器的配置事件。

使用 **Remove-IpamDhcpConfigurationEvent** cmdlet 从数据库中删除相关事件。

如果您没有指定开始日期，该cmdlet会使用数据库中第一个IPAM配置事件的日期；如果您没有指定结束日期，该cmdlet会使用最后一个IPAM配置事件的日期。所有日期均使用IPAM服务器的时间区设置。

如果某个命令的搜索结果超过10,000条，该cmdlet仅返回前10,000条结果，并会提示用户这些结果只是部分数据。

## 示例

### 示例 1：获取指定日期范围内所有服务器的事件
```
PS C:\> $Today = Get-Date
PS C:\> $StartDate= $Today.AddDays(-7)
PS C:\> Get-IpamDhcpConfigurationEvent -EndDate $Today -StartDate $StartDate | Export-Csv "C:\IpamEvents.csv"
```

这个示例会获取所有DHCP服务器的配置事件，然后将它们保存为.csv文件。

第一个命令使用 `Get-Date` cmdlet 创建一个 `DateTime` 对象，然后将其存储在 `$Today` 变量中。默认情况下，`Get-Date` 会返回当前日期。有关 `Get-Date` 和 `DateTime` 对象的更多信息，请输入 `Get-Help Get-Date`。

第二个命令将一个新的 `DateTime` 对象存储在 `$StartTime` 变量中。该日期比存储在 `$Today` 变量中的日期早七天。

第三个命令用于获取所有DHCP服务器在开始日期（存储在$StartTime变量中）和结束日期（存储在$Today变量中）之间的配置事件。该命令通过管道运算符将这些事件传递给**Export-Csv** cmdlet，该cmdlet会将结果保存为.csv文件。有关此cmdlet的更多信息，请输入`Get-Help Export-Csv`。

### 示例 2：获取指定服务器在某个日期范围内的事件信息
```
PS C:\> $Today = Get-Date
PS C:\> $StartDate= $Today.AddDays(-7)
PS C:\> Get-IpamConfigurationEvent -EndDate $Today -ServerName "dhcp01.contoso.com","dhcp02.contoso.com" -StartDate $StartDate | Export-Csv "C:\IpamFilteredEvents.csv"
```

这个示例获取了两台DHCP服务器的配置事件，并将这些事件保存为一个.csv文件。

第一个命令使用 `Get-Date` cmdlet 创建一个 `DateTime` 对象，然后将其存储在 `$Today` 变量中。

第二个命令将一个新的 `DateTime` 对象存储在 `$StartTime` 变量中。该日期比存储在 `$Today` 变量中的日期早七天。

第三个命令用于获取从开始日期（存储在 `$StartDate` 变量中）到结束日期（存储在 `$Today` 变量中）之间的配置事件。该命令指定了两台 DHCP 服务器的 FQDN（Fully Qualified Domain Name，全限定域名）。通过管道运算符，这个命令将事件传递给 **Export-Csv** cmdlet，后者会将结果保存为 .csv 文件。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值为本地计算机上的当前会话。

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

### -EndDate
该参数用于指定结束日期，日期以 **DateTime** 对象的形式提供。此 cmdlet 会从 IPAM 数据库中检索在该日期之后发生的事件。若要获取一个 **DateTime** 对象，请使用 **Get-Date** cmdlet 并按照 **DD/MM/YYYY** 格式输入日期。有关更多信息，请输入 `Get-Help Get-Date`。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ServerName
指定一个包含DHCP服务器FQDN（Fully Qualified Domain Name）的数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -StartDate
使用 **DateTime** 对象指定开始日期。该cmdlet会获取从这个日期开始的事件。要获取一个 **DateTime** 对象，可以使用 **Get-Date** cmdlet，并以 **DD/MM/YYYY** 格式指定日期。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamDhcpConfigurationEvent
此cmdlet返回一个对象，该对象表示IPAM中的DHCP服务器配置事件。

## 备注

## 相关链接

[Remove-IpamDhcpConfigurationEvent](./Remove-IpamDhcpConfigurationEvent.md)

