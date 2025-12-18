---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/get-rmssystemhealthreport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-RmsSystemHealthReport
---

# 获取RMS系统健康报告

## 摘要
生成Active Directory Rights Management Services（AD RMS）集群的系统健康报告。

## 语法

```
Get-RmsSystemHealthReport [-StartTime <DateTime>] [-EndTime <DateTime>] [-ServerName <String>]
 [-RequestType <String>] [-DomainName <String>] [-UserName <String>] -ReportType <ReportType>
 [-Path] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Get-RmsSystemHealthReport` cmdlet 生成一份报告，其中包含有关 Active Directory 权限管理服务（AD RMS）集群整体运行状况的信息。

要获取该报告，请设置所需报告类型的参数，然后将 *Path* 参数设置为 AD RMS 提供程序的驱动器路径 `<PSDrive>:\`Report`，其中 `<PSDrive>` 是提供程序的驱动器 ID。您也可以指定相对路径。例如，点（.）表示当前位置。

除非指定了*RequestType*、*ServerName*、*DomainName*或*UserName*，否则此cmdlet会为指定的ReportType生成一份总结报告。

## 示例

#### 示例 1：获取请求的报告
```
PS C:\> Get-RmsSystemHealthReport -Path "." -ReportType Request
```

此命令会显示由 AD RMS 集群处理的请求的摘要报告。

#### 示例 2：获取用户活动报告
```
PS C:\> Get-RmsSystemHealthReport -Path "." -StartTime 12/1/2008 -EndTime 12/31/2008 -ReportType User
```

该命令会显示2008年整个日历年度内用户活动的汇总报告。

### 示例 3：获取某个域中用户的报告
```
PS C:\> Get-RmsSystemHealthReport -Path "." -ReportType User -DomainName "Research"
```

该命令会显示“Research”领域中所有用户发出的请求的汇总报告。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您确认是否要执行该操作。

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

### -DomainName
指定用户电子邮件的域名。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -EndTime
用于指定系统健康报告的时间段的结束时间。此参数用于设置一个时间值。有关如何设置时间的详细信息，请参阅*StartTime*参数的描述。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Path
指定提供者驱动器及其路径，或者是当前驱动器上的相对路径。此参数是必需的。使用点（.）来表示当前位置。该参数不支持通配符，也没有默认值。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportType
指定报告的类型。此参数的可接受值包括：

- Server
- Request
- Domain
- User

```yaml
Type: ReportType
Parameter Sets: (All)
Aliases:
Accepted values: Server, Request, Domain, User

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -RequestType
Specifies the type of user request, such as Acquire License, Pre-Certify, and Get Client Licensor Certificate.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -ServerName
Specifies the name of the server for which you are requesting the health report.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -StartTime
Specifies the beginning of a time period.
This parameter specifies a time value.

The following examples show commonly-used syntax to specify a time.
Time is assumed to be local time unless otherwise specified.
When a time value is not specified, the time is assumed to 12:00:00 AM local time.
When a date is not specified, the date is assumed to be the current date.

`4/17/2006`

`Monday, April 17, 2006`

`2:22:45 PM`

`Monday, April 17, 2006 2:22:45 PM`

These examples specify the same date and the time without the seconds.

`4/17/2006 2:22 PM`

`Monday, April 17, 2006 2:22 PM`

`2:22 PM`

The following example shows how to specify a date and time by using the RFC1123 standard.
This example defines time by using Greenwich Mean Time (GMT).

`Mon, 17 Apr 2006 21:22:48 GMT`

The following example shows how to specify a round-trip value as Coordinated Universal Time (UTC).
This example represents Monday, April 17, 2006 at 2:22:48 PM UTC.

`2000-04-17T14:22:48.0000000`

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -UserName
Specifies the user name for which you are requesting a system health report.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[Get-RmsUserRequestReport](./Get-RmsUserRequestReport.md)

