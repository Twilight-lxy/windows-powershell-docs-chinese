---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmStorageReport.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/set-fsrmstoragereport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-FsrmStorageReport
---

# Set-FsrmStorageReport

## 摘要
更改存储报告的设置。

## 语法

### 查询（cdxml）（默认值）
```
Set-FsrmStorageReport [-Name] <String[]> [-Namespace <String[]>] [-ReportType <StorageReportReportTypeEnum[]>]
 [-FileScreenAuditDaysSince <UInt32>] [-FileScreenAuditUser <String[]>] [-FileGroupIncluded <String[]>]
 [-FileOwnerUser <String[]>] [-FileOwnerFilePattern <String>] [-PropertyName <String>]
 [-FolderPropertyName <String>] [-PropertyFilePattern <String>] [-LargeFileMinimum <UInt64>]
 [-LargeFilePattern <String>] [-LeastAccessedMinimum <UInt32>] [-LeastAccessedFilePattern <String>]
 [-MostAccessedMaximum <UInt32>] [-MostAccessedFilePattern <String>] [-QuotaMinimumUsage <UInt32>]
 [-ReportFormat <StorageReportReportFormatsEnum[]>] [-MailTo <String>] [-Schedule <CimInstance>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-FsrmStorageReport -InputObject <CimInstance[]> [-Namespace <String[]>]
 [-ReportType <StorageReportReportTypeEnum[]>] [-FileScreenAuditDaysSince <UInt32>]
 [-FileScreenAuditUser <String[]>] [-FileGroupIncluded <String[]>] [-FileOwnerUser <String[]>]
 [-FileOwnerFilePattern <String>] [-PropertyName <String>] [-FolderPropertyName <String>]
 [-PropertyFilePattern <String>] [-LargeFileMinimum <UInt64>] [-LargeFilePattern <String>]
 [-LeastAccessedMinimum <UInt32>] [-LeastAccessedFilePattern <String>] [-MostAccessedMaximum <UInt32>]
 [-MostAccessedFilePattern <String>] [-QuotaMinimumUsage <UInt32>]
 [-ReportFormat <StorageReportReportFormatsEnum[]>] [-MailTo <String>] [-Schedule <CimInstance>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-FsrmStorageReport` cmdlet 用于更改服务器上存储报告的设置。您无法修改交互式存储报告或未设置定时任务的存储报告的设置。必须指定 `Name` 参数以及至少一个其他参数。

## 示例

### 示例 1：更改存储报告的类型
```
PS C:\> Set-FsrmStorageReport -Name "Get storage usage info" -ReportTypes @(LargeFiles, DuplicateFiles)
```

这条命令将名为“获取存储使用信息”的报告更改为生成一个关于大文件（LargeFiles）和重复文件的报告（DuplicateFiles）。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -FileGroupIncluded
指定一个文件组名称数组，这些文件组将包含在报告中。每个字符串都必须是一个有效的文件组名称。

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

### -FileOwnerFilePattern
指定一个文件字符串，这些文件将包含在按所有者分类的报告中。您可以在该字符串中使用通配符字符 * 和 ?。如果指定了此参数，则必须为 *ReportType* 参数设置 FilesByOwner。

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

### -FileOwnerUser
指定一个用户数组（格式为 Domain/User），用于确定哪些用户的文件应包含在“按文件所有者分类的报告”中。默认值为空列表，表示所有用户的文件都会被纳入报告。

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

### -FileScreenAuditDaysSince
指定自审计事件发生以来的最小天数，这些天内的数据将被包含在报告中。如果您指定了此参数，则必须为*ReportType*参数设置FileScreenAuditFiles。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FileScreenAuditUser
用于指定要包含审计事件的用户电子邮件地址数组。默认值为空列表，表示所有用户。如果您指定了此参数，则必须为 *ReportType* 参数设置 FileScreenAuditFiles。

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

### -FolderPropertyName
该参数用于指定要通过属性报告来显示的文件夹分类属性名称。您需要在 **FsrmClassificationPropertyDefinition** 对象中设置 `Name` 属性的值。如果您指定了此参数，则必须为 `ReportType` 参数设置 `FoldersByProperty`。

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
指定传递给此 cmdlet 的输入数据。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该 cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -LargeFileMinimum
指定要包含在大型文件报告中的最小文件大小。如果您指定了此参数，则必须为*ReportType*参数设置LargeFiles。

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

### -LargeFilePattern
指定要包含在大型文件报告中的一组文件。您可以在字符串中使用通配符字符“\*”和“?”。如果指定了此参数，则必须为“*ReportType*”参数设置“LargeFiles”值。

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

