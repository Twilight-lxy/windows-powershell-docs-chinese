---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmFileScreenTemplate.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/new-fsrmfilescreentemplate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-FsrmFileScreenTemplate
---

# New-FsrmFileScreenTemplate

## 摘要
创建一个文件屏幕模板。

## 语法

```
New-FsrmFileScreenTemplate [-Name] <String> [-Description <String>] [-IncludeGroup <String[]>] [-Active]
 [-Notification <CimInstance[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`New-FsrmFileScreenTemplate` cmdlet 用于创建文件筛选模板。文件筛选模板定义了需要阻止的文件组、要执行的筛选类型（主动式或被动式），以及该文件筛选模板生成的各类通知内容。

你可以使用文件屏幕模板来集中管理所有的文件屏幕，只需更新模板即可，而无需逐一修改每个文件屏幕。当你对某个模板进行修改时，可以选择将这些更改应用到所有基于该模板的文件屏幕上，或者仅应用到那些属性与该模板相匹配的文件屏幕上。

## 示例

### 示例 1：创建一个被动文件扫描模板
```
PS C:\> New-FsrmFileScreenTemplate "Filter Non-HTML text files" -IncludeGroup "Non-HTML text files"
```

此命令创建了一个名为“过滤非HTML文本文件”的被动文件筛选模板，该模板会记录所有属于“非HTML文本文件”文件组的文件。这个文件筛选模板是被动的（passive），因为命令中没有指定“Active”参数。这意味着用户可以创建非HTML格式的文本文件。

### 示例 2：创建一个活跃的文件屏幕模板
```
PS C:\> $Notification = New-FsrmAction -Type Email -MailTo "[Admin Email];[File Owner]" -Subject "Warning: attempted to create a non-HTML text file" -Body "You attempted to create a non-HTML text file. This is not allowed." -RunLimitInterval 120
PS C:\> New-FsrmFileScreenTemplate -Name "Filter Non-HTML text files" -IncludeGroup "Non-HTML text files" -Notification $Notification -Active
```

第一个命令创建了一个文件服务器资源管理器（File Server Resource Manager，简称FSRM）操作对象，并将结果存储在$Notification变量中。该操作会向文件的所有者和管理员发送电子邮件通知。*RunLimitInterval*参数指定了一个间隔时间，即服务器在再次发送电子邮件通知之前需要等待2分钟。

这第二条命令创建了一个名为“过滤非HTML文本文件”的活动文件筛选模板，该模板会限制所有属于“非HTML文本文件”类别的文件。当用户尝试创建一个非HTML文本文件时，文件筛选机制会执行存储在$Notification变量中的通知操作。

## 参数

### -Active
这表示服务器会拒绝执行任何违反文件安全策略的输入/输出（I/O）操作。如果您不指定此参数，服务器不会拒绝这些违规操作，而是会继续执行与文件安全策略相关的所有操作。

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

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。您可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
在运行该 cmdlet 之前，会提示您进行确认。

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

### -Description
为文件屏幕模板指定一个描述。

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

### -IncludeGroup
指定一个文件组名称数组，这些文件组需要从文件筛选过程中排除出去。

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

### -Name
指定文件屏幕模板的名称。

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

### -Notification
指定一个通知操作对象的数组。您可以使用 `New-New-FsrmFmjNotificationAction` cmdlet 来创建一个 **FsrmFmjNotificationAction** 对象。

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

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### Microsoft.ManagementInfrastructure.CimInstance[]

## 输出

### System.Object

## 备注

## 相关链接

[Get-FsrmFileScreenTemplate](./Get-FsrmFileScreenTemplate.md)

[New-FsrmAction](./New-FsrmAction.md)

[Remove-FsrmFileScreenTemplate](./Remove-FsrmFileScreenTemplate.md)

[Set-FsrmFileScreenTemplate](./Set-FsrmFileScreenTemplate.md)

