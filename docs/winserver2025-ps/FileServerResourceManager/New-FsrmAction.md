---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmAction.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/new-fsrmaction?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-FsrmAction
---

# New-FsrmAction

## 摘要
返回一个FSRM（文件系统资源管理器）操作对象。

## 语法

```
New-FsrmAction [-Type] <ActionTypeEnum> [-MailTo <String>] [-MailCC <String>] [-MailBCC <String>]
 [-Subject <String>] [-Body <String>] [-EventType <ActionEventTypeEnum>] [-Command <String>]
 [-WorkingDirectory <String>] [-CommandParameters <String>] [-SecurityLevel <ActionSecurityLevelEnum>]
 [-KillTimeOut <Int32>] [-ShouldLogError] [-ReportTypes <ActionReportTypeEnum[]>] [-RunLimitInterval <Int32>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-FsrmAction` cmdlet 返回一个文件服务器资源管理器（File Server Resource Manager, FSRM）操作对象。`FsrmAction` 对象本身不包含该操作的触发条件（即启动该操作的特定事件或条件）。你可以将这个操作对象传递给其他使用通知功能或配额阈值的 cmdlets。

`FsrmAction` 对象封装了一个单一的操作，例如发送电子邮件。FSRM 仅会在该操作对象被用作其他对象的一部分时才会保存它。例如，你可以使用 `FsrmAction` 对象来创建通知和配额阈值。保存下来的对象将作为触发该操作的依据。

`New-FsrmAction` cmdlet 支持以下操作：

- Email: Send email to the user or administrator that the event triggered
- Event: Create an event log entry
- Command: Run a command that the administrator specifies
- Report: Run one or more storage reports

## 示例

### 示例 1：创建一个用于发送电子邮件的操作
```
PS C:\> New-FsrmAction Email -MailCC "john.smith@contosco.com" -MailTo "sarah.jones@contosco.com" -Subject "Warning: Approaching storage limit" -Body "You are about to reach the end of your available storage."
```

这个命令返回一个对象，该对象表示当关联事件发生时，服务器会发送一封电子邮件。电子邮件的收件人是用户sarah.jones@contosco.com，而电子邮件的抄送收件人是管理员john.smith@contosco.com。

### 示例 2：创建一个具有运行次数限制的操作
```
PS C:\> New-FsrmAction Email -MailTo "john.smith@contosco.com;sarah.jones@contosco.com" -Subject "Warning: Approaching storage limit" -Body "You are about to reach the end of your available storage." -RunLimitInterval 120
```

该命令返回一个对象，表示当相关事件发生时，服务器会向管理员和文件所有者发送电子邮件。该命令规定：该事件每120分钟内最多只能触发一次。如果事件确实发生了，在时间间隔结束之前，所执行的操作将不会产生任何效果。

### 示例 3：创建一个用于记录事件的动作
```
PS C:\> New-FsrmAction Event -EventType Information -Body "The user [File Owner] is about to reach the end of his available storage." -RunLimitInterval 180
```

该命令返回一个对象，表明当相关事件发生时，服务器会记录包含指定消息的事件日志。该事件每180分钟内最多只能触发一次；如果事件确实触发了，在时间间隔结束之前不会创建额外的事件日志条目。

### 示例 4：创建一个动作，用于运行命令并记录错误
```
PS C:\> New-FsrmAction Command -Command "c:\windows\system32\cmd.exe"-CommandParameters "echo [source file path] >> c:\log.txt" -ShouldLogError
```

该命令返回一个对象，该对象表明当相关事件发生时，服务器会使用指定的参数运行Cmd.exe程序。此外，该命令还要求服务器将命令执行过程中产生的错误代码记录到错误日志中。

### 示例 5：创建一个用于运行存储报告的操作
```
PS C:\> New-FsrmAction Report -ReportType @(LargeFiles, DuplicateFiles)
```

该命令返回一个对象，该对象表明服务器会运行LargeFiles和DuplicateFiles脚本，并在相关事件发生时生成相应的报告。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

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

### -Body
用于指定电子邮件的内容。如果您指定了此参数，则必须为“类型”（Type）参数设置“电子邮件”（Email）或“事件指定”（Event Specify）。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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

### -Command
指定程序或脚本的完整路径。如果指定了此参数，则必须为“类型”（Type）参数设置相应的命令（Command）。

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

