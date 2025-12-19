---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmFileScreenTemplate.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/set-fsrmfilescreentemplate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-FsrmFileScreenTemplate
---

# Set-FsrmFileScreenTemplate

## 摘要
更改文件屏幕模板的配置设置。

## 语法

### 查询（cdxml）（默认设置）
```
Set-FsrmFileScreenTemplate [-Name] <String[]> [-Description <String>] [-IncludeGroup <String[]>] [-Active]
 [-UpdateDerived] [-UpdateDerivedMatching] [-Notification <CimInstance[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-FsrmFileScreenTemplate -InputObject <CimInstance[]> [-Description <String>] [-IncludeGroup <String[]>]
 [-Active] [-UpdateDerived] [-UpdateDerivedMatching] [-Notification <CimInstance[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-FsrmFileScreenTemplate` cmdlet 用于修改文件屏幕模板的配置设置。

当你对某个文件屏幕模板进行修改时，可以选择将这些修改应用到使用该原始模板创建的所有现有文件屏幕上。你可以指定 `UpdateDerivedMatching` 参数，仅修改那些仍然与原始模板匹配的文件屏幕；或者指定 `UpdateDerived` 参数，修改所有使用原始模板创建的文件屏幕（无论你对这些文件屏幕做了哪些修改）。

## 示例

### 示例 1：更改文件屏幕模板的包含组
```
PS C:\> Set-FsrmFileScreenTemplate -Name "Filter Media files" -IncludeGroup @("Media Files", "Text Files")
```

这个命令将一个名为“Filter Media files”的文件屏幕模板更改为同时包含媒体文件和文本文件。

#### 示例 2：更改文件屏幕模板及其派生文件的包含组
```
PS C:\> Set-FsrmFileScreenTemplate "1GB limit" -IncludeGroup @("Media Files", "Text Files") -UpdateDerived
```

此命令用于更新一个名为“1GB限制”的文件屏幕模板，使其同时支持媒体文件和文本文件的显示。服务器还会将这些设置应用到所有基于该模板创建的文件屏幕中。

## 参数

### -Active
表示服务器在执行任何违反文件屏蔽规则的输入/输出（I/O）操作时会失败。如果您不指定此参数，服务器在执行违反文件屏蔽规则的I/O操作时不会失败，并且仍会继续执行与该文件屏蔽规则相关的所有操作。

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

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业的结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
在运行 cmdlet 之前，会提示您确认是否要继续。

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

### -InputObject
指定要传递给此cmdlet的输入数据。你可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

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

### -Name
指定文件屏幕模板的名称。

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

### -Notification
指定一个通知操作对象数组。您可以使用 **New-FsrmFmjNotificationAction** cmdlet 来创建一个 **FsrmFmjNotificationAction** 对象。

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

### -ThrottleLimit
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值为`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最优限制值。此限制仅适用于当前执行的cmdlet，而不适用于整个会话或整个计算机。

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

### -UpdateDerived
表示服务器会修改所有使用原始文件屏幕模板创建的现有文件屏幕。如果您指定了此参数，则无法指定*UpdateDerivedMatching*参数。

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

### -UpdateDerivedMatching
表示服务器仅更新自您使用原始文件屏幕模板创建以来未被修改过的文件屏幕。如果您指定了此参数，则无法指定*UpdateDerived*参数。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被运行。

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

### System.String[]

### Microsoft.ManagementInfrastructure.CimInstance[]

### System.Management Automation.SwitchParameter

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#Root/Microsoft/Windows/FSRM/MSFT_FsrmFileScreenTemplate

## 备注

## 相关链接

[Get-FsrmFileScreenTemplate](./Get-FsrmFileScreenTemplate.md)

[New-FsrmFileScreenTemplate](./New-FsrmFileScreenTemplate.md)

[New-FsrmFmjNotificationAction](./New-FsrmFmjNotificationAction.md)

[Remove-FsrmFileScreenTemplate](./Remove-FsrmFileScreenTemplate.md)

