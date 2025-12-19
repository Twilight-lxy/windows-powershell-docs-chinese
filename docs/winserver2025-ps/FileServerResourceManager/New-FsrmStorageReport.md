---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmStorageReport.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/new-fsrmstoragereport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-FsrmStorageReport
---

# 新Fsm存储报告

## 摘要
在服务器上创建一份存储报告。

## 语法

```
New-FsrmStorageReport [-Name] <String> -Namespace <String[]> [-Interactive]
 -ReportType <StorageReportReportTypeEnum[]> [-FileScreenAuditDaysSince <UInt32>]
 [-FileScreenAuditUser <String[]>] [-FileGroupIncluded <String[]>] [-FileOwnerUser <String[]>]
 [-FileOwnerFilePattern <String>] [-PropertyName <String>] [-FolderPropertyName <String>]
 [-PropertyFilePattern <String>] [-LargeFileMinimum <UInt64>] [-LargeFilePattern <String>]
 [-LeastAccessedMinimum <UInt32>] [-LeastAccessedFilePattern <String>] [-MostAccessedMaximum <UInt32>]
 [-MostAccessedFilePattern <String>] [-QuotaMinimumUsage <UInt32>]
 [-ReportFormat <StorageReportReportFormatsEnum[]>] [-MailTo <String>] [-Schedule <CimInstance>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-FsrmStorageReport` cmdlet 可用于在服务器上生成存储报告。存储报告任务会指定一组目录，服务器会对这些目录进行分析，以生成一种或多种类型的报告，帮助您更好地了解指定目录中存储资源的使用情况。您可以配置报告任务使其按照计划运行，也可以根据需要手动触发其执行。

## 示例

### 示例 1：生成一份大型文件存储报告
```powershell
# The first command gets a **DateTime** object and stores it in the $d variable.
PS C:\> $d = Get-Date "12:00am"

# This second command returns a **FsrmScheduledTask** object that describes a schedule that runs the task at midnight on the first day
# of the month. The command stores results in the $task variable.
PS C:\> $task = New-FsrmScheduledTask -Time $d -Monthly 1

# The third command creates a LargeFiles storage report named "Find large files" on C:\Shares.
# The command sets the schedule for the report stored in the $task variable, and limits the
# report to files larger than 10MB.
PS C:\> New-FsrmStorageReport -Name "Find large files" -Namespace @("C:\Shares") -Schedule $task -ReportType @("LargeFiles") -LargeFileMinimum 10MB
```

这个示例生成了一份“LargeFiles存储报告”，服务器每月会运行一次该报告，并且报告仅涵盖大小超过10MB的文件。

### 示例 2：使用命名空间条件生成大型文件存储报告
```powershell
# The first command gets a **DateTime** object and stores it in the $d variable.
PS C:\> $d = get-date "12:00am"

# This second command returns an **FsrmScheduledTask** object that describes a schedule
# that runs the task at midnight on the first day of the month. The command stores results in
# the $task variable.
PS C:\> $task = new-FsrmScheduledTask -Time $d -Monthly 1

# The third command creates a LargeFiles storage report named "Find large files" that generates a
# Large Files report on any folders whose Folder Usage property includes the User Data value.
# The command sets the schedule for the report stored in the $task variable.
PS C:\> New-FsrmStorageReport -Name "Find large files" -Namespace @("[FolderUsage=User Data]") -Schedule $task -ReportType @("LargeFiles")
```

这个示例创建了一个名为“LargeFiles”的存储报告，服务器会每月运行一次该报告，并统计那些其“Folder Usage”属性中包含“User Data”值的文件夹。此外，该报告仅针对大小超过10MB的文件进行统计。

