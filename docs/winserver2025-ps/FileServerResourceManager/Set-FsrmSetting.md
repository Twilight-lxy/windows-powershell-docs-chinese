---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmSetting.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/set-fsrmsetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-FsrmSetting
---

# Set-FsrmSetting

## 摘要
更改该计算机的全局FSRM（文件系统管理器）设置。

## 语法

```
Set-FsrmSetting [-InputObject <CimInstance[]>] [-SmtpServer <String>] [-FromEmailAddress <String>]
 [-AdminEmailAddress <String>] [-EmailNotificationLimit <Int32>] [-EventNotificationLimit <Int32>]
 [-CommandNotificationLimit <Int32>] [-ReportNotificationLimit <Int32>] [-ReportLimitMaxFile <Int32>]
 [-ReportLimitMaxFileGroup <Int32>] [-ReportLimitMaxOwner <Int32>] [-ReportLimitMaxFilesPerFileGroup <Int32>]
 [-ReportLimitMaxFilesPerOwner <Int32>] [-ReportLimitMaxFilesPerDuplicateGroup <Int32>]
 [-ReportLimitMaxDuplicateGroup <Int32>] [-ReportLimitMaxQuota <Int32>]
 [-ReportLimitMaxFileScreenEvent <Int32>] [-ReportLimitMaxPropertyValue <Int32>]
 [-ReportLimitMaxFilesPerPropertyValue <Int32>] [-ReportLocationIncident <String>]
 [-ReportLocationScheduled <String>] [-ReportLocationOnDemand <String>]
 [-ReportFileScreenAuditDaysSince <Int32>] [-ReportFileScreenAuditUser <String[]>]
 [-ReportFileGroupIncluded <String[]>] [-ReportFileOwnerUser <String[]>] [-ReportFileOwnerFilePattern <String>]
 [-ReportPropertyName <String>] [-ReportPropertyFilePattern <String>] [-ReportLargeFileMinimum <UInt64>]
 [-ReportLargeFilePattern <String>] [-ReportLeastAccessedMinimum <Int32>]
 [-ReportLeastAccessedFilePattern <String>] [-ReportMostAccessedMaximum <Int32>]
 [-ReportMostAccessedFilePattern <String>] [-ReportQuotaMinimumUsage <Int32>] [-ReportFileScreenAuditEnable]
 [-ReportClassificationFormat <FsrmReportClassificationFormatEnum[]>] [-ReportClassificationMailTo <String>]
 [-ReportClassificationLog <FsrmReportClassificationLogEnum[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-FsrmSetting` cmdlet 用于更改计算机的全局文件服务器资源管理器（FSRM）设置。

## 示例

### 示例 1：更改 FSRM 设置以管理员电子邮件地址为准
```
PS C:\> Set-FsrmSetting -AdminEmailAddress "john@contoso.com"
```

该命令指定了电子邮件收件人的地址为“john@contoso.com”，服务器会将这封邮件发送给管理员。

### 示例 2：更改 FSRM 设置以调整命令通知的限制
```
PS C:\> Set-FsrmSetting -CommandNotificationLimit 80
```

此命令将 80 分钟指定为同一类型的命令通知事件之间至少应间隔的时间（即两次事件运行之间的最短时间）。

### 示例 3：更改 FSRM 设置以调整报告分类格式
```
PS C:\> Set-FsrmSetting -ReportClassificationFormat @('Xml')
```

该命令指定了服务器生成的分类报告的格式为XML。

### 示例 4：更改 FSRM 设置以指定报告分类日志的类型
```
PS C:\> Set-FsrmSetting -ReportClassificationLog @('ErrorsInSystemLog')
```

该命令指定 `ErrorsInSystemLog` 为文件分类系统在分类过程中生成的日志类型。

### 示例 5：更改用于大文件报告和配额使用报告的 FSRM 设置
```
PS C:\> Set-FsrmSetting -ReportLargeFilePattern '*' -ReportLimitMaxQuota 100
```

该命令使用了通配符“*”，表示大型文件报告会包含所有符合`ReportLargeFileMinimum`参数所设置值的文件。同时，该命令还指定了在配额使用报告中最多可以包含100个配额项。

#### 示例 6：更改 SMTP 服务器的 FSRM 设置以及按所有者生成文件报告的功能
```
PS C:\> Set-FsrmSetting -SmtpServer "10.121.24.132" -ReportFileOwnerFilePattern "*.xml"
```

此命令将 10.121.24.132 指定为 FSRM 用于发送电子邮件的 SMTP 服务器的 IP 地址。该命令还指定了 “*.XML” 作为文件模式，用于匹配“按所有者显示的文件报告”相关文件。

## 参数

### -AdminEmailAddress
指定一个由分号分隔的电子邮件地址列表，这些地址是服务器发送给管理员的所有邮件的接收者。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -CommandNotificationLimit
指定命令类型通知中各个运行事件之间所需的最小时间间隔（以分钟为单位）。如果同时发生多个命令通知，服务器只有在自上次执行该操作以来至少经过了这个时间间隔后，才会再次触发相应的命令通知。

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

### -Confirm
在运行cmdlet之前会提示您确认是否要继续。

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

### -EmailNotificationLimit
该参数用于指定电子邮件类型通知中各运行事件之间的最小时间间隔（以分钟为单位）。如果同时有多个命令通知需要执行，服务器只有在距离上一次执行相应操作至少经过了指定的时间后，才会再次运行这些命令通知。

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

### -EventNotificationLimit
指定同一类型事件通知中连续两次运行事件之间的最小时间间隔（以分钟为单位）。如果多次命令通知同时发生，服务器只有在距离上次执行该操作至少过去了指定的时间后，才会再次执行相应的命令通知。

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

