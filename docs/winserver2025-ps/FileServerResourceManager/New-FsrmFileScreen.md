---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmFileScreen.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/new-fsrmfilescreen?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-FsrmFileScreen
---

# New-FsrmFileScreen

## 摘要
创建一个文件屏幕（用于展示文件内容）。

## 语法

```
New-FsrmFileScreen [-Path] <String> [-Description <String>] [-IncludeGroup <String[]>] [-Active]
 [-Template <String>] [-Notification <CimInstance[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-FsrmFileScreen` cmdlet 用于为服务器上的某个路径创建一个文件筛选规则。该文件筛选规则会阻止用户将多个文件同时保存到指定的文件夹中。

如果您指定了“Active”参数，文件屏蔽功能会阻止用户保存属于被阻止文件组的文件，并在用户尝试保存这些文件时生成通知。该功能不会阻止用户或应用程序访问在创建文件屏蔽功能之前已保存到该路径的文件，无论这些文件是否属于被阻止的文件组。

## 示例

### 示例 1：创建一个被动文件扫描程序
```powershell
PS C:\> New-FsrmFileScreen -Path "C:\Shares" -Description "Filter Non-HTML text files" -IncludeGroup "Non-HTML text files" -Active:$false
```

此命令在 C:\Shares 目录上创建了一个被动文件筛选规则，用于记录所有属于“非 HTML 文本文件”文件组的文件。该文件筛选规则的模板被设置为“被动模式”，因为命令中指定了 `-Active:$false` 参数。这意味着用户可以正常创建非 HTML 格式的文本文件。

### 示例 2：创建一个活动文件屏幕
```powershell
PS C:\> $Notification = New-FsrmAction -Type Email -MailTo "[Admin Email];[File Owner]" -Subject "Warning: attempted to create a non-HTML text file" -Body "You attempted to create a non-HTML text file. This is not allowed." -RunLimitInterval 120
PS C:\> New-FsrmFileScreen -Path "C:\Shares\Ctrshare03" -IncludeGroup "Non-HTML text files" -Notification $Notification -Active
```

第一个命令创建了一个文件服务器资源管理器（File Server Resource Manager，简称FSRM）操作对象，并将结果存储在$Notification变量中。该操作会向文件的所有者和管理员发送电子邮件通知。**RunLimitInterval**参数指定了一个间隔时间，即2分钟；在这段时间内，服务器无法再次发送电子邮件通知。

这第二条命令会在 `C:\Shares\Ctrshare03` 上创建一个文件筛选规则，该规则会限制所有属于“非HTML文本文件”文件组的文件。当用户尝试创建一个非HTML文本文件时，文件筛选规则会执行存储在 `$Notification` 变量中的通知操作。

### 示例 3：根据文件屏幕模板创建一个新的文件屏幕
```powershell
PS C:\> New-FsrmFileScreen -Path "C:\shares\ctrshare03" -Template "Block Image Files"
```

该命令根据“阻止图像文件”模板中的设置，在 `C:\shares\ctrshare03` 上创建一个文件屏幕。

## 参数

### -Active
表示服务器会拒绝执行任何违反文件系统安全规则的输入/输出（I/O）操作。该功能默认是启用的。

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
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Description
为文件屏幕指定一个描述。

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
指定一个文件组名称数组。这些文件组包含了服务器用于识别被该规则阻止的文件的文件名模式。

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
指定一个通知操作对象的数组。你可以使用 **New-FsrmFmjNotificationAction** cmdlet 来创建一个 **FsrmFmjNotificationAction** 对象。

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

### -Path
指定一个有效的本地文件夹路径。

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

### -Template
在服务器上指定一个文件屏幕模板。

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
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在运行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### Microsoft.ManagementInfrastructure.CimInstance[]

## 输出

### System.Object

## 备注

## 相关链接

[Get-FsrmFileGroup](./Get-FsrmFileGroup.md)

[Get-FsrmFileScreen](./Get-FsrmFileScreen.md)

[New-FsrmFmjNotificationAction](./New-FsrmFmjNotificationAction.md)

[Remove-FsrmFileScreen](./Remove-FsrmFileScreen.md)

[Reset-FsrmFileScreen](./Reset-FsrmFileScreen.md)

[Set-FsrmFileScreen](./Set-FsrmFileScreen.md)

