---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FSRMAutoQuota.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/new-fsrmautoquota?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-FsrmAutoQuota
---

# New-FsrmAutoQuota

## 摘要
创建一个自动应用的配额设置。

## 语法

```
New-FsrmAutoQuota [-Path] <String> [-Template <String>] [-Disabled] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**New-FsrmAutoQuota** cmdlet 用于创建自动应用的配额。通过使用自动应用配额功能，您可以将一个配额模板分配给父卷或文件夹。文件服务器资源管理器（FSRM）会根据该模板自动生成相应的配额。系统会为现有的所有子文件夹以及将来创建的子文件夹生成配额。

你可以使用 **Get-FsrmAutoQuota** cmdlet 来验证所有自动生成的配额。`Get-FsrmAutoQuota` 会为每个子文件夹返回相应的配额信息，以及父卷或文件夹中自动应用的配额配置文件。

## 示例

### 示例 1：为文件夹创建自动应用配额的功能
```
PS C:\> New-FsrmAutoQuota -Path "C:\Shares\CtrShare03" -Template "250 MB Extended Limit"
```

此命令会在名为 C:\Shares\CtrShare03 的文件夹上创建一个自动应用的配额设置。服务器会根据“250 MB 扩展限制”模板，为 C:\Shares\CtrShare03 中的每个现有子文件夹以及您在该文件夹中新建的子文件夹生成相应的配额。

### 示例 2：创建一个处于非活动状态的自动配额应用机制
```
PS C:\> New-FsrmAutoQuota -Path "C:\Shares\CtrShare03" -Template "100 MB Limit" -Disabled
```

此命令会在文件夹 C:\Shares\CtrShare03 上创建一个自动应用的配额，并将该配额设置为“100 MB 的限制”。同时，该命令会禁用自动应用配额的功能，这意味着服务器将不再为 C:\Shares\CtrShare03 中的子文件夹生成配额。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -Disabled
表示服务器不会跟踪与该配额相关的配额数据，也不会执行任何与配额阈值相关联的操作。

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

### -Path
指定一个有效的本地文件夹路径。服务器会将该自动配额应用到该文件夹中的所有子文件夹（无论是现有的还是未来的子文件夹）。

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
用于指定服务器上某个配额模板（quota template）的名称。

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
指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，不适用于会话或整个计算机。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.Management.Automation.SwitchParameter

## 输出

### System.Object

## 备注

## 相关链接

[Get-FsrmAutoQuota](./Get-FsrmAutoQuota.md)

[Remove-FsrmAutoQuota](./Remove-FsrmAutoQuota.md)

[Set-FsrmAutoQuota](./Set-FsrmAutoQuota.md)

[更新-FsrmAutoQuota](./Update-FsrmAutoQuota.md)