### -FromEmailAddress
指定FSRM发送电子邮件时使用的默认电子邮件地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给此 cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的该项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -ReportClassificationFormat
指定服务器生成的分类报告格式数组。该参数的可接受值为：

- DHTML
- HTML
- XML
- CSV
- Text

```yaml
Type: FsrmReportClassificationFormatEnum[]
Parameter Sets: (All)
Aliases:
Accepted values: DHtml, Html, Text, Csv, Xml

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportClassificationLog
指定文件分类基础设施在分类过程中可以生成的日志类型数组。该参数的可接受值为：

- None
- ClassificationsInLogFile
- ErrorsInLogFile
- ClassificationsInSystemLog
- ErrorsInSystemLog

```yaml
Type: FsrmReportClassificationLogEnum[]
Parameter Sets: (All)
Aliases:
Accepted values: ClassificationsInLogFile, ErrorsInLogFile, ClassificationsInSystemLog, ErrorsInSystemLog

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportClassificationMailTo
指定一个由分号分隔的电子邮件地址列表。在预定的分类任务完成后，服务器会将分类结果发送到这些电子邮件地址中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportFileGroupIncluded
指定一个文件组名称数组，这些文件组需要包含在报告中。每个字符串都必须是一个有效的文件组名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportFileOwnerFilePattern
指定一个文件模式字符串，用于指示哪些文件应包含在按所有者分类的文件报告中。您可以在该字符串中使用通配符字符 * 和 ?。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportFileOwnerUser
指定一个用户数组（采用 Domain/User 格式），该数组中的用户将包含在“按文件所有者显示的文件列表”报告中。默认值为空列表，表示包含所有用户。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportFileScreenAuditDaysSince
指定自审计事件发生以来需要包含在报告中的最短天数。

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

### -ReportFileScreenAuditEnable
表示已启用了文件屏幕审计功能。

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

### -ReportFileScreenAuditUser
指定一个用户电子邮件地址数组，用于包含审计事件的相关信息。默认值是一个空列表，表示包含所有用户。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportLargeFileMinimum
指定要包含在大型文件报告中的最小文件大小。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportLargeFilePattern
指定要包含在大文件报告中的一组文件字符串。您可以在该字符串中使用通配符字符 * 和 ?。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportLeastAccessedFilePattern
指定一组文件，这些文件将被包含在“访问频率最低的报告”中。您可以在文件名字符串中使用通配符字符 * 和 ?。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportLeastAccessedMinimum
指定报告上次被访问以来的最短时间（以天为单位），该时间将被计入访问频率最低的报告列表中。

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

### -ReportLimitMaxDuplicateGroup
指定在重复文件报告中包含的重复文件组的最大数量。

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

### -ReportLimitMaxFile
指定存储报告中可包含的最大文件数量。

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

### -ReportLimitMaxFileGroup
指定文件组报告中可包含的最大文件组数量。

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

### -ReportLimitMaxFileScreenEvent
指定文件屏幕审计报告中应包含的最大文件屏幕事件数量。

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

### -ReportLimitMaxFilesPerDuplicateGroup
指定单个重复文件组中应包含在重复文件报告中的最大文件数量。

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

### -ReportLimitMaxFilesPerFileGroup
指定任何文件组中可包含在文件组报告中的最大文件数量。

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

### -ReportLimitMaxFilesPerOwner
指定任何所有者在按所有者分类的文件报告中可以包含的最大文件数量。

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

### -ReportLimitMaxFilesPerPropertyValue
指定每个属性值在“按属性分组的文件报告”中可包含的最大文件数量。

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

### -ReportLimitMaxOwner
指定文件按所有者分类的报告中可以包含的最大所有者数量。

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

### -ReportLimitMaxPropertyValue
指定在按属性分类的文件报告中可包含的属性值的最大数量。

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

### -ReportLimitMaxQuota
指定在配额使用报告中应包含的最大配额数量。

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

### -ReportLocationIncident
指定一个文件夹的路径，服务器将事件报告存储在该文件夹中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportLocationOnDemand
指定一个文件夹的路径，服务器会在此文件夹中按需存储报告文件。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportLocationScheduled
指定一个文件夹的路径，服务器会将计划生成的报告存储在该文件夹中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportMostAccessedFilePattern
指定一个文件字符串，这些文件将包含在访问频率最高的报告中。您可以在该字符串中使用通配符字符 * 和 ?。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportMostAccessedMaximum
指定自报告上次被访问以来的最大天数，这些天数将被计入“最常被访问的报告”中。

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

### -ReportNotificationLimit
指定报告通知中各个运行事件之间的最小时间间隔（以分钟为单位）。如果多次报告通知同时发生，服务器只有在距离上次执行该操作至少过去了指定的时间后，才会再次触发相应的报告通知。

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

### -ReportPropertyFilePattern
指定要在按属性生成的文件报告中包含的一组文件名称。您可以在这些文件名中使用通配符字符 * 和 ?。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportPropertyName
指定要通过属性报告来显示的文件对应的属性名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportQuotaMinimumUsage
指定要包含在配额使用报告中的最低配额使用水平。

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

### -SmtpServer
指定 FSRM 用于发送电子邮件的 SMTP 服务器的完全限定域名（FQDN）或 IP 地址。

你可以使用 **Send-FsrmTestEmail** cmdlet 来发送电子邮件，以测试你指定的 SMTP 服务器。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最优限制值。该限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#Root/Microsoft/Windows/FSRM/MSFT_FSRMSettings

## 备注

## 相关链接

[Get-FsrmSetting](./Get-FsrmSetting.md)