### 示例 3：为文件组中的文件生成存储报告
```powershell
# The first command gets a **DateTime** object and stores it in the $d variable.
PS C:\> $d = get-date "12:00am"

# This second command returns a **FsrmScheduledTask** object that describes a schedule that
# runs the task at midnight on the first day of the month. The command stores results in
# the $task variable.
PS C:\> $task = new-FsrmScheduledTask -Time $d -Monthly 1

# The third command creates a storage report named "Find large files" and file groups on th
# folder C:\Shares. The command sets the schedule for the report stored in the $task variable,
# set the report type to LargeFiles and a FilesByFileGroup, limits the report to files larger
# than 10MB, and restricts the FilesByFileGroup report to include only files from the
# "Text files file" group.
PS C:\> New-FsrmStorageReport -Name "Find large files and file groups" -Namespace @("C:\Shares") -Schedule $task -ReportType @("LargeFiles", "FilesByFileGroup") -LargeFileMinimum 10MB -FileGroupIncluded "Text files"
```

这个示例创建了一份存储报告，服务器每月会运行该报告，并生成一份“LargeFiles”报告和一份“FilesByFileGroup”报告。

### 示例 4：创建一份交互式的存储报告
```powershell
PS C:\> New-FsrmStorageReport -Name "Find large files" -Namespace @("C:\Shares") -Interactive -ReportType @("LargeFiles")
```

此命令会创建一个名为“Find large files”的存储报告，服务器会立即执行该报告。该命令为文件夹 C:\Shares 生成一个 LargeFile 存储报告，并将这份报告保存到 **C:\StorageReports\Interactive** 文件夹中。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
在运行该cmdlet之前，会提示您确认是否要继续执行操作。

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
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -FileOwnerFilePattern
指定一组文件，这些文件将包含在按文件所有者分类的报告中。您可以在字符串中使用通配符字符“\*”和“?”。如果您指定了此参数，则必须为“*ReportType*”参数设置“FilesByOwner”。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -FileOwnerUser
指定一个用户数组（采用 Domain/User 格式），这些用户的文件将包含在“按所有者分类的文件报告”中。默认值为空列表，表示所有用户都会被包含在内。

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

### -FileScreenAuditDaysSince
指定自审计事件发生之日起至少需要过去多少天才能将该事件包含在报告中。如果您指定了此参数，则必须为*ReportType*参数设置FileScreenAuditFiles。

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

### -FileScreenAuditUser
用于指定要包含审计事件的用户电子邮件地址数组。默认值是一个空列表，表示所有用户。如果您指定了此参数，则必须为 *ReportType* 参数设置 FileScreenAuditFiles。

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

### -FolderPropertyName
指定要通过属性报告来显示的文件夹的分类属性名称。该名称应在 **FsrmClassificationPropertyDefinition** 对象中设置。如果您指定了此参数，则必须为 *ReportType* 参数设置 FoldersByProperty。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Interactive
表示该报告是交互式的。当您指定此参数时，报告不需要任何调度安排；报告无法被修改；在运行该cmdlet时会立即生成报告；并且服务器会在报告执行完成后自动将其从系统中删除。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LargeFileMinimum
指定要包含在大文件报告中的最小文件大小。如果指定了此参数，则必须为*ReportType*参数设置LargeFiles属性。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LargeFilePattern
指定要包含在大型文件报告中的一组文件。您可以在字符串中使用通配符字符“\*”和“?”。如果您指定了此参数，则必须为“*ReportType*”参数设置“LargeFiles”。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LeastAccessedFilePattern
指定要包含在“最少被访问报告”中的文件列表。您可以在该字符串中使用通配符字符“\*”和“?”。如果您指定了此参数，则必须为“*ReportType*”参数设置“LeastRecentlyAccessed”的值。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LeastAccessedMinimum
指定自报告上次被访问以来的最短天数，该天数将计入“访问频率最低的报告”中。如果您指定了此参数，则必须为*ReportType*参数设置LeastRecentlyAccessed属性。

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