### -LeastAccessedFilePattern
指定要包含在“访问频率最低的报告”中的文件字符串。您可以在该字符串中使用通配符字符 * 和 ?。如果您指定了此参数，则必须为 *ReportType* 参数设置 “LeastRecentlyAccessed” 的值。

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

### -LeastAccessedMinimum
该参数用于指定自报告上次被访问以来的最短时间（以天为单位），只有在这段时间内被访问的报告才会被纳入“访问频率最低的报告”列表中。如果您指定了此参数，那么必须同时为*ReportType*参数设置相应的值（即LeastRecentlyAccessed）。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MailTo
用于指定电子邮件收件人的电子邮件地址列表，这些地址之间用分号分隔。\[Admin Email\] 是一个有效的电子邮件地址。

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

### -MostAccessedFilePattern
指定一组文件，这些文件将被包含在访问频率最高的报告中。您可以在字符串中使用通配符字符“\*”和“?”。如果您指定了此参数，则必须为“*ReportType*”参数设置“MostRecentlyAccessed”值。

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

### -MostAccessedMaximum
指定自报告上次被访问以来的最大天数，这些天内的报告将被纳入“最常被访问的报告”列表中。如果您指定了此参数，则必须为 *ReportType* 参数设置 “MostRecentlyAccessed” 的值。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
用于指定存储报告的名称数组。如果您没有为某个存储报告指定名称，服务器会自动生成一个标准名称。如果您指定了“交互式”（*Interactive*）参数，则必须同时指定此参数。

```yaml
Type: String[]
Parameter Sets: Query (cdxml)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Namespace
指定一组属于报告作用域的命名空间。每个字符串必须是服务器上 `FolderType` 属性的一个值、字符串 “All Shares”，或者是一个静态路径。`FolderType` 属性必须采用以下格式：`\[文件夹类型属性名称=\<值\>\)`。

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

### -PropertyFilePattern
指定要包含在按属性生成的报表文件中的文件字符串。可以在该字符串中使用通配符字符“\*”和“?”。如果指定了此参数，则必须为*ReportType*参数设置FilesByProperty。

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

### -PropertyName
该参数用于指定要通过属性报告来显示的文件分类属性的名称。您需要在**FsrmClassificationPropertyDefinition**对象中设置“Name”属性的值。如果您指定了此参数，则必须为*ReportType*参数设置“FilesByProperty”。

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

### -QuotaMinimumUsage
指定要包含在配额使用报告中的最低配额使用水平。如果您指定了此参数，则必须为*ReportType*参数设置QuotaUsage。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportFormat
指定分类报告生成的报表格式数组。该参数的可接受值包括：

- DHTML
- HTML
- XML
- CSV
- Text

```yaml
Type: StorageReportReportFormatsEnum[]
Parameter Sets: (All)
Aliases:
Accepted values: DHtml, Html, Text, Csv, XML

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportType
指定该操作生成的报表类型。仅当您将*Type*参数设置为“Report”时，才需要指定此参数。该参数的可接受值包括：

- DuplicateFiles
- FilesByFileGroup
- FilesByOwner
- FilesByProperty
- LargeFiles
- LeastRecentlyAccessed
- MostRecentlyAccessed
- QuotaUsage

```yaml
Type: StorageReportReportTypeEnum[]
Parameter Sets: (All)
Aliases:
Accepted values: LargeFiles, FilesByFileGroup, LeastRecentlyAccessed, MostRecentlyAccessed, QuotaUsage, FilesByOwner, DuplicateFiles, FileScreenAuditFiles, FilesByProperty, FoldersByProperty

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Schedule
指定一个文件服务器资源管理器（FSRM）的计划任务对象，该对象用于描述存储报告运行的时间安排。可以使用 **New-FsrmScheduledTask** cmdlet 来创建计划任务对象。

```yaml
Type: CimInstance
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行的命令行脚本（cmdlet）的最大操作数量。如果省略此参数或输入值为`0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM （Common Information Model）命令行脚本的数量来计算一个最优的并发限制。这个并发限制仅适用于当前正在执行的命令行脚本，而不影响整个会话或计算机本身的性能。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.ManagementInfrastructure.CimInstance[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#Root/Microsoft/Windows/FSRM/MSFT_FSRMStorageReport

## 备注

## 相关链接

[Get-FsrmStorageReport](./Get-FsrmStorageReport.md)

[New-FsrmStorageReport](./New-FsrmStorageReport.md)

[Remove-FsrmStorageReport](./Remove-FsrmStorageReport.md)

[Start-FsrmStorageReport](./Start-FsrmStorageReport.md)

[Stop-FsrmStorageReport](./Stop-FsrmStorageReport.md)

[Wait-FsrmStorageReport](./Wait-FsrmStorageReport.md)

