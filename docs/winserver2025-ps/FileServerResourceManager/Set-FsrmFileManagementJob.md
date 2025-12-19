---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FSRMFileManagementJob.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/set-fsrmfilemanagementjob?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-FsrmFileManagementJob
---

# Set-FsrmFileManagementJob

## 摘要
更改文件管理作业的配置设置。

## 语法

### 查询（CDXML）（默认值）
```
Set-FsrmFileManagementJob [-Name] <String[]> [-Description <String>] [-Namespace <String[]>] [-Disabled]
 [-Condition <CimInstance[]>] [-Action <CimInstance>] [-ReportFormat <FmjReportFormatsEnum[]>]
 [-ReportLog <FmjReportLogsEnum[]>] [-MailTo <String>] [-Notification <CimInstance[]>]
 [-Schedule <CimInstance>] [-Continuous] [-ContinuousLog] [-ContinuousLogSize <UInt64>]
 [-Parameters <String[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-FsrmFileManagementJob -InputObject <CimInstance[]> [-Description <String>] [-Namespace <String[]>]
 [-Disabled] [-Condition <CimInstance[]>] [-Action <CimInstance>] [-ReportFormat <FmjReportFormatsEnum[]>]
 [-ReportLog <FmjReportLogsEnum[]>] [-MailTo <String>] [-Notification <CimInstance[]>]
 [-Schedule <CimInstance>] [-Continuous] [-ContinuousLog] [-ContinuousLogSize <UInt64>]
 [-Parameters <String[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-FsrmFileManagementJob` cmdlet 用于更改文件管理作业的配置设置。除了 `Name` 参数外，您还必须指定至少一个其他参数。

## 示例

### 示例 1：修改文件管理任务的条件
```
The first command returns a condition object for file management job that verifies that a file has a PII classification property set to true. The command stores the results in the $condition variable.
PS C:\> $condition = New-FsrmFmjCondition -Property "PII" -Condition Equal -Value "1"

The second command gets the file management job named "Expire stale data" and stores the results in the $current variable.
PS C:\> $current = Get-FsrmFileManagementJob -Name "Expire stale data"

The third command adds the new condition to the existing conditions of the file management job.
PS C:\> $newConditions = $current.Conditions + $condition

The fourth command sets the condition of the file management job named "Expire stale data" to the condition stored in the $newConditions variable.
PS C:\> Set-FsrmFileManagementJob "Expire stale data" -Condition $newConditions
```

这个示例修改了名为“Expire stale data”的文件管理任务，使其在原有的条件基础上，只包含那些将 PII（个人身份信息）属性设置为 “true” 的文件。

## 参数

### -Action
指定一个 **FsrmFmjAction** 对象。您可以使用 **New-FsrmFmjAction** cmdlet 来创建一个 **FsrmFmjAction** 对象。

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

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个 **FsrmFmjCondition** 对象。你可以使用 **New-FsrmFmjCondition** cmdlet 来创建一个 **FsrmFmjCondition** 对象。

```yaml
Type: CimInstance[]
Parameter Sets: (All)
Aliases:

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

### -Continuous
表示服务器在后台持续对文件进行分类处理。

如果您指定了此参数，则无法指定任何通知内容；同时，您指定的条件中也不能包含那些分类属性被设置为以下值的对象：

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
Accept pipeline input: False
Accept wildcard characters: False
```

### -ContinuousLog
这表示服务器会记录连续的分类活动日志。要记录分类活动，必须指定“Continuous”参数。

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

### -ContinuousLogSize
指定包含连续分类活动的日志的最大大小。要记录分类活动，必须指定“Continuous”参数。

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

### -Description
为文件管理任务指定一个描述信息。

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

### -Disabled
表示文件管理任务已禁用。

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

### -InputObject
指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传送到该 cmdlet。

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

### -MailTo
指定一个由分号分隔的电子邮件地址列表，文件服务器会将邮件发送到这些地址。

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

### -Name
为文件管理任务指定一个名称。

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
指定一个命名空间数组，这些命名空间属于当前作用域的范围。每个值必须是服务器上定义的 `FolderType` 属性的值（格式为 „\[文件夹类型属性名称=\<值\>\“），或者是某个静态路径。

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

### -Notification
指定一个 **FsrmFmjNotificationAction** 对象。您可以使用 **New-FsrmFmjNotificationAction** cmdlet 来创建一个 **FsrmFmjNotificationAction** 对象。

```yaml
Type: CimInstance[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Parameters
使用 `<name>\>=<value>` 的格式指定一个字符串数组。文件分类基础设施（File Classification Infrastructure）和其他管理工具会使用这些参数。

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
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -ReportFormat
指定文件管理任务生成的报告格式数组。该参数的可接受值包括：

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
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportLog
指定文件管理任务生成的报表类型数组。该参数的可接受值为：

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
Accept pipeline input: False
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

Required: False
Position: Named
Default value: None
Accept pipeline input: False
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

### System.String[]

### Microsoft.ManagementInfrastructure.CimInstance[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#Root/Microsoft/Windows/FSRM/MSFT_FSRMFileManagementJob

## 备注

## 相关链接

[Get-FsrmFileManagementJob](./Get-FsrmFileManagementJob.md)

[New-FsrmFileManagementJob](./New-FsrmFileManagementJob.md)

[New-FsrmFmjCondition](./New-FsrmFmjCondition.md)

[New-FsrmFmjNotificationAction](./New-FsrmFmjNotificationAction.md)

[New-FsrmScheduledTask](./New-FsrmScheduledTask.md)

[Remove-FsrmFileManagementJob](./Remove-FsrmFileManagementJob.md)

[开始-FsrmFileManagementJob作业](./Start-FsrmFileManagementJob.md)

[Stop-FsrmFileManagementJob](./Stop-FsrmFileManagementJob.md)

[Wait-FsrmFileManagementJob](./Wait-FsrmFileManagementJob.md)

