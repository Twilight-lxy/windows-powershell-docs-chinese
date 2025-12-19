---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamConfigurationEvent.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamconfigurationevent?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamConfigurationEvent
---

# Get-IpamConfigurationEvent

## 摘要
从 IPAM 数据库中获取 IPAM 配置事件。

## 语法

```
Get-IpamConfigurationEvent [-UserName <String[]>] [-UserDomainName <String[]>] [-UserForestName <String[]>]
 [-StartDate <DateTime>] [-EndDate <DateTime>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-IpamConfigurationEvent` cmdlet 用于从 IPAM 数据库中获取 IP 地址管理 (IPAM) 配置事件。如果您不指定任何参数，该 cmdlet 将获取 IPAM 服务器的所有配置事件。您可以指定 `StartDate` 和 `EndDate` 参数来获取在特定时间范围内发生的配置事件；也可以指定 `UserDomainName` 参数来过滤发生在某个用户域内的配置事件；此外还可以指定 `UserName` 参数来过滤由特定用户进行的配置更改。

请为 *startDate* 和 *endDate* 参数指定在 IPAM 服务器时区内的日期值。此 cmdlet 返回的数据包含开始日期和结束日期。如果您未指定 *StartDate* 参数，cmdlet 将使用 IPAM 数据库中第一个 IPAM 配置事件的起始日期；如果您未指定 *EndDate* 参数，cmdlet 将使用 IPAM 中最后一个有效的服务器配置事件的日期。

如果某个命令的输出结果超过 10,000 条，那么该cmdlet仅返回前 10,000 条结果，并会提示用户这些结果只是部分数据。

## 示例

#### 示例 1：获取指定时间范围内的 IPAM 服务器配置事件
```
PS C:\> $Today = Get-Date
PS C:\> $LastMonth = $Today.AddDays(-30)
PS C:\> Get-IpamConfigurationEvent -StartDate $LastMonth -EndDate $Today
```

这个示例获取了过去30天内IPAM服务器的所有配置事件。

第一个命令使用 `Get-Date` cmdlet 创建一个 `DateTime` 对象，然后将其存储在 `$Today` 变量中。默认情况下，`Get-Date` 会返回当前日期。有关 `Get-Date` 和 `DateTime` 对象的更多信息，请输入 `Get-Help Get-Date`。

第二个命令从存储在 $Today 变量中的 **DateTime** 对象中减去 30 天，然后将结果存储在 $LastMonth 变量中。

第三个命令会获取过去30天内IPAM服务器的所有配置事件信息。

### 示例 2：获取用户的 IPAM 配置事件
```
PS C:\> $Today = Get-Date
PS C:\> $LastMonth = $Today.AddDays(-30)
PS C:\> Get-IpamConfigurationEvent -StartDate $LastMonth -EndDate $Today -UserName "Administrator"
```

这个示例会获取该用户在过去30天内与IPAM服务器相关的所有配置事件。

第一个命令使用 `Get-Date` cmdlet 创建一个 `DateTime` 对象，然后将其存储在 `$Today` 变量中。默认情况下，`Get-Date` 会返回当前日期。

第二个命令从存储在 $Today 变量中的 **DateTime** 对象中减去 30 天，然后将结果存储在 $LastMonth 变量中。

第三个命令用于获取名为“Administrator”的用户在过去30天内与IPAM服务器相关的配置事件信息。

### 示例 3：获取属于该用户的域中的 IPAM 配置事件
```
PS C:\> $Today = Get-Date
PS C:\> $LastMonth = $Today.AddDays(-30)
PS C:\> Get-IpamConfigurationEvent -StartDate $LastMonth -EndDate $Today -UserName "Administrator" -UserDomainName "Contoso.com"
```

这个示例会获取指定域中用户在过去的30天内与该IPAM服务器相关的所有配置事件。

第一个命令使用 `Get-Date` cmdlet 创建一个 `DateTime` 对象，然后将其存储在 `$Today` 变量中。默认情况下，`Get-Date` 会返回当前日期。

第二个命令从存储在 $Today 变量中的 **DateTime** 对象中减去 30 天，然后将结果存储在 $LastMonth 变量中。

第三个命令会获取名为“Administrator”的用户在域名为“Contoso.com”下的IPAM服务器在过去30天内发生的所有配置事件。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定结束日期为一个 **DateTime** 对象。该 cmdlet 会从这个日期开始，从 IPAM 数据库中检索配置事件。要获取一个 **DateTime** 对象，可以使用 **Get-Date** cmdlet，并以 **DD/MM/YYYY** 格式指定日期。有关更多信息，请输入 `Get-Help Get-Date`。

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

### -StartDate
指定一个开始日期，该日期以 **DateTime** 对象的形式提供。此cmdlet会从IPAM数据库中获取从这个开始日期到结束日期之间的配置事件。要获取一个 **DateTime** 对象，请使用 **Get-Date** cmdlet，并以 **DD/MM/YYYY** 格式指定日期。有关更多信息，请输入 `Get-Help Get-Date`。

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
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前运行的 cmdlet，而不适用于整个会话或整个计算机。

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

### -UserDomainName
指定一个包含用户域名称的数组。该cmdlet会过滤发生在这些用户域中的配置事件。

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

### -UserForestName


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

### -UserName
指定一个包含用户名的数组。该cmdlet会获取这些用户生成的配置事件。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamConfigurationEvent
此cmdlet返回一个对象，该对象代表IPAM服务器的配置事件。

## 备注

## 相关链接

[Remove-IpamConfigurationEvent](./Remove-IpamConfigurationEvent.md)

