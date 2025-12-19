---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FSRMFmjNotification.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/new-fsrmfmjnotification?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-FsrmFMJNotification
---

# New-FsrmFMJNotification

## 摘要
返回一个用于文件管理任务的通知对象。

## 语法

```
New-FsrmFMJNotification [-Days] <UInt32> [-Action <CimInstance[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-FsrmFMJNotification` cmdlet 返回一个通知对象，您可以使用该对象来创建文件管理作业操作。您可以将 `FsrmFMJNotification` 对象作为输入参数传递给 `New-FsrmFileManagementJob` cmdlet 和 `Set-FsrmFileManagementJob` cmdlet。

`FsrmFmjAction` 对象定义了一个通知周期，在该周期之后文件管理任务才会对文件执行相应的操作。此 cmdlet 支持以下操作：

- Email
- Event
- Command

## 示例

### Example 1: Create a notification for file management jobs
```
PS C:\> $action = New-FsrmFmjNotificationAction -Type Email -MailTo "[Admin Email];[File Owner]" -Subject "Warning: Files will expire soon" -Body "The attached list of files will expire in 30 days." -AttachmentFileListSize 1000
PS C:\> New-FsrmFmjNotification -Days 30 -Action $action
```

第一个命令返回一个对象，该对象表示一个通知动作。这个通知动作会将指定的电子邮件消息发送给管理员和文件所有者，并规定该动作最多可以在邮件中附加1000个文件。该命令将通知动作对象存储在 `$action` 变量中。

第二个命令会返回一个通知对象，该对象用于文件管理作业；这个文件管理作业会在其实际执行前的30天内运行存储在 `$action` 变量中的通知动作。

## 参数

### -Action
指定一个文件管理作业操作的数组。你可以使用 **New-FsrmFmjAction** cmdlet 来创建一个作业操作。

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

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业 (About Jobs)](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -Days
指定文件管理任务在对该文件执行操作之前多少天会触发通知动作。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值（即并发操作的最大数量）。这个限制仅适用于当前正在执行的 cmdlet，而不涉及整个会话或整个计算机。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32

### Microsoft.ManagementInfrastructure.CimInstance[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接

[New-FsrmFileManagementJob](./New-FsrmFileManagementJob.md)

[New-FsrmFmjAction](./New-FsrmFmjAction.md)

[New-FsrmFmjNotificationAction](./New-FsrmFmjNotificationAction.md)

[Set-FsrmFileManagementJob](./Set-FsrmFileManagementJob.md)

