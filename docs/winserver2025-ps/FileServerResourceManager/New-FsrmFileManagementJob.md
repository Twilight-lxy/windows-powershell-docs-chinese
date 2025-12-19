---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FSRMFileManagementJob.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/new-fsrmfilemanagementjob?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-FsrmFileManagementJob
---

# 新的Fsrm文件管理作业

## 摘要
创建一个文件管理任务。

## 语法

```
New-FsrmFileManagementJob [-Name] <String> [-Description <String>] -Namespace <String[]> [-Disabled]
 [-Condition <CimInstance[]>] -Action <CimInstance> [-ReportFormat <FmjReportFormatsEnum[]>]
 [-ReportLog <FmjReportLogsEnum[]>] [-MailTo <String>] [-Notification <CimInstance[]>] -Schedule <CimInstance>
 [-Continuous] [-ContinuousLog] [-ContinuousLogSize <UInt64>] [-Parameters <String[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-FsrmFileManagementJob` cmdlet 在服务器上创建一个文件管理任务。该任务会指定执行时间表、条件、当文件满足所有条件时应运行的命令或操作、用户通知方式以及报告生成规则。

要使用此cmdlet创建一个文件管理任务，您必须传递一个**FsrmScheduledTask**对象、一个**FsrmFmjAction**对象以及一个**FsrmFmjNotification**对象。

## 示例

### 示例 1：创建一个文件管理任务，用于定期删除过期的数据
```
The first command gets a **DateTime** object and stores it in the variable $date.
PS C:\> $date = Get-Date "12:00am"

This second command returns a **FsrmScheduledTask** object that runs the task at midnight on the first day of the month. The command stores results in the $task variable.
PS C:\> $task = New-FsrmScheduledTask -Time $date -Monthly 1

The third command returns an action object for a management job and stores the results in the $action variable. The command specifies an expiration action and specifies a path that the action uses to expire files.
PS C:\> $action = New-FsrmFmjAction -Type Expiration -ExpirationFolder "C:\Expire"

The fourth command creates a file management job named "Expire all data" for the folder C:\Share01. The command specifies the schedule stored in the $task variable and specifies the action stored in the $action variable.
PS C:\> New-FsrmFileManagementJob -Name "Expire all data" -Namespace @("C:\Share01") -Schedule $task -Action $action
```

这个示例创建了一个文件管理任务，用于删除命名空间中的所有数据。

### 示例 2：创建一个文件管理任务，用于持续删除过期的数据
```
The first command gets a **DateTime** object and stores it in the variable $date.
PS C:\> $date = Get-Date "12:00am"

This second command returns a **FsrmScheduledTask** object that runs the task at midnight on the first day of the month. The command stores results in the $task variable.
PS C:\> $task = New-FsrmScheduledTask -Time $date -Monthly 1

The third command returns an action object for a management job and stores the results in the $action variable. The command specifies an expiration action and specifies a path that the action uses to expire files.
PS C:\> $action = New-FsrmFmjAction -Type Expiration -ExpirationFolder "C:\Expire"

The fourth command creates a file management job named "Expire all data" for the folder C:\Share01. The command specifies the schedule stored in the $task variable, specifies the action stored in the $action variable, and specifies that the server continuously apply classification to files in the background.
PS C:\> New-FsrmFileManagementJob -Name "Expire all data" -Namespace @("C:\Share01") -Schedule $task -Action $action -Continuous
```

这个示例创建了一个文件管理任务：当服务器运行该文件管理任务时，或者当某个文件被修改或重新分类时，该任务会删除相应命名空间中的数据。

### 示例 3：创建一个文件管理任务，并在该任务执行时发送通知
```
The first command gets a **DateTime** object and stores it in the variable $date.
PS C:\> $date = Get-Date "12:00am"

This second command returns a **FsrmScheduledTask** object that runs the task at midnight on the first day of the month. The command stores results in the $task variable.
PS C:\> $task = New-FsrmScheduledTask -Time $date -Monthly 1

The third command returns an action object for a management job and stores the results in the $action variable. The command specifies an expiration action and specifies a path that the action uses to expire files.
PS C:\> $action = New-FsrmFmjAction -Type Expiration -ExpirationFolder "C:\Expire"

The fourth command returns a notification action object that sends the specified email message to the administrator and file owner. The command specifies that the action can attach a maximum of 1000 files to the message. The command stores the results in the $notificationaction variable.
PS C:\> $notificationaction = New-FsrmFmjNotificationAction -Type Email -MailTo "[Admin Email];[File Owner]" -Subject "Warning: Files will expire soon" -Body "The attached list of files will expire in 30 days." -AttachmentFileListSize 1000

The fifth command returns a notification object for a file management job that runs the notification action stored in the $notificationaction variable 30 days before the file management job acts. The command stores the results in the $notification variable.
PS C:\> $notification = New-FsrmFmjNotification -Days 30 -Action $notificationaction

The sixth command creates a file management job named "Expire all data" for the folder C:\Share01. The command specifies the schedule stored in the $task variable, specifies the action stored in the $action variable, and specifies the notification stored in the $notification variable.
PS C:\> New-FsrmFileManagementJob -Name "Expire all data" -Namespace @("C:\Share01") -Schedule $task -Action $action -Notification $notification
```

这个示例创建了一个文件管理任务，该任务会在指定的命名空间中删除过期的数据，并在服务器执行文件管理任务之前的30天向文件所有者和管理员发送电子邮件通知。