### -CommandParameters
用于指定程序或脚本的参数。如果您指定了该参数，则必须为“类型”（Type）参数设置相应的命令（Command）。

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

### -EventType
指定该操作的事件类型。如果您指定了此参数，则必须为*Type*参数设置“Event”值。该参数的可接受值为：

- None
- Information
- Warning
- Error

```yaml
Type: ActionEventTypeEnum
Parameter Sets: (All)
Aliases:
Accepted values: None, Information, Warning, Error

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -KillTimeOut
Specifies the timeout period, in minutes, after which the process that the action created is ended.
Specify the default, -1, to indicate that the server does not end the process.
If you specify this parameter, you must set Command for the *Type* parameter.

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MailBCC
Specifies a semicolon-separated list of email addresses for the Bcc recipients of an email.
Valid email addresses are an administrator email account or the owner of the file.
If you specify this parameter, you must set Email for the *Type* parameter.

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

### -MailCC
Specifies a semicolon-separated list of email addresses for the Cc recipients of an email.
Valid email addresses are an administrator email account or the owner of the file.
If you specify this parameter, you must set Email for the *Type* parameter.

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

### -MailTo
Specifies a semicolon-separated list of email addresses for the recipients of an email.
Valid email addresses are an administrator email account or the owner of the file.
If you specify this parameter, you must set Email for the *Type* parameter.

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

### -ReportTypes
Specifies an array of report types that the action generates.
If you specify this parameter, you must set Report for the *Type* parameter.
The acceptable values for this parameter are:

- DuplicateFiles
- FilesByFileGroup
- FilesByOwner
- FilesByProperty
- LargeFiles
- LeastRecentlyAccessed
- MostRecentlyAccessed
- QuotaUsage

```yaml
Type: ActionReportTypeEnum[]
Parameter Sets: (All)
Aliases:
Accepted values: LargeFiles, FilesByFileGroup, LeastRecentlyAccessed, MostRecentlyAccessed, QuotaUsage, FilesByOwner, DuplicateFiles, FileScreenAuditFiles, FilesByProperty

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RunLimitInterval
Specifies the minimum interval, in minutes, before the server can run the action again.
For example, if the interval expired since the action last ran, the server runs the action again in response to an event; otherwise, the server cannot run the action again.
The default value, 60, specifies that there is no limit.

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SecurityLevel
Specifies the computer account type under which the program or script runs.
The acceptable values for this parameter are:

- LocalService
- NetworkService
- LocalSystem

```yaml
Type: ActionSecurityLevelEnum
Parameter Sets: (All)
Aliases:
Accepted values: None, NetworkService, LocalService, LocalSystem

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ShouldLogError
Indicates that the server records errors codes from running commands in the event log.

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

### -Subject
Specifies the subject of an email.
The maximum size of a subject is 1 KB.
If you specify this parameter, you must set Email for the *Type* parameter.

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

### -Type
Specifies the type of the action.
This setting determines the action that the server takes in response to a quota or file screen event.
The acceptable values for this parameter are:

- Email
- Event
- Command
- Report

```yaml
Type: ActionTypeEnum
Parameter Sets: (All)
Aliases:
Accepted values: Event, Email, Command, Report

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
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

### -WorkingDirectory
Specifies the working directory in which the program or script runs.
You must specify a valid path to a folder.
FSRM does not support paths to remote computers.

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

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### Microsoft.PowerShell.Cmdletization.GeneratedTypes.ActionTypeEnum

### System.String

### Microsoft.PowerShell.Cmdletization.GeneratedTypes.ActionEventTypeEnum

### Microsoft.PowerShell.Cmdletization.GeneratedTypes.ActionSecurityLevelEnum

### System.Int32

### System.Management.Automation.SwitchParameter

### Microsoft.PowerShell.Cmdletization.GeneratedTypes.ActionReportTypeEnum[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接

[New-FsrmQuotaThreshold](./New-FsrmQuotaThreshold.md)

[New-FsrmFileScreen](./New-FsrmFileScreen.md)

[New-FsrmStorageReport](./New-FsrmStorageReport.md)

[New-FsrmScheduledTask](./New-FsrmScheduledTask.md)

[New-FsrmFileManagementJob](./New-FsrmFileManagementJob.md)

[New-FsrmFMJNotification](./New-FsrmFMJNotification.md)

