---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmScheduledTask.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/new-fsrmscheduledtask?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-FsrmScheduledTask
---

# New-FsrmScheduledTask

## 摘要
创建一个计划任务对象。

## 语法

```
New-FsrmScheduledTask [-Time] <DateTime> [-RunDuration <Int32>] [-Weekly <FsrmScheduledTaskDaysEnum[]>]
 [-Monthly <Int32[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`New-FsrmScheduledTask` cmdlet 用于创建一个计划任务对象，该对象用于定义报告生成、文件分类及文件管理操作的调度规则。

## 示例

### 示例 1：创建一个每周定时执行的任务
```
PS C:\> $d = get-date "12:00am"
PS C:\> New-FsrmScheduledTask -Time $d -Weekly @(Monday, Tuesday, Wednesday, Thursday, Friday)
```

第一个命令获取一个 `DateTime` 对象，并将其存储在变量 `$d` 中。

第二个命令返回一个 **FsrmScheduledTask** 对象，该对象定义了一个调度方案：任务每天从周一到周五的午夜自动运行。

### 示例 2：创建一个每月定期执行的任务
```
PS C:\> $d = get-date "12:00am"
PS C:\> New-FsrmScheduledTask -Time $d -Monthly @(-1,15) -RunDuration 4
```

第一个命令获取一个 `DateTime` 对象，并将其存储在变量 `$d` 中。

这第二条命令返回一个 **FsrmScheduledTask** 对象，该对象描述了一个调度任务：该任务会在每个月的15日以及每月的最后一天午夜执行。*RunDuration* 参数指定，如果任务在4小时后仍未完成，服务器将终止该进程。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Monthly
指定一个用于运行任务的日期数组。如果输入值為 -1，则表示任务将在该月的最后一天执行。如果您指定了此参数，请不要同时指定 “*Weekly*”（每周）参数。

```yaml
Type: Int32[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RunDuration
指定服务器在取消任务之前运行该任务的小时数。值 0 表示服务器会将该任务运行完毕。

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

### -ThrottleLimit
指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -Time
指定一个日期和时间值（采用标准的协调世界时（UTC）格式），以便运行该任务。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Weekly
指定一个包含工作日的数组，以便在这些工作日运行任务。如果指定了此参数，请不要同时指定“Monthly”参数。

```yaml
Type: FsrmScheduledTaskDaysEnum[]
Parameter Sets: (All)
Aliases:
Accepted values: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

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

### SystemDateTime

### System.Int32

### Microsoft.PowerShell CmdletizationGeneratedTypes.FsrmScheduledTaskDaysEnum[]

### System.Int32[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接

[New-FsrmFileManagementJob](./New-FsrmFileManagementJob.md)

[New-FsrmStorageReport](./New-FsrmStorageReport.md)

[Set-FsrmClassification](./Set-FsrmClassification.md)

[Set-FsrmFileManagementJob](./Set-FsrmFileManagementJob.md)

[Set-FsrmStorageReport](./Set-FsrmStorageReport.md)