### -MailTo
用于指定电子邮件接收者的电子邮件地址列表，这些地址之间用分号分隔。\[Admin Email\] 是一个有效的电子邮件地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MostAccessedFilePattern
指定一组文件，这些文件将被包含在访问频率最高的报告中。您可以在字符串中使用通配符“\*”和“?”。如果您指定了此参数，则必须为“*ReportType*”参数设置“MostRecentlyAccessed”值。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MostAccessedMaximum
指定报告上次被访问以来的最大天数范围，该范围内的报告将被纳入“最常被访问的报告”列表中。如果您指定了此参数，则必须为*ReportType*参数设置MostRecentlyAccessed属性。

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

### -Name
指定存储报告的名称。如果您不指定名称，服务器会生成一个默认名称。如果您指定了“交互式”（Interactive）参数，则必须同时指定此参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Namespace
指定一组属于报告作用域的命名空间（namespace）。每个字符串必须是服务器上 `FolderType` 属性的值、字符串 “All Shares”，或者是一个静态路径。`FolderType` 属性的格式应为 `\[文件夹类型属性名称=\<值\>\`。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PropertyFilePattern
指定一组文件字符串，这些文件将包含在按属性生成的报告中。您可以在字符串中使用通配符字符 “\*” 和 “?”。如果您指定了此参数，则必须为 “*ReportType*” 参数设置 “FilesByProperty”。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PropertyName
该参数用于指定要通过属性报告来显示的文件分类属性的名称。请在 **FsrmClassificationPropertyDefinition** 对象中设置 “Name” 属性的值。如果指定了此参数，则必须为 “ReportType” 参数设置 “FilesByProperty”。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -QuotaMinimumUsage
指定要包含在配额使用报告中的最低配额使用水平。如果您指定了此参数，则必须为 *ReportType* 参数设置 QuotaUsage。

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

### -ReportFormat
指定分类报告生成的报表格式数组。该参数的可接受值为：

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
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReportType
指定该操作生成的报表类型。仅当您将*Type*参数设置为“Report”时，才需要指定此参数。该参数的可接受值为：

- DuplicateFiles
- FilesByFileGroup
- FilesByOwner
- FilesByProperty
-	FileScreenAuditFiles
- FoldersByProperty
- LargeFiles
- LeastRecentlyAccessed
- MostRecentlyAccessed
- QuotaUsage

```yaml
Type: StorageReportReportTypeEnum[]
Parameter Sets: (All)
Aliases:
Accepted values: LargeFiles, FilesByFileGroup, LeastRecentlyAccessed, MostRecentlyAccessed, QuotaUsage, FilesByOwner, DuplicateFiles, FileScreenAuditFiles, FilesByProperty, FoldersByProperty

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Schedule
指定一个文件服务器资源管理器（FSRM）的计划任务对象，该对象描述了存储报告运行的时间安排。可以使用 **New-FsrmScheduledTask** cmdlet 来创建计划任务对象。

```yaml
Type: CimInstance
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时建立的、用于执行该cmdlet的操作的最大数量。如果省略此参数或输入值`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值（即并发操作的数量）。此限制仅适用于当前正在执行的cmdlet，而不适用于整个会话或整个计算机。

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
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

### System.String

### System.String[]

### System.Management Automation.SwitchParameter

### Microsoft.PowerShell CmdletIZATION.GeneratedTypes.StorageReportReportTypeEnum[]

### System.UInt32

### System.UInt64

### Microsoft.PowerShell CmdletIZATIONGeneratedTypes.StorageReportReportFormats Enum[]

### Microsoft.ManagementInfrastructure.CimInstance

## 输出

### System.Object
## 备注

## 相关链接

[Get-FsrmStorageReport](./Get-FsrmStorageReport.md)

[New-FsrmScheduledTask](./New-FsrmScheduledTask.md)

[New-FsrmStorageReport](./New-FsrmStorageReport.md)

[Remove-FsrmStorageReport](./Remove-FsrmStorageReport.md)

[Set-FsrmStorageReport](./Set-FsrmStorageReport.md)

[Start-FsrmStorageReport](./Start-FsrmStorageReport.md)

[Stop-FsrmStorageReport](./Stop-FsrmStorageReport.md)

[Wait-FsrmStorageReport](./Wait-FsrmStorageReport.md)