### 示例 4：创建一个基于条件的文件管理任务
```
The first command gets a **DateTime** object and stores it in the variable $date.
PS C:\> $date = Get-Date "12:00am"

This second command returns an **FsrmScheduledTask** object that runs the task at midnight on the first day of the month. The command stores results in the $task variable.
PS C:\> $task = New-FsrmScheduledTask -Time $date -Monthly 1

The third command returns an action object for a management job and stores the results in the $action variable. The command specifies an expiration action and specifies a path that the action uses to expire files.
PS C:\> $action = New-FsrmFmjAction -Type Expiration -ExpirationFolder "C:\Expire"

The fourth command returns a condition object for file management job that verifies that a file has a PII classification property set to true. The command stores the results in the $condition variable.
PS C:\> $condition = New-FsrmFmjCondition -Property "PII" -Condition Equal -Value "1"

The fifth command creates a file management job named "Expire all data" for the folder C:\Share01. The command specifies the schedule stored in the $task variable, specifies the action stored in the $action variable, and specifies the condition stored in the $condition variable.
PS C:\> New-FsrmFileManagementJob -Name "Expire all data" -Namespace @("C:\Share01") -Schedule $task -Action $action -Condition $condition
```

这个示例创建了一个文件管理任务，该任务会删除所有将个人身份信息（PII）属性设置为“true”的文件。

## 参数

### -Action
用于指定一个 **FsrmFmjAction** 对象。您可以使用 **New-FsrmFmjAction** cmdlet 来创建一个 **FsrmFmjAction** 对象。

```yaml
Type: CimInstance
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该 cmdlet。输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -Condition
用于指定一个 **FsrmFmjCondition** 对象。你可以使用 **New-FsrmFmjCondition** cmdlet 来创建一个 **FsrmFmjCondition** 对象。

```yaml
Type: CimInstance[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前会提示您进行确认。

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

### -Continuous
表示服务器在后台持续对文件进行分类处理。

如果您指定了这个参数，那么就无法指定任何通知内容；同时，您指定的条件中也不能包含那些分类属性（classification property）被设置为以下值的对象：  
- File.DateCreated  
- File.DateLastModified  
- File.DateLastAccessed

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

### -ContinuousLog
表示服务器会记录连续的分类活动。要记录分类活动，必须指定“Continuous”参数。

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

### -ContinuousLogSize
指定包含连续分类活动的日志的最大大小。要记录分类活动，必须设置“Continuous”参数。

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

### -Description
为文件管理任务指定一个描述信息。

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

### -Disabled
表示文件管理任务已被禁用。

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

### -MailTo
指定一个由分号分隔的电子邮件地址列表，文件服务器会将邮件发送到这些地址。

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

### -Name
指定文件管理任务的名称。

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
指定一个命名空间数组，这些命名空间属于当前的作用域范围。每个值必须是服务器上定义的 `FolderType` 属性的一个值（格式为 “\[文件夹类型属性名称=\<值\>\”)，或者是一个静态路径。

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

### -Notification
用于指定一个 **FsrmFmjNotificationAction** 对象。您可以使用 **New-FsrmFmjNotificationAction** cmdlet 来创建一个 **FsrmFmjNotificationAction** 对象。

```yaml
Type: CimInstance[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Parameters
指定一个字符串数组，其格式为 `<名称>`=`<值>`。文件分类基础设施（File Classification Infrastructure）和其他管理工具会使用这些参数。

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

### -ReportFormat
指定文件管理任务生成的报表格式数组。该参数的可接受值为：

- DHTML
- HTML
- XML
- CSV
- Text

```yaml
Type: FmjReportFormatsEnum[]
Parameter Sets: (All)
Aliases:
Accepted values: DHtml, Html, Text, Csv, XML

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReportLog
指定文件管理作业生成的报表类型数组。该参数的可接受值包括：

- Information
- Error
- Audit

```yaml
Type: FmjReportLogsEnum[]
Parameter Sets: (All)
Aliases:
Accepted values: Error, Information, Audit

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Schedule
Specifies a File Server Resource Manager (FSRM) scheduled task object that describes the schedule for performing the continuous classification.
Use the **New-FsrmScheduledTask** cmdlet to create a scheduled task object.
Any duration information in the FSRM scheduled task object is ignored.

```yaml
Type: CimInstance
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
Specifies the maximum number of concurrent operations that can be established to run the cmdlet.
If this parameter is omitted or a value of `0` is entered, then Windows PowerShell® calculates an optimum throttle limit for the cmdlet based on the number of CIM cmdlets that are running on the computer.
The throttle limit applies only to the current cmdlet, not to the session or to the computer.

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
Shows what would happen if the cmdlet runs.
The cmdlet is not run.

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
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### System.String

### System.String[]

### System.Management.Automation.SwitchParameter

### Microsoft.ManagementInfrastructure.CimInstance[]

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.PowerShell Cmdletization GeneratedTypes.FmjReportFormatsEnum[]

### Microsoft.PowShell Cmdletization GeneratedTypes.FmjReportLogsEnum[]

### System.UInt64

## 输出

### System.Object

## 备注

## 相关链接

[Get-FsrmFileManagementJob](./Get-FsrmFileManagementJob.md)

[New-FsrmFmjAction](./New-FsrmFmjAction.md)

[New-FsrmFmjCondition](./New-FsrmFmjCondition.md)

[New-FsrmFMJNotification](./New-FsrmFMJNotification.md)

[New-FsrmFmjNotificationAction](./New-FsrmFmjNotificationAction.md)

[New-FsrmScheduledTask](./New-FsrmScheduledTask.md)

[Remove-FsrmFileManagementJob](./Remove-FsrmFileManagementJob.md)

[Set-FsrmFileManagementJob](./Set-FsrmFileManagementJob.md)

[开始-FsrmFileManagementJob作业](./Start-FsrmFileManagementJob.md)

[Stop-FsrmFileManagementJob](./Stop-FsrmFileManagementJob.md)

[Wait-FsrmFileManagementJob](./Wait-FsrmFileManagementJob.md)

